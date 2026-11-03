# NUC-MIRROR-UNIFORM: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission NUC-MIRROR-UNIFORM, kind reconstruction, question key nuc-coulomb-mirror-displacement. Theorist's
design, 2026-11-03. The sixth design of this question and the leanest; none of the five before it was a try
(no kit locked, no evidence read). This file is committed before the kit exists; nothing below changes
afterwards; a change is a new name. No mass value of the evidence cell was read while writing it. Every number
here is a registered number, a value returned by the sealed code (quoted from the scratch run
analysis/lab/drafts/NUC-MIRROR-UNIFORM/scratch_constants.py, which imports benchmarks/lab/nuc_new_5/driver.py
unchanged and opens no table and no checkpoint), stated arithmetic on those, or a synthetic fixture. The cures
for the five deaths are in DISCLOSURES at the end; they are also built into sections 3, 5 and 9.

## 0. WHY

The Director's proposal, in my words. The weights-of-atoms row's Coulomb cell reads "Coulomb term derived from
winding charge and spacing (+9%)". The +9% is a coefficient comparison: the derived uniform-sphere a_C = 0.7716 MeV
against the empirical SEMF 0.711 (NUC-018). The term has never been scored on a measurement by itself, because in
every mass confrontation (NUC-BLIND-1, NUC-BLIND-2, NUC-NEW-5) the calibrated bond depth (a_V on Ca-40), the
surface term and the symmetry term carry most of the number. On one channel they all cancel exactly: the binding
difference of a T = 1/2 mirror pair, B(Z, N = Z+1) minus B(Z+1, N = Z), at odd A. In the registered three-term and
four-term models (NUC-018; NUC-A plus NUC-B) the volume term a_V A, the surface term (a_S/a_V) a_V A^(2/3) and the
symmetry term a_A (N-Z)^2/A, with (N-Z)^2 = 1 for both members, are identical for the two members; neither model
has a pairing term; what remains is a_C [(Z+1)^2 - Z^2]/A^(1/3) = a_C A^(2/3), because 2Z+1 = A. The Ca-40
calibration does not enter (section 5, C-2, verifies this on the sealed code to 1e-9). So the mirror displacement
energies score the derived Coulomb term alone, with no calibration in the channel.

North Star row: Weights of atoms, the Coulomb cell. Gear: depth, held to one try by the Director's word; the lead
is the cell's own registered miss (NUC-018: a_C 0.772 against 0.711, +9 percent) and the registry's silence on the
mirror channel (the Director's search and mine, this file's section 2, find no mirror-pair reading anywhere; the
five withdrawn designs of this question were never run). This is a reconstruction: it moves no target from
blocked to derived and retires no input, and says so (section 7).

## 1. THE QUESTION

Q1 (the magnitude). Does the registered uniform-sphere Coulomb term, a_C = 0.7716295 MeV on Z^2/A^(1/3) with
a_C from d0 = 2.026 fm and no constant fitted to any mass, reproduce the measured Coulomb displacement energies
of the AME2012 T = 1/2 mirror pairs at A >= 13 to within the coefficient's own registered offset (8.5 percent,
section 4)? U-AGREES would upgrade the cell's evidence from "coefficient within 9 percent of the SEMF's" to
"confirmed on a calibration-free channel at 8.5 percent". U-MISS-HIGH or U-MISS-LOW would replace the cell's
+9 percent, on this channel, with a measured bias and its sign. U-NULL-FLOOR would say the channel cannot
resolve the band. No answer changes a claim's status or a grade (section 7).

Q2 (the shape). Does the fractional miss of the uniform sphere change monotonically with A across the pairs?
TREND-FALLING (the miss shrinks with A) is the shape the self-energy and exchange corrections have (both scale
relative to Z^2 as a negative power of Z); TREND-FLAT is a pure coefficient miss; TREND-RISING is a shape the
registered corrections (NUC-C, uncoded) do not have. Q2 arms the next step (which correction, if any, to code);
it names no cause.

## 2. THE EVIDENCE SET

