"""Q54 GRID RIDER (charter analysis/Q54_charter_LOCKED.md, runs
after the column verdict): phi-continue the profile's deep pair
(states s10, s11) to 144x54 via the S3R protocol verbatim --
phi-only FFT zero-pad seed, a2 pin at each member's OWN A2,
SJ-CREDENTIALED instrument, full stage-1 bars. B36 = 0.9332 at
c* = 17 already computed (>= 0.30: rider live). After both members
resolve, the verdict step computes B54 (band 16..18 pt mass of the
54 tangent) and H54 (19..27) against the locked lines. SJ_MEMO=jac;
peak ~2.7 GB per C4. One member per completion; rerun to advance.
"""
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
CKPT = pathlib.Path('/tmp/q54rider_ckpt.pkl')
DUR = ROOT / 'analysis' / 'q54_rider_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
PROF = ROOT / 'analysis' / 'q54_profile_ckpt.pkl'
BUDGET = 60


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    prof = pickle.loads(PROF.read_bytes())
    S = prof['prof-5/4']['states']
    T36 = q1.QTGrid(144, 36, 4, 5)
    T54 = q1.QTGrid(144, 54, 4, 5)

    for which, idx in (('prev', -2), ('deep', -1)):
        key = f'q54rider|{which}'
        rec = st.get(key, {})
        if rec.get('done'):
            continue
        x36 = np.asarray(S[idx], float)
        _, c2 = T36.modes(T36.geom(x36)[2])
        pin = float(abs(c2))
        if 'x0' not in rec:
            rec = dict(pin=pin, x0=phi_zeropad(x36, 144, 36, 54),
                       done=False)
            st[key] = rec
            print(f"[{key}] seed built. pin A2 = {pin:.7f}  seed "
                  f"RMS {T54.field_rms(rec['x0']):.2e}", flush=True)
        assert abs(rec['pin'] - pin) < 1e-12
        sj, _ = SJ.make_instrument(T54, np.asarray(rec['x0'], float),
                                   'a2', pin, 50.0, cache=str(PAT))
        bs = SJ.BandedTorusSolver(144, 54, nglob=2)
        xn = SJ.gn_sparse(T54, np.asarray(rec['x0'], float), 'a2',
                          pin, sj, bs, rounds=BUDGET, st=st,
                          key=key + '|solve')
        m, ok = q1.gate(T54, xn, key, pin=pin)
        rounds = st.get(key + '|solve-cum', None) or \
            st.get(key + '|solve', {}).get('it', -1)
        if ok:
            rec = dict(st[key])
            rec.update(done=True, outcome='GATED', x=xn, metrics=m)
            st[key] = rec
            DUR.write_bytes(pickle.dumps(dict(st)))
            print(f"[{key}] ** GATED **  RMS {m['rms']:.1e}  clos "
                  f"{m['clos']:.1e}", flush=True)
        else:
            it = st.get(key + '|solve', {}).get('it', -1)
            if it >= BUDGET - 1:
                rec = dict(st[key])
                rec.update(done=True, outcome='REFUSED', x=xn,
                           metrics=m)
                st[key] = rec
                DUR.write_bytes(pickle.dumps(dict(st)))
                print(f"[{key}] ** REFUSED at budget ** -- recorded,"
                      f" evidence-bearing.", flush=True)
            else:
                print(f"[{key}] not gated this chunk (it {it}) -- "
                      f"resume", flush=True)
        return

    print("[q54rider] BOTH MEMBERS RESOLVED -- run the rider verdict"
          " step (B54, H54 vs locked lines).", flush=True)


if __name__ == '__main__':
    main()
