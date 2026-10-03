"""COMMISSION NYQ-CONTROL-2 (charter analysis/NYQ_CONTROL_2_charter_LOCKED.md, locked 2026-10-03).
The Nyquist question on the instrument that raised it: the 2026-09-16 bordered corrector
(benchmarks/foundations/kernel_continuation_0916.py, frozen; fixed lam, fraction ladder, a
single rejected step terminal, no stall rule) with de-aliasing as its ONLY amendment.
Order: c3 (the fault reproduction, dealias OFF) FIRST; if it does not gate with wsNyq > 1e-3 the
driver stops before the sweep (NYQ2-IRREPRODUCIBLE is then the verdict). Then c1, c2, and the
six-b de-aliased sweep. One bordered round per invocation (as v3) so an interruption loses at
most a round; the solver's round messages go to the log. Checkpoint analysis/nyq_control_2_ckpt.pkl
(atomic). Terminal line: 'NYQ-CONTROL-2 COMPLETE -- run the verdict'. One machine per job."""
import numpy as np, pickle, pathlib, sys, hashlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1                   # noqa
from benchmarks.foundations import sparsej_instrument as SJ              # noqa
from benchmarks.foundations import kernel_continuation_0916 as KC        # noqa  (FROZEN solver)
from benchmarks.foundations.kernel_cont import setup                      # noqa


def _atomic_write(path, data):
    import os
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_bytes(data); os.replace(tmp, path)


ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'nyq_control_2_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
SOLVER = ROOT / 'benchmarks' / 'foundations' / 'kernel_continuation_0916.py'
NYQ_BAR = 1e-4
G288, G144 = (288, 36, 4, 5), (144, 36, 3, 4)
PLAN = [  # (label, grid, source, b, dealias, rounds, nyq_bar)   -- order is the charter's
    ('c3|b=-0.100|nodealias',  G288, 'B',      -0.10, False, 40, None),
    ('c1|b=+0.000',            G288, 'B',       0.00, True,  10, NYQ_BAR),
    ('c2|aligned|b=+0.000',    G144, 'ALIGNED', 0.00, True,  10, NYQ_BAR),
    ('B|b=-0.100',             G288, 'B',      -0.10, True,  60, NYQ_BAR),
    ('B|b=-0.200',             G288, 'B',      -0.20, True,  60, NYQ_BAR),
    ('B|b=-0.050',             G288, 'B',      -0.05, True,  60, NYQ_BAR),
    ('B|b=+0.050',             G288, 'B',       0.05, True,  60, NYQ_BAR),
    ('B|b=+0.100',             G288, 'B',       0.10, True,  60, NYQ_BAR),
    ('B|b=+0.200',             G288, 'B',       0.20, True,  60, NYQ_BAR),
]
C3 = PLAN[0][0]


def load_source(kind):
    if kind == 'B':
        d = pickle.loads((ROOT / 'analysis' / 'antiarc_s288_ckpt.pkl').read_bytes()); return np.asarray(d['s288|s0']['x'], float)
    d = pickle.loads((ROOT / 'analysis' / 'qsweep_stage1_ckpt.pkl').read_bytes()); return np.asarray(d['q4/3']['members'][0]['x'], float)


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    if 'solver_sha256' not in st:
        st['solver_sha256'] = hashlib.sha256(SOLVER.read_bytes()).hexdigest()
        print(f"[nyq2] frozen solver sha256 {st['solver_sha256']}", flush=True)
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    c3 = st.get(C3)
    if c3 is not None and c3.get('done') and not (c3['gated_nobar'] and c3['nyq'] > 1e-3):
        print("[nyq2] c3 did not reproduce the fault on the 09-16 solver; the sweep is not run (charter). NYQ-CONTROL-2 COMPLETE -- run the verdict", flush=True); save(); return
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
            R.update(x0=x0, x=x0, pin=pin, c=c, sigma=float(sig), rms0=float(m['rms']), nyq0=float(m['nyq'])); save()
            print(f"[nyq2 {label}] source RMS {m['rms']:.1e} wsNyq {m['nyq']:.1e} pin {pin:.7f}; near-null |Jc|/row {sig:.1e}; dealias={dealias}; budget {rounds}", flush=True); return
        x0 = np.asarray(R['x0'], float); pin = R['pin']; c = np.asarray(R['c'], float)
        sj, _ = SJ.make_instrument(T, x0, 'a2', pin, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        # one round per invocation: the first carries the predictor (gap = b); later rounds are
        # pure corrector rounds at fixed b. The 09-16 solver: fixed lam 1e-9, no state carried.
        x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), pin, c, b, x0, sj, bs, rounds=1,
                                 log=lambda msg: print(f"[nyq2 {label}]{msg}", flush=True), dealias=dealias)
        m = q1.metrics(T, x); rms, clos, nyq = float(m['rms']), float(m['clos']), float(m['nyq'])
        rejected = (hist == [])                                     # the 09-16 rule: a rejected step is terminal
        if not rejected:
            R['x'] = x; R['hist'] += [tuple(h) + (nyq,) for h in hist]
        else:
            m = q1.metrics(T, np.asarray(R['x'], float)); rms, clos, nyq = float(m['rms']), float(m['clos']), float(m['nyq'])
        gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR and nyq <= NYQ_BAR
        gated_nobar = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
        stop = gated or (gated_nobar and nyq_bar is None) or rejected or len(R['hist']) >= rounds
        if stop:
            manner = 'gated' if (gated or (gated_nobar and nyq_bar is None)) else ('rejected step' if rejected else 'budget')
            R.update(done=True, gated=bool(gated), gated_nobar=bool(gated_nobar), rms=rms, clos=clos, nyq=nyq, om2=float(m['om2']), manner=manner)
            state = 'GATED (clean)' if gated else ('gates only WITH Nyquist' if gated_nobar else 'floor')
            print(f"[nyq2 {label}] {state}  RMS {rms:.1e} clos {clos:.1e} wsNyq {nyq:.1e} om2 {m['om2']:+.6f} rounds {len(R['hist'])} ended by {manner}", flush=True)
        save(); return
    print("[nyq2] NYQ-CONTROL-2 COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