The table. data/ame2012/AME2012.txt in the repository, sha256
88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the pin NUC-NEW-5 CONFIG carries as
ame2012_sha256; NUC-032 carries the same), rows 'Z N M' with M the atomic mass excess in MeV, the table the blind
draws NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 treat as experimental. No other table; no AME2020 row (that file is
not in the repository and a build that needed it would wait on a person).

The rule (no choice left to the worker, no draw needed; the rule selects what is there). A pair is every odd
A >= 13 with Z_p = (A+1)/2 such that BOTH rows (Z, N) = (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present in the
table. A >= 13 because the registered models' domain is A >= 12 (NUC-NEW-5 CONFIG min_a = 12) and 13 is the
smallest odd A in it. No upper limit on A; no exclusion by any other criterion. The pairs unit of the driver
reads the Z and N columns only to form the label list (ascending A), seals the labels, and neither stores nor
prints any M. The design does not know n; the build records it. The expectation, stated and not leaned on: the
public count of mirror pairs with both masses measured by 2012 is about thirty (A = 13 to about 71).

The one read. The evidence unit opens the file once more, after the file's sha256 is re-checked against the pin,
and reads M for exactly the 2n labelled rows into one raw array that is sealed (sha256 of the bytes) before any
statistic is formed. Every later number derives from that one payload.

What the programme has and has not inspected, plainly. The AME2012 table as a whole has been inspected many
times in absolute masses (NUC-026 at 2398 nuclides; NUC-BLIND-1 and -2 drew hold-outs from it; NUC-NEW-5's audit
read it). The Coulomb displacement channel has never been formed, scored or printed in the registry or in any
analysis file (search of the memory for mirror, displacement, Nolen-Schiffer returns only this question's five
withdrawn designs and the NUC-C commission document). No constant of the model was fitted to any AME2012 mass
except a_V on Ca-40, which cancels identically in this channel. Bar W (blind hold-out) is therefore not
triggered: the quantity scored carries no calibration. The blindness of this channel rests on the programme's
non-formation of the difference, which the record cannot externally verify; it is stated, not claimed as more.

## 3. THE MODELS OR PREMISES

Frozen as registered, imported unchanged from benchmarks/lab/nuc_new_5/driver.py (the credentialed NUC-NEW-5
instrument; its a_c() and binding() are NUC-BLIND-1's constants, credentialed there by C-1 byte equality):

- a_c() = coulomb_factor / (r0_over_d0 * d0_fm) with CONFIG coulomb_factor = 0.6 * 1.44 = 0.864 MeV fm,
  d0_fm = 2.026 (the observed saturation spacing, NUC-017, adopted by NUC-018), r0_over_d0 = (3/(4 pi sqrt 2))^(1/3).
  THE SEALED CODE RETURNS a_c() = 0.7716295256894924 MeV (scratch run; r0_over_d0 = 0.5526694571400057,
  r0 = 1.1197083201656515 fm). The registry quotes 0.7716 (NUC-018 rider, NUC-032) and 0.772 (NUC-018); both agree
  with the code at the digits they quote. No hand value is used anywhere in this design.
- The channel model: CDE_U(A) = a_c() * A^(2/3) MeV, the exact difference binding(A, Z_p - 1, ...) minus
  binding(A, Z_p, ...) for any a_V, a_S/a_V, a_A (section 5, C-2). Values the code gives: A = 13, 4.266166;
  A = 21, 5.873384; A = 33, 7.938738; A = 45, 9.762263; A = 61, 11.957179; A = 75, 13.723019 MeV.
- The measured channel: CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p), with d_n - d_h =
  8.07131714 - 7.28897059 = 0.78234655 MeV from CONFIG (the code's difference: 0.7823465499999998). This is
  B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) in the driver's own binding-from-excess convention (ca40_binding_from), i.e.
  the Coulomb energy excess of the proton-rich member under charge symmetry of the non-Coulomb terms.

Nothing is calibrated and nothing is re-fit. d0 = 2.026 fm is a measured nuclear scale (NUC-017), which is why
the Coulomb cell is graded D2 on the scorecard and stays there whatever the form (section 7). NUC-C (diffuseness
and exchange corrections) is NOT scored: it has no code in the repository and its Poisson integrator cost two
designs their budgets. The self-energy-corrected variant Z(Z-1) is reported as a diagnostic (section 4), no form.

## 4. THE STATISTICS AND BARS

For pair i (ascending A): delta_i = CDE_U(A_i) / CDE_meas,i - 1 (the fractional miss of the uniform sphere; positive
means the sphere overshoots). Summary statistics, all recorded:
- mean_delta = (1/n) sum delta_i (equal weight per pair; the statistic Q1 is decided on);
- rms_delta, min and max delta_i with their A;
- diagnostic (no form): mean of delta'_i = CDE_U(A_i) (1 - 1/A_i) / CDE_meas,i - 1, the Z(Z-1) variant;
- diagnostic (no form): mean_delta displayed beside NUC-C's registered heavy-nucleus total (0.823 to 0.704,
  -14.5 percent, NUC-C), with the note that NUC-C's numbers are at Pb-208 and do not transfer to this channel.

