"""FINE-DISP-1 PREVIEW (the executor's exploratory run on the author's instruction, 2026-10-21, AFTER the charter's
forms were fixed at queue commit 5201dc8 and disclosed in the charter). Not the commission's driver: the lab's run
is the record. The SHIN6 engine (benchmarks/foundations/shin6_3d_bloch.py) inherited verbatim, plus the D2 bending
channel along the three nearest-neighbour axes:

    E_bend = (kappa / 2) sum_s sum_b w_s(b) | P_perp(b) (u_{s+b} - 2 u_s + u_{s-b}) |^2,
    w_s(b) = mean over {s-b, s, s+b} of (b . T)^4,   kappa = (kb / T0 a^2) x (tension weight of an aligned bond),

so that on a straight chain along b the bending term is exactly FND-REL-004's and beta shifts by -kb / (T0 a^2).
Fit (D1): y = (omega / k)^2 = c^2 [1 - beta (k a)^2 + gamma (k a)^4], k a in {0.02 .. 0.20}, per direction and band.
"""
import itertools
import json
import sys
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations import shin6_3d_bloch as S   # noqa: E402

KS = np.arange(0.02, 0.2001, 0.02)
NN3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]     # the three axes; +b and -b give the same second difference, so each once
# kappa is normalized to the engine's along-fibre stiffness: the straight medium's k -> 0 value of (omega/k)^2 along
# its tangent (norm_scale squared), which is the engine's T0/mu including the next-nearest bonds. With that
# normalization a straight chain's beta shifts by exactly -kb/(T0 a^2) (checked as v2).
_Ps, _ss, _Ts, _PRs = S.build_cell(1 / 3, False)
W_ALIGNED = S.norm_scale(_Ps, _ss, _Ts, _PRs) ** 2


def dyn_matrix_bend(kv, P, sites, T, PR, kb_ratio):
    D = S.dyn_matrix(kv, P, sites, T, PR)
    if kb_ratio == 0:
        return D
    n = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    kap = kb_ratio * W_ALIGNED
    B = np.zeros_like(D)
    for s in sites:
        for b in NN3:
            bh = np.array(b, float)
            sm = tuple((s[m] - b[m]) % P for m in range(3))
            sp = tuple((s[m] + b[m]) % P for m in range(3))
            w = np.mean([(bh @ T[q]) ** 4 for q in (sm, s, sp)])
            if w < 1e-14:
                continue
            Pp = np.eye(3) - np.outer(bh, bh)
            trip = ((sm, 1.0, -bh), (s, -2.0, np.zeros(3)), (sp, 1.0, bh))   # (site, coefficient, displacement in lattice units)
            for (qi, ci, ri) in trip:
                for (qj, cj, rj) in trip:
                    ph = np.exp(1j * (kv @ (rj - ri)))
                    i, j = idx[qi], idx[qj]
                    B[3 * i:3 * i + 3, 3 * j:3 * j + 3] += kap * w * ci * cj * Pp * ph
    return (D + B + (D + B).conj().T) / 2


def two_bands(kv, P, sites, T, PR, kb_ratio):
    D = dyn_matrix_bend(kv, P, sites, T, PR, kb_ratio)
    w2, V = np.linalg.eigh(D)
    om = np.sqrt(np.clip(w2, 0, None))
    vs = S.pw_vectors(kv, P, sites, T)
    wt = sum(np.abs(V.conj().T @ v) ** 2 for v in vs)
    order = np.argsort(-wt)
    return [(om[b], wt[b]) for b in order[:2]]


def fit_direction(d, P, sites, T, PR, kb_ratio):
    out = []
    for band in (0, 1):
        ys, wts = [], []
        for k in KS:
            r = two_bands(k * d, P, sites, T, PR, kb_ratio)
            ys.append((r[band][0] / k) ** 2); wts.append(r[band][1])
        ys = np.array(ys)
        X = np.vstack([np.ones_like(KS), KS ** 2, KS ** 4]).T
        c, *_ = np.linalg.lstsq(X, ys, rcond=None)
        out.append(dict(c=float(np.sqrt(c[0])), beta=float(-c[1] / c[0]), gamma=float(c[2] / c[0]),
                        resid=float(np.abs(X @ c - ys).max()), min_wt=float(min(wts))))
    return out


def run(f, wound, kb_ratio, label):
    P, sites, T, PR = S.build_cell(f, wound)
    rows = []
    for d in S.DIRS:
        for band, r in enumerate(fit_direction(d, P, sites, T, PR, kb_ratio)):
            r.update(dir=[round(float(x), 4) for x in d], band=band); rows.append(r)
    betas = np.array([r['beta'] for r in rows])
    rec = dict(label=label, f=f, wound=wound, kb_ratio=kb_ratio, P=P, beta_iso=float(betas.mean()),
               A=float((betas.max() - betas.min()) / 2), beta_min=float(betas.min()), beta_max=float(betas.max()),
               max_resid=float(max(r['resid'] for r in rows)), min_wt=float(min(r['min_wt'] for r in rows)),
               band_gap=float(abs(betas[0::2].mean() - betas[1::2].mean())), rows=rows)
    print(f"{label:<34} kb/T0a^2 {kb_ratio:.5f}: beta_iso {rec['beta_iso']:+.6f}  A {rec['A']:.6f}  "
          f"[{rec['beta_min']:+.6f}, {rec['beta_max']:+.6f}]  bands differ {rec['band_gap']:.1e}  "
          f"resid {rec['max_resid']:.1e}  min pw wt {rec['min_wt']:.2f}", flush=True)
    return rec


if __name__ == '__main__':
    KBS = [0.0, 0.02, 0.04, 0.06, 0.07909]
    out = dict(date='2026-10-21', note=__doc__, straight=[], straight_chain=[], wound=[])
    print('v1/v2 STRAIGHT CONTROL (P = 1), beta per kb; the on-axis closed form is 1/12 - kb/(T0 a^2):')
    for kb in KBS:
        r = run(1 / 3, False, kb, 'straight (13 directions)')
        ax = [x['beta'] for x in r['rows'] if x['dir'] == [0.0, 0.0, 1.0]]
        r['on_axis_beta'] = float(np.mean(ax)); r['closed_form'] = 1 / 12 - kb
        print(f"      along-fibre (z) beta {r['on_axis_beta']:+.7f}  closed form {r['closed_form']:+.7f}  "
              f"diff {r['on_axis_beta'] - r['closed_form']:+.1e}")
        out['straight'].append(r)
    print('\nWOUND, adjudicating member f = 1/5 (P = 5), kb sweep:')
    for kb in KBS:
        out['wound'].append(run(1 / 5, True, kb, 'wound f=1/5 (ADJUDICATING)'))
    print('\nWOUND context members at kb = 0 and the ceiling:')
    for f in (1 / 4, 1 / 3):
        for kb in (0.0, 0.07909):
            out['wound'].append(run(f, True, kb, f'wound f={f:.3g} (context)'))
    (ROOT / 'analysis' / 'fine_disp_preview.json').write_text(json.dumps(out, indent=1))
    print('\nwritten analysis/fine_disp_preview.json')
