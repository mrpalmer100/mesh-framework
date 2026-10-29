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
  D. (--part2 CKPT) the credential proper at the registered density: the hull at NP 36 (24 x 8, and 48 x 12 as its
     own refinement) marched to the two 13/9 waypoint pins against the RETAINED 13/9 members of COMPOSITE-SELECT Leg
     B (432 x 36, from the full sealed checkpoint on the machine of record): om1, om2, gamma, the restricted state
     in the cell's metrics, the cell-equation residual of the restricted state, and FND-135's price on both.
Usage: python benchmarks/foundations/qp_hull_leg0.py [--quick] [--part2 CKPT [--resume]]
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


def price_hull(H, x):
    """FND-135's closed form on the hull (the torus average in place of the cell mean): (1 + ke) / gamma."""
    ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = H.geom(x)
    ke = 0.5 * np.mean(np.abs(1j * om1 * w + om2 * (w @ H.DP1.T)) ** 2 + (om2 * (ze @ H.DP1.T)) ** 2)
    return float((1.0 + ke) / gam), float(ke)


def load_members(ckpt):
    """The retained 13/9 members: from the sealed Leg B checkpoint (a .pkl on the machine of record) or from the
    repository extract analysis/qp_hull_13_9_members.npz written by tools/qp_hull_members_extract.py (the lab's
    driver can only bind what the manifest holds, QP-HULL-2's abandonment defect 3)."""
    import pickle
    if str(ckpt).endswith('.npz'):
        z = np.load(ckpt, allow_pickle=False)
        n = int(z['n'])
        return [dict(A2=float(z[f'A2_{i}']), x=z[f'x_{i}'], rms=float(z[f'rms_{i}']), om2=float(z[f'om2_{i}']), gam=float(z[f'gam_{i}']))
                for i in range(n)]
    d = pickle.loads(pathlib.Path(ckpt).read_bytes())
    return d['cell|13/9']['members']


def maxrss_gb():
    import resource
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e9 if sys.platform == 'darwin' else r / 1e6          # bytes on macOS, kB on Linux


