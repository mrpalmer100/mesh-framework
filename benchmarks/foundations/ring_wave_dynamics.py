"""RING-WAVE-STABILITY Leg 0, part 2: the DYNAMICS instrument for a closed rope carrying a twist field, and its
credential on known answers only (executor, sandbox, 2026-10-26). The ring-wave evidence cell (a PERTURBED ring-wave
followed for growth) is never run here; the unperturbed exact solution is integrated for two periods as a
conservation check, which is the Director's named known answer, and no growth is read from it.

THE ACTION (c = 1, T = 1 units; kappa the twist stiffness of GRV-020's Goldstone energy (kappa / 2) Phi'^2)
  S = - Int d^2 sigma sqrt(-h) [ T + (kappa / 2) h^ab d_a Phi d_b Phi ],   h_ab the string's induced metric.
This is the "scalar on the induced metric" form, the one Leg C's static functional (elec_rope_wave.py) is the
Routhian of: at rest the twist energy is (kappa / 2)(Phi'^2 + Phi-dot^2) per proper length, and the energy flux
of a travelling twist is its momentum (EM-019). Static gauge tau = t and ARC-LENGTH gauge sigma = s (|x'| = 1,
imposed as the holonomic constraint that all segments have equal length) give the Lagrangian density
  L = - sqrt(1 - v_perp^2) + (kappa / 2) [ Phi-dot^2 - 2 (x-dot . t) Phi-dot Phi' - (1 - x-dot^2) Phi'^2 ] / sqrt(1 - v_perp^2),
with t the unit tangent and v_perp the transverse velocity. The arc-length gauge removes the reparametrization
freedom (a node's tangential velocity is fixed by the equal-spacing constraint), so every remaining degree of
freedom is physical: 2M + 1 for the shape (transverse displacements and the total length) and M for the twist.
The static ring with its twist travelling at c, Phi = (s - t) / R, is a stationary solution at R^2 = kappa / T
(dL / dR = 2 pi [-1 + kappa / R^2] = 0): the centripetal balance of the wave momentum against the tension, which is
Leg C's virial.

A DIFFERENT THEORY, named so the charter can ask the registry which one it holds: Nambu-Goto in five dimensions,
S = -T Int sqrt(-det(d X . d X + (kappa / T) d Phi d Phi)), treats the twist as a fifth target coordinate; it agrees
with the form above to first order in kappa Phi'^2 / T and differs at O(1), and the ring-wave sits at
kappa Phi'^2 / T = 1 exactly. The instrument implements the induced-metric form; the lab's theorist must say
whether GRV-020 / EM-RECON-012 / EM-019 fix the form, before any evidence run.

THE INTEGRATOR: a variational (discrete Euler-Lagrange) integrator with the midpoint discrete Lagrangian
L_d(q_a, q_b) = h L((q_a + q_b) / 2, (q_b - q_a) / h) and the holonomic constraints enforced at every step
(Marsden-West constrained DEL, the SHAKE structure): D2 L_d(q_k-1, q_k) + D1 L_d(q_k, q_k+1) + G(q_k)^T lambda_k = 0,
g(q_k+1) = 0, solved by Newton with the Jacobian from JAX. The discrete Lagrangian inherits the continuous
symmetries exactly (translations, rotations about any axis, Phi -> Phi + const), so linear momentum, angular
momentum and the twist charge are conserved to roundoff and the energy oscillates boundedly at O(h^2): those are
the known answers K4 of the credential.

KNOWN ANSWERS (Leg 0 part 2)
  K1  Twist wave on a frozen ring: with the shape held, Phi obeys the wave equation; the mode n period is
      2 pi R / n (c = 1) and the energy is conserved. Discrete dispersion as the bar.
  K2  The Nambu-Goto pulsating circle (kappa = 0): R(t) = R0 cos(t / R0) exactly, E = 2 pi R0 T conserved; followed
      from R0 to R0 / 2 (the collapse itself is lightlike and not followed).
  K3  The exact ring-wave, unperturbed, for two periods: E, J, P, winding conserved; the shape stays a circle to the
      discretization tolerance over that span. No growth is read; the span is too short to read one.
  K4  Noether on generic smooth data without the gauge pin: P and J exact, E drift of order h^2 (order measured);
      with the pin, the torque it exerts on fast generic data is reported (the pin's price).
  K5  Leg C's shape theorem on the beta = 0.5 family member: a deformed static loop with its twist travelling is
      stationary (kappa Phi-dot Phi' = T balances tension locally for any shape); the deformation does not move
      at first order in eps. Not the beta = 1 evidence cell.

THE GAUGE PIN: the equal-spacing constraints leave one collective sliding mode (all nodes moving along the loop),
pure gauge in the continuum and nearly so here; the discrete Lagrangian gives it a tiny inertia, and on perturbed
data it ran away (node speeds of 16 c by t = 1 at M = 16). It is pinned by one holonomic constraint on node 0
((x_0 - centroid) . y = const). The pin exerts a torque at the discretization level, so J is a bar on every run.

Usage: python3 benchmarks/foundations/ring_wave_dynamics.py --credential [--M 48] [--out analysis/...json]
"""
import argparse, json, math, pathlib, sys, time
import numpy as np

try:
    import jax, jax.numpy as jnp
    jax.config.update('jax_enable_x64', True)
except ImportError:                                       # the instrument needs JAX (pip install jax)
    jax = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = 1.0


