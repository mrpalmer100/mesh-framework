"""The ELECTRON LEDGER's numbers (analysis/ELECTRON_LEDGER.md, section 6): the rotating-string closed forms and
what they give with the electron's mass and spin as inputs. An executor's exploratory computation, 2026-10-23;
registers nothing. Pure arithmetic; no corpus instrument is run.

A string of tension T rotating rigidly about its midpoint with its ends at the speed of light (the Regge
rotator) has, from the relativistic energy and angular-momentum densities T gamma and T gamma omega r^2 / c^2
integrated over r in [-R, R] with omega = c / R:
    E = pi T R,         J = pi T R^2 / (2 c),       so   J = E^2 / (2 pi T c)   (the Regge relation)
and therefore, for ANY tension,   R = 2 c J / E.
A unit charge carried at one lightlike end is a current q c / (2 pi R) around an area pi R^2:
    mu = q c R / 2,     g = (mu / J)(2 m / q) with m = E / c^2  =  2   exactly, for any T and R.
With J = hbar / 2 and E = m_e c^2:  R = hbar / (m_e c) = the reduced Compton wavelength, and the tension that
carries the electron is T_eff = m_e^2 c^3 / (pi hbar).
"""
import math

HBAR = 1.054571817e-34
C = 2.99792458e8
M_E = 9.1093837e-31
ALPHA = 1 / 137.035999
T0_MPOINT = 434.0            # J/m, FND-MATTER-044
N_SUB = (4.6e9, 1.3e10)      # FND-083's priced window


def rotator(T, R):
    E = math.pi * T * R
    J = math.pi * T * R ** 2 / (2 * C)
    return E, J


def main():
    T_eff = M_E ** 2 * C ** 3 / (math.pi * HBAR)
    R = HBAR / (M_E * C)
    E, J = rotator(T_eff, R)
    print(f'T_eff = m_e^2 c^3 / (pi hbar) = {T_eff:.5e} J/m')
    print(f'R = hbar / (m_e c)            = {R:.5e} m  (reduced Compton wavelength)')
    print(f'E = pi T_eff R                = {E:.5e} J   against m_e c^2 = {M_E * C ** 2:.5e} J  (ratio {E / (M_E * C ** 2):.12f})')
    print(f'J = pi T_eff R^2 / (2c)       = {J:.5e} J s against hbar/2 = {HBAR / 2:.5e} J s  (ratio {J / (HBAR / 2):.12f})')
    mu = 1.602176634e-19 * C * R / 2
    mu_B = 1.602176634e-19 * HBAR / (2 * M_E)
    print(f'mu = q c R / 2                = {mu:.5e} J/T against mu_B = {mu_B:.5e} J/T (ratio {mu / mu_B:.12f}); g = (mu/J)(2m/q) = {(mu / J) * (2 * M_E / 1.602176634e-19):.12f}')
    print(f'edge speed omega R = c exactly; rotation period 2 pi R / c = {2 * math.pi * R / C:.4e} s; frequency {C / (2 * math.pi * R):.4e} Hz (half the zitterbewegung frequency 2 m c^2 / h)')
    print(f'electrostatic self-energy of a unit charge at scale R, alpha hbar c / R, over m_e c^2 = {ALPHA:.5f}')
    print(f'T0 (M-point) / T_eff = {T0_MPOINT / T_eff:.4e}: the electron is carried by 1/{T0_MPOINT / T_eff:.0f} of a coarse strand\'s tension')
    for n in N_SUB:
        print(f'  at n_sub = {n:.1e}: T0_f = {T0_MPOINT / n:.3e} J/m, sub-strands carrying T_eff = {T_eff / (T0_MPOINT / n):.3e}')
    # the Regge check at the muon and tau: same T_eff would need J = E^2/(2 pi T c)
    for name, m in (('muon', 1.883531627e-28), ('tau', 3.16754e-27)):
        Em = m * C ** 2
        print(f'  {name} on the SAME tension: J = E^2/(2 pi T_eff c) = {Em ** 2 / (2 * math.pi * T_eff * C) / (HBAR / 2):.1f} x hbar/2 (a spin-1/2 lepton cannot sit on the electron\'s Regge line; its tension would be {m ** 2 * C ** 3 / (math.pi * HBAR):.3e} J/m)')


if __name__ == '__main__':
    main()
