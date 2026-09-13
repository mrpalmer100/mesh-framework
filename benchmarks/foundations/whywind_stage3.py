"""WHY-WINDING STAGE 3 (TARGETED) -- resolution replication of the
collapse mode. Executed under analysis/WHYWIND_stage3_bars_LOCKED.md.

Usage:
    python3 benchmarks/foundations/whywind_stage3.py --credential
        seed-transfer + pre-solve residual check only (no solves)
    python3 benchmarks/foundations/whywind_stage3.py [--budget SEC]
        resumable campaign: solves all six members, then renders the
        verdict mechanically. Checkpoint /tmp/s3w_ckpt.pkl; rerun to
        resume. Run detached per the house pattern:
    setsid nohup python3 benchmarks/foundations/whywind_stage3.py \
        > /tmp/s3w.log 2>&1 < /dev/null &
"""
import pathlib
import pickle
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations.qsweep_stage1 import (                # noqa: E402
    QTGrid, metrics, RMS_BAR, CLOSURE_BAR)
from benchmarks.foundations import traverse96_scout as T96        # noqa: E402


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

CK2C = pathlib.Path('analysis/qsweep_stage2c_ckpt.pkl')
CKPT = pathlib.Path('/tmp/s3w_ckpt.pkl')
CELLS = {'4/3': (3, 4), '5/3': (3, 5)}
GRIDS = {'base': (96, 36), 'probe': (96, 54)}
SRC = (144, 36)


def load():
    return pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


T96.save = save          # route the solver's checkpointing here


def bind_resumable_jac(Tn, tag):
    """Reap-proof FD Jacobian for large-dof members. (Installed
    2026-08-28 after the probe solves livelocked: the container reaps
    workers on a ~10-min cadence and the 15554-dof jac build is a
    single >5-min round, so no round ever completed. The build now
    streams column chunks into a disk memmap with a progress marker;
    a reaped build resumes at its last chunk. Numerics identical to
    TGrid96.jac: same h, same chunking, f32 store. The returned
    memmap is sliced row-wise by lm_round/gn_exact's dsyrk loops,
    which keeps RAM at the JtJ + chunk level.)"""
    import types

    def jac(self, x, pin_mode, aux, PW, chunk=256, dtype=np.float32):
        dname = np.dtype(dtype).name
        mmp = pathlib.Path(f'/home/claude/s3w_jac_{tag}_{dname}.bin')
        meta = pathlib.Path(f'/home/claude/s3w_jac_{tag}_{dname}.meta')
        for other in ('float32', 'float64'):
            if other != dname:
                pathlib.Path(
                    f'/home/claude/s3w_jac_{tag}_{other}.bin'
                ).unlink(missing_ok=True)
                pathlib.Path(
                    f'/home/claude/s3w_jac_{tag}_{other}.meta'
                ).unlink(missing_ok=True)
        h = 1e-8 * (1.0 + np.abs(x))
        r0 = self.wres(x, pin_mode, aux, PW)
        rows, n = r0.size, x.size
        sig = float(np.sum(x) + 1e-3 * np.sum(x * x))
        start = 0
        mode = 'w+'
        if mmp.exists() and meta.exists():
            try:
                s_old, a_old = meta.read_text().split()
                if abs(float(s_old) - sig) < 1e-12 * (1 + abs(sig)):
                    start, mode = int(a_old), 'r+'
            except Exception:
                pass
        J = np.memmap(mmp, dtype=dtype, mode=mode, shape=(rows, n))
        for a in range(start, n, chunk):
            b = min(a + chunk, n)
            X = np.repeat(x[None, :], b - a, axis=0)
            X[np.arange(b - a), np.arange(a, b)] += h[a:b]
            J[:, a:b] = ((self.wres_batch(X, pin_mode, aux, PW)
                          - r0[None, :]) / h[a:b, None]).T.astype(dtype)
            meta.write_text(f'{sig!r} {b}')
        J.flush()
        return J

    Tn.jac = types.MethodType(jac, Tn)


