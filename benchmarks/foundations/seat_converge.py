"""COMMISSION SEAT-CONVERGE -- the registered certified knot table re-seated under KNOT-REACH-2's convergence rule.
Charter analysis/SEAT_CONVERGE_charter_LOCKED.md. One doubling per invocation (checkpoint analysis/seat_converge_ckpt.pkl,
atomic; resumable); the PC runs it through go.py:
    python go.py benchmarks\\foundations\\seat_converge.py COMPLETE
Ten knots, each from its REGISTERED constructor at its registered point count, nothing new in the geometry:
  3_1, 5_1, 7_1   the torus parametrisation of FND-MATTER-019 / KNOT-REACH (knot_reach.torus, 40 n points)
  4_1             the trace-closure braid of FND-MATTER-020 (figure_eight_seated.braid_41, N = 130)
  5_2, 6_2, 6_3   the certified 3-strand words of FND-MATTER-021 (braid_family_spectrum.braid_closure, N = 130)
  6_1, 7_2, 8_1   the plat words of FND-MATTER-023 (plat_constructor.plat_closure, N = 140), identified by determinant
                  AND the Alexander odd part (alexander_certifier_61), as those claims identify them
The rule (C-1 of KNOT-REACH-2, unchanged): cumulative budgets 25000 x 2^k, the tightener resumed from the previous
doubling's coordinates; CONVERGED at the first k >= 1 whose length differs from the previous doubling's by under 1
percent; cap 1,600,000; a knot at the cap unconverged is recorded WALLED (its last length kept, flagged) and the table
goes on to the next knot (unlike the ladder, one knot's wall does not stop the others: the knots are independent).
Certificates at construction and after every doubling: det at tilts 0.013 and 0.11, and for 6_1 / 7_2 / 8_1 the
Alexander odd part; a loss is REFUSED by name and that knot stops (the others continue).
The ledger per knot as FND-MATTER-019 reads it: L/D, S, contacts. The verdict (seat_converge_verdict.py) reads the
table once by FND-MATTER-069's rule and the wall tests.
"""
import os, pathlib, pickle, shutil, sys, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'foundations')); sys.path.insert(0, str(ROOT))
from two_term_mass_model import tighten_coords                       # noqa: E402
from topology_certifier import knot_det                              # noqa: E402
from mapping_calibrated import build_table                           # noqa: E402
from knot_reach import torus, ledger, _atomic                        # noqa: E402
from figure_eight_seated import braid_41                             # noqa: E402
from braid_family_spectrum import braid_closure                      # noqa: E402
from plat_constructor import plat_closure, LADDER                    # noqa: E402
from alexander_certifier_61 import alexander_at, odd_part            # noqa: E402

CKPT = ROOT / 'analysis' / 'seat_converge_ckpt.pkl'
BASE, CAP, CONV = 25000, 1_600_000, 0.01
SMOKE = '--smoke' in sys.argv
SMOKE_DIV = float(os.environ.get('SC_SMOKE_DIV', '20'))

# name: (constructor, crossing number, det, Alexander odd part or None, registered seat L/D or None, registered flag)
KNOTS = {
    '3_1': (lambda: torus(3), 3, 3, None, 16.84, ''),
    '4_1': (lambda: braid_41(130), 4, 5, None, 21.64, ''),
    '5_1': (lambda: torus(5), 5, 5, None, 25.09, ''),
    '5_2': (lambda: braid_closure((1, 1, 1, 2, -1, 2)), 5, 7, None, 27.5, ''),
    '6_1': (lambda: plat_closure(LADDER['6_1'][0])[0], 6, 9, 0, 32.3, 'WALL (FND-MATTER-032, terminal grade)'),
    '6_2': (lambda: braid_closure((1, 1, 1, -2, 1, -2)), 6, 11, None, None, ''),
    '6_3': (lambda: braid_closure((1, 1, -2, 1, -2, -2)), 6, 13, None, None, ''),
    '7_1': (lambda: torus(7), 7, 7, None, 31.45, 'KNOT-REACH-2 seat'),
    '7_2': (lambda: plat_closure(LADDER['7_2'][0])[0], 7, 11, 5, 38.6, 'provisional (FND-MATTER-023)'),
    '8_1': (lambda: plat_closure(LADDER['8_1'][0])[0], 8, 13, 1, None, 'named next-order (FND-MATTER-023)'),
}
ORDER = ['3_1', '4_1', '5_1', '5_2', '6_1', '6_2', '6_3', '7_1', '7_2', '8_1']


