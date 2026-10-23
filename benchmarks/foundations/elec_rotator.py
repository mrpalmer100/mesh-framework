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

CONTROL RECORD (2026-10-23, M = 48, K = 8, finite-difference L-BFGS): from a flat-ellipse seed at J = pi T0 (R = 1)
the folded rotating string is found with E = 6.1828 (2 pi T0 R = 6.2832, -1.6 percent), J on target to 5e-4,
edge speed 0.99989, R_end = 2 J / E to 1.6 percent, <r^2>_q / R^2 = 0.355 (exact 1/3), g = 0.637 for the uniform
line charge (exact 2/3; g = 2 needs the charge at the lightlike ends). From a near-circle seed the optimizer finds
instead a ring rotating about a diameter, a genuine stationary state 25 to 30 percent above the fold in E at the
same J: the landscape has more than one rotating branch, and the pair march seeds accordingly. At fixed Omega
(the Routhian) the rotating states are saddles and a minimizer collapses the loop, which is why the instrument
minimizes E at fixed J (ELECTRON_LEDGER section 3).

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
from scipy.optimize import minimize
from scipy.special import erf

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from rope_solver.topology.linking import hopf_curves, linking_number     # noqa: E402

T0 = 1.0
K = 8                   # Fourier modes per coordinate (the engine's K)
A_THICK = 0.24          # the engine's smearing width, in units of the base radius at z0 = 0
D_HARD = 0.06           # the engine's hard-core separation
VMAX2 = 1.0 - 1e-6      # v_perp^2 is clamped below 1 inside the sqrt
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


def geometry(cs, Omega):
    """Per-segment midpoints, lengths, unit tangents, rigid and transverse velocity at the midpoint, and the
    segment's gamma-weight integrated exactly from the squared transverse speeds at its two nodes (c = 1)."""
    out = []
    for c in cs:
        nxt = np.roll(c, -1, axis=0); prv = np.roll(c, 1, axis=0)
        seg = nxt - c
        ds = np.linalg.norm(seg, axis=1)
        t = seg / ds[:, None]
        tn = (nxt - prv); tn /= np.linalg.norm(tn, axis=1)[:, None]                       # node tangents
        vn = Omega * np.stack([-c[:, 1], c[:, 0], np.zeros(len(c))], axis=1)                # node velocities
        vpn = vn - (np.sum(vn * tn, axis=1))[:, None] * tn
        v2n = np.sum(vpn ** 2, axis=1)
        mid = 0.5 * (c + nxt)
        v = Omega * np.stack([-mid[:, 1], mid[:, 0], np.zeros(len(mid))], axis=1)       # Omega z x p
        vperp = v - (np.sum(v * t, axis=1))[:, None] * t
        gint = _gamma_int(v2n, np.roll(v2n, -1))                                            # per segment
        out.append(dict(mid=mid, ds=ds, t=t, v=v, vperp=vperp, v2=np.sum(vperp ** 2, axis=1), v2n=v2n, gint=gint))
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


def routhian(z, Omega, kappa, M, B, single):
    cs = curves(z, M, B, single)
    g = geometry(cs, Omega)
    F = 0.0
    for gi in g:
        v2 = gi['v2n']
        over = np.clip(v2 - VMAX2, 0, None)
        F += T0 * np.sum(np.sqrt(1.0 - np.minimum(gi['v2'], VMAX2)) * gi['ds']) + 1e3 * np.sum(over) * gi['ds'].mean()
    if kappa > 0:
        F += coulomb(cs, kappa)[0]
    return F + hardcore(cs)