def spectral_transfer(field, ns_new, np_new):
    """s: FFT truncation 144->96; phi: FFT zero-pad 36->54. Real
    fields; norm-preserving per numpy 'forward' conventions handled
    explicitly."""
    ns, npn = field.shape
    F = np.fft.fft2(field) / (ns * npn)
    G = np.zeros((ns_new, np_new), complex)
    ks = np.fft.fftfreq(ns, 1 / ns).astype(int)
    kp = np.fft.fftfreq(npn, 1 / npn).astype(int)
    for i, m in enumerate(ks):
        if abs(m) > ns_new // 2 - 1:
            continue
        for j, n in enumerate(kp):
            if abs(n) > np_new // 2 - 1:
                continue
            G[m % ns_new, n % np_new] = F[i, j]
    return (np.fft.ifft2(G) * ns_new * np_new).real


def seed(T_old, T_new, x):
    th, pt, Tf, om1, om2 = T_old.unpack(np.asarray(x))
    f = lambda a: spectral_transfer(a, T_new.NS, T_new.NP)
    return T_new.pack(f(th), f(pt), f(Tf), om1, om2)


def resumable_lm(Tn, st, key, x0, a2pin, deadline):
    """Phase-resumable damped-GN driver for large-dof members.
    (Installed 2026-08-28: at 15554 dof BOTH the jac build and the
    normal-matrix accumulation individually exceed the container's
    ~10-min worker reap window, so the monolithic lm_round/gn_exact
    could never finish a round. This driver mirrors lm_round's
    numerics -- f64 normal accumulation, damped Cholesky steps,
    f64-residual acceptance -- but checkpoints BETWEEN phases:
    A jac (chunk-resumable memmap, bind_resumable_jac), B JtJ/Jtr
    accumulation (chunk-resumable to disk), C factor+step (redone
    whole if reaped; JtJ persists). Solver path differs from
    gn_exact in the endgame (small-lam LM instead of exact GN);
    the bars judge the STATE, not the path.)"""
    import scipy.linalg as sla
    from scipy.linalg import blas as _blas
    PW = 50.0
    tag = key.replace('|', '_').replace('/', '')
    jtj_p = pathlib.Path(f'/home/claude/s3w_jtj_{tag}.f64')
    jtr_p = pathlib.Path(f'/home/claude/s3w_jtj_{tag}_jtr.npy')
    acc_p = pathlib.Path(f'/home/claude/s3w_jtj_{tag}.acc')
    x = np.asarray(st.get(key + '|xlm', x0))
    lam = st.get(key + '|lam', 1e-4)
    rounds = st.get(key + '|rounds', 0)
    n = x.size
    while rounds < 60:
        if deadline and time.time() > deadline - 30:
            break
        r_now = Tn.field_rms(x)
        if r_now < RMS_BAR:
            break
        # f64 ENDGAME (option (ii), authorized 2026-08-29, bounded):
        # below 1e-6 the f32-stored FD Jacobian's ~6e-8 relative
        # noise rejects the punch-through steps (observed limit
        # cycle at 2.3e-7 on p42|4/3|deep). Endgame rounds use an
        # f64-stored jac; budget 10 f64 rounds, then the stall is
        # RECORDED (fallback (i)) rather than ground indefinitely.
        f64round = r_now < 1e-6
        if f64round:
            nf = st.get(key + '|f64r', 0)
            if nf >= 10:
                print(f"      [f64 endgame budget exhausted at RMS "
                      f"{r_now:.1e}: stall recorded]", flush=True)
                accepted = False
                break
            st[key + '|f64r'] = nf + 1
        # phase A: jac (self-resumable via bind_resumable_jac)
        J = Tn.jac(x, 'a2', a2pin, PW,
                   dtype=(np.float64 if f64round else np.float32))
        r0 = Tn.wres(x, 'a2', a2pin, PW)
        sig = float(np.sum(x) + 1e-3 * np.sum(x * x))
        # phase B: chunk-resumable JtJ/Jtr accumulation on disk
        start = 0
        if jtj_p.exists() and acc_p.exists():
            try:
                s_old, a_old = acc_p.read_text().split()
                if abs(float(s_old) - sig) < 1e-12 * (1 + abs(sig)):
                    start = int(a_old)
            except Exception:
                start = 0
        JtJ = np.memmap(jtj_p, dtype=np.float64, order='F',
                        mode='r+' if start else 'w+', shape=(n, n))
        Jtr = (np.load(jtr_p) if (start and jtr_p.exists())
               else np.zeros(n))
        for a in range(start, J.shape[0], 1024):
            B = np.asfortranarray(J[a:a + 1024].astype(np.float64))
            JtJ[:] = _blas.dsyrk(1.0, B, beta=1.0, c=JtJ, trans=1,
                                 lower=1, overwrite_c=1)
            Jtr += B.T @ r0[a:a + 1024]
            np.save(jtr_p, Jtr)
            acc_p.write_text(f'{sig!r} {min(a + 1024, J.shape[0])}')
            if deadline and time.time() > deadline - 30:
                st[key + '|xlm'] = x
                st[key + '|lam'] = lam
                st[key + '|rounds'] = rounds
                save(st)
                return x, Tn.field_rms(x), False
        JtJ.flush()
        # phase C: damped Cholesky trials (redone whole if reaped).
        # (Amended 2026-08-29: at 18146 dof the in-RAM A copy
        # (2.63 GB anonymous) OOM-killed every lifetime. A is now a
        # DISK-BACKED scratch memmap: the factorization's working
        # set becomes reclaimable page cache, and LAPACK factors it
        # in place. Numerics unchanged.)
        import shutil
        d = np.sqrt(np.maximum(np.diag(JtJ).astype(np.float64), 1e-12))
        f0 = 0.5 * float(r0 @ r0)
        A_p = pathlib.Path(f'/home/claude/s3w_A_{tag}.f64')
        accepted = False
        for _ in range(6):
            del JtJ
            shutil.copyfile(jtj_p, A_p)
            JtJ = np.memmap(jtj_p, dtype=np.float64, order='F',
                            mode='r', shape=(n, n))
            A = np.memmap(A_p, dtype=np.float64, order='F',
                          mode='r+', shape=(n, n))
            A[np.arange(n), np.arange(n)] += lam * d * d
            try:
                c, low = sla.cho_factor(A, lower=True,
                                        overwrite_a=True,
                                        check_finite=False)
                dx = -sla.cho_solve((c, low), Jtr, check_finite=False)
            except Exception:
                del A
                lam *= 10
                continue
            del A, c
            xt = x + dx
            rt = Tn.wres(xt, 'a2', a2pin, PW)
            if 0.5 * float(rt @ rt) < f0:
                x, lam, accepted = xt, max(lam / 3, 1e-9), True
                break
            lam *= 10
        rounds += 1
        st[key + '|xlm'] = x
        st[key + '|lam'] = lam
        st[key + '|rounds'] = rounds
        save(st)
        print(f"      [lm-r {rounds}: RMS {Tn.field_rms(x):.1e}  "
              f"lam {lam:.0e}{'' if accepted else '  (no step)'}]",
              flush=True)
        if not accepted and lam > 1e7:
            break
    done = (Tn.field_rms(x) < RMS_BAR or rounds >= 60
            or (not accepted if rounds else False))
    if done:
        for p in (jtj_p, jtr_p, acc_p,
                  pathlib.Path(f'/home/claude/s3w_A_{tag}.f64')):
            p.unlink(missing_ok=True)
        for k in ('|xlm', '|lam', '|rounds'):
            st.pop(key + k, None)
        save(st)
    return x, Tn.field_rms(x), done


