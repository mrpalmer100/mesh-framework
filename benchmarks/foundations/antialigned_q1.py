"""ANTI-ALIGNED (ITEM 6a) Q1 + v1/v2  [v2: RAMP LADDER, the registered q-sweep protocol] -- the linear internal spectrum per retained cell,
both sectors, at infinitesimal amplitude (A2 = 0.02 R2), on the 144x36 chart with the
SJ-CREDENTIALED instrument (stage-2's Leg 0 protocol: a2-pinned small-amplitude solve
with om2 FREE; the converged om2 is the linear root). Two seeds per sector as stage 2
used (aligned +0.65 Om1 / +1.2 Om1; anti-aligned -0.35 Om1 / -0.65 Om1). Cells: 3/2
(v1/v2 reproduction: +3.201 / -2.221), 4/3, 5/3, 5/4. One (cell, seed) per invocation;
checkpoint analysis/antialigned_ckpt.pkl. Charter D1: 'on a mode' = within 1e-4 of
Om1 n / N1 (the cell ladder sqrt(T) k1 n / N1). NO number from the charter's expected
outcomes is entered; the ladder is computed from the cell's own Om1.
"""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import truestate_stage2 as S2    # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antialigned_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
CELLS = [('3/2', 2, 3), ('4/3', 3, 4), ('5/3', 3, 5), ('5/4', 4, 5)]
SEEDS = [('aligned', +0.65), ('aligned', +1.20), ('anti', -0.35), ('anti', -0.65)]   # x Om1
RAMP = (0.15, 0.30, 0.55, 0.80)                       # registered sub-pin ladder (q-sweep stage 1)
CKPT_PAT = PAT



def ramp_seed(T, G, sub, om2_seed):
    W, Z, Tf, gam, om1 = G.level1()
    ph = np.exp(1j * G.K2 * G.sgrid)[:, None] * np.exp(-1j * G.pgrid)[None, :]
    return T.from_stage2(G.pack(W + sub * ph, Z, Tf, gam, om1, om2_seed)), om1


def sparse_solve(T, seed, pin, rounds, st, key, stop_rms=None, hard_cap=None):
    """protocol-faithful rung budget (q54_stage1_sparse.sparse_solve semantics)."""
    ck, fk = key + '-cum', key + '-lastw'
    cum = st.get(ck, 0); cap = hard_cap if hard_cap is not None else 4 * rounds
    if cum >= cap: return np.asarray(st[key]['x'], float)
    if cum >= rounds and key in st:
        w = float(np.linalg.norm(T.wres(np.asarray(st[key]['x'], float), 'a2', pin, 50.0)))
        if abs(w - st.get(fk, -1.0)) < 1e-12: return np.asarray(st[key]['x'], float)
        st[fk] = w
    sj, _ = SJ.make_instrument(T, seed, 'a2', pin, 50.0, cache=str(PAT))
    bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    return SJ.gn_sparse(T, seed, 'a2', pin, sj, bs, rounds=max(1, cap - cum), st=st, key=key, stop_rms=stop_rms)


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.startswith('aa|') and not k.endswith('-cum') and not k.endswith('-lastw'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v); _atomic_write(CKPT, pickle.dumps(dict(self)))
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    for tag, N1, N2 in CELLS:
        for sec, fac in SEEDS:
            if sec == 'aligned' and tag != '3/2': continue     # aligned roots at 4/3, 5/3, 5/4 are held by the registered waypoint-1 members
            key = f'aa|{tag}|{sec}|{fac:+.2f}'
            if st.get(key + '|done'): continue
            T = q1.QTGrid(144, 36, N1, N2); G = T.G2; A2 = 0.02 * S2.R2
            xw = None; om1 = G.level1()[4]
            for frac in RAMP:
                sub = frac * A2; rk = f'{key}|rung{frac}'
                if rk in st: xw = np.asarray(st[rk], float); continue
                seed = ramp_seed(T, G, sub, fac * om1)[0] if xw is None else xw
                xw = sparse_solve(T, seed, sub, 10, st, f'{key}|sub{frac}', stop_rms=1e-5)
                st[rk] = xw
                print(f"  [{key}] rung {frac} A2 {sub:.7f}: RMS {T.field_rms(xw):.1e}", flush=True); return
            xn = sparse_solve(T, xw, A2, 60, st, f'{key}|gate', hard_cap=60)
            m, ok = q1.gate(T, xn, key, pin=A2)
            it = st.get(f'{key}|gate-cum', 0)
            if ok or it >= 60:
                ladder = [om1 * n / N1 for n in range(1, 4 * N1 + 1)]
                near = min(ladder, key=lambda L: abs(abs(m['om2']) - L)); rel = abs(abs(m['om2']) - near) / near
                st[key + '|done'] = dict(gated=bool(ok), om2=float(m['om2']), om1=float(om1), rms=float(m['rms']), ladder_nearest=float(near), rel=float(rel))
                print(f"[{key}] {'GATED' if ok else 'BUDGET'} om2 = {m['om2']:+.5f} (Om1 {om1:.5f}); nearest cell mode {near:.5f} "
                      f"({'ON' if rel < 1e-4 else 'off'} by {rel:.1e})", flush=True)
            else:
                print(f"[{key}] gate resume (round {it})", flush=True)
            return
    print("[antialigned] ALL CELLS COMPLETE -- run the Q1 verdict", flush=True)


if __name__ == '__main__':
    main()
