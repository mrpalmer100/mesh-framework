"""COMMISSION KNOT-REACH -- the mass-versus-crossing law on the torus ladder T(2,n), to the solver's reach.
Charter analysis/KNOT_REACH_charter_LOCKED.md. One rung per invocation (resumable; checkpoint analysis/knot_reach_ckpt.pkl,
atomic); the PC runs it through go.py with the terminal pattern COMPLETE:
    python go.py benchmarks\\foundations\\knot_reach.py COMPLETE
K1 the ladder: T(2,n), n in RUNGS, the FND-MATTER-019 parametrisation ((2 + cos n t) cos 2t, (2 + cos n t) sin 2t, sin n t)
   times the trefoil's scale 1.8, point count 40 n, iterations 25000 n/3 (rules fixed at lock, B-2); certified by
   determinant (knot_det == n) at both ends at both registered tilts (0.013 and 0.11), or REFUSED by name (B-1).
K2 the ledger per rung as FND-MATTER-019 reads it: L (units of D), the zero-point term, contact count and length.
K5 the grade test: the tightened length at half the budget against the full budget; a change over 3 percent fails
   the registered grade and the rung is the reach (B-5: the budget is not raised).
K3/K4 (the fit and the price) are in knot_reach_verdict.py, computed once from the sealed checkpoint.
"""
import pathlib, pickle, shutil, sys, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'foundations')); sys.path.insert(0, str(ROOT))
from two_term_mass_model import tighten_coords, profile            # noqa: E402
from topology_certifier import knot_det                             # noqa: E402
from mapping_calibrated import build_table, contact_phys            # noqa: E402

CKPT = ROOT / 'analysis' / 'knot_reach_ckpt.pkl'
RUNGS = (3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
SCALE, PTS_PER_N, ITERS_PER_N = 1.8, 40, 25000 / 3
A_C = -0.509658; B_C = 2 * np.pi * (2.5 - 7 * np.sqrt(2) / 4); DIR = -0.502506   # FND-MATTER-013/014/019
GRADE = 0.03
SMOKE = '--smoke' in sys.argv            # sandbox only: rungs 3 and 5, separate checkpoint; iteration rule divided by KR_SMOKE_DIV (default 20)
import os
SMOKE_DIV = float(os.environ.get('KR_SMOKE_DIV', '20'))


def torus(n):
    N = PTS_PER_N * n
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)
    return np.stack([(2 + np.cos(n * t)) * np.cos(2 * t), (2 + np.cos(n * t)) * np.sin(2 * t), np.sin(n * t)], axis=1) * SCALE


def _atomic(path, data):
    import os
    tmp = path.with_suffix('.tmp'); tmp.write_bytes(data); os.replace(tmp, path)


def certified(P, n):
    return knot_det(P) == n and knot_det(P, 0.11) == n


def ledger(P, Ns, dEs):
    def dE_loop(Lam):
        if Lam >= 120:
            return (A_C + B_C * np.log(Lam)) / Lam
        return float(np.interp(np.clip(Lam, Ns[0], 120), Ns, dEs))
    kap, _, edge, L, _ = profile(P)
    kap = np.maximum(kap, 1e-4); Lam = 2 * np.pi / kap
    Eb = float(np.sum(edge * np.array([dE_loop(x) / x for x in Lam])))
    nc, lc = contact_phys(P)
    return dict(L=float(L), S=Eb + DIR * lc, nc=int(nc), lc=float(lc))


def main():
    global CKPT
    rungs = (3, 5) if SMOKE else RUNGS
    if SMOKE:
        CKPT = ROOT / 'analysis' / 'knot_reach_SMOKE_ckpt.pkl'
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < 20.0 and not SMOKE:
        print(f"[kr] REFUSING TO START: {free_gb:.2f} GB free; free at least 20 GB", flush=True); raise SystemExit(2)
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else dict(rungs={}, reach=None, halt=None)
    if st['halt']:
        print(f"[kr] KNOT-REACH COMPLETE -- run the verdict ({st['halt']})", flush=True); return
    Ns, dEs = build_table()
    for n in rungs:
        if n in st['rungs']:
            continue
        iters = int(ITERS_PER_N * n / (SMOKE_DIV if SMOKE else 1))
        P0 = torus(n)
        if not certified(P0, n):
            st['rungs'][n] = dict(refused='construction certificate', det=(knot_det(P0), knot_det(P0, 0.11)))
            st['halt'] = f'rung {n} refused at construction'; _atomic(CKPT, pickle.dumps(st))
            print(f"[kr n={n}] REFUSED: construction certificate det {st['rungs'][n]['det']} != {n}", flush=True); return
        t0 = time.time()
        half = tighten_coords(P0.copy(), iters=iters // 2)
        Lh = ledger(half, Ns, dEs)['L']
        full = tighten_coords(half.copy(), iters=iters - iters // 2)
        ok = certified(full, n)
        led = ledger(full, Ns, dEs)
        grade = abs(led['L'] - Lh) / led['L']
        rec = dict(n=n, N=len(P0), iters=iters, L_half=Lh, grade=grade, det_ok=ok, seconds=time.time() - t0, **led)
        st['rungs'][n] = rec
        if not ok:
            st['halt'] = f'rung {n} refused: certificate lost after tightening'
        elif grade > GRADE:
            st['reach'] = max([k for k in st['rungs'] if k < n], default=None); st['halt'] = f'rung {n} fails the 3-percent grade ({grade:.3f}); reach {st["reach"]}'
        _atomic(CKPT, pickle.dumps(st))
        print(f"[kr n={n}] {'certified' if ok else 'CERTIFICATE LOST'}; N {len(P0)} iters {iters}; L/D {led['L']:.3f} (half-budget {Lh:.3f}, grade {grade:.4f}); S {led['S']:.3f}; contacts {led['nc']} len {led['lc']:.2f}; {rec['seconds']/60:.1f} min", flush=True)
        if st['halt']:
            print(f"[kr] KNOT-REACH COMPLETE -- run the verdict ({st['halt']})", flush=True)
        return
    st['reach'] = max(st['rungs']); st['halt'] = f'ladder complete; reach {st["reach"]}'; _atomic(CKPT, pickle.dumps(st))
    print(f"[kr] KNOT-REACH COMPLETE -- run the verdict (ladder complete; reach {st['reach']})", flush=True)


if __name__ == '__main__':
    main()
