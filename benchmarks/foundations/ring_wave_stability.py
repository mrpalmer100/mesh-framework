"""RING-WAVE-STABILITY Leg 0: the constrained-Hessian stability instrument, credentialed on KNOWN answers only
(executor, sandbox, 2026-10-26). The ring-wave evidence cell (the travelling-twist ring of elec_rope_wave.py at
beta_p = 1) is NEVER evaluated here: this file has no code path that builds it, and the fold it does touch is the
competitor state whose numbers are already on the record.

WHAT THE INSTRUMENT IS
  constrained_spectrum(f, cons, x, ...): for an energy f(x) and hard constraints cons(x) = 0 at a configuration x,
  (a) the Lagrange multipliers by least squares, (b) the STATIONARITY measure S = |P grad f| L / f (the projected
  gradient, scaled by the configuration's length, over its energy; the Director's "gradient / E" of ELEC-004A,
  0.37 there, made dimensionless), (c) the Hessian of the Lagrangian f - lambda . cons by symmetric finite
  differences, (d) its restriction to the constraint tangent space with the symmetry generators (rigid motions,
  the reparametrization of a tension rope) projected out, (e) the spectrum: number of negative, null and positive
  modes and the lowest eigenvector. Node coordinates throughout (M points in R^3), never a Fourier truncation:
  a Fourier-space minimum can be a node-space saddle, and the lock must not inherit that hole.

THE KNOWN ANSWERS (Leg 0)
  K1  MICHELL (FND-STRAND-003's threshold, as a number): a closed inextensible rod of bending stiffness B and
      torsional stiffness C, carrying link Lk entirely as twist on the flat circle, E = (B / l) sum (1 - t_i . t_i+1)
      + 2 pi^2 C (Lk - Wr)^2 / L with the writhe from the EXACT polygon Gauss integral (Klenin and Langowski 2000,
      method 1a), loses stability at Lk_c = sqrt(3) B / C (Michell 1889; Zajac 1962; Le Bret 1979) in the n = 2
      out-of-plane mode. The instrument must find that crossing by its own spectrum, with the discretization
      converging as M^-2, for two values of B / C.
  K2  STATIONARITY: S = 0 (to FD precision) at the twisted circle, which is an exact stationary point; a circle
      displaced by a known n = 3 ripple of amplitude a returns S proportional to a (the ceiling instrument
      reports what it is handed and nothing else).
  K3  THE ROPE WIRING: pieces_nodes (the elec_rope_wave energetics on a node polygon, Omega eliminated by the
      J root find) reproduces elec_rope_wave.pieces on the same polygon to 1e-12; and on the co-moving fold
      (beta_p = 0, kappa_tw 0.5, J = pi, the competitor state of the record, re-minimized here from the flat seed)
      the node-space stationarity S and the constrained spectrum are REPORTED as the instrument's reading of the
      reference minimum: a free minimization that converged has no negative constrained modes beyond the
      Fourier truncation's reach, and whatever the node Hessian shows there is the instrument's calibration, not
      a result about the ring-wave.
  K4  WRITHE: the exact polygon writhe agrees with the registered midpoint Gauss integral (strand_calugareanu.writhe)
      on a chiral closed curve to O(M^-2), and is 0 to 1e-14 on a planar polygon.

Usage: python3 benchmarks/foundations/ring_wave_stability.py --credential [--M 16,24,32,48] [--out analysis/...json]
"""
import argparse, json, math, pathlib, sys, time
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import elec_rotator as er
import elec_rope_wave as erw
import strand_calugareanu as sc

ROOT = pathlib.Path(__file__).resolve().parents[2]


