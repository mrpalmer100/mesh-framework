"""COMMISSION KERNEL-CONT driver (charter analysis/KERNEL_CONT_charter_LOCKED.md).
Stage A: 144x36 cell 4/3 anti-aligned floored state; controls c1 (b = 0 reproduces the GN
floor) and c2 (an aligned member gates unchanged under the bordered solve at b = 0); the b
sweep with bisection. Stage B: 288x36 cell 5/4, the S288 s0 state. One unit of work per
invocation (one bordered ROUND); checkpoint analysis/kernel_cont_ckpt.pkl. Run AFTER Leg B
(memory). Terminal line: 'KERNEL-CONT COMPLETE -- run the verdict'."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import truestate_stage2 as S2         # noqa
from benchmarks.foundations import kernel_continuation as KC      # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'kernel_cont_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
SWEEP = [-0.20, -0.10, -0.05, 0.05, 0.10, 0.20, 0.30]
ROUNDS = 40
STAGES = {
    'A': dict(grid=(144, 36), cell=(3, 4), src=('analysis/antialigned_ckpt.pkl', 'aa|4/3|anti|-0.35|gate', 'x'),
              ctrl=('analysis/qsweep_stage1_ckpt.pkl', None)),
    'B': dict(grid=(288, 36), cell=(4, 5), src=('analysis/antiarc_s288_ckpt.pkl', 's288|s0', 'x'), ctrl=None),
}


def load_state(spec):
    f, k, fld = spec; d = pickle.loads((ROOT / f).read_bytes()); return np.asarray(d[k][fld], float)


def setup(T, x, pin):
    """near-null direction at the floored state; injection direction and phase partner excluded."""
    import scipy.sparse as sp
    G = T.G2; iom = len(x) - 1; om2 = float(T.geom(x)[10])
    W, Z, Tf, gam, om1 = G.level1(); ph = np.exp(1j * G.K2 * G.sgrid)[:, None] * np.exp(-1j * G.pgrid)[None, :]
    x0 = T.from_stage2(G.pack(W, Z, Tf, gam, om1, om2))
    e2 = T.from_stage2(G.pack(W + pin * ph, Z, Tf, gam, om1, om2)) - x0; e2[iom] = 0; e2 /= np.linalg.norm(e2)
    e2p = T.from_stage2(G.pack(W + pin * 1j * ph, Z, Tf, gam, om1, om2)) - x0; e2p[iom] = 0; e2p -= (e2p @ e2) * e2; e2p /= np.linalg.norm(e2p)
    sj, _ = SJ.make_instrument(T, x, 'a2', pin, 50.0, cache=str(PAT)); J, _ = sj(x, 'a2', pin, 50.0); J = sp.csr_matrix(J)
    c, sig = KC.near_null(T, J, x, iom, exclude=(e2, e2p))
    return c, sig


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    for stage in ('A', 'B'):
        S = st.setdefault(stage, {}); spec = STAGES[stage]
        if S.get('done'): continue
        NS, NP = spec['grid']; N1, N2 = spec['cell']; T = q1.QTGrid(NS, NP, N1, N2)
        if 'x_floor' not in S:
            x = load_state(spec['src']); m = q1.metrics(T, x); pin = float(m['A2'])
            S.update(x_floor=x, pin=pin, rms_floor=float(m['rms']), om2_floor=float(m['om2']))
            c, sig = setup(T, x, pin); S.update(c=c, sigma=float(sig)); save()
            print(f"[kc {stage}] floored state RMS {m['rms']:.2e} om2 {m['om2']:+.6f} pin {pin:.7f}; near-null |Jc|/row {sig:.2e}", flush=True)
            if sig > 1e-3:
                S.update(done=True, verdict='KC-REFUSED'); save(); print(f"[kc {stage}] KC-REFUSED (no near-null direction)", flush=True)
            return
        x_floor = np.asarray(S['x_floor'], float); pin = S['pin']; c = np.asarray(S['c'], float)
        sj, _ = SJ.make_instrument(T, x_floor, 'a2', pin, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        # control c1 (b = 0), then the sweep, then a bisection level
        plan = [0.0] + SWEEP + S.get('bisect', [])
        for b in plan:
            key = f'b={b:+.3f}'; R = S.setdefault('runs', {}).setdefault(key, dict(b=b, x=x_floor, hist=[], done=False))
            if R['done']: continue
            x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), pin, c, b, x_floor, sj, bs, rounds=1, log=lambda s: None)
            R['x'] = x; R['hist'] += hist
            rms = float(T.field_rms(x, 'a2', pin)); clos = float(T.closure_max(x)); om2 = float(T.geom(x)[10])
            R.update(rms=rms, clos=clos, om2=om2)
            gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
            if gated or len(R['hist']) >= ROUNDS or (hist == [] and len(R['hist']) > 0):
                R['done'] = True; R['gated'] = bool(gated)
                print(f"[kc {stage} {key}] {'GATED' if gated else 'floor'} RMS {rms:.2e} clos {clos:.1e} om2 {om2:+.6f} rounds {len(R['hist'])}", flush=True)
            save(); return
        if 'bisect' not in S:
            done = {k: v for k, v in S['runs'].items() if v['done'] and v['b'] != 0.0}
            best = sorted(done.values(), key=lambda v: v['rms'])[:2]
            if len(best) == 2:
                lo, hi = sorted(v['b'] for v in best); S['bisect'] = [lo + (hi - lo) / 3, lo + 2 * (hi - lo) / 3]
                save(); print(f"[kc {stage}] bisecting between b {lo:+.3f} and {hi:+.3f}", flush=True); return
        S['done'] = True; S['verdict'] = 'see verdict script'; save()
        print(f"[kc {stage}] stage complete", flush=True); return
    print("[kc] KERNEL-CONT COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
