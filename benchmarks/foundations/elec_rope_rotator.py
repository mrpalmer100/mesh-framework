"""
E2b: ONE closed rope with one unit of twist, folded and rotating at fixed J; the twist distribution decided by
the registered twist energy, and g read off the twist-density current.

Why this instrument (analysis/ELEC_E2_rotator_results.md section 5): the registry's charge is the linking of the
two strands OF ONE ROPE, i.e. the winding of the rope's internal twist phase Phi(s) around the closed loop
(GG-006, GRV-020), and a rope's two strands are bound at the registered standoff (GRV-020 Branch-A, EM-RECON-017/
018), so the rotating candidate is a single curve (the bound pair, tension T = 1 in these units) carrying an
internal field Phi(s) with oint Phi' ds = 2 pi. The free-loop pair of elec_rotator.py is not that object.

THE MODEL. Shape: elec_rotator's single-curve chart (K = 8 Fourier modes on a circle). Rotation: rigid, about z,
at Omega fixed by J(z, Phi, Omega) = J_target (root find), rest frame enforced (P = 0). Energies, all carried on
the moving element with its gamma (internal energy density per proper length, Lorentz-scalar):
    E_tension = T int gamma ds
    E_twist   = (kappa_tw / 2) int gamma Phi'^2 ds            (the Goldstone energy, GRV-020)
    E_Coulomb = kappa_C sum_ij q_i q_j erf(r_ij / 2a) / r_ij   (the twist-density charge, kappa_C = alpha pi)
with q_i = Phi'_i ds_i / 2 pi the charge of segment i (sum q_i = 1) and J = int gamma (T + eps_twist)(p x v_perp)_z ds.
The twist distribution is parametrized by positive weights q_i = ds_i exp(u_i) / sum (uniform in length at u = 0),
Phi'_i = 2 pi q_i / ds_i.
Shape z and twist u are minimized TOGETHER at fixed J. The moment: mu = (1 / 2) sum q_i (p_i x v_i)_z with the
material (rigid) velocity, since the distribution is stationary in the rotating frame; g = (mu / J)(2 E / q).

WHAT THE ARITHMETIC SAYS BEFORE RUNNING, AND ITS CORRECTION (kept in order): the record's section 5 argued that
minimizing E_twist at fixed winding gives Phi' proportional to 1 / gamma, hence g = 1/2. That minimizes E. At
FIXED J the functional is the Routhian E - Omega J, and for internal energy eps on a rigidly rotating element
gamma eps (1 - Omega (p x v_perp)) = gamma eps (1 - v^2) = eps / gamma, so the twist energy is weighted by
1 / gamma and the minimum at fixed winding is Phi' proportional to gamma: the twist goes TOWARD the lightlike
folds, because twist is mass and at fixed J mass is cheapest where it buys the most angular momentum per unit
energy. The twist-only check on the explicit fold (2026-10-23) gave g = 0.90 rising toward 1 with q_max / q_min
= 3.8, i.e. the energy-following row: g = 1. The table on the fold, with x = r / R weighted by the charge:
1 / gamma gives 1/2, uniform 2/3, gamma 1, edge 2 (all four verified on the explicit fold with fixed weights:
0.504, 0.672, 0.996, and 2 by construction). The registered reading therefore predicts g = 1, not 1/2 and not 2.
kappa_tw sets only the back-reaction on the shape; the Coulomb repulsion (order kappa_C / T) pushes charge
outward slightly. The number to beat is 2.

Usage: python3 elec_rope_rotator.py --R 1,2 --kappa_tw 0.01,0.1,1 --M 48
"""
import argparse, json, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize
from scipy.special import erf

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import elec_rotator as er

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = 1.0
A_SMEAR = er.A_THICK


def unpack(x, M):
    nz = 1 + 2 * 3 * 2 * er.K
    return x[:nz], x[nz:nz + M]


def charges(u, ds):
    """Segment charges q_i = ds_i exp(u_i) / sum: uniform IN LENGTH at u = 0 (the chart bunches nodes at the folds,
    so uniform-per-segment would be a gamma-weighted density, the table's g = 1 row, not its g = 2/3 row)."""
    w = ds * np.exp(u - u.max())
    return w / w.sum()


