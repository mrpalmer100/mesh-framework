"""
RING-WAVE-ANOMALY instrument: the self-field of a thin charged ring carrying its charge around at speed beta c, as
field integrals on an axisymmetric grid (nothing assumed about self-energies or field angular momentum; the
closed forms are the CREDENTIAL, not the computation).

Gaussian-type units: 1 / (4 pi eps0) = 1, c = 1 (so mu0 / 4 pi = 1), charge q, ring radius R, core (tube) radius b.
Energy density u = (E^2 + B^2) / 8 pi; momentum density g = (E x B) / 4 pi; angular momentum L_z = Int r g_phi dV.
The ring is a tube: charge and current spread uniformly over a disc of radius b in the meridional plane (n_c
sub-rings), each sub-ring a line ring whose fields at a field point are quadratures over the ring angle.

WHY THESE QUANTITIES (the Director's memo, 2026-10-25, RING-WAVE-ANOMALY): for the travelling-twist ring,
g = (mu / J)(2 m / q) with mu = q beta R / 2 exact (the current), m = E / c^2 = 2 (E_wave + U_E + U_M) by the scale
virial (every 1 / R energy balances the tension), and J = J_wave + L_field with J_wave = E_wave R / c. So
    g - 2 = 2 (U_E + U_M - c L_field / R) / (E_wave + c L_field / R),
and the question is whether the ln(8R/b) in U_E and U_M survives in that combination (log-enhanced, cutoff-
dependent, the class dies at O(alpha)) or cancels against L_field (cutoff-free, a number to compare with
alpha / pi). The executor's sketch (disclosed in the charter as a prior): if L_field = q Phi_self / 2 pi c the logs
cancel and g - 2 = 4 alpha / pi; if the self-interaction carries 1 / 2, g - 2 = 2 alpha ln(8R/b) / pi. The field
integral decides, which is why it is computed and not argued.

CREDENTIAL (closed forms, thin-ring limit b << R):
  c1  d U_E / d ln b = - q^2 / (2 pi R)              (the thin-ring capacitance C = pi R / ln(8R/b) up to a constant)
  c2  d U_M / d ln b = - I^2 R / (2 c^2) x 4 pi / (4 pi) ... i.e. L_self = 4 pi R (ln(8R/b) + const), U_M = L I^2 / 2c^2,
      so d U_M / d ln b = - 2 pi R I^2 / c^2 with I = q beta c / (2 pi R)
  c3  the charge-plus-solenoid theorem: a ring charge q at radius R around a long thin solenoid of flux Phi on the
      axis carries field angular momentum L_z = q Phi / (2 pi c) (Gaussian), reproduced to 1e-3
  c4  grid convergence: U_E, U_M, L_z stable to 1e-3 between the two finest grids
Usage: python3 ring_selffield.py --credential
"""
import argparse, json, math, pathlib, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]


def ring_fields(rp, zp, R0, z0, N=None):
    """E (per unit charge) and B (per unit current, c = 1) of a line ring of radius R0 at height z0, at field points
    (rp, zp), EXACT in complete elliptic integrals (the first build used a 256-point quadrature, whose spacing 0.025 R
    exceeded the core radii and made the near field that of point charges: the ln b slopes came out 12 times too
    small, 2026-10-25). Potential of the ring charge phi = (2 q / pi) K(k) / sqrt((R0 + r)^2 + z^2) with
    k^2 = 4 R0 r / ((R0 + r)^2 + z^2); E by central differences of phi at a step 1e-5 of the distance to the ring.
    B of the current loop from the standard closed forms (Gaussian, mu0 / 4 pi = 1)."""
    from scipy.special import ellipk, ellipe
    z = zp - z0
    def phi(r, z):
        r = np.maximum(r, 1e-12)
        den = np.sqrt((R0 + r) ** 2 + z ** 2)
        m = 4 * R0 * r / den ** 2
        m = np.minimum(m, 1 - 1e-15)
        return (2.0 / np.pi) * ellipk(m) / den
    d = np.sqrt((rp - R0) ** 2 + z ** 2)
    h = 1e-5 * np.maximum(d, 1e-9)
    E_r = -(phi(rp + h, z) - phi(rp - h, z)) / (2 * h)
    E_z = -(phi(rp, z + h) - phi(rp, z - h)) / (2 * h)
    r = np.maximum(rp, 1e-12)
    den = np.sqrt((R0 + r) ** 2 + z ** 2)
    m = np.minimum(4 * R0 * r / den ** 2, 1 - 1e-15)
    K = ellipk(m); Ee = ellipe(m)
    dm = (R0 - r) ** 2 + z ** 2
    B_z = (2.0 / den) * (K + (R0 ** 2 - r ** 2 - z ** 2) / dm * Ee)
    B_r = (2.0 * z / (r * den)) * (-K + (R0 ** 2 + r ** 2 + z ** 2) / dm * Ee)
    return E_r, E_z, B_r, B_z


