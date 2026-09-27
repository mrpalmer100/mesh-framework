"""KERNEL CONTINUATION -- a bordered Gauss-Newton solve along a degenerate direction, built
on the credentialed sparse instrument (SparseJac + BandedTorusSolver) without touching it.

Why: at an exact resonance (the anti-aligned sector at the difference frequency, FND-172/
S288) the a2-pinned linearization has a near-null vector c (Q2: the other polarization of the
(s - phi) helical pattern). Gauss-Newton floors there -- the residual keeps a component that
only a move ALONG c removes, and the least-squares step along c is ~0 because J c ~ 0. The
second-order solvability condition (Lyapunov-Schmidt) picks the kernel coordinate b; the
solver cannot find b by descent. So we make b an explicit continuation parameter:

    unknowns  x  (state, om2 free, a2 pinned)      constraint  c^T (x - x_ref) = b
    bordered step: [J ; c^T] dx = [-F ; b - c^T(x - x_ref)]

solved with the bordering algorithm on the normal equations the banded solver already
factors: y1 = (J^T J + lam D)^-1 (-J^T F),  y2 = (J^T J + lam D)^-1 c,
dx = y1 + mu y2 with mu chosen so that c^T dx = target. Two banded solves per round, one
factorization. Sweep b; the member (if any) is where the RMS drops to the bar; a floor at
every b means the obstruction is not along c (report, do not rescue).

Near-null direction: found in the physical harmonic subspace (the (1,1) subspace where the
level-2 injection lives), NOT by a global smallest-singular-value search, which returns
Nyquist grid modes (ANTI-ALIGNED Q2, recorded caution). The om2 column and the pattern-phase
partner are projected out.

Provenance: built 2026-09-12 as the named next-order of ANTI-ARC-S288; fault-13 remedy (de-aliased
corrector, Nyquist bar) 2026-09-23; lam ladder and floor detector 2026-09-24/27. Uncredentialed until
its own commission (KERNEL-CONT) sets bars and controls; use for exploration and for that
commission only.
"""
import numpy as np
import scipy.sparse as sp

from benchmarks.foundations import sparsej_instrument as SJ
from benchmarks.foundations import qsweep_stage1 as q1


def dealias_s(T, dx, kmax_frac=1.0 / 3.0):
    """FAULT-13 REMEDY (2026-09-23): remove the high s-harmonics (|k| > kmax_frac * NS) from a step
    in the th and pt fields, so the corrector cannot gate by adding grid-scale structure along the
    strand. The om2 component and the T field are untouched."""
    NS, NP = T.NS, T.NP; N = NS * NP; out = dx.copy(); kmax = int(kmax_frac * NS)
    for f in (0, 1):
        F = np.fft.rfft(dx[f * N:(f + 1) * N].reshape(NS, NP), axis=0)
        F[kmax + 1:, :] = 0.0
        out[f * N:(f + 1) * N] = np.fft.irfft(F, n=NS, axis=0).ravel()
    return out


def harmonic_basis(T, x0, ks, m, iom):
    """unit basis vectors of the (s-harmonic ks, phi-harmonic m) subspace in the th and pt
    fields, as displacements of x0 (om2 component zeroed)."""
    NS, NP = T.NS, T.NP
    th0, pt0, T0, o1, o2 = T.unpack(x0)
    s = np.arange(NS) / NS * 2 * np.pi; p = np.arange(NP) / NP * 2 * np.pi
    S_, P_ = np.meshgrid(s, p, indexing='ij'); B = []
    combos = [np.cos(ks * S_ - m * P_), np.sin(ks * S_ - m * P_)]
    if m > 0:
        combos += [np.cos(ks * S_ + m * P_), np.sin(ks * S_ + m * P_)]
    for fld in (0, 1):
        for f in combos:
            th = np.zeros((NS, NP)); pt = np.zeros((NS, NP)); (th if fld == 0 else pt)[:] = f
            v = T.pack(th0 + th, pt0 + pt, T0, o1, o2) - x0; v[iom] = 0.0
            B.append(v / np.linalg.norm(v))
    Bq, _ = np.linalg.qr(np.array(B).T)
    return Bq


def near_null(T, J, x0, iom, exclude=(), ks=1, m=1):
    """the near-null right vector of J in the (ks, m) harmonic subspace, orthogonal to the
    vectors in `exclude` (e.g. the injection direction and its phase partner). Returns
    (c, sigma) with sigma = |J c| / mean row norm."""
    Bq = harmonic_basis(T, x0, ks, m, iom)
    for u in exclude:
        Bq = Bq - np.outer(u, u @ Bq)
    Bq, _ = np.linalg.qr(Bq)
    U, S, Vt = np.linalg.svd(J @ Bq, full_matrices=False)
    c = Bq @ Vt[-1]; c /= np.linalg.norm(c)
    rown = np.sqrt(J.multiply(J).sum() / J.shape[0])
    return c, float(np.linalg.norm(J @ c) / rown)


