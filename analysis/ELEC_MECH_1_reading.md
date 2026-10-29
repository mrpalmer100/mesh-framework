# The electron mechanism classes on the second-moment screen (the executor's reading, 2026-10-25)

Status: a reading, not a commission. ELEC-MECH-1 was drafted as a commission and withdrawn by the lab after one
review round (2026-10-25); both reviewers showed that every class's outcome was a closed form, on the record, or
scale-free from a computed cell, so no verdict was open before the lock. They were right. The content stands as the
executor's reading and is filed here; the charter is parked (analysis/queue/parked/) with this reason.

## The screen
For any stationary configuration in its rest frame, g = (mu / J)(2 m / q) = <omega_q r^2>_q / <omega_E r^2>_E, the
ratio of the charge's and the energy's angular-velocity-weighted second moments (ELEC-G-2's D1 is the rigid case).

## The classes and their numbers
  M1   Rigid closed rope, twist co-moving (E2b): g = 0.97, 0.91, 0.95 at kappa_tw = 0.01, 0.1, 1. FAILS 2.
  M2   Rigid fold, charge locus by rule: 1/gamma 1/2, uniform 2/3, proportional to gamma 1, edge 2 (closed forms,
       verified; the edge row needs ends). FAILS 2 for every registered locus.
  M3   The alpha terminus (ELEC-102): 1.82 (edge reading), 1.11 (profile-weighted). FAILS 2.
  M4   Open rope with end charge: g = 2 exactly, at the price of ENDS, which are not registered objects.
  M5   Lightlike pulse carrying all the energy, no tension counted: g = 1. FAILS 2.
  M6   The texture soliton (ELEC-074) in rigid rotation: the ELEC-102 computation on its profile; dead as the
       electron by ELEC-075 regardless.
  M7b  Closed rope with its twist travelling at c (analysis/ELEC_MECH_1_legC_instrument.md): g = E / E_wave and
       the scale virial gives E = 2 E_wave, so g = 2 for any shape, nothing tuned (2.001 to 2.004 by free
       minimization, two seeds, different shapes). REACHES 2. Prices: 9 percent above M1 at equal kappa and J
       (stability); J = 2 pi kappa / c, which with the registered kappa is HBAR-003's S_1 (the hbar wall), and
       T = m_e^2 c^3 / 4 pi hbar against the tension ladder (A7). Credit: J quantized by the winding (R3).
  M8   Intrinsic azimuthal spin of the strand pair: a correction of order (d0 / R)^2 to M7's moments in the
       rigid-pair limit; not separately computed.
Completeness: a direction of escape the list does not cover is the spinor route (g = 2 as a non-classical moment
ratio), for which the registry has no mechanics; named, open.

## What follows (revised 2026-10-26)
ELEC-KAPPA-1 was withdrawn by the lab: J_1 = 2 pi kappa / c is the RING's angular momentum, not the class's (a
non-circular member carries less at the same winding; analysis/ELEC_MECH_1_legC_instrument.md section 7a), and
its confrontation with hbar / 2 is HBAR-003's wall restated (Leg C section 6). The M7b row's "J = 2 pi kappa / c"
above is to be read with that restriction, and its "credit: J quantized by the winding (R3)" is the ring's
property only. The class's open question with an unknown answer is its STABILITY (the Director's
RING-WAVE-STABILITY): whether the travelling-twist state is a protected stationary point or decays to the
co-moving fold 9 percent below it. The instrument for that is credentialed on known answers in
benchmarks/foundations/ring_wave_stability.py (analysis/RING_WAVE_STABILITY_leg0.md) without touching the
ring-wave cell.
