"""benchmarks/foundations/svd_diagnostic.py

The smallest-singular-value diagnostic along the aligned branch
(external review step 3, adopted after FND-145). Bars locked BEFORE
computing: analysis/SVD_DIAG_bars_LOCKED.md. This file implements
those bars and nothing else; interpretation rules A/B/C are applied
mechanically from the registered thresholds.

Run detached and MEMORY-EXCLUSIVE (the 112x42 Jacobian holds 0.8 GB
f32 and LAPACK wants workspace on top):

    setsid nohup python3 benchmarks/foundations/svd_diagnostic.py \
        > /tmp/svd_diag.log 2>&1 < /dev/null &

Per-state checkpoint to /tmp/svd_diag_ckpt.pkl; rerun to resume.
"""
import pathlib
import pickle
import sys
import time

import numpy as np
from scipy.linalg import svd as _svd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations.traverse96_scout import TGrid96  # noqa: E402
from benchmarks.foundations.traverse_steepened import RMS_BAR  # noqa: E402


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

CKPT = pathlib.Path('/tmp/svd_diag_ckpt.pkl')
P94 = pathlib.Path('/tmp/p94_ckpt.pkl')
N96 = pathlib.Path('/tmp/n96_ckpt.pkl')
PW = 50.0
FLOOR = 1e-6          # bar (iii): report below this as "< floor"
XCHK = 0.05           # bar (ii): inverse-iteration vs LAPACK, 5% rel


def load(p):
    return pickle.loads(p.read_bytes())


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


# ------------------------------------------------------------------
# AMENDMENT 1 (see analysis/SVD_DIAG_bars_LOCKED.md): the chart holds
# genuine structural null directions (recon() projects mean and
# s-Nyquist modes), which appear as a dense sigma cluster at the
# FD/f32 noise scale. The diagnostic therefore reads the smallest
# sigma ABOVE the per-state floor (1e-6 * smax); vectors come from the
# same LAPACK factorization on the 96-grid states; the cluster sample
# vector's anatomy must certify the structural reading or the rules
# are not applied.

def matvec(J, v):
    return (J @ v.astype(np.float32)).astype(np.float64)


def true_sigma(T, x, a2, v, drop_pin=False, h=1e-7):
    """AMENDMENT 2: ||J_true v|| via a float64 directional finite
    difference of wres itself -- float32-store independent. For the
    free matrix the pin row's contribution (row m-3, the continuation
    pin) is removed from the residual difference before the norm."""
    r0 = T.wres(x, 'a2', a2, PW)
    r1 = T.wres(x + h * v, 'a2', a2, PW)
    d = (r1 - r0) / h
    if drop_pin:
        d = np.delete(d, d.size - 3)
    return float(np.linalg.norm(d))


def anatomy(T, v):
    N = T.N
    th = v[:N].reshape(T.NS, T.NP)
    pt = v[N:2 * N].reshape(T.NS, T.NP)
    Tb = v[2 * N:3 * N]
    tail = v[3 * N:]
    tot = float(v @ v)
    fr = dict(th=float(np.sum(th ** 2)) / tot,
              pt=float(np.sum(pt ** 2)) / tot,
              T=float(np.sum(Tb ** 2)) / tot,
              om=float(np.sum(tail ** 2)) / tot)

    def dom(F):
        A = np.abs(np.fft.fft2(F))
        ks, kp = np.unravel_index(np.argmax(A), A.shape)
        ks = ks if ks <= F.shape[0] // 2 else ks - F.shape[0]
        kp = kp if kp <= F.shape[1] // 2 else kp - F.shape[1]
        return int(ks), int(kp)
    fr['th_mode'] = dom(th)
    fr['pt_mode'] = dom(pt)
    return fr


def eff_report(sv, smax):
    """k0 below floor, sigma_eff, and the ten sigmas above the floor."""
    floor = 1e-6 * smax
    below = sv[sv < floor]
    above = np.sort(sv[sv >= floor])
    k0 = int(below.size)
    rng = (float(below.min()), float(below.max())) if k0 else None
    return k0, rng, float(above[0]), [float(x) for x in above[:10]]


