"""COMMISSION ANTI-ARC-NYQ (charter analysis/ANTIARC_NYQ_charter_LOCKED.md, locked 2026-10-04).
The registered stage-2c arc march of FND-174 (antiarc.py: ds 0.08, 144x36 cell 5/4, the
credentialed sparse instrument, plain Gauss-Newton) re-run with the gate's Nyquist flag as a BAR
(wsNyq <= 1e-4), in two arms: A1 the march verbatim; A2 the same march with every GN step
projected onto s-harmonics |k| <= NS/3 (kernel_continuation.dealias_s, through gn_sparse's
inert `project` hook). Controls: c1 FND-173's polished member re-gated in place by plain GN
(its wsNyq read for the first time against a bar); c2 one aligned stage-2c arc point from the
registered 4/3 waypoint-1 member under A1 and under A2. One unit of work per invocation
(a control solve, a seed, or one arc point of up to 60 rounds, resumable through the sparse
instrument's own persistence); atomic checkpoint analysis/antiarc_nyq_ckpt.pkl; per-point
measurements SEALED. Terminal line: 'ANTI-ARC-NYQ COMPLETE -- run the verdict'.
Shakedown (recorded, 2026-10-04): the first PC invocation accepted the aligned s1 seed on RMS/closure alone, so gn_sparse's
5-percent pin stop returned the unmoved member, the seed pair was identical and the arc tangent divided by zero.
antiarc.py gates s1 with q1.gate(pin=...) (PIN_TOL 1e-8); restored here, plus a hard refusal on a zero tangent.
The checkpoint from that invocation was discarded (c1 only; no arc point existed)."""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import kernel_continuation as KC      # noqa  (dealias_s only)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antiarc_nyq_ckpt.pkl'
SRC_ANTI = ROOT / 'analysis' / 'antialigned_ckpt.pkl'
SRC_ALIGNED = ROOT / 'analysis' / 'qsweep_stage1_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
DS, NPTS, NYQ_BAR = 0.08, 20, 1e-4
CELLS = {'anti': (4, 5), 'aligned': (3, 4)}


def _atomic_write(path, data):
    import os
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_bytes(data); os.replace(tmp, path)


class PersistDict(dict):
    def __setitem__(self, k, v):
        if isinstance(k, str) and k.startswith('sj|') and not k.endswith('-cum'):
            super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
        super().__setitem__(k, v); _atomic_write(CKPT, pickle.dumps(dict(self)))


def proj_for(T, arm):
    return (lambda dx: KC.dealias_s(T, dx)) if arm == 'A2' else None


def read(T, x, pin=None):
    m = q1.metrics(T, x)
    m['gated_rc'] = bool(m['rms'] < q1.RMS_BAR and m['clos'] < q1.CLOSURE_BAR)
    m['gated_clean'] = bool(m['gated_rc'] and m['nyq'] <= NYQ_BAR)
    return m


def solve_a2(T, st, key, seed, pin, arm, rounds=60):
    sj, _ = SJ.make_instrument(T, seed, 'a2', pin, 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    cum = st.get(key + '-cum', 0)
    x = SJ.gn_sparse(T, seed, 'a2', pin, sj, bs, rounds=max(1, rounds - cum), st=st, key=key, project=proj_for(T, arm))
    return x, st.get(key + '-cum', 0)


def arc_point(T, st, key, xa, xb, arm):
    N = T.NS * T.NP
    t = xb - xa; nt = float(np.linalg.norm(t))
    if nt == 0.0:
        raise SystemExit(f"[aan {key}] seed pair identical (|xb - xa| = 0); refusing to march from a degenerate tangent")
    t /= nt
    sj, _ = SJ.make_instrument(T, xb, 'arc', (xb, t, DS), 50.0, cache=str(PAT)); bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    cum = st.get(key + '-cum', 0)
    xn = SJ.gn_sparse(T, xb + DS * t, 'arc', (xb, t, DS), sj, bs, rounds=max(1, 60 - cum), st=st, key=key, project=proj_for(T, arm))
    m = read(T, xn); cum = st.get(key + '-cum', 0)
    if not m['gated_rc']:
        return None, m, cum
    _, c2p = T.modes(T.geom(xb)[2]); _, c2n = T.modes(T.geom(xn)[2])
    dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi; dx = xn - xb
    m.update(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float((abs(c2n) - abs(c2p)) / DS),
             vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS), fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)), rounds=cum)
    return xn, m, cum


