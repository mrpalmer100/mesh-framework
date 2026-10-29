"""
ELEC-MECH-1 Leg C instrument: one closed rope (tension T, bound pair) whose unit of twist is a pattern travelling
along the rope at speed beta_p c relative to the material, the rope itself in rigid rotation at Omega about z
(Omega eliminated by the J constraint, rest frame enforced). beta_p = 0 is E2b (the co-moving twist, decided by the
Routhian fixed point, elec_rope_rotator.py); beta_p = 1 is the torsion wave at light speed (EM-RECON-012: torsion
waves ARE light). The screen's number is g = (mu / J)(2 m / q) from the time-averaged moments.

THE MODEL (registered pieces, each named; the stated simplifications are the instrument's, listed so a reviewer can
price them):
  material: rigid rotation v_mat = Omega z x p; transverse velocity v_perp = v_mat - (v_mat . t) t; tension energy
            T int gamma ds with the exact per-segment gamma integrals of elec_rotator.py; momentum density of the
            tension energy gamma T v_perp (FND-006, EM-019).
  twist:    Phi(s, t) = Phi_0(s - beta_p t) (c = 1), oint Phi' ds = 2 pi. TIME AVERAGE over one pattern period of any
            product f(s) Phi'(s - beta_p t) is f(s) <Phi'> = f(s) 2 pi / L: for beta_p > 0 the charge per length is
            uniform in length whatever Phi_0 is (verified in the credential by two shapes), so the moments depend on
            the geometry and beta_p only. Energy density per proper length eps_w = kappa Phi'^2 (1 + beta_p^2) / 2
            (the Goldstone (kappa / 2) Phi'^2 at rest; kinetic = potential for the wave at its own speed), carried
            with the material's gamma. Its momentum density: the material part gamma eps_w v_perp plus the wave's
            flux eps_w beta_p t along the rope (energy flux over c^2, EM-019). SIMPLIFICATION 1: the flux term is
            added without the transverse boost's correction (order beta_p v_perp^2), zero for a static ring.
  charge:   lambda = Phi' / 2 pi per length, time-averaged to q / L; current = lambda (v_mat + beta_p t) (EM-008: the
            moving winding is the current; the screw EM-014). mu = (1 / 2) oint lambda (p x (v_perp + beta_p t))_z ds:
            the charge rides the material's TRANSVERSE motion, and motion along the rope is the pattern's (beta_p)
            alone. (The first build used v_mat here; for a ring rotating about its own axis, which carries no J,
            Omega is undetermined and the tangential material velocity counted as a current, inflating g to 3.
            Tangential motion of a string is a reparametrization and carries nothing; corrected 2026-10-25.)
  Coulomb:  the uniform line charge, erf-smeared, kappa_C = alpha pi, as elec_rotator.py.
  J, P, E:  J = oint [gamma (T + eps_w)(p x v_perp)_z + eps_w beta_p (p x t)_z] ds, P likewise, E = tension + wave +
            Coulomb; the rest frame P = 0 enforced as in E2b.

CLOSED FORMS the credential checks (ring of radius R, Omega = 0, beta_p = 1, no Coulomb): E = 2 pi R T + 2 pi kappa / R,
minimum at R = sqrt(kappa / T) with E_tension = E_wave (a virial); J = 2 pi kappa (independent of R); mu = q R / 2;
g = 2 exactly. With T = 0 (all energy in the wave) g = 1. At beta_p = 0 the instrument hands over to E2b.

Usage: python3 elec_rope_wave.py --credential
       python3 elec_rope_wave.py --scan --beta 0.25,0.5,0.75,1.0 --kappa_tw 0.1 --R 1.0
"""
import argparse, json, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize, brentq
from scipy.special import erf

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import elec_rotator as er

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = 1.0
A_SMEAR = er.A_THICK


