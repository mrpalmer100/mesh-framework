"""Dry run (new cells only, include_existing=False, so each form can be exercised in isolation; see the note on the
locked statistic in analysis/COMPOSITE_SELECT_legB_verdict_readiness.md) of benchmarks/foundations/composite_legB_verdict.py on synthetic checkpoints in composite_legB.py's exact
layout (2026-10-04, ahead of LADDER COMPLETE). Forms exercised: RAT-SMOOTH, RAT-RESONANT, RAT-MIXED, RAT-OPEN,
INCOMPLETE; the QC price rows are exercised with do_price=False (states are random vectors). Run from the repo root."""
import pickle, pathlib, sys, io, contextlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from benchmarks.foundations import composite_legB_verdict as V
CELLS = V.CELLS
def meas(A2, rate): return dict(A2=A2, rate=rate, vpt=1e-2, fdir=0.3, rms=5e-9, clos=1e-8, om2=3.2)
def prof(D, n=12, A2s=None):
    A2s = A2s if A2s is not None else np.linspace(0.0040, 0.0066, n)
    rate_hi = 1e-4; return dict(states=[np.zeros(4) for _ in range(n + 2)], meas=[meas(a, rate_hi * (D if a < 0.0055 else 1.0)) for a in A2s])
def ckpt(Dfun, done=True, halt_cells=()):
    st = {}
    for tag, N1, N2 in CELLS:
        D = Dfun(N2 / N1, N1)
        halted = tag in halt_cells
        st[f'cell|{tag}'] = dict(phase='done' if done else 'prof54', members=[], prof36=prof(D) if not halted else dict(states=[], meas=[]), cont54={}, prof54=prof(D * 0.9) if not halted else dict(states=[], meas=[]), halt=('refused' if halted else None))
    return st
def run(name, st, expect36):
    p = pathlib.Path('/tmp') / f'legb_dry_{name}.pkl'; p.write_bytes(pickle.dumps(st)); buf = io.StringIO()
    with contextlib.redirect_stdout(buf): v = V.main(p, do_price=False, include_existing=False)
    got = v if isinstance(v, str) else v[0]; ok = expect36 in got
    print(f"{'PASS' if ok else 'FAIL'}  {name:16s} expected {expect36:14s} got {got}")
    if not ok: print(buf.getvalue()[-1200:])
    return ok
R = []
R.append(run('smooth', ckpt(lambda q, N1: 20.0 - 10.0 * q), 'RAT-SMOOTH'))      # D monotone in q, blind to N1
R.append(run('resonant', ckpt(lambda q, N1: {5: 9.0, 7: 4.0, 9: 1.5}[N1] + 0.01 * q), 'RAT-RESONANT'))            # D tracks the order, blind to q
R.append(run('mixed', ckpt(lambda q, N1: 10.0 * (q - 1.4) + {5: 2.0, 7: 1.0, 9: 0.0}[N1]), 'RAT-'))      # both move: MIXED or NO CALL, both are readings
R.append(run('open', ckpt(lambda q, N1: 5.0, halt_cells=('13/9', '14/9', '11/7', '10/7')), 'RAT-OPEN'))
R.append(run('incomplete', ckpt(lambda q, N1: 5.0, done=False), 'INCOMPLETE'))
print(f"{sum(R)}/{len(R)} forms read as expected")
