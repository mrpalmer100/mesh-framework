"""COMPOSITE-SELECT Leg B -- the rational ladder (charter D3, gating amendment).
Cells at the registered density 48 s-points per sqrt3 (NS = 48 N1), NP = 36 then 54:
  below 1.492: 7/5, 10/7, 13/9 ; above: 8/5, 11/7, 14/9 (N1 = 9 conditional on memory).
Per cell, phases (one unit of work per invocation; resumable; SJ_MEMO=jac):
  l1      level-1 seed + registered level-1 check (v2)
  ramp    the run_q ramp VERBATIM as ported in q54_stage1_sparse (sub-pin ladder
          0.15/0.3/0.55/0.8, protocol-faithful rung budgets, two gated waypoints)
  prof36  stage-2c arc profile from the waypoint pair, ds 0.08, 20 points, sealed
  cont54  phi-continue prof36's s0/s1 to NP = 54 (S3R rule, a2 pins, full bars)
  prof54  arc profile at 54, ds 0.08, 20 points, sealed
Statistics (D by nearest-point pairing at 0.0048 / 0.0063, A2_max, om2 at matched A2,
C1 f_dir rise) are computed by the verdict script, never printed here.
Checkpoint analysis/composite_legB_ckpt.pkl. Fresh pattern per (grid, mode, cell) at a
non-degenerate state (faults 9/10/11).
"""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import truestate_stage2 as S2         # noqa
from benchmarks.foundations.s3r_replication import phi_zeropad    # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'composite_legB_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
CELLS = [('7/5', 5, 7), ('8/5', 5, 8), ('10/7', 7, 10), ('11/7', 7, 11), ('13/9', 9, 13), ('14/9', 9, 14)]
DS, NPTS = 0.08, 20
ORDER = ['l1', 'ramp', 'prof36', 'cont54', 'prof54']