# ----------------------------------------------------------------------------------------------------------------
# exact polygon writhe (Klenin and Langowski 2000, method 1a): the Gauss integral of two straight segments in
# closed form as a signed solid angle; summed over non-adjacent pairs. Exact for polygons, zero for planar ones.
# ----------------------------------------------------------------------------------------------------------------
def _unit(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / np.where(n < 1e-300, 1.0, n)


def writhe_exact(X):
    M = len(X)
    i, j = np.triu_indices(M, 2)
    keep = ~((i == 0) & (j == M - 1))
    i, j = i[keep], j[keep]
    p1, p2 = X[i], X[(i + 1) % M]
    p3, p4 = X[j], X[(j + 1) % M]
    r12, r34 = p2 - p1, p4 - p3
    r13, r14, r23, r24 = p3 - p1, p4 - p1, p3 - p2, p4 - p2
    n1 = _unit(np.cross(r13, r14)); n2 = _unit(np.cross(r14, r24))
    n3 = _unit(np.cross(r24, r23)); n4 = _unit(np.cross(r23, r13))
    s = lambda a, b: np.arcsin(np.clip(np.sum(a * b, axis=1), -1.0, 1.0))
    om = s(n1, n2) + s(n2, n3) + s(n3, n4) + s(n4, n1)
    sign = np.sign(np.sum(np.cross(r34, r12) * r13, axis=1))
    return float(np.sum(om * sign) / (2 * math.pi))


# ----------------------------------------------------------------------------------------------------------------
# the generic constrained spectrum
# ----------------------------------------------------------------------------------------------------------------
def fd_grad(f, x, h):
    g = np.zeros_like(x)
    for k in range(len(x)):
        e = np.zeros_like(x); e[k] = h
        g[k] = (f(x + e) - f(x - e)) / (2 * h)
    return g


def fd_jac(cons, x, h):
    c0 = np.atleast_1d(cons(x))
    Jc = np.zeros((len(c0), len(x)))
    for k in range(len(x)):
        e = np.zeros_like(x); e[k] = h
        Jc[:, k] = (np.atleast_1d(cons(x + e)) - np.atleast_1d(cons(x - e))) / (2 * h)
    return c0, Jc


def fd_hess(f, x, h):
    """Symmetric four-point second differences; 2 N^2 + O(N) evaluations."""
    N = len(x); H = np.zeros((N, N)); f0 = f(x)
    fp = np.zeros(N); fm = np.zeros(N)
    for k in range(N):
        e = np.zeros(N); e[k] = h
        fp[k] = f(x + e); fm[k] = f(x - e)
        H[k, k] = (fp[k] - 2 * f0 + fm[k]) / h ** 2
    for a in range(N):
        ea = np.zeros(N); ea[a] = h
        for b in range(a + 1, N):
            eb = np.zeros(N); eb[b] = h
            v = (f(x + ea + eb) - f(x + ea - eb) - f(x - ea + eb) + f(x - ea - eb)) / (4 * h * h)
            H[a, b] = H[b, a] = v
    return H


def fd_hess_rich(f, x, h):
    """Richardson-extrapolated FD Hessian: (4 H_{h/2} - H_h) / 3 removes the h^2 truncation term. At M = 48 on the
    Michell ring the plain h = 1e-3 l0 Hessian biased Lk_c by +1.3e-3 against h = 5e-4 l0 (2026-10-26); the
    extrapolated form is the instrument's default."""
    return (4.0 * fd_hess(f, x, 0.5 * h) - fd_hess(f, x, h)) / 3.0


def constrained_spectrum(f, cons, x, length, h=1e-4, gens=None, null_tol=1e-6, hess=None, rich=True):
    """Returns the stationarity measure, multipliers, and the spectrum of the Lagrangian Hessian on the constraint
    tangent space with the generators (columns of gens, N x k) removed. hess: optional callable x -> Hessian of
    f - lambda . cons (for a cheaper analytic or structured path); default is the finite-difference Hessian."""
    x = np.asarray(x, float); N = len(x)
    g = fd_grad(f, x, h)
    c0, Jc = fd_jac(cons, x, h)
    lam, *_ = np.linalg.lstsq(Jc.T, g, rcond=None)
    r = g - Jc.T @ lam
    E0 = f(x)
    S = float(np.linalg.norm(r) * length / abs(E0)) if E0 else float('nan')
    L = (lambda y: f(y) - float(lam @ np.atleast_1d(cons(y))))
    H = (fd_hess_rich(L, x, h) if rich else fd_hess(L, x, h)) if hess is None else hess(x, lam)
    # tangent space of the constraints
    U, s, Vt = np.linalg.svd(Jc, full_matrices=True)
    rank = int(np.sum(s > 1e-9 * max(1.0, s[0])))
    Z = Vt[rank:].T                                           # N x (N - rank)
    if gens is not None and gens.shape[1]:
        G = Z @ (Z.T @ gens)                                  # the generators projected into the tangent space
        Q, _ = np.linalg.qr(G)
        Z = Z - Q @ (Q.T @ Z)
        Zq, Zs, _ = np.linalg.svd(Z, full_matrices=False)
        Z = Zq[:, Zs > 1e-8]
    W = Z.T @ H @ Z; W = 0.5 * (W + W.T)
    ev, vec = np.linalg.eigh(W)
    scale = max(1.0, float(np.max(np.abs(ev))))
    nneg = int(np.sum(ev < -null_tol * scale)); nnull = int(np.sum(np.abs(ev) <= null_tol * scale))
    return dict(S=S, E=E0, grad_norm=float(np.linalg.norm(g)), resid_norm=float(np.linalg.norm(r)), lam=lam,
                cons_viol=float(np.max(np.abs(c0))), eig=ev, modes=Z @ vec, nneg=nneg, nnull=nnull, npos=len(ev) - nneg - nnull,
                dim=len(ev), H=H, Z=Z)


def rigid_generators(X):
    """Translations and rotations of a node polygon as N-vectors (N = 3 M)."""
    M = len(X); G = []
    for a in range(3):
        v = np.zeros((M, 3)); v[:, a] = 1.0; G.append(v.ravel())
    for a in range(3):
        w = np.zeros(3); w[a] = 1.0; G.append(np.cross(w, X).ravel())
    return np.array(G).T


def tangential_generators(X):
    """Sliding of each node along its local tangent (reparametrization of a tension rope): M vectors."""
    M = len(X); t = _unit(np.roll(X, -1, 0) - np.roll(X, 1, 0)); G = []
    for k in range(M):
        v = np.zeros((M, 3)); v[k] = t[k]; G.append(v.ravel())
    return np.array(G).T


# ----------------------------------------------------------------------------------------------------------------
# K1: the Michell ring
# ----------------------------------------------------------------------------------------------------------------
def circle(M, R=1.0):
    th = 2 * math.pi * np.arange(M) / M
    return np.stack([R * np.cos(th), R * np.sin(th), np.zeros(M)], axis=1)


def michell_energy(X, B, C, Lk):
    seg = np.roll(X, -1, 0) - X
    ell = np.linalg.norm(seg, axis=1); t = seg / ell[:, None]
    L = float(ell.sum()); l0 = L / len(X)
    Eb = (B / l0) * float(np.sum(1.0 - np.sum(t * np.roll(t, -1, 0), axis=1)))
    Wr = writhe_exact(X)
    Etw = 2 * math.pi ** 2 * C * (Lk - Wr) ** 2 / L
    return Eb + Etw


def michell_cons(X, l0):
    return np.linalg.norm(np.roll(X, -1, 0) - X, axis=1) - l0


def michell_spectrum(M, B, C, Lk, h=None):
    X0 = circle(M); l0 = 2 * math.pi / M
    h = 1e-3 * l0 if h is None else h                         # the FD step scales with the segment, so the truncation floor does not grow with M
    f = lambda y: michell_energy(y.reshape(M, 3), B, C, Lk)
    cons = lambda y: michell_cons(y.reshape(M, 3), l0)
    return constrained_spectrum(f, cons, X0.ravel(), 2 * math.pi, h=h, gens=rigid_generators(X0))


def mode_wavenumber(X0, v):
    """Dominant azimuthal wavenumber of the out-of-plane part of a mode (the circle's Fourier content)."""
    M = len(X0); dz = v.reshape(M, 3)[:, 2]
    if np.linalg.norm(dz) < 1e-6 * np.linalg.norm(v):
        return -1, 0.0
    F = np.abs(np.fft.rfft(dz)); n = int(np.argmax(F[1:]) + 1)
    return n, float(np.linalg.norm(dz) / np.linalg.norm(v))


def michell_threshold(M, B, C, h=None, verbose=True):
    """Lk_c from the spectrum. At the circle Wr = 0 and grad Wr = 0 (reflection parity), so the Lagrangian Hessian
    is exactly linear in Lk: W(Lk) = W0 + Lk (W1 - W0). The instrument computes the Hessian at Lk = 0 and 1 by the
    generic path, CHECKS the linearity at Lk = 2 (a third generic Hessian), and finds the crossing of the lowest
    eigenvalue of the pencil by a root find. Reported: Lk_c, the crossing mode's wavenumber, the linearity residual."""
    t0 = time.time()
    s0 = michell_spectrum(M, B, C, 0.0, h); s1 = michell_spectrum(M, B, C, 1.0, h); s2 = michell_spectrum(M, B, C, 2.0, h)
    Z = s0['Z']
    W0 = Z.T @ s0['H'] @ Z; W1 = Z.T @ s1['H'] @ Z; W2 = Z.T @ s2['H'] @ Z
    lin = float(np.linalg.norm(W2 - (2 * W1 - W0)) / np.linalg.norm(W1 - W0))
    D = W1 - W0

    def lam_min(Lk):
        return float(np.linalg.eigvalsh(0.5 * ((W0 + Lk * D) + (W0 + Lk * D).T))[0])

    from scipy.optimize import brentq
    a, b = 0.0, 1.0
    while lam_min(b) > 0 and b < 50:
        a, b = b, 2 * b
    Lk_c = brentq(lam_min, a, b, xtol=1e-10)
    Wc = W0 + Lk_c * D; ev, vec = np.linalg.eigh(0.5 * (Wc + Wc.T))
    n, zfrac = mode_wavenumber(circle(M), Z @ vec[:, 0])
    out = dict(M=M, B=B, C=C, Lk_c=Lk_c, Lk_c_theory=math.sqrt(3) * B / C, mode_n=n, mode_zfrac=zfrac, linearity=lin,
               S_circle=s1['S'], cons_viol=s1['cons_viol'], nnull_at_Lk1=s1['nnull'], nneg_at_Lk0=s0['nneg'], nneg_at_Lk1=s1['nneg'],
               dim=s1['dim'], seconds=time.time() - t0)
    if verbose:
        print(f"  Michell M {M:4d} B/C {B / C:.3f}: Lk_c {Lk_c:.6f} (theory {out['Lk_c_theory']:.6f}, rel {Lk_c / out['Lk_c_theory'] - 1:+.2e})  "
              f"mode n={n} zfrac {zfrac:.3f}  linearity {lin:.1e}  S(circle) {s1['S']:.1e}  nneg(Lk 0) {s0['nneg']} nnull {s1['nnull']} dim {s1['dim']}  {out['seconds']:.0f}s", flush=True)
    return out


def richardson(Ms, vals):
    """Fit v(M) = v_inf + a M^-p to all points (least squares over p on a grid, linear in v_inf and a); returns
    v_inf, p and the fit's rms residual. With two points p = 2 is assumed."""
    Ms = np.asarray(Ms, float); vals = np.asarray(vals, float)
    if len(Ms) == 2:
        a = (vals[0] - vals[1]) / (Ms[0] ** -2 - Ms[1] ** -2); return float(vals[1] - a * Ms[1] ** -2), 2.0, 0.0
    best = None
    for p in np.linspace(1.0, 4.0, 601):
        A = np.stack([np.ones_like(Ms), Ms ** -p], 1); coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
        res = float(np.sqrt(np.mean((A @ coef - vals) ** 2)))
        if best is None or res < best[2]:
            best = (float(coef[0]), float(p), res)
    return best


# ----------------------------------------------------------------------------------------------------------------
# K2: the stationarity ceiling reports what it is handed
# ----------------------------------------------------------------------------------------------------------------
def stationarity_probe(M, B, C, Lk, amps, h=None):
    l0 = 2 * math.pi / M; h = 1e-3 * l0 if h is None else h; X0 = circle(M); th = 2 * math.pi * np.arange(M) / M
    f = lambda y: michell_energy(y.reshape(M, 3), B, C, Lk)
    cons = lambda y: michell_cons(y.reshape(M, 3), l0)
    rows = []
    for a in amps:
        X = X0.copy(); X[:, 2] += a * np.cos(3 * th)
        g = fd_grad(f, X.ravel(), h); c0, Jc = fd_jac(cons, X.ravel(), h)
        lam, *_ = np.linalg.lstsq(Jc.T, g, rcond=None); r = g - Jc.T @ lam
        S = float(np.linalg.norm(r) * 2 * math.pi / f(X.ravel()))
        rows.append(dict(amp=a, S=S))
    return rows


# ----------------------------------------------------------------------------------------------------------------
# K3: the rope wiring (elec_rope_wave energetics on a node polygon; Omega eliminated by the J root find)
# ----------------------------------------------------------------------------------------------------------------
def pieces_nodes(Xn, Omega, beta, kappa_tw, kappa_C):
    """elec_rope_wave.pieces with the curve given as nodes. Copies its arithmetic line for line on cs = [X - mean]."""
    T = erw.T; A_SMEAR = erw.A_SMEAR
    cs = [Xn - Xn.mean(0)]
    g = er.geometry(cs, Omega)[0]
    ds = g['ds']; L = float(ds.sum())
    phip = 2 * math.pi / L
    eps_w = 0.5 * kappa_tw * phip ** 2 * (1.0 + beta ** 2)
    w = g['sgint'] * g['sds']
    E_t = T * float(np.sum(w)); E_w = eps_w * float(np.sum(w)); dens = T + eps_w
    J_mat = dens * float(np.sum(w * g['spxv']))
    P_mat = dens * np.sum(w[..., None] * g['svp'], axis=(0, 1))
    tpx = g['mid'][:, 0] * g['t'][:, 1] - g['mid'][:, 1] * g['t'][:, 0]
    J_flux = eps_w * beta * float(np.sum(tpx * ds)); P_flux = eps_w * beta * np.sum(g['t'] * ds[:, None], axis=0)
    J = J_mat + J_flux; Pm = P_mat + P_flux
    Jvec = dens * np.sum((w[..., None] * np.cross(g['smid'], g['svp'])), axis=(0, 1)) + eps_w * beta * np.sum(np.cross(g['mid'], g['t']) * ds[:, None], axis=0)
    q = ds / L; mid = g['mid']; vp = g['vperp'][:, :2]
    mu = 0.5 * float(np.sum(q * (mid[:, 0] * vp[:, 1] - mid[:, 1] * vp[:, 0]))) + 0.5 * beta * float(np.sum(q * tpx))
    from scipy.special import erf
    P = mid; d = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=2); iu = np.triu_indices(len(P), 1); r = d[iu]
    E_C = kappa_C * (np.sum(q[iu[0]] * q[iu[1]] * erf(r / (2 * A_SMEAR)) / r) + np.sum(q ** 2) / (2 * A_SMEAR * math.sqrt(math.pi)))
    over = np.sum((np.clip(g['sv2'] - er.VSOFT, 0, None) / er.WALL) ** 2) * ds.mean()
    return dict(E=E_t + E_w + float(E_C), E_t=E_t, E_w=E_w, E_C=float(E_C), J=J, Pm=Pm, Jvec=Jvec, mu=mu, over=over, L=L,
                g=(mu / J) * 2 * (E_t + E_w + float(E_C)) if J else float('nan'), edge=float(math.sqrt(g['sv2max'])))


