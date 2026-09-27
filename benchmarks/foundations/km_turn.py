"""COMMISSION KM-TURN (charter analysis/KM_TURN_charter_LOCKED.md). Two tests on the PC:
  A: backward BORDERED arc march from the sealed p51 -> p50 states (tangent reversed), 12 points.
  B: forward PLAIN-GN arc march from the sealed p38 -> p39 states, 15 points, through the turn.
One unit of work per invocation; checkpoint analysis/km_turn_ckpt.pkl (atomic writes).
Terminal line: 'KM-TURN COMPLETE -- run the verdict'. Executed 2026-09-19..22 (sealed record kept)."""
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
CKPT = ROOT / 'analysis' / 'km_turn_ckpt.pkl'
SRC = ROOT / 'analysis' / 'kernel_march_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
NS, NP, N1, N2 = 288, 36, 4, 5
DS, ROUNDS = 0.08, 60
TESTS = {'A': dict(seed=(51, 50), npts=12, solver='bordered'),
         'B': dict(seed=(38, 39), npts=15, solver='gn')}


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    def save(): _atomic_write(CKPT, pickle.dumps(st))
    T = q1.QTGrid(NS, NP, N1, N2)
    src = pickle.loads(SRC.read_bytes())['prof']['states']
    for name, spec in TESTS.items():
        P = st.setdefault(name, dict(states=[], meas=[], halt=None, arc={}))
        if not P['states']:
            a, b = spec['seed']; P['states'] = [np.asarray(src[2 + a], float), np.asarray(src[2 + b], float)]; save()
            print(f"[turn {name}] seeded from sealed p{a} -> p{b} ({spec['solver']})", flush=True); return
        if P['halt']: continue
        i = len(P['meas'])
        if i >= spec['npts']: continue
        R = P['arc'].setdefault(f'p{i}', dict(hist=[], done=False))
        xa, xb = np.asarray(P['states'][-2], float), np.asarray(P['states'][-1], float)
        t = xb - xa; t /= np.linalg.norm(t); aux = (xb, t, DS); xp = xb + DS * t
        sj, _ = SJ.make_instrument(T, xb, 'arc', aux, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        if spec['solver'] == 'bordered':
            if 'c' not in R:
                _, c2 = T.modes(T.geom(xp)[2]); c, sig, _ = kernel_dir(T, xp, float(abs(c2)), 'arc', aux); R.update(c=c, sigma=sig, x=xp); save(); return
            x, hist = KC.bordered_gn(T, np.asarray(R['x'], float), None, np.asarray(R['c'], float), 0.0, xp, sj, bs, rounds=1, log=lambda s: None, pin_mode='arc', aux=aux)
            R['x'] = x; R['hist'] += hist; used = len(R['hist']); stalled = (hist == [])
        else:
            gst = R.setdefault('gst', {})
            x = SJ.gn_sparse(T, np.asarray(R.get('x', xp), float), 'arc', aux, sj, bs, rounds=1, st=gst, key='g')
            R['x'] = x; R['hist'].append(1); used = len(R['hist']); stalled = False
        rms = float(T.field_rms(x)); clos = float(T.closure_max(x)); gated = rms < q1.RMS_BAR and clos < q1.CLOSURE_BAR
        if gated:
            m = measure(T, xb, x, DS)
            if spec['solver'] == 'bordered': m['sigma'] = R['sigma']
            P['states'].append(x); P['meas'].append(m); R['done'] = True; save()
            print(f"[turn {name} p{i}] GATED  A2 {m['A2']:.7f}  rate {m['rate']:+.3e}  f_dir {m['fdir']:.4f}  om2 {m['om2']:+.6f}  (sealed)", flush=True); return
        if used >= ROUNDS or stalled:
            R['done'] = True; P['halt'] = f'p{i} refused'; save(); print(f"[turn {name}] point {i} REFUSED (RMS {rms:.1e} after {used} rounds)", flush=True); return
        save(); return
    print("[turn] KM-TURN COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