def sparse_solve(T, seed, pin, rounds, st, key, stop_rms=None, hard_cap=None):
    """q54_stage1_sparse.sparse_solve, verbatim semantics (frozen-close, 4x nominal ceiling)."""
    ck, fk = key + '-cum', key + '-lastw'
    cum = st.get(ck, 0); cap = hard_cap if hard_cap is not None else 4 * rounds
    if cum >= cap:
        return np.asarray(st[key]['x'], float)
    if cum >= rounds and key in st:
        w = float(np.linalg.norm(T.wres(np.asarray(st[key]['x'], float), 'a2', pin, 50.0)))
        if abs(w - st.get(fk, -1.0)) < 1e-12:
            return np.asarray(st[key]['x'], float)
        st[fk] = w
    sj, _ = SJ.make_instrument(T, seed, 'a2', pin, 50.0, cache=str(PAT))
    bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    return SJ.gn_sparse(T, seed, 'a2', pin, sj, bs, rounds=max(1, cap - cum), st=st, key=key, stop_rms=stop_rms)


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
            if isinstance(k, str) and k.startswith('lb|') and not k.endswith('-cum') and not k.endswith('-lastw'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))
    st = PersistDict(pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {})
    for tag, N1, N2 in CELLS:
        NS = 48 * N1
        c = st.setdefault(f'cell|{tag}', dict(phase='l1', members=[], prof36=dict(states=[], meas=[]),
                                             cont54={}, prof54=dict(states=[], meas=[]), halt=None))
        if c['halt'] or c['phase'] == 'done':
            continue
        T36 = q1.QTGrid(NS, 36, N1, N2)
        print(f"== cell {tag}  grid {NS}x36  phase {c['phase']} ==", flush=True)
        if c['phase'] == 'l1':
            x0 = q1.level1_seed(T36)
            ok = q1.level1_check(T36, x0, f'{tag} l1')
            c['l1'] = dict(x=x0, ok=bool(ok)); c['phase'] = 'ramp' if ok else 'l1'
            if not ok: c['halt'] = 'level-1 check failed'
            st[f'cell|{tag}'] = c; return
        if c['phase'] == 'ramp':
            x = c['members'][-1]['x'] if c['members'] else None
            A2 = q1.WAYPOINTS[len(c['members'])]
            key = f'lb|{tag}|ramp{len(c["members"])}'
            if x is None:
                xw = None
                for frac in (0.15, 0.3, 0.55, 0.8):
                    sub = frac * A2
                    if f'{key}|rung{frac}' in st: xw = np.asarray(st[f'{key}|rung{frac}'], float); continue
                    seed = q1.ramp_seed(T36, sub) if xw is None else xw
                    xw = sparse_solve(T36, seed, sub, 10, st, f'{key}|sub{frac}', stop_rms=1e-5)
                    st[f'{key}|rung{frac}'] = xw; return
            else:
                xw = None
                for frac in (0.4, 0.7):
                    sub = abs(c['members'][-1]['A2']) + frac * (A2 - abs(c['members'][-1]['A2']))
                    if f'{key}|rung{frac}' in st: xw = np.asarray(st[f'{key}|rung{frac}'], float); continue
                    xw = sparse_solve(T36, xw if xw is not None else np.asarray(x, float), sub, 10, st, f'{key}|sub{frac}', stop_rms=1e-5)
                    st[f'{key}|rung{frac}'] = xw; return
            xn = sparse_solve(T36, xw, A2, 60, st, f'{key}|gate', hard_cap=60)
            m, ok = q1.gate(T36, xn, f'{tag} A2 = {A2:.7f}', pin=A2)
            if ok:
                m['x'] = xn; c['members'].append(m)
                if len(c['members']) == len(q1.WAYPOINTS): c['phase'] = 'prof36'
            elif st.get(f'{key}|gate-cum', 0) >= 60:
                c['halt'] = f'waypoint {A2:.7f} refused'
            st[f'cell|{tag}'] = c; return
        if c['phase'] == 'prof36':
            P = c['prof36']
            if not P['states']:
                P['states'] = [np.asarray(c['members'][0]['x'], float), np.asarray(c['members'][1]['x'], float)]
            i = len(P['meas'])
            if i >= NPTS: c['phase'] = 'cont54'; st[f'cell|{tag}'] = c; return
            res, r, cum = arc_point(T36, st, f'lb|{tag}|p36|{i}', P['states'][-2], P['states'][-1])
            if res is None:
                if cum >= 60: P['halt'] = f'p{i} refused'; c['phase'] = 'cont54'
                st[f'cell|{tag}'] = c; return
            P['states'].append(res[0]); P['meas'].append(res[1]); st[f'cell|{tag}'] = c
            print(f"  [{tag} p36 {i}] GATED A2 {res[1]['A2']:.7f} (sealed)", flush=True); return
        if c['phase'] == 'cont54':
            T54 = q1.QTGrid(NS, 54, N1, N2); S = c['prof36']['states']
            for which, idx in (('s0', 2), ('s1', 3)):
                if which in c['cont54'] and c['cont54'][which].get('done'): continue
                x36 = np.asarray(S[idx], float); _, c2 = T36.modes(T36.geom(x36)[2]); pin = float(abs(c2))
                rec = c['cont54'].setdefault(which, dict(pin=pin, x0=phi_zeropad(x36, NS, 36, 54), done=False))
                xn = sparse_solve(T54, np.asarray(rec['x0'], float), pin, 60, st, f'lb|{tag}|c54|{which}', hard_cap=60)
                m, ok = q1.gate(T54, xn, f'{tag} 54 {which}', pin=pin)
                if ok: rec.update(done=True, x=xn)
                elif st.get(f'lb|{tag}|c54|{which}-cum', 0) >= 60: rec.update(done=True, x=None, refused=True)
                st[f'cell|{tag}'] = c; return
            if any(c['cont54'][w].get('refused') for w in ('s0', 's1')):
                c['halt'] = '54 continuation refused'; st[f'cell|{tag}'] = c; return
            c['phase'] = 'prof54'; st[f'cell|{tag}'] = c; return
        if c['phase'] == 'prof54':
            T54 = q1.QTGrid(NS, 54, N1, N2); P = c['prof54']
            if not P['states']:
                P['states'] = [np.asarray(c['cont54']['s0']['x'], float), np.asarray(c['cont54']['s1']['x'], float)]
            i = len(P['meas'])
            if i >= NPTS: c['phase'] = 'done'; st[f'cell|{tag}'] = c; return
            res, r, cum = arc_point(T54, st, f'lb|{tag}|p54|{i}', P['states'][-2], P['states'][-1])
            if res is None:
                if cum >= 60: P['halt'] = f'p{i} refused'; c['phase'] = 'done'
                st[f'cell|{tag}'] = c; return
            P['states'].append(res[0]); P['meas'].append(res[1]); st[f'cell|{tag}'] = c
            print(f"  [{tag} p54 {i}] GATED A2 {res[1]['A2']:.7f} (sealed)", flush=True); return
    print("[legB] LADDER COMPLETE -- run the QB verdict", flush=True)


if __name__ == '__main__':
    main()
