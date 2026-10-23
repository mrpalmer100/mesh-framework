"""E2: the rotating charge-one pair at fixed angular momentum (analysis/ELECTRON_LEDGER.md, sections 6 to 8).
The executor's instrument, 2026-10-23; registers nothing. Units T0 = 1, c = 1.

THE FUNCTIONAL. A tensioned string with no material points moves only transversely (FND-REL-002); for a rigid
rotation at rate Omega about z, the element at p has velocity v = Omega z x p and transverse velocity
v_perp = v - (v . t) t with t the unit tangent. The Nambu-Goto string's energy and momentum densities are
T0 gamma ds and T0 gamma v_perp ds with gamma = 1 / sqrt(1 - v_perp^2) (c = 1), and a steadily rotating
configuration is a stationary point, at fixed Omega, of the rotating-frame functional
    F[shape; Omega] = T0 Int sqrt(1 - v_perp^2) ds  +  E_C[shape]  +  P_hc[shape],
whose first term is the Nambu-Goto action per unit time (the string wants to extend until its transverse
speed reaches c, where the weight vanishes: the lightlike folds). E_C is the Coulomb self-energy of the
registered source (a uniform line charge along both curves, Gaussian-smeared with width A_THICK, total charge 1,
as ELEC-036 built it), evaluated pairwise with erf smearing instead of the 14^3 Poisson grid; P_hc the
hard-core penalty keeping the two curves D_HARD apart (the engine's constraint, as a penalty). The Coulomb term
is taken static (its magnetic and retardation corrections are of relative order v^2 times the Coulomb fraction,
which under H is alpha; recorded, not included).

OUTPUTS at each Omega: E = T0 Int gamma ds + E_C; J = T0 Int gamma (p x v_perp)_z ds; the charge second moment
and the energy second moment; the edge speed max |v_perp|; the Coulomb fraction; the magnetic moment from the
moving source, mu = (1/2) Int (p x j) with j = rho v (the pattern rides the shape; both the rigid v and v_perp
readings are reported); g = (mu / J)(2 m / q) with m = E, q = 1.

THE CONTROL (section 8): a single closed loop with no Coulomb term, rotating, must flatten into the folded
string with ends at r = 1 / Omega and give E = 2 pi T0 R, J = pi T0 R^2 and R_end = 2 J / E, and with the
charge uniform along it its second moment is R^2 / 3.

CONTROL RECORD (2026-10-23, final form: M = 48, K = 8, NSUB = 8, Omega eliminated by J(z, Omega) = J_target, rest
frame enforced by W_MOM (P / E)^2, finite-difference L-BFGS). Flat-ellipse seed, single loop, kappa = 0, hard core off:
  R = 1: E = 6.3606 (2 pi T0 R = 6.2832, +1.2 percent), 2 J / E = 0.983 (fold: 1), <r^2>_q / R^2 = 0.403 (1/3),
         4 pi T0 J / E^2 = 0.971 (bound 1), cm speed 1e-5, J 0.5 percent under target at the speed wall.
  R = 2: E = 12.600 (12.566, +0.27 percent), 2 J / E = 1.974 (2), <r^2>_q / R^2 = 0.355 (1/3), 4 pi T0 J / E^2 = 0.984,
         cm speed 4e-6, J 1.0 percent under target at the speed wall.
The near-circle seed finds a different stationary branch at both radii (E 19 and 34 percent above the fold, Regge
ratio 0.70 and 0.55), so the pair march seeds flat. Two loopholes were closed on the way to this record, and both
are warnings for every rotator number: (1) node tangents from central differences are meaningless at a cusp, and the
exact-constraint solver found loops 20 percent BELOW the fold's energy at the same J through them (violating the
closed-string Regge bound E^2 >= 4 pi T0 J); the geometry now uses the segment tangent and sub-segment gamma
integrals, and 4 pi T0 J / E^2 <= 1 is printed on every line as the check; (2) without the momentum constraint the
minimizer finds the lopsided hairpin (one tip lightlike at 1 / Omega, the other end on the axis, E = pi T0 R,
J = pi T0 R^2 / 2) whose J is orbital angular momentum of a centre of energy moving at 0.6 c; the rest frame is now
enforced and the cm speed printed. At fixed Omega (the Routhian) the rotating states are saddles and a minimizer
collapses the loop, which is why the instrument minimizes E at fixed J (ELECTRON_LEDGER section 3).

THE PARAMETRIZATION is the clasp engine's (ELEC-020 / electron_augmented_lagrangian.Model): two closed curves,
Hopf-linked base circles of radius R = e^{z0} (C1 in the xy-plane about the origin, C2 in the xz-plane about
(R, 0, 0)), each deformed by K Fourier modes per coordinate; z has 1 + 2 x 3 x 2K entries.
"""
import argparse
import json
import math
import pathlib
import sys
import time

