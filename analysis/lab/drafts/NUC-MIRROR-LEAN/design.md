# NUC-MIRROR-LEAN: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission NUC-MIRROR-LEAN, kind novel_prediction as proposed (section 7 says what it is in the house's grades:
a confrontation of a frozen term with a channel the programme never formed, not a prediction of an unmeasured
quantity), question key nuc-coulomb-mirror-displacement. Theorist's design, 2026-11-04. The seventh design of this
question; none of the six before it was a try (no kit locked, no evidence read). This file is committed before the
kit exists; nothing below changes afterwards; a change is a new name. No mass value of the evidence cell was read
while writing it. Every number here is a registered number, a value returned by the sealed code (quoted from the
scratch run analysis/lab/drafts/NUC-MIRROR-LEAN/scratch_constants.py, which imports
benchmarks/lab/nuc_new_5/driver.py unchanged and opens no table and no checkpoint), stated arithmetic on those, or a
synthetic fixture. The cures for the six deaths are in DISCLOSURES at the end and are built into sections 3, 5 and 9.

## 0. WHY

The Director's proposal, in my words. The weights-of-atoms row's Coulomb cell reads "Coulomb term derived from
winding charge and spacing (+9%)". The +9% is a coefficient comparison: the derived uniform-sphere a_C = 0.7716 MeV
(NUC-018, NUC-031) against the empirical SEMF coefficient 0.711 that NUC-018 compares it with. The term has never
been scored on a measurement by itself: in every mass confrontation (NUC-BLIND-1, NUC-BLIND-2, NUC-NEW-5) the
calibrated bond depth a_V (Ca-40), the surface term and the symmetry term carry most of the number. On one channel
all three cancel exactly: the binding difference of a T = 1/2 mirror pair at odd A, B(Z_p - 1, Z_p) minus
B(Z_p, Z_p - 1) with Z_p = (A + 1)/2. In the registered models (NUC-018 three-term; NUC-A plus NUC-B four-term) the
volume term a_V A, the surface term (a_S/a_V) a_V A^(2/3) and the symmetry term a_A (N - Z)^2/A, with (N - Z)^2 = 1
for both members, are identical for the two members; neither model has a pairing term; what remains is
a_C [Z_p^2 - (Z_p - 1)^2]/A^(1/3) = a_C A^(2/3), because 2 Z_p - 1 = A. The Ca-40 calibration does not enter
(C-2 verifies this on the sealed code). So the mirror displacement energies score the derived Coulomb term alone.

North Star row: Weights of atoms, the Coulomb cell. Gear: depth; the lead is the cell's own registered miss
(NUC-018: 0.772 against 0.711) and the registry's silence on the mirror channel (search of the memory for mirror,
displacement, Nolen-Schiffer returns only this question's six withdrawn designs and the NUC-C commission
document; none was run). It moves no target from blocked to derived and retires no input, and says so (section 7).

## 1. THE QUESTION

Q1, the only question. Does the registered uniform-sphere Coulomb term, a_C = 0.7716295 MeV on Z^2/A^(1/3) with
a_C from d0 = 2.026 fm and no constant fitted to any mass, reproduce the measured Coulomb displacement energies of
the AME2012 T = 1/2 mirror pairs at A >= 13 to within the coefficient's own registered offset (B1 = 0.085,
section 4)? U-AGREES would upgrade the cell's evidence from "coefficient within 9 percent of the SEMF's" to
"confirmed on a calibration-free channel at 8.5 percent". U-MISS-HIGH or U-MISS-LOW would add to the cell, on this
channel, a measured bias with its sign. U-NULL-FLOOR would say the channel cannot resolve the band. No answer
changes a claim's status or a grade (section 7). There is no Q2: the earlier trend question and the NUC-C leg are
dropped (DISCLOSURES).

## 2. THE EVIDENCE SET