def build_JtJ(J):
    """Blocked syrk accumulation of J^T J in float64, lower triangle."""
    from scipy.linalg import blas as _blas
    n = J.shape[1]
    JtJ = np.zeros((n, n), order='F')
    for a in range(0, J.shape[0], 1024):
        B = np.asfortranarray(J[a:a + 1024].astype(np.float64))
        JtJ = _blas.dsyrk(1.0, B, beta=1.0, c=JtJ, trans=1,
                          lower=1, overwrite_c=1)
    return JtJ


def downdate_pin(JtJ, r):
    """Exact rank-1 removal of the pin row: JtJ_free = JtJ - r r^T,
    lower triangle, in place (dsyr)."""
    from scipy.linalg import blas as _blas
    return _blas.dsyr(-1.0, np.asfortranarray(r.astype(np.float64)),
                      a=JtJ, lower=1, overwrite_a=1)


def bottom_from_JtJ(JtJ, k=150, want_vectors=True, overwrite=False):
    """smax by dsymv power iteration; bottom eigenpairs by syevr
    subset on the lower-stored normal matrix. sigma = sqrt(eig)."""
    from scipy.linalg import eigh
    from scipy.linalg import blas as _blas
    n = JtJ.shape[0]
    v = np.random.default_rng(0).standard_normal(n)
    v /= np.linalg.norm(v)
    for _ in range(120):
        w = _blas.dsymv(1.0, JtJ, v, lower=1)
        v = w / np.linalg.norm(w)
    smax = float(np.sqrt(v @ _blas.dsymv(1.0, JtJ, v, lower=1)))
    k = min(k, n - 1)
    if want_vectors:
        ev, V = eigh(JtJ, lower=True, subset_by_index=[0, k],
                     check_finite=False, overwrite_a=overwrite)
        return np.sqrt(np.maximum(ev, 0.0)), V.T, smax
    ev = eigh(JtJ, lower=True, subset_by_index=[0, k],
              eigvals_only=True, check_finite=False,
              overwrite_a=overwrite)
    return np.sqrt(np.maximum(ev, 0.0)), None, smax


def targeted_vector(J, sigma, iters=6, cg_max=800, seed=1):
    """S4 only: shifted inverse iteration at the LAPACK sigma."""
    n = J.shape[1]
    v = np.random.default_rng(seed).standard_normal(n)
    v /= np.linalg.norm(v)
    mu = sigma ** 2
    for _ in range(iters):
        b = v
        x = np.zeros_like(b)
        r = b.copy(); pvec = r.copy(); rs = r @ r
        for _ in range(cg_max):
            Ap = (J.T @ (J @ pvec.astype(np.float32)).astype(np.float32)
                  ).astype(np.float64) + mu * pvec
            alpha = rs / (pvec @ Ap)
            x += alpha * pvec
            r -= alpha * Ap
            rs_new = r @ r
            if rs_new < 1e-16 * (b @ b):
                break
            pvec = r + (rs_new / rs) * pvec
            rs = rs_new
        v = x / np.linalg.norm(x)
    return v


