"""QP-HULL-1 Leg 0, part 1: the small-grid credential of the hull instrument (benchmarks/foundations/qp_hull.py),
written 2026-10-20 by the executor; no number at q = 1.492 beyond the first ramp waypoint is produced (the
charter's v7 forbids the question's numbers before the lock; the waypoint-1 pin at 0.0018792 is the ramp's first
rung, an instrument-convergence quantity, and is reported here as such).

Runs, each a level-1 recovery followed by the sub-pin ladder to waypoint 1 (fractions 0.15, 0.3, 0.55, 0.8, 1 of
0.0018792, the Q-SWEEP protocol), writing analysis/qp_hull_leg0.json:
  A. resolution sweep at q = 1.492: (NT1, NT2) in the list below at NP = 12; the quantities om2, gamma, the
     level-1 theta and the per-point closure, to read the density at which om2 converges to 1e-4 relative.
  B. hull vs cell at a HIGH-order rational, q = 13/9 (the partner of the level-2 mode sits at (13, -8), far
     outside the amplitudes here, so no locking): hull (NT1, NT2, NP) against the registered cell instrument
     QTGrid(9 NT1, NP, 9, 13) through the same ladder; the restricted hull state against the cell state in the
     cell's metrics (max |dtheta|, |dpt|, |dT|, |dom2|), and the cell-equation residual of the restricted state.
  C. hull vs cell at q = 3/2 (the LOW-order rational): the same comparison; this one is NOT a credential bar
     (at rational q the cell locks the degenerate modes (0, 1) and (3, -1), which the hull keeps separate; the
     difference is Q2's content) and is recorded to show the effect's size at this density.
Usage: python benchmarks/foundations/qp_hull_leg0.py [--quick]   (--quick: the smallest grids only, a smoke)
"""
import json
import os
import pathlib
import sys
import time

import numpy as np

os.environ.setdefault('SJ_MEMO', '0')
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations import qp_hull as QH                   # noqa: E402
from benchmarks.foundations import qsweep_stage1 as Q1             # noqa: E402
from benchmarks.foundations import sparsej_instrument as SJ        # noqa: E402

OUT = ROOT / 'analysis' / 'qp_hull_leg0.json'
FRACS = (0.15, 0.3, 0.55, 0.8, 1.0)


def ladder_hull(H, log):
    x = QH.solve(H, H.level1_seed(), 'a2', 0.0, rounds=12, verbose=False)
    l1 = dict(rms=float(H.field_rms(x)), theta=float(H.unpack(x)[0].mean()), theta_ptp=float(np.ptp(H.unpack(x)[0])),
              om1=float(H.unpack(x)[3]))
    A2w = Q1.WAYPOINTS[0]
    xs = H.ramp_seed(x, FRACS[0] * A2w)
    rungs = []
    for f in FRACS:
        t0 = time.time()
        xs = QH.solve(H, xs, 'a2', f * A2w, rounds=40, stop_rms=1e-9 if f < 1 else None, verbose=False)
        m = QH.metrics(H, xs); m['pin'] = f * A2w; m['seconds'] = time.time() - t0
        rungs.append(m)
        log(f'    hull {H.NT1}x{H.NT2}x{H.NP} q {H.q:.4f} pin {f * A2w:.6f}: rms {m["rms"]:.1e} A2 {m["A2"]:.6f} '
            f'om2 {m["om2"]:.6f} gam {m["gam"]:.7f} clos {m["clos"]:.1e} ({m["seconds"]:.0f}s)')
    return x, xs, l1, rungs


