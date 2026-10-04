# v3.32.0 (4 Oct 2026) -- THE NORTH STAR CUT: ONE EXTERNAL NUMBER MATCHED, ONE DERIVED CLAIM CORRECTED, ONE CONTINUUM CLAIM REFUTED ON REPRODUCIBILITY, ONE INSTRUMENT RETIRED

**775 claims** (761 at v3.31.0). Fourteen new claims (FND-170 to FND-182,
ELEC-101), one status change (FND-175 registered to Failed and kept), riders
on sixteen prior claims, the North Star page, two instruments frozen or
retired, two papers regenerated. Everything here ran against v3.31.0 between
5 September and 4 October; two local runs (COMPOSITE-SELECT Leg B on the Mac;
nothing on the PC) carry into the next release.

## The one-paragraph version

The programme wrote down what it is for (docs/NORTH_STAR.md: a physical model
that makes sense, with as few fitted parameters as possible, predicting the
weights of atoms, the gravitational force and the strength of magnets) and
spent the month against that page. The first external number the wave arc
can produce was produced: the registered zero-point ledger predicts the
measured Casimir force pi^2 hbar c/(240 d^4) exactly, given hbar, by
universality on three registered closures (FND-178, consistency-tier; the
plate-geometry sign and d^-4 approach measured independently, FND-170). In
the course of it the corpus's two zero-points (the spectral half-sum the
Casimir force measures; the dynamical budget share of Prediction 32) were
found to be distinct objects and named apart (NAME_REGISTRY; 71 claims
tagged, 14 reviewed). On the magnet-facing side a steady EMF cannot spin a
strand from the bulk (FND-179, exact: the torque is a total derivative), the
registered reconnection is not the terminal that could (FND-180), and the
check exposed a false sentence in GRV-045, which was corrected on the
author's word and its benchmark rewritten to assert the amended statement.
The positive result: the lock gives a charge a derived force along its
strand, F = 2 pi c_L eps', the mesh's own qE, obeyed by the registered kink
with sine-Gordon mass and a radiation-set terminal speed (FND-181); from it
the vacuum's charge-creation field, a window [1.1e15, 3.2e18] V/m with one
unpinned input, the kink width (FND-182, census tier T2 by ruling ELEC-101).
The anti-aligned sector received its ration and gave back an instrument
finding: the bordered kernel-branch corrector that produced FND-175's
continuum family cannot re-obtain its own gates from bit-identical inputs,
because at the resonance its regularization equals the near-null singular
value squared and the step is set by library internals. FND-175 is refuted
on reproducibility and kept; FND-176/177 are artifact records; FND-174
carries a reopened caution; the resonance (FND-172) and the member (FND-173)
stand on clean states. The census over Predictions 20 to 34 held the firm
discriminator count at two plus one adjudicated and ruled that criterion C1
admits no window.

## What is new

### Claims
- FND-170 CASIMIR-PLATE (F3 sign result): attractive plate force from the
  carried modes alone, no zero-point continuation, no hand subtraction;
  d-dependence approaching d^-4.
- FND-171 LADDER: the nuclear asymmetry coefficient bracketed by two derived
  ladders, 12.8 MeV (nucleon-mass) to 39.5 MeV (bundle-mode); R4's
  non-locality confirmed necessary.
- FND-172 ANTI-ALIGNED Q1: the anti-aligned linear root is the level-1
  dispersion at the difference wavenumber, closed form, four cells.
- FND-173 ANTI-ALIGNED Q2/D3: a full-bar anti-aligned member at q = 5/4
  (RMS 8.35e-10), 8e-5 detuned from the resonance; the 2D kernel exhibited.
- FND-174 ANTI-ARC / ANTI-ARC-X: the anti-aligned family marches flat
  through the aligned collapse region on 144x36 (20/20 gated). Now carries a
  reopened caution (see FND-175).
- FND-175 KERNEL-CONT: a continuum family along the resonance kernel by
  bordered continuation. REFUTED ON REPRODUCIBILITY 4 Oct (NYQ-CONTROL-2),
  Failed and kept.
- FND-176 KERNEL-MARCH, FND-177 KERNEL-MARCH-2: the bordered march and its
  regularization. Artifact records of the retired instrument; FND-177's
  plain Gauss-Newton control points stand on their own.