def omega_nodes(Xn, J_t, beta, kappa_tw, kappa_C):
    from scipy.optimize import brentq
    c = Xn - Xn.mean(0); rmax = float(np.max(np.hypot(c[:, 0], c[:, 1])))
    Om_hi = math.sqrt(er.VSOFT) / max(rmax, 1e-9)
    f = lambda Om: pieces_nodes(Xn, Om, beta, kappa_tw, kappa_C)['J'] - J_t
    j0 = f(0.0)
    if j0 > -1e-9 * J_t:
        return 0.0
    if f(Om_hi) < 0:
        return Om_hi
    return brentq(f, 0.0, Om_hi, xtol=1e-12, rtol=1e-12, maxiter=200)


def rope_functions(J_t, beta, kappa_tw, kappa_C, M, w_wall=1e3):
    """f(y) = E + wall at the Omega that delivers J; cons(y) = (Jvec_x, Jvec_y, P_x, P_y) = 0 (rest frame, J on the axis)."""
    def f(y):
        X = y.reshape(M, 3); Om = omega_nodes(X, J_t, beta, kappa_tw, kappa_C)
        p = pieces_nodes(X, Om, beta, kappa_tw, kappa_C)
        return p['E'] + w_wall * p['over']

    def cons(y):
        X = y.reshape(M, 3); Om = omega_nodes(X, J_t, beta, kappa_tw, kappa_C)
        p = pieces_nodes(X, Om, beta, kappa_tw, kappa_C)
        return np.array([p['Jvec'][0], p['Jvec'][1], p['Pm'][0], p['Pm'][1]])
    return f, cons


