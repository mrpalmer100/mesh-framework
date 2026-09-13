"""Q54 stage 1 on the SJ-CREDENTIALED instrument (charter
Amendment 1, analysis/Q54_charter_LOCKED.md; spot-bar v2 PASS on
record). run_q's ramp REPLICATED VERBATIM -- same seeds, sub-pin
ladder fractions, rung persistence, waypoint amplitudes, fine pin,
budgets, and gates -- with gn_sparse in place of gn_lean (the
fault-7/8 lesson: this file was diffed against run_q line-by-line;
any divergence is a ledger fault). Rates (arc marches) follow in
the profile driver. Resumable; rerun until members + fine exist.
Durable export analysis/q54_stage1_ckpt.pkl."""
import numpy as np, pickle, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1     # noqa
from benchmarks.foundations import sparsej_instrument as SJ  # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
DUR = ROOT / 'analysis' / 'q54_stage1_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
QTAG = 'q5/4'


def sparse_solve(T, seed, pin, rounds, st, key, stop_rms=None,
                 hard_cap=None):
    # Effective-round budgets under chunked execution: the
    # registered dense runs resume past nominal per-invocation
    # budgets (the 96x36 diagnostic's rung 1 took ~35 effective
    # rounds), so a hard cap at the nominal figure is STRICTER
    # than protocol and hands weak states up the ladder. A rung
    # closes on stop_rms, on frozen-no-progress (wres unchanged
    # across an invocation after >= nominal rounds), or at 4x
    # nominal as a hard ceiling.
    ck = key + '-cum'
    fk = key + '-lastw'
    cum = st.get(ck, 0)
    cap = hard_cap if hard_cap is not None else 4 * rounds
    if cum >= cap:
        return np.asarray(st[key]['x'], float)
    if cum >= rounds and key in st:
        import numpy as _np
        w = float(_np.linalg.norm(T.wres(
            _np.asarray(st[key]['x'], float), 'a2', pin, 50.0)))
        if abs(w - st.get(fk, -1.0)) < 1e-12:
            return _np.asarray(st[key]['x'], float)   # frozen: close
        st[fk] = w
    sj, _ = SJ.make_instrument(T, seed, 'a2', pin, 50.0,
                               cache=str(PAT))
    bs = SJ.BandedTorusSolver(T.NS, T.NP, nglob=2)
    return SJ.gn_sparse(T, seed, 'a2', pin, sj, bs,
                        rounds=max(1, cap - cum),
                        st=st, key=key, stop_rms=stop_rms)


