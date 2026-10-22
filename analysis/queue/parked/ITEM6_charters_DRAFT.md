# THE ITEM-6 CHARTERS -- FOUR SHORT COMMISSIONS (DRAFTS, NOT LOCKED)
# Drafted 2026-09-02 for the author's desk, against corpus v3.29.0 plus
# the post-release state. Each locks ONLY on the author's word and
# BEFORE its own first computation. These are the four "cheaper items
# with real content" of the 2026-09-02 strategic read; each is a
# one-session (at most two) commission and each is independent of the
# other five charters on the desk. House rules apply in full: bars
# before numbers, negatives registered, no rescue, grants reserved.

=======================================================================
# 6a. COMMISSION ANTI-ALIGNED -- THE Om1/2 ROOT
=======================================================================

## THE QUESTION
FND-142 found the anti-aligned sector's linear root sitting EXACTLY
on Om1/2 (2.2212 vs 2.2213 = sqrt(T) k1/2, the n = 1 cell mode), the
continuation there degenerate, near-solutions plateauing at RMS
~1e-5, no member registrable; "whether an anti-aligned branch exists
off-resonance is a degenerate-perturbation question, open." The
18 Aug handoff named it a competing job of equal standing; it never
ran. Two questions, in order:
  Q1  Is the root ON a cell mode at every rationalization, or only
      at q = 3/2? (The de-rationalization test the handoff named.)
  Q2  Does an anti-aligned two-frequency branch bifurcate off the
      resonance at all (Lyapunov-Schmidt on the 2D kernel), and if
      so can a member be gated?
The physics stake is HANDEDNESS: FND-088's exhaustive solve carried
both level-2 signs; if no anti-aligned branch exists, the level-2
winding's handedness relative to level-1 is FORCED, not chosen, and
the "handedness fork" of the angle-family file closes by theorem.

## GIVEN
The torus instrument (TRUESTATE stage 2, sparse re-instrument
credentialed); the retained cells 4/3, 3/2, 5/3, 5/4 and their
level-1 recoveries; FND-142's anti-aligned near-solutions and the
linear spectrum; the cell-mode spectrum sqrt(T) k1 n / N1 per cell.

## DESIGN COMMITMENTS
D1. Q1 by symbol and by measurement: the anti-aligned linear root
    Om2^(-)(q) computed at each retained cell from the linearized
    operator at A2 -> 0; compared with the cell-mode ladder of that
    cell. "On a mode" means within 1e-4 relative of some
    sqrt(T) k1 n / N1 (the FND-142 precision).
D2. Q2 as a reduction, not a search: at the resonant cell, project
    the nonlinear residual onto the 2D kernel (the level-2 mode and
    the coincident cell mode); form the second-order solvability
    condition; state whether a branch exists at second order, at
    what detuning, and with what leading amplitude relation.
D3. One gating attempt, only if D2 predicts a branch: seed at the
    predicted detuning and amplitude, full bars (RMS <= 1e-9,
    closure < 1e-6), charter budget 60 rounds (the registered
    fine-solve budget), no extension.