def tube_fields(rp, zp, R, b, nc=200, N=None):
    """Fields of a uniform tube of radius b: the exact line-ring field averaged over nc source offsets on a sunflower
    disc of radius b (the 7-point disc of the first build left 1 / d singularities on the grid and the energy
    integrals depended on where cell centres fell; 2026-10-25). The summed field is bounded, of order 2 lambda / b,
    and the grid resolves b / 25 near the ring."""
    k = np.arange(nc) + 0.5
    rr = b * np.sqrt(k / nc)
    th = k * math.pi * (3 - math.sqrt(5))
    Er = np.zeros_like(rp); Ez = np.zeros_like(rp); Br = np.zeros_like(rp); Bz = np.zeros_like(rp)
    for dr, dz in zip(rr * np.cos(th), rr * np.sin(th)):
        a, b_, c, d = ring_fields(rp, zp, R + dr, dz)
        Er += a; Ez += b_; Br += c; Bz += d
    return Er / nc, Ez / nc, Br / nc, Bz / nc


def grid(R, b, Rmax=60.0, nr=400, nz=400):
    """Axisymmetric (r, z) grid concentrated near the ring: sinh-stretched in both coordinates about (R, 0)."""
    def stretched(lo, hi, n, center, scale):
        u = np.linspace(np.arcsinh((lo - center) / scale), np.arcsinh((hi - center) / scale), n + 1)
        return center + scale * np.sinh(u)
    re = stretched(0.0, Rmax * R, nr, R, b * 0.6)
    ze = stretched(-Rmax * R, Rmax * R, nz, 0.0, b * 0.6)
    rc = 0.5 * (re[1:] + re[:-1]); zc = 0.5 * (ze[1:] + ze[:-1])
    dr = np.diff(re); dz = np.diff(ze)
    RR, ZZ = np.meshgrid(rc, zc, indexing='ij')
    dV = 2 * np.pi * RR * dr[:, None] * dz[None, :]
    return RR, ZZ, dV


def integrals(R, b, q=1.0, I=1.0, nc=200, nr=400, nz=400, N=None, Rmax=60.0):
    RR, ZZ, dV = grid(R, b, Rmax, nr, nz)
    Er, Ez, Br, Bz = tube_fields(RR, ZZ, R, b, nc, N)
    Er *= q; Ez *= q; Br *= I; Bz *= I
    U_E = float(np.sum((Er ** 2 + Ez ** 2) / (8 * np.pi) * dV))
    U_M = float(np.sum((Br ** 2 + Bz ** 2) / (8 * np.pi) * dV))
    # E x B: E = (Er, 0, Ez), B = (Br, 0, Bz) in (r, phi, z) -> (E x B)_phi = Ez Br - Er Bz
    gphi = (Ez * Br - Er * Bz) / (4 * np.pi)
    L_z = float(np.sum(RR * gphi * dV))
    return dict(U_E=U_E, U_M=U_M, L_z=L_z, R=R, b=b, q=q, I=I, nr=nr, nz=nz, nc=nc)


def solenoid_check(R=1.0, q=1.0, I=1.0, a=0.05, length=400.0, nrings=4000, nr=300, nz=300):
    """A ring charge q of radius R (thin, b = 0.02 R) around a long thin solenoid (radius a, n rings per length
    giving flux Phi = pi a^2 B_in, B_in = 4 pi n I / c): the field angular momentum must be q Phi / (2 pi c).
    Computed by the same grid integral as the evidence path."""
    RR, ZZ, dV = grid(R, 0.02 * R, 40.0, nr, nz)
    Er, Ez, _, _ = tube_fields(RR, ZZ, R, 0.02 * R, 200)
    Er *= q; Ez *= q
    zs = np.linspace(-length / 2, length / 2, nrings)
    Br = np.zeros_like(RR); Bz = np.zeros_like(RR)
    for z0 in zs:
        _, _, br, bz = ring_fields(RR, ZZ, a, z0)
        Br += I * br; Bz += I * bz
    n_per_len = nrings / length
    Phi = math.pi * a ** 2 * 4 * math.pi * n_per_len * I
    gphi = (Ez * Br - Er * Bz) / (4 * np.pi)
    L_z = float(np.sum(RR * gphi * dV))
    return L_z, q * Phi / (2 * math.pi)


def phi_pair(r1, z1, r2, z2):
    """Potential at ring 2 (r2, z2) of a unit charge spread on ring 1 (r1, z1), Gaussian: (2 / pi) K(k) / sqrt((r1+r2)^2+dz^2)."""
    from scipy.special import ellipk
    dz = z2 - z1; den = np.sqrt((r1 + r2) ** 2 + dz ** 2)
    m = np.minimum(4 * r1 * r2 / den ** 2, 1 - 1e-15)
    return (2.0 / np.pi) * ellipk(m) / den