# ----------------------------------------------------------------------------------------------------------------
# fields: q = (X.ravel() [3M], Phi [M]); Phi stored unwrapped with winding n (Phi_{i+M} = Phi_i + 2 pi n)
# ----------------------------------------------------------------------------------------------------------------
def make_lagrangian(M, kappa, winding, gauge_ref=None, lock=0.0):
    """gauge_ref: if not None, the value of (x_0 - centroid) . y-hat that a gauge constraint holds fixed. The
    equal-spacing constraints leave one sliding mode (all nodes moving along the loop together, a relabelling):
    exactly null for the pure string (kappa = 0), where it must be pinned, and merely soft for kappa > 0, where the
    twist's transport gives it a small inertia and the Newton system is regular. The pin breaks rotational
    symmetry about z (it exerts a torque on generic data), so it is used only where the data's symmetry makes it
    torque-free (kappa = 0 tests) and never on generic data."""
    two_pi_n = 2 * math.pi * winding

    def split(q):
        return q[:3 * M].reshape(M, 3), q[3 * M:]

    def lagrangian(q, qd):
        X, P = split(q); U, W = split(qd)
        Xp = jnp.roll(X, -1, 0); Xm = jnp.roll(X, 1, 0)
        Pp = jnp.roll(P, -1) + jnp.where(jnp.arange(M) == M - 1, two_pi_n, 0.0)
        Pm = jnp.roll(P, 1) - jnp.where(jnp.arange(M) == 0, two_pi_n, 0.0)
        dp = jnp.linalg.norm(Xp - X, axis=1); dm = jnp.linalg.norm(X - Xm, axis=1)
        ell = 0.5 * (dp + dm)                                          # node-centred length
        chord = Xp - Xm; t = chord / jnp.linalg.norm(chord, axis=1, keepdims=True)
        sp = (Pp - P) / dp; sm = (P - Pm) / dm                         # the two adjacent segment slopes
        Phip = 0.5 * (sp + sm)                                         # for the mixed term
        Phip2 = 0.5 * (sp ** 2 + sm ** 2)                              # the gradient energy: three-point, no checkerboard mode
        vpar = jnp.sum(U * t, axis=1); u2 = jnp.sum(U * U, axis=1)
        vperp2 = jnp.clip(u2 - vpar ** 2, 0.0, 1.0 - 1e-12)
        g = 1.0 / jnp.sqrt(1.0 - vperp2)
        f = -T / g + 0.5 * kappa * g * (W ** 2 - 2.0 * vpar * W * Phip - (1.0 - u2) * Phip2)
        f = f - lock * (1.0 - jnp.cos(P))                                # SWEEP's lock, V'' per length (2026-10-27); 0 by default
        return jnp.sum(ell * f)

    def constraints(q):
        X, _ = split(q)
        d2 = jnp.sum((jnp.roll(X, -1, 0) - X) ** 2, axis=1)
        eq = d2[1:] - d2[:-1]                                          # equal spacing (M - 1)
        if gauge_ref is None:
            return eq
        return jnp.concatenate([eq, jnp.array([(X[0] - X.mean(0))[1] - gauge_ref])])

    return lagrangian, constraints, split


