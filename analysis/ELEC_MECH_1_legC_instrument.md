# ELEC-MECH-1 Leg C instrument: the travelling twist on the closed rope (executor, sandbox, 2026-10-25)

Instrument: `benchmarks/foundations/elec_rope_wave.py` (queue ae7a724 and after), built on `elec_rotator.py` /
`elec_rope_rotator.py`. Records: `analysis/elec_rope_wave_naturalJ.json`, `analysis/elec_rope_rotator_R1_k05.json`,
the scan log appended below when it completes. Dimensionless units: T = 1, c = 1.

## 1. The closed form that motivated it (registered pieces only)
A static closed rope of radius R, tension T, carrying its one unit of twist as a torsion wave travelling at c
(EM-RECON-012: torsion waves are light): energy E = 2 pi R T + 2 pi kappa / R (the Goldstone energy kappa Phi'^2 for
the wave at its own speed, Phi' = 1 / R), minimum at R* = sqrt(kappa / T) where E_tension = E_wave (a virial);
angular momentum from the wave's flux (EM-019) J = 2 pi kappa / c, independent of R; moment from the transported
winding (EM-008) mu = q c R / 2. Hence g = (mu / J)(2 m / q) = 2 exactly, nothing tuned: the charge circulates at c
while half the mass sits still in the tension. The same arithmetic with the tension excluded from m gives 1 (the
zitterbewegung pulse); E2 record section 5's M5 row was that case and was underspecified.

## 2. Credential (closed forms through the production functions, M = 48)
E on the ring to 2.5e-7 at R*, J and mu to the 48-gon's chord factor (1.4e-3, inside the stated tolerance
2 (pi / M)^2), E_t / E_w = 1 at R*, g = 2 at R* and 1.25 / 4.99 at R* / 2 and 2 R* (the ratio E_t / E_w + 1, as the
formula says), g = 1 with the tension excluded, time-average independence of the twist shape (a moving Gaussian
pulse and a uniform twist give the same <r^2>_q to 1e-9), and a free minimization at fixed J = 2 pi kappa landing
on R* to 1.3e-3 with g = 1.998. One defect found and fixed on the way: the charge must ride the transverse
material motion only (tangential motion of a string is a reparametrization; counting it as a current inflated g
to 3 on a ring whose rotation about its own axis carries no J).

## 3. Results
(a) Pattern speed scan at kappa_tw = 0.1, J = pi (ring and flat seeds, M = 48): the minimum is the rotating fold
    at every beta_p, with g = 0.76, 0.79, 0.95, 1.05 at beta_p = 0.25, 0.5, 0.75, 1 (flat seed; the ring seed
    reaches the same region, higher by up to 1.8 at beta_p = 0.25 where it lands on the vertical-ring branch).
    Structural reason: the ring-wave carries J = 2 pi kappa whatever its radius, so at fixed J it exists only at
    kappa = J / 2 pi; away from that the shape must rotate to carry J and folds. kappa_tw = 1 rungs: appended below.
(b) At the ring-wave's own J (kappa_tw = 0.5, J = pi, beta_p = 1): both seeds converge to the ring, E = 8.9016
    (closed form 8.8858 plus Coulomb 0.0141), R = 0.7086 (sqrt 0.5 = 0.7071), E_t = E_w to 0.3 percent, the flux
    carrying 99.9 percent of J, cm speed 3e-8, g = 2.0034. The fold seed collapses into the ring in 1018
    iterations: within the travelling-twist class the ring is the minimum.
(c) The co-moving fold at the same kappa_tw = 0.5 and J = pi (E2b's instrument): E = 8.1000, g = 0.916. The
    ring-wave is 9.0 percent ABOVE the co-moving fold at equal kappa and J: the g = 2 state is not the ground
    state of the rope with this twist energy; the travelling wave costs twice the static twist's energy at the
    same Phi' (kinetic = potential) and the fold spends that difference on its larger J-per-energy.

## 4. What this gives the screen
M7 splits: M7a (co-moving twist, E2b): g = 0.91 to 0.97, FAILS-2. M7b (travelling twist at c, the ring-wave):
g = 2 exactly, REACHES-2, at two prices to be written on its face: (i) stability, 9 percent above M7a at equal
kappa and J; (ii) scale, J = hbar / 2 forces kappa = hbar c / 4 pi and m = m_e forces T = m_e^2 c^3 / (4 pi hbar),
so R = sqrt(kappa / T) = lambda-bar_C, and the registered rope's kappa / T is of order its standoff squared
(about 1e-34 m^2) against the 1.5e-25 m^2 required: nine orders (A7 in its sharpest form). One structural credit:
J = 2 pi kappa / c is quantized by the winding, which is R3 (HBAR-003) answered by topology times a rope constant,
for this class alone. Whether (i) is a kill depends on a registered reason for the twist to travel rather than
ride (none registered; the Goldstone equation admits both), which is a Q2 gap to name.

## 5. kappa_tw = 1 scan (appended when it lands)