Floor (Q1). Two half-widths on mean_delta, the larger is the floor h:
- h_boot: bootstrap over pairs, resample the n values delta_i with replacement, 10000 resamples, seed 20261103,
  h_boot = the 99.0th percentile of |mean(delta*) - mean_delta| (resamples and percentile follow NUC-NEW-5 CONFIG
  floor_resamples = 10000, floor_percentile = 99.0; the seed is this design's date);
- h_inst: the measurement floor from a disjoint resource: NUC-NEW-5's registered mass tolerance class
  audit_tol_MeV = 0.100 per mass, sqrt 2 times that per difference, divided by the smallest model CDE in the
  domain, CDE_U(13) = 4.266166 MeV, divided by sqrt n: h_inst = 0.141421 / 4.266166 / sqrt n = 0.033150 / sqrt n.
  (AME2012 mirror masses are known to keV; this floor is deliberately coarse and cannot hide a miss.)
h = max(h_boot, h_inst). The floor is computed inside the evidence unit from the sealed payload and sealed with
it; the verdict reads it. It is read before any sign is read: no MISS form exists unless |mean_delta| > h.

Band B1 = 0.085: the coefficient's own registered offset, a_c()/0.711 - 1 = 0.0853 (NUC-018's derived 0.772
against the empirical 0.711, registered "+9 percent"; the code's value 0.08527 rounded to three figures). A miss
inside B1 is what the registry already records for the coefficient; a miss outside it is new information about
the term on a channel with no calibration in it. B1 is fixed here and is not from the cell.

Q1 rule (in this order):
1. h > B1: U-NULL-FLOOR (the pair scatter or the instrument floor is wider than the band; no sign is read).
2. |mean_delta| <= B1: U-AGREES (with the diagnostic flag sign_resolved = |mean_delta| > h recorded).
3. mean_delta > B1: U-MISS-HIGH (then |mean_delta| > B1 >= h, so the floor is cleared by construction).
4. mean_delta < -B1: U-MISS-LOW (likewise).

Q2 statistic. rho_S = Spearman rank correlation of delta_i against A_i. Null: 10000 permutations of the delta_i
over the A_i, seed 20261104, p99 = the 99.0th percentile of |rho_S*| (same resample count and percentile
provenance as above; NUC-NEW-5 CONFIG q3_percentile = 99.0 is the registered permutation convention).
Q2 rule: n < 6 or fewer than 3 distinct delta_i: TREND-OPEN (provenance of 6: a perfect rank correlation at
n = 6 has permutation probability 2/720 = 0.28 percent, below the 1 percent tail, so n = 6 is the smallest n at
which any trend can clear p99; at n = 5 it is 2/120 = 1.67 percent and nothing can). Else rho_S < -p99:
TREND-FALLING; rho_S > p99: TREND-RISING; |rho_S| <= p99: TREND-FLAT.

Count halt. n < 6 halts the evidence unit (INSTRUMENT-OPEN for Q1 as well; the same provenance); n is recorded
whatever it is. No other threshold exists. Nothing is set after a preview; the verdict prints nothing until the
token is decided (labkit's rule).

## 5. THE CREDENTIALS

All in the credential unit, run before the pairs unit; each is halt-grade unless marked diagnostic. A halt
renders INSTRUMENT-OPEN for Q1 and Q2 and the evidence is never read.

- C-1 (halt): the imported a_c() equals 0.7716295256894924 to 1e-9 (the sealed code's own value; the registered
  0.7716 is checked at 1e-4 as a diagnostic consistency line). CONFIG d0_fm = 2.026 and coulomb_factor = 0.864 to
  1e-12; d_n - d_h = 0.78234655 to 1e-8.
- C-2 (halt): the cancellation identity on the sealed binding(): for A in {13, 21, 33, 45, 61, 75}, Z = (A-1)/2,
  and the three triples (a_V, a_S/a_V, a_A) = (15.0, 1.34, 0.0), (17.77, 1.108, 19.85), (16.21, 1.34, 19.85):
  |binding(A, Z, ...) - binding(A, Z+1, ...) - a_c() A^(2/3)| < 1e-9 (scratch run: worst 3.0e-14).
- C-3 (halt): the parser and the pair rule on a synthetic 'Z N M' table (fixture T, written to a temporary
  directory, never under data/): planted pairs at A = 13, 17, 21, 25, 33, 45, 61, 75 (Z_p = 7, 9, 11, 13, 17, 23,
  31, 38) and distractors (6, 5) with (5, 6) [A = 11, below the domain]; (8, 7) alone [A = 15, partner absent];
  (9, 6) with (6, 9) [A = 15, T_z = 3/2]; (20, 20) [the calibrator]; (8, 8). Expected: exactly the eight planted
  labels, ascending A, and nothing else.
- C-4 (halt): the form rule on three fixture payloads, built from fixture T's labels with M(Z_p - 1, Z_p) = 0 and
  M(Z_p, Z_p - 1) = CDE_meas - (d_n - d_h):
  F1: CDE_meas = 0.9 CDE_U for every pair, so delta_i = 1/0.9 - 1 = 0.111111 exactly (code: 0.11111111111111116).
      Expected mean_delta = 0.111111 to 1e-9, h_boot = 0, h_inst = 0.033150/sqrt 8 = 0.011720, Q1 = U-MISS-HIGH,
      Q2 = TREND-OPEN (one distinct value).
  F2: CDE_meas = CDE_U for every pair, delta_i = 0. Expected mean_delta = 0 to 1e-9, Q1 = U-AGREES with
      sign_resolved = False, Q2 = TREND-OPEN.
  F3: delta_i = 0.20, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06 in ascending A (CDE_meas = CDE_U/(1 + delta_i)).
      Expected mean_delta = 0.13 to 1e-9, rho_S = -1 exactly, Q1 = U-MISS-HIGH, Q2 = TREND-FALLING (at n = 8 the
      permutation probability of |rho*| = 1 is 2/40320, so p99 < 1 with certainty).
  The fixture CDE_meas values at A = 13, 21, 33, 45, 61 under F1 are, from the code, 3.839549, 5.286045, 7.144864,
  8.786037, 10.761461 MeV (planted M_high 3.057203, 4.503699, 6.362518, 8.003690, 9.979114 MeV); the worker's kit
  computes the rest by the same rule and the credential checks the rendered forms, not these displays.
- C-5 (halt): before the pairs unit and again before the evidence unit, sha256(data/ame2012/AME2012.txt) equals
  the pin in section 2. Diagnostic: the row count (the prior design stated 2438; recorded, not gated).
- C-6 (halt): n >= 6 (section 4).
- Manifest: labkit's manifest of the locked files (this design, the two kit files, benchmarks/lab/nuc_new_5/driver.py,
  benchmarks/lab/_kit/labkit.py, data/ame2012/AME2012.txt) taken at the first unit and re-verified at every later
  one.

Smoke (LAB_SMOKE=1): every unit in one process on fixture F3's table written to a temporary directory
(checkpoint analysis/nuc_mirror_uniform_smoke.pkl); the verdict withholds all forms. The smoke never opens
data/ame2012/AME2012.txt and never touches the evidence checkpoint.

## 6. THE FORMS

Q1, exhaustive, decided by section 4 alone: U-AGREES; U-MISS-HIGH; U-MISS-LOW; U-NULL-FLOOR; INSTRUMENT-OPEN
(any halt, any exception, any credential failure).
Q2, exhaustive: TREND-FALLING; TREND-RISING; TREND-FLAT; TREND-OPEN (n < 6 or fewer than 3 distinct deltas);
INSTRUMENT-OPEN (with Q1's).
Combinations: INSTRUMENT-OPEN is rendered for both questions together. Any other Q1 form may pair with any Q2
form; U-NULL-FLOOR with a TREND form is possible (a scatter too wide for the band can still be ordered in A) and
is reported as such without reading a sign for Q1.

## 7. WHAT COUNTS

Each form yields one rider on NUC-018 (and a line in the Coulomb cell of NORTH_STAR section 2), worded:

- U-AGREES: "NUC-MIRROR-UNIFORM (date, analysis/NUC_MIRROR_UNIFORM_results.md): the derived uniform-sphere
  Coulomb term, a_C = 0.7716 MeV from d0 = 2.026 fm with no constant fitted to a mass, scored on the n AME2012
  T = 1/2 mirror displacement energies at A >= 13, the channel in which the calibrated bond depth, the surface term
  and the symmetry term cancel exactly: mean fractional miss X (floor h), inside the coefficient's registered
  8.5 percent offset; U-AGREES. Trend in A: <Q2 token>, rho_S = Y. Grade D2 unchanged."
- U-MISS-HIGH / U-MISS-LOW: the same sentence with "mean fractional miss X (floor h), outside the registered
  8.5 percent band, sign <over/under>; U-MISS-<HIGH/LOW>: on the calibration-free channel the uniform sphere
  <overshoots/undershoots> the measured displacement energies by X; the cell's '+9 percent' is a coefficient
  comparison and this is the term's own miss. Trend in A: <Q2 token>, rho_S = Y. Grade D2 unchanged."
- U-NULL-FLOOR: "... the pair scatter floor h exceeds the 8.5 percent band; no sign read; U-NULL-FLOOR. Grade D2
  unchanged." (A clean null, full credit.)
- INSTRUMENT-OPEN: "... the kit halted at <credential>; no evidence read; INSTRUMENT-OPEN." No rider on NUC-018;
  a line in the results file only.

What moves. No grade: the Coulomb cell is D2 (exact given d0 = 2.026 fm, a measured scale) and every form leaves it
D2. None of the five numbers of NORTH_STAR 2b. Targets moved blocked to derived: 0; inputs retired: 0. The result
replaces one coefficient comparison with one measured bias on a calibration-free channel, which is reconstruction
work on a target row, and the release note says so in those words.

What it does NOT establish. Not the cause of a miss (self-energy, exchange, diffuseness, the odd nucleon's orbit,
charge-symmetry breaking; the Nolen-Schiffer literature names all of these and this design names none as found).
Not NUC-C's corrections (uncoded, unscored). Not the mass models' absolute accuracy (NUC-BLIND-2, NUC-NEW-5 stand
as they are). Not anything about A < 13 or about T = 1 or T = 3/2 multiplets. Not a prediction: AME2012 masses
predate the model; this is a confrontation of a frozen term with a channel the programme never formed.

## 8. NOT ASSUMED

Not leaned on: the Director's expected form (U-MISS-HIGH by roughly 15 to 30 percent). Not leaned on: the
theorist's prior, stated for the record: from the public Nolen-Schiffer literature the Z^2 uniform sphere with
the self-energy included overshoots displacement energies, more at light A than at heavy, so my prior is
U-MISS-HIGH with TREND-FALLING and a mean above the Director's band at the light end; I have not computed any
measured value and the design's bars do not depend on either prior. Not assumed: that AME2012's rows are all
experimental (the pin is the hash; the row-count line is diagnostic). Not assumed: that the Z^2 form is the right
form (it is the registered one; the Z(Z-1) variant is a diagnostic, not a model). Not assumed: that a_C's offset
against the SEMF (B1) is a physical bar; it is the registry's own stated precision for the coefficient and the
only provenance-honest band available. Not assumed: that a trend in A, if found, is exchange or diffuseness; Q2
reports a shape and names no cause. Not assumed: charge symmetry of the non-Coulomb terms beyond what the
registered models already impose (their non-Coulomb terms depend on A and (N-Z)^2 only, which is the cancellation
C-2 checks; nature's charge-symmetry breaking, at the 100 keV class, sits inside h_inst's coarse floor).

## 9. AUTONOMY AND COMPUTE

No step waits on a person: the table is in the repository under a pinned hash, the pair rule is deterministic,
the seeds are fixed in this file; no draw is needed and no beacon round is committed (the rule selects every
eligible pair, so there is nothing to draw). The author is not consulted; the verdict runs once from the sealed
checkpoint.

Compute: under one cpu-minute in total (a few thousand rows parsed, 20000 resamples of at most a few dozen
numbers); memory under 100 MB; wall time seconds per unit. Timeout of 600 s per unit is ample.

Instruments that exist: benchmarks/lab/nuc_new_5/driver.py (a_c(), binding(), CONFIG, imported unchanged;
credentialed under NUC-NEW-5, C-1 byte equality on NUC-BLIND-2's prediction files); benchmarks/lab/_kit/labkit.py
(Driver, Checkpoint, Halt, Verdict; its own tests benchmarks/lab/_kit/test_labkit.py).

The worker writes exactly two files, copied from the labkit example pair: benchmarks/lab/nuc_mirror_uniform/driver.py
(units in the locked order: credential [C-1 to C-4, fixture T written to a temporary directory], pairs [C-5,
labels sealed, no M stored], evidence [C-5 again, the one read, C-6, delta_i, the floors, rho_S and p99, all
sealed], done) and benchmarks/lab/nuc_mirror_uniform/verdict.py (reads the checkpoint only; applies section 4;
prints one FORM line per question; writes analysis/NUC_MIRROR_UNIFORM_results.md once, with the per-pair table
A, Z_p, CDE_meas, CDE_U, delta_i, the diagnostics, mean_delta, h_boot, h_inst, h, rho_S, p99). No build script,
no hold-out directory, no manifest file beyond labkit's own: the five earlier designs carried those and the worker
budgets did not survive them. The kit's charter is a copy of this design with the lock date and the kit file
hashes added, nothing else.

## DISCLOSURES (the cures, by death)

1. NUC-MIRROR-CDE and NUC-MIRROR-COULOMB died because C-1 pinned a hand value 0.771605 at 1e-5 that the sealed
   code does not return. Cure: every constant in this design that sealed code computes was read from the code by
   the scratch run (a_c() = 0.7716295256894924, r0/d0 = 0.5526694571400057, r0 = 1.1197083201656515 fm,
   d_n - d_h = 0.7823465499999998, the CDE_U and fixture values); C-1 pins the code's own value at 1e-9 and checks
   the registered 0.7716 at 1e-4 as a diagnostic; no tolerance is tighter than the digits quoted.
2. NUC-MIRROR-DISPLACE died because the design task exceeded its budget. Cure: this design read four files and
   five registry entries, ran one scratch script, and carries one model on one channel.
3. NUC-CDE-UNIFORM died because the worker did not finish the kit in 35 turns. Cure: the NUC-C leg (its Poisson
   integrator and conventions) is dropped entirely; the kit is two files on the labkit template, four halt
   credentials plus two hash checks and a count, three fixtures whose answers are arithmetic, no build tool, no
   hold-out directory, no second model, no draw.
4. The Director's two cures are both in place: a_c() read from the code (section 3, C-1); one model, one channel,
   all AME2012 mirror pairs with A >= 13 and |T_z| = 1/2, no draw (section 2); the pair-scatter floor is read
   before any sign (section 4, rule order 1 before 3 and 4).