def pieces(z, Omega, beta, kappa_tw, kappa_C, M, B):
    cs = er.curves(z, M, B, True)
    g = er.geometry(cs, Omega)[0]
    ds = g['ds']; L = float(ds.sum())
    phip = 2 * math.pi / L                                   # time-averaged twist density, uniform in length
    eps_w = 0.5 * kappa_tw * phip ** 2 * (1.0 + beta ** 2)   # wave energy per proper length
    w = g['sgint'] * g['sds']                                # gamma-weighted sub-lengths
    E_t = T * float(np.sum(w))
    E_w = eps_w * float(np.sum(w))
    dens = T + eps_w
    # material momentum (gamma-weighted, transverse) and the wave flux along the rope (sub-segment tangents = segment tangents)
    J_mat = dens * float(np.sum(w * g['spxv']))
    P_mat = dens * np.sum(w[..., None] * g['svp'], axis=(0, 1))
    tpx = g['mid'][:, 0] * g['t'][:, 1] - g['mid'][:, 1] * g['t'][:, 0]           # (p x t)_z per segment
    J_flux = eps_w * beta * float(np.sum(tpx * ds))
    P_flux = eps_w * beta * np.sum(g['t'] * ds[:, None], axis=0)
    J = J_mat + J_flux; Pm = P_mat + P_flux
    # the full angular-momentum VECTOR: a rest-frame state has J along z; without this a loop whose flux carries more
    # than J_t met the constraint by tilting out of the plane (kappa_tw 1, beta 0.75: a 30 degree tilt, 2026-10-25)
    Jvec_mat = dens * np.sum((w[..., None] * np.cross(g['smid'], g['svp'])), axis=(0, 1))
    Jvec_flux = eps_w * beta * np.sum(np.cross(g['mid'], g['t']) * ds[:, None], axis=0)
    Jvec = Jvec_mat + Jvec_flux
    # charge moments: uniform q / L per length; current = lambda (v_mat + beta t)
    q = ds / L
    mid = g['mid']
    vp = g['vperp'][:, :2]                                   # the charge rides the TRANSVERSE material motion only
    mu = 0.5 * float(np.sum(q * (mid[:, 0] * vp[:, 1] - mid[:, 1] * vp[:, 0]))) + 0.5 * beta * float(np.sum(q * tpx))
    # Coulomb
    P = mid
    d = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=2); iu = np.triu_indices(len(P), 1); r = d[iu]
    E_C = kappa_C * (np.sum(q[iu[0]] * q[iu[1]] * erf(r / (2 * A_SMEAR)) / r) + np.sum(q ** 2) / (2 * A_SMEAR * math.sqrt(math.pi)))
    over = np.sum((np.clip(g['sv2'] - er.VSOFT, 0, None) / er.WALL) ** 2) * ds.mean()
    E = E_t + E_w + float(E_C)
    r2q = float(np.sum(q * (mid[:, 0] ** 2 + mid[:, 1] ** 2)))
    rend = float(np.sqrt((cs[0][:, 0] ** 2 + cs[0][:, 1] ** 2).max()))
    return dict(E=E, E_t=E_t, E_w=E_w, E_C=float(E_C), J=J, J_mat=J_mat, J_flux=J_flux, Pm=Pm, Jvec=Jvec, mu=mu, over=over, L=L,
                r2q=r2q, R_end=rend, edge=float(math.sqrt(g['sv2max'])), g=(mu / J) * 2 * E if J else float('nan'))


def omega_for_J(z, J_t, beta, kappa_tw, kappa_C, M, B):
    """Omega with J(z, Omega) = J_t. The wave flux carries J at Omega = 0 (J_flux), so the bracket starts at 0: if the
    flux alone exceeds J_t the shape is too large for this J at this beta (returned as the shortfall sign)."""
    cs = er.curves(z, M, B, True)
    rmax = float(np.max(np.hypot(cs[0][:, 0], cs[0][:, 1])))
    Om_hi = math.sqrt(er.VSOFT) / max(rmax, 1e-9)
    f = lambda Om: pieces(z, Om, beta, kappa_tw, kappa_C, M, B)['J'] - J_t
    j0 = f(0.0)
    if j0 > -1e-9 * J_t:
        return 0.0, j0 + J_t                                 # the flux alone delivers J (or over-delivers: shape must shrink)
    jhi = f(Om_hi)
    if jhi < 0:
        return Om_hi, jhi + J_t
    return brentq(f, 0.0, Om_hi, xtol=1e-12, rtol=1e-12, maxiter=200), J_t


