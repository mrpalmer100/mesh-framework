"""Q54 STAGE-2c PROFILE -- the adjudicating march (charter:
analysis/Q54_charter_LOCKED.md; Amendment 1 instrument; Amendment 2
recorded in the results doc: the separate stage-1 rates marches are
subsumed by this profile's identical arc machinery, noted before
any discriminator number existed).

VERBATIM the registered qsweep_profile.run protocol, kernels per
Amendment 1: seed pair = the two GATED Q54 waypoints (A2 0.0018792,
0.0046979 -- the same amplitudes the registered columns marched
from); ds = 0.08; budget 12 points; stage-1 full gates per point;
per-step measurements dA2/ds, V_pt, f_dir with the C3-credentialed
formulas (sparsej_c3 lineage, rates verified to 0.06 pct against
the registered 4/3 profile). Pattern: fresh (144x36, arc, n2=5),
measured at a NON-DEGENERATE arc state (fault-9/10/11 rules).
Checkpoint /tmp/q54prof_ckpt.pkl; durable export
analysis/q54_profile_ckpt.pkl per gated point. THE DISCRIMINATORS
ARE NOT COMPUTED HERE -- the verdict step runs them once, after
the profile completes or the budget exhausts. SJ_MEMO=jac.
"""
import numpy as np, pickle, pathlib, sys, time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1           # noqa
from benchmarks.foundations import sparsej_instrument as SJ      # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = pathlib.Path('/tmp/q54prof_ckpt.pkl')
DUR = ROOT / 'analysis' / 'q54_profile_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
S1 = ROOT / 'analysis' / 'q54_stage1_ckpt.pkl'
N = 144 * 36
DS = 0.08
BUDGET = 12


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            if isinstance(k, str) and k.startswith('p54-s') \
                    and not k.endswith('-cum'):
                super().__setitem__(k + '-cum',
                                    self.get(k + '-cum', 0) + 1)
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    T = q1.QTGrid(144, 36, 4, 5)
    s1 = pickle.loads(S1.read_bytes())
    rec = st.setdefault('prof-5/4', dict(states=[], meas=[]))
    if not rec['states']:
        rec['states'] = [np.asarray(s1['members'][0]['x'], float),
                         np.asarray(s1['members'][1]['x'], float)]
        st['prof-5/4'] = rec

    while len(rec['meas']) < BUDGET:
        i = len(rec['meas'])
        xa, xb = rec['states'][-2], rec['states'][-1]
        t = xb - xa
        t /= np.linalg.norm(t)
        t0 = time.time()
        sj, _ = SJ.make_instrument(T, xb, 'arc', (xb, t, DS), 50.0,
                                   cache=str(PAT))
        bs = SJ.BandedTorusSolver(144, 36, nglob=2)
        xn = SJ.gn_sparse(T, xb + DS * t, 'arc', (xb, t, DS), sj, bs,
                          rounds=60, st=st, key=f'p54-s{i}')
        r = T.field_rms(xn)
        clos = T.closure_max(xn)
        if not (r < q1.RMS_BAR and clos < q1.CLOSURE_BAR):
            rounds = st.get(f'p54-s{i}', {}).get('it', -1)
            cum = st.get(f'p54-s{i}-cum', 0)
            if cum >= 60:
                rec['halt'] = f'point {i} refused at budget ' \
                              f'(RMS {r:.1e} clos {clos:.1e})'
                st['prof-5/4'] = rec
                DUR.write_bytes(pickle.dumps(dict(st)))
                print(f"[p54 s{i}] ** REFUSED at budget ** -- "
                      f"recorded; the verdict step reads the "
                      f"profile as-is.", flush=True)
                return
            print(f"[p54 s{i}] not gated this chunk (cum {cum}) -- "
                  f"resume", flush=True)
            return
        _, c2p = T.modes(T.geom(xb)[2])
        _, c2n = T.modes(T.geom(xn)[2])
        rate = (abs(c2n) - abs(c2p)) / DS
        dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi
        dx = xn - xb
        m = dict(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float(rate),
                 vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS),
                 fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
                 rms=float(r), clos=float(clos),
                 mins=float(time.time() - t0) / 60)
        rec['meas'].append(m)
        rec['states'].append(xn)
        st['prof-5/4'] = rec
        DUR.write_bytes(pickle.dumps(dict(st)))
        print(f"[p54 s{i}] GATED  A2 {m['A2']:.7f}  (rate, vpt, fdir "
              f"recorded, sealed)", flush=True)
        return          # one point per completion; rerun to advance

    print("[p54] PROFILE COMPLETE (12 points). Run the charter's "
          "verdict step ONCE.", flush=True)


def _cum_hook():
    pass


if __name__ == '__main__':
    main()