def main():
    class PersistDict(dict):
        # per-round persistence (the reap-window pattern from
        # sparsej_c3/S3R): gn_sparse writes st[key] each round.
        # The '-sj' keys also feed a cumulative round counter so
        # rung budgets are enforced ACROSS chunks.
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.endswith('-sj'):
                super().__setitem__(k + '-cum', self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v)
            q1._atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(q1.load())
    T = q1.QTGrid(144, 36, 4, 5)
    q = st.setdefault(QTAG, {})
    if q.get('halt'):
        print(f"== {QTAG} previously halted: {q['halt']} ==", flush=True)
        return
    assert 'l1' in q, 'level-1 must exist (dense, on record)'

    q.setdefault('members', [])
    x = q['members'][-1]['x'] if q['members'] else None
    while len(q['members']) < len(q1.WAYPOINTS):
        A2 = q1.WAYPOINTS[len(q['members'])]
        print(f"  [{QTAG}] ramp pin A2 = {A2:.7f} (sparse, Amendment 1)",
              flush=True)
        if x is None:
            xw = None
            for frac in (0.15, 0.3, 0.55, 0.8):
                rk = f'{QTAG}-rung{frac}-done'
                if rk in st:
                    xw = st[rk]
                    continue
                sub = frac * A2
                seed = q1.ramp_seed(T, sub) if xw is None else xw
                print(f"    [sub-pin {sub:.7f}]", flush=True)
                xw = sparse_solve(T, seed, sub, 10, st,
                                  f'{QTAG}-ramp0-sub{frac}-sj',
                                  stop_rms=1e-5)
                st[rk] = xw
                q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            seed = xw
        else:
            base = q1.metrics(T, x)['A2']
            xw = x
            for frac in (0.4, 0.7):
                sub = base + frac * (A2 - base)
                rk = f'{QTAG}-w{len(q["members"])}rung{frac}-done'
                if rk in st:
                    xw = st[rk]
                    continue
                print(f"    [sub-pin {sub:.7f}]", flush=True)
                xw = sparse_solve(T, xw, sub, 12, st,
                                  f'{QTAG}-w{len(q["members"])}'
                                  f'-sub{frac}-sj', stop_rms=1e-5)
                st[rk] = xw
                q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            seed = xw
        xn = sparse_solve(T, seed, A2, 60, st,
                          f'{QTAG}-ramp{len(q["members"])}-sj')
        m, ok = q1.gate(T, xn, f'{QTAG} A2 = {A2:.7f}', pin=A2)
        if not ok:
            r = st.get(f'{QTAG}-ramp{len(q["members"])}-sj-cum', 0)
            if r >= 60:
                m['x'] = xn
                q['members'].append(m)
                q['halt'] = f'gates at waypoint {A2:.7f}'
                q1.CKPT.write_bytes(pickle.dumps(dict(st)))
                print(f"  [{QTAG}] waypoint REFUSED at budget -- "
                      f"recorded, kept.", flush=True)
                return
            q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            print(f"  [{QTAG}] waypoint not gated this chunk "
                  f"(round {r}) -- resume", flush=True)
            return
        m['x'] = xn
        q['members'].append(m)
        q1.CKPT.write_bytes(pickle.dumps(dict(st)))
        DUR.write_bytes(pickle.dumps(
            {k: v for k, v in q.items() if k != 'l1'}))
        print(f"  [{QTAG}] waypoint {len(q['members'])} ** GATED ** "
              f"A2 {m['A2']:.7f} om2 {m['om2']:.5f}", flush=True)
        x = xn
        return              # one waypoint per completion; rerun

    if 'fine' not in q:
        print(f"  [{QTAG}] fine pin A2 = {q1.FINE_PIN:.7f} (sparse)",
              flush=True)
        base = q1.metrics(T, q['members'][-1]['x'])['A2']
        xw = q['members'][-1]['x']
        for frac in (0.4, 0.7):
            sub = base + frac * (q1.FINE_PIN - base)
            rk = f'{QTAG}-finerung{frac}-done'
            if rk in st:
                xw = st[rk]
                continue
            print(f"    [sub-pin {sub:.7f}]", flush=True)
            xw = sparse_solve(T, xw, sub, 12, st,
                              f'{QTAG}-fine-sub{frac}-sj',
                              stop_rms=1e-5)
            st[rk] = xw
            q1.CKPT.write_bytes(pickle.dumps(dict(st)))
        xn = sparse_solve(T, xw, q1.FINE_PIN, 60, st, f'{QTAG}-fine-sj',
                          hard_cap=60)
        m, ok = q1.gate(T, xn, f'{QTAG} A2 = {q1.FINE_PIN:.7f}',
                        pin=q1.FINE_PIN)
        r = st.get(f'{QTAG}-fine-sj-cum', 0)
        if ok:
            m['x'] = xn
            q['fine'] = m
            q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            DUR.write_bytes(pickle.dumps(
                {k: v for k, v in q.items() if k != 'l1'}))
            print(f"  [{QTAG}] fine pin ** GATED **", flush=True)
        elif r >= 60:
            q['fine'] = None            # registered fallback: arc march
            q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            print(f"  [{QTAG}] fine pin did not land at member grade "
                  f"(registered near-singularity class); arc-march "
                  f"fallback per protocol.", flush=True)
        else:
            q1.CKPT.write_bytes(pickle.dumps(dict(st)))
            print(f"  [{QTAG}] fine not gated this chunk (round {r})"
                  f" -- resume", flush=True)
        return

    print(f"[{QTAG}] STAGE-1 SOLVES COMPLETE -- rates next "
          f"(arc marches, profile driver).", flush=True)


if __name__ == '__main__':
    main()