def ladder_cell(T, log):
    sj, _ = SJ.make_instrument(T, Q1.level1_seed(T), 'a2', 0.0, 50.0)
    bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    x = SJ.gn_sparse(T, Q1.level1_seed(T), 'a2', 0.0, sj, bs, rounds=30)
    l1 = dict(rms=float(T.field_rms(x)), theta=float(T.unpack(x)[0].mean()), theta_ptp=float(np.ptp(T.unpack(x)[0])),
              om1=float(T.unpack(x)[3]))
    A2w = Q1.WAYPOINTS[0]
    xs = Q1.ramp_seed(T, FRACS[0] * A2w)
    sj, _ = SJ.make_instrument(T, xs, 'a2', FRACS[0] * A2w, 50.0)
    rungs = []
    for f in FRACS:
        t0 = time.time()
        xs = SJ.gn_sparse(T, xs, 'a2', f * A2w, sj, bs, rounds=40, stop_rms=1e-9 if f < 1 else None)
        m = Q1.metrics(T, xs); m['pin'] = f * A2w; m['seconds'] = time.time() - t0
        rungs.append(m)
        log(f'    cell {T.NS}x{T.NP} q {T.G2.N2}/{T.G2.N1} pin {f * A2w:.6f}: rms {m["rms"]:.1e} A2 {m["A2"]:.6f} '
            f'om2 {m["om2"]:.6f} gam {m["gam"]:.7f} clos {m["clos"]:.1e} ({m["seconds"]:.0f}s)')
    return x, xs, l1, rungs


def compare(H, xh, T, xc):
    xr = H.restrict_state(xh, T)
    thh, pth, Th, o1h, o2h = T.unpack(xr); thc, ptc, Tc, o1c, o2c = T.unpack(xc)
    return dict(dtheta=float(np.abs(thh - thc).max()), dpt=float(np.abs(np.angle(np.exp(1j * (pth - ptc)))).max()),
                dT=float(np.abs(Th - Tc).max()), dom2=float(abs(o2h - o2c)), dom1=float(abs(o1h - o1c)),
                cell_rms_of_restricted=float(T.field_rms(xr)))


def main(quick=False):
    rec = dict(date='2026-10-20', A=[], B=[], C=[])
    log = lambda s: print(s, flush=True)

    def save():
        OUT.write_text(json.dumps(rec, indent=1, default=str) + '\n')
    NP = 8 if quick else 12
    grids_A = [(12, 8), (24, 8)] if quick else [(12, 8), (12, 12), (12, 16), (24, 8), (24, 12), (36, 8), (48, 8), (48, 12)]
    log('== A. resolution sweep at q = 1.492')
    for nt1, nt2 in grids_A:
        H = QH.HGrid(nt1, nt2, NP, QH.Q_PHYS)
        t0 = time.time()
        x1, xw, l1, rungs = ladder_hull(H, log)
        rec['A'].append(dict(grid=[nt1, nt2, NP], level1=l1, rungs=rungs, seconds=time.time() - t0)); save()
    for tag, (n1, n2), grids in (('B', (9, 13), [(12, 8)] if quick else [(12, 8), (24, 8), (24, 12)]),
                                 ('C', (2, 3), [(12, 8)] if quick else [(12, 8), (24, 8), (48, 8)])):
        log(f'== {tag}. hull vs cell at q = {n2}/{n1}')
        for nt1, nt2 in grids:
            H = QH.HGrid(nt1, nt2, NP, n2 / n1)
            T = Q1.QTGrid(nt1 * n1, NP, n1, n2)
            t0 = time.time()
            xh1, xhw, l1h, rh = ladder_hull(H, log)
            xc1, xcw, l1c, rc = ladder_cell(T, log)
            cmp_l1 = compare(H, xh1, T, xc1); cmp_w = compare(H, xhw, T, xcw)
            log(f'    level-1: theta hull {l1h["theta"]:.8f} cell {l1c["theta"]:.8f}; waypoint-1 restricted vs cell: {cmp_w}')
            rec[tag].append(dict(grid=[nt1, nt2, NP], cell=[nt1 * n1, NP, n1, n2], hull_level1=l1h, cell_level1=l1c,
                                 hull_rungs=rh, cell_rungs=rc, compare_level1=cmp_l1, compare_waypoint1=cmp_w,
                                 hull_null_modes=H.null, seconds=time.time() - t0)); save()
    log(f'written {OUT}')


if __name__ == '__main__':
    main(quick='--quick' in sys.argv)
