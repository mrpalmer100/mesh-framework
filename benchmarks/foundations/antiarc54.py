"""COMMISSION ANTI-ARC-54 -- the anti-aligned 5/4 family at 144x54 (charter
analysis/ANTIARC54_charter_LOCKED.md). Seed pair = ANTI-ARC's sealed p0/p1 states
phi-continued to 54 (S3R rule), a2-pinned at their own A2, full bars; then the stage-2c
arc march at ds 0.08 on 144x54 for 20 points, measurements SEALED. One unit of work per
invocation; checkpoint analysis/antiarc54_ckpt.pkl. Terminal line:
'ANTI-ARC-54 COMPLETE -- run the verdict'."""
import numpy as np, pickle, pathlib, sys

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
CKPT = ROOT / 'analysis' / 'antiarc54_ckpt.pkl'
SRC = ROOT / 'analysis' / 'antiarc_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'     # the cache also holds the 144x54 patterns (Q54/GR54)
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
            if isinstance(k, str) and k.startswith('a54|') and not k.endswith('-cum') and not k.endswith('-lastw'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v); _atomic_write(CKPT, pickle.dumps(dict(self)))
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    T54 = q1.QTGrid(144, 54, N1, N2); T36 = q1.QTGrid(144, 36, N1, N2)
    P = st.setdefault('prof', dict(states=[], meas=[], halt=None))
    seeds = st.setdefault('seeds', {})
    if len(P['states']) < 2 and not P['halt']:
        src = pickle.loads(SRC.read_bytes())['prof']['states']
        for which, idx in (('s0', 2), ('s1', 3)):                  # ANTI-ARC's sealed p0 and p1 states
            if which in seeds and seeds[which].get('done'): continue
            x36 = np.asarray(src[idx], float); _, c2 = T36.modes(T36.geom(x36)[2]); pin = float(abs(c2))
            rec = seeds.setdefault(which, dict(pin=pin, x0=phi_zeropad(x36, 144, 36, 54), done=False))
            key = f'a54|{which}'; cum = st.get(key + '-cum', 0)
            seed = np.asarray(st[key]['x'], float) if key in st else np.asarray(rec['x0'], float)
            sj, _ = SJ.make_instrument(T54, np.asarray(rec['x0'], float), 'a2', pin, 50.0, cache=str(PAT))
            bs = SJ.BandedTorusSolver(144, 54, nglob=2)
            xn = SJ.gn_sparse(T54, seed, 'a2', pin, sj, bs, rounds=max(1, 60 - cum), st=st, key=key)
            m, ok = q1.gate(T54, xn, f'antiarc54 {which}', pin=pin)
            if ok:
                rec.update(done=True, x=xn); st['seeds'] = seeds
                print(f"[antiarc54] {which} GATED at 54: A2 {pin:.7f} om2 {m['om2']:+.6f} RMS {m['rms']:.1e}", flush=True)
            elif st.get(key + '-cum', 0) >= 60:
                P['halt'] = f'{which} refused at 54'; st['prof'] = P; print(f"[antiarc54] ANTI-ARC-54 REFUSED ({which})", flush=True)
            return
        P['states'] = [np.asarray(seeds['s0']['x'], float), np.asarray(seeds['s1']['x'], float)]; st['prof'] = P
        print("[antiarc54] seed pair gated at 54; arc march begins", flush=True); return
    if P['halt']:
        print("[antiarc54] ANTI-ARC-54 COMPLETE -- run the verdict (halted early)", flush=True); return
    i = len(P['meas'])
    if i >= NPTS:
        print("[antiarc54] ANTI-ARC-54 COMPLETE -- run the verdict", flush=True); return
    res, r, cum = arc_point(T54, st, f'a54|p{i}', P['states'][-2], P['states'][-1])
    if res is None:
        if cum >= 60:
            P['halt'] = f'p{i} refused'; st['prof'] = P; print(f"[antiarc54] point {i} REFUSED", flush=True)
        return
    P['states'].append(res[0]); P['meas'].append(res[1]); st['prof'] = P
    print(f"[antiarc54 p{i}] GATED  A2 {res[1]['A2']:.7f}  (measurements sealed)", flush=True)


if __name__ == '__main__':
    main()