import numpy as np
from scipy.optimize import minimize, brentq
from scipy.special import erf

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from rope_solver.topology.linking import hopf_curves, linking_number     # noqa: E402

T0 = 1.0
K = 8                   # Fourier modes per coordinate (the engine's K)
A_THICK = 0.24          # the engine's smearing width, in units of the base radius at z0 = 0
D_HARD = 0.06           # the engine's hard-core separation
VMAX2 = 1.0 - 1e-6
VSOFT = 1.0 - 1e-4            # quadratic wall begins here: the optimizer never reaches the hard cap, where the objective kinks
WALL = 1e-4      # v_perp^2 is clamped below 1 inside the sqrt
W_MOM = 1e5                   # penalty weight on (P / E)^2, the centre-of-energy speed squared
HC = [True]             # hard-core penalty on (the pair); the control switches it off to reach the folded string


def basis(M):
    t = np.linspace(0, 2 * np.pi, M, endpoint=False)
    return np.array([f(k * t) for k in range(1, K + 1) for f in (np.sin, np.cos)])      # (2K, M)


def curves(z, M, B=None, single=False):
    B = basis(M) if B is None else B
    R = float(np.exp(z[0]))
    c1, c2 = hopf_curves(M, R=R)
    co = z[1:].reshape(2, 3, 2 * K)
    p1 = c1 + np.einsum('ak,kn->na', co[0], B)
    if single:
        return [p1 - p1.mean(0)]
    p2 = c2 + np.einsum('ak,kn->na', co[1], B)
    cen = np.vstack([p1, p2]).mean(0)
    return [p1 - cen, p2 - cen]


def _gamma_int(a, b):
    """Int_0^1 dx / sqrt(1 - (a + (b - a) x)) for the squared transverse speed varying linearly along a segment
    from a to b (both below 1): exact, and finite as b -> 1, which the midpoint rule is not (the lightlike fold)."""
    a = np.minimum(a, VMAX2); b = np.minimum(b, VMAX2)
    d = b - a
    small = np.abs(d) < 1e-9
    out = np.empty_like(a)
    out[small] = 1.0 / np.sqrt(1.0 - a[small])
    ns = ~small
    out[ns] = 2.0 * (np.sqrt(1.0 - a[ns]) - np.sqrt(1.0 - b[ns])) / d[ns]
    return out


NSUB = 8      # sub-segments per segment for the gamma-weighted integrals


