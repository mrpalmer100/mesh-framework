# GRANT-CANDIDATE-SWEEP -- the loosened thread: a weak lock on the rope's azimuth, priced for the author's desk
# (DRAFT 2026-10-27; a candidate, not a grant; the decision is reserved to the author; the author's standing
# instruction: pursue it to the extent it leads to the proper cadence, and if it does not, retract and keep on record)

## Why a candidate exists
The clean-room study (docs/CLEAN_ROOM_ELECTRON_STUDY.md) reduced the mechanical electron to one absence in the
registry: a beat, a mode of the medium at the zitterbewegung frequency Omega = 2 m_e c^2 / hbar with the twist's
far field relaxed beyond c / Omega. The beat census (analysis/BEAT_CENSUS_reading.md) found nothing registered within
thirty-fold of it. The census also recorded an objection: a gap for the rope's azimuth would gap the U(1) that is
electromagnetism. That objection is WRONG on the registry as it stands, and finding so is what makes this candidate
possible: GRV-102 and EM-RECON-025 resolved the "torsion dynamics = light" clause of GRV-020 as an allocation that
over-reached; light is the collective transverse Goldstone pair (two polarizations), not the azimuth wave (one).
Charge remains the azimuth's winding; the photon does not live on the azimuth. The azimuth may therefore be gapped.
Gaede's picture, that a rope's threads can loosen and sweep around their partner, is this degree of freedom; the
registry's name for its lock is f (NODE-STANDOFF: V_0 = f T0 a / 2 per node), which JUNCTION-LOCK found to be zero
at the registered level and which the face-holding tie would put at about 3.5. The candidate is a THIRD value of f,
small, with its consequences priced before anyone chooses it.

## The candidate, stated in full
The rope's internal azimuth Phi (GRV-020's Goldstone, whose winding is charge) is weakly locked to its surroundings
by a periodic potential V(Phi) = V_0 (1 - cos Phi) per node, V_0 = f T0 a / 2 with f much smaller than one, so that:
  (i)   the azimuth has a gap, Omega^2 = V'' / I with V'' = V_0 / a per length and I = kappa / c^2 the azimuth's
        inertia per length (an IDENTITY for the tension-geometric stiffness kappa = T0 sum rho^2, since mu = T0 / c^2:
        the inertia and the stiffness are the same sum);
  (ii)  a winding of the azimuth is a sine-Gordon kink of width l = sqrt(kappa / V'') = c / Omega, which is the
        screening length by identity, with rest energy E = 8 sqrt(kappa V'') and action E / Omega = 8 kappa / c with
        no free amplitude (A5 of the study);
  (iii) FND-182's charge-creation identity E_c = (4 pi / 5) V_0 / (e a) applies to it unchanged.
Nothing else is granted: no new field, no new constant beyond f, and f is not chosen here.

