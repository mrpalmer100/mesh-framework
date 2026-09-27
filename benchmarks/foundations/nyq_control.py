"""COMMISSION NYQ-CONTROL (charter analysis/NYQ_CONTROL_charter_LOCKED.md): the KERNEL-CONT stage-B
sweep repeated with the DE-ALIASED bordered corrector and the wsNyq <= 1e-4 bar, plus controls
c1 (b = 0 floor), c2 (aligned member unchanged), c3 (the fault reproduced with dealias=False).
v3 (2026-09-27): one bordered ROUND per invocation with the solver's round messages IN THE LOG,
the lam ladder bounded at 1e-5, the floor detector on, and short budgets for the controls.
Checkpoint analysis/nyq_control_v3_ckpt.pkl (atomic). Terminal line:
'NYQ-CONTROL COMPLETE -- run the verdict'."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import kernel_continuation as KC      # noqa
from benchmarks.foundations.kernel_cont import setup               # noqa


def _atomic_write(path, data):
    import os
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_bytes(data); os.replace(tmp, path)


ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'nyq_control_v3_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
NYQ_BAR = 1e-4
G288, G144 = (288, 36, 4, 5), (144, 36, 3, 4)
PLAN = [  # (label, grid, source, b, dealias, rounds, nyq_bar)
    ('c1|b=+0.000',            G288, 'B',       0.00, True,  10, NYQ_BAR),
    ('B|b=-0.100',             G288, 'B',      -0.10, True,  60, NYQ_BAR),
    ('B|b=-0.200',             G288, 'B',      -0.20, True,  60, NYQ_BAR),
    ('B|b=-0.050',             G288, 'B',      -0.05, True,  60, NYQ_BAR),
    ('B|b=+0.050',             G288, 'B',       0.05, True,  60, NYQ_BAR),
    ('B|b=+0.100',             G288, 'B',       0.10, True,  60, NYQ_BAR),
    ('B|b=+0.200',             G288, 'B',       0.20, True,  60, NYQ_BAR),
    ('c3|b=-0.100|nodealias',  G288, 'B',      -0.10, False, 60, None),
    ('c2|aligned|b=+0.000',    G144, 'ALIGNED', 0.00, True,  10, NYQ_BAR),
]


def load_source(kind):
    if kind == 'B':
        d = pickle.loads((ROOT / 'analysis' / 'antiarc_s288_ckpt.pkl').read_bytes()); return np.asarray(d['s288|s0']['x'], float)
    d = pickle.loads((ROOT / 'analysis' / 'qsweep_stage1_ckpt.pkl').read_bytes()); return np.asarray(d['q4/3']['members'][0]['x'], float)


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    for label, (NS, NP, N1, N2), src, b, dealias, rounds, nyq_bar in PLAN:
        R = st.setdefault(label, dict(hist=[], done=False))
        if R['done']: continue
        T = q1.QTGrid(NS, NP, N1, N2)
        if 'x0' not in R:
            x0 = load_source(src); m = q1.metrics(T, x0); pin = float(m['A2'])
            if src == 'B':
                c, sig = setup(T, x0, pin)
            else:
                import scipy.sparse as sp
                sj, _ = SJ.make_instrument(T, x0, 'a2', pin, 50.0, cache=str(PAT)); J, _ = sj(x0, 'a2', pin, 50.0); J = sp.csr_matrix(J)
                c, sig = KC.near_null(T, J, x0, len(x0) - 1)
            R.update(x0=x0, x=x0, pin=pin, c=c, sigma=float(sig), rms0=float(m['rms']), nyq0=float(m['nyq']), lam=1e-9); save()
            print(f"[nyq {label}] source RMS {m['rms']:.1e} wsNyq {m['nyq']:.1e} pin {pin:.7f}; near-null |Jc|/row {sig:.1e}; dealias={dealias}; budget {rounds}", flush=True); return
        x0 = np.asarray(R['x0'], float); pin = R['pin']; c = np.asarray(R['c'], float)
        sj, _ = SJ.make_instrument(T, x0, 'a2', pin, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        # the first invocation carries the predictor (round 0); later invocations are pure corrector rounds
        # (b already reached), so bordered_gn's it==0 predictor branch is skipped because gap ~ 0.
        lamstate = {'lam': R.get('lam', 1e-9)}
        x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), pin, c, b, x0, sj, bs, rounds=1, state=lamstate,
                                 log=lambda msg: print(f"[nyq {label}]{msg}", flush=True), dealias=dealias, nyq_bar=nyq_bar)
        R['x'] = x; R['hist'] += hist; R['lam'] = lamstate['lam']
        m = q1.metrics(T, x); rms, clos, nyq = float(m['rms']), float(m['clos']), float(m['nyq'])
        gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR and nyq <= NYQ_BAR
        gated_nobar = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
        # floor: no accepted step this round, or 6 consecutive accepted rounds each below 1e-3 relative decrease
        H = [h[2] for h in R['hist']]                      # wres per accepted round
        floored = (hist == []) or (len(H) >= 7 and all((1 - H[-k] / H[-k - 1]) < 1e-3 for k in range(1, 7)))
        stop = gated or (gated_nobar and nyq_bar is None) or len(R['hist']) >= rounds or floored
        if stop:
            R.update(done=True, gated=bool(gated), gated_nobar=bool(gated_nobar), rms=rms, clos=clos, nyq=nyq, om2=float(m['om2']))
            verdict = 'GATED (clean)' if gated else ('gates only WITH Nyquist' if gated_nobar else 'floor')
            print(f"[nyq {label}] {verdict}  RMS {rms:.1e} clos {clos:.1e} wsNyq {nyq:.1e} om2 {m['om2']:+.6f} rounds {len(R['hist'])}", flush=True)
        save(); return
    print("[nyq] NYQ-CONTROL COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