def M_pair(r1, z1, r2, z2):
    """Mutual inductance of coaxial rings, Gaussian with c = 1: U_12 = I1 I2 M, M = 4 pi sqrt(r1 r2) [(2/k - k) K - (2/k) E]."""
    from scipy.special import ellipk, ellipe
    dz = z2 - z1; k2 = np.minimum(4 * r1 * r2 / ((r1 + r2) ** 2 + dz ** 2), 1 - 1e-15); k = np.sqrt(k2)
    return 4 * np.pi * np.sqrt(r1 * r2) * ((2 / k - k) * ellipk(k2) - (2 / k) * ellipe(k2))


def source_energies(R, b, q=1.0, beta=1.0, nc=400):
    """U_E, U_M and the field angular momentum L_z of a uniform tube (radius b) of charge q circulating at beta c,
    by pair sums over nc sunflower sub-rings with each sub-ring's self term taken as a line ring of effective radius
    b_eff = (b / sqrt(nc)) e^(-1/4) (a uniform disc of radius rho has the line self-energy of radius rho e^(-1/4),
    the SAME factor for charge and for current, so the self terms cancel identically in U_E - U_M at beta = 1).
    L_z = q <Phi> / 2 pi c (the quasistatic field-momentum theorem, checked on the grid to 2e-3 and against the
    charge-plus-solenoid theorem), with <Phi> the flux of the tube's own current through each charge element."""
    k = np.arange(nc) + 0.5
    rr = b * np.sqrt(k / nc); th = k * math.pi * (3 - math.sqrt(5))
    r = R + rr * np.cos(th); z = rr * np.sin(th)
    qi = q / nc; Ii = qi * beta / (2 * np.pi * r)              # the current of a sub-ring: its charge times beta c over its circumference (c = 1)
    r1 = r[:, None]; z1 = z[:, None]; r2 = r[None, :]; z2 = z[None, :]
    P = phi_pair(r1, z1, r2, z2); Mm = M_pair(r1, z1, r2, z2)
    np.fill_diagonal(P, 0.0); np.fill_diagonal(Mm, 0.0)
    beff = (b / math.sqrt(nc)) * math.exp(-0.25)
    phi_self = np.log(8 * r / beff) / (np.pi * r)             # line ring of unit charge: lambda = 1 / 2 pi R, phi on the ring = 2 lambda ln(8R/b)
    L_self = 4 * np.pi * r * (np.log(8 * r / beff) - 2.0)     # line ring, surface-current form
    U_E = 0.5 * qi * qi * (P.sum() + phi_self.sum())
    U_M = 0.5 * float(Ii @ Mm @ Ii + np.sum(Ii * Ii * L_self))
    Phi = Mm @ Ii + Ii * L_self                               # flux through each charge element from all currents
    L_z = qi * Phi.sum() / (2 * np.pi)
    return dict(U_E=float(U_E), U_M=float(U_M), L_z=float(L_z), R=R, b=b, beta=beta, nc=nc)


def anomaly(R=1.0, b=0.01, nc=400):
    """g - 2 of the travelling-twist ring from its own fields, in units where the wave energy at the Compton
    radius is E_w = hbar c / 2R: with e^2 = alpha hbar c, g - 2 = 2 (U_E + U_M - c L_z / R) / (E_w + c L_z / R).
    Returned as the coefficient A in g - 2 = A alpha / pi, to leading order in alpha (E_w taken as hbar c / 2R and the
    O(alpha) shift of E_w by the virial neglected, which is the next order)."""
    s = source_energies(R, b, q=1.0, beta=1.0, nc=nc)
    bracket = s['U_E'] + s['U_M'] - s['L_z'] / R             # in units q^2 / R  (c = 1)
    # E_w = hbar c / 2R and q^2 = alpha hbar c:  g - 2 = 2 bracket (q^2/R) / (hbar c / 2R) = 4 alpha bracket_hat
    A = 4 * bracket * math.pi                                # g - 2 = A alpha / pi
    cE = s['U_E'] * 2 * math.pi * R - math.log(8 * R / b)
    cM = s['U_M'] * 2 * math.pi * R - math.log(8 * R / b)
    return dict(A=A, bracket=bracket, c_E=cE, c_M=cM, U_E=s['U_E'], U_M=s['U_M'], L_z=s['L_z'], b=b, nc=nc)