def pieces(z, u, Omega, kappa_tw, kappa_C, M, B):
    """E (tension, twist, Coulomb), J, momentum P, charge moment data, for the single curve."""
    cs = er.curves(z, M, B, True)
    g = er.geometry(cs, Omega)[0]
    ds = g['ds']
    q = charges(u, ds)                               # per segment, sum 1
    phip = 2 * math.pi * q / ds                      # twist density per segment
    eps_tw = 0.5 * kappa_tw * phip ** 2              # internal energy density per length, per segment
    w = g['sgint'] * g['sds']                        # gamma-weighted sub-lengths, (Mseg, NSUB)
    E_t = T * np.sum(w)
    E_tw = float(np.sum(eps_tw * np.sum(w, axis=1)))
    dens = T + eps_tw                                # energy density per proper length, per segment
    J = float(np.sum(dens[:, None] * w * g['spxv']))
    Pm = np.sum((dens[:, None] * w)[..., None] * g['svp'], axis=(0, 1))
    # Coulomb of the twist-density charge at the segment midpoints
    P = g['mid']
    d = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=2)
    iu = np.triu_indices(len(P), 1)
    r = d[iu]
    E_C = kappa_C * (np.sum(q[iu[0]] * q[iu[1]] * erf(r / (2 * A_SMEAR)) / r) + np.sum(q ** 2) / (2 * A_SMEAR * math.sqrt(math.pi)))
    over = np.sum((np.clip(g['sv2'] - er.VSOFT, 0, None) / er.WALL) ** 2) * ds.mean()
    return dict(E_t=E_t, E_tw=E_tw, E_C=float(E_C), E=E_t + E_tw + float(E_C), J=J, Pm=Pm, over=over, q=q, g=g, cs=cs, phip=phip)


def omega_for_J(z, u, J_t, kappa_tw, kappa_C, M, B):
    cs = er.curves(z, M, B, True)
    rmax = float(np.max(np.hypot(cs[0][:, 0], cs[0][:, 1])))
    Om_hi = math.sqrt(er.VSOFT) / max(rmax, 1e-9)
    f = lambda Om: pieces(z, u, Om, kappa_tw, kappa_C, M, B)['J'] - J_t
    jhi = f(Om_hi)
    if jhi < 0:
        return Om_hi, jhi + J_t
    jlo = f(1e-3)
    if jlo > 0:
        return 1e-3, jlo + J_t
    from scipy.optimize import brentq
    return brentq(f, 1e-3, Om_hi, xtol=1e-12, rtol=1e-12, maxiter=200), J_t


def objective(x, J_t, kappa_tw, kappa_C, M, B, w_J=300.0):
    z, u = unpack(x, M)
    Om, Jr = omega_for_J(z, u, J_t, kappa_tw, kappa_C, M, B)
    p = pieces(z, u, Om, kappa_tw, kappa_C, M, B)
    pen = 1e3 * p['over'] + er.W_MOM * float(np.sum(p['Pm'][:2] ** 2)) / p['E'] ** 2 + w_J * (Jr / J_t - 1) ** 2
    return p['E'] + pen


def observables(z, u, Om, kappa_tw, kappa_C, M, B):
    p = pieces(z, u, Om, kappa_tw, kappa_C, M, B)
    g, q = p['g'], p['q']
    mid = g['mid']
    vr = Om * np.stack([-mid[:, 1], mid[:, 0]], axis=1)
    mu = 0.5 * float(np.sum(q * (mid[:, 0] * vr[:, 1] - mid[:, 1] * vr[:, 0])))
    E, J = p['E'], p['J']
    r2q = float(np.sum(q * (mid[:, 0] ** 2 + mid[:, 1] ** 2)))
    rend = float(np.sqrt((p['cs'][0][:, 0] ** 2 + p['cs'][0][:, 1] ** 2).max()))
    w = g['sgint'] * g['sds']
    r2e = float(np.sum((T + 0.5 * kappa_tw * p['phip'] ** 2)[:, None] * w * (g['smid'][..., 0] ** 2 + g['smid'][..., 1] ** 2)) / (p['E_t'] + p['E_tw']))
    # where the charge sits against the speed: <v^2>_q
    v2n = np.sum(g['vperp'] ** 2, axis=1)
    return dict(Omega=Om, E=E, E_tension=p['E_t'], E_twist=p['E_tw'], E_C=p['E_C'], J=J, R_end=rend, two_J_over_E=2 * J / E,
                g=(mu / J) * 2 * E, x2_charge=r2q / rend ** 2, x2_energy=r2e / rend ** 2, r2_ratio=r2q / r2e,
                v2_charge=float(np.sum(q * v2n)), edge=float(math.sqrt(g['sv2max'])), regge=4 * math.pi * T * J / (p['E_t'] + p['E_tw']) ** 2,
                cm_speed=float(np.linalg.norm(p['Pm'][:2]) / E), q_max_over_min=float(q.max() / q.min()),
                twist_fraction=p['E_tw'] / E, coulomb_fraction=p['E_C'] / E)


