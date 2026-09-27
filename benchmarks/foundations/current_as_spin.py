"""COMMISSION CURRENT-AS-SPIN (charter analysis/CURRENT_AS_SPIN_charter_LOCKED.md, locked 2026-09-27).

PART A -- torque injection. The registered screw-stretch sector (EM-RECON-023): energy per unit
  length (lambda/2) Phi'^2 + (k_s/2) u'^2 + c_L u' Phi' with the lock c_L = lambda gamma tau_0
  (EM-RECON-012), inertia I (twist) and mu (stretch). Drive: a steady longitudinal strain
  gradient (the EMF reading, EM-018) as a steady body force on u.
  A1 symbolic: the torque density on the azimuth is a TOTAL DERIVATIVE, d/ds (lambda Phi' +
     c_L u'), so a bulk strain gradient exerts zero net torque on the azimuth's zero mode; the
     net torque is the difference of the twist flux J = lambda Phi' + c_L u' between the ends,
     which vanishes under the natural (torsion-free) end condition.
  A2 numeric control: a chain of N sites, u pinned at both ends, twist free, body force on u
     switched on from rest; the strand-averaged d(Phi)/dt over the last half of the run
     (bar B-A1) and the end fluxes are recorded; three drive strengths, two lengths.
  A3 displays (unregistered inputs, run to NAME the missing input, never adopted): a terminal
     that imposes a twist flux at s = 0 (constant angular acceleration, no steady rate) and a
     terminal that imposes a rotation rate at s = 0 (the strand spins at that rate).

PART B -- spin persistence. Symbolic: for the registered contact form V(r), r the centre-line
  separation, dV/dphi = 0 (EM-RECON-023) AND dV/du = 0 (sliding a straight strand along its own
  tangent leaves the centre line invariant; u is gauge, EM-RECON-012). Numeric: the transverse
  displacement leak through a crossing of contrast g, from the registered point-contact model
  (FND-REL-005's pinning class): two chains coupled at one site by a spring g, a wave packet on
  chain 1, the energy fraction transferred to chain 2, fitted over a decade of g (bar B-B).

Outputs SEALED to analysis/current_as_spin_partA.npz and _partB.npz; verdict by
current_as_spin_verdict.py. No number here is a bar.
"""
import sys, pathlib, time
import numpy as np
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUTA = ROOT / 'analysis' / 'current_as_spin_partA.npz'
OUTB = ROOT / 'analysis' / 'current_as_spin_partB.npz'

# registered ratios for the chain control (values do not enter the structural result)
LAM, TAU0, GAM = 1.0, 1.0, 3.0            # torsional stiffness, base twist rate, lock gamma (symbolic in A1)
CL = LAM * GAM * TAU0                     # lock coupling c_L = lambda gamma tau_0
KS = 2.0 + LAM * GAM ** 2 * TAU0 ** 2     # k/T0 = 2 (FND-027) plus the lock's stiffening (EM-RECON-012)
I_T, MU = 1.0, 1.0


def symbolic_A1():
    s = sp.symbols('s'); lam, cL, ks = sp.symbols('lambda c_L k_s', positive=True)
    Phi = sp.Function('Phi')(s); u = sp.Function('u')(s)
    E = lam / 2 * sp.diff(Phi, s) ** 2 + ks / 2 * sp.diff(u, s) ** 2 + cL * sp.diff(u, s) * sp.diff(Phi, s)
    torque = -(sp.diff(E, Phi) - sp.diff(sp.diff(E, sp.diff(Phi, s)), s))   # -dE/dPhi (Euler-Lagrange)
    J = lam * sp.diff(Phi, s) + cL * sp.diff(u, s)
    total_derivative = sp.simplify(torque - sp.diff(J, s)) == 0
    return str(sp.simplify(torque)), str(J), total_derivative