def members():
    st2c = pickle.loads(CK2C.read_bytes())
    out = []
    for q in CELLS:
        X = st2c['prof-%s' % q]['states']
        for which, idx in (('prev', 11), ('deep', 12)):
            out.append((q, which, np.asarray(X[idx])))
    return out


def band(P, n0, m0, tolerance=1):
    NS, NP = P.shape
    tot = P.sum()
    s = 0.0
    for sgn in (1, -1):
        for dm in range(-tolerance, tolerance + 1):
            for dn in range(-tolerance, tolerance + 1):
                s += P[(sgn * (m0 + dm)) % NS, (sgn * (n0 + dn)) % NP]
    return s / tot


def spectrum(T, t):
    tp = t[T.N:2 * T.N].reshape(T.NS, T.NP)
    P = np.abs(np.fft.fft2(tp)) ** 2
    return P, float(np.linalg.norm(tp))


def top_modes(P, k=4):
    tot = P.sum()
    idx = np.dstack(np.unravel_index(
        np.argsort(P.ravel())[::-1][:2 * k], P.shape))[0]
    seen, out = set(), []
    for ms, nph in idx:
        m = ms if ms <= P.shape[0] // 2 else ms - P.shape[0]
        n = nph if nph <= P.shape[1] // 2 else nph - P.shape[1]
        key = (abs(m), abs(n))
        if key in seen:
            continue
        seen.add(key)
        out.append((m, n, P[ms, nph] * 2 / tot))
    return out[:k]