## VALIDATION BARS
v1. The aligned linear root reproduced at every cell (FND-142's
    +3.201 at 3/2; FND-147's per-cell values) to 1e-4.
v2. The resonant near-solution plateau of FND-142 (RMS ~1e-5)
    reproduced from the retained seed before any projection.
v3. The Lyapunov-Schmidt reduction verified on a known case: the
    aligned branch at small A2 must be recovered by the same
    projection (its bifurcation is non-degenerate), to 1 percent in
    the leading amplitude relation.

## VERDICT FORMS (exactly one)
  AA-STRUCTURAL: the anti-aligned root lies on a cell mode at EVERY
      retained cell. The resonance is not the 3/2 instrument's
      accident; it is the anti-aligned combination landing on a
      difference frequency by construction. Q2's reduction then
      decides existence.
  AA-ACCIDENTAL: the root is on a cell mode only at 3/2. The
      resonance was the rationalization's; Q2 runs at a non-
      resonant cell instead and a member is attempted there.
  AA-BRANCH: a member gates at full bars off-resonance (or at the
      non-resonant cell). The anti-aligned two-frequency state
      EXISTS; both handedness branches are real; the Sigma_wave
      anti-aligned corner (FND-139's conflict) has an object to be
      priced on, named as the next-order.
  AA-NO-BRANCH: the solvability condition fails (no second-order
      branch) AND the gating attempt refuses at every cell tried.
      NO anti-aligned composite exists in the registered class: the
      level-2 handedness is FORCED. Registrable at Modeled with the
      class named; the handedness fork closes; FND-139's anti-
      aligned corner is retired.
  AA-OPEN: v1-v3 fail, or the reduction predicts a branch the
      budget cannot gate. Reported; the predicted seed kept.

## SCHEDULING
Symbolic reduction: one session. Linear roots per cell: minutes each
on retained states. One gating attempt at most. Results to
analysis/ANTI_ALIGNED_results.md.

=======================================================================
# 6b. COMMISSION AXIS-MEANING -- WHAT THE PINNED AXIS REPRESENTS
=======================================================================

## THE QUESTION
The electron core carries a derived axis (index-2 tangent zeros, two
polar defects, ELEC-090/091), pinned by the weave at ordinary
strength (anisotropy fraction 0.21, 166x the noise floor, on the
order-4 cubic harmonic fixed in advance, ELEC-096/099), and NOT the
spin (ELEC-100). ELEC-091 records three readings of what it is --
(1) observable, (2) non-observable scaffolding, (3) coarse-grains
away -- and no commission was chartered. Each reading makes a
different prediction; this commission computes them and lets the
registry and the data adjudicate.
  Q1  Under reading (1): the pinning energy E_pin(n) =
      C_pin s^(-3/2) [sum n_i^4 - 3/5] E_core at the PHYSICAL s,
      converted to an orientation-dependent electron energy in the
      laboratory. Confronted with the electron-sector isotropy
      bounds (the Hughes-Drever class and the SME electron
      c-coefficients; datasets and their stated limits fixed at
      lock). Does reading (1) survive?
  Q2  Under reading (2): is there a registered reason the pinned
      axis has no laboratory handle -- i.e., the axis is always at
      a lattice minimum, the six minima are O_h-degenerate, and no
      registered interaction couples to which minimum? If the
      registry supplies the reason, reading (2) is self-consistent;
      if a registered coupling does couple (any claim in which the
      axis direction enters an energy or a rate), it is named and
      reading (2) fails.
  Q3  Under reading (3): the two conditionalities on ELEC-099
      (pre-asymptotic s = 1.5; the prolate proxy inclusion). An
      s-ladder on the registered engine, s in {1.5, 2, 3, 4}: does
      the anisotropy fraction fall as s^(-3/2) (the fixed scaling,
      confirmed) or faster (coarse-graining), or not at all?

## GIVEN
ELEC-096's harmonic and scaling law (fixed input); ELEC-099's
measured amplitude -5.2273, fraction 0.21, floor 3.15e-2, and its
three blinding controls; the registered strand engine and its PBC
setup; E_core and the physical s from the registered electron
geometry (ELEC-073/081 lineage, both estimators); the 1e-6 eV
degeneracy bar already registered on ELEC-099's face.

## DESIGN COMMITMENTS
D1. Q1's conversion uses only registered scales; E_pin at physical s
    is a symbol until the consequence leg. The external bounds are
    loaded once, at the end, with citations fixed at lock.
D2. Q2 is a registry sweep: every claim whose text or benchmark
    takes the core-axis direction as an input is listed (the
    ELEC-100 dependency-trace method, re-run outward from the axis
    rather than inward from spin). The list is the finding.
D3. Q3 reuses ELEC-099's protocol verbatim (six axes, full
    relaxation, the pre-fixed harmonic, the null projection and
    global-rotation controls at every s). The s-ladder is fixed at
    lock; the s^(-3/2) line is drawn before the points exist.

## VALIDATION BARS
v1. ELEC-099's s = 1.5 result reproduced (amplitude within the
    three-seed floor; null projection at machine zero; global
    rotation invariant).
v2. The physical s and E_core reproduced from their registered
    claims to their registered tolerances.
v3. Clean room: no bound value from the isotropy literature in any
    Leg 1-3 file.

## VERDICT FORMS (one per reading; the joint line last)
  R1-EXCLUDED: the predicted laboratory anisotropy at physical s
      exceeds the registered electron-sector bound. Reading (1) is
      dead by data; kept.
  R1-LIVE: it lies below the bound by a recorded factor. Reading (1)
      survives as a PREDICTION with a bound on its face (the axis
      is an observable of the vacuum frame at a stated, currently
      unreachable, level). Registrable on the predictions ledger at
      its earned tier.
  R2-CONSISTENT: the sweep finds no registered coupling to the
      minimum's identity; reading (2) stands as scaffolding.
  R2-COUPLED: a registered claim couples to the axis direction; it
      is named and reading (2) fails at that claim.
  R3-COARSE: the s-ladder falls faster than s^(-3/2) (fit-free:
      each rung's fraction below the drawn line by more than the
      floor); the pinning coarse-grains away and reading (3) is
      supported.
  R3-FIXED: the ladder tracks s^(-3/2) within the floor; the
      scaling stands and reading (3) is not supported.
  Joint: the surviving reading(s) named; if exactly one survives,
      ELEC-091's open item is CLOSED to that reading at Modeled
      with the data on its face; if two or more survive, the
      discriminating experiment between them is named as the
      next-order.