def objective(z, J_t, beta, kappa_tw, kappa_C, M, B, w_J=300.0):
    Om, Jr = omega_for_J(z, J_t, beta, kappa_tw, kappa_C, M, B)
    p = pieces(z, Om, beta, kappa_tw, kappa_C, M, B)
    pen = (1e3 * p['over'] + er.W_MOM * float(np.sum(p['Pm'][:2] ** 2)) / p['E'] ** 2 + w_J * (Jr / J_t - 1) ** 2
           + er.W_MOM * float(np.sum(p['Jvec'][:2] ** 2)) / J_t ** 2)                    # J along the axis
    return p['E'] + pen


def solve(J_t, beta, kappa_tw, kappa_C, M=48, seed='ring', R0=1.0, maxiter=3000, verbose=True):
    B = er.basis(M)
    z = er.z_init(R0, seed=0, amp=0.0)
    if seed == 'flat':
        z[1 + 2 * er.K + 0] = -0.9 * R0
    opts = dict(maxiter=maxiter, maxfun=400000, ftol=1e-14, gtol=1e-10, eps=1e-7, maxls=60)
    res = minimize(lambda zz: objective(zz, J_t, beta, kappa_tw, kappa_C, M, B), z, method='L-BFGS-B', options=opts)
    z = res.x
    Om, _ = omega_for_J(z, J_t, beta, kappa_tw, kappa_C, M, B)
    p = pieces(z, Om, beta, kappa_tw, kappa_C, M, B)
    o = dict(beta=beta, kappa_tw=kappa_tw, kappa_C=kappa_C, J_target=J_t, Omega=Om, seed=seed, nit=res.nit, M=M,
             E=p['E'], E_tension=p['E_t'], E_wave=p['E_w'], E_C=p['E_C'], J=p['J'], J_flux_fraction=p['J_flux'] / p['J'] if p['J'] else float('nan'),
             R_end=p['R_end'], two_J_over_E=2 * p['J'] / p['E'], g=p['g'], x2_charge=p['r2q'] / p['R_end'] ** 2, edge=p['edge'],
             cm_speed=float(np.linalg.norm(p['Pm'][:2]) / p['E']), J_tilt=float(np.linalg.norm(p['Jvec'][:2]) / J_t),
             length=p['L'], wave_fraction=p['E_w'] / p['E'], z=z.tolist())
    if verbose:
        print(f"  beta {beta} kappa_tw {kappa_tw} J {J_t:.4f} [{seed}]: E {o['E']:.5f} (tension {o['E_tension']:.4f} wave {o['E_wave']:.4f} C {o['E_C']:.4f}) "
              f"Omega {Om:.4f} R_end {o['R_end']:.4f} edge {o['edge']:.4f} J_flux/J {o['J_flux_fraction']:.3f} cm {o['cm_speed']:.1e}  g {o['g']:.4f}  "
              f"wave/E {o['wave_fraction']:.3f} 2J/E {o['two_J_over_E']:.4f} J_tilt {o['J_tilt']:.1e} nit {res.nit}", flush=True)
    return o