def chain_A(N, f0, T_end=400.0, dt=0.02, twist_bc='free', omega0=0.0, jflux=0.0):
    """u pinned at both ends (u_0 = u_N = 0), Phi free unless a terminal condition is imposed."""
    Phi = np.zeros(N + 1); u = np.zeros(N + 1); vP = np.zeros(N + 1); vu = np.zeros(N + 1)
    f = np.full(N + 1, f0); f[0] = f[N] = 0.0
    def forces(Phi, u):
        dP = np.diff(Phi); du = np.diff(u)
        JP = LAM * dP + CL * du                     # twist flux on each bond
        Ju = KS * du + CL * dP                      # tension on each bond
        tP = np.zeros(N + 1); tu = np.zeros(N + 1)
        tP[:-1] += JP; tP[1:] -= JP                # force on site j = J_j - J_{j-1} (-dE/dPhi_j)
        tu[:-1] += Ju; tu[1:] -= Ju
        if jflux:
            tP[0] += -LAM * jflux                   # a terminal injecting twist flux at s = 0 (display)
        return tP, tu + f
    steps = int(T_end / dt); hist_rate = []; half = steps // 2
    for n in range(steps):
        tP, tu = forces(Phi, u)
        vP += 0.5 * dt * tP / I_T; vu += 0.5 * dt * tu / MU
        vu[0] = vu[N] = 0.0
        if omega0: vP[0] = omega0
        Phi += dt * vP; u += dt * vu
        tP, tu = forces(Phi, u)
        vP += 0.5 * dt * tP / I_T; vu += 0.5 * dt * tu / MU
        vu[0] = vu[N] = 0.0
        if omega0: vP[0] = omega0
        if n >= half: hist_rate.append(vP.mean())
    hist_rate = np.array(hist_rate)
    dP = np.diff(Phi); du = np.diff(u)
    J = LAM * dP + CL * du
    return dict(mean_rate=float(hist_rate.mean()), rate_drift=float(hist_rate[-len(hist_rate)//4:].mean() - hist_rate[:len(hist_rate)//4].mean()),
                twist_rate_scale=float(np.abs(CL / LAM * du).max()), J_left=float(J[0]), J_right=float(J[-1]),
                strain_gap=float(du[-1] - du[0]), Phi_end=float(Phi[N] - Phi[0]))


def partA():
    t0 = time.time()
    torque, J, tot = symbolic_A1()
    print("[cas A1] torque density on the azimuth =", torque)
    print("[cas A1] twist flux J =", J, "; torque == dJ/ds:", tot)
    print("[cas A1] net torque on the zero mode = J(L) - J(0): a boundary term; zero under torsion-free ends.")
    rows = []
    for N in (100, 200):
        for f0 in (1e-4, 1e-3, 1e-2):
            r = chain_A(N, f0); rows.append((N, f0, r))
            print(f"[cas A2] N {N:3d} f0 {f0:.0e}: <dPhi/dt> {r['mean_rate']:+.2e} (drift {r['rate_drift']:+.2e}) vs twist-rate scale "
                  f"{r['twist_rate_scale']:.2e}; end fluxes J {r['J_left']:+.1e} / {r['J_right']:+.1e}; strain gap {r['strain_gap']:+.2e}")
    d1 = chain_A(100, 1e-3, jflux=1e-3); d2 = chain_A(100, 1e-3, omega0=1e-3)
    print(f"[cas A3] display, twist flux injected at s=0: <dPhi/dt> {d1['mean_rate']:+.2e} with drift {d1['rate_drift']:+.2e} (accelerating: no steady rate without a sink)")
    print(f"[cas A3] display, rotation rate imposed at s=0: <dPhi/dt> {d2['mean_rate']:+.2e} (the strand follows the terminal)")
    np.savez(OUTA, N=[r[0] for r in rows], f0=[r[1] for r in rows],
             mean_rate=[r[2]['mean_rate'] for r in rows], rate_drift=[r[2]['rate_drift'] for r in rows],
             scale=[r[2]['twist_rate_scale'] for r in rows], J_left=[r[2]['J_left'] for r in rows], J_right=[r[2]['J_right'] for r in rows],
             strain_gap=[r[2]['strain_gap'] for r in rows], disp_flux_rate=d1['mean_rate'], disp_flux_drift=d1['rate_drift'],
             disp_omega_rate=d2['mean_rate'], torque=torque, J=J, total_derivative=tot, elapsed=time.time() - t0)
    print(f"[cas A] sealed -> {OUTA.name} ({time.time() - t0:.0f} s)")


def symbolic_B():
    x1, y1, x2, y2, phi, u = sp.symbols('x1 y1 x2 y2 phi u', real=True); Ac, sig = sp.symbols('A_c sigma', positive=True)
    # strand 1 along x through (0,0) with tangent (1,0); strand 2 crossing it; centre-line separation r
    # azimuth phi rotates strand 1 about its own axis: centre line invariant -> r independent of phi
    # longitudinal displacement u slides strand 1 along (1,0): every centre-line point maps to another centre-line point
    r = sp.sqrt((x1 + u - x2) ** 2 + (y1 - y2) ** 2)          # naive: as if a MATERIAL point moved
    r_line = sp.Abs(y1 - y2)                                    # separation of the LINES (the registered object)
    V = Ac / (1 + (r_line / sig) ** 4)
    return str(sp.diff(V, phi)), str(sp.diff(V, u))


def leak_B(g, N=1200, k0=0.3, T_end=None):
    """two chains (unit mass, unit springs, c = 1) coupled at their midpoints by a contact spring g;
    a Gaussian wave packet on chain 1 launched toward the crossing; energy fraction in chain 2 after."""
    m = N // 2
    x = np.arange(N + 1, dtype=float); s0 = m - 250; w = 40.0
    env = np.exp(-((x - s0) / w) ** 2)
    y1 = env * np.cos(k0 * (x - s0)); v1 = -env * np.sin(k0 * (x - s0)) * (-2 * np.sin(k0 / 2)) * 0  # start at rest, split later
    # exact right-moving packet: y(x,t)=env(x-t) cos(k0(x-t)) -> v = -dy/dx
    v1 = -np.gradient(y1)
    y2 = np.zeros(N + 1); v2 = np.zeros(N + 1)
    dt = 0.2; T_end = T_end or 700.0
    def acc(y1, y2):
        a1 = np.zeros_like(y1); a2 = np.zeros_like(y2)
        a1[1:-1] = y1[2:] - 2 * y1[1:-1] + y1[:-2]; a2[1:-1] = y2[2:] - 2 * y2[1:-1] + y2[:-2]
        a1[m] += -g * (y1[m] - y2[m]); a2[m] += -g * (y2[m] - y1[m])
        return a1, a2
    for _ in range(int(T_end / dt)):
        a1, a2 = acc(y1, y2); v1 += 0.5 * dt * a1; v2 += 0.5 * dt * a2
        y1 += dt * v1; y2 += dt * v2
        a1, a2 = acc(y1, y2); v1 += 0.5 * dt * a1; v2 += 0.5 * dt * a2
    def energy(y, v): return 0.5 * (v ** 2).sum() + 0.5 * (np.diff(y) ** 2).sum()
    E1, E2 = energy(y1, v1), energy(y2, v2)
    return E2 / (E1 + E2)


def partB():
    t0 = time.time()
    dphi, du = symbolic_B()
    print(f"[cas B1] registered contact form V(r_line): dV/dphi = {dphi}; dV/du = {du}  (both identically zero)")
    gs = np.logspace(-2.5, -1, 7); fr = np.array([leak_B(g) for g in gs])
    (slope, icpt), *_ = np.linalg.lstsq(np.vstack([np.log(gs), np.ones_like(gs)]).T, np.log(fr), rcond=None)
    halves = []
    for sel in (slice(0, 4), slice(3, 7)):
        (s_, i_), *_ = np.linalg.lstsq(np.vstack([np.log(gs[sel]), np.ones(4)]).T, np.log(fr[sel]), rcond=None); halves.append((s_, np.exp(i_)))
    for g, f in zip(gs, fr): print(f"[cas B2] g {g:.4f}: transverse energy leak fraction {f:.3e}")
    print(f"[cas B2] fit leak = A g^n: n = {slope:.3f}, A = {np.exp(icpt):.3f}; halves n = {halves[0][0]:.3f}/{halves[1][0]:.3f}, A = {halves[0][1]:.3f}/{halves[1][1]:.3f}")
    print("[cas B3] azimuthal leak through the registered contact form: exactly zero at every order (dV/dphi = dV/du = 0);")
    print("         the finite route is EM-RECON-026's collective coupling, whose crossing transfer rate is GRV-118 obligation (3), not computed here.")
    np.savez(OUTB, gs=gs, fr=fr, n=slope, A=np.exp(icpt), n_halves=[h[0] for h in halves], A_halves=[h[1] for h in halves],
             dVdphi=dphi, dVdu=du, elapsed=time.time() - t0)
    print(f"[cas B] sealed -> {OUTB.name} ({time.time() - t0:.0f} s)")


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('A', 'all'): partA()
    if which in ('B', 'all'): partB()
