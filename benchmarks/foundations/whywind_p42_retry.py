"""WHYWIND p42|4/3|deep RETRY -- on the SJ-CREDENTIALED instrument.

Charter: analysis/WHYWIND_probe42_bars_LOCKED.md, UNCHANGED. This is
the single retry the WHYWIND-F clause and the approved queue action
authorize, executable here because SPARSE-J credentialed
(analysis/SPARSEJ_credential_results.md). Seed: the charter's own
rule -- phi-only FFT zero-pad 36 -> 42 of the retained deep member
(2c states[12]), s untouched; NOT the refusal session's endgame
state (it slid off its constraints; see WHYWIND_probe42_results.md).
Pin: 'a2' at the member's registered A2. Bars: stage-1 full gates
(RMS < 1e-8, closure < 1e-6, pin < 1e-8, geometry floors).
Outcome either way is the deliverable: GATED -> the locked P42
verdict lines run next; REFUSED under this full-f64 exact solve ->
evidence-bearing for state-intrinsic fragility per the charter
scope of SPARSEJ_charter_LOCKED.md, registering per WHYWIND-F.
Checkpoint /tmp/p42r_ckpt.pkl; durable export to analysis/ at any
terminal outcome. Run in reap-window chunks; SJ_MEMO=jac advised.
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
CKPT = pathlib.Path('/tmp/p42r_ckpt.pkl')
DUR = ROOT / 'analysis' / 'whywind_p42_retry_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
S2C = ROOT / 'analysis' / 'qsweep_stage2c_ckpt.pkl'
ROUND_BUDGET = 60          # the probe charter's stage-1 budget


def phi_zeropad(x, NS, NP0, NP1):
    """The charter's seed: phi-only FFT zero-pad, s untouched.
    pt handled as an angle (unwrap, carry winding trend)."""
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
    T = q1.QTGrid(144, 42, 3, 4)
    rec = pickle.loads(S2C.read_bytes())['prof-4/3']
    xdeep36 = np.asarray(rec['states'][12], float)
    _, c2 = T36_modes(xdeep36)
    pin = float(abs(c2))

    class PersistDict(dict):
        def __setitem__(self, k, v):
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    if 'pin' not in st:
        st['pin'] = pin
        st['seed_done'] = False
    assert abs(st['pin'] - pin) < 1e-12, 'pin mismatch vs checkpoint'

    if not st.get('seed_done'):
        x = phi_zeropad(xdeep36, 144, 36, 42)
        st['x0'] = x
        st['seed_done'] = True
        print(f"[p42r] seed built. pin A2 = {pin:.7f}  "
              f"seed field RMS {T.field_rms(x):.2e}", flush=True)

    sj, _ = SJ.make_instrument(T, st['x0'], 'a2', pin, 50.0,
                               cache=str(PAT))
    bs = SJ.BandedTorusSolver(144, 42, nglob=2)

    t0 = time.time()
    xn = SJ.gn_sparse(T, st['x0'], 'a2', pin, sj, bs,
                      rounds=ROUND_BUDGET, st=st, key='p42r-deep')
    m, ok = q1.gate(T, xn, 'p42r|4/3|deep', pin=pin)
    rounds_done = st.get('p42r-deep', {}).get('it', -1)
    st['last_metrics'] = m
    if ok:
        st['gated_x'] = xn
        st['outcome'] = 'GATED'
        DUR.write_bytes(pickle.dumps(dict(st)))
        print(f"[p42r] ** GATED ** on the credentialed instrument. "
              f"Durable export written. The locked P42 verdict lines "
              f"run NEXT (F17 credential on retained 144x36 states "
              f"first). Nothing computed here beyond the gate.",
              flush=True)
    else:
        print(f"[p42r] not gated at this chunk (round {rounds_done}, "
              f"{(time.time()-t0)/60:.1f} min this chunk). Resume; "
              f"refusal is declared only at the round budget with "
              f"progress stopped, mirroring the refusal protocol.",
              flush=True)
    print(f"[p42r] peak RSS "
          f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB",
          flush=True)


def T36_modes(x36):
    T36 = q1.QTGrid(144, 36, 3, 4)
    return T36.modes(T36.geom(x36)[2])


if __name__ == '__main__':
    main()
