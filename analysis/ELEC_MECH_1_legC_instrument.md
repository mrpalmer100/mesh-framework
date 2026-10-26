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

## 5. The scans, and the shape-independence of g = 2 in the travelling-twist class

kappa_tw = 0.1, J = pi (the fold regime; analysis/elec_rope_wave_scan_k01.log): g = 0.76, 0.79, 0.95, 1.05 at beta_p =
0.25, 0.5, 0.75, 1 (flat seed; E 6.71, 6.76, 6.88, 7.00). kappa_tw = 1, J = pi, with the angular-momentum vector
pinned to the axis (analysis/elec_rope_wave_scan_k1.log; the first run let a loop meet J by tilting 30 degrees, a
bookkeeping hole closed the same day): beta_p = 0.5 a rotating intermediate state, g = 1.43 to 1.47 (E 10.48, the
flux 35 to 37 percent of J); beta_p = 0.75 and 1 STATIC planar loops, g = 2.001 to 2.004 (E 11.12 and 12.58),
E_t = E_w to 0.1 percent, from both seeds, with DIFFERENT shapes at the same energy (R_end 0.86 and 1.10; 0.77 and
1.47): to carry a J below the ring's natural 2 pi kappa the loop adds length without area (J_flux proportional to
A / L^2), and the energy does not care which way.

The reason, which the record states as the class's theorem rather than the ring's property: for ANY static closed
loop with its twist travelling at beta_p c, mu = q beta_p A / L (the current q beta_p / L around the enclosed area)
and J = 2 beta_p A E_w / L (the flux eps_w beta_p around the same area), so g = (mu / J)(2 E / q) = E / E_w; and the
scale virial (E_t proportional to L, E_w proportional to 1 / L, the two equal at the minimum over scale) gives
E = 2 E_w for every shape. g = 2 is shape-independent in this class and depends on no parameter; what the shape
and kappa_tw decide is the energy and whether the state is static or must also rotate (the intermediate regime
at beta_p = 0.5, where the loop carries part of J by rotation and g sits between 1 and 2).

Records: analysis/elec_rope_wave_naturalJ.json, analysis/elec_rope_rotator_R1_k05.json, analysis/elec_rope_wave_scan_k1.json.

## 6. The scale wall is the registry's hbar wall (added 2026-10-25)
M7b's angular momentum J = 2 pi kappa / c with the registered torsional stiffness of order T w^2 is HBAR-003's strand
action quantum S_1 = pi T w^2 / 2 c: the same 3549-fold short of hbar / 2 that the HBAR series mapped, and the
tension ladder (A7) on top. The Q3 table for M7b should cite HBAR-003 and FND-183 (ACTION-BRIDGE) for the kappa
half of kappa / T = lambda-bar_C^2 rather than restate it: the electron class that gets g = 2 by mechanics meets
the two walls the registry has already named, in one object.


## 7. Corrections of record (2026-10-26, after the lab's reviews of ELEC-KAPPA-1 and RING-WAVE-ANOMALY-R)
Three statements above are narrower than they read, and the lab's reviewers caught each one. They are corrected
here rather than edited in place, so the record shows what was claimed and when it was narrowed.

(a) J = 2 pi kappa / c is a RING result, not a class result. Sections 1, 4 and 6 write the angular momentum of the
travelling-twist class as 2 pi kappa / c "independent of R". That holds for the circle, where the wave flux
kappa Phi' Phi-dot / c with Phi' = 2 pi / L and the moment arm R give 2 pi kappa (beta / c)(2 A / L) = 2 pi kappa / c
at A = pi R^2, L = 2 pi R. For a general static loop at beta_p = 1 the flux angular momentum is
J_flux = eps_w (2 A) / c with eps_w = kappa (2 pi / L)^2, that is J = (2 pi kappa / c) (4 pi A / L^2), and the
isoperimetric factor 4 pi A / L^2 is at most 1, equal to 1 only for the circle (section 5 states the proportionality
to A / L^2, and the kappa_tw = 1 rungs at beta_p = 0.75 and 1 carried J = pi below the ring's 2 pi kappa by adding
length without area). The ring is the member that carries the MOST angular momentum per unit winding. So the class quantizes J by the winding ONLY through the ring; a non-circular member
carries less at the same winding. The statement in section 4 ("J = 2 pi kappa / c is quantized by the winding,
which is R3 answered by topology times a rope constant") is therefore the ring's property, and the credit it
claims for the class is withdrawn to that extent. ELEC-KAPPA-1's confrontation of J_1 = 2 pi kappa / c with
hbar / 2 was built on the class reading and would have scored the ring alone (the skeptical reviewer's point).

(b) Reading (ii) of ELEC-KAPPA-1 D1 (the strands' own torsion "following the pair's twist", 2 C) does not by itself
establish that the pair's twist propagates at c. EM-RECON-012 registers torsion waves at c on a rope with the
registered rigidity; what travels at c in the ring-wave is the Goldstone phase of GRV-020, whose speed is set by
kappa and the rope's twist inertia together, and the instrument here fixed beta_p by hand (section 5's beta_p is
a parameter, not a solved speed). Nothing in this record derives beta_p = 1 for the registered rope. The class
reaches g = 2 at beta_p = 1; whether the registered rope's twist travels at that speed is open and is a question
about the twist inertia, which the card does not carry.

(c) The field / twist split is SILENT in the registry. The RING-WAVE-ANOMALY reading (analysis/RING_WAVE_ANOMALY_
reading.md) treated the magnetic self-energy U_M as additive to the twist energy and obtained g - 2 = 4 alpha / pi.
The lab's worker read EM-015 and EM-018 for RING-WAVE-ANOMALY-R and found them NEUTRAL on whether the twist
energy already contains the field energy; the dictionary claims (EM-017 to EM-022) describe the twist as the
mechanical form of the field without stating the energy accounting. So 4 alpha / pi is the additive reading's
number, conditional, and the registry owes the split before any O(alpha) statement about this class is more
than that. The reading's face already says "conditional"; this entry records that the condition is unmet by
citation, not merely unexamined.

(d) What stands unchanged: g = E / E_wave = 2 by the scale virial for ANY static closed loop whose twist travels
at beta_p c with the charge riding the transverse material motion (section 5's theorem; two seeds, different
shapes, 2.001 to 2.004); the 9 percent energy price over the co-moving fold at equal kappa and J; the scale wall
kappa / T = lambda-bar_C^2 (section 6's identification with HBAR-003 and FND-183 is about the ring's kappa and
is unaffected by (a) in that the ring is the member that carries the most J per winding).