def observables(z, Omega, kappa, M, B, single):
    cs = curves(z, M, B, single)
    g = geometry(cs, Omega)
    E_t, J, Eden_r2, edge = 0.0, 0.0, 0.0, 0.0
    for gi in g:
        gam = gi['gint']
        E_t += T0 * np.sum(gam * gi['ds'])
        pxv = gi['mid'][:, 0] * gi['vperp'][:, 1] - gi['mid'][:, 1] * gi['vperp'][:, 0]
        J += T0 * np.sum(gam * pxv * gi['ds'])
        r2 = gi['mid'][:, 0] ** 2 + gi['mid'][:, 1] ** 2
        Eden_r2 += T0 * np.sum(gam * r2 * gi['ds'])
        edge = max(edge, float(np.sqrt(gi['v2n'].max())))
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
    return dict(Omega=Omega, E=float(E), E_tension=float(E_t), E_C=float(E_C), coulomb_fraction=float(E_C / E),
                J=float(J), R_end=rend, two_J_over_E=float(2 * J / E) if E else float('nan'), r2_charge=r2q, r2_energy=float(r2e),
                second_moment_ratio=float(r2q / r2e), edge_speed=edge, mu_rigid=mu_rigid, mu_perp=mu_perp, g_rigid=g_rigid,
                g_perp=g_perp, length=float(sum(np.sum(gi['ds']) for gi in g)), linking=lk)


def energy_and_J(z, Omega, kappa, M, B, single):
    cs = curves(z, M, B, single)
    g = geometry(cs, Omega)
    E, J, over = 0.0, 0.0, 0.0
    for gi in g:
        over += np.sum(np.clip(gi['v2n'] - VMAX2, 0, None)) * gi['ds'].mean()
        gam = gi['gint']
        E += T0 * np.sum(gam * gi['ds'])
        pxv = gi['mid'][:, 0] * gi['vperp'][:, 1] - gi['mid'][:, 1] * gi['vperp'][:, 0]
        J += T0 * np.sum(gam * pxv * gi['ds'])
    if kappa > 0:
        E += coulomb(cs, kappa)[0]
    return E, J, 1e3 * over + hardcore(cs)


def solve_fixed_J(z0, Omega0, J_target, kappa, M=64, single=False, maxiter=3000, verbose=False, w=(30.0, 300.0, 3000.0)):
    """Minimize E over the shape AND Omega with J held at J_target (penalty continuation, then the last stage is the
    answer). This is the ensemble of ELECTRON_LEDGER section 3: at fixed angular momentum the rotation is repulsive
    at short scale, so the minimum exists; at fixed Omega (the Routhian F) the rotating solution is a saddle and an
    unconstrained minimizer shrinks the loop to the hard core (the first control run, 2026-10-23, R_end 0.16 at
    1 / Omega = 2)."""
    B = basis(M)
    x = np.concatenate([z0, [math.log(Omega0)]])
    res = None
    for wj in w:
        def f(x):
            E, J, pen = energy_and_J(x[:-1], math.exp(x[-1]), kappa, M, B, single)
            return E + pen + wj * (J / J_target - 1.0) ** 2
        bounds = [(None, None)] * (len(x) - 1) + [(-6.0, 6.0)]
        res = minimize(f, x, method='L-BFGS-B', bounds=bounds, options=dict(maxiter=maxiter, maxfun=400000, ftol=1e-13, gtol=1e-9))
        x = res.x
        if verbose:
            E, J, pen = energy_and_J(x[:-1], math.exp(x[-1]), kappa, M, B, single)
            print(f'    w {wj:g}: E {E:.6f} J {J:.6f} (target {J_target:.6f}, off {J / J_target - 1:+.2e}) Omega {math.exp(x[-1]):.5f} pen {pen:.2e} nit {res.nit}', flush=True)
    return x[:-1], math.exp(x[-1]), res