class StringIntegrator:
    def __init__(self, M, kappa, winding, h, q0, freeze_shape=False, freeze_twist=False, gauge_pin=None, lock=0.0):
        if jax is None:
            raise RuntimeError('JAX is required: pip install jax')
        self.M, self.kappa, self.winding, self.h, self.freeze, self.freeze_twist = M, kappa, winding, h, freeze_shape, freeze_twist
        if gauge_pin is None:
            gauge_pin = True            # 2026-10-26: without the pin the sliding mode ran away on perturbed data (node speeds
                                        # of 16 c on the beta = 0.5 member by t = 1); with it the price is a small torque,
                                        # measured by the J bar of every run (K4 reports both)
        X0 = np.asarray(q0)[:3 * M].reshape(M, 3); gauge_ref = float((X0[0] - X0.mean(0))[1]) if gauge_pin else None
        Lf, gf, self.split = make_lagrangian(M, kappa, winding, gauge_ref, lock)
        N = 4 * M
        if freeze_shape:
            gf = lambda q: jnp.zeros(0)
        nc = 0 if freeze_shape else (M if gauge_pin else M - 1)
        self.N, self.nc = N, nc
        self.L, self.g = Lf, gf

        def Ld(qa, qb):
            return h * Lf(0.5 * (qa + qb), (qb - qa) / h)
        D1 = jax.grad(Ld, 0); D2 = jax.grad(Ld, 1)
        G = jax.jacfwd(gf)
        mask = jnp.concatenate([jnp.zeros(3 * M) if freeze_shape else jnp.ones(3 * M), jnp.zeros(M) if freeze_twist else jnp.ones(M)])
        self.mask = mask

        def F(z, qprev, q):
            qn = z[:N]; lam = z[N:]
            r = D2(qprev, q) + D1(q, qn) + (G(q).T @ lam if nc else 0.0)
            r = jnp.where(mask > 0, r, qn - q)                         # frozen coordinates: q_{k+1} = q_k
            return jnp.concatenate([r, gf(qn)])
        self.F = jax.jit(F); self.JF = jax.jit(jax.jacfwd(F, 0))
        self.D1, self.D2 = jax.jit(D1), jax.jit(D2)
        self.pL = jax.jit(jax.grad(Lf, 1))                              # continuous momentum dL / dq-dot
        self.Lj = jax.jit(Lf)
        self.Gj = jax.jit(G)

    def init(self, q0, v0):
        """First step from a position and velocity: p0 = dL/dq-dot(q0, v0) = -D1 Ld(q0, q1) + G^T lambda, g(q1) = 0."""
        q0 = jnp.asarray(q0); v0 = jnp.asarray(v0); N = self.N
        p0 = self.pL(q0, v0); mask = self.mask

        def F0(z):
            q1 = z[:N]; lam = z[N:]
            r = p0 + self.D1(q0, q1) + (self.Gj(q0).T @ lam if self.nc else 0.0)
            r = jnp.where(mask > 0, r, q1 - q0)
            return jnp.concatenate([r, self.g(q1)])
        J0 = jax.jacfwd(F0)
        z = jnp.concatenate([q0 + self.h * v0, jnp.zeros(self.nc)])
        for _ in range(30):
            r = F0(z)
            if float(jnp.max(jnp.abs(r))) < 1e-12:
                break
            z = z - jnp.linalg.solve(J0(z), r)
        self.qprev, self.q = q0, z[:N]
        self.t = self.h
        return self

    def step(self):
        z = jnp.concatenate([2 * self.q - self.qprev, jnp.zeros(self.nc)])
        for it in range(30):
            r = self.F(z, self.qprev, self.q)
            if float(jnp.max(jnp.abs(r))) < 1e-13:
                break
            z = z - jnp.linalg.solve(self.JF(z, self.qprev, self.q), r)
        else:
            raise RuntimeError(f'Newton did not converge at t = {self.t:.4f} (residual {float(jnp.max(jnp.abs(r))):.2e})')
        self.qprev, self.q = self.q, z[:self.N]
        self.t += self.h
        return self

    # observables at the midpoint of the last step (where the discrete momentum lives)
    def observables(self):
        qm = 0.5 * (self.qprev + self.q); qd = (self.q - self.qprev) / self.h
        p = self.pL(qm, qd)
        X, Phi = self.split(np.asarray(qm)); pX, pPhi = self.split(np.asarray(p))
        E = float(jnp.dot(p, qd) - self.Lj(qm, qd))
        # the DISCRETE momentum p_k = D2 L_d(q_{k-1}, q_k) at q_k: the quantity the discrete Noether theorem conserves
        # exactly for every symmetry of L_d (translations, rotations, Phi shifts); the midpoint continuous momentum
        # above agrees with it for translations and differs at O(h^2) for rotations
        pd = self.D2(self.qprev, self.q); Xk, _ = self.split(np.asarray(self.q)); pdX, pdPhi = self.split(np.asarray(pd))
        P = pdX.sum(0); J = np.cross(Xk, pdX).sum(0)
        Q = float(pdPhi.sum())                                          # the twist charge (Phi -> Phi + const)
        R = np.linalg.norm(X - X.mean(0), axis=1)
        seg = np.linalg.norm(np.roll(X, -1, 0) - X, axis=1)
        return dict(t=self.t - 0.5 * self.h, E=E, P=P.tolist(), J=J.tolist(), Q=Q, R_mean=float(R.mean()), R_spread=float(R.max() - R.min()),
                    L=float(seg.sum()), seg_spread=float(seg.max() - seg.min()))


# ----------------------------------------------------------------------------------------------------------------
# initial data
# ----------------------------------------------------------------------------------------------------------------
def ring(M, R, winding=1, phase_speed=-1.0, Phi0=0.0):
    """Static circle of radius R with Phi = winding * s / R + Phi0, travelling at phase_speed (Phi-dot = phase_speed * winding / R)."""
    th = 2 * math.pi * np.arange(M) / M
    X = np.stack([R * np.cos(th), R * np.sin(th), np.zeros(M)], 1)
    Phi = winding * th + Phi0
    q = np.concatenate([X.ravel(), Phi]); v = np.concatenate([np.zeros(3 * M), np.full(M, phase_speed * winding / R)])
    return q, v


def discrete_ring_radius(M, kappa, winding=1, beta=1.0):
    """The polygon's own equilibrium radius for the travelling twist at phase speed beta (Phi-dot = -beta winding / R):
    the root of dL_d / dR along uniform scaling. The continuum family is R^2 = kappa (1 + beta^2) / (2 T) (Leg C's
    static ring at beta_p = beta; beta = 1 gives the virial R^2 = kappa / T); the polygon's differs at O(M^-2)."""
    from scipy.optimize import brentq
    Lf, _, _ = make_lagrangian(M, kappa, winding, 0.0)
    Lj = jax.jit(Lf)

    th = jnp.asarray(2 * math.pi * np.arange(M) / M)

    def LR(r, w):                                             # the shape scaled at FIXED velocities (Euler-Lagrange's partial)
        X = jnp.stack([r * jnp.cos(th), r * jnp.sin(th), jnp.zeros(M)], 1)
        q = jnp.concatenate([X.ravel(), winding * th]); v = jnp.concatenate([jnp.zeros(3 * M), jnp.full(M, w)])
        return Lj(q, v)
    dLdR = lambda R: float(jax.grad(LR, 0)(R, -beta * winding / R))
    Rc = math.sqrt(kappa * (1 + beta ** 2) / (2 * T))
    return brentq(dLdR, 0.5 * Rc, 1.5 * Rc, xtol=1e-14)


def equalize(X, iters=200):
    """Move nodes along the polygon until all chords are equal (to 1e-13): resample by arc length, repeat."""
    for _ in range(iters):
        seg = np.linalg.norm(np.roll(X, -1, 0) - X, axis=1)
        if seg.max() - seg.min() < 1e-13:
            break
        s = np.concatenate([[0], np.cumsum(seg)]); Xc = np.vstack([X, X[:1]]); su = np.linspace(0, s[-1], len(X), endpoint=False)
        X = np.stack([np.interp(su, s, Xc[:, a]) for a in range(3)], 1)
    return X


