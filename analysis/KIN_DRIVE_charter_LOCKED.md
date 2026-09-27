# COMMISSION KIN-DRIVE -- DOES THE REGISTERED STRAIN GRADIENT MOVE A WINDING ALONG ITS STRAND, AND AT WHAT SPEED?
# (CHARTER, LOCKED 2026-09-27 on the author's word ("Lock kin-drive"), before any number was computed)

North Star line (docs/NORTH_STAR.md section 5): serves the "Strength of magnets" row at
the step the terminal price tests named (FND-KIN-001, the kinematics of charge transport),
and the "Weights of atoms" row's 1836 road, which needs charge to move on a strand at all.
A DERIVED force law on a winding would be the first registered statement of how a charge
moves under the mesh's own electric field. Outcome class: structural, with one number (the
force per unit strain gradient) and one speed statement.

## The question

A charge is a localized winding of the screw azimuth: a 2 pi kink in Phi (GG-006; the
registered kink of FND-STRAND-002). The registered electric field along a strand is a
longitudinal strain gradient (EM-018). Does the strain gradient exert a force on the kink,
what is the force, and how does the kink move: pinned, drifting at a steady speed, or
accelerating?

## The candidate mechanism, stated before computing

The derived lock (EM-RECON-012) enters the screw-stretch energy as the cross term
c_L u' Phi' (EM-RECON-023). A kink carries Phi' = 2 pi delta(s - s0), so its lock energy is
2 pi c_L eps(s0), with eps = u' the local strain. A kink therefore has an energy that
depends on WHERE it sits in a strain field, and the force on it is

    F_kink = -d/ds0 [2 pi c_L eps(s0)] = -2 pi c_L eps'(s0):

charge (2 pi of winding) times field (c_L times the strain gradient). This is the mesh's
q E along the strand, and it is built from registered objects only: the lock and EM-018's
reading of E. Nothing is added. The commission tests whether the registered kink actually
obeys it, and what "moves" means for a kink on the registered chain.

## Registered parts list (reads owed at lock marked [R])

  The kink and its chain: FND-STRAND-002's engine (benchmarks/foundations/
    strand_twist_transport.py): the discrete twist chain phi_ddot = kt Lap(phi) - sin(phi),
    on-site potential from the strand's orientation (FND-STRAND-008: every mode has a
    mass; band [1, sqrt(1 + 4 kt)]), kink 4 arctan exp(x/w) with width w = sqrt(kt), wave
    speed c_t = w in the chain's units; total winding conserved to 1e-12 in transport;
    the Peierls-Nabarro cliff (FND-KIN-002 law, seven orders across w = 0.8..2.8). [R]
    the chain's unit conventions and the PN values at w = 2.0 and 2.8.
  The lock: EM-RECON-012 (c_L = lambda gamma tau_0, gradient-order, Derived) as used in
    FND-179; the cross term c_L u' Phi' of EM-RECON-023. [R] the sign convention of the
    cross term (it fixes the direction of the force relative to the strain gradient).
  The field: EM-018 (E is the longitudinal strain gradient); EM-RECON-027 (kappa_0 fixes
    the strain-to-volt normalization; NOT consumed here, the force is reported per unit
    strain gradient in the chain's units).
  Transport discipline: FND-KIN-001 (dissipationless drift is the requirement); FND-KIN-004
    (kink transport costs far less than rigid translation); FND-179 (the bulk cannot spin
    the strand: consistent, since a moving kink advances Phi locally, not globally).
  The torsion speed: FND-MATTER-047 (v_t/c = 1/sqrt5) for converting the chain's c_t to a
    physical ceiling, reported, not used in a bar.

## Protocol (sandbox; derivation plus the registered chain)

D1 (derivation). The force law above, symbolic, from the discrete cross term
    c_L sum_j eps_j (phi_{j+1} - phi_j): the force on site j is c_L (eps_j - eps_{j-1}),
    i.e. a uniform torque F = c_L eps' on the field where the strain gradient is uniform;
    the force on a kink is 2 pi F by integrating over the kink. Also derived: the uniform
    torque tilts the on-site potential, sin(phi) = F has no solution for F > 1, so the
    chain's vacuum ceases to exist above the strain gradient eps'_c = 1/c_L: the mesh's
    breakdown field, recorded as a consequence (compare the corpus's registered Schwinger-
    class threshold, EM-021), not used in a bar.
K1 (the force, measured). On FND-STRAND-002's chain at w = 2.0 and w = 2.8 (the coasting
    regime), a kink from rest under uniform F in {1e-4, 3e-4, 1e-3, 3e-3}; the kink centre
    (winding-weighted) tracked; the initial acceleration a extracted from the first
    parabolic segment; the effective mass M = 2 pi F / a compared with the sine-Gordon
    kink mass of the chain, M_sG = 8/w (energy 8 w over c_t^2 = w^2). Bar: M within 5
    percent of 8/w at the two smallest F, or the force law is NOT what the registered
    chain does (the discrepancy is the finding).
K2 (pinning). The threshold F_th below which the kink does not depin at each w, bracketed
    to a factor 1.5 by bisection; compared with the registered PN barrier (FND-STRAND-002's
    pn_barrier, E_PN) through the depinning estimate for a sinusoidal PN potential of
    amplitude E_PN and period one node: the maximum restoring force is pi E_PN, so the
    kink depins when 2 pi F exceeds it, F_th = E_PN / 2. Bar: within a factor 2 of that
    estimate (the PN potential is not exactly sinusoidal); the number is the record
    either way.
