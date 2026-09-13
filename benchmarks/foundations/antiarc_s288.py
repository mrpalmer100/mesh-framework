"""COMMISSION ANTI-ARC-S288 -- the anti-aligned 5/4 family with s refined 2x (288 x 36).
Charter analysis/ANTIARC_S288_charter_LOCKED.md. Seed pair = ANTI-ARC's sealed p0/p1
(144x36) s-zero-padded to 288 (the S3R phi rule transposed), a2-pinned at their own A2,
gated at the q-sweep bars; the resolution bar wsNyq <= 1e-4 is RECORDED per seed (the
verdict script applies it). Then the stage-2c arc march at ds 0.08 on 288x36 for 20
points, measurements SEALED. One unit of work per invocation; checkpoint
analysis/antiarc_s288_ckpt.pkl. Terminal line: 'ANTI-ARC-S288 COMPLETE -- run the verdict'.
Run AFTER Leg B finishes (memory). Cheaper per round than 144x54: the banded cost scales
with the phi count (36), not the s count."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antiarc_s288_ckpt.pkl'
SRC = ROOT / 'analysis' / 'antiarc_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'     # the cache file; new 288x36 patterns are added to it
DS, NPTS, N1, N2 = 0.08, 20, 4, 5
NS0, NS1, NP = 144, 288, 36


def _pad_s(F, NS1):
    C = np.fft.rfft(F, axis=0)
    C1 = np.zeros((NS1 // 2 + 1, F.shape[1]), complex)
    C1[:C.shape[0], :] = C
    return np.fft.irfft(C1, n=NS1, axis=0) * (NS1 / F.shape[0])


def s_zeropad(x, NS0, NS1, NP):
    """spectral zero-padding along s (axis 0); the phase field (f = 1) is unwrapped along s,
    its integer winding trend removed, padded, and the trend restored on the new grid --
    the S3R phi rule transposed to s."""
    N0, N1 = NS0 * NP, NS1 * NP
    out = np.empty(3 * N1 + 2); out[-2:] = x[-2:]
    for f in range(3):
        F = x[f * N0:(f + 1) * N0].reshape(NS0, NP)
        if f == 1:
            Fu = np.unwrap(F, axis=0)
            k = np.round((Fu[-1, :] - Fu[0, :]) / (2 * np.pi) * NS0 / (NS0 - 1))
            tr0 = (np.arange(NS0)[:, None] / NS0) * 2 * np.pi * k[None, :]
            G = _pad_s(Fu - tr0, NS1) + (np.arange(NS1)[:, None] / NS1) * 2 * np.pi * k[None, :]
        else:
            G = _pad_s(F, NS1)
        out[f * N1:(f + 1) * N1] = G.ravel()
    return out


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
    mm = q1.metrics(T, xn)
    m = dict(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float((abs(c2n) - abs(c2p)) / DS),
             vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS), fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
             rms=float(r), clos=float(clos), om2=float(T.geom(xn)[10]), nyq=float(mm['nyq']))
    return (xn, m), r, 0


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.startswith('s288|') and not k.endswith('-cum') and not k.endswith('-lastw'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v); _atomic_write(CKPT, pickle.dumps(dict(self)))
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    T = q1.QTGrid(NS1, NP, N1, N2); T36 = q1.QTGrid(NS0, NP, N1, N2)
    P = st.setdefault('prof', dict(states=[], meas=[], halt=None))
    seeds = st.setdefault('seeds', {})
    if len(P['states']) < 2 and not P['halt']:
        src = pickle.loads(SRC.read_bytes())['prof']['states']
        for which, idx in (('s0', 2), ('s1', 3)):
            if which in seeds and seeds[which].get('done'): continue
            x36 = np.asarray(src[idx], float); _, c2 = T36.modes(T36.geom(x36)[2]); pin = float(abs(c2))
            rec = seeds.setdefault(which, dict(pin=pin, x0=s_zeropad(x36, NS0, NS1, NP), done=False))
            if which == 's0' and 's0' not in st.get('seeds', {}) or not rec.get('checked'):
                m0 = q1.metrics(T, np.asarray(rec['x0'], float))
                print(f"[s288] {which} after s-pad: A2 {m0['A2']:.7f} (36: {pin:.7f}) RMS {m0['rms']:.1e} wsNyq {m0['nyq']:.1e} om2 {m0['om2']:+.6f}", flush=True)
                rec['checked'] = True; st['seeds'] = seeds
            key = f's288|{which}'; cum = st.get(key + '-cum', 0)
            seed = np.asarray(st[key]['x'], float) if key in st else np.asarray(rec['x0'], float)
            sj, _ = SJ.make_instrument(T, np.asarray(rec['x0'], float), 'a2', pin, 50.0, cache=str(PAT))
            bs = SJ.BandedTorusSolver(NS1, NP, nglob=2)
            xn = SJ.gn_sparse(T, seed, 'a2', pin, sj, bs, rounds=max(1, 60 - cum), st=st, key=key)
            m, ok = q1.gate(T, xn, f's288 {which}', pin=pin)
            if ok:
                rec.update(done=True, x=xn, nyq=float(m['nyq']), om2=float(m['om2']), rms=float(m['rms'])); st['seeds'] = seeds
                print(f"[s288] {which} GATED at 288x36: A2 {pin:.7f} om2 {m['om2']:+.6f} RMS {m['rms']:.1e} wsNyq {m['nyq']:.1e} "
                      f"[resolution bar 1e-4: {'MET' if m['nyq'] <= 1e-4 else 'NOT met'}]", flush=True)
            elif st.get(key + '-cum', 0) >= 60:
                P['halt'] = f'{which} refused at 288'; st['prof'] = P; print(f"[s288] ANTI-ARC-S288 REFUSED ({which})", flush=True)
            return
        P['states'] = [np.asarray(seeds['s0']['x'], float), np.asarray(seeds['s1']['x'], float)]; st['prof'] = P
        print("[s288] seed pair gated; arc march begins", flush=True); return
    if P['halt']:
        print("[s288] ANTI-ARC-S288 COMPLETE -- run the verdict (halted early)", flush=True); return
    i = len(P['meas'])
    if i >= NPTS:
        print("[s288] ANTI-ARC-S288 COMPLETE -- run the verdict", flush=True); return
    res, r, cum = arc_point(T, st, f's288|p{i}', P['states'][-2], P['states'][-1])
    if res is None:
        if cum >= 60:
            P['halt'] = f'p{i} refused'; st['prof'] = P; print(f"[s288] point {i} REFUSED", flush=True)
        return
    P['states'].append(res[0]); P['meas'].append(res[1]); st['prof'] = P
    print(f"[s288 p{i}] GATED  A2 {res[1]['A2']:.7f}  wsNyq {res[1]['nyq']:.1e}  (measurements sealed)", flush=True)


if __name__ == '__main__':
    main()
