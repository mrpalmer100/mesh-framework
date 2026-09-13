"""GR54-A -- 4/3 displacement replication at 144x54 (charter
analysis/GR54A_charter_LOCKED.md). GR54 driver, cell 4/3, 20 pts.

GR54 -- 54-grid profile replication (charter
analysis/GR54_charter_LOCKED.md). Phase 1: phi-continue profile s0,
s1 to 144x54 (S3R rule, a2 pins, 60-round budgets). Phase 2: the
stage-2c arc protocol verbatim at 54 from that pair -- ds=0.08, 12
points, full gates, sealed measurements. One unit of progress per
invocation; rerun to advance. SJ_MEMO=jac.
"""
import numpy as np, pickle, pathlib, sys, time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations.s3r_replication import phi_zeropad    # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = pathlib.Path('/tmp/gr54a_ckpt.pkl')
DUR = ROOT / 'analysis' / 'gr54a_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
PROF = ROOT / 'analysis' / 'qsweep_stage2c_ckpt.pkl'
NS, NP = 144, 54
N = NS * NP
DS = 0.08
BUDGET = 20   # GR54-X extension (charter analysis/GR54X_charter_LOCKED.md)


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.startswith('gr54') \
                    and k.endswith('|solve'):
                super().__setitem__(k + '-cum',
                                    self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    prof = pickle.loads(PROF.read_bytes())
    S36 = prof['prof-4/3']['states']
    T36 = q1.QTGrid(144, 36, 3, 4)
    T54 = q1.QTGrid(144, 54, 3, 4)

    # ---- Phase 1: seed pair continuations (s0, s1 -> 54)
    for which, idx in (('s0', 2), ('s1', 3)):
        key = f'gr54a|{which}'
        rec = st.get(key, {})
        if rec.get('done'):
            continue
        x36 = np.asarray(S36[idx], float)
        _, c2 = T36.modes(T36.geom(x36)[2])
        pin = float(abs(c2))
        if 'x0' not in rec:
            rec = dict(pin=pin, x0=phi_zeropad(x36, 144, 36, 54),
                       done=False)
            st[key] = rec
            print(f"[{key}] seed built. pin {pin:.7f}", flush=True)
        sj, _ = SJ.make_instrument(T54, np.asarray(rec['x0'], float),
                                   'a2', pin, 50.0, cache=str(PAT))
        bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
        xn = SJ.gn_sparse(T54, np.asarray(rec['x0'], float), 'a2',
                          pin, sj, bs, rounds=60, st=st,
                          key=key + '|solve')
        m, ok = q1.gate(T54, xn, key, pin=pin)
        if ok:
            rec = dict(st[key])
            rec.update(done=True, x=xn, metrics=m)
            st[key] = rec
            DUR.write_bytes(pickle.dumps(dict(st)))
            print(f"[{key}] ** GATED ** RMS {m['rms']:.1e} clos "
                  f"{m['clos']:.1e}", flush=True)
        else:
            cum = st.get(key + '|solve-cum', 0)
            if cum >= 60:
                rec = dict(st[key])
                rec.update(done=True, x=None, refused=True,
                           metrics=m)
                st[key] = rec
                DUR.write_bytes(pickle.dumps(dict(st)))
                print(f"[{key}] ** REFUSED at budget **", flush=True)
            else:
                print(f"[{key}] not gated (cum {cum}) -- resume",
                      flush=True)
        return

    if st['gr54a|s0'].get('refused') or st['gr54a|s1'].get('refused'):
        print("[gr54a] seed continuation refused -- GR-OPEN path; "
              "stop and record.", flush=True)
        return

    # ---- Phase 2: arc profile at 54
    rec = st.setdefault('gr54aprof', dict(states=[], meas=[]))
    if not rec['states']:
        rec['states'] = [np.asarray(st['gr54a|s0']['x'], float),
                         np.asarray(st['gr54a|s1']['x'], float)]
        st['gr54aprof'] = rec
    if len(rec['meas']) >= BUDGET:
        print("[gr54a] PROFILE COMPLETE -- run the verdict "
              "ONCE.", flush=True)
        return
    i = len(rec['meas'])
    xa, xb = rec['states'][-2], rec['states'][-1]
    t = xb - xa
    t /= np.linalg.norm(t)
    sj, _ = SJ.make_instrument(T54, xb, 'arc', (xb, t, DS), 50.0,
                               cache=str(PAT))
    bs = SJ.BandedTorusSolver(NS, NP, nglob=2)
    xn = SJ.gn_sparse(T54, xb + DS * t, 'arc', (xb, t, DS), sj, bs,
                      rounds=60, st=st, key=f'gr54a|p{i}|solve')
    r = T54.field_rms(xn)
    clos = T54.closure_max(xn)
    if not (r < q1.RMS_BAR and clos < q1.CLOSURE_BAR):
        cum = st.get(f'gr54a|p{i}|solve-cum', 0)
        if cum >= 60:
            rec['halt'] = f'point {i} refused (RMS {r:.1e})'
            st['gr54aprof'] = rec
            DUR.write_bytes(pickle.dumps(dict(st)))
            print(f"[gr54a p{i}] ** REFUSED at budget ** recorded.",
                  flush=True)
        else:
            print(f"[gr54a p{i}] not gated (cum {cum}) -- resume",
                  flush=True)
        return
    _, c2p = T54.modes(T54.geom(xb)[2])
    _, c2n = T54.modes(T54.geom(xn)[2])
    dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi
    dx = xn - xb
    m = dict(A2=float((abs(c2n) + abs(c2p)) / 2),
             rate=float((abs(c2n) - abs(c2p)) / DS),
             vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS),
             fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
             rms=float(r), clos=float(clos))
    rec['meas'].append(m)
    rec['states'].append(xn)
    st['gr54aprof'] = rec
    DUR.write_bytes(pickle.dumps(dict(st)))
    print(f"[gr54a p{i}] GATED  A2 {m['A2']:.7f}  (measurements "
          f"sealed)", flush=True)


if __name__ == '__main__':
    main()