def rope_spectrum(Xn, J_t, beta, kappa_tw, kappa_C, h=1e-4, drop_tangential=True):
    M = len(Xn); f, cons = rope_functions(J_t, beta, kappa_tw, kappa_C, M)
    G = [rigid_generators(Xn)]
    if drop_tangential:
        G.append(tangential_generators(Xn))
    gens = np.hstack(G)
    Om = omega_nodes(Xn, J_t, beta, kappa_tw, kappa_C); p = pieces_nodes(Xn, Om, beta, kappa_tw, kappa_C)
    return constrained_spectrum(f, cons, Xn.ravel(), p['L'], h=h, gens=gens), p


def wiring_check(M=48):
    """pieces_nodes against elec_rope_wave.pieces on the same (non-circular) polygon."""
    B = er.basis(M); z = er.z_init(1.0, seed=3, amp=0.05)
    X = er.curves(z, M, B, True)[0]
    worst = 0.0
    for beta in (0.0, 0.6, 1.0):
        for Om in (0.0, 0.3):
            a = erw.pieces(z, Om, beta, 0.5, math.pi / 137.035999, M, B); b = pieces_nodes(X, Om, beta, 0.5, math.pi / 137.035999)
            for k in ('E', 'E_t', 'E_w', 'E_C', 'J', 'mu', 'L'):
                worst = max(worst, abs(a[k] - b[k]) / max(1e-300, abs(a[k])))
            worst = max(worst, float(np.max(np.abs(a['Jvec'] - b['Jvec']))), float(np.max(np.abs(a['Pm'] - b['Pm']))))
    return worst