def part2(ckpt, grids=((24, 8), (48, 12)), NP=36, resume=False, rec_name='qp_hull_leg0_part2.json', chain=True):
    """Part 2, as run on the machine of record 2026-10-20/21. Every solve writes its state to analysis/ as it
    finishes (level 1, each rung, each member), so --resume continues from the last converged state after a stop.
    The first grid walks the Q-SWEEP ladder to member 0 and then three rungs across the gap to member 1 (the
    first run jumped the gap in one pin and the solve exhausted its rounds at rms 2.6e-5). A finer grid does not
    repeat the ladder: each member is seeded by prolonging the coarser grid's converged member (zero-padded 2D
    FFT, exact) and solved once at its pin; the finer grid's level-1 line is not re-derived (the coarse one
    matched Leg B's theta to 8 digits and the finer level-1 solve alone took 10579 s)."""
    log = lambda s_: print(s_, flush=True)
    adir = ROOT / 'analysis'
    T = Q1.QTGrid(432, NP, 9, 13)
    members = load_members(ckpt)
    out = dict(date=time.strftime('%Y-%m-%d'), part='2', cell='13/9 at 432 x 36 (COMPOSITE-SELECT Leg B, retained)', grids=[])
    rec_path = adir / rec_name
    for m in members:
        xm = np.asarray(m['x'], float)
        S, ke = T.G2.price(T.to_stage2(xm))
        log(f'  retained member A2 {m["A2"]:.7f}: rms {m["rms"]:.1e} om1 {T.unpack(xm)[3]:.7f} om2 {m["om2"]:.7f} gam {m["gam"]:.7f} '
            f'Sigma_wave {S:.6f} (ke {ke:.6f})')

    def save(path, H, x, pin):
        pickle.dump(dict(grid=[H.NT1, H.NT2, H.NP], A2=pin, x=x, rms=float(H.field_rms(x)), clos=float(H.closure_max(x)),
                         pins=QH.pin_residual(H, x, 'a2', pin)), open(path, 'wb'))

    def load(path, H, pin):
        if not (resume and path.exists()):
            return None
        r = pickle.load(open(path, 'rb'))
        x = np.asarray(r['x'], float)
        if x.size != H.n or abs(float(r.get('A2', pin)) - pin) > 1e-12:
            return None
        rms, clos, pr = float(H.field_rms(x)), float(H.closure_max(x)), QH.pin_residual(H, x, 'a2', pin)   # recomputed, not trusted
        if rms < Q1.RMS_BAR and clos < Q1.CLOSURE_BAR and pr < 1e-8:
            log(f'    resumed {path.name} (rms {rms:.1e} clos {clos:.1e} pins {pr:.1e})')
            return x
        log(f'    {path.name} on disk but unconverged (rms {rms:.1e} clos {clos:.1e} pins {pr:.1e}); re-solving')
        return None

    def rung(H, xs, pin, path, final):
        x = load(path, H, pin)
        if x is not None:
            return x
        t0 = time.time()
        xs = QH.solve(H, xs, 'a2', pin, rounds=60, stop_rms=None if final else 1e-9, verbose=False)
        save(path, H, xs, pin)
        log(f'    pin {pin:.7f}: rms {H.field_rms(xs):.1e} clos {H.closure_max(xs):.1e} om2 {H.unpack(xs)[4]:.7f} ({time.time() - t0:.0f}s, maxrss {maxrss_gb():.1f} GB)')
        return xs

    prev = None                                           # (H, [member states]) of the previous grid
    for gi, (nt1, nt2) in enumerate(grids):
        H = QH.HGrid(nt1, nt2, NP, 13 / 9)
        tag = f'qp_hull_leg0_part2_{nt1}x{nt2}x{NP}'
        g = dict(grid=[nt1, nt2, NP], level1=None, members=[])
        states = []
        if prev is None:
            p1 = adir / f'{tag}_l1.pkl'
            x = load(p1, H, 0.0)
            if x is None:
                t0 = time.time()
                x = QH.solve(H, H.level1_seed(), 'a2', 0.0, rounds=20, verbose=False)
                save(p1, H, x, 0.0)
                log(f'  hull {nt1}x{nt2}x{NP}: level-1 theta {H.unpack(x)[0].mean():.8f} om1 {H.unpack(x)[3]:.7f} '
                    f'gam {H.geom(x)[5]:.8f} ({time.time() - t0:.0f}s)')
            g['level1'] = dict(rms=float(H.field_rms(x)), theta=float(H.unpack(x)[0].mean()), om1=float(H.unpack(x)[3]), gam=float(H.geom(x)[5]))
            xs = H.ramp_seed(x, FRACS[0] * members[0]['A2'])
            for mi, m in enumerate(members):
                if mi == 0:
                    pins = [f * m['A2'] for f in FRACS]
                else:
                    a, b = members[mi - 1]['A2'], m['A2']
                    pins = [a + f * (b - a) for f in (1 / 3, 2 / 3, 1.0)]
                for k, pin in enumerate(pins):
                    final = k == len(pins) - 1
                    xs = rung(H, xs, pin, adir / (f'{tag}_{mi}.pkl' if final else f'{tag}_{mi}_r{k}.pkl'), final)
                states.append(xs)
        else:
            # member 0 by exact prolongation of the coarse member (a converged coarse state is a good seed; the
            # 48x12 solve from the 24x8 member 0 converged in 20 rounds); the later members by three rungs from
            # the fine grid's previous member, NOT by prolonging the coarse one, which at A2 0.0047 was itself
            # under-resolved in theta2 and seeded the fine solve at RMS 0.5 (2026-10-21).
            Hp, sp = prev
            for mi, m in enumerate(members):
                if mi == 0:
                    xs = rung(H, H.prolong_state(sp[0], Hp), m['A2'], adir / f'{tag}_0.pkl', True)
                else:
                    a, b = members[mi - 1]['A2'], m['A2']
                    xs = states[mi - 1]
                    for k, f in enumerate((1 / 3, 2 / 3, 1.0)):
                        pin = a + f * (b - a); final = k == 2
                        xs = rung(H, xs, pin, adir / (f'{tag}_{mi}.pkl' if final else f'{tag}_{mi}_r{k}.pkl'), final)
                states.append(xs)
                report(H, xs, m, nt1, nt2, g)
        if prev is None:
            for mi, m in enumerate(members):
                report(H, states[mi], m, nt1, nt2, g)
        out['grids'].append(g)
        rec_path.write_text(json.dumps(out, indent=1, default=str) + '\n')
        prev = (H, states) if chain else None
        g['maxrss_gb'] = maxrss_gb()
        rec_path.write_text(json.dumps(out, indent=1, default=str) + '\n')
    log(f'written {rec_path} (peak RSS of this process {maxrss_gb():.1f} GB)')