- FND-178 CASIMIR-F3: CAS-LEDGER-CONSISTENT (coefficient by universality,
  -pi^2/1440 per polarization to 0.003 percent on the carried-mode chain) and
  CAS-IDENTITY-SHORT-RANGE (the helix's pinned-segment residual 2e-13: the
  wave arc's rotation contributes nothing to the Casimir force).
- FND-179 CURRENT-AS-SPIN: TWIST-NOT-SPIN, exact; and ASYMMETRY (a two-chain
  contact leaks O(g^2) transverse and zero azimuthal).
- FND-180 TERMINAL-TWIST: TERMINAL-RECON-WRONG-VARIABLE; GRV-045 amended
  (punch-through exchange 0.21 x 2 pi Frenet / 0.028 writhe; the reported
  1.007 x 2 pi was a final-state value present in the seed; F1 and F3 stand).
- FND-181 KIN-DRIVE: KIN-FORCE-DERIVED (M = 2 pi F / |a| = 8/w to 1 percent
  at two widths) and KIN-DRIFTS (relativistic to 0.5 c_t; terminal 0.68 c_t
  by phonon radiation; depinning below 1e-8; breakdown gradient 1/c_L).
- FND-182 KIN-BREAKDOWN: E_c = 2 pi T0 r^2 / (5 e w^2 a^2); window
  [1.1e15, 3.2e18] V/m across the registered scale sets and w in [0.8, 2.8];
  above every applied field, below Schwinger over most of the range; T2.
- ELEC-101: the census pass over Predictions 20 to 34 plus the FND-182
  candidate; firm count two plus one adjudicated; C1 admits no window
  (author's ruling); FND-182 stays T2 until the kink width is a number.

### Riders and corrections
- GRV-045 amended (F2 and F4 withdrawn, F1 and F3 stand; benchmark rewritten
  to read Frenet rotation and writhe before and after, asserting the bounded
  exchange; passes).
- FND-031 (E_crit = 2.0e23 V/m is the linearity limit, not breakdown);
  FND-132 and FND-MATTER-041 (budget vs spectral zero-point); FND-088;
  ELEC-062 (C1 ruling); NUC-022/029/030 (LADDER); FND-139/142/147/163/164/167
  (anti-aligned reads); EM-023.
- FND-175 refuted on reproducibility; FND-176/177 artifact records; FND-174
  caution reopened.
- Zero-point naming riders on 14 claims (13 spectral, ELEC-101 both by
  design); the 27 September sweep's review closed.

### Instruments
- benchmarks/foundations/casimir_f3.py (the carried-mode half-sum with exact
  bulk and surface subtraction, two polarizations, helix pinned segment);
  current_as_spin.py (two-chain lock with twist flux); terminal_twist.py
  (GRV-045's engine read before and after); kin_drive.py (driven sine-Gordon
  kink on a 2400-node chain); kin_breakdown.py (symbolic E_c with machine
  dimensional check); each with its verdict script.
- benchmarks/gravity/handedness_reconnection.py amended (frenet_phi, writhe,
  the bounded-exchange assertions).
- nyq_control.py (v3) and nyq_control_2.py with kernel_continuation_0916.py,
  the 2026-09-16 bordered corrector FROZEN (sha256 recorded by driver and
  verdict) with de-aliasing as its only amendment; tools/nyq2_forensics.py.
  The bordered corrector is RETIRED from the kernel question.
- Rule in force since 23 Sep: the credentialed gate's Nyquist flag is a BAR
  (wsNyq <= 1e-4), not a note.

### Documents
- docs/NORTH_STAR.md: the goal in the author's words; the scorecard (weights
  of atoms, gravitational force, strength of magnets, also carried, Casimir
  row); the input ledger; the one fence; the rule that every charter names
  the target it moves, the input it retires, or the discriminator it arms.
  HANDOFF opens with it.
- docs/NAME_REGISTRY.md addendum (spectral vs budget zero-point);
  KNOWN_LIMITATIONS gains "Conduction and charge transport" and the fence's
  spectral restatement; ROPE_PARAMETERS section 5b (the medium's electric
  limits); WHERE_IT_STANDS addenda of 27 Sep and 4 Oct; STRATEGIC_TARGETS
  sections G to O; the terminal primitive priced and parked
  (analysis/GRANT_CANDIDATE_TERMINAL_price_sheet.md, TERMINAL_price_tests.md).

## Papers regenerated
falsifiable_predictions (.docx and .pdf): the Casimir coefficient, formerly
"deliberately not added", enters as a computed consistency-tier entry
(Prediction 35) with its provenance (hbar imported, GRV-014); the charge-
creation field enters as Prediction 36 at census tier T2 with its one
unpinned input named; Prediction 32 gains the budget-vs-spectral qualifier
and the note that its upper edge waits on Leg B; the reader's recount of 4
October carries the census verdicts over 20 to 34 and the C1 ruling.
rope_blackholes (.docx and .pdf): one paragraph recording the GRV-045
amendment (the exchange is bounded and small, not a quantized 2 pi; the
no-hair column's "charge survives reconnection" is unchanged and
strengthened). docs/PAPERS.md annotated.

## Failures kept
FND-175 (reproducibility); the GRV-045 sentences withdrawn on the record;
F3's Part 2 period-average shakedown; CURRENT-AS-SPIN's sign error and
overwritten seal; KIN-DRIVE's short-chain first draft and its unbracketable
depinning threshold; NYQ-CONTROL's CONTROL-FAIL kept as a verdict in its own
right; the terminal primitive's two cheap tests both adverse (T-A 22 orders
below Einstein-de Haas; T-C discharged at the bulk, boundary open).

## Scorecard delta (NORTH_STAR section 6)
Rows moved: none from blocked to derived. Casimir row: consistency-tier
reproduction, zero fitted parameters, hbar imported. Inputs retired: one
(the anti-aligned continuum family leaves "Also carried"). Discriminators
armed: none new; the route to a third named (pin the strand mass scale in
eV, which collapses FND-182's window to a number).

## In flight (next release)
COMPOSITE-SELECT Leg B (the Mac; cell 11/7 at 31 of 40 points, 13/9 and
14/9 pending; the P32 upper edge and the Leg C price table wait on it). The
PC is free. Named for the sandbox: the strand-mass-scale derivation.