def fold_reading(M=48, kappa_tw=0.5, J_t=math.pi, h=1e-4, maxiter=3000):
    """The co-moving fold (beta_p = 0) re-minimized in the Fourier space of the record, then read in node space."""
    kappa_C = math.pi / 137.035999
    o = erw.solve(J_t, 0.0, kappa_tw, kappa_C, M=M, seed='flat', maxiter=maxiter, verbose=True)
    z = np.array(o['z']); X = er.curves(z, M, er.basis(M), True)[0]
    t0 = time.time()
    spec, p = rope_spectrum(X, J_t, 0.0, kappa_tw, kappa_C, h=h)
    ev = spec['eig']
    out = dict(M=M, kappa_tw=kappa_tw, J=J_t, beta=0.0, E=p['E'], g=p['g'], edge=p['edge'], R_end=o['R_end'], fourier_nit=o['nit'],
               S_nodes=spec['S'], cons_viol=spec['cons_viol'], nneg=spec['nneg'], nnull=spec['nnull'], npos=spec['npos'], dim=spec['dim'],
               eig_low=[float(v) for v in ev[:8]], eig_high=float(ev[-1]), seconds=time.time() - t0)
    print(f"  fold reading M {M}: E {p['E']:.5f} g {p['g']:.4f} edge {p['edge']:.5f}  S(nodes) {spec['S']:.3e}  spectrum dim {spec['dim']}: "
          f"neg {spec['nneg']} null {spec['nnull']} pos {spec['npos']}  lowest {ev[:4]}  highest {ev[-1]:.2e}  {out['seconds']:.0f}s", flush=True)
    return out