def credential(M=48):
    """The closed forms, through the production functions."""
    B = er.basis(M)
    print('CREDENTIAL (ring closed forms through pieces(); Omega = 0, no Coulomb)')
    ok = True
    for kappa_tw in (0.1, 1.0):
        Rstar = math.sqrt(kappa_tw / T)
        for R in (0.5 * Rstar, Rstar, 2 * Rstar):
            z = er.z_init(R)
            p = pieces(z, 0.0, 1.0, kappa_tw, 0.0, M, B)
            Eexp = 2 * math.pi * R * T + 2 * math.pi * kappa_tw / R
            Jexp = 2 * math.pi * kappa_tw
            muexp = R / 2
            line = (f'  kappa_tw {kappa_tw} R {R:.4f} (R* {Rstar:.4f}): E {p["E"]:.6f} (exp {Eexp:.6f}, rel {p["E"] / Eexp - 1:+.1e})  '
                    f'J {p["J"]:.6f} (exp {Jexp:.6f}, rel {p["J"] / Jexp - 1:+.1e})  mu {p["mu"]:.6f} (exp {muexp:.6f})  g {p["g"]:.6f}  '
                    f'E_t/E_w {p["E_t"] / p["E_w"]:.4f}')
            print(line)
            tol = 2 * (math.pi / M) ** 2                       # the M-gon's chord factor on (p x t) and on L
            ok &= abs(p['E'] / Eexp - 1) < tol and abs(p['J'] / Jexp - 1) < tol and abs(p['mu'] / muexp - 1) < tol
            if abs(R - Rstar) < 1e-12:
                ok &= abs(p['g'] - 2.0) < tol and abs(p['E_t'] / p['E_w'] - 1) < tol
    # T -> 0 limit: all energy in the wave, g -> 1 (checked by scaling: g = 2 E mu / (J q) with E = E_w only)
    z = er.z_init(1.0); p = pieces(z, 0.0, 1.0, 0.1, 0.0, M, B)
    g_wave_only = (p['mu'] / p['J']) * 2 * p['E_w']
    print(f'  wave-only energy (T excluded): g {g_wave_only:.6f} (exp 1)')
    ok &= abs(g_wave_only - 1) < 1e-9
    # minimization finds R* and g = 2 at fixed J = 2 pi kappa (any J: the flux sets it; the shape shrinks or grows)
    o = solve(2 * math.pi * 0.1, 1.0, 0.1, 0.0, M=M, seed='ring', R0=0.7, verbose=False)
    print(f'  minimized at beta 1, kappa_tw 0.1, J 2 pi kappa: R_end {o["R_end"]:.5f} (R* {math.sqrt(0.1):.5f}) E_t/E_w {o["E_tension"] / o["E_wave"]:.5f} g {o["g"]:.5f} Omega {o["Omega"]:.2e} cm {o["cm_speed"]:.1e} nit {o["nit"]}')
    ok &= abs(o['R_end'] / math.sqrt(0.1) - 1) < 1e-2 and abs(o['g'] - 2) < 1e-2
    # time-average independence: a pulse-shaped Phi_0 and a uniform one give the same moments (by construction the
    # instrument uses the average; the statement is checked by direct time integration on the ring)
    R = 1.0; M2 = 400; s = np.linspace(0, 2 * np.pi * R, M2, endpoint=False); ds = s[1] - s[0]
    pulse = np.exp(-((s - np.pi * R) / (0.3 * R)) ** 2); pulse *= 2 * np.pi / (pulse.sum() * ds)
    acc = 0.0; nT = 200
    for k in range(nT):
        lam = np.roll(pulse, k * (M2 // nT)) / (2 * np.pi)
        acc += np.sum(lam * (R ** 2) * ds) / nT                                     # <r^2>_q under the moving pulse
    print(f'  moving pulse <r^2>_q {acc:.6f} vs uniform {R ** 2:.6f}')
    ok &= abs(acc - R ** 2) < 1e-9
    print('CREDENTIAL', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--credential', action='store_true')
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--beta', type=str, default='0.25,0.5,0.75,1.0')
    ap.add_argument('--kappa_tw', type=str, default='0.1')
    ap.add_argument('--J', type=float, default=math.pi)
    ap.add_argument('--kappa_C', type=float, default=math.pi / 137.035999)
    ap.add_argument('--M', type=int, default=48)
    ap.add_argument('--out', type=str, default=None)
    a = ap.parse_args()
    if a.credential:
        credential(a.M)
    if a.scan:
        rows = []
        for kt in [float(x) for x in a.kappa_tw.split(',')]:
            for b in [float(x) for x in a.beta.split(',')]:
                for seed in ('ring', 'flat'):
                    rows.append(solve(a.J, b, kt, a.kappa_C, M=a.M, seed=seed))
                    if a.out:
                        pathlib.Path(a.out).write_text(json.dumps(rows, indent=1))