def geometry(cs, Omega):
    """Per segment: constant unit tangent t = (p_{i+1} - p_i) / ds, rigid velocity v = Omega z x p linear along the
    segment, transverse velocity v_perp = v - (v . t) t linear, so v_perp^2 is quadratic; each segment is split into
    NSUB sub-segments with the gamma-weight integrated exactly for a linear v_perp^2 on each (_gamma_int), and E, J
    and the moments use the same weights at the sub-midpoints. The first version took node tangents from central
    differences, which are meaningless at a cusp: a node at the fold tip could show a small transverse speed and a
    cheap gamma, and the exact-constraint solver found loops 20 percent below the Regge bound E^2 = 4 pi T0 J of
    the folded string that way (2026-10-23). With the segment tangent the fold tip is lightlike on both adjacent
    segments, as it must be. Returned per curve: mid, ds, t, v, vperp (segment level, for the moments) and
    smid, sds, sgint, spxv, sv2max (sub-segment level, for E and J and the speed wall)."""
    out = []
    xs = np.linspace(0.0, 1.0, NSUB + 1)
    for c in cs:
        nxt = np.roll(c, -1, axis=0)
        seg = nxt - c
        ds = np.linalg.norm(seg, axis=1)
        t = seg / ds[:, None]
        # sub-nodes: p(x) = c + x seg, shape (Mseg, NSUB+1, 3)
        P = c[:, None, :] + xs[None, :, None] * seg[:, None, :]
        V = Omega * np.stack([-P[..., 1], P[..., 0], np.zeros(P.shape[:2])], axis=-1)
        Vp = V - np.sum(V * t[:, None, :], axis=-1)[..., None] * t[:, None, :]
        v2 = np.sum(Vp ** 2, axis=-1)                                     # (Mseg, NSUB+1)
        a = v2[:, :-1].ravel(); b = v2[:, 1:].ravel()
        sgint = _gamma_int(a, b).reshape(v2.shape[0], NSUB)
        Pm = 0.5 * (P[:, :-1, :] + P[:, 1:, :]); Vpm = 0.5 * (Vp[:, :-1, :] + Vp[:, 1:, :])
        svp = Vpm                                                          # sub-midpoint transverse velocity
        spxv = Pm[..., 0] * Vpm[..., 1] - Pm[..., 1] * Vpm[..., 0]
        sds = np.repeat(ds[:, None], NSUB, axis=1) / NSUB
        mid = 0.5 * (c + nxt)
        v = Omega * np.stack([-mid[:, 1], mid[:, 0], np.zeros(len(mid))], axis=1)
        vperp = v - (np.sum(v * t, axis=1))[:, None] * t
        out.append(dict(mid=mid, ds=ds, t=t, v=v, vperp=vperp, smid=Pm, sds=sds, sgint=sgint, spxv=spxv, sv2=v2,
                        svp=svp, sv2max=float(v2.max())))
    return out


def coulomb(cs, kappa, a=A_THICK):
    """Pairwise Coulomb energy of Gaussian-smeared charges q_i = ds_i / L_total on both curves, kappa * sum."""
    mids, qs = [], []
    for c in cs:
        nxt = np.roll(c, -1, axis=0)
        ds = np.linalg.norm(nxt - c, axis=1)
        mids.append(0.5 * (c + nxt)); qs.append(ds)
    P = np.vstack(mids); q = np.concatenate(qs); q = q / q.sum()
    d = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=2)
    iu = np.triu_indices(len(P), 1)
    r = d[iu]
    pair = np.sum(q[iu[0]] * q[iu[1]] * erf(r / (2 * a)) / r)
    self_e = np.sum(q ** 2) / (2 * a * math.sqrt(math.pi))
    return kappa * (pair + self_e), P, q


def hardcore(cs, w=1e3):
    """Penalty on inter-curve point distances below D_HARD (and intra-curve non-neighbours)."""
    pen = 0.0
    if not HC[0]:
        return 0.0
    if len(cs) == 2:
        d = np.linalg.norm(cs[0][:, None, :] - cs[1][None, :, :], axis=2)
        pen += np.sum(np.clip(D_HARD - d, 0, None) ** 2)
    for c in cs:
        M = len(c)
        d = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=2)
        idx = np.abs(np.subtract.outer(np.arange(M), np.arange(M)))
        idx = np.minimum(idx, M - idx)
        mask = idx >= 3
        pen += 0.5 * np.sum(np.clip(D_HARD - d[mask], 0, None) ** 2)
    return w * pen