## What it is and is not
It is a weak on-site potential for a registered angle, of the kind the registry has priced twice (NODE-STANDOFF's
f-table; STRAND-MASS-SCALE's chain) and once found to be zero (JUNCTION-LOCK, at the registered contact). It is not a
derivation of f: JUNCTION-LOCK's f = 0 was by construction (a point node with a harmonic bond has no azimuth), so a
nonzero f needs a node that is not a point, which is the "tie holds the face" extension FND-184 named and the
author did not grant. SWEEP is that extension with the tie's strength left to be measured rather than priced at 3.5.

## The cheap test, run (T-1; benchmarks/foundations/sweep_t1.py; log analysis/SWEEP_T1.log)
Impose the electron on (i) to (iii): E = m_e c^2 and 8 kappa / c = hbar / 2 (so that the kink's action is the spin and
Omega is the zitter frequency). Everything is then fixed:
    kappa = hbar c / 16 = 1.98e-27 J m         the one input; the pair has 5.7e-32, the FND-188 rope 1.3e-22
    Omega = 1.553e21 rad/s                      the beat, by construction
    l = c / Omega = 1.93e-13 m = 3,218 a        the kink coasts (far above the 2.8 a regime edge)
    V'' = m_e^2 c^3 / 4 hbar = 5.3e-2 J/m;  V_0 = 19.8 eV per node;  f = 2.4e-4
    E_c = (4 pi / 5) V'' / e = 8.3e17 V/m = (pi / 5) E_Schwinger   914 times the laser record, 0.63 of Schwinger
    strands for kappa: 50 at disk packing (R = 4.3e-16 m), 373 at the pair's packing
Two of these are identities that hold for ANY kappa once the electron is imposed, and they are the content:
the kink width equals the screening length c / Omega, and the charge-creation field is pi / 5 of the Schwinger
field. The second was not put in. FND-182's identity came from a strain-gradient force law on a winding, with no
hbar in it; the Schwinger field is QED's pair-creation threshold. That a weak azimuthal lock tuned only to the
electron's mass and spin lands its charge-creation field at 0.63 of QED's threshold is the kind of coincidence
the house records and does not read; it is recorded here, and it is the first thing a falsifier would test.

## The price (on the face)
P1. f is calibrated by m_e, as the M-point's a and T0 are (FND-MATTER-044). The candidate buys the structure (a gap
    for the azimuth with the kink as the charge carrier), not the number. The beat census says no registered
    mechanism produces f = 2.4e-4; it is a node property the registry does not hold.
P2. kappa = hbar c / 16 is the stiffness wall by another name: the electron's rope must have about 50 strands at
    disk packing or 370 at the pair's. The registered pair has neither. The candidate does not remove the wall; it
    converts "kappa / hbar c" into a strand count for the electron's rope, which is a different count from
    FND-188's.
P3. INCOMPATIBLE WITH FND-188 AS STATED. GRANT-HBAR-ROPE puts the quantum of action in the coherent transverse
    motion of a 12,882-strand rope; SWEEP puts it in the twist kink of a 50- to 370-strand rope. Both cannot be
    the electron. If SWEEP is adopted, the electron's n_rs falls outside FND-188's factor-3 tripwire by two orders,
    and FND-188 supersedes by its own C1, kept on record (the author's instruction). The HBAR-005 patch would then
    be the kink's length (3,218 a) rather than a rope's radius.
P4. THE CORE SIZE. The kink's transverse core is the rope's radius, 4e-16 m at disk packing. The electron's
    compositeness bounds (from g - 2 and high-energy scattering) sit near 1e-18 to 1e-19 m. The candidate survives
    only if what a probe scatters from is the winding's far field (a scalar topological charge sourced at the
    core) and not the rope's material cross-section; that is design item (i) of the study, unsolved.
P5. The kink carries no angular momentum of its own; the spin hbar / 2 enters as the kink's ACTION 8 kappa / c,
    not as a mechanical J. Whether that action is a spin is C1 of the study (the frame locking), unsolved.

## What it buys (if granted, each a registered consequence)
B1. The beat: the medium has a mode at the zitter frequency, A4 of the study, and D6 (quantization as resonance)
    becomes a registered question rather than an absence.
B2. The electron as a Compton-length coasting kink of the azimuth on a rope of order 50 to 370 strands, with
    E = m_e c^2, action hbar / 2, size c / Omega, pointlike winding core, topological charge, pair threshold 2 m_e c^2.
B3. A PREDICTION with no free parameter: vacuum charge creation at E_c = (pi / 5) E_Schwinger = 8.3e17 V/m, below
    QED's threshold by 0.63 and above the laser record by 900. FND-182 moves from T4 back to a live discriminator
    with a single number instead of a three-order window.
B4. Gap 2 (V_0) closes with a value; gap 3 (the internal dimension) is NOT touched, because the azimuth is the
    registered angle and light was never on it.

