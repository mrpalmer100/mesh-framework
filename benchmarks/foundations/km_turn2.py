"""COMMISSION KM-TURN-2 (charter analysis/KM_TURN2_charter_LOCKED.md): continue the resonant
branch R across the crossing at A2 ~0.00733. Seed = sealed KERNEL-MARCH p44 -> p45; the FIRST
point uses a 3 ds predictor/arc step (charter amendment) to land beyond the singular point; then
the ordinary bordered arc march at ds 0.08 for 11 more points; plain-solver control every 4th
point. One unit of work per invocation; checkpoint analysis/km_turn2_ckpt.pkl (atomic writes).
Terminal line: 'KM-TURN-2 COMPLETE -- run the verdict'. Executed 2026-09-22..23 (sealed)."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import kernel_continuation as KC      # noqa
from benchmarks.foundations.kernel_march import kernel_dir, measure   # noqa


def _atomic_write(path, data):
    import os
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_bytes(data); os.replace(tmp, path)


ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'km_turn2_ckpt.pkl'
SRC = ROOT / 'analysis' / 'kernel_march_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
NS, NP, N1, N2 = 288, 36, 4, 5
DS, NPTS, ROUNDS = 0.08, 12, 60
SEED = (44, 45)


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    T = q1.QTGrid(NS, NP, N1, N2)
    P = st.setdefault('prof', dict(states=[], meas=[], halt=None, arc={}))
    if not P['states']:
        src = pickle.loads(SRC.read_bytes())['prof']['states']
        P['states'] = [np.asarray(src[2 + SEED[0]], float), np.asarray(src[2 + SEED[1]], float)]; save()
        print(f"[turn2] seeded from sealed p{SEED[0]} -> p{SEED[1]} (R below the crossing); first step 3 ds", flush=True); return
    if P['halt']:
        print("[turn2] KM-TURN-2 COMPLETE -- run the verdict (halted early)", flush=True); return
    i = len(P['meas'])
    if i >= NPTS:
        print("[turn2] KM-TURN-2 COMPLETE -- run the verdict", flush=True); return
    R = P['arc'].setdefault(f'p{i}', dict(hist=[], done=False))
    xa, xb = np.asarray(P['states'][-2], float), np.asarray(P['states'][-1], float)
    t = xb - xa; t /= np.linalg.norm(t)
    ds = 3 * DS if i == 0 else DS                    # the first step is 3 ds (charter amendment)
    aux = (xb, t, ds); xp = xb + ds * t
    sj, _ = SJ.make_instrument(T, xb, 'arc', aux, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
    if 'c' not in R:
        _, c2 = T.modes(T.geom(xp)[2]); c, sig, _ = kernel_dir(T, xp, float(abs(c2)), 'arc', aux); R.update(c=c, sigma=sig, x=xp); save(); return
    x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), None, np.asarray(R['c'], float), 0.0, xp, sj, bs, rounds=1, log=lambda s: None, pin_mode='arc', aux=aux)
    R['x'] = x; R['hist'] += hist
    rms = float(T.field_rms(x)); clos = float(T.closure_max(x)); gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
    if gated:
        m = measure(T, xb, x, ds); m['sigma'] = R['sigma']; m['ds'] = ds
        if (i + 1) % 4 == 0:
            xg = SJ.gn_sparse(T, x, 'arc', aux, sj, bs, rounds=10, st={}, key=f'gnctl{i}')
            m['rms_gn'] = float(T.field_rms(xg)); m['gn_gates'] = bool(m['rms_gn'] < q1.RMS_BAR and T.closure_max(xg) < q1.CLOSURE_BAR)
        P['states'].append(x); P['meas'].append(m); R['done'] = True; save()
        on = 'R' if (m['rate'] > 1.15e-3 and m['fdir'] > 0.53) else ('N' if (m['rate'] < 1.15e-3 and m['fdir'] < 0.53) else '?')
        extra = f"  GN-control rms {m['rms_gn']:.1e} {'GATES' if m['gn_gates'] else 'floors'}" if 'rms_gn' in m else ''
        print(f"[turn2 p{i}] GATED  A2 {m['A2']:.7f}  rate {m['rate']:+.3e}  f_dir {m['fdir']:.4f}  om2 {m['om2']:+.6f}  on {on}{extra}  (sealed)", flush=True); return
    if len(R['hist']) >= ROUNDS or hist == []:
        R['done'] = True; P['halt'] = f'p{i} refused'; save()
        print(f"[turn2] point {i} REFUSED (RMS {rms:.1e} after {len(R['hist'])} rounds)", flush=True); return
    save()


if __name__ == '__main__':
    main()