def measure_state(tag, T, x, tangent=None, vectors=True, k=150):
    t0 = time.time()
    rms = T.field_rms(x)
    ws, zp, w, ze, gphi, gam, th, pt, Tf, om1, om2 = T.geom(x)
    _, c2 = T.modes(w)
    a2 = float(np.abs(c2))
    flagged = rms >= RMS_BAR
    print(f"[{tag}] RMS {rms:.2e}  A2 {a2:.7f}  n {x.size}"
          f"{'  FLAGGED (>= RMS bar)' if flagged else ''}", flush=True)

    dtype = np.float64 if vectors else np.float32
    J = T.jac(x, 'a2', a2, PW, dtype=dtype)
    m = J.shape[0]
    print(f"[{tag}] J built {J.shape} {dtype.__name__} in "
          f"{time.time()-t0:.0f}s", flush=True)
    r_pin = np.array(J[m - 3], dtype=np.float64)
    JtJ = build_JtJ(J)
    if vectors:
        del J
        J = None
    print(f"[{tag}] JtJ accumulated in {time.time()-t0:.0f}s", flush=True)

    out = dict(tag=tag, rms=float(rms), A2=a2, n=int(x.size),
               flagged=bool(flagged))
    for name in ('J', 'Jfree'):
        if name == 'Jfree':
            if vectors:
                JtJ = downdate_pin(JtJ, r_pin)
            else:
                # values-only path (S4): the 'J' eigh ran with
                # overwrite_a=True to avoid a 1.6 GB copy (the copy
                # OOMed the container), so JtJ is rebuilt from the
                # retained f32 J, then downdated. The spent JtJ must
                # be FREED FIRST: the rebuild allocates its result
                # before the name rebinds, and holding both plus J
                # is a 3.9 GB peak (the second OOM of this stage).
                JtJ = None
                JtJ = downdate_pin(build_JtJ(J), r_pin)
        sig, V, smax = bottom_from_JtJ(
            JtJ, k=k, want_vectors=vectors,
            overwrite=(name == 'Jfree' or not vectors))
        floor = 1e-6 * smax
        k0 = int(np.sum(sig < floor))
        if k0 >= sig.size - 10:
            raise RuntimeError(f'{tag}/{name}: cluster reaches subset '
                               f'edge (k0 {k0} of {sig.size}); raise k')
        rng = ((float(sig[0]), float(sig[k0 - 1])) if k0 else None)
        seff = float(sig[k0])
        top10 = [float(v_) for v_ in sig[k0:k0 + 10]]
        print(f"[{tag}] {name}: smax {smax:.4e}  k0(below floor) {k0}"
              f"  cluster {['%.1e' % r for r in rng] if rng else '-'}"
              f"  sigma_eff {seff:.4e}  eff-ratio {seff/smax:.3e}",
              flush=True)
        print(f"[{tag}] {name} ten-above-floor "
              f"{['%.3e' % v_ for v_ in top10]}", flush=True)
        rec = dict(smax=smax, k0=k0, cluster=rng, seff=seff,
                   ratio=seff / smax, ten=top10)
        if V is not None:
            v_eff = V[k0].astype(np.float64)
            ts = true_sigma(T, x, a2, v_eff, drop_pin=(name == 'Jfree'))
            chk = abs(ts - seff) / seff
            rec['selfchk'] = float(chk)
            rec['true_sigma'] = ts
            rec['v_eff'] = v_eff
            rec['v_eff_an'] = anatomy(T, v_eff)
            print(f"[{tag}] {name} bar(ii) f64-FD true-operator check: "
                  f"||Jv|| {ts:.4e} vs sigma_eff {seff:.4e}  rel "
                  f"{chk:.2%} {'PASS' if chk < XCHK else 'FAIL -- HALT'}",
                  flush=True)
            print(f"[{tag}] {name} v_eff anatomy {rec['v_eff_an']}",
                  flush=True)
            if k0:
                v_cl = V[0].astype(np.float64)
                ts_cl = true_sigma(T, x, a2, v_cl,
                                   drop_pin=(name == 'Jfree'))
                rec['cluster_an'] = anatomy(T, v_cl)
                rec['cluster_true'] = ts_cl
                print(f"[{tag}] {name} cluster-sample anatomy "
                      f"{rec['cluster_an']}", flush=True)
                print(f"[{tag}] {name} cluster-sample f64-FD ||Jv|| "
                      f"{ts_cl:.2e} vs floor {floor:.2e}  "
                      f"{'below-floor CERTIFIED' if ts_cl < floor else 'ABOVE FLOOR -- cluster nature OPEN'}",
                      flush=True)
            if tangent is not None and name == 'Jfree':
                t_hat = tangent / np.linalg.norm(tangent)
                Vnull = V[:max(k0, 1)]
                proj = float(np.linalg.norm(Vnull @ t_hat))
                rec['tangent_proj'] = proj
                print(f"[{tag}] bar(i) tangent in near-null space: "
                      f"|proj| {proj:.5f} "
                      f"{'PASS' if proj > 0.99 else 'FAIL -- HALT'}",
                      flush=True)
            del V
        out[name] = rec
    del JtJ
    out['secs'] = time.time() - t0
    print(f"[{tag}] done in {out['secs']:.0f}s", flush=True)
    return out