def run(integ, q0, v0, t_end, every=1):
    integ.init(q0, v0); rows = [integ.observables()]
    k = 0
    while integ.t < t_end - 1e-12:
        integ.step(); k += 1
        if k % every == 0:
            rows.append(integ.observables())
    return rows


# ----------------------------------------------------------------------------------------------------------------
# credential
# ----------------------------------------------------------------------------------------------------------------
def k1_twist_wave(M=48, R=1.0, kappa=0.5, n=3, h=None):
    """Frozen ring, Phi = standing wave cos(n theta) of amplitude a on top of winding 0: period 2 pi R / n."""
    h = h or 0.02 * 2 * math.pi * R / M
    th = 2 * math.pi * np.arange(M) / M
    X = np.stack([R * np.cos(th), R * np.sin(th), np.zeros(M)], 1)
    a = 0.1
    q0 = np.concatenate([X.ravel(), a * np.cos(n * th)]); v0 = np.zeros(4 * M)
    integ = StringIntegrator(M, kappa, 0, h, q0, freeze_shape=True)
    period = 2 * math.pi * R / n
    rows = run(integ, q0, v0, 1.5 * period, every=1)
    # the Phi field at t = period should return to its initial profile; measure the first return of the mode amplitude
    integ2 = StringIntegrator(M, kappa, 0, h, q0, freeze_shape=True).init(q0, v0)
    amps = []; ts = []
    while integ2.t < 1.2 * period:
        integ2.step(); _, Phi = integ2.split(np.asarray(integ2.q)); amps.append(float(np.dot(Phi, np.cos(n * th)) * 2 / M)); ts.append(integ2.t)
    amps = np.array(amps); ts = np.array(ts)
    # the amplitude is a cos(omega t): fit omega from the first zero crossing (quarter period)
    k = int(np.argmax(amps < 0)); tq = ts[k - 1] + (ts[k] - ts[k - 1]) * amps[k - 1] / (amps[k - 1] - amps[k])
    period_meas = 4 * tq
    # discrete dispersion of the three-point chain on the polygon: omega_d = (2 / l) sin(pi n / M), l the CHORD 2 R sin(pi / M)
    l = 2 * R * math.sin(math.pi / M); omega_d = (2.0 / l) * math.sin(math.pi * n / M); period_disc = 2 * math.pi / omega_d
    E = np.array([r['E'] for r in rows])
    return dict(M=M, n=n, h=h, period_exact=period, period_discrete=period_disc, period_measured=period_meas,
                rel_to_discrete=period_meas / period_disc - 1, rel_to_exact=period_meas / period - 1, E_drift=float((E.max() - E.min()) / abs(E[0])))


def k2_pulsating(M=48, R0=1.0, h=None):
    h = h or 0.01 * 2 * math.pi * R0 / M
    q0, v0 = ring(M, R0, winding=0, phase_speed=0.0)
    integ = StringIntegrator(M, 0.0, 0, h, q0, freeze_twist=True).init(q0, v0)
    rows = [integ.observables()]; worst = 0.0
    while True:
        integ.step(); o = integ.observables(); rows.append(o)
        exact = R0 * math.cos(o['t'] / R0)
        worst = max(worst, abs(o['R_mean'] - exact))
        if exact < 0.5 * R0:
            break
    E = np.array([r['E'] for r in rows])
    return dict(M=M, h=h, t_end=rows[-1]['t'], R_end=rows[-1]['R_mean'], R_exact_end=R0 * math.cos(rows[-1]['t'] / R0), worst_R_error=worst,
                E0=float(E[0]), E_exact=2 * math.pi * R0 * T, E_drift=float((E.max() - E.min()) / abs(E[0])), R_spread_max=max(r['R_spread'] for r in rows))


def k3_ring_wave(M=48, kappa=0.5, h=None, periods=2.0):
    """The exact ring-wave, unperturbed: R* = sqrt(kappa / T), Phi = (s - t) / R*. Conservation over two periods."""
    Rc = math.sqrt(kappa / T); R = discrete_ring_radius(M, kappa); h = h or 0.01 * 2 * math.pi * R / M
    q0, v0 = ring(M, R, winding=1, phase_speed=-1.0)
    integ = StringIntegrator(M, kappa, 1, h, q0)
    rows = run(integ, q0, v0, periods * 2 * math.pi * R, every=5)
    E = np.array([r['E'] for r in rows]); Jz = np.array([r['J'][2] for r in rows]); P = np.array([np.linalg.norm(r['P']) for r in rows])
    Q = np.array([r['Q'] for r in rows])
    return dict(M=M, kappa=kappa, R=R, R_continuum=Rc, h=h, t_end=rows[-1]['t'], E0=float(E[0]), E_closed_form=2 * math.pi * Rc * T + 2 * math.pi * kappa / Rc,
                J0=float(Jz[0]), J_closed_form=2 * math.pi * kappa, E_drift=float((E.max() - E.min()) / abs(E[0])),
                J_drift=float((Jz.max() - Jz.min()) / abs(Jz[0])), P_max=float(P.max()), Q_drift=float(Q.max() - Q.min()),
                R_spread_max=max(r['R_spread'] for r in rows), R_mean_end=rows[-1]['R_mean'], R_mean_drift=float(max(abs(r['R_mean'] - R) for r in rows)), seg_spread_max=max(r['seg_spread'] for r in rows))