def main():
    import shutil
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < 2.0:                                   # 2026-10-04: the PC filled up mid-write (745 MB free); refuse to start rather than die inside a checkpoint write
        print(f"[aan] REFUSING TO START: {free_gb:.2f} GB free on the drive holding {ROOT}; free at least 2 GB and rerun (the checkpoint is intact; atomic writes)", flush=True)
        raise SystemExit(2)
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    Ta = q1.QTGrid(144, 36, *CELLS['anti']); Tl = q1.QTGrid(144, 36, *CELLS['aligned'])
    # ---- c1: FND-173's polished member re-gated in place (plain GN, 20 rounds) ----
    if 'c1' not in st:
        s0 = np.asarray(pickle.loads(SRC_ANTI.read_bytes())['d3|5/4|anti|polished']['x'], float)
        m0 = read(Ta, s0); pin = m0['A2']
        x, cum = solve_a2(Ta, st, 'sj|c1', s0, pin, 'A1', rounds=20); m = read(Ta, x)
        if m['gated_rc'] or cum >= 20:
            st['c1'] = dict(x=x, x0=s0, pin=pin, m0=m0, m=m, rounds=cum)
            print(f"[aan c1] FND-173 member: as stored RMS {m0['rms']:.1e} clos {m0['clos']:.1e} wsNyq {m0['nyq']:.1e}; re-gated RMS {m['rms']:.1e} clos {m['clos']:.1e} wsNyq {m['nyq']:.1e} om2 {m['om2']:+.6f} rounds {cum}; gated_rc {m['gated_rc']} gated_clean {m['gated_clean']}", flush=True)
        return
    # ---- c2: aligned waypoint-1 member, s1 at 1.02 A2, one arc point; under A1 and A2 ----
    for arm in ('A1', 'A2'):
        key = f'c2{arm}'
        if key in st and st[key].get('done'): continue
        R = st.setdefault(key, dict(done=False))
        a0 = np.asarray(pickle.loads(SRC_ALIGNED.read_bytes())['q4/3']['members'][0]['x'], float)
        if 's1' not in R:
            pin1 = 1.02 * read(Tl, a0)['A2']
            x, cum = solve_a2(Tl, st, f'sj|{key}|s1', a0, pin1, arm); m = read(Tl, x)
            _, ok = q1.gate(Tl, x, f'aan {key} s1', pin=pin1)       # as antiarc.py: the pin is part of the gate (PIN_TOL)
            if ok: R['s1'] = x; R['s1m'] = m; st[key] = R; print(f"[aan {key}] aligned s1 gated at pin {pin1:.7f}: RMS {m['rms']:.1e} wsNyq {m['nyq']:.1e} rounds {cum}", flush=True)
            elif cum >= 60: R.update(done=True, s1m=m, halt='s1 refused'); st[key] = R; print(f"[aan {key}] aligned s1 REFUSED", flush=True)
            return
        xn, m, cum = arc_point(Tl, st, f'sj|{key}|p0', a0, np.asarray(R['s1'], float), arm)
        if xn is not None or cum >= 60:
            R.update(done=True, m=m, x=xn, halt=None if xn is not None else 'p0 refused'); st[key] = R
            print(f"[aan {key}] aligned arc point: RMS {m['rms']:.1e} clos {m['clos']:.1e} wsNyq {m['nyq']:.1e} gated_clean {m['gated_clean']} rounds {cum}", flush=True)
        return
    # ---- seeds s0, s1 for the anti-aligned march (shared by both arms; s1 under plain GN) ----
    if 'seeds' not in st:
        s0 = np.asarray(st['c1']['x0'], float); pin1 = 1.02 * read(Ta, s0)['A2']
        x, cum = solve_a2(Ta, st, 'sj|s1', s0, pin1, 'A1'); m = read(Ta, x)
        _, ok = q1.gate(Ta, x, 'aan s1', pin=pin1)                   # as antiarc.py
        if ok:
            st['seeds'] = dict(s0=s0, s1=x, s1m=m); print(f"[aan seeds] s1 gated A2 {pin1:.7f} RMS {m['rms']:.1e} wsNyq {m['nyq']:.1e} om2 {m['om2']:+.6f}", flush=True)
        elif cum >= 60:
            st['seeds'] = dict(s0=s0, s1=None, s1m=m, halt='s1 refused'); print("[aan seeds] s1 REFUSED", flush=True)
        return
    if st['seeds'].get('halt'):
        print("[aan] ANTI-ARC-NYQ COMPLETE -- run the verdict (s1 refused)", flush=True); return
    # ---- arms ----
    for arm in ('A1', 'A2'):
        P = st.setdefault(arm, dict(states=[np.asarray(st['seeds']['s0'], float), np.asarray(st['seeds']['s1'], float)], meas=[], halt=None))
        if P['halt'] or len(P['meas']) >= NPTS: continue
        i = len(P['meas'])
        xn, m, cum = arc_point(Ta, st, f'sj|{arm}|p{i}', P['states'][-2], P['states'][-1], arm)
        if xn is None:
            if cum >= 60:
                P['halt'] = f'p{i} refused'; P['meas'].append(dict(m, halt=True)); st[arm] = P
                print(f"[aan {arm} p{i}] REFUSED (RMS {m['rms']:.1e} after 60 rounds)", flush=True)
            return
        P['states'].append(xn); P['meas'].append(m); st[arm] = P
        print(f"[aan {arm} p{i}] gated_rc; wsNyq {m['nyq']:.1e} {'CLEAN' if m['gated_clean'] else 'over bar'}; A2 {m['A2']:.7f} (other measurements sealed) rounds {cum}", flush=True)
        return
    print("[aan] ANTI-ARC-NYQ COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
