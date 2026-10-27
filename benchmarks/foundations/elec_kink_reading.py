"""The twist kink as an electron candidate, read on the registered chain (executor, 2026-10-27). Closed forms only.
The registry already holds the kink: a winding on a strand IS a 2 pi kink of the orientation angle (FND-STRAND-002's
transported kink, FND-181's force on a winding, FND-182's kink width w), with the on-site orientation potential V_0
as closure gap 2 (FND-186), sourced by the surface-contact grant (FND-184) and unpriced (STRAND-MASS-SCALE refused:
A_c in joules, sigma in metres, the crossing density). The chain identities (STRAND-MASS-SCALE results): per node
kt = T0 r^2 / (2a) (rod route, r = d_c / 2), w^2 = kt / V_0, and the registered COASTING regime w in [0.8, 2.8]
(FND-STRAND-002 / FND-KIN-002: free transport needs w >= 0.8, charge must move). A sine-Gordon kink with stiffness
kappa (J m) and well V (J/m) has rest energy E = 8 sqrt(kappa V) = 8 kt / w per node and gap omega = c / (w a), so its
action E / omega = 8 kappa / c with no free parameter (the soliton constraint). Read for the single strand, the
registered pair (kappa_pair = T0 d0^2 / 2, consult reading A) and bundles scaled as (n / 2)^2 from the pair."""
import math
HBAR = 1.054571817e-34; C = 2.99792458e8; ME = 9.1093837015e-31; EV = 1.602176634e-19
T0, A, DC = 434.0, 6.0e-17, 1.87e-19
ME2 = ME * C * C
kt_strand = T0 * (DC / 2) ** 2 / (2 * A)
kappa_pair = 0.5 * T0 * (0.43 * 0.6272 * A) ** 2; kt_pair = kappa_pair / A
print(f'per-node twist stiffness: single strand kt = {kt_strand:.3e} J ({kt_strand / EV:.3e} eV); pair kt = {kt_pair:.3e} J ({kt_pair / EV / 1e3:.1f} keV); T0 a = {T0 * A / EV / 1e3:.0f} keV')
for name, kt in (('single strand', kt_strand), ('two-strand pair', kt_pair)):
    for w in (0.8, 2.8):
        V0 = kt / w ** 2; E = 8 * kt / w
        print(f'  {name:16s} coasting w = {w}: V_0 = {V0 / EV:.3e} eV per node, kink E = {E / EV:.3e} eV = {E / ME2:.2e} m_e c^2; E/omega = 8 kappa/c = {8 * kt * A / C:.2e} J s = hbar / {HBAR / (8 * kt * A / C):.1e}')
    w_e = 8 * kt / ME2
    print(f'  {name:16s} kink of mass m_e needs w = {w_e:.2e} a (V_0 = {kt / w_e ** 2 / EV / 1e3:.2e} keV per node, f = V_0 / (T0 a / 2) = {kt / w_e ** 2 / (T0 * A / 2):.2e})')
print('bundles of n strands at the pair packing (kappa (n/2)^2 kappa_pair), coasting regime:')
for w in (0.8, 2.8):
    n = 2 * math.sqrt(ME2 * w / (8 * kt_pair))
    print(f'  w = {w}: a kink of mass m_e needs n = {n:.1f} strands; its action 8 kappa / c = hbar / {HBAR / (8 * (n / 2) ** 2 * kappa_pair / C):.1e}')
print('NODE-STANDOFF (registered): the coasting regime implies f ~ 1e-7 to 1e-4 (V_0 far below T0 a); a kink of electron mass on the pair needs f of order 1e4 and is pinned.')