## SCHEDULING
Q2 is reading: hours. Q1 is arithmetic on registered scales: hours.
Q3 is four ELEC-099-class relaxation sets: one session. Results to
analysis/AXIS_MEANING_results.md.

=======================================================================
# 6c. COMMISSION METALLIC -- THE 2.8x SHORTFALL DECOMPOSED
=======================================================================

## THE QUESTION
CHEM-MET-001 derives metallic cohesion from delocalized mode
sharing, passes its own discrimination bar (Na metallic vs Cl2
molecular) and its non-saturation bar, and lands the cohesive energy
consistently ~2.8x LOW across both elements with the self-consistent
spacing already executed. The registered next-orders are the p-band
directional structure and "the x2.8 cohesion shortfall's
decomposition." This commission does the decomposition with a closed
list of registered channels, target-free.

## THE CANDIDATE CHANNELS (closed at lock; each computed, none
## adopted; each a functional of registered objects with zero new
## constants)
  M-a COHERENT COLLECTIVE SHARING: the registered R4-class channel
      (NUC-028/029/030: pairwise-coherent amplitude with volume
      normalization, E_coh ~ sqrt(N) at fixed per-state coupling)
      applied to the metal's z-fold coordination shell, against the
      pairwise mode-overlap sum the registered model uses. This is
      the one channel with a DEPENDENCY PATH from another sector;
      it is on the list for that reason and for no numerical one.
  M-b p-BAND DIRECTIONAL STRUCTURE: the registered next-order;
      the mode-overlap functional evaluated with the p-type angular
      factor rather than the s-type isotropic one.
  M-c SPACING FEEDBACK, already executed (the July spacing session):
      carried as the baseline, not re-run.
  M-d THE CONSISTENCY-TIER INHERITANCE: the adopted Schroedinger
      scale (13.6 eV coupling calibration, EM-RECON-006/010) as the
      metal inherits it; its contribution to the shortfall is
      DISPLAYED as the sector's grade ceiling, not as a channel to
      tune.

## GIVEN
benchmarks/em/metallic_bonding_foundations.py and its registered
inputs; the two elements and the measured cohesive energies as
CHEM-MET-001 loaded them (targets, consequence leg only); the R4
realization (benchmarks/nuclear/samekh_coh_realization.py) for the
functional form of M-a; the chemistry paper's p-band machinery for
M-b.

## DESIGN COMMITMENTS
D1. Each channel's cohesion is computed for BOTH elements and for
    the Cl2 control in the same run; the Na/Cl2 discrimination bar
    of CHEM-MET-001 is re-applied to every channel (a channel that
    closes the shortfall by making Cl2 metallic fails).
D2. The shortfall factor F = E_measured / E_model is recomputed per
    channel per element; the decomposition is the vector of
    per-channel factors, reported whole.
D3. M-a's coordination number z is the registered lattice's (bcc
    for Na), not a fit; M-a's per-state coupling is the registered
    mode-overlap coupling, not v0.

## VALIDATION BARS
v1. CHEM-MET-001's registered numbers reproduced (the 2.8x on both
    elements; discrimination held; non-saturation held).
v2. M-a's functional form reproduces NUC-029's -1/2 exponent on the
    nuclear test before it is applied to the metal (the form is
    transplanted only if it is the registered one).
v3. Clean room: the measured cohesive energies appear in no channel
    file before the consequence leg.

## VERDICT FORMS (exactly one)
  MET-CLOSED: one channel (or the registered sum of channels, no
      weights) brings F within 25 percent of 1 for BOTH elements
      with the Na/Cl2 discrimination held. The shortfall is
      decomposed and the channel named; CHEM-MET-001 moves from
      "declared shortfall" to Modeled-consistency-tier with the
      channel on its face.
  MET-PARTIAL: F improves for both elements but stays outside 25
      percent; the residual factor and its element-dependence
      recorded; the next-order named from the residual's shape.
  MET-DISCRIM-FAIL: a channel closes the number and breaks the
      discrimination. The channel is refused (it makes the wrong
      thing a metal) and kept on the record as a caution.
  MET-OPEN: no channel moves F outside the floor. The 2.8x is not a
      channel omission in the registered inventory; the shortfall is
      re-registered as a bound on the mode-sharing functional's
      form.

## SCHEDULING
One session; the benchmark class is seconds-per-element.
Results to analysis/METALLIC_results.md.

=======================================================================
# 6d. COMMISSION KOIDE-WEINBERG -- DERIVE OR DEMOTE
=======================================================================

