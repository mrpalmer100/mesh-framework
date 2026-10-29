"""N1 of FND-188 (GRANT-HBAR-ROPE): the electron scale wall of the travelling-twist class re-priced on the registered
objects, as closed forms on the card (executor reading, 2026-10-27). No solver, no fit. Carries the HBAR-ROPE rider
(FND-188 C2) and is NOT a confrontation of hbar, m_e or the magnetic moment (C3): it states where the class's
(E, J) land on registered objects, with the electron's (m_e c^2, hbar / 2) as the fixed point the class must reach.

THE CLASS (Leg C, analysis/ELEC_MECH_1_legC_instrument.md): a closed rope of tension T and twist stiffness kappa with
its one unit of twist travelling at c is static at R* = sqrt(kappa / T) with E = 4 pi sqrt(kappa T) (virial, half
tension half wave) and J = 2 pi kappa / c, hence g = 2 and the REGGE-LIKE RELATION E^2 = 8 pi T c J, independent of
kappa. The electron's point (E, J) = (m_e c^2, hbar / 2) therefore fixes the tension the class needs,
T* = m_e^2 c^3 / (4 pi hbar) = 1.69e-2 J/m, whatever kappa is; kappa* = hbar c / 4 pi then fixes R* = lambda-bar_C.

THE OBJECTS (docs/ROPE_PARAMETERS.md): a strand (T0 = 434 J/m, a = 6.0e-17 m); the two-strand pair at standoff
d0 = (0.40 to 0.46) x 0.6272 a with kappa_pair = T0 d0^2 / 2 (+ 2C, negligible); a rope of n strands as a uniform
bundle of radius a sqrt(n) with T = n T0 and kappa = sum T0 rho^2 = n T0 R^2 / 2 (the pair formula applied strand by
strand); the granted rope n_rs = 12,882 (FND-188); the fine level T0_f = T0 / n_sub with n_sub >= 4.6e9 (FND-087's
priced window; FINE-DISP-1).
"""
import math

HBAR = 1.054571817e-34; C = 2.99792458e8; ME = 9.1093837015e-31; EV = 1.602176634e-19
T0, A = 434.0, 6.0e-17
LAMBDA_C = HBAR / (ME * C)
E_E, J_E = ME * C ** 2, HBAR / 2


def ring(kappa, T):
    R = math.sqrt(kappa / T); E = 4 * math.pi * math.sqrt(kappa * T); J = 2 * math.pi * kappa / C
    return R, E, J


def row(label, kappa, T):
    R, E, J = ring(kappa, T)
    print(f'  {label:38s} T {T:9.3e} J/m  kappa {kappa:9.3e} J m  R* {R:9.3e} m  E {E / EV / 1e6:10.4g} MeV ({E / E_E:9.3g} m_e)  '
          f'J {J / HBAR:10.4g} hbar ({J / J_E:9.3g} x hbar/2)')
    return R, E, J


if __name__ == '__main__':
    T_star = ME ** 2 * C ** 3 / (4 * math.pi * HBAR); kappa_star = HBAR * C / (4 * math.pi)
    print(f'THE CLASS NEEDS: T* = m_e^2 c^3 / 4 pi hbar = {T_star:.3e} J/m = T0 / {T0 / T_star:.3g};  kappa* = hbar c / 4 pi = {kappa_star:.3e} J m;  R* = {math.sqrt(kappa_star / T_star):.3e} m = lambda-bar_C ({LAMBDA_C:.3e})')
    print(f'  Regge-like relation of the class: E^2 = 8 pi T c J; at the electron point T = {E_E ** 2 / (8 * math.pi * C * J_E):.3e} J/m (the same T*).')
    print('ON THE REGISTERED OBJECTS (M-point card):')
    for frac in (0.40, 0.46):
        d0 = frac * 0.6272 * A
        row(f'two-strand pair, d0 = {frac} x 0.6272 a', 0.5 * T0 * d0 ** 2, T0)
    n_rs = 12882
    row('granted rope, n_rs = 12,882 (FND-188)', n_rs * T0 * (A ** 2 * n_rs) / 2, n_rs * T0)
    # the bundle that carries J = hbar / 2: J = 2 pi kappa / c = pi n^2 T0 a^2 / c = 2 n^2 S1, with n_rs S1 = hbar
    S1 = math.pi * T0 * A ** 2 / (2 * C)
    n_half = math.sqrt(n_rs / 4)
    row(f'bundle with J = hbar/2: n = {n_half:.1f} strands', n_half ** 2 * T0 * A ** 2 / 2, n_half * T0)
    for n_sub in (4.6e9, 1.3e10):
        Tf = T0 / n_sub; af = A / math.sqrt(n_sub); d0f = 0.43 * 0.6272 * af
        row(f'fine-level pair, n_sub = {n_sub:.1e}', 0.5 * Tf * d0f ** 2, Tf)
    print('THE LADDER AGAINST T*:')
    print(f'  strand T0 = {T0} J/m is {T0 / T_star:.3g} x T*;  any bundle of n strands is n x that;  the fine level T0_f = T0 / n_sub is '
          f'{T0 / 4.6e9 / T_star:.2g} to {T0 / 1.3e10 / T_star:.2g} x T* at the priced window.')
    print(f'  The rung the class needs, T* = T0 / {T0 / T_star:.0f}, lies between the strand and the fine level; the ladder (FND-110) has no rung there.')
    print('WHAT MOVED UNDER THE GRANT: nothing toward the electron. The pair already has E near m_e c^2 (by the M-point calibration, '
          'FND-MATTER-044, not a prediction) and J short by 4e4; the granted rope overshoots both.')
