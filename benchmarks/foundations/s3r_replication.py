"""S3R -- stage-3 replication at 144x54 (charter:
analysis/S3R_charter_LOCKED.md, locked before any solve).

Four solves in the charter's order: 5/3 prev, 5/3 deep, 4/3 prev,
4/3 deep. Each: phi-only FFT zero-pad seed (FND-160 rule), a2 pin
at the member's own A2, stage-1 full gates, 60-round budget on the
SJ-CREDENTIALED instrument. Reap-window chunked; rerun until done.
Checkpoint /tmp/s3r_ckpt.pkl; durable export
analysis/s3r_ckpt.pkl updated at every gate/refusal. Run with
SJ_MEMO=jac. Adjudicates nothing here: gates and refusals only;
the locked statistic runs in the charter's verdict step after the
required members exist.
"""
import numpy as np, pickle, pathlib, sys, time, resource

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
CKPT = pathlib.Path('/tmp/s3r_ckpt.pkl')
DUR = ROOT / 'analysis' / 's3r_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
S2C = ROOT / 'analysis' / 'qsweep_stage2c_ckpt.pkl'
BUDGET = 60
ORDER = [('5/3', 11, 'prev'), ('5/3', 12, 'deep'),
         ('4/3', 11, 'prev'), ('4/3', 12, 'deep')]


def phi_zeropad(x, NS, NP0, NP1):
    N0, N1 = NS * NP0, NS * NP1
    out = np.empty(3 * N1 + 2)
    out[-2:] = x[-2:]
    for f in range(3):
        F = x[f * N0:(f + 1) * N0].reshape(NS, NP0)
        if f == 1:
            Fu = np.unwrap(F, axis=1)
            k = np.round((Fu[:, -1] - Fu[:, 0]) /
                         (2 * np.pi) * NP0 / (NP0 - 1))
            tr0 = (np.arange(NP0)[None, :] / NP0) * 2 * np.pi * k[:, None]
            G = _pad(Fu - tr0, NP1) + \
                (np.arange(NP1)[None, :] / NP1) * 2 * np.pi * k[:, None]
        else:
            G = _pad(F, NP1)
        out[f * N1:(f + 1) * N1] = G.ravel()
    return out


def _pad(F, NP1):
    C = np.fft.rfft(F, axis=1)
    C1 = np.zeros((F.shape[0], NP1 // 2 + 1), complex)
    C1[:, :C.shape[1]] = C
    return np.fft.irfft(C1, n=NP1, axis=1) * (NP1 / F.shape[1])


def main():
    class PersistDict(dict):
        def __setitem__(self, k, v):
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    s2c = pickle.loads(S2C.read_bytes())

    for cell, idx, which in ORDER:
        key = f's3r|{cell}|{which}'
        rec = st.get(key, {})
        if rec.get('done'):
            continue
        n2 = {'4/3': 4, '5/3': 5}[cell]
        T54 = q1.QTGrid(144, 54, 3, n2)
        T36 = q1.QTGrid(144, 36, 3, n2)
        x36 = np.asarray(s2c[f'prof-{cell}']['states'][idx], float)
        _, c2 = T36.modes(T36.geom(x36)[2])
        pin = float(abs(c2))
        if 'x0' not in rec:
            rec = dict(pin=pin, x0=phi_zeropad(x36, 144, 36, 54),
                       done=False)
            st[key] = rec
            print(f"[{key}] seed built. pin A2 = {pin:.7f}  seed RMS "
                  f"{T54.field_rms(rec['x0']):.2e}", flush=True)
        assert abs(rec['pin'] - pin) < 1e-12

        sj, _ = SJ.make_instrument(T54, rec['x0'], 'a2', pin, 50.0,
                                   cache=str(PAT))
        bs = SJ.BandedTorusSolver(144, 54, nglob=2)
        xn = SJ.gn_sparse(T54, rec['x0'], 'a2', pin, sj, bs,
                          rounds=BUDGET, st=st, key=key + '|solve')
        m, ok = q1.gate(T54, xn, key, pin=pin)
        rounds = st.get(key + '|solve', {}).get('it', -1)
        if ok:
            rec = dict(st[key]); rec.update(done=True, outcome='GATED',
                                            x=xn, metrics=m)
            st[key] = rec
            DUR.write_bytes(pickle.dumps(dict(st)))
            print(f"[{key}] ** GATED **. Durable export written. "
                  f"Next member on rerun.", flush=True)
        else:
            if rounds >= BUDGET - 1:
                rec = dict(st[key]); rec.update(done=True,
                                                outcome='REFUSED',
                                                x=xn, metrics=m)
                st[key] = rec
                DUR.write_bytes(pickle.dumps(dict(st)))
                print(f"[{key}] ** REFUSED at budget ** (round "
                      f"{rounds}). Recorded; evidence-bearing per "
                      f"charter. Next member on rerun.", flush=True)
            else:
                print(f"[{key}] not gated this chunk (round {rounds}"
                      f"). Resume.", flush=True)
        print(f"[s3r] peak RSS "
              f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f}"
              f" GB", flush=True)
        return          # one member per invocation path; rerun to advance

    print("[s3r] ALL FOUR MEMBERS DONE. Run the charter's verdict "
          "step (statistic on gated pairs; S3R-CRED first).",
          flush=True)


if __name__ == '__main__':
    main()
