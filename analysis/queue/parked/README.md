# Parked drafts

Drafts of commissions the lab withdrew after review (2026-10-19/20). A withdrawn name stays taken in the lab, so
a successor is drafted under a new name (GRV-2PI-DERIVE-2 and so on) and the revised draft goes in analysis/
beside the others. These are kept for the record and for the parts worth reusing; the lab's Director does not
read this directory.

- GRV-2PI-DERIVE-1: parked after 3 rounds; the external reviewer wants the harness to compute the flux from the
  construction's outputs rather than accept a self-certified C-8.
- GRV-EFE-DERIVE-1: parked after 3 rounds; harness engineering (freeze unit gated on delivery, terminal hash
  mismatch, controls wrapped, efe_core.py and guard.py in the review package).
- GRV-NU-DERIVE-1: parked on the machine-checklist forms line.
- GRV-EFE-1: abandoned by the worker ("cannot make the sealed input credentialed from inside this sandbox").
- GRV-BLIND-3: abandoned; both reviewers found the same-table statistic self-referential. Retired rather than
  revised; a blind confrontation needs a non-SPARC sample and the sealed-input credentialing GRV-EFE-1 lacked.
- QP-HULL-1: abandoned on a compute estimate of the v1 instrument; the spectral hull is small; Leg 0 part 2 is on
  the record (analysis/QP_HULL_1_leg0_results.md, 2026-10-24: the hull converges onto the 13/9 cell, om2 gap 1.7e-5
  at member 1 and 3.7e-3 at member 2 on 48x12x36); successor QP-HULL-2 is charted on it.
- ITEM6 (ANTI-ALIGNED, AXIS-MEANING, METALLIC, KOIDE-WEINBERG): four charters in one old draft file, all four executed and withdrawn before 2026-10-20; moved here 2026-10-21 so the Director stops re-reading it.
- ELEC-FF-SUB-1: withdrawn 2026-10-21 14:31; the worker declined to redraft against the external round-2 review
  (harness checked tokens and formula agreement, not a coupling mechanism; positive fixture accepted a fabricated
  extent). Successor ELEC-FF-SUB-2 drafted with a harness-evaluated density. The SUB-1 draft stays in analysis/
  as the record of the first form.
- ELEC-G-1: withdrawn 2026-10-21 15:20 after 3 rounds; the skeptical reviewer passed the physics in rounds 2 and 3,
  the external failed each round on harness defects (fail-closed halts, output published before the form,
  one-shot rendering). Successor ELEC-G-2 on the harness kit, with the round-1 control-leg fix.
- FINE-DISP-1: vetoed by the author after the executor's preview on the evidence cell made the lock impossible
  under checklist items B and I (both reviewers, round 1); the preview stands as an exploratory record
  (analysis/FINE_DISP_1_preview.md). A blind successor would be the same coefficient on the registered fibre
  operator, a different instrument, chartered only after the kit is in use.
- ELEC-MECH-1: withdrawn 2026-10-25 after one lock round (both reviewers: every class outcome was a closed form, on the record, or scale-free from a computed cell, so no verdict was open before the lock; the worker abandoned). Right call. Its content is the executor's reading, analysis/ELEC_MECH_1_reading.md; successor ELEC-KAPPA-1 asks the one number nobody knows.

- ELEC-KAPPA-1: withdrawn by the lab 2026-10-25 16:15 (worker abandonment, both reviewers). Reasons kept: (1) the
  executor's Leg C section 6 estimate (J_1 at the registered kappa is HBAR-003's S_1) is a preview of the
  confrontation, so the outcome was known to within the band before the lock; (2) J_1 = 2 pi kappa / c is the
  RING's angular momentum, not the class's (a non-circular member carries (2 pi kappa / c)(4 pi A / L^2), less), so
  the confrontation scored one member and called it the class; (3) reading (ii) (the strands' rod torsion, 2 C)
  does not establish that the pair's twist propagates at c; (4) the pair-tension convention (T0 per strand or per
  pair) was not fixed. Record corrected in analysis/ELEC_MECH_1_legC_instrument.md section 7. Not redrafted: the
  number it wanted is on the record as HBAR-003's wall; nothing with an unknown outcome remains in it.
