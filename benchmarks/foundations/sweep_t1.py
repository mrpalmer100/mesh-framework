"""GRANT-CANDIDATE-SWEEP, cheap test T-1 (sandbox, 2026-10-27): the chain from a weak azimuthal lock to the beat, the
kink, and the charge-creation field, in closed forms. The rope's internal azimuth Phi has twist stiffness kappa (J m)
and, for the tension-geometric stiffness kappa = T0 sum rho^2, an inertia per length I = mu sum rho^2 = kappa / c^2
EXACTLY (FND-006, mu = T0 / c^2). A lock V(Phi) = V_0 (1 - cos Phi) per node, curvature V'' = V_0 / a per length, gives:
  the beat          Omega^2 = V'' / I = V'' c^2 / kappa
  the kink width    l = sqrt(kappa / V'') = c / Omega        (the screening length, by identity)
  the kink energy   E = 8 sqrt(kappa V'') = 8 kappa Omega / c
  the kink action   E / Omega = 8 kappa / c                   (no free amplitude)
  charge creation   E_c = (4 pi / 5) V_0 / (e a) = (4 pi / 5) V'' / e   (FND-182's identity, STRAND-MASS-SCALE)
Imposing the electron (E = m_e c^2, action 8 kappa / c = hbar / 2 so that Omega is the zitter frequency) fixes every
quantity; the test prints them and the strand count the stiffness needs under two packings."""
import math
HBAR = 1.054571817e-34; C = 2.99792458e8; ME = 9.1093837015e-31; E_CH = 1.602176634e-19; EV = E_CH
T0, A = 434.0, 6.0e-17
kappa = HBAR * C / 16
Omega = 2 * ME * C ** 2 / HBAR
Vpp = kappa * Omega ** 2 / C ** 2
V0 = Vpp * A
f = V0 / (T0 * A / 2)
Ec = (4 * math.pi / 5) * Vpp / E_CH
ES = ME ** 2 * C ** 3 / (E_CH * HBAR)
ell = math.sqrt(kappa / Vpp)
E = 8 * math.sqrt(kappa * Vpp)
print(f'kappa = hbar c / 16 = {kappa:.3e} J m  (the pair has {0.5 * T0 * (0.43 * 0.6272 * A) ** 2:.2e}; FND-188 rope {12882 ** 2 * T0 * A ** 2 / 2:.2e})')
print(f'Omega = 2 m_e c^2 / hbar = {Omega:.3e} rad/s;  kink width l = c / Omega = {ell:.3e} m = {ell / A:.0f} a (coasts: far above 2.8 a)')
print(f'lock curvature V\'\' = kappa Omega^2 / c^2 = m_e^2 c^3 / 4 hbar = {Vpp:.3e} J/m;  V_0 per node = {V0:.3e} J = {V0 / EV:.1f} eV;  f = V_0 / (T0 a / 2) = {f:.2e}')
print(f'kink energy E = 8 kappa Omega / c = {E:.3e} J = {E / (ME * C * C):.4f} m_e c^2;  action 8 kappa / c = {8 * kappa / C / HBAR:.3f} hbar')
print(f'charge-creation field E_c = (4 pi / 5) V\'\' / e = {Ec:.3e} V/m = {Ec / ES:.3f} x Schwinger ({ES:.3e}); = pi / 5 exactly;  laser record 9.1e14: {Ec / 9.1e14:.0f} x above')
n_disk = math.sqrt(2 * kappa / (T0 * A * A)); n_pair = 2 * math.sqrt(kappa / (0.5 * T0 * (0.43 * 0.6272 * A) ** 2))
print(f'strand count for kappa: disk packing n = {n_disk:.0f} (R = a sqrt n = {A * math.sqrt(n_disk):.2e} m); pair packing n = {n_pair:.0f}')
print('identities: E_c / E_Schwinger = pi / 5 and l = c / Omega hold for ANY kappa once E = m_e c^2 and 8 kappa / c = hbar / 2 are imposed; kappa itself is the one input.')