def k4_noether(M=32, kappa=0.3, hs=(0.04, 0.02, 0.01)):
    """Generic smooth data (a wobbly loop with a twist pulse and transverse velocity): P, J exact; E drift order h^2."""
    th = 2 * math.pi * np.arange(M) / M
    X = np.stack([np.cos(th) * (1 + 0.15 * np.cos(2 * th)), np.sin(th) * (1 - 0.1 * np.sin(3 * th)), 0.1 * np.sin(2 * th)], 1)
    # equal spacing by arc-length resampling
    seg = np.linalg.norm(np.roll(X, -1, 0) - X, axis=1); s = np.concatenate([[0], np.cumsum(seg)])
    Xc = np.vstack([X, X[:1]]); su = np.linspace(0, s[-1], M, endpoint=False)
    X = np.stack([np.interp(su, s, Xc[:, a]) for a in range(3)], 1)
    Phi = th + 0.3 * np.exp(-((th - math.pi) / 0.6) ** 2)
    V = 0.2 * np.stack([-np.sin(th), np.cos(th), 0.15 * np.cos(3 * th)], 1); W = 0.2 * np.cos(th)
    X = equalize(X)
    q0 = np.concatenate([X.ravel(), Phi]); v0 = np.concatenate([V.ravel(), W])
    rows_out = []
    for h in hs:
        for pin in (False, True):
            integ = StringIntegrator(M, kappa, 1, h, q0, gauge_pin=pin)
            rows = run(integ, q0, v0, 1.0, every=1)
            E = np.array([r['E'] for r in rows]); P = np.array([r['P'] for r in rows]); J = np.array([r['J'] for r in rows]); Q = np.array([r['Q'] for r in rows])
            rows_out.append(dict(h=h, pin=pin, E_drift=float(E.max() - E.min()), P_drift=float(np.max(np.abs(P - P[0]))), J_drift=float(np.max(np.abs(J - J[0]))),
                                 Q_drift=float(Q.max() - Q.min()), steps=len(rows) - 1))
    d = [r['E_drift'] for r in rows_out if not r['pin']]
    order = math.log(d[0] / d[1]) / math.log(hs[0] / hs[1]) if d[1] > 0 else float('nan')
    return dict(M=M, kappa=kappa, rows=rows_out, E_order=order)


def k5_shape_degeneracy(M=48, kappa=0.5, beta=0.5, eps=1e-2, n=3, periods=2.0):
    """Leg C's shape theorem as a dynamical known answer, on the beta = 0.5 FAMILY MEMBER (not the beta = 1 evidence
    cell): a static closed loop of the right length carrying its twist as a travelling wave is stationary for ANY
    shape, because the wave's momentum flux balances the tension locally (kappa Phi-dot Phi' = T at every point,
    which fixes L and nothing else). A radially deformed ring (1 + eps cos n theta) should therefore stay where it is
    to O(eps^2); the residual motion is the second-order breathing of the length mode."""
    R = discrete_ring_radius(M, kappa, 1, beta); q0, v0 = ring(M, R, 1, -beta)
    th = 2 * math.pi * np.arange(M) / M; r = R * (1 + eps * np.cos(n * th))
    X = equalize(np.stack([r * np.cos(th), r * np.sin(th), np.zeros(M)], 1)); q0[:3 * M] = X.ravel()
    h = 0.01 * 2 * math.pi * R / M
    integ = StringIntegrator(M, kappa, 1, h, q0); rows = run(integ, q0, v0, periods * 2 * math.pi * R, every=5)
    X0 = X.copy(); worst = 0.0; vmax = 0.0; dshape = 0.0; k = 0
    integ2 = StringIntegrator(M, kappa, 1, h, q0).init(q0, v0)
    while integ2.t < periods * 2 * math.pi * R:
        integ2.step(); k += 1; Xk, _ = integ2.split(np.asarray(integ2.q)); U = np.asarray((integ2.q - integ2.qprev) / h)[:3 * M].reshape(M, 3)
        worst = max(worst, float(np.linalg.norm(Xk - X0, axis=1).max())); vmax = max(vmax, float(np.linalg.norm(U, axis=1).max()))
        if k % 200 == 0:                                        # the correspondence-free shape distance (K6), sampled
            dshape = max(dshape, shape_distance(Xk, X0)['D_max'])
    J = np.array([r['J'][2] for r in rows]); E = np.array([r['E'] for r in rows])
    return dict(M=M, beta=beta, eps=eps, n=n, R=R, worst_displacement=worst, worst_over_eps2R=worst / (eps ** 2 * R), vmax=vmax,
                D_shape_max=dshape, D_shape_over_epsR=dshape / (eps * R),
                J_drift=float(J.max() - J.min()), E_drift=float((E.max() - E.min()) / abs(E[0])), R_spread0=float(np.ptp(np.hypot(X[:, 0], X[:, 1]))))


# ----------------------------------------------------------------------------------------------------------------
# the shape observable (added 2026-10-27 for RING-WAVE-STABILITY-3, after the external reviewer's round-3 finding on
# the lab's indexed-node Procrustes: in the arc-length gauge the nodes are equally spaced along the loop, so the gauge's
# collective sliding mode moves every node ALONG an unchanged shape, by a fractional number of spacings; an indexed-
# node residual then reports a shape change that is not one, up to half a spacing (0.065 R at M = 48, i.e. 65 eps R
# at eps = 1e-3, far above any hold bar). The distance below is correspondence-free: the reference polygon X0 is
# interpolated trigonometrically in its node index (spectral for the smooth shapes in use), and the residual is
# minimized over a CONTINUOUS index shift s (the slide), a rigid rotation (Kabsch) and a translation. Known-answer
# fixtures K6; the dynamics decide nothing with it until K6 passes.)
# ----------------------------------------------------------------------------------------------------------------
def trig_interp(X0, u):
    """The closed polygon X0 (M x 3, nodes equally spaced) as a trigonometric polynomial in the node index, at the
    real indices u (any shape, periodic in M)."""
    M = len(X0); c = np.fft.rfft(X0, axis=0); n = np.arange(c.shape[0])
    ph = np.exp(2j * math.pi * np.outer(u, n) / M)
    w = np.full(c.shape[0], 2.0); w[0] = 1.0
    if M % 2 == 0:
        w[-1] = 1.0
    return (np.real(ph @ (c * w[:, None])) / M)


