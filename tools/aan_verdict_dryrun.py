"""Dry run of benchmarks/foundations/antiarc_nyq_verdict.py against synthetic checkpoints shaped as antiarc_nyq.py writes them
(2026-10-04, before the PC run completed). Ten forms read correctly; the eleventh fixture (a halted point without the
driver's halt flag) is a state the driver cannot write and the verdict rightly refuses it as non-terminal. Run from the repo root."""
import pickle, pathlib, sys, io, contextlib, numpy as np
import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from benchmarks.foundations import antiarc_nyq_verdict as V
n = 2 * 144 * 36 + 2
def m(rms=5e-9, clos=1e-8, nyq=1e-7, A2=0.002, fdir=0.77, rounds=10, halt=False):
    d = dict(rms=rms, clos=clos, nyq=nyq, A2=A2, om2=-1.1106, rate=2.1e-3, vpt=1e-2, fdir=fdir, rounds=rounds,
             gated_rc=rms < 1e-8 and clos < 1e-6)
    d['gated_clean'] = d['gated_rc'] and nyq <= 1e-4
    if halt: d['halt'] = True
    return d
def arm(points, states_n):
    rng = np.random.default_rng(0)
    return dict(states=[rng.normal(size=n) for _ in range(states_n)], meas=points, halt=None)
def ckpt(c1_nyq=8.7e-4, c1_rms=8e-10, c2_clean=(True, True), s1_halt=None, A1=None, A2=None):
    st = {'c1': dict(x0=np.zeros(n), x=np.zeros(n), pin=0.002, m0=m(rms=c1_rms, nyq=c1_nyq), m=m(rms=c1_rms, nyq=c1_nyq), rounds=1)}
    for arm_, ok in zip(('A1', 'A2'), c2_clean):
        st[f'c2{arm_}'] = dict(done=True, m=m(nyq=1e-9 if ok else 5e-3), s1m=m(), s1=np.zeros(n), x=np.zeros(n), halt=None)
    st['seeds'] = dict(s0=np.zeros(n), s1=np.zeros(n), s1m=m(nyq=8e-4), halt=s1_halt)
    if A1 is not None: st['A1'] = A1
    if A2 is not None: st['A2'] = A2
    return st
def run(name, st, expect):
    p = pathlib.Path(f'/tmp/aan_dry_{name}.pkl'); p.write_bytes(pickle.dumps(st))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): v = V.main(p)
    ok = (v == expect) or (expect in str(v))
    print(f"{'PASS' if ok else 'FAIL'}  {name:24s} expected {expect:22s} got {v}")
    if not ok: print(buf.getvalue()[-1500:])
    return ok
flat_clean = [m(nyq=5e-5, A2=0.0020 + 0.0002 * i, fdir=0.77 + 0.001 * i) for i in range(20)]      # A2_max 0.0058, rise 0.019
flat_nyq = [m(nyq=8e-4, A2=0.0020 + 0.0002 * i, fdir=0.77 + 0.001 * i) for i in range(20)]
collapse_clean = [m(nyq=5e-5, A2=0.0020 + 0.0002 * i, fdir=0.11 + 0.012 * i) for i in range(20)]  # rise 0.228
refused = [m(rms=1e-6, nyq=8e-4, halt=True)]
short_clean = [m(nyq=5e-5, A2=0.0020 + 0.0001 * i, fdir=0.77) for i in range(20)]                  # A2_max 0.0039 < licence
R = []
R.append(run('flat_clean_A2_only', ckpt(A1=arm(flat_nyq, 22), A2=arm(flat_clean, 22)), 'ANTI-FLAT-CLEAN'))
R.append(run('flat_clean_both', ckpt(A1=arm(flat_clean, 22), A2=arm(flat_clean, 22)), 'ANTI-FLAT-CLEAN'))
R.append(run('collapse_clean', ckpt(A1=arm(flat_nyq, 22), A2=arm(collapse_clean, 22)), 'ANTI-COLLAPSE-CLEAN'))
R.append(run('flat_nyq', ckpt(A1=arm(flat_nyq, 22), A2=arm(refused, 2)), 'ANTI-FLAT-NYQ'))
a2h = arm(refused, 2); a2h['halt'] = 'p0 refused'
R.append(run('flat_nyq_A2_halted', ckpt(A1=arm(flat_nyq, 22), A2=a2h), 'ANTI-FLAT-NYQ'))
a1h = arm(refused, 2); a1h['halt'] = 'p0 refused'
R.append(run('refused_both', ckpt(A1=a1h, A2=a2h), 'ANTI-NYQ-REFUSED'))
R.append(run('control_fail_c2', ckpt(c2_clean=(True, False), A1=arm(flat_nyq, 22), A2=arm(flat_clean, 22)), 'ANTI-NYQ-CONTROL-FAIL'))
R.append(run('control_fail_c1', ckpt(c1_rms=1e-6, A1=arm(flat_nyq, 22), A2=arm(flat_clean, 22)), 'ANTI-NYQ-CONTROL-FAIL'))
R.append(run('s1_refused', ckpt(s1_halt='s1 refused'), 'ANTI-NYQ-REFUSED'))
R.append(run('provisional_scope', ckpt(A1=arm(flat_nyq, 22), A2=arm(short_clean, 22)), 'provisional'))
R.append(run('incomplete', ckpt(A1=arm(flat_nyq[:5], 7), A2=arm(flat_clean, 22)), 'INCOMPLETE'))
print(f"{sum(R)}/{len(R)} forms read correctly")