def solve(z0, Omega, kappa, M=64, single=False, maxiter=400, verbose=False):
    B = basis(M)
    f = lambda z: routhian(z, Omega, kappa, M, B, single)
    res = minimize(f, z0, method='L-BFGS-B', options=dict(maxiter=maxiter, maxfun=200000, ftol=1e-12, gtol=1e-8))
    if verbose:
        print(f'    Omega {Omega:.4f}: F {res.fun:.6f} nit {res.nit} nfev {res.nfev} {"ok" if res.success else res.message}')
    return res.x, res


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
                  f'<r^2>_q/R^2 {o["r2_charge"] / R ** 2:.4f} (1/3)  g_rigid {o["g_rigid"]:.4f} g_perp {o["g_perp"]:.4f}', flush=True)
        continue
        z, Omega, res = solve_fixed_J(z, 0.8 / R, J_t, 0.0, M=M, single=True, verbose=True)
        o = observables(z, Omega, 0.0, M, basis(M), True)
        exp = dict(E=2 * math.pi * T0 * R, J=J_t, R=R)
        rows.append(dict(obs=o, expected=exp))
        HC[0] = True
        print(f'    R_end {o["R_end"]:.5f} (expected {R:.5f}; 1/Omega {1 / Omega:.5f})  E {o["E"]:.5f} (2 pi T0 R {exp["E"]:.5f}, rel {o["E"] / exp["E"] - 1:+.2e})  '
              f'J {o["J"]:.5f} (pi T0 R^2 {exp["J"]:.5f}, rel {o["J"] / exp["J"] - 1:+.2e})  2J/E {o["two_J_over_E"]:.5f}  '
              f'edge {o["edge_speed"]:.5f}  <r^2>_q/R^2 {o["r2_charge"] / R ** 2:.4f} (1/3)  g_rigid {o["g_rigid"]:.4f} g_perp {o["g_perp"]:.4f}')
    return rows


def pair_march(kappa, Js, M=64, out=None):
    """The Hopf-linked pair, E minimized at fixed J along a ladder of J; each solve seeded by the previous. Seeds:
    the base Hopf pair with C1 flattened toward the rotation plane (the control's lesson), small random modes."""
    print(f'PAIR: Hopf-linked two curves, kappa = {kappa}, M = {M}, J ladder {Js}')
    rows = []
    R0 = math.sqrt(Js[0] / (math.pi * T0))
    z = z_init(R0, seed=2, amp=0.02 * R0)
    z[1 + 2 * K + 0] = -0.5 * R0            # C1: y = 0.5 R sin t (a flattened loop in the rotation plane, still linked)
    Omega = 0.8 / R0
    for J_t in Js:
        z, Omega, res = solve_fixed_J(z, Omega, J_t, kappa, M=M, verbose=True)
        o = observables(z, Omega, kappa, M, basis(M), False)
        o['J_target'] = J_t
        rows.append(o)
        print(f'    J {J_t:.4f}: E {o["E"]:.5f} J {o["J"]:.5f} Omega {Omega:.4f} 2J/E {o["two_J_over_E"]:.4f} R_end {o["R_end"]:.4f} edge {o["edge_speed"]:.4f} '
              f'E_C/E {o["coulomb_fraction"]:.4f} <r2>_q/<r2>_E {o["second_moment_ratio"]:.4f} g_rigid {o["g_rigid"]:.4f} g_perp {o["g_perp"]:.4f} Lk {o["linking"]:.3f}', flush=True)
        if out:
            pathlib.Path(out).write_text(json.dumps(dict(kappa=kappa, M=M, rows=rows, z_last=z.tolist(), Omega_last=Omega), indent=1))
        # seed the next rung by scaling the shape with sqrt(J)
        z = z.copy(); z[0] += 0.5 * math.log(Js[min(Js.index(J_t) + 1, len(Js) - 1)] / J_t)
    return rows


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--control', action='store_true')
    ap.add_argument('--pair', action='store_true')
    ap.add_argument('--kappa', type=float, default=math.pi / 137.035999)     # alpha pi: the Coulomb strength at the rotator scale (ledger 6)
    ap.add_argument('--Js', type=str, default='0.5,1.0,2.0,4.0')
    ap.add_argument('--M', type=int, default=64)
    ap.add_argument('--out', type=str, default=str(ROOT / 'analysis' / 'elec_rotator_march.json'))
    a = ap.parse_args()
    if a.control:
        control(a.M)
    if a.pair:
        pair_march(a.kappa, [float(x) for x in a.Js.split(',')], M=a.M, out=a.out)
