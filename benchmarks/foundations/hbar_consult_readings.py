"""Two readings from the hbar consult of 2026-10-26 (analysis/consults/HBAR_consult_2026-10-26.md), closed forms on
registered numbers; no solver, no fit. Run: python3 benchmarks/foundations/hbar_consult_readings.py

READING A (idea 3 of the executor's memo): the rope's own twist stiffness as the action quantum.
  J_1 = 2 pi kappa_pair / c for the travelling-twist ring (Leg C), against hbar / 2, with kappa_pair from the card:
  the tension-geometric term T0 d0^2 / 2 (two strands at radius d0 / 2 lengthen as the pair twists) plus the strands'
  own rod torsion 2 C. d0 = (0.40 to 0.46) sigma0 with sigma0 = w the strand width and w / a = 0.6272 (EM-RECON-018,
  FND-068); C = 4.21e-36 J m (lattice branch) or 5.95e-36 (Sigma route), GRV-073 / docs/ROPE_PARAMETERS.md; T0 and a
  at the M-point (FND-MATTER-044) and at the pre-M-point values HBAR-003 used (T = 1700 J/m, w = 0.0578 fm), so the
  registered 3549 is reproduced and its M-point value stated.
  The executor's chat estimate of 2026-10-26 ('dead by nine orders') used d0 at the strand THICKNESS d_c scale; the
  card's standoff is a quarter of a spacing, and this script is the correction.

READING B (idea 2): the mesoscopic patch as GRV-028's screening length.
  HBAR-005: hbar = pi T L^2 / 2c needs L_hbar / w = 74.6 (a patch 75 spacings across). GRV-028: the gap-mismatch
  scalar's mass^2 per site is the O(1) bare elastic cost minus the universal zero-point correction 0.019 (closed form
  -(1/8)<lambda^(-3/2)>), net positive with a 50x margin. A Yukawa range xi = a / m. The patch would need
  m^2 = (a / L_hbar)^2; compare with what the registered margin allows.
"""
import math

HBAR = 1.054571817e-34; C_LIGHT = 2.99792458e8


def reading_a():
    print('READING A: the twist route, J_1 = 2 pi kappa_pair / c against hbar / 2')
    rows = []
    for label, T0, a in (('M-point (card)', 434.0, 6.0e-17), ('HBAR-003 point', 1700.0, 5.78e-17)):
        S1 = math.pi * T0 * a ** 2 / (2 * C_LIGHT)
        print(f'  {label}: T0 {T0} J/m, a {a:.3e} m: S1 = pi T0 a^2 / 2c = {S1:.3e} J s, hbar / S1 = {HBAR / S1:.0f}')
        w = 0.6272 * a
        for frac in (0.40, 0.46):
            d0 = frac * w
            kT = 0.5 * T0 * d0 ** 2
            for Cname, Cval in (('C lattice', 4.21e-36), ('C Sigma', 5.95e-36)):
                for rod in (0.0, 2 * Cval):
                    kappa = kT + rod
                    J1 = 2 * math.pi * kappa / C_LIGHT
                    F = (HBAR / 2) / J1
                    rows.append((label, frac, Cname, rod > 0, kappa, J1, F))
        # print the band
        sub = [r for r in rows if r[0] == label]
        Fs = [r[6] for r in sub]
        kap = [r[4] for r in sub]
        print(f'    d0 = (0.40 to 0.46) x 0.6272 a = {0.40 * w:.2e} to {0.46 * w:.2e} m; kappa_pair = {min(kap):.2e} to {max(kap):.2e} J m '
              f'(2C adds {2 * 4.21e-36 / min(kap):.1e} to {2 * 5.95e-36 / min(kap):.1e} of it); kappa_pair / (T0 a^2) = {min(kap) / (T0 * a * a):.3f} to {max(kap) / (T0 * a * a):.3f}')
        print(f'    J_1 = {min(r[5] for r in sub):.2e} to {max(r[5] for r in sub):.2e} J s;  F = (hbar / 2) / J_1 = {min(Fs):.2e} to {max(Fs):.2e}')
    print('  ACTION-BRIDGE F-LOR rows for comparison: 2.2e3 to 9.0e3 (GRV-092 point); 1.4e4 to 4.2e4 (the three scale sets).')
    return rows


def reading_b():
    print('READING B: the patch as the screening length')
    L_over_a = 74.6
    m2_needed = 1.0 / L_over_a ** 2
    zp = 0.019
    print(f'  patch needs xi / a = {L_over_a} i.e. m^2 = {m2_needed:.2e} per site (lattice units)')
    print(f'  GRV-028: zero-point correction -{zp} per site; bare cost O(1) with a 50x margin (bare about 1; the margin edge is bare = {50 * zp:.2f})')
    for bare in (1.0, 50 * zp, zp + m2_needed):
        m2 = bare - zp
        xi = 1 / math.sqrt(m2) if m2 > 0 else float('inf')
        print(f'    bare {bare:.4f}: net m^2 {m2:.4f}, xi / a = {xi:.2f}, action ratio (xi / L_hbar)^2 = {(xi / L_over_a) ** 2:.2e}')
    print('  The patch requires the bare cost tuned to within 1 percent of the zero-point correction (bare = 0.0192), against a registered O(1);')
    print('  at the registered value xi / a is about 1, short of 74.6 by 75 in length and 5600 in action.')


if __name__ == '__main__':
    reading_a(); reading_b()
