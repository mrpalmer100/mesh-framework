"""COMMISSION SEAT-CONVERGE -- verdict, computed ONCE from the sealed checkpoint by the locked forms.
V1 the table: every knot's converged (or walled) seat L/D, S, contacts, iterations, against its registered seat.
V2 the stability rule of FND-MATTER-069, read on the converged table: sigma(n) = min over knots of crossing number n
   of L/D, divided by n; STRICT local minima over n = 3..8 (both neighbours required). Form STABLE-SET-{...} or
   MONOTONE-NULL. Knots WALLED at the cap enter with their last length, flagged, and the rule is read twice: with and
   without the walled knots (both printed; the form is read WITH them, as the registry's own table was).
V3 the walls: 6_1 (registered 32.3, terminal grade) and 7_2 (registered 38.6, provisional): WALL-DISSOLVED if the
   converged seat is more than 5 percent below the registered one, WALL-STANDS otherwise.
V4 the solver systematic: mean of L/D over the literature ideal (the values FND-MATTER-069 carries: 3_1 16.37, 4_1 21.04,
   5_1 23.55, 7_1 30.7) on the converged knots that have one (registered +2.3 percent).
    python benchmarks\\foundations\\seat_converge_verdict.py [analysis\\seat_converge_ckpt.pkl]
"""
import pathlib, pickle, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'seat_converge_ckpt.pkl'
LIT = {'3_1': 16.37, '4_1': 21.04, '5_1': 23.55, '7_1': 30.7}
WALLS = {'6_1': 32.3, '7_2': 38.6}


def rule(table):
    sig = {}
    for name, r in table.items():
        sig[r['n']] = min(sig.get(r['n'], np.inf), r['L'] / r['n'])
    ns = sorted(sig)
    stable = [n for n in ns if n - 1 in sig and n + 1 in sig and sig[n] < sig[n - 1] and sig[n] < sig[n + 1]]
    return sig, stable


def main(path=CKPT):
    st = pickle.loads(pathlib.Path(path).read_bytes())
    K = {k: v for k, v in st['knots'].items() if 'L' in v}
    print(f"[sc verdict] knots on the table: {sorted(K)}; refused: {[k for k, v in st['knots'].items() if 'L' not in v]}")
    for k in sorted(K, key=lambda x: (K[x]['n'], x)):
        r = K[k]
        print(f"[sc verdict]   {k}: n={r['n']} N={r['N']} L/D {r['L']:8.3f} ({r['rule']:9s}, iters {r['iters']:7d}, grade {r['grade']:.4f}) S {r['S']:8.3f} contacts {r['nc']:3d}; registered {r['registered']} {r['flag']}; {r['seconds']/60:.1f} min")
    # V2
    sig, stable = rule(K)
    print("[sc verdict V2] sigma(n) = min L/n: " + ', '.join(f"n={n}: {sig[n]:.3f}" for n in sorted(sig)))
    print(f"[sc verdict V2] strict local minima WITH walled knots: {stable}")
    K2 = {k: v for k, v in K.items() if v['rule'] != 'walled'}
    sig2, stable2 = rule(K2)
    print(f"[sc verdict V2] strict local minima WITHOUT walled knots: {stable2} (sigma over n = {sorted(sig2)})")
    form = f"STABLE-SET-{stable}" if stable else 'MONOTONE-NULL'
    # V3
    walls = {}
    for w, reg in WALLS.items():
        if w in K:
            walls[w] = 'WALL-DISSOLVED' if K[w]['L'] < 0.95 * reg else 'WALL-STANDS'
            print(f"[sc verdict V3] {w}: converged/last L/D {K[w]['L']:.3f} vs registered {reg} ({K[w]['rule']}) -> {walls[w]}")
    # V4
    ex = [(k, K[k]['L'] / LIT[k] - 1) for k in LIT if k in K and K[k]['rule'] == 'converged']
    if ex:
        print(f"[sc verdict V4] solver systematic over literature ideal: " + ', '.join(f"{k} {100*e:+.1f}%" for k, e in ex) + f"; mean {100*np.mean([e for _, e in ex]):+.1f}% (registered +2.3%)")
    print(f"[sc verdict] VERDICT: {form}; walls {walls}")
    return form


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else CKPT)