def bordered_gn(T, x, pin, c, b_target, x_ref, sj, bs, rounds=30, PW=50.0, lam=1e-9,
                stop_rms=None, log=print, pin_mode='a2', aux=None, dealias=False, nyq_bar=None,
                stall_rounds=6, stall_df=1e-3, state=None):
    """Gauss-Newton with the bordering constraint c^T (x - x_ref) = b_target. Same acceptance
    ladder in spirit as gn_sparse (fractions 1, .5, .25, .1), same bars read by the caller.
    pin_mode/aux: 'a2' with aux = pin (default), or 'arc' with aux = (xb, t, ds) for the
    stage-2c arc constraint (KERNEL-MARCH, 2026-09-16).
    dealias=True (FAULT-13 remedy, 2026-09-23): every step is projected onto s-harmonics
    |k| <= NS/3 before acceptance. nyq_bar: the solve is not reported converged unless the
    gate's wsNyq <= nyq_bar (hist entries carry it as their 6th field).
    On a rejected step (2026-09-24/27): lam escalates x10 within the round, to 1e-5 at most
    (four rungs), before no-step is declared; lam relaxes x0.5 on success. A FLOOR is declared
    after stall_rounds consecutive accepted rounds each below stall_df relative decrease --
    the credentialed solver's stall trigger, so a floored solve does not burn its budget."""
    stop_rms = stop_rms or q1.RMS_BAR
    if aux is None: aux = pin
    if state is not None: lam = float(state.get('lam', lam))   # lam persists across one-round-per-invocation drivers
    n = len(x); d2 = np.ones(n)
    hist = []; stall = 0

    def _step(J, r0, lam):
        bs.factor(J, lam, d2)
        y1 = bs.solve(J.T @ r0)                    # solves (J^T J + lam D) y1 = -J^T r0
        y2 = bs.solve(-c)                          # solves (J^T J + lam D) y2 =  c
        gap = b_target - float(c @ (x - x_ref))
        mu = (gap - float(c @ y1)) / float(c @ y2)
        dx = y1 + mu * y2
        if dealias:
            dx = dealias_s(T, dx)
        return dx, mu, gap

    for it in range(rounds):
        J, r0 = sj(x, pin_mode, aux, PW); J = sp.csr_matrix(J)
        dx, mu, gap = _step(J, r0, lam)
        log(f"      [kc {it}: J assembled; factored at lam {lam:.0e}; |dx| {float(np.linalg.norm(dx)):.2e}; gap {gap:+.2e}]")
        f0 = float(np.linalg.norm(r0)); acc = None
        if it == 0 and abs(gap) > 1e-6:
            # PREDICTOR: the first move along the kernel is a prescribed displacement to the
            # target b, taken unconditionally; the corrector rounds that follow reduce the
            # residual at fixed b through the acceptance ladder.
            x = x + dx; ft = float(np.linalg.norm(T.wres(x, pin_mode, aux, PW))); rms = T.field_rms(x, pin_mode, aux)
            b_now = float(c @ (x - x_ref)); nyq = float(q1.metrics(T, x)['nyq'])
            hist.append((it, rms, ft, b_now, mu, nyq))
            log(f"      [kc {it}: PREDICTOR to b {b_now:+.3e}  RMS {rms:.2e}  wres {ft:.2e}  wsNyq {nyq:.1e}  mu {mu:+.2e}]")
            continue
        while True:
            for a_ in (1.0, 0.5, 0.25, 0.1, 0.03):
                xt = x + a_ * dx
                ft = float(np.linalg.norm(T.wres(xt, pin_mode, aux, PW)))
                if ft < f0:
                    acc = (a_, xt, ft); break
            if acc is not None or lam >= 1e-5:
                break
            lam *= 10.0
            log(f"      [kc {it}: step rejected; escalating lam to {lam:.0e}]")
            dx, mu, gap = _step(J, r0, lam)
        if acc is None:
            log(f"      [kc {it}: no accepted step at lam {lam:.0e}; |mu| {abs(mu):.2e}  b {float(c @ (x - x_ref)):+.3e}]")
            break
        a_, x, ft = acc
        lam = max(lam * 0.5, 1e-9)
        rms = T.field_rms(x, pin_mode, aux); b_now = float(c @ (x - x_ref)); nyq = float(q1.metrics(T, x)['nyq'])
        hist.append((it, rms, ft, b_now, mu, nyq))
        df = 1.0 - ft / f0
        log(f"      [kc {it}: RMS {rms:.2e}  wres {ft:.2e}  b {b_now:+.3e}  wsNyq {nyq:.1e}  lam {lam:.0e}  frac {a_}  df {100 * df:.2f}%]")
        if rms < stop_rms and (nyq_bar is None or nyq <= nyq_bar):
            break
        stall = stall + 1 if df < stall_df else 0
        if stall >= stall_rounds:
            log(f"      [kc {it}: FLOOR -- {stall_rounds} consecutive rounds below {stall_df:.0e} relative decrease]")
            break
    if state is not None: state['lam'] = lam
    return x, hist


def sweep(T, x_floor, pin, sj, bs, c, b_values, rounds=20, log=print):
    """From a floored state, solve the bordered problem at each b; report RMS(b).
    The member is where RMS meets the bar; a floor at every b means the obstruction is
    elsewhere -- report, do not rescue."""
    out = []
    for b in b_values:
        x, hist = bordered_gn(T, x_floor, pin, c, b, x_floor, sj, bs, rounds=rounds, log=log)
        rms = T.field_rms(x, 'a2', pin); om2 = float(T.geom(x)[10])
        out.append(dict(b=b, rms=rms, om2=om2, x=x))
        log(f"    [sweep b={b:+.3e}] RMS {rms:.2e}  om2 {om2:+.6f}  rounds {len(hist)}")
    return out