## THE QUESTION
Two Conjecture-grade entries are coupled and already inconsistent
with each other: EW-001, sin^2 theta_W = 1/(3 sqrt 2) = 0.2357 from
winding/Hopf geometry, 1.94 percent from the quoted 0.23122; and
PM-001, the Koide phase (3 + Phi) = 4.618 giving the lepton ratios to
~1 percent WITH the measured angle, and FAILING (mu/e ~ 1605 against
206.8) with the model's OWN angle. KNOWN_LIMITATIONS holds both
"pending a derivation-or-demotion." This commission executes that
sentence, target-free, in one sitting.
  Q1  SENSITIVITY. d ln(m_mu / m_e) / d ln(sin^2 theta_W) under
      PM-001's construction, exactly. A relation whose output moves
      eightfold under a two-percent input is not a prediction; it
      is a fit to the input. The number is computed before any
      demotion is discussed.
  Q2  THE SCHEME. A scale-free geometric number can be compared to
      exactly one renormalization point. EW-001 as registered
      compares to 0.23122 (the MS-bar value at M_Z). The low-Q^2
      effective angle is a different number (~0.238). Which point
      the conjecture claims is fixed at lock, BEFORE the comparison
      is re-read, so that no point can be chosen for its proximity.
      Locked at drafting: the registered comparison, 0.23122, stands
      unless the author changes it at lock; the low-Q^2 value is
      DISPLAYED alongside, never adjudicated against.
  Q3  THE DEPENDENCY PATH. For each entry: is there a derivation
      chain from registered objects to the number with zero choices
      (FND-088's protocol: require a dependency path before looking
      at the target)? The three Weinberg papers (rope_weinberg_angle,
      rope_two_axioms_weinberg, rope_hopf_weinberg) and
      rope_lepton_masses are read for the chain, and every choice
      point is listed. PM-003's structural reclassification (the
      lepton problem is a 3-level excitation spectrum) is the
      standing context and is not re-litigated.

## GIVEN
The two claims and their papers; PM-003 (Derived); the registered
comparison values as the claims quote them; the measured lepton
masses (consequence leg only).

## DESIGN COMMITMENTS
D1. Q1 is exact algebra on PM-001's stated construction, symbolic.
D2. Q3's choice-point list is the finding for each entry: a chain
    with zero choice points is a DERIVATION with a miss to explain;
    a chain with one or more choice points is a CONJECTURE whose
    choices are now named; no chain is a NUMEROLOGY entry.
D3. No new geometry is proposed. This commission adjudicates what is
    registered; a new derivation, if the author wants one attempted,
    is its own charter.

## VALIDATION BARS
v1. PM-001's ~1 percent landing with the measured angle and its
    1605 failure with 1/(3 sqrt 2) both reproduced from the stated
    construction.
v2. EW-001's 1.94 percent reproduced against the locked comparison.
v3. Clean room: no lepton mass and no measured angle in the Q1/Q3
    files.

## VERDICT FORMS (one per entry)
  EW-DERIVATION-WITH-MISS: zero choice points; 1/(3 sqrt 2) follows
      from registered geometry. The entry is UPGRADED to a derived
      number with a registered 1.94 percent miss at the locked
      comparison point, and the miss becomes a named open item
      (running / threshold effects are NOT invoked to close it
      unless a registered mechanism supplies them).
  EW-DEMOTE: one or more choice points, or the chain does not
      reach the number. The entry is demoted from Conjecture to a
      kept coincidence with its choice points on the face, and the
      predictions ledger's structural entry that cites it is
      annotated.
  PM-DEMOTE: the sensitivity of Q1 exceeds 10 (output moves more
      than tenfold per unit relative input) OR the chain has choice
      points. PM-001 is demoted to a kept coincidence; the Koide
      relation's status in the corpus becomes "an observed relation
      among measured masses, not a rope result," which is what the
      data supported all along.
  PM-RETAIN: sensitivity below 10 AND a zero-choice chain. PM-001
      stands as a conditional relation, its condition (the measured
      angle) stated as an input.
  Joint: if EW demotes and PM was conditional on EW, the pair is
      recorded as resolved by the demotion; the inconsistency
      KNOWN_LIMITATIONS carries is closed.

## SCHEDULING
Reading and symbolic algebra; one short session. Results to
analysis/KOIDE_WEINBERG_results.md.

=======================================================================
## STANDING (all four)
Registered claims untouched until the author grants. Grants reserved
to the author. None of the four depends on GR54 or on any of the
other five charters; ANTI-ALIGNED shares the torus instrument with
COMPOSITE-SELECT and should not run concurrently with it in the same
container. Each ships with its own results doc; this file is split
into four LOCKED files at lock, one per commission, so that each
verdict lives with its own bars.

DRAFTS, NOT LOCKED. Lock lines and amendments, if any, go below each
commission's own text once split.