def certified(P, name):
    _, n, det, alex, *_ = KNOTS[name]
    ok = knot_det(P) == det and knot_det(P, 0.11) == det
    if ok and alex is not None:
        ok = odd_part(alexander_at(P, 2)) == alex and odd_part(alexander_at(P, 2, 0.11)) == alex
    return bool(ok)


def main():
    global CKPT, BASE, CAP
    names = ORDER
    if SMOKE:
        names = ['4_1', '5_2']; CKPT = ROOT / 'analysis' / 'seat_converge_SMOKE_ckpt.pkl'; BASE = int(BASE / SMOKE_DIV); CAP = int(CAP / SMOKE_DIV)
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < 20.0 and not SMOKE:
        print(f"[sc] REFUSING TO START: {free_gb:.2f} GB free; free at least 20 GB", flush=True); raise SystemExit(2)
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else dict(knots={}, live=None, rule=dict(base=BASE, cap=CAP, conv=CONV))
    Ns, dEs = build_table()
    for name in names:
        if name in st['knots']:
            continue
        live = st.get('live')
        if live is None or live['name'] != name:
            P0 = np.asarray(KNOTS[name][0](), float)
            if not certified(P0, name):
                st['knots'][name] = dict(refused='construction certificate', det=(knot_det(P0), knot_det(P0, 0.11)))
                st['live'] = None; _atomic(CKPT, pickle.dumps(st))
                print(f"[sc {name}] REFUSED at construction: det {st['knots'][name]['det']}", flush=True); return
            live = dict(name=name, N=len(P0), P=P0, cum=0, k=-1, Ls=[], seconds=0.0); st['live'] = live
        k = live['k'] + 1; target = BASE * 2 ** k; step = target - live['cum']
        t0 = time.time()
        P = tighten_coords(np.array(live['P'], float), iters=step)
        ok = certified(P, name); led = ledger(P, Ns, dEs)
        live.update(P=P, cum=target, k=k, seconds=live['seconds'] + time.time() - t0); live['Ls'].append(led['L'])
        change = abs(live['Ls'][-1] - live['Ls'][-2]) / live['Ls'][-1] if k >= 1 else float('nan')
        print(f"[sc {name} k={k}] cum {target}; L/D {led['L']:.3f}; change {change:.4f}; cert {'ok' if ok else 'LOST'}; contacts {led['nc']}; {(time.time()-t0)/60:.1f} min", flush=True)
        done = None
        if not ok:
            done = 'certificate lost'
        elif k >= 1 and change < CONV:
            done = 'converged'
        elif target >= CAP:
            done = 'walled'
        if done:
            _, n, det, alex, reg, flag = KNOTS[name]
            rec = dict(name=name, n=n, N=live['N'], iters=target, L_half=live['Ls'][-2] if k >= 1 else float('nan'), grade=change, det_ok=ok,
                       seconds=live['seconds'], doublings=list(live['Ls']), rule=done, registered=reg, flag=flag, **led)
            st['knots'][name] = rec; st['live'] = None
            print(f"[sc {name}] {done.upper()}: iters {target}; L/D {led['L']:.3f} (registered {reg}); S {led['S']:.3f}; contacts {led['nc']} len {led['lc']:.2f}; {live['seconds']/60:.1f} min", flush=True)
        _atomic(CKPT, pickle.dumps(st))
        return
    print("[sc] SEAT-CONVERGE COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