def run(R, kappa_tw, kappa_C, M, twist_only=False, maxiter=3000, verbose=True):
    B = er.basis(M)
    J_t = math.pi * T * R * R
    z = er.z_init(R, seed=0, amp=0.0); z[1 + 2 * er.K + 0] = -0.9 * R       # the control's flat-ellipse seed
    u = np.zeros(M)
    x0 = np.concatenate([z, u])
    if twist_only:
        # the fold's shape first (no twist energy), then the twist on that fixed shape: the arithmetic check
        f0 = lambda zz: objective(np.concatenate([zz, u]), J_t, 0.0, 0.0, M, B)
        r0 = minimize(f0, z, method='L-BFGS-B', options=dict(maxiter=maxiter, maxfun=400000, ftol=1e-13, gtol=1e-9, eps=1e-7, maxls=60))
        z = r0.x
        f1 = lambda uu: objective(np.concatenate([z, uu]), J_t, kappa_tw, kappa_C, M, B)
        r1 = minimize(f1, u, method='L-BFGS-B', options=dict(maxiter=maxiter, maxfun=400000, ftol=1e-13, gtol=1e-9, eps=1e-7, maxls=60))
        u = r1.x; nit = (r0.nit, r1.nit)
    else:
        f = lambda xx: objective(xx, J_t, kappa_tw, kappa_C, M, B)
        res = minimize(f, x0, method='L-BFGS-B', options=dict(maxiter=maxiter, maxfun=600000, ftol=1e-13, gtol=1e-9, eps=1e-7, maxls=60))
        z, u = unpack(res.x, M); nit = res.nit
    Om, _ = omega_for_J(z, u, J_t, kappa_tw, kappa_C, M, B)
    o = observables(z, u, Om, kappa_tw, kappa_C, M, B)
    o.update(R=R, kappa_tw=kappa_tw, kappa_C=kappa_C, M=M, nit=nit, twist_only=twist_only)
    if verbose:
        print(f"  R {R} kappa_tw {kappa_tw} {'twist-only' if twist_only else 'joint'}: E {o['E']:.5f} (tension {o['E_tension']:.4f} twist {o['E_twist']:.4f} C {o['E_C']:.4f}) "
              f"J {o['J']:.5f} 2J/E {o['two_J_over_E']:.4f} R_end {o['R_end']:.4f} edge {o['edge']:.4f} regge {o['regge']:.4f} cm {o['cm_speed']:.1e}  "
              f"g {o['g']:.4f}  <x^2>_q {o['x2_charge']:.4f} <x^2>_E {o['x2_energy']:.4f} <v^2>_q {o['v2_charge']:.4f} q_max/q_min {o['q_max_over_min']:.2f} nit {nit}", flush=True)
    return o, z, u


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--R', type=str, default='1.0')
    ap.add_argument('--kappa_tw', type=str, default='0.01,0.1,1.0')
    ap.add_argument('--kappa_C', type=float, default=math.pi / 137.035999)
    ap.add_argument('--M', type=int, default=48)
    ap.add_argument('--twist_only', action='store_true')
    ap.add_argument('--out', type=str, default=None)
    a = ap.parse_args()
    print(f'E2b: one twisted rope, folded and rotating; M {a.M}, kappa_C {a.kappa_C:.5f}; g = 2 <x^2> on the fold: 1/2 (twist-minimizing), 2/3 (uniform), 1 (energy-following), 2 (edge)')
    rows = []
    for R in [float(x) for x in a.R.split(',')]:
        for kt in [float(x) for x in a.kappa_tw.split(',')]:
            o, z, u = run(R, kt, a.kappa_C, a.M, twist_only=a.twist_only)
            o['z'] = z.tolist(); o['u'] = u.tolist(); rows.append(o)
            if a.out:
                pathlib.Path(a.out).write_text(json.dumps(rows, indent=1))
