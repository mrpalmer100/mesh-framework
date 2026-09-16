"""COMMISSION KERNEL-MARCH (charter analysis/KERNEL_MARCH_charter_LOCKED.md): the anti-aligned
5/4 family marched on 288x36 with the BORDERED solver (kernel_continuation.py) in place of GN.
s0 = FND-175's b = -0.10 member; s1 = bordered a2-pinned member at 1.02 A2; then 20 bordered arc
points at ds 0.08, the near-null direction recomputed at each predictor state, the kernel
coordinate carried along the tangent, measurements SEALED. One unit of work (one bordered ROUND)
per invocation; checkpoint analysis/kernel_march_ckpt.pkl. Terminal line:
'KERNEL-MARCH COMPLETE -- run the verdict'. Runs on the PC (python go.py ...)."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import kernel_continuation as KC      # noqa
import scipy.sparse as sp                                          # noqa


def _atomic_write(path, data):
    import os
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_bytes(data); os.replace(tmp, path)


ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'kernel_march_ckpt.pkl'
SRC = ROOT / 'analysis' / 'kernel_cont_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
NS, NP, N1, N2 = 288, 36, 4, 5
DS, NPTS, ROUNDS = 0.08, 20, 60


def kernel_dir(T, x, pin, pin_mode, aux):
    """near-null direction at state x (the (1,1) subspace; injection direction + phase partner excluded)."""
    G = T.G2; iom = len(x) - 1; om2 = float(T.geom(x)[10])
    W, Z, Tf, gam, om1 = G.level1(); ph = np.exp(1j * G.K2 * G.sgrid)[:, None] * np.exp(-1j * G.pgrid)[None, :]
    x0 = T.from_stage2(G.pack(W, Z, Tf, gam, om1, om2))
    e2 = T.from_stage2(G.pack(W + pin * ph, Z, Tf, gam, om1, om2)) - x0; e2[iom] = 0; e2 /= np.linalg.norm(e2)
    e2p = T.from_stage2(G.pack(W + pin * 1j * ph, Z, Tf, gam, om1, om2)) - x0; e2p[iom] = 0; e2p -= (e2p @ e2) * e2; e2p /= np.linalg.norm(e2p)
    sj, _ = SJ.make_instrument(T, x, pin_mode, aux, 50.0, cache=str(PAT)); J, _ = sj(x, pin_mode, aux, 50.0); J = sp.csr_matrix(J)
    c, sig = KC.near_null(T, J, x, iom, exclude=(e2, e2p))
    return c, float(sig), sj


def measure(T, xb, xn, ds):
    N = T.NS * T.NP
    _, c2p = T.modes(T.geom(xb)[2]); _, c2n = T.modes(T.geom(xn)[2])
    dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi; dx = xn - xb
    return dict(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float((abs(c2n) - abs(c2p)) / ds),
                vpt=float(np.sqrt(np.mean(dpt ** 2)) / ds), fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
                rms=float(T.field_rms(xn)), clos=float(T.closure_max(xn)), om2=float(T.geom(xn)[10]))


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    T = q1.QTGrid(NS, NP, N1, N2)
    P = st.setdefault('prof', dict(states=[], meas=[], halt=None))
    # ---- seeds -------------------------------------------------------------------------------
    if 's0' not in st:
        r = pickle.loads(SRC.read_bytes())['B']['runs']['b=-0.100']
        x = np.asarray(r['x'], float); m = q1.metrics(T, x); st['s0'] = dict(x=x, pin=float(m['A2']), rms=float(m['rms']), om2=float(m['om2'])); save()
        print(f"[km] s0 = FND-175 b=-0.10 member: A2 {m['A2']:.7f} om2 {m['om2']:+.6f} RMS {m['rms']:.1e}", flush=True); return
    if 's1' not in st or not st['s1'].get('done'):
        S1 = st.setdefault('s1', dict(pin=1.02 * st['s0']['pin'], x=st['s0']['x'], hist=[], done=False))
        x0 = np.asarray(st['s0']['x'], float)
        if 'c' not in S1:
            c, sig, _ = kernel_dir(T, x0, S1['pin'], 'a2', S1['pin']); S1.update(c=c, sigma=sig); save()
            print(f"[km] s1: kernel direction at s0 |Jc|/row {sig:.2e}; bordered a2 solve at 1.02 A2 begins", flush=True); return
        sj, _ = SJ.make_instrument(T, x0, 'a2', S1['pin'], 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        x, hist = KC.bordered_gn(T, np.asarray(S1['x'], float), S1['pin'], np.asarray(S1['c'], float), 0.0, x0, sj, bs, rounds=1, log=lambda s: None)
        S1['x'] = x; S1['hist'] += hist; m = q1.metrics(T, x)
        gated = m['rms'] < q1.RMS_BAR and m['clos'] < q1.CLOSURE_BAR
        if gated or len(S1['hist']) >= ROUNDS or hist == []:
            S1['done'] = True; S1['gated'] = bool(gated)
            if gated:
                P['states'] = [x0, x]; print(f"[km] s1 GATED: A2 {m['A2']:.7f} om2 {m['om2']:+.6f} RMS {m['rms']:.1e} (rounds {len(S1['hist'])})", flush=True)
            else:
                P['halt'] = 's1 refused'; print(f"[km] KERNEL-MARCH REFUSED (s1: RMS {m['rms']:.1e} after {len(S1['hist'])} rounds)", flush=True)
        save(); return
    if P['halt']:
        print("[km] KERNEL-MARCH COMPLETE -- run the verdict (halted early)", flush=True); return
    i = len(P['meas'])
    if i >= NPTS:
        print("[km] KERNEL-MARCH COMPLETE -- run the verdict", flush=True); return
    # ---- one bordered arc point (one round per invocation) --------------------------------------
    A = st.setdefault('arc', {}); R = A.setdefault(f'p{i}', dict(hist=[], done=False))
    xa, xb = np.asarray(P['states'][-2], float), np.asarray(P['states'][-1], float)
    t = xb - xa; t /= np.linalg.norm(t); aux = (xb, t, DS)
    if 'c' not in R:
        xp = xb + DS * t; _, c2 = T.modes(T.geom(xp)[2])
        c, sig, _ = kernel_dir(T, xp, float(abs(c2)), 'arc', aux); R.update(c=c, sigma=sig, x=xp); save(); return
    sj, _ = SJ.make_instrument(T, xb, 'arc', aux, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
    xp = xb + DS * t
    x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), None, np.asarray(R['c'], float), 0.0, xp, sj, bs, rounds=1, log=lambda s: None, pin_mode='arc', aux=aux)
    R['x'] = x; R['hist'] += hist
    rms = float(T.field_rms(x)); clos = float(T.closure_max(x)); gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
    if gated:
        m = measure(T, xb, x, DS); m['b_step'] = float(np.asarray(R['c'], float) @ (x - xb)); m['sigma'] = R['sigma']
        P['states'].append(x); P['meas'].append(m); R['done'] = True; save()
        print(f"[km p{i}] GATED  A2 {m['A2']:.7f}  sigma {R['sigma']:.1e}  (measurements sealed)", flush=True); return
    if len(R['hist']) >= ROUNDS or hist == []:
        R['done'] = True; P['halt'] = f'p{i} refused'; save()
        print(f"[km] point {i} REFUSED (RMS {rms:.1e} after {len(R['hist'])} rounds)", flush=True); return
    save()


if __name__ == '__main__':
    main()