## Falsifiers (any one kills the candidate as stated)
F1. If light is the azimuth wave after all (a reversal of EM-RECON-025's resolution), the gap is a photon mass of
    m_e c^2 and the candidate is dead on arrival.
F2. E_c: observation of vacuum charge creation at any field below 8.3e17 V/m without a QED mechanism, or its
    absence at fields above 8.3e17 V/m within the mechanism's window, kills it; the laser record (9.1e14, no
    creation) is consistent and is the floor.
F3. The core: a registered electron structure computation on a 50-strand rope that puts a material cross-section
    of 4e-16 m in the scattering amplitude kills it (P4).
F4. The lock: any registered determination of the node's azimuthal lock (a derivation of the tie, a dynamical pin)
    that lands outside a factor 3 of V_0 = 20 eV per node kills it by name (the FND-121 tripwire form).
F5. The count: an independent determination of the electron rope's strand count outside [50 / 3, 373 x 3] kills it.

## Scope discipline
The granted f may not be used to confront hbar or m_e (it was set by them; clean room, as FND-188 C3). It MAY be used
to confront E_c (B3), the kink's size, the gap's consequences for the twist spectrum, and the generation spectrum
(the kink's excited states, C2 of the study). Every quantity carrying it takes the SWEEP rider.

## Retirement clause (the author's instruction, written in)
If the candidate, adopted, does not lead to the cadence (the beat with its consequences B1 to B3 surviving one
locked confrontation), it is retracted by name on the same release, every SWEEP-rider quantity reverts, FND-188
is reinstated if it was superseded under P3, and the sheet stays on the record with the reason.

## Cheap tests still runnable before any adoption (sandbox, no machine time)
T-2. The frame locking (C1): on the dynamics instrument, whether a 2 pi azimuth kink on a framed closed rope
     carries a half turn of the Calugareanu frame per circuit (FND-STRAND-003's ledger); known-answer credential
     on the static twisted ring. Decides whether the kink's action is a spin.
T-3. The far field of the kink (P4): the azimuthal winding's field outside the rope under the registered 1/r
     conditioning (GRV-005) with the gap, i.e. whether the screened winding presents a point charge at distances
     between 4e-16 m and 2e-13 m. Closed forms.
T-4. The generation ratio (C2), DECIDED HERE at zero cost: a sine-Gordon kink has no internal bound state (its
     only discrete mode is translation; the breather is a neutral kink-antikink pair), and any periodic lock's kink
     has its internal modes BELOW the continuum edge, so no excitation of the kink sector exceeds E_0 + hbar Omega =
     3 E_0 (E_0 = hbar Omega / 2). The muon at 206.8 E_0 cannot be an excited electron kink. Dirac's membrane test
     fails for the excited-state reading, as it did for Dirac. The alternative the chain allows: generations as
     three LOCK STRENGTHS on one rope, f = 2.4e-4, 10.4 (= 206.8^2 f_e) and 2950, each with the spin unchanged
     (8 kappa / c is the rope's, not the lock's), each with its kink width at its own Compton scale, and each with
     E_c = (pi / 5) of its own Schwinger field. That is a restatement with three inputs, not a prediction, unless
     the three f follow from a registered node structure; it is recorded so that nobody mistakes B2 for a lepton
     spectrum. B2 holds for the electron alone.

## Decision line (the author's)
Adopt / decline / hold pending T-2 and T-3. The executor's recommendation: HOLD and run T-2 and T-3 first (T-4 is
decided: no lepton spectrum from one lock). T-3 is the one that can kill the candidate on an experimental bound
(the electron's size) without any registration, and T-2 is the one that decides whether the candidate's hbar / 2
is a spin or only an action. If both survive, the candidate is worth adopting for B3's number alone: a charge-
creation field at pi / 5 of Schwinger is the first zero-parameter prediction the electron sector has produced.

## T-2 RUN (2026-10-27, sandbox; benchmarks/foundations/sweep_t2.py; log analysis/SWEEP_T2.log)
On the registered Calugareanu machinery (strand_calugareanu.twist_from_frames; the exact polygon writhe), a rope
of two strands at separation d around a circle of radius R, M = 2400 nodes, three thin-rope ratios d / R = 0.3,
0.1, 0.03:
  FULL TWIST (the 2 pi kink; two closed strands): Lk(X, Y) = 1.0000 by the Gauss linking integral at every d / R;
    each strand's ledger with the partner-pointing frame Tw + Wr = 1.0000 (Tw 1.0000, Wr 0.0000 in the thin limit).
    The frame returns after ONE circuit. This is the registered unit charge (GG-006).
  HALF TWIST (the pi kink; the strands exchange; one closed strand of two circuits, the (2, 1) torus curve): the
    frame is reversed after one circuit (n . n0 = -1.000) and returns after two (+1.000): the double cover is real.
    The doubled strand's ledger: Tw = 1.000, Wr = 1.000, SELF-LINKING SL = Tw + Wr = 2.0000 at every d / R.
READ. C1 FAILS at the registered charge accounting. The state whose frame needs two circuits to return carries
self-linking 2, twice the integer of the unit-charge state; the unit-charge state (Lk = 1) returns its frame every
circuit and has no double cover. Spin 1/2 by the belt and charge e by linking are carried by DIFFERENT states of
the rope, and no registered rule assigns a charge to the half-twist state at all (FND-184's pre-adoption read:
"a half material twist is twist, not linking"). So the hbar / 2 that SWEEP's kink carries is an action and not a
belt-trick spin of the charged state; P5 stands as a price, not a hope; g = 2 and spin 1/2 are not one fact here.
A structural consequence for the record, not scored: FND-184's lock has period pi, so a 2 pi kink is two pi kinks,
which in a pi-periodic potential do not bind; the unit charge on such a rope would split into two separated
half-kinks, each a local exchange of the strands (the fractionalization of polyacetylene's soliton), unless a
registered interaction binds them. Nothing registered does. That is a second debt on B2, named here.
What T-2 leaves standing: B1 (the beat) and B3 (E_c = pi / 5 of Schwinger) do not depend on C1 and are untouched.
B2 (the kink as the electron) now owes the spin AND the binding of its halves. T-3 (the core as a point charge)
still decides whether B2 survives at all.

## B1 MADE CONCRETE (2026-10-27, sandbox; benchmarks/foundations/sweep_b1.py; log analysis/SWEEP_B1.log)
The beat, on the locked azimuth of a rope held by its nodes (shape frozen, which is the physical case for a kink
on a rope in the weave; the dynamics instrument gained the lock term, ring_wave_dynamics.make_lagrangian(lock=),
0 by default, and with the shape frozen its twist sector is exactly the sine-Gordon equation, integrated here by
Stoermer-Verlet at M = 1600). Units kappa = c = 1, V'' = 100, so Omega = 10 and l = c / Omega = 0.1.
  (1) The gap is real and the dispersion is the massive one: omega(n)^2 = Omega^2 + omega_d(n)^2 to 1e-7 at n = 0, 5,
      20 and 1e-5 at n = 80; the azimuth's lowest mode beats at Omega with no wavelength, and every mode above it
      is the free wave with the beat added in quadrature.
  (2) The static 2 pi kink: E = 79.9983 against 8 sqrt(kappa V'') = 80 (2e-5, the ring's finite size), width from
      the maximal slope 0.10002 against c / Omega = 0.1; integrated for fifty beats it does not move and its energy
      holds to 7e-14. The kink's width IS the screening length, as the identity said.
  (3) The moving kink at v = 0.3, 0.6, 0.9: energy gamma E_0 to 2e-6, 1e-5, 9e-5; width l / gamma to 1e-4; it travels
      at the set speed to 1e-3; energy conserved to 1e-9 or better. The locked twist sector is Lorentz covariant on
      the instrument, so a kink has a rest energy, a Compton-scale rest width, and the kinematics of a particle.
B1 is therefore not an assertion: a weak lock on the azimuth makes the medium beat, and the winding on that
medium is a relativistic soliton of rest energy 8 sqrt(kappa V'') and width c / Omega. What B1 does not settle is
unchanged: the value of the lock (P1), the stiffness (P2), the spin (T-2, failed), the binding of the halves under
a pi-periodic lock (T-2's debt), and the core (T-3, not yet run).

## T-3 RUN (2026-10-27, sandbox; benchmarks/foundations/sweep_t3.py; log analysis/SWEEP_T3.log)
The kink's charge is its winding density sech(s / l) along the rope, carried on strands at radius rho across it;
a probe sees F(q) = sech(pi q l / 2) J0(q rho).
  (a) ALONG the rope: <s^2>^(1/2) = 1.75e-13 m against the Dirac electron's own Darwin spread 3.34e-13 m (the
      ratio of mean squares 0.27); F_par = 0.755 at q = m_e c / hbar and 0.997 at a tenth of it. A Compton-length
      kink has the charge spread QED already attributes to the electron. Not a kill; if anything the right order.
  (b) ACROSS the rope: e+ e- -> e+ e- tests of QED at the 1 percent level bound a transverse charge radius to
      1.3e-18 m (PETRA class, 30 GeV/c) and 4e-19 m (LEP2 class, 100 GeV/c). The registered pair has
      rho = d0 / 2 = 8.1e-18 m (21 times over; F_perp = -0.39 at 100 GeV/c); the 50-strand bundle 4.2e-16 m
      (1,100 times over); the 373-strand bundle 1.5e-15 m (3,800 times over).
READ. B2 is KILLED across the rope on an experimental bound, for every strand count including the registered
pair: a charge carried on strands at the registered spacing a = 6.0e-17 m is not pointlike to e+ e- scattering by
one to three orders of magnitude. This is not specific to SWEEP: it is a statement about ANY mesh electron whose
charge sits on strands at the registered standoff, and it is the form-factor bill FND-188's P1 named, presented
now with a number. The one loophole is a registered rule that a winding's field is sourced on the rope's
centreline with no transverse multipoles (the probe coupling to the topological charge and not to where the
strands are); the EM dictionary (EM-015 to EM-022) is silent on it, and nothing registered supplies it. That
loophole is itself a grant, and a larger one than SWEEP.
What stands: B1 (the beat, made concrete) and B3 (E_c at pi / 5 of Schwinger) do not depend on the transverse
structure of the charge; they are properties of the lock and the kink's length, not its cross-section.

## Decision line, revised after T-2 and T-3
The candidate as a MODEL OF THE ELECTRON (B2) is dead on this registry: no spin (T-2), unbound halves under a
pi-periodic lock (T-2), and a transverse charge radius one to three orders above the e+ e- bound (T-3). The
candidate as a MECHANISM (B1, B3) survives: a weak lock makes the medium beat, the winding on it is a
relativistic soliton, and the lock that reproduces the electron's mass and action puts the vacuum's
charge-creation field at pi / 5 of Schwinger. The executor's recommendation: DO NOT ADOPT as the electron; keep
the sheet on record with T-1 to T-3 as the reason, per the author's instruction; the mechanism (a weak azimuthal
lock) stays priced for any later object that is not a rope of registered strands.

## T-3 CORRECTED (2026-10-27, later; analysis/ROAD1_centreline_reading.md)
T-3 scored the winding as a coupling source (charge at the strands, Born form factor J0(q rho)). EM-015 registers the
winding as a CONSTRAINT source and GRV-020 / ELEC-089 define its azimuth about the common centreline; the exterior
field of a winding has no isotropic size correction, and a 2 pi kink averages every anisotropic one to zero
(road1_check.py: the orientation-averaged field equals the point-winding field to 2e-15 outside the strands). The
transverse form factor of the charge is 1; the bound of T-3 is a bound on the MASS form factor. The T-3 kill of B2
is lifted pending the author's word on the FND-189 rider. T-2's findings stand: B2 still owes the spin and the
binding of its halves. The decision line of "T-3 RUN" is therefore reopened: not adopted as the electron on T-2's
grounds alone, with the size objection withdrawn.