def report(H, xs, m, nt1, nt2, g):
    NP = H.NP
    T = Q1.QTGrid(432, NP, 9, 13)
    log = lambda s_: print(s_, flush=True)
    rel = lambda a, b: abs(a - b) / abs(b)
    mh = QH.metrics(H, xs)
    xm = np.asarray(m['x'], float)
    cmp_ = compare(H, xs, T, xm)
    Sh, keh = price_hull(H, xs); Sc, kec = T.G2.price(T.to_stage2(xm))
    rec = dict(A2_pin=m['A2'], hull=mh, cell=dict(rms=m['rms'], om1=float(T.unpack(xm)[3]), om2=m['om2'], gam=m['gam']),
               rel_om1=rel(mh['om1'], float(T.unpack(xm)[3])), rel_om2=rel(mh['om2'], m['om2']), rel_gam=rel(mh['gam'], m['gam']),
               compare=cmp_, price_hull=Sh, price_cell=Sc, rel_price=rel(Sh, Sc))
    g['members'].append(rec)
    log(f'  == {nt1}x{nt2}x{NP} A2 {m["A2"]:.7f}: om2 hull {mh["om2"]:.7f} cell {m["om2"]:.7f} rel {rec["rel_om2"]:.1e}; om1 rel {rec["rel_om1"]:.1e}; '
        f'gam rel {rec["rel_gam"]:.1e}; restricted-vs-cell dtheta {cmp_["dtheta"]:.1e} dpt {cmp_["dpt"]:.1e} dT {cmp_["dT"]:.1e}; '
        f'cell rms of restricted {cmp_["cell_rms_of_restricted"]:.1e}; Sigma_wave hull {Sh:.6f} cell {Sc:.6f} rel {rec["rel_price"]:.1e}')
    return rec


def main(quick=False):
    rec = dict(date='2026-10-20', A=[], B=[], C=[])
    log = lambda s: print(s, flush=True)

    def save():
        OUT.write_text(json.dumps(rec, indent=1, default=str) + '\n')
    NP = 8 if quick else 12
    grids_A = [(12, 8), (24, 8)] if quick else [(12, 8), (12, 12), (24, 8), (24, 12), (48, 8)]
    log('== A. resolution sweep at q = 1.492')
    for nt1, nt2 in grids_A:
        H = QH.HGrid(nt1, nt2, NP, QH.Q_PHYS)
        t0 = time.time()
        x1, xw, l1, rungs = ladder_hull(H, log)
        rec['A'].append(dict(grid=[nt1, nt2, NP], level1=l1, rungs=rungs, seconds=time.time() - t0)); save()
    for tag, (n1, n2), grids in (('B', (9, 13), [(12, 8)] if quick else [(12, 8), (24, 8)]),
                                 ('C', (2, 3), [(12, 8)] if quick else [(12, 8), (24, 8)])):
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
    if '--part2' in sys.argv:
        kw = {}
        if '--grids' in sys.argv:                      # e.g. --grids 24x24 or --grids 48x8,48x16 (each grid walks its own ladder)
            kw['grids'] = tuple(tuple(int(v) for v in g.split('x')) for g in sys.argv[sys.argv.index('--grids') + 1].split(','))
            kw['chain'] = False
        if '--out' in sys.argv:
            kw['rec_name'] = sys.argv[sys.argv.index('--out') + 1]
        part2(sys.argv[sys.argv.index('--part2') + 1], resume='--resume' in sys.argv, **kw)
    else:
        main(quick='--quick' in sys.argv)