def observables(z, Omega, kappa, M, B, single):
    cs = curves(z, M, B, single)
    g = geometry(cs, Omega)
    E_t, J, Eden_r2, edge = 0.0, 0.0, 0.0, 0.0
    Pm = np.zeros(3)
    for gi in g:
        w = gi['sgint'] * gi['sds']
        E_t += T0 * np.sum(w)
        J += T0 * np.sum(w * gi['spxv'])
        r2 = gi['smid'][..., 0] ** 2 + gi['smid'][..., 1] ** 2
        Eden_r2 += T0 * np.sum(w * r2)
        Pm += T0 * np.sum(w[..., None] * gi['svp'], axis=(0, 1))
        edge = max(edge, math.sqrt(gi['sv2max']))
    E_C, P, q = coulomb(cs, kappa) if kappa > 0 else (0.0, *coulomb(cs, 1.0)[1:])
    E = E_t + E_C
    r2q = float(np.sum(q * (P[:, 0] ** 2 + P[:, 1] ** 2)))
    r2e = Eden_r2 / E_t
    # magnetic moment of the moving source: mu = (1/2) sum q (p x v)_z, with the rigid v and with v_perp
    mids = np.vstack([gi['mid'] for gi in g]); vr = np.vstack([gi['v'] for gi in g]); vp = np.vstack([gi['vperp'] for gi in g])
    mu_rigid = 0.5 * float(np.sum(q * (mids[:, 0] * vr[:, 1] - mids[:, 1] * vr[:, 0])))
    mu_perp = 0.5 * float(np.sum(q * (mids[:, 0] * vp[:, 1] - mids[:, 1] * vp[:, 0])))
    g_rigid = (mu_rigid / J) * 2 * E if J else float('nan')
    g_perp = (mu_perp / J) * 2 * E if J else float('nan')
    rend = max(float(np.sqrt((c[:, 0] ** 2 + c[:, 1] ** 2).max())) for c in cs)
    lk = float(linking_number(cs[0], cs[1])) if len(cs) == 2 else 0.0
    # closest approach between the two curves (segment midpoints), against the hard core D_HARD: a pair sitting on
    # the core is a clasp held only by the core, and its Gauss linking number smears below 1 (2026-10-23)
    min_sep = float(np.min(np.linalg.norm(g[0]['mid'][:, None, :] - g[1]['mid'][None, :, :], axis=2))) if len(cs) == 2 else float('nan')
    return dict(Omega=Omega, E=float(E), E_tension=float(E_t), E_C=float(E_C), coulomb_fraction=float(E_C / E),
                J=float(J), R_end=rend, two_J_over_E=float(2 * J / E) if E else float('nan'), r2_charge=r2q, r2_energy=float(r2e),
                second_moment_ratio=float(r2q / r2e), edge_speed=edge, mu_rigid=mu_rigid, mu_perp=mu_perp, g_rigid=g_rigid,
                g_perp=g_perp, length=float(sum(np.sum(gi['ds']) for gi in g)), linking=lk,
                cm_speed=float(np.linalg.norm(Pm[:2]) / E_t), regge=float(4 * math.pi * T0 * J / E_t ** 2), min_sep=min_sep)


def energy_and_J(z, Omega, kappa, M, B, single):
    cs = curves(z, M, B, single)
    g = geometry(cs, Omega)
    E, J, over = 0.0, 0.0, 0.0
    Pm = np.zeros(3)
    for gi in g:
        over += np.sum((np.clip(gi['sv2'] - VSOFT, 0, None) / WALL) ** 2) * gi['ds'].mean()
        w = gi['sgint'] * gi['sds']
        E += T0 * np.sum(w)
        J += T0 * np.sum(w * gi['spxv'])
        Pm += T0 * np.sum(w[..., None] * gi['svp'], axis=(0, 1))
    if kappa > 0:
        E += coulomb(cs, kappa)[0]
    # rest frame: the rotation axis must pass through the centre of energy, P = T0 int gamma v_perp ds = 0; without
    # this the minimizer finds the lopsided hairpin (one tip lightlike at 1 / Omega, the other end on the axis,
    # E = pi T0 R, J = pi T0 R^2 / 2) whose J is orbital angular momentum of a moving centre of mass (2026-10-23)
    pen_P = W_MOM * float(np.sum(Pm[:2] ** 2)) / E ** 2
    return E, J, 1e3 * over + hardcore(cs) + pen_P