- RING-WAVE-ANOMALY-R: withdrawn by the lab 2026-10-25 18:30 (worker abandonment on the merits; external reviewer's
  objections 1 and 4). Reasons kept: (1) North Star: a replication of a number already on record moves no target,
  retires no input and discriminates nothing, so it is interior work the section 5 budget does not allow in
  sequence; (2) the replication re-derives its own credential (the coefficient A = 2(c_E - c_M) is the derivation
  being checked, so D2's bars and D3's threshold were set after inspection of the result); (3) the dictionary
  question Q2 is already answerable: the worker read EM-015 and EM-018 as NEUTRAL (the registry is SILENT on
  whether the twist energy contains the field energy), so the form would have been ANOMALY-UNDECIDED by
  construction; (4) the executor's reading remains the record of 4 alpha / pi, conditional on additive field
  energy. Not redrafted. The next electron commission with an unknown outcome is RING-WAVE-STABILITY (the
  Director's memo 2026-10-25 #2), proposed by the Director under approval mode; its Leg 0 instrument is
  benchmarks/foundations/ring_wave_stability.py, credentialed on known answers only.
- RING-WAVE-STABILITY (author's draft, 2026-10-26): never proposed; the name was taken by the Director's own
  Hessian-only proposal of 2026-10-25, which the author declined in favour of this draft, and the Director then read
  the declined name as covering the draft. Re-filed unchanged as RING-WAVE-STABILITY-2 (analysis/RING_WAVE_STABILITY_2_charter_DRAFT.md).
- CROSSING-PRICE-1: withdrawn by the worker 2026-10-27 09:00 before drafting; the executor concedes all five reasons.
  (1) D1 was ill-posed: a tension-bending profile with a point constraint and no span has infimum zero (E L stays at
  1.234 as L grows), and l_b = r / sqrt 2 = 6.6e-20 m makes bending irrelevant; the price is T0 d^2 / 2L, set entirely
  by an unregistered span. (2) D2's self-consistency was degenerate by algebra (U(x) = x^2 + 1 / (1 + x^4) has no
  interior minimum; STANDOFF-NONE forced before any run). (3) The premise was stale: JUNCTION-LOCK (verdict
  JUNCTION-FREE) found f = 0 identically at the registered level, NODE-STANDOFF found crossings away from nodes do
  not interact, FND-070 assigns the just-in-contact placement to matter and not the vacuum, and FND-182 moved T2 to
  T4; the executor had not read those records and re-opened a closed question. (4) The outcome was bounded: any
  registered span gives PINNED by an order or more, as CROSSING-PRICE (w = 0.003 at touching) and NODE-STANDOFF's G5
  already say. (5) Notation and T-1 bookkeeping defects. Not redrafted. The two alternatives the worker named (a price
  sheet for V_0 as a function of unregistered A_c and span, with the coasting span L* of order 1e4 to 1e5 a; or the
  junction's azimuthal locking under the 'tie holds the face' grant) are the author's to choose; neither is a commission.
- RING-WAVE-STABILITY-2: withdrawn by the lab 2026-10-27 13:00 after 3 review rounds. The worker's lab-side
  charter and kit (benchmarks/lab/ring_wave_stability_2/) were never pushed (the lab commits only on a lock), so
  the record of what was built is the review transcript. Progress across the rounds: S2's pre-pin preview made
  exploratory and the form-bearing cells disjoint (cured, both reviewers); the v5 J bar re-sourced from the
  beta = 0.5 credential rather than inspected kappa = 0.3 fixtures (cured); deformed-polygon shape floor and
  late-time control gate added; Q2 qualifying set made consistent with the NEUTRAL-DRIFTS witness rule; the
  check amplitude 3e-3 made consistent; failed trajectories probe-local. Round 3: skeptical PASS (non-blocking:
  49 trajectories and the 11 half-step units in the budget; Q0 presented as inventory only). External FAIL on
  two points: (a) Q0 is form-bearing while its classification rule was written after the drafter inspected all
  five claim texts it adjudicates, so its result is not blind; cure named: drop Q0 from the FORM list, keep the
  wording inventory as background, mark every dynamics decision conditional on action (i); (b) the worker's
  procrustes_shape registers nodes by index, so a cyclic relabeling of an unchanged noncircular polygon can
  report nonzero D_shape; cure named: correspondence-aware (or correspondence-free) shape distance with
  known-answer fixtures (unchanged polygon under cyclic relabeling, relabeling plus rotation, genuine
  deformation) and locked bars. Successor RING-WAVE-STABILITY-3 to be drafted on the author's word with both
  cures and every round-1/2 repair written into the executor's draft, since the worker's revisions are not on
  any branch.
- RING-WAVE-STABILITY-3: withdrawn by the lab 2026-10-27 21:32 after 3 review rounds (76 minutes; $13 in all). The
  round-3 cures of -2 held: Q0 as a premise was accepted by both reviewers, and the external called the
  correspondence-free shape observable "a substantive new discriminator". Rounds 1 and 2 were the worker's kit
  again (S2 excluded from the form-bearing set at lock; a saturating instability must class GROWS, with a fixture;
  a growing run that fails scored from its valid prefix as a witness, with the end state read from the prefix;
  the production step credentialed on K2 at large amplitude; a late-time floor for Q1; a drift-statistic
  agreement for the Q1b half-step gate; Q2 witnesses by the same predicate as Q1; mixed-availability end marks;
  the F1b bar made prospective), all cured by round 3, where the skeptical reviewer PASSED. The external FAILED
  round 3 on ONE point: NORTH_STAR section 5. ELEC-G-2 (2026-10-22) was itself interior, no target-facing session
  has completed since, and the rule says at most one interior session between target-facing ones; the charter's
  own words concede it, and "the cited approval is not presented as an explicit exception to section 5". A second
  point travels with it: the readings must not call RING-STABLE + NEUTRAL-HOLDS an A2 pass or RING-UNSTABLE an A2
  failure (no dynamical spectrum is computed; the experiment tests selected finite-amplitude probes for 40
  periods under an adopted action), and END-FOLD establishes two end-state marks, not decay into a g = 0.9 state.
  Not a physics or instrument objection. The successor waits on the author's decision under section 5 (his own
  rule): an explicit dated exception on that page, a target-facing session first, or the shelf. The worker's -3
  kit was not pushed.