# ----------------------------------------------------------------------------------------------------------------
def credential(Ms=(16, 24, 32, 48), ratios=(1.0, 0.6), do_fold=True, out=None):
    rec = dict(date='2026-10-26', instrument='benchmarks/foundations/ring_wave_stability.py', Ms=list(Ms))
    print('K4 writhe: exact polygon formula against the registered midpoint integral and a planar polygon')
    th = 2 * math.pi * np.arange(96) / 96
    chiral = np.stack([np.cos(th) + 0.3 * np.cos(2 * th), np.sin(th) - 0.2 * np.sin(3 * th), 0.4 * np.sin(2 * th) + 0.15 * np.cos(5 * th)], 1)
    w_planar = abs(writhe_exact(circle(64)))
    rows = []
    for M in (48, 96, 192, 384):
        thM = 2 * math.pi * np.arange(M) / M
        XM = np.stack([np.cos(thM) + 0.3 * np.cos(2 * thM), np.sin(thM) - 0.2 * np.sin(3 * thM), 0.4 * np.sin(2 * thM) + 0.15 * np.cos(5 * thM)], 1)
        rows.append(dict(M=M, exact=writhe_exact(XM), registered=sc.writhe(XM)))
        print(f"  M {M:4d}: exact {rows[-1]['exact']:.8f}  registered midpoint {rows[-1]['registered']:.8f}  diff {rows[-1]['exact'] - rows[-1]['registered']:+.2e}")
    rec['K4'] = dict(planar=w_planar, rows=rows)
    print(f"  planar polygon writhe {w_planar:.1e}")

    print('K1 Michell: Lk_c from the constrained spectrum, two B / C, convergence in M')
    rec['K1'] = {}
    for ratio in ratios:
        res = [michell_threshold(M, ratio, 1.0) for M in Ms]
        vals = [r['Lk_c'] for r in res]
        v_inf, p, fitres = richardson(Ms, vals)
        theory = math.sqrt(3) * ratio
        print(f"  B/C {ratio}: Lk_c(M) {[round(v, 6) for v in vals]} -> extrapolated {v_inf:.6f} (order {p:.2f}, fit rms {fitres:.1e}); theory {theory:.6f}; rel {v_inf / theory - 1:+.2e}")
        rec['K1'][str(ratio)] = dict(rows=res, Lk_c_inf=v_inf, order=p, fit_rms=fitres, theory=theory, rel=v_inf / theory - 1)

    print('K2 stationarity probe (n = 3 ripple on the twisted circle, Lk = 1, B/C = 1)')
    rows = stationarity_probe(48, 1.0, 1.0, 1.0, (0.0, 1e-3, 1e-2, 1e-1))
    for r in rows:
        print(f"  amp {r['amp']:.0e}: S {r['S']:.3e}")
    rec['K2'] = rows

    print('K3 rope wiring: pieces_nodes against elec_rope_wave.pieces')
    w = wiring_check(48); print(f"  worst relative difference {w:.1e}")
    rec['K3'] = dict(wiring_worst=w)
    if do_fold:
        rec['K3']['fold'] = fold_reading(48)

    ok = dict(K4_planar=w_planar < 1e-12, K4_agree=abs(rec['K4']['rows'][-1]['exact'] - rec['K4']['rows'][-1]['registered']) < 1e-3,
              K1=all(abs(v['rel']) < 1e-2 and v['order'] > 1.5 for v in rec['K1'].values()),
              K2_zero=rec['K2'][0]['S'] < 1e-4, K2_monotone=all(rec['K2'][k]['S'] < rec['K2'][k + 1]['S'] for k in range(len(rec['K2']) - 1)),
              K3_wiring=w < 1e-10)
    rec['bars'] = ok
    print('BARS: ' + '  '.join(f"{k} {'PASS' if v else 'FAIL'}" for k, v in ok.items()))
    if out:
        pathlib.Path(out).write_text(json.dumps(rec, indent=1, default=float))
        print(f"  record -> {out}")
    return rec


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--credential', action='store_true')
    ap.add_argument('--M', type=str, default='16,24,32,48')
    ap.add_argument('--ratios', type=str, default='1.0,0.6')
    ap.add_argument('--no-fold', action='store_true')
    ap.add_argument('--out', type=str, default=None)
    a = ap.parse_args()
    if a.credential:
        credential(tuple(int(m) for m in a.M.split(',')), tuple(float(r) for r in a.ratios.split(',')), not a.no_fold, a.out)