def omega_for_J(z, J_target, kappa, M, B, single, Omega_lo=1e-3):
    """Omega such that J(z, Omega) = J_target, for the shape z: J is monotone in Omega below the speed cap, so a
    bracketed root find gives it. Returns (Omega, J_reached): if the shape cannot carry J_target below the cap,
    J_reached < J_target at the cap Omega and the caller penalizes the shortfall (the shape must grow)."""
    cs = curves(z, M, B, single)
    rmax = max(float(np.max(np.hypot(c[:, 0], c[:, 1]))) for c in cs)
    Omega_hi = math.sqrt(VSOFT) / max(rmax, 1e-9)             # every node below the wall at this Omega
    def Jof(Om):
        return energy_and_J(z, Om, 0.0, M, B, single)[1] - J_target
    jhi = Jof(Omega_hi)
    if jhi < 0.0:
        return Omega_hi, jhi + J_target
    jlo = Jof(Omega_lo)
    if jlo > 0.0:
        return Omega_lo, jlo + J_target
    Om = brentq(Jof, Omega_lo, Omega_hi, xtol=1e-12, rtol=1e-12, maxiter=200)
    return Om, J_target


def solve_fixed_J(z0, Omega0, J_target, kappa, M=64, single=False, maxiter=3000, verbose=False, w=300.0):
    """Minimize E over the shape with Omega eliminated by J(z, Omega) = J_target (omega_for_J): the constraint is
    exact at every evaluation and the objective is smooth where the shape can carry J_target; a shape that cannot
    (too small for the speed cap) pays w (J / J_target - 1)^2 and grows. Earlier versions (penalty continuation,
    then an augmented Lagrangian over [z, log Omega]) stalled with zero iterations whenever the fold sat just under
    the speed cap: the gradient was sound but L-BFGS-B's line search could not resolve the 1e-5-scale descent
    against the wall a step of 1e-4 away (diagnosed 2026-10-23). This is the ensemble of ELECTRON_LEDGER section 3:
    at fixed angular momentum the rotation is repulsive at short scale, so the minimum exists; at fixed Omega (the
    Routhian F) the rotating solution is a saddle and an unconstrained minimizer shrinks the loop to the hard core
    (the first control run, 2026-10-23, R_end 0.16 at 1 / Omega = 2)."""
    B = basis(M)
    def f(z):
        Om, Jr = omega_for_J(z, J_target, kappa, M, B, single)
        E, J, pen = energy_and_J(z, Om, kappa, M, B, single)
        return E + pen + w * (Jr / J_target - 1.0) ** 2
    res = minimize(f, z0, method='L-BFGS-B', options=dict(maxiter=maxiter, maxfun=400000, ftol=1e-13, gtol=1e-9, eps=1e-7, maxls=60))
    z = res.x
    Om, Jr = omega_for_J(z, J_target, kappa, M, B, single)
    E, J, pen = energy_and_J(z, Om, kappa, M, B, single)
    if verbose:
        print(f'    fixed J: E {E:.6f} J {J:.6f} (target {J_target:.6f}, off {J / J_target - 1:+.2e}) Omega {Om:.5f} pen {pen:.2e} nit {res.nit} nfev {res.nfev} {res.message}', flush=True)
    return z, Om, res


def z_init(R, seed=0, amp=0.0):
    rng = np.random.default_rng(seed)
    z = np.zeros(1 + 2 * 3 * 2 * K)
    z[0] = math.log(R)
    z[1:] = amp * rng.normal(size=len(z) - 1)
    return z


