# The beat census: what in the registered medium oscillates near 1.55e21 rad/s (executor reading, 2026-10-27)

Instrument `benchmarks/foundations/beat_census.py`; log `analysis/beat_census.log`. The clean-room study
(docs/CLEAN_ROOM_ELECTRON_STUDY.md, A4) needs the medium to have a mode at the zitterbewegung frequency
Omega = 2 m_e c^2 / hbar = 1.55e21 rad/s, a length c / Omega = lambda-bar_C / 2 = 3,200 spacings. The rule of the
census: a frequency counts only if a registered mode oscillates at it; a combination of constants that lands is not
a mode (HBAR-005 already audited the combinations and found no natural exponent).

## 1. Every registered mode, at the M-point card
    mode                                                   omega [rad/s]   omega / Omega
    transverse lattice cutoff 2c/a                         1.0e25          6.4e3
    node bond c/a (JUNCTION-LOCK: harmonic point junction) 5.0e24          3.2e3
    longitudinal cutoff c_L/a, k/T0 = 2 (1.9e8)            7.1e24 (6.9e28) 4.6e3 (4.4e7)
    torsion wave (GRV-020 Goldstone; JUNCTION-LOCK f = 0)  0               no gap
    torsional segment mode pi v_t / a, v_t = 1.05 c        1.7e25          1.1e4   (a segment of 10,600 a would do it)
    twist gap under the junction tie, f = 3.5              4.2e27          2.7e6
    two-strand ring-wave c / R*                            2.6e25          1.7e4
    granted rope ring mode c / R, R = 113 a (FND-188)      4.4e22          28
    HBAR-005 patch, c / (74.6 w)                           7.0e22          45
    fine-level rotating wave, c / a_f at the grant's a_f   1.4e30          8.7e8
    pair standoff mode sqrt(A_c / sigma0^2 mu)             unpriced (A_c)  lands at Omega only for A_c = 3.8e-8 T0,
                                                                           2e7 below the registered bound A_c > 0.40 T0 a
Within 1.5 orders of Omega: one entry, the granted rope's ring mode, at 28 times the target, and it is a rider of
FND-188 (a count set by hbar) rather than a registered oscillation of anything.

## 2. Reading
Nothing registered beats at the electron. Every intrinsic mode of the strand and the node sits three to nine
orders ABOVE Omega (they are lattice-scale); the only mode the registry can gap, the twist under the junction tie,
gaps six orders too high; the one mode whose frequency is unpriced, the pair's standoff, would need a contact
amplitude twenty million times below the registered bound. The nearest things are not modes but lengths that
already carry hbar (the granted rope, the HBAR-005 patch), and they miss by 30 to 45.

## 3. Why this is not a matter of looking harder
A beat for the twist is a gap for the twist, and the twist's shift symmetry is the one continuous internal
symmetry the medium has (FND-185 GAUGE-INVENTORY: real dimension 1, SO(2) on the azimuth, already spent on
electromagnetism: winding is charge, torsion is light). Gapping it would give the photon a mass. The way every
known theory avoids that (the Standard Model's Higgs breaking SU(2) x U(1) to the U(1) of light) needs MORE than one
internal angle, so that one combination is gapped and another stays free. FND-185 counted the medium's internal
dimension at 1 and FND-186 filed the shortfall as closure gap 3. So "what beats at 1.55e21" is, on this registry,
the same question as gap 3: a second internal angle on the strand with a restoring force, which no registered
energy holds (FND-185 lists the strand's own-axis azimuth as "absent from E"). The electron's mass in this medium
is the mechanical form of the Higgs question, and the census says the registry does not yet contain the field
that answers it. That is a grant-class item: a second angle, its energy, and a falsifier stated first.
