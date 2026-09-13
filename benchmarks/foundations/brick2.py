"""BRICK 2 -- coupling matrix elements (charter LOCKED + A1).
One cell per invocation; persists to /tmp/brick2_ckpt.pkl and
analysis/brick2_ckpt.pkl. M = max over the (m, n) mode's four real
vectors of |v . (J t)_pt| / (||v|| ||J t||), J at the deepest gated
member under its own a2 pin, t = normalized deep-pair tangent.
"""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = pathlib.Path('/tmp/brick2_ckpt.pkl')
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
NS = 144
NP = 36
N = NS * NP

CELLS = {
    '4/3': dict(N1=3, N2=4, src='analysis/qsweep_stage2c_ckpt.pkl',
                key='prof-4/3', line=(6, 2), jn=None),
    '5/3': dict(N1=3, N2=5, src='analysis/qsweep_stage2c_ckpt.pkl',
                key='prof-5/3', line=(12, 3), jn=(15, 6)),
    '5/4': dict(N1=4, N2=5, src='analysis/q54_profile_ckpt.pkl',
                key='prof-5/4', line=(10, 4), jn=(8, 2)),
}


def mode_M(w_pt, w_norm, m, n):
    i = np.arange(NS)[:, None] * (2 * np.pi * m / NS)
    p = np.arange(NP)[None, :] * (2 * np.pi * n / NP)
    best = 0.0
    for sgn in (+1, -1):
        for f in (np.cos, np.sin):
            v = f(i + sgn * p).ravel()
            best = max(best, abs(v @ w_pt) / (np.linalg.norm(v) *
                                              w_norm))
    return best


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    for cell, cfg in CELLS.items():
        if cell in st:
            continue
        d = pickle.loads((ROOT / cfg['src']).read_bytes())
        S = d[cfg['key']]['states']
        xa, xb = np.asarray(S[-2], float), np.asarray(S[-1], float)
        T = q1.QTGrid(NS, NP, cfg['N1'], cfg['N2'])
        t = xb - xa
        t /= np.linalg.norm(t)
        _, c2 = T.modes(T.geom(xb)[2])
        pin = float(abs(c2))
        sj, _ = SJ.make_instrument(T, xb, 'a2', pin, 50.0,
                                   cache=str(PAT))
        J, _r0 = sj(xb, 'a2', pin, 50.0)
        w = np.asarray(J @ t).ravel()
        w_pt = w[N:2 * N]
        wn = float(np.linalg.norm(w))
        m, n = cfg['line']
        out = dict(A2=pin, M=mode_M(w_pt, wn, m, n), line=(m, n),
                   w_norm=wn,
                   pt_frac=float(np.linalg.norm(w_pt) / wn))
        if cfg['jn']:
            out['M_jn'] = mode_M(w_pt, wn, *cfg['jn'])
            out['jn_line'] = cfg['jn']
        st[cell] = out
        _atomic_write(CKPT, pickle.dumps(st))
        (ROOT / 'analysis' / 'brick2_ckpt.pkl').write_bytes(
            pickle.dumps(st))
        print(f"[{cell}] A2 {pin:.6f}  M(m={m},n={n}) = "
              f"{out['M']:.5f}  ptfrac {out['pt_frac']:.3f}" +
              (f"  M_jn = {out['M_jn']:.5f}" if cfg['jn'] else ""),
              flush=True)
        return
    print("[brick2] ALL CELLS DONE -- run the verdict.", flush=True)


if __name__ == '__main__':
    main()