def control(M=64):
    """A single loop, no Coulomb, at fixed J: the folded rotating string with folds at r = R = sqrt(J / (pi T0)),
    E = 2 pi T0 R, Omega = 1 / R, R_end = 2 J / E."""
    print('CONTROL: single loop, kappa = 0, hard core off, E minimized at fixed J')
    HC[0] = False
    rows = []
    for R in (1.0, 2.0):
        J_t = math.pi * T0 * R ** 2
        # two seeds: a near-circle (which finds the vertical-ring branch, a rotating solution with higher E) and a
        # flat ellipse in the rotation plane (which must find the folded string, the minimum); the control is the
        # second, the first is recorded so the pair march's seeds are chosen with eyes open
        for seed_name, z in (('near-circle', z_init(0.7 * R, seed=1, amp=0.03 * R)), ('flat-ellipse', z_init(R, seed=1, amp=0.0))):
            if seed_name == 'flat-ellipse':
                z[1 + 2 * K + 0] = -0.9 * R        # curve 0, y coordinate, sin(t): y = 0.1 R sin t
            print(f'  seed {seed_name}, R {R}')
            z, Omega, res = solve_fixed_J(z, 0.8 / R, J_t, 0.0, M=M, single=True, verbose=True)
            o = observables(z, Omega, 0.0, M, basis(M), True)
            exp = dict(E=2 * math.pi * T0 * R, J=J_t, R=R)
            print(f'    R_end {o["R_end"]:.5f} (expected {R:.5f}; 1/Omega {1 / Omega:.5f})  E {o["E"]:.5f} (2 pi T0 R {exp["E"]:.5f}, rel {o["E"] / exp["E"] - 1:+.2e})  '
                  f'J {o["J"]:.5f} (rel {o["J"] / exp["J"] - 1:+.2e})  2J/E {o["two_J_over_E"]:.5f}  edge {o["edge_speed"]:.5f}  '
                  f'<r^2>_q/R^2 {o["r2_charge"] / R ** 2:.4f} (1/3)  g_rigid {o["g_rigid"]:.4f} g_perp {o["g_perp"]:.4f}  '
                  f'cm_speed {o["cm_speed"]:.2e}  4piJ/E^2 {o["regge"]:.4f}', flush=True)
    return rows


def pair_seeds(R0, Omega0):
    """Seeds for one rung at scale R0: flat (C1 flattened toward the rotation plane, the control's lesson), base
    Hopf (both circles round), and a tilted pair; each with small random modes."""
    seeds = {}
    z = z_init(R0, seed=2, amp=0.02 * R0); z[1 + 2 * K + 0] = -0.5 * R0; seeds['flat'] = (z, Omega0)
    z = z_init(R0, seed=3, amp=0.02 * R0); seeds['round'] = (z, Omega0)
    z = z_init(R0, seed=4, amp=0.02 * R0); z[1 + 2 * K + 0] = -0.8 * R0; z[1 + 6 * K + 0] = 0.3 * R0; seeds['tilt'] = (z, Omega0)
    return seeds