def kabsch(X, Y):
    """Rigid alignment of X onto Y (equal index correspondence): returns R, t minimizing sum |R X_i + t - Y_i|^2."""
    cx = X.mean(0); cy = Y.mean(0); H = (X - cx).T @ (Y - cy)
    U, _, Vt = np.linalg.svd(H); d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1.0, 1.0, d]); Rm = Vt.T @ D @ U.T
    return Rm, cy - Rm @ cx


def shape_distance(X, X0, grid_per_node=4, refine_iters=60, project=True):
    """Correspondence-free rigid-invariant distance between the closed polygon X and the reference shape through X0.
    Stage 1 (registration): the rms residual |R X_i + t - C0(i + s)| is minimized over a CONTINUOUS uniform index
    shift s (the arc-length gauge's slide; a grid of grid_per_node per node, then golden-section refinement), with
    the rotation R and translation t by Kabsch at each s. Stage 2 (projection, project=True): with R, t fixed, each
    node's index u_i is refined about i + s to the nearest point of the curve C0 (an equal-chord polygon inscribed in
    a curve at a slid start has index spacings that are uniform only to O(spacing^2), so stage 1 alone carries that
    floor; K6 F1b versus F1c). Returns D_max and D_rms of the projected residual, the uniform-shift residual D_max_uniform,
    and s."""
    M = len(X); idx = np.arange(M)

    def resid(s, want_max=False):
        Y = trig_interp(X0, idx + s); Rm, t = kabsch(X, Y); r = np.linalg.norm(X @ Rm.T + t - Y, axis=1)
        return (float(r.max()), float(np.sqrt(np.mean(r ** 2))), Rm, t) if want_max else float(np.sqrt(np.mean(r ** 2)))
    ss = np.arange(0, M, 1.0 / grid_per_node); vals = np.array([resid(s) for s in ss])
    k = int(np.argmin(vals)); a = ss[k] - 1.0 / grid_per_node; b = ss[k] + 1.0 / grid_per_node
    g = (math.sqrt(5) - 1) / 2; c = b - g * (b - a); d = a + g * (b - a); fc = resid(c); fd = resid(d)
    for _ in range(refine_iters):
        if fc < fd:
            b, d, fd = d, c, fc; c = b - g * (b - a); fc = resid(c)
        else:
            a, c, fc = c, d, fd; d = a + g * (b - a); fd = resid(d)
    s = 0.5 * (a + b); Dmax_u, Drms_u, Rm, t = resid(s, True)
    out = dict(D_max_uniform=Dmax_u, D_rms_uniform=Drms_u, s=float(s % M))
    if not project:
        out.update(D_max=Dmax_u, D_rms=Drms_u); return out
    u = idx + s
    for _ in range(5):                                           # project, then re-fit the rigid motion on the projected correspondences
        Z = X @ Rm.T + t
        lo = u - 0.5; hi = u + 0.5
        f = lambda uu: np.linalg.norm(Z - trig_interp(X0, uu), axis=1)
        c = hi - g * (hi - lo); d = lo + g * (hi - lo); fc = f(c); fd = f(d)
        for _ in range(refine_iters):
            m = fc < fd
            hi = np.where(m, d, hi); lo = np.where(m, lo, c)
            c = hi - g * (hi - lo); d = lo + g * (hi - lo); fc = f(c); fd = f(d)
        u = 0.5 * (lo + hi); Rm, t = kabsch(X, trig_interp(X0, u))
    # joint least squares over the rigid motion and the per-node curve parameters (the ICP above converges only
    # linearly; this finishes it): parameters (rotation vector about Rm, translation, u_i)
    from scipy.optimize import least_squares
    from scipy.spatial.transform import Rotation

    def res(pv):
        Rj = Rotation.from_rotvec(pv[:3]).as_matrix() @ Rm; tj = t + pv[3:6]; uj = pv[6:]
        return (X @ Rj.T + tj - trig_interp(X0, uj)).ravel()
    p0 = np.concatenate([np.zeros(6), u])
    sol = least_squares(res, p0, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
    Rm = Rotation.from_rotvec(sol.x[:3]).as_matrix() @ Rm; t = t + sol.x[3:6]; u = sol.x[6:]
    Z = X @ Rm.T + t; f = lambda uu: np.linalg.norm(Z - trig_interp(X0, uu), axis=1); lo = hi = u
    r = f(0.5 * (lo + hi)); out.update(D_max=float(r.max()), D_rms=float(np.sqrt(np.mean(r ** 2))))
    return out


def indexed_procrustes_distance(X, X0):
    """The defective observable (the lab's round-3 instrument, for the record): Kabsch on index correspondence."""
    Rm, t = kabsch(X, X0)
    return float(np.linalg.norm(X @ Rm.T + t - X0, axis=1).max())


def equalize_spectral(X0, start=0.0, fine=512, iters=200):
    """The equal-chord polygon inscribed in the trigonometric curve through X0 whose first vertex sits at index
    `start` (vertices placed along that curve, sampled fine per node, their arc spacings relaxed until the chords
    agree to 1e-12). The shape is preserved to the fine sampling, where equalize() (piecewise linear) moves nodes
    onto the chords, an O(spacing^2) shape change."""
    M = len(X0); C = trig_interp(X0, start + np.arange(0, M, 1.0 / fine))
    seg = np.linalg.norm(np.roll(C, -1, 0) - C, axis=1); s = np.concatenate([[0], np.cumsum(seg)]); Cc = np.vstack([C, C[:1]])
    a = np.full(M, s[-1] / M)
    for _ in range(iters):
        su = np.concatenate([[0], np.cumsum(a)])[:-1]
        Y = np.stack([np.interp(su, s, Cc[:, k]) for k in range(3)], 1)
        c = np.linalg.norm(np.roll(Y, -1, 0) - Y, axis=1)
        if np.ptp(c) < 1e-12:
            break
        a = a * (c.mean() / c); a *= s[-1] / a.sum()
    return Y


def k6_shape_registration(M=48, R=0.707359, base_eps=0.05, base_n=3, shift_nodes=7, slide=0.37, defo=1e-3, defo_n=5):
    """Known-answer fixtures for shape_distance (exact answers 0, 0, 0, 0, defo * R; bars below):
    F1  the unchanged noncircular polygon under a cyclic relabeling by shift_nodes nodes (bar 1e-10 R);
    F1b the same polygon with its nodes slid along the shape by a FRACTIONAL spacing (slide), re-equalized with the
        instrument's equalize() (piecewise linear, nodes moved onto the chords): an O(spacing^2) shape change made by
        the equalizer, not by the dynamics (whose constraint is the chord length, not a chord placement); recorded
        as the observable's reading of that artifact. Bar 5e-5 R at M = 48 and 6.25e-6 R at M = 96 (M^-3), set on
        2026-10-27 AFTER this fixture's first run (uniform-shift stage only) read 2.8e-5 R and 3.4e-6 R (a credential
        fixture, not an evidence cell; disclosed in the charter);
    F1c the same slide with the nodes kept ON the smooth curve with equal chords (equalize_spectral; bar 1e-8 R):
        the projected distance is exact for a slid equal-chord polygon, where the uniform-shift stage alone reads the
        O(spacing^2) non-uniformity of its index spacings (reported as D_max_uniform);
    F2  relabeling plus a rigid rotation (0.7 rad in plane, 0.1 rad tilt) plus a translation (bar 1e-10 R);
    F3  a genuine deformation, radial defo R cos(defo_n theta), re-equalized (exact defo R to the equalization's
        tangential part; bar: D_max within [0.5, 1.5] defo R, so the registration neither absorbs nor inflates it);
    F4  (informative, no bar) the indexed-node Procrustes on F1 and F1b, the round-3 defect."""
    th = 2 * math.pi * np.arange(M) / M; r = R * (1 + base_eps * np.cos(base_n * th))
    X0 = equalize(np.stack([r * np.cos(th), r * np.sin(th), np.zeros(M)], 1))
    out = dict(M=M, R=R, base_eps=base_eps, base_n=base_n)
    X1 = np.roll(X0, shift_nodes, axis=0); out['F1'] = shape_distance(X1, X0)
    X1b = equalize(trig_interp(X0, np.arange(M) + slide)); out['F1b'] = shape_distance(X1b, X0)
    X1c = equalize_spectral(X0, slide); out['F1c'] = shape_distance(X1c, X0)
    out['F1c_chord_spread'] = float(np.ptp(np.linalg.norm(np.roll(X1c, -1, 0) - X1c, axis=1)))
    ca, sa = math.cos(0.7), math.sin(0.7); cb, sb = math.cos(0.1), math.sin(0.1)
    Rz = np.array([[ca, -sa, 0], [sa, ca, 0], [0, 0, 1]]); Rx = np.array([[1, 0, 0], [0, cb, -sb], [0, sb, cb]])
    X2 = X1 @ (Rx @ Rz).T + np.array([0.3, -0.2, 0.1]); out['F2'] = shape_distance(X2, X0)
    rr = np.hypot(X0[:, 0], X0[:, 1]); tt = np.arctan2(X0[:, 1], X0[:, 0]); r3 = rr * (1 + defo * np.cos(defo_n * tt))
    X3 = equalize(np.stack([r3 * np.cos(tt), r3 * np.sin(tt), np.zeros(M)], 1)); out['F3'] = shape_distance(X3, X0)
    out['F3_exact'] = defo * R; out['F3_indexed'] = float(np.linalg.norm(X3 - X0, axis=1).max())
    out['F4_indexed_F1'] = indexed_procrustes_distance(X1, X0); out['F4_indexed_F1b'] = indexed_procrustes_distance(X1b, X0)
    out['F1b_bar'] = 5e-5 * R * (48.0 / M) ** 3
    # F1b is INFORMATIVE (2026-10-28): its first bar was set after a reading, so it is not a credential bar; the slide
    # reading is credentialed by F1c (prospective bar), and F1b's reading enters the charter as a floor number only
    out['bars'] = dict(F1=out['F1']['D_max'] < 1e-10 * R, F1c=out['F1c']['D_max'] < 1e-8 * R,
                       F2=out['F2']['D_max'] < 1e-10 * R, F3=0.5 * defo * R <= out['F3']['D_max'] <= 1.5 * defo * R)
    return out


def credential(M=48, out=None):
    rec = dict(date='2026-10-27', instrument='benchmarks/foundations/ring_wave_dynamics.py', M=M)
    t0 = time.time()
    print('K1 twist wave on a frozen ring')
    r1 = k1_twist_wave(M); rec['K1'] = r1
    print(f"  n {r1['n']}: period measured {r1['period_measured']:.6f}, discrete {r1['period_discrete']:.6f} (rel {r1['rel_to_discrete']:+.1e}), exact {r1['period_exact']:.6f} (rel {r1['rel_to_exact']:+.1e}); E drift {r1['E_drift']:.1e}")
    print('K2 Nambu-Goto pulsating circle (kappa = 0), R0 to R0 / 2')
    r2 = k2_pulsating(M); rec['K2'] = r2
    print(f"  R(t_end) {r2['R_end']:.6f} exact {r2['R_exact_end']:.6f}; worst |R - exact| {r2['worst_R_error']:.1e}; E0 {r2['E0']:.6f} (2 pi R0 = {r2['E_exact']:.6f}) drift {r2['E_drift']:.1e}; circle kept to {r2['R_spread_max']:.1e}")
    print('K3 the exact ring-wave, unperturbed, two periods (conservation only; no growth read)')
    r3 = k3_ring_wave(M); rec['K3'] = r3
    print(f"  R_d {r3['R']:.6f} (continuum sqrt(kappa / T) = {r3['R_continuum']:.6f}): E0 {r3['E0']:.6f} (closed form {r3['E_closed_form']:.6f}) drift {r3['E_drift']:.1e}; J0 {r3['J0']:.6f} (2 pi kappa = {r3['J_closed_form']:.6f}) drift {r3['J_drift']:.1e}; "
          f"|P| max {r3['P_max']:.1e}; Q drift {r3['Q_drift']:.1e}; circle kept to {r3['R_spread_max']:.1e}, R_mean drift {r3['R_mean_drift']:.1e}; spacing kept to {r3['seg_spread_max']:.1e}")
    print('K4 Noether on generic data')
    r4 = k4_noether(); rec['K4'] = r4
    for r in r4['rows']:
        print(f"  h {r['h']} pin {str(r['pin']):5s}: E drift {r['E_drift']:.2e}  |dP| {r['P_drift']:.1e}  |dJ| {r['J_drift']:.1e}  dQ {r['Q_drift']:.1e}  ({r['steps']} steps)")
    print(f"  energy-drift order {r4['E_order']:.2f} (unpinned); the pinned |dJ| is the gauge pin's torque on fast generic data")
    print('K5 shape degeneracy on the beta = 0.5 family member (Leg C theorem; not the evidence cell)')
    r5 = k5_shape_degeneracy(M); rec['K5'] = r5
    print(f"  n {r5['n']} eps {r5['eps']}: worst node displacement {r5['worst_displacement']:.2e} = {r5['worst_over_eps2R']:.2f} eps^2 R (first order would be {r5['eps'] * r5['R']:.1e}); "
          f"vmax {r5['vmax']:.1e}; |dJ| {r5['J_drift']:.1e}; E drift {r5['E_drift']:.1e}; D_shape (K6 observable, every 200 steps) {r5['D_shape_max']:.2e} = {r5['D_shape_over_epsR']:.4f} eps R")
    print('K6 the shape observable on known answers (relabeling, fractional slide, rigid motion, deformation)')
    r6 = {M_: k6_shape_registration(M_) for M_ in (48, 96)}; rec['K6'] = r6
    for M_, o in r6.items():
        print(f"  M {M_}: F1 relabel {o['F1']['D_max']:.1e}  F1b slide+equalize {o['F1b']['D_max']:.2e} (bar {o['F1b_bar']:.2e}; uniform-shift stage {o['F1b']['D_max_uniform']:.2e})  "
              f"F1c slide on curve {o['F1c']['D_max']:.1e}  F2 relabel+rigid {o['F2']['D_max']:.1e}  F3 deformation {o['F3']['D_max']:.3e} (exact {o['F3_exact']:.3e})  "
              f"| indexed Procrustes reads F1 {o['F4_indexed_F1']:.1e} F1b {o['F4_indexed_F1b']:.1e}")
    ok = dict(K1=abs(r1['rel_to_discrete']) < 2e-3 and r1['E_drift'] < 1e-6,
              K2=r2['worst_R_error'] < 1e-3 and abs(r2['E0'] - r2['E_exact']) / r2['E_exact'] < 1e-3 and r2['E_drift'] < 1e-4,
              K3=abs(r3['E0'] - r3['E_closed_form']) / r3['E_closed_form'] < 1e-3 and abs(r3['J0'] - r3['J_closed_form']) / r3['J_closed_form'] < 1e-3
                 and r3['E_drift'] < 1e-4 and r3['J_drift'] < 1e-7 and r3['P_max'] < 1e-8 and r3['R_mean_drift'] < 1e-4 and r3['R_spread_max'] < 1e-6,
              K4=all(r['P_drift'] < 1e-9 and r['J_drift'] < 1e-9 for r in r4['rows'] if not r['pin']) and r4['E_order'] > 1.8,
              K5=r5['worst_displacement'] < 0.1 * r5['eps'] * r5['R'] and r5['J_drift'] < 1e-7,
              K6=all(all(o['bars'].values()) for o in r6.values()))
    rec['bars'] = ok; rec['seconds'] = time.time() - t0
    print('BARS: ' + '  '.join(f"{k} {'PASS' if v else 'FAIL'}" for k, v in ok.items()) + f"   ({rec['seconds']:.0f}s)")
    if out:
        pathlib.Path(out).write_text(json.dumps(rec, indent=1, default=float))
    return rec


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--credential', action='store_true')
    ap.add_argument('--M', type=int, default=48)
    ap.add_argument('--out', type=str, default=None)
    a = ap.parse_args()
    if a.credential:
        credential(a.M, a.out)
