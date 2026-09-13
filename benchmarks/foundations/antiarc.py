"""COMMISSION ANTI-ARC -- the anti-aligned family marched (charter
analysis/ANTIARC_charter_LOCKED.md). s0 = FND-173's polished 5/4 anti-aligned member;
s1 = a2-pinned continuation at 1.02 x A2 (om2 free, full bars); then the registered
stage-2c arc protocol at ds = 0.08 on 144x36 for 12 points, measurements SEALED.
One unit of work per invocation; checkpoint analysis/antiarc_ckpt.pkl; SJ_MEMO=jac in the
session, 1 locally. Terminal line: 'ANTI-ARC COMPLETE -- run the verdict'."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import truestate_stage2 as S2         # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antiarc_ckpt.pkl'
SRC = ROOT / 'analysis' / 'antialigned_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
DS, NPTS, N1, N2 = 0.08, 20, 4, 5


def arc_point(T, st, key, xa, xb):
    N = T.NS * T.NP
    t = xb - xa; t /= np.linalg.norm(t)
    sj, _ = SJ.make_instrument(T, xb, 'arc', (xb, t, DS), 50.0, cache=str(PAT))
    bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    xn = SJ.gn_sparse(T, xb + DS * t, 'arc', (xb, t, DS), sj, bs, rounds=60, st=st, key=key)
    r = T.field_rms(xn); clos = T.closure_max(xn)
    ok = r < q1.RMS_BAR and clos < q1.CLOSURE_BAR
    if not ok:
        return None, r, st.get(key + '-cum', 0)
    _, c2p = T.modes(T.geom(xb)[2]); _, c2n = T.modes(T.geom(xn)[2])
    dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi; dx = xn - xb
    m = dict(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float((abs(c2n) - abs(c2p)) / DS),
             vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS), fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
             rms=float(r), clos=float(clos), om2=float(T.geom(xn)[10]))
    return (xn, m), r, 0


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.startswith('ar|') and not k.endswith('-cum') and not k.endswith('-lastw'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v); _atomic_write(CKPT, pickle.dumps(dict(self)))
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    T = q1.QTGrid(144, 36, N1, N2)
    P = st.setdefault('prof', dict(states=[], meas=[], halt=None))
    if not P['states']:
        src = pickle.loads(SRC.read_bytes())['d3|5/4|anti|polished']
        s0 = np.asarray(src['x'], float); _, c2 = T.modes(T.geom(s0)[2]); A2 = abs(c2)
        print(f"[antiarc] s0 = FND-173 polished member: A2 {A2:.7f} om2 {T.geom(s0)[10]:+.6f} RMS {T.field_rms(s0,'a2',A2):.1e}", flush=True)
        pin1 = 1.02 * A2; key = 'ar|s1'
        cum = st.get(key + '-cum', 0)
        seed = np.asarray(st[key]['x'], float) if key in st else s0
        sj, _ = SJ.make_instrument(T, s0, 'a2', pin1, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(144, 36, nglob=2)
        xn = SJ.gn_sparse(T, seed, 'a2', pin1, sj, bs, rounds=max(1, 60 - cum), st=st, key=key)
        m, ok = q1.gate(T, xn, 'antiarc s1', pin=pin1)
        if ok:
            P['states'] = [s0, xn]; st['prof'] = P; print(f"[antiarc] s1 GATED A2 {pin1:.7f} om2 {m['om2']:+.6f}", flush=True)
        elif st.get(key + '-cum', 0) >= 60:
            P['halt'] = 's1 refused'; st['prof'] = P; print("[antiarc] ANTI-ARC REFUSED (s1)", flush=True)
        return
    if P['halt']:
        print("[antiarc] ANTI-ARC COMPLETE -- run the verdict (halted early)", flush=True); return
    i = len(P['meas'])
    if i >= NPTS:
        print("[antiarc] ANTI-ARC COMPLETE -- run the verdict", flush=True); return
    res, r, cum = arc_point(T, st, f'ar|p{i}', P['states'][-2], P['states'][-1])
    if res is None:
        if cum >= 60:
            P['halt'] = f'p{i} refused'; st['prof'] = P; print(f"[antiarc] point {i} REFUSED", flush=True)
        return
    P['states'].append(res[0]); P['meas'].append(res[1]); st['prof'] = P
    print(f"[antiarc p{i}] GATED  A2 {res[1]['A2']:.7f}  (measurements sealed)", flush=True)


if __name__ == '__main__':
    main()