def pair_march(kappa, Js, M=64, out=None, multiseed=False, warm=None):
    """The Hopf-linked pair, E minimized at fixed J along a ladder of J. Default: each rung seeded by the previous
    rung's shape scaled with sqrt(J) (one chain). With multiseed, every rung is also solved from the fresh seeds of
    pair_seeds and the lowest E is kept, since a single chain can land on a higher branch (the first march of
    2026-10-23 did at J = 2: the Regge ratio dropped from 0.84 to 0.62 in one rung). With warm (a JSON written by
    an earlier march) the chain starts from that march's shape at the first J in Js that it covered."""
    print(f'PAIR: Hopf-linked two curves, kappa = {kappa}, M = {M}, J ladder {Js}, multiseed {multiseed}')
    rows, shapes = [], {}
    R0 = math.sqrt(Js[0] / (math.pi * T0))
    z, Omega = pair_seeds(R0, 0.8 / R0)['flat']
    if warm:
        W = json.loads(pathlib.Path(warm).read_text())
        if 'shapes' in W:
            avail = {float(k): v for k, v in W['shapes'].items()}
            Jw = max((j for j in avail if j <= Js[0]), default=None)
            if Jw is not None:
                z = np.array(avail[Jw]['z']); Omega = avail[Jw]['Omega']; z[0] += 0.5 * math.log(Js[0] / Jw)
                print(f'    warm start from {warm} at J {Jw}')
    for J_t in Js:
        cands = [('chain', z, Omega)]
        if multiseed:
            Rr = math.sqrt(J_t / (math.pi * T0))
            cands += [(name, zz, Om) for name, (zz, Om) in pair_seeds(Rr, 0.8 / Rr).items()]
        best = None
        for name, z0, Om0 in cands:
            print(f'  seed {name}:', flush=True)
            zs, Oms, res = solve_fixed_J(z0, Om0, J_t, kappa, M=M, verbose=True)
            o = observables(zs, Oms, kappa, M, basis(M), False)
            o['J_target'] = J_t; o['seed'] = name
            print(f'    J {J_t:.4f} [{name}]: E {o["E"]:.5f} J {o["J"]:.5f} Omega {Oms:.4f} 2J/E {o["two_J_over_E"]:.4f} R_end {o["R_end"]:.4f} edge {o["edge_speed"]:.4f} '
                  f'E_C/E {o["coulomb_fraction"]:.4f} <r2>_q/<r2>_E {o["second_moment_ratio"]:.4f} g_rigid {o["g_rigid"]:.4f} g_perp {o["g_perp"]:.4f} Lk {o["linking"]:.3f} '
                  f'cm_speed {o["cm_speed"]:.2e} 4piJ/E^2 {o["regge"]:.4f} min_sep {o["min_sep"]:.4f} (core {D_HARD})', flush=True)
            if abs(o['linking']) < 0.5:
                print('      (unlinked: discarded)', flush=True); continue
            if best is None or o['E'] < best[0]['E']:
                best = (o, zs, Oms)
        o, z, Omega = best
        rows.append(o); shapes[str(J_t)] = dict(z=z.tolist(), Omega=Omega, seed=o['seed'])
        print(f'    J {J_t:.4f} BEST [{o["seed"]}]: E {o["E"]:.5f} 4piJ/E^2 {o["regge"]:.4f}', flush=True)
        if out:
            pathlib.Path(out).write_text(json.dumps(dict(kappa=kappa, M=M, rows=rows, shapes=shapes), indent=1))
        k = Js.index(J_t)
        if k + 1 < len(Js):
            z = z.copy(); z[0] += 0.5 * math.log(Js[k + 1] / J_t)
    return rows


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--control', action='store_true')
    ap.add_argument('--pair', action='store_true')
    ap.add_argument('--kappa', type=float, default=math.pi / 137.035999)     # alpha pi: the Coulomb strength at the rotator scale (ledger 6)
    ap.add_argument('--Js', type=str, default='0.5,1.0,2.0,4.0')
    ap.add_argument('--M', type=int, default=64)
    ap.add_argument('--out', type=str, default=str(ROOT / 'analysis' / 'elec_rotator_march.json'))
    ap.add_argument('--multiseed', action='store_true')
    ap.add_argument('--warm', type=str, default=None)
    ap.add_argument('--dhard', type=float, default=None, help='override the hard-core separation D_HARD (regulator scan)')
    a = ap.parse_args()
    if a.dhard is not None:
        D_HARD = a.dhard
        print(f'D_HARD overridden to {D_HARD}')
    if a.control:
        control(a.M)
    if a.pair:
        pair_march(a.kappa, [float(x) for x in a.Js.split(',')], M=a.M, out=a.out, multiseed=a.multiseed, warm=a.warm)