K3 (the speed). Above threshold, the kink's velocity history v(t): does it (a) reach a
    steady drift, (b) accelerate and saturate at c_t = w with the relativistic form
    v(t) = (2 pi F t / M) / sqrt(1 + (2 pi F t / (M w))^2), or (c) something else. Bar for
    (b): the measured v(t) within 3 percent of the form up to v = 0.9 c_t at the smallest
    F above threshold. A steady drift (a) at the registered couplings would need a loss
    the chain does not contain and would be a finding of the first order.
K4 (the disclosure). The chain is FND-STRAND-002's: backbone rigid, no writhe coupling
    (Phase 2b, named there, not built). The force law's consequences beyond the chain
    (writhe, the collective loss route, resistance) are named, not claimed.

## Bars (LOCKED before computing)

B-K1  M = 2 pi F / a within 5 percent of 8/w at the two smallest F, both w.
B-K2  F_th bracketed to a factor 1.5; comparison with E_PN/2 reported (factor-2 bar).
B-K3  v(t) within 3 percent of the relativistic form to 0.9 c_t at the smallest F above
      threshold; the alternative outcomes (a) and (c) rendered as found.
B-K4  Total winding conserved to 1e-9 in every run (the chain's own invariant); a run that
      violates it is REFUSED, not read.

## Verdict forms (LOCKED)

KIN-FORCE-DERIVED:    B-K1 passes: a winding on a strand feels F = 2 pi c_L eps' from the
    registered lock; the mesh has a q E along the strand, built from registered objects.
    FND-KIN-001's "underived" narrows to: the force is derived, the choreography of
    dissipation is not. Registered with K2's threshold and K3's speed statement.
KIN-FORCE-FAILS:      B-K1 fails: the registered chain does not obey the lock's force law;
    the measured M and its F-dependence are the finding; the candidate mechanism is kept
    as a failure.
KIN-PINNED:           K1 passes but K2's threshold exceeds any strain gradient the
    registered EMF can supply at laboratory fields (compared through EM-RECON-027 as a
    display): charges do not move on a strand under ordinary fields; kept as a failure of
    the transport picture with the number.
KIN-ACCELERATES:      K3 (b): no steady drift exists at the registered couplings; a driven
    winding accelerates toward the torsion speed. Registered as the transport law, with
    the consequence named: a steady current needs a loss the registry does not hold (the
    collective route, GRV-118 obligation 3), the same gap as FND-179 B and the terminal
    price sheet's F1.
KIN-DRIFTS:           K3 (a): a steady drift at the registered couplings; the mechanism
    that supplies the loss is identified in the run or the form is not rendered.
REFUSED:              B-K4 or the engine's own checks fail.

## Rules

Bars are bars; no rescue; one verdict from sealed outputs (analysis/kin_drive.npz); failures
kept; the engine used as registered (its potential, its kink, its units); no damping term
added; no coupling added beyond the registered cross term; the strain field is a prescribed
background (EM-018's reading), swept never chosen; riders and grants the author's.

## Reads owed at lock

FND-STRAND-002 (units, w values, the kink launch, PN numbers); EM-RECON-023 (cross-term sign);
EM-RECON-012 (c_L composition); EM-018 (the strain-gradient reading, verbatim); FND-KIN-001
(the dissipationless requirement, verbatim); FND-STRAND-008 (the on-site potential's origin).

## Cost and machines

Sandbox: the chain runs are seconds each; the bisection minutes. No Mac or PC time.

## Author's lock

Locked on the author's word on 2026-09-27. No computation ran before this line was written.

## READS AT LOCK (executed 2026-09-27 before any computation)

1. FND-STRAND-002: the chain is phi_ddot = kt Lap(phi) - sin(phi), energy (kt/2)(dphi)^2 +
   (1 - cos phi) per bond/site, kink 4 arctan exp(x/w) with kt = w^2, so c_t = w node per
   time unit and the kink's rest energy is 8 w, mass 8/w; ends held (phidot = 0 at the end
   nodes); the winding-weighted centre is the registered kink tracker; relaxed PN values
   at w = 2.0 and 2.8 are within the coupling-form band of the lattice's 6.8e-7 and 4.8e-9.
   As attributed. The commission uses the routine's dynamics, tracker and ends verbatim.
2. EM-RECON-023: the cross term is + c_L u' Phi' with c_L a positive constant of the
   mechanics; on the chain, energy c_L sum_j eps_j (phi_{j+1} - phi_j), so the force on
   site j is c_L (eps_j - eps_{j-1}) = c_L eps'. As attributed; the sign of the kink force
   is reported from the run, not assumed.
3. EM-RECON-012: c_L = lambda gamma tau_0 as used by FND-179; only the product enters,
   and it is absorbed into F = c_L eps' (the swept quantity). As attributed.
4. EM-018: phi's channel is the longitudinal tension channel; E is its gradient; the
   strain field is prescribed as a background. As attributed.
5. FND-KIN-001: "dissipationless drift: a freely moving knot must not decelerate"; the
   choreography open. As attributed; K3's outcome (a) would contradict the requirement
   and is therefore the first-order finding the charter says it is.
6. FND-STRAND-008: the on-site potential is the strand's orientation potential, giving
   every mode a mass; it is what makes the kink a stable localized winding. As attributed.
Outcome: no correction, no bar moved. Computation may begin.