def credential():
    T_old = {q: QTGrid(*SRC, *CELLS[q]) for q in CELLS}
    for gname, (ns, npn) in GRIDS.items():
        for q, which, x in members():
            Tn = QTGrid(ns, npn, *CELLS[q])
            xs = seed(T_old[q], Tn, x)
            m = metrics(Tn, xs)
            print(f"  [{gname} {q} {which}] seed RMS {m['rms']:.2e}  "
                  f"A2 {m['A2']:.7f}  clos {m['clos']:.2e}")
    print('credential: seeds constructed and evaluated on all grids.')


def campaign(budget):
    deadline = time.time() + budget if budget else None
    st = load()
    T_old = {q: QTGrid(*SRC, *CELLS[q]) for q in CELLS}
    for sweep in range(12):
        alldone = True
        for gname, (ns, npn) in GRIDS.items():
            for q, which, x in members():
                key = f'{gname}|{q}|{which}'
                if st.get(key + '|done'):
                    continue
                alldone = False
                Tn = QTGrid(ns, npn, *CELLS[q])
                if Tn.n > 12000:
                    bind_resumable_jac(Tn, key.replace('|', '_')
                                       .replace('/', ''))
                x0 = st.get(key + '|x', None)
                if x0 is None:
                    x0 = seed(T_old[q], Tn, x)
                # pin: the member's own registered A2 from the SOURCE
                _, c2src = T_old[q].modes(T_old[q].geom(np.asarray(x))[2])
                a2pin = float(np.abs(c2src))
                print(f"== solving {key}  (dof {Tn.n}, pin A2 "
                      f"{a2pin:.7f}, sweep {sweep})", flush=True)
                # ROLLING DEADLINES (fix installed 2026-08-28 after
                # the worker was reaped silently mid-member with no
                # traceback and the since-last-save rounds lost):
                # resumable_solve only checkpoints at its deadline,
                # so we hand it short deadlines and loop -- a save
                # every few minutes regardless of who kills us.
                while True:
                    roll = time.time() + 420
                    if deadline:
                        roll = min(roll, deadline)
                    if Tn.n > 12000:
                        xs, rms, done = resumable_lm(
                            Tn, st, key + '|solve', x0, a2pin, roll)
                    else:
                        xs, rms, done = T96.resumable_solve(
                            Tn, st, key + '|solve', x0, 'a2', a2pin,
                            roll)
                    st[key + '|x'] = xs
                    x0 = xs
                    save(st)
                    if done or (deadline
                                and time.time() > deadline - 210):
                        break
                if done:
                    m = metrics(Tn, xs)
                    gated = (m['rms'] < RMS_BAR
                             and m['clos'] < CLOSURE_BAR)
                    prev = st.get(key + '|last_rms')
                    if gated:
                        st[key + '|done'] = True
                    elif prev is not None and m['rms'] > prev / 1.2:
                        # STALLED (no real progress across a full
                        # solve pass): a true refusal; recorded.
                        st[key + '|done'] = True
                    # else: BUDGET EXIT while still converging (the
                    # rounds_max cap) -- instrument scheduling, not
                    # physics; the member stays open and the next
                    # sweep resumes from xs. (Fix installed
                    # 2026-08-28 after base|4/3|prev exited the cap
                    # at 8.0e-8 vs the 1e-8 bar while converging at
                    # ~0.83/round.)
                    st[key + '|last_rms'] = m['rms']
                    st[key + '|gated'] = gated
                    st[key + '|metrics'] = m
                    print(f"   gated={gated}  RMS {m['rms']:.2e}  "
                          f"clos {m['clos']:.2e}  A2 {m['A2']:.7f}",
                          flush=True)
                save(st)
                if deadline and time.time() > deadline - 210:
                    print('budget reached; rerun to resume.')
                    return
        if alldone:
            break
    verdict(st)


