"""COMMISSION KNOT-REACH -- verdict, computed ONCE from the sealed checkpoint by the forms locked in
analysis/KNOT_REACH_charter_LOCKED.md. K3 the law: log L = p log n + c by least squares on the certified rungs with
n >= 7 (fixed window, B-2), p with its standard error; the same for the two-term mass m = L + lam S at lam in {0, 0.3}
(FND-MATTER-019's window); the per-crossing cost dL/dn on the top three rungs. K4 the price: under the fitted law,
the crossing number at which m/m(3_1) reaches 343 (FND-MATTER-066's demand) and at which m/m(ring) reaches 1836
(ring: L = pi, S = 0 by the registered anchor), with the fit's error band. K5 the reach: the largest certified rung
at 3-percent grade. No knot is named a particle (B-3).
    python benchmarks\\foundations\\knot_reach_verdict.py [analysis\\knot_reach_ckpt.pkl]
"""
import pickle, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'knot_reach_ckpt.pkl'
NMIN, BAND = 7, (0.9, 1.1)
DEMAND_TREFOIL, DEMAND_RING, L_RING = 343.0, 1836.0, float(np.pi)


def fit(ns, ms):
    x, y = np.log(ns), np.log(ms)
    A = np.column_stack([x, np.ones_like(x)])
    (p, c), res, *_ = np.linalg.lstsq(A, y, rcond=None)
    dof = max(len(x) - 2, 1)
    s2 = float(res[0]) / dof if len(res) else float(np.sum((y - A @ [p, c]) ** 2)) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return float(p), float(c), float(np.sqrt(cov[0, 0]))


def price(p, c, se, m_ref, demand, n_ref_label):
    out = {}
    for lab, pp in (('central', p), ('p-se', p - se), ('p+se', p + se)):
        out[lab] = float(np.exp((np.log(demand * m_ref) - c) / pp))
    print(f"[kr verdict K4]   crossings for m/m({n_ref_label}) = {demand:g}: {out['central']:.0f} (band {min(out['p-se'], out['p+se']):.0f} to {max(out['p-se'], out['p+se']):.0f})")
    return out


def main(path=CKPT):
    st = pickle.loads(pathlib.Path(path).read_bytes())
    rows = sorted((n, r) for n, r in st['rungs'].items() if 'L' in r)
    cert = [(n, r) for n, r in rows if r['det_ok'] and r['grade'] <= 0.03]
    print(f"[kr verdict] rungs run {[n for n, _ in rows]}; certified at grade {[n for n, _ in cert]}; halt: {st.get('halt')}")
    for n, r in rows:
        print(f"[kr verdict]   n={n:2d} N={r['N']:4d} L/D {r['L']:8.3f} grade {r['grade']:.4f} S {r['S']:8.3f} contacts {r['nc']:3d} len {r['lc']:7.2f} det_ok {r['det_ok']} {r['seconds']/60:.1f} min")
    reach = max((n for n, _ in cert), default=None)
    print(f"[kr verdict K5] reach: n = {reach} (largest rung certified at both ends and within the 3-percent grade)")
    win = [(n, r) for n, r in cert if n >= NMIN]
    if len(win) < 3:
        print(f"[kr verdict] VERDICT: REACH-SHORT ({len(win)} certified rungs at n >= {NMIN}; the law is not read)"); return 'REACH-SHORT'
    ns = np.array([n for n, _ in win], float); Ls = np.array([r['L'] for _, r in win]); Ss = np.array([r['S'] for _, r in win])
    p, c, se = fit(ns, Ls)
    print(f"[kr verdict K3] pure length: log L = {p:.4f} log n + {c:.4f}; p = {p:.4f} +/- {se:.4f} on {len(win)} rungs (n >= {NMIN})")
    top = win[-3:]
    dLdn = [(top[i + 1][1]['L'] - top[i][1]['L']) / (top[i + 1][0] - top[i][0]) for i in range(len(top) - 1)]
    print(f"[kr verdict K3] per-crossing cost dL/dn on the top rungs: {', '.join(f'{v:.3f}' for v in dLdn)} (D per crossing)")
    for lam in (0.0, 0.3):
        pm, cm, sem = fit(ns, Ls + lam * Ss)
        print(f"[kr verdict K3] two-term mass at lam = {lam}: p = {pm:.4f} +/- {sem:.4f}")
    # K4 the price, under the pure-length law (FND-MATTER-066's own convention)
    tre = st['rungs'].get(3)
    m3 = tre['L'] if tre else float(np.exp(c + p * np.log(3)))
    print(f"[kr verdict K4] price under the fitted pure-length law (m(3_1) = {m3:.3f} D, m(ring) = pi D):")
    price(p, c, se, m3, DEMAND_TREFOIL, '3_1')
    price(p, c, se, L_RING, DEMAND_RING, 'ring')
    verdict = 'LINEAR' if BAND[0] <= p <= BAND[1] else ('SUPERLINEAR' if p > BAND[1] else 'SUBLINEAR')
    print(f"[kr verdict] VERDICT: {verdict} (p = {p:.4f} +/- {se:.4f}; band {BAND}); reach n = {reach}")
    return verdict


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else CKPT)
