"""GRANT-CANDIDATE-SWEEP, cheap test T-3 (sandbox, 2026-10-27): does the kink present a point charge?
The charge of the kink is its winding density Phi'(s) = (2 / l) sech(s / l) ALONG the rope (l = c / Omega =
lambda-bar_C / 2) carried on strands at radius rho ACROSS the rope (rho = d0 / 2 for the pair, a sqrt(n) for a bundle
of n at disk packing). A probe of momentum transfer q sees the form factor F(q) = F_par(q) F_perp(q) with
F_par(q) = sech(pi q l / 2) (the Fourier transform of sech) and F_perp(q) = J0(q rho) for charge on a ring of
radius rho (the azimuthal average of the twisted pair). Two comparisons, each a closed form:
  (a) along the rope: the mean-square length <s^2> = (pi^2 / 12) l^2 against the Dirac electron's own Darwin
      spread, <r^2>_Darwin = 3 lambda-bar_C^2 / 4 (Foldy): the Compton-scale structure QED already has;
  (b) across the rope: the momentum transfer at which |1 - F_perp| reaches 1 percent, against the reach of
      e+ e- -> e+ e- tests of QED (PETRA, 1980s: Lambda of a few hundred GeV, q up to about 30 GeV/c at 1 percent;
      LEP2: q of order 100 GeV/c), which bound a transverse charge radius to about 4e-19 m."""
import math
HBAR = 1.054571817e-34; C = 2.99792458e8; ME = 9.1093837015e-31; GEV = 1.602176634e-10
LC = HBAR / (ME * C); ell = LC / 2
A = 6.0e-17; d0 = 0.43 * 0.6272 * A
print(f'kink length l = lambda-bar_C / 2 = {ell:.3e} m')
s2 = math.pi ** 2 / 12 * ell ** 2; darwin = 0.75 * LC ** 2
print(f'(a) along the rope: <s^2>^(1/2) = {math.sqrt(s2):.3e} m; the Dirac electron\'s Darwin spread <r^2>^(1/2) = {math.sqrt(darwin):.3e} m; ratio of <r^2>: {s2 / darwin:.2f}')
print(f'    F_par at q = m_e c / hbar: {1 / math.cosh(math.pi * (1 / LC) * ell / 2):.3f}; at q = 0.1 m_e c / hbar: {1 / math.cosh(math.pi * 0.1 * ell / LC / 2):.5f}')
print('    reading: a Compton-length kink has the same order of charge spread QED already attributes to the electron (the Darwin term); not a kill.')
print('(b) across the rope: F_perp = J0(q rho); |1 - F| = 1 percent at q rho = 0.2 (J0(x) = 1 - x^2/4 + ...)')
for q_gev, label in ((30.0, 'PETRA-class QED test, 1 percent'), (100.0, 'LEP2-class, 1 percent')):
    q = q_gev * GEV / (HBAR * C)
    print(f'    q = {q_gev:.0f} GeV/c ({label}): transverse radius must satisfy rho < 0.2 / q = {0.2 / q:.2e} m')
for name, rho in (('registered pair, d0 / 2', d0 / 2), ('bundle of 50 (disk), a sqrt 50', A * math.sqrt(50)), ('bundle of 373 (pair packing), ~ (373/2) d0 / 2', 373 / 2 * d0 / 2)):
    q100 = 100.0 * GEV / (HBAR * C); x = q100 * rho
    from scipy.special import j0
    print(f'    {name:44s} rho = {rho:.2e} m: q rho at 100 GeV/c = {x:.1f}, F_perp = {j0(x):+.3f}; exceeds the 1 percent bound by {rho / (0.2 / q100):.0f}x')
print('    reading: any charge carried on strands at the registered spacing has a transverse radius 20 to 1000 times above what')
print('    e+e- scattering allows; the kink on a registered rope is NOT pointlike across the rope. The only loophole is a rule that')
print('    the winding\'s field is sourced on the centreline with no transverse multipoles, which nothing registered supplies.')