def main():
    st = load(CKPT) if CKPT.exists() else {}
    p94 = load(P94)
    n96 = load(N96)

    T96 = TGrid96(96, 36)
    queue = [
        ('S0-member0', T96, n96['members'][0]['x'], None),
        ('S1-member1', T96, n96['members'][1]['x'], None),
        ('S2-marchhead', T96, n96['appr']['x2'],
         n96['appr']['x2'] - n96['appr']['x1']),
        ('S3-p94landed', T96, p94['landed'], None),
    ]
    for tag, T, x, tan in queue:
        if tag in st:
            print(f"[{tag}] checkpointed; skipping", flush=True)
            continue
        st[tag] = measure_state(tag, T, np.asarray(x, float), tan)
        save(st)

    if 'S4-adjudicated' not in st:
        T112 = TGrid96(112, 42)
        st['S4-adjudicated'] = measure_state(
            'S4-adjudicated', T112, np.asarray(p94['confsolve']['x'], float),
            vectors=False, k=300)
        save(st)

    # ---------------- mechanical application of the registered rules
    # (amendment 1: rules operate on the EFFECTIVE ratios; the cluster
    # anatomy must certify the structural-null reading first)
    s0, s3 = st['S0-member0'], st['S3-p94landed']
    s2st = st['S2-marchhead']

    def structural(rec):
        # Amendment 2 / implementation note: certification is
        # OPERATOR-LEVEL -- the cluster sample's f64-FD ||J_true v||
        # must sit below the floor. The amendment-1 anatomy heuristic
        # is retired (its readings stay on the record).
        ct = rec.get('cluster_true')
        if ct is None:
            return True
        return ct < 1e-6 * rec['smax']

    cert = all(structural(st[k][mm])
               for k in ('S0-member0', 'S1-member1', 'S2-marchhead',
                         'S3-p94landed')
               for mm in ('J', 'Jfree'))
    halts = []
    for k in ('S0-member0', 'S1-member1', 'S2-marchhead', 'S3-p94landed'):
        for mm in ('J', 'Jfree'):
            c = st[k][mm].get('selfchk')
            if c is not None and c >= XCHK:
                halts.append(f'{k}/{mm} self-consistency {c:.2%}')
    tp = s2st['Jfree'].get('tangent_proj', 0.0)
    if tp <= 0.99:
        halts.append(f'tangent projection {tp:.4f}')
    if not cert:
        halts.append('cluster anatomy does not certify structural nulls '
                     '-- cluster nature OPEN')
    print("\n== RULES (locked + amendments 1-3) ==", flush=True)
    if halts:
        print("INSTRUMENT BAR FAILED -- HALT, no interpretation:", flush=True)
        for h in halts:
            print("   ", h, flush=True)
        return
    ra2_drop = s0['J']['ratio'] / s3['J']['ratio']
    r2_drop = s0['Jfree']['ratio'] / s3['Jfree']['ratio']
    print(f"Ra2(eff): S0 {s0['J']['ratio']:.3e} -> S3 "
          f"{s3['J']['ratio']:.3e}  (drop {ra2_drop:.1f}x)", flush=True)
    print(f"R2 (eff): S0 {s0['Jfree']['ratio']:.3e} -> S3 "
          f"{s3['Jfree']['ratio']:.3e}  (drop {r2_drop:.1f}x)", flush=True)
    if ra2_drop >= 10 and r2_drop < 3:
        print("RULE A: A2-CHART DEGENERACY -- the chart, not the branch.",
              flush=True)
    elif ra2_drop >= 10 and r2_drop >= 10:
        an = s3['Jfree']['v_eff_an']
        if an['om'] >= 0.3:
            print("RULE B-res: approaching genuine degeneracy, "
                  "resonance-type.", flush=True)
        elif an['T'] >= 0.5:
            print("RULE B-gauge: approaching genuine degeneracy, "
                  "tension/gauge-type.", flush=True)
        else:
            print("RULE B-open: second direction softening, UNCLASSIFIED "
                  "-- registered open.", flush=True)
    elif ra2_drop < 10 and r2_drop < 10:
        print("RULE C: HEALTHY bottom spectrum -- does not explain the "
              "dA2/ds collapse; q-sensitivity probe promoted.", flush=True)
    else:
        print("NO CALL -- outside the registered rules; stays open.",
              flush=True)


if __name__ == '__main__':
    main()

