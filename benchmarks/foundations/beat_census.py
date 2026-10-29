"""The beat census (executor reading, 2026-10-27): every registered frequency of the medium in physical units,
against the beat the clean-room study needs, Omega = 2 m_e c^2 / hbar = 1.55e21 rad/s (a length c / Omega =
lambda-bar_C / 2 = 1.93e-13 m = 3,200 spacings). Closed forms on the card; no fit. The rule: a frequency counts only
if a registered mode oscillates at it; a combination of constants that lands is not a mode."""
import math
HBAR = 1.054571817e-34; C = 2.99792458e8; ME = 9.1093837015e-31
T0, A, DC = 434.0, 6.0e-17, 1.87e-19; MU = T0 / C ** 2; R_ROD = DC / 2
OMEGA = 2 * ME * C ** 2 / HBAR; L = C / OMEGA
print(f'target: Omega = {OMEGA:.3e} rad/s, length c / Omega = {L:.3e} m = {L / A:.0f} a')
rows = []
def add(name, om, note=''):
    rows.append((name, om, note)); print(f'  {name:52s} {om:10.2e}  ({om / OMEGA:9.2e} x Omega)  {note}')
print('registered modes:')
add('transverse wave, lattice cutoff 2c/a', 2 * C / A, 'FND-STRAND-001 chain; no gap below it')
add('node bond, c/a (harmonic point junction)', C / A, 'JUNCTION-LOCK: the node is a point with a harmonic bond')
add('longitudinal cutoff c_L/a at k/T0 = 2', math.sqrt(2) * C / A, 'EM-RECON-009 branch')
add('longitudinal cutoff c_L/a at k/T0 = 1.9e8', math.sqrt(1.9e8) * C / A, 'QB-008 branch')
add('torsion wave: Goldstone, gap 0', 0.0, 'GRV-020; JUNCTION-LOCK f = 0: no on-site well at the registered level')
vt = math.sqrt(4.21e-36 / (MU * R_ROD ** 2))
add('torsional segment mode pi v_t/a (v_t = sqrt(C/I_T))', math.pi * vt / A, f'v_t = {vt / C:.2f} c; a segment of {math.pi * vt / OMEGA / A:.0f} a would beat at Omega')
add('twist gap under the junction tie f = 3.5', math.sqrt(3.5 * T0 * A / 2 / (MU * R_ROD ** 2 * A)), 'STRAND-MASS-SCALE omega_min^2 = V_0 c^2/(T0 a r^2); the one registered gap route')
kp = 0.5 * T0 * (0.43 * 0.6272 * A) ** 2
add('two-strand ring-wave c/R*, R* = sqrt(kappa_pair/T0)', C / math.sqrt(kp / T0), 'Leg C at the card')
add('granted rope ring mode c/R, R = 113 a (FND-188)', C / (113 * A), 'HBAR-ROPE rider')
add('HBAR-005 patch c/(74.6 w)', C / (74.6 * 5.78e-17), 'the mesoscopic patch as a length')
add('fine-level rotating wave, c/a_f at a_f = lambda/4 (1.4 PeV)', C / 2.21e-22, 'FND-130/131, FND-087')
# the standoff mode of the pair: omega^2 = K_c / mu with K_c ~ A_c / sigma0^2 per length; A_c unpriced; the A_c that would land
sig0 = 0.6272 * A
Ac_needed = OMEGA ** 2 * sig0 ** 2 * MU
print(f"  pair standoff mode sqrt(A_c/(sigma0^2 mu)): UNPRICED (A_c); lands at Omega for A_c = {Ac_needed:.2e} J/m = {Ac_needed / T0:.1e} T0,"
      f" i.e. {Ac_needed * sig0:.1e} J per crossing against the registered bound A_c > 0.40 T0 a = {0.4 * T0 * A:.1e} J: excluded by {0.4 * T0 * A / (Ac_needed * sig0):.0e}")
print('dimensional: HBAR-005 audited every length from (w, d_c): the Compton scale needs w^1.752 d_c^-0.752, no natural exponent.')
near = [r for r in rows if r[1] > 0 and abs(math.log10(r[1] / OMEGA)) < 1.5]
print(f'within 1.5 orders of Omega: {[r[0] for r in near] or "none"}')