def verdict(st):
    res = {}
    for gname, (ns, npn) in GRIDS.items():
        for q in CELLS:
            kp, kd = (f'{gname}|{q}|prev', f'{gname}|{q}|deep')
            if not (st.get(kp + '|gated') and st.get(kd + '|gated')):
                print(f'{gname} {q}: pair not fully gated; no tangent.')
                return
            Tn = QTGrid(ns, npn, *CELLS[q])
            t = st[kd + '|x'] - st[kp + '|x']
            t = t / np.linalg.norm(t)
            P, pts = spectrum(Tn, t)
            res[(gname, q)] = P
            print(f'\n== {gname} {q}: pt_share {pts:.3f}  top modes:')
            for m, n, fr in top_modes(P):
                print(f'    m={m:+3d} n={n:+3d}  frac {fr:.3f}')
    F17b = band(res[('base', '4/3')], 17, 19)
    F17p = band(res[('probe', '4/3')], 17, 19)
    Pp = res[('probe', '4/3')]
    NPp = Pp.shape[1]
    hi = sum(Pp[:, j] .sum() for j in range(NPp)
             if min(j, NPp - j) >= 21) / Pp.sum()
    beat_ok = False
    for m, n, fr in top_modes(res[('base', '5/3')], k=1):
        beat_ok = (abs(m), abs(n)) in {(2 * k, k) for k in range(1, 6)}
    print('\n== VERDICT BLOCK ==')
    cred = F17b >= 0.20 and beat_ok
    print(f'S3-CRED: F17(96x36)={F17b:.3f} (>=0.20); 5/3 beat top mode '
          f'({beat_ok})  -> {"PASS" if cred else "S3-F-INSTRUMENT"}')
    if not cred:
        print('**** VERDICT: S3-F-INSTRUMENT ****')
        return
    dom = top_modes(res[('probe', '4/3')], k=1)[0]
    dom_ok = (abs(dom[1]), abs(dom[0])) == (17, 19) or \
             (abs(dom[0]), abs(dom[1])) == (19, 17)
    phys = F17p >= 0.5 * F17b and dom_ok and hi < 0.10
    art = F17p < 0.05
    print(f'F17(96x54)={F17p:.3f} vs 0.5x base {0.5*F17b:.3f}; dominant '
          f'mode (m={dom[0]},n={dom[1]}) at-band={dom_ok}; '
          f'HIBAND={hi:.3f} (<0.10)')
    v = ('S3-PHYSICAL' if phys else
         'S3-ARTIFACT' if art else 'S3-OPEN')
    print(f'\n**** VERDICT: {v} ****')


if __name__ == '__main__':
    if '--credential' in sys.argv:
        credential()
    else:
        b = 0
        if '--budget' in sys.argv:
            b = int(sys.argv[sys.argv.index('--budget') + 1])
        campaign(b)