The table. data/ame2012/AME2012.txt in the repository, sha256
88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the pin NUC-NEW-5 CONFIG carries as
pins['ame2012_sha256']; NUC-031 and NUC-032 carry the same), rows 'Z N M' with M the atomic mass excess in MeV,
the table the blind draws NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 treat as experimental. No other table.

The rule (the one filter; no choice left to the worker, no draw). A pair is every odd A >= 13 with Z_p = (A + 1)/2
such that BOTH rows (Z, N) = (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present in the table. A >= 13 because the
registered models' domain is A >= 12 (NUC-NEW-5 CONFIG min_a = 12) and 13 is the smallest odd A in it. No upper
limit on A; no other exclusion. Rows are parsed exactly as ca40_binding_from() parses them: a line splits into
three tokens, Z and N compared as integer strings, M read as float. The design does not know n; the build records
it. The expectation, stated and not leaned on: about thirty pairs (A = 13 to about 71).

The one read. The evidence unit re-checks the file's sha256 against the pin, forms the label list (ascending A),
reads M for exactly the 2n labelled rows into one raw array that is sealed (sha256 of its bytes) before any
statistic is formed. Every later number derives from that one payload. The driver never prints a mass, a
displacement energy, a delta or a mean; the verdict prints the FORM line once (labkit's rule).

What the programme has and has not inspected, plainly. AME2012 as a whole has been inspected many times in
absolute masses (NUC-026 at 2398 nuclides; NUC-BLIND-1 and -2 drew hold-outs from it; NUC-NEW-5's audit read it).
The Coulomb displacement channel has never been formed, scored or printed in the registry or in any analysis
file. No constant of the model was fitted to any AME2012 mass except a_V on Ca-40, which cancels identically in
this channel; bar W (blind hold-out) is therefore not triggered. The blindness of the channel rests on the
programme's non-formation of the difference, which the record cannot externally verify; it is stated, not
claimed as more.

## 3. THE MODELS OR PREMISES

Frozen as registered, imported unchanged from benchmarks/lab/nuc_new_5/driver.py (the credentialed NUC-NEW-5
instrument; its a_c() and binding() are NUC-BLIND-1's constants, credentialed there by C-1 byte equality):

- a_c() = coulomb_factor / (r0_over_d0 * d0_fm), CONFIG coulomb_factor = 0.6 * 1.44 = 0.864 MeV fm, d0_fm = 2.026
  (the observed saturation spacing, NUC-017, adopted by NUC-018), r0_over_d0 = (3/(4 pi sqrt 2))^(1/3).
  THE SEALED CODE RETURNS a_c() = 0.7716295256894924 MeV (scratch run; r0_over_d0 = 0.5526694571400057). The
  registry quotes 0.7716 (NUC-031) and 0.772 (NUC-018); both agree with the code at the digits they quote. No hand
  value is used anywhere in this design.
- The channel model: CDE_U(A) = a_c() * A^(2/3) MeV, the exact difference binding(A, Z_p - 1, ...) minus
  binding(A, Z_p, ...) for any (a_V, a_S/a_V, a_A) (C-2). Code values: A = 13, 4.266166; 17, 5.101620; 21,
  5.873384; 25, 6.597340; 33, 7.938738; 45, 9.762263; 61, 11.957179; 75, 13.723019 MeV.
- The measured channel: CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p), with d_n - d_h from CONFIG
  (code: 0.7823465499999998 MeV). This is B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) in the driver's own
  binding-from-excess convention (ca40_binding_from: B = Z d_h + N d_n - M).

Nothing is calibrated and nothing is re-fit. d0 = 2.026 fm is a measured nuclear scale (NUC-017), which is why the
Coulomb cell is D2 and stays there whatever the form. NUC-C (diffuseness and exchange) is NOT scored: it has no
code in the repository. The self-energy variant Z(Z - 1), i.e. CDE_U (1 - 1/A), is reported as one diagnostic
line with no form.

## 4. THE STATISTICS AND BARS

For pair i (ascending A): delta_i = CDE_U(A_i) / CDE_meas,i - 1 (the fractional miss; positive means the sphere
overshoots). Recorded: mean_delta = (1/n) sum delta_i (equal weight per pair; the statistic Q1 is decided on);
rms_delta; min and max delta_i with their A; the diagnostic mean of delta'_i = CDE_U(A_i)(1 - 1/A_i)/CDE_meas,i - 1
(no form).

Floor (the pair-scatter floor test). Two half-widths on mean_delta; the larger is the floor h:
- h_boot: bootstrap over pairs, resample the n values delta_i with replacement, 10000 resamples, seed 20261104,
  h_boot = the 99.0th percentile of |mean(delta*) - mean_delta| (resamples and percentile follow NUC-NEW-5 CONFIG
  floor_resamples = 10000, floor_percentile = 99.0; the seed is this design's date). The convention is the sealed
  driver's own (benchmarks/lab/nuc_new_5/driver.py lines 250 to 256), fixed here so the fixture values of C-3 are
  reproducible to 1e-9: rng = numpy.random.default_rng(20261104); for each of the 10000 resamples, one call
  s = rng.choice(delta, size=n, replace=True) on the delta array in ascending-A order, dev_i = |mean(s) - mean_delta|;
  h_boot = numpy.percentile(dev, 99.0) with the default (linear) method;
- h_inst: the measurement floor from a disjoint resource: NUC-NEW-5's registered mass tolerance class
  audit_tol_MeV = 0.100 per mass, sqrt 2 times that per difference, divided by the smallest model CDE in the
  domain, CDE_U(13), divided by sqrt n: h_inst = 0.1 sqrt 2 / CDE_U(13) / sqrt n = 0.03314952 / sqrt n (code value
  of the numerator: 0.03314952113422842). AME2012 mirror masses are known to keV; this floor is deliberately coarse
  and cannot hide a miss.
h = max(h_boot, h_inst), computed inside the evidence unit from the sealed payload and sealed with it. It is read
before any sign is read, and it is read against the band edge, not against zero: a side of B1 is rendered only
when the floor-widened interval [mean_delta - h, mean_delta + h] lies wholly on that side of the band
(house discipline 5: the effect scored here is band membership, so the floor must clear the distance to B1).

Band B1 = 0.085: the coefficient's own registered offset, a_c()/0.711 - 1 = 0.08527 (code; NUC-018's derived 0.772
against the empirical 0.711, the scorecard's "+9%"), rounded to three figures. A miss inside B1 is what the
registry already records for the coefficient; a miss outside it is new information about the term on a channel
with no calibration in it. B1 is fixed here, from the registered comparison, not from the cell.

Q1 rule, in this order (the first rule that holds decides; checked on the worked cases mean 0.08 with h 0.07 and
mean 0.09 with h 0.07, both of which render U-OPEN-BAND by the scratch run, neither a side):
1. h > B1: U-NULL-FLOOR (the floor is wider than the band; no sign is read).
2. |mean_delta| + h <= B1: U-AGREES (the whole floor-widened interval lies inside the band).
3. mean_delta - h > B1: U-MISS-HIGH (the whole interval lies above the band).
4. mean_delta + h < -B1: U-MISS-LOW (the whole interval lies below the band).
5. Otherwise: U-OPEN-BAND (the floor straddles a band edge; no side is read). The diagnostic flag
   sign_resolved = |mean_delta| > h is recorded under every form and decides nothing.

Count halt. n < 5 halts the evidence unit (INSTRUMENT-OPEN). Provenance: the bootstrap's 99th percentile needs at
least 100 distinct resamples to be resolvable at the 1 percent level; the number of distinct bootstrap samples of
n items is C(2n - 1, n), which is 126 at n = 5 and 35 at n = 4. n is recorded whatever it is. No other threshold
exists; nothing is set after a preview.

## 5. THE CREDENTIALS

All in the credential unit, run before the evidence unit; each is halt-grade unless marked diagnostic. A halt
renders INSTRUMENT-OPEN and the evidence is never read.

- C-1 (halt): the imported a_c() equals 0.7716295256894924 to 1e-9 (the sealed code's own value, no hand
  arithmetic). Diagnostic lines: |a_c() - 0.7716| < 1e-4 (the registered digits, NUC-031); CONFIG d0_fm = 2.026
  and coulomb_factor = 0.864 to 1e-12; d_n - d_h = 0.78234655 to 1e-8.
- C-2 (halt): the cancellation identity on the sealed binding(): for A in {13, 17, 21, 25, 33, 45, 61, 75},
  Z = (A - 1)/2, and the three triples (a_V, a_S/a_V, a_A) = (15.0, 1.34, 0.0), (17.77, 1.108, 19.85),
  (16.21, 1.34, 19.85): |binding(A, Z, ...) - binding(A, Z + 1, ...) - a_c() A^(2/3)| < 1e-9 (scratch run: worst
  3.0e-14).
- C-3 (halt): the filter and the form rule on fixture T, a synthetic 'Z N M' table written to a temporary
  directory (never under data/): planted pairs at A = 13, 17, 21, 25, 33, 45, 61, 75 (Z_p = 7, 9, 11, 13, 17, 23,
  31, 38), each with M(Z_p - 1, Z_p) = 0 and M(Z_p, Z_p - 1) = 0.9 CDE_U(A) - (d_n - d_h) (code: 3.057203, 3.809112,
  4.503699, 5.155259, 6.362518, 8.003690, 9.979114, 11.568371 MeV), and distractors with M = 0: (6, 5) with (5, 6)
  [A = 11, below the domain]; (8, 7) alone [A = 15, partner absent]; (9, 6) with (6, 9) [A = 15, T_z = 3/2]; (20, 20);
  (8, 8). Expected, checked by the same functions the evidence unit calls: labels exactly the eight planted pairs,
  ascending A, n = 8; delta_i = 1/0.9 - 1 for every pair, mean_delta = 0.111111 to 1e-9 (code:
  0.11111111111111116); h_boot = 0 to 1e-12; h_inst = 0.03314952/sqrt 8 = 0.011720 to 1e-9 (code:
  0.011720125593549844); form U-MISS-HIGH.
  Every form must be reached. Five payloads F1 to F5 on the same eight labels, each written as its own table with
  M(Z_p - 1, Z_p) = 0 and M(Z_p, Z_p - 1) = CDE_U(A)/(1 + f_i) - (d_n - d_h), f_i the planted delta per pair in
  ascending A, written with repr(float(M)) so the text round-trips exactly; plus the four-pair table T4. Expected
  values are the code's (scratch run analysis/lab/drafts/NUC-MIRROR-LEAN/scratch_fixtures.py, section 4's bootstrap
  convention, seed 20261104), pinned halt-grade at 1e-9 unless stated:

  | payload | f_i (ascending A) | mean_delta | h_boot | h_inst | h | form |
  |---|---|---|---|---|---|---|
  | F1 | 1/0.9 - 1 for all | 0.11111111111111116 | 0 (to 1e-12) | 0.011720125593549844 | 0.011720125593549844 | U-MISS-HIGH |
  | F2 | 0 for all | 0.0 | 0 (to 1e-12) | 0.011720125593549844 | 0.011720125593549844 | U-AGREES |
  | F3 | 1/1.2 - 1 for all (CDE_meas = 1.2 CDE_U) | -0.16666666666666663 | 0 (to 1e-12; code 5.6e-17) | 0.011720125593549844 | 0.011720125593549844 | U-MISS-LOW |
  | F4 | 0.05, 0.11 alternating (A = 13: 0.05) | 0.08000000000000007 | 0.02250000000000002 | 0.011720125593549844 | 0.02250000000000002 | U-OPEN-BAND |
  | F5 | 0.0, 0.5 alternating (A = 13: 0.0) | 0.25 | 0.1875 | 0.011720125593549844 | 0.1875 | U-NULL-FLOOR |
  | T4 | F1's rows at A = 13, 17, 21, 25 only, plus the distractors | n = 4 | | | | C-5 halt, INSTRUMENT-OPEN |

  F4 decides by rule 5 (|mean| + h = 0.10250000000000009 > B1 and mean - h = 0.05750000000000005 < B1); F5 by rule 1
  (h = 0.1875 > B1); F3 by rule 4 (mean + h = -0.15494654107311678 < -B1). On T4 the evidence routine must raise
  the C-5 halt (n = 4 < 5) before any M is read; C-3 passes on T4 only when that halt is raised. C-3 as a whole
  passes only when all six expectations hold; the same filter, statistic, floor and rule functions the evidence
  unit calls are used, with no fixture-specific branch.
- C-4 (halt): before the evidence unit, sha256(data/ame2012/AME2012.txt) equals the pin in section 2.
  Diagnostic: the row count (recorded, not gated).
- C-5 (halt): n >= 5 (section 4), inside the evidence unit, before any M is read.
- Manifest: labkit's manifest of the locked files (this design, the two kit files,
  benchmarks/lab/nuc_new_5/driver.py, benchmarks/lab/_kit/labkit.py, data/ame2012/AME2012.txt) taken at the
  first unit and re-verified at every later one.

Smoke (LAB_SMOKE=1): every unit in one process on fixture T written to a temporary directory (checkpoint
analysis/nuc_mirror_lean_smoke.pkl); the verdict withholds all forms in smoke. The smoke never opens
data/ame2012/AME2012.txt and never touches the evidence checkpoint.

## 6. THE FORMS

Q1, exhaustive, decided by section 4 alone: U-AGREES; U-MISS-HIGH; U-MISS-LOW; U-OPEN-BAND (the floor straddles a
band edge; no side read; a clean open result); U-NULL-FLOOR; INSTRUMENT-OPEN (any halt, any exception, any
credential failure, n < 5). Exactly one is rendered: rules 1 to 5 partition every (mean_delta, h) with h >= 0.
There is no second question, so no combinations.

## 7. WHAT COUNTS

Each form yields one rider on NUC-018 (and a line in the Coulomb cell of NORTH_STAR section 2), worded:

- U-AGREES: "NUC-MIRROR-LEAN (date, analysis/NUC_MIRROR_LEAN_results.md): the derived uniform-sphere Coulomb term,
  a_C = 0.7716 MeV from d0 = 2.026 fm with no constant fitted to a mass, scored on the n AME2012 T = 1/2 mirror
  displacement energies at A >= 13, the channel in which the calibrated bond depth, the surface term and the
  symmetry term cancel exactly: mean fractional miss X, rms Y (floor h); the floor-widened interval |X| + h lies
  inside the coefficient's registered 8.5 percent band B1; U-AGREES. X is an equal-weight average over the pairs
  and says nothing about the light-A versus heavy-A behaviour, which this commission does not read. Grade D2
  unchanged."
- U-OPEN-BAND: the same sentence with "mean fractional miss X, rms Y (floor h); the floor straddles the edge of the
  8.5 percent band (|X| + h > B1 and |X| - h < B1); no side of the band is read and no sign is claimed against it;
  U-OPEN-BAND. Grade D2 unchanged." A clean open result, full credit; the per-pair table is published.
- U-MISS-HIGH / U-MISS-LOW: the same sentence with "mean fractional miss X, rms Y (floor h); the whole floor-widened
  interval X -/+ h lies outside the registered 8.5 percent band; U-MISS-<HIGH/LOW>: on the calibration-free channel the uniform sphere <overshoots/undershoots>
  the measured displacement energies by X; the cell's '+9%' is a coefficient comparison and this is the term's own
  miss. Grade D2 unchanged." The cell's text gains "(mirror channel: X)". Kept at full weight; never re-chartered
  to rescue it.
- U-NULL-FLOOR: "... the floor h exceeds the 8.5 percent band; no sign read; U-NULL-FLOOR. Grade D2 unchanged."
  A clean null, full credit.
- INSTRUMENT-OPEN: no rider on NUC-018; a line in the results file naming the credential that halted; no evidence
  read.

What moves. No grade: the Coulomb cell is D2 (exact given d0 = 2.026 fm, a measured scale) and every form leaves
it D2. None of the five numbers of NORTH_STAR 2b. Targets moved blocked to derived: 0; inputs retired: 0. The
result replaces one coefficient comparison with one measured bias on a calibration-free channel: reconstruction
work on a target row, and the release note says so in those words. It is not a T1 prediction (AME2012 masses
predate the model).

What it does NOT establish. Not the cause of a miss (self-energy, exchange, diffuseness, the odd nucleon's orbit,
charge-symmetry breaking: the Nolen-Schiffer literature names all of these and this design names none as found).
Not NUC-C's corrections (uncoded, unscored). Not the mass models' absolute accuracy (NUC-BLIND-2 and NUC-NEW-5
stand as they are). Not anything about A < 13, about T = 1 or T = 3/2 multiplets, or about any trend in A (no
trend statistic exists in this design; the per-pair table is published and a trend reading would be a new
commission with its own bars).

## 8. NOT ASSUMED

Not leaned on: the Director's registered expected form (U-MISS-HIGH by roughly 15 to 30 percent). Not leaned on:
the theorist's prior, stated for the record: from the public Nolen-Schiffer literature the Z^2 uniform sphere
overshoots displacement energies, more at light A; my prior is U-MISS-HIGH with a mean above the Director's band
at the light end; I have computed no measured value and no bar depends on either prior. Not assumed: that every
AME2012 row is experimental (the pin is the hash; the row count is diagnostic). Not assumed: that the Z^2 form is
the right form (it is the registered one; Z(Z - 1) is a diagnostic, not a model). Not assumed: that B1 is a
physical bar; it is the registry's own stated precision for the coefficient and the only provenance-honest band
available. Not assumed: charge symmetry of the non-Coulomb terms beyond what the registered models already impose
(their non-Coulomb terms depend on A and (N - Z)^2 only, which is what C-2 checks; nature's charge-symmetry
breaking, at the 100 keV class, sits inside h_inst's coarse floor and is one of the causes section 7 does not
adjudicate).

## 9. AUTONOMY AND COMPUTE

No step waits on a person: the table is in the repository under a pinned hash, the filter is deterministic, the
seed is fixed in this file; no draw is needed and no beacon round is committed (the rule selects every eligible
pair, so there is nothing to draw). The verdict runs once from the sealed checkpoint.

Compute: under one cpu-minute (a few thousand rows parsed, 10000 resamples of a few dozen numbers); memory under
100 MB; wall time seconds per unit; a 600 s timeout per unit is ample.

Instruments that exist: benchmarks/lab/nuc_new_5/driver.py (a_c(), binding(), CONFIG, sha256_file; imported
unchanged; credentialed under NUC-NEW-5) and benchmarks/lab/_kit/labkit.py (Driver, Checkpoint, Halt, Verdict).

The worker writes exactly two files, on the nuc_new_5 pair as template: benchmarks/lab/nuc_mirror_lean/driver.py
(units in the locked order: credential [C-1, C-2, C-3 on fixture T in a temporary directory]; evidence [C-4,
labels by the filter, C-5, the one read, delta_i, mean, rms, the diagnostic, h_boot, h_inst, h, all sealed]; done)
and benchmarks/lab/nuc_mirror_lean/verdict.py (reads the checkpoint only; applies section 4; prints one FORM line;
writes analysis/NUC_MIRROR_LEAN_results.md once, with the per-pair table A, Z_p, CDE_meas, CDE_U, delta_i, and
mean_delta, rms_delta, the diagnostic mean, h_boot, h_inst, h, n, the hashes). No build script, no hold-out
directory, no manifest file beyond labkit's own, no second model, no second question, no draw. The kit's charter
is a copy of this design with the lock date and the kit file hashes added, nothing else. Target size: the driver
under 200 lines, the verdict under 80.

## DISCLOSURES (the cures, by death)

1. NUC-MIRROR-CDE and NUC-MIRROR-COULOMB died because C-1 pinned a hand value 0.771605 at 1e-5 that the sealed
   code does not return. Cure: every constant that sealed code computes was read from the code by the scratch run
   (a_c() = 0.7716295256894924, d_n - d_h = 0.7823465499999998, the CDE_U, fixture and floor values); C-1 pins the
   code's own value at 1e-9 and checks the registered 0.7716 at 1e-4 as a diagnostic; no tolerance is tighter than
   the digits quoted.
2. NUC-MIRROR-DISPLACE died because the design task exceeded its budget. Cure: this design read one driver header,
   one prior design, one registry entry and two searches, ran one scratch script, and carries one model on one
   channel with one question.
3. NUC-CDE-UNIFORM and NUC-MIRROR-UNIFORM died because the worker did not finish the kit in 35 turns; the second
   of them was already uniform-only, so leanness of the model was not enough. Cure beyond that: the trend question
   (Spearman statistic, permutation null, third fixture) is dropped; the parser fixture and the form fixture are
   one fixture; the credentials are three halts, one hash check and one count; the kit is two files with a stated
   size target; the verdict has one FORM line. Nothing in the kit is new numerics: the filter, a mean, an rms, a
   bootstrap percentile.
4. The Director's three cures are in place: a_c() read from the code (section 3, C-1); uniform-sphere leg only,
   no NUC-C leg (section 3); the NUC-NEW-5 driver reused unchanged plus one filter (section 2), one bias/rms
   statistic and one pair-scatter floor test read before any sign (section 4, rule 1 before rules 3 and 4).

## DISCLOSURES, REVISION (the skeptical reviewer's objections, each: what changed)

5. "The band decision is not floor-protected; rules 2 to 4 render a side of B1 when the floor straddles it; the
   floor clears zero, not the threshold" (three objections on sections 4 and 6 and on exhaustiveness): section 4's
   rule replaced by the reviewer's ordering: (1) h > B1 U-NULL-FLOOR; (2) |mean_delta| + h <= B1 U-AGREES; (3)
   mean_delta - h > B1 U-MISS-HIGH; (4) mean_delta + h < -B1 U-MISS-LOW; (5) otherwise U-OPEN-BAND. The sentence
   "the floor is cleared by construction" is deleted; the floor paragraph now states that h is read against the
   band edge. The worked cases (0.08, 0.07) and (0.09, 0.07) both render U-OPEN-BAND by the scratch run. Section 6
   lists U-OPEN-BAND; section 7 gives it a rider (clean open, no sign claimed against the band). Section 1 names it
   below.
6. "C-3 must reach every form": section 5 C-3 now carries a fixture table of five payloads F1 to F5 on fixture T's
   eight labels (F3: CDE_meas = 1.2 CDE_U, delta = -1/6, U-MISS-LOW; F4: f alternating 0.05/0.11, mean 0.08, h_boot
   0.0225 from the code on seed 20261104, U-OPEN-BAND; F5: f alternating 0.0/0.5, h_boot 0.1875 > B1, U-NULL-FLOOR)
   and the four-pair table T4 that must raise the C-5 halt. Every expected value is the code's to 1e-9 (scratch
   analysis/lab/drafts/NUC-MIRROR-LEAN/scratch_fixtures.py); the bootstrap convention is written into section 4
   (default_rng, one rng.choice per resample, numpy.percentile default) so the worker's code reproduces them.
7. "U-AGREES wording": section 7 now states that agreement means |mean_delta| + h lies inside B1, that mean_delta is
   an equal-weight average over A, and that it says nothing about light-A versus heavy-A behaviour. The MISS
   wording states that the whole floor-widened interval lies outside the band.

Section 1 addendum: U-OPEN-BAND would say the channel resolves neither side of the 8.5 percent band at this n and
floor; it changes no claim's status and no grade, and is not re-chartered to rescue a side.