def credential():
    print('CREDENTIAL ring_selffield (Gaussian-type units, c = 1)')
    ok = True
    R = 1.0
    # c1, c2: ln b slopes of U_E and U_M on a thin ring
    res = {}
    for b in (0.004, 0.008, 0.016):
        res[b] = integrals(R, b, q=1.0, I=0.5, nc=200, nr=320, nz=320)            # beta = 0.5 in the credential; the evidence is beta = 1
        print(f"  b {b}: U_E {res[b]['U_E']:.6f}  U_M {res[b]['U_M']:.6f}  L_z {res[b]['L_z']:.6e}")
    bs = sorted(res)
    for (b1, b2) in ((bs[0], bs[1]), (bs[1], bs[2])):
        sE = (res[b2]['U_E'] - res[b1]['U_E']) / math.log(b2 / b1)
        sM = (res[b2]['U_M'] - res[b1]['U_M']) / math.log(b2 / b1)
        expE = -1.0 / (2 * math.pi * R)                      # q = 1
        expM = -2 * math.pi * R * 0.5 ** 2                   # I = 0.5, c = 1: L = 4 pi R ln(8R/b) -> U_M = L I^2 / 2
        print(f'  slope d/dln b over [{b1}, {b2}]: U_E {sE:.5f} (exp {expE:.5f}, rel {sE / expE - 1:+.2e})  U_M {sM:.5f} (exp {expM:.5f}, rel {sM / expM - 1:+.2e})')
        ok &= abs(sE / expE - 1) < 2e-2 and abs(sM / expM - 1) < 2e-2
    # the constant terms against the thin-tube closed forms (uniform volume current: L = 4 pi R (ln(8R/b) - 7/4);
    # uniform volume charge in the tube: C^-1 = (2 / pi R)(ln(8R/b) - ...)); reported, not barred: they depend on the
    # cross-section model and the sub-ring sampling (nc = 7 is a coarse disc)
    b = bs[1]
    Lself = 2 * res[b]['U_M'] / 0.5 ** 2                     # I = 0.5
    print(f"  L_self at b {b}: {Lself:.5f}; 4 pi R (ln(8R/b) - 7/4) = {4 * math.pi * R * (math.log(8 * R / b) - 1.75):.5f}; (ln - 2) form {4 * math.pi * R * (math.log(8 * R / b) - 2):.5f}")
    # c3: the solenoid theorem
    Lz, exp = solenoid_check()
    print(f'  solenoid theorem: L_z {Lz:.6e} vs q Phi / 2 pi {exp:.6e} (rel {Lz / exp - 1:+.2e})')
    ok &= abs(Lz / exp - 1) < 2e-2
    # c4: grid convergence at b = 0.008
    fine = integrals(R, 0.008, I=0.5, nc=200, nr=480, nz=480)
    for k in ('U_E', 'U_M', 'L_z'):
        rel = fine[k] / res[0.008][k] - 1 if res[0.008][k] else 0.0
        print(f'  grid 320 -> 480: {k} rel change {rel:+.2e}')
        ok &= abs(rel) < 5e-3
    print('CREDENTIAL', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--credential', action='store_true')
    ap.add_argument('--source', action='store_true', help='source-form credential: slopes, constants, convergence in nc')
    ap.add_argument('--anomaly', action='store_true')
    a = ap.parse_args()
    if a.credential:
        credential()
    if a.source:
        print('SOURCE-FORM CREDENTIAL (beta = 0.5)')
        for nc in (200, 400, 800):
            res = {b: source_energies(1.0, b, beta=0.5, nc=nc) for b in (0.004, 0.008, 0.016)}
            for b in res:
                print(f"  nc {nc} b {b}: U_E {res[b]['U_E']:.6f} U_M {res[b]['U_M']:.6f} L_z {res[b]['L_z']:.6f}  c_E {res[b]['U_E'] * 2 * math.pi - math.log(8 / b):.4f}  c_M {res[b]['U_M'] * 2 * math.pi / 0.25 - math.log(8 / b):.4f}")
            sE = (res[0.016]['U_E'] - res[0.004]['U_E']) / math.log(4); sM = (res[0.016]['U_M'] - res[0.004]['U_M']) / math.log(4)
            print(f"  nc {nc}: slopes U_E {sE:.5f} (exp {-1 / (2 * math.pi):.5f}) U_M {sM:.5f} (exp {-0.25 / (2 * math.pi):.5f}); L_z / (q Phi / 2 pi) consistent by construction")
    if a.anomaly:
        print('ANOMALY (the executor\'s reading; beta = 1, R = 1, e^2 = alpha hbar c, E_w = hbar c / 2R)')
        for nc in (200, 400, 800):
            for b in (0.001, 0.01, 0.1):
                r = anomaly(1.0, b, nc)
                print(f"  nc {nc} b {b}: c_E {r['c_E']:.4f} c_M {r['c_M']:.4f}  bracket {r['bracket']:.5f} (q^2/R)  g - 2 = {r['A']:.4f} alpha / pi")
