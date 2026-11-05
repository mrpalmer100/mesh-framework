# NUC-MIRROR-LEAN-3: SEALED EVIDENCE DESIGN (the author's route; written before the kit is touched)

Commission NUC-MIRROR-LEAN-3, kind reconstruction, question key nuc-coulomb-mirror-displacement. The executor's
design on the author's instruction, 2026-11-05, the text of NUC-MIRROR-LEAN-2 (sealed 97d5d8f, 4 November; skeptical
pass at lock, external FAIL at lock) with two corrections and nothing else changed: the history below and in
DISCLOSURES 3 and 5 is told as it happened, and the kit is held to the read order this design already states.
NUC-MIRROR-LEAN-2 was itself NUC-MIRROR-LEAN (the lab's seventh design of this question, sealed f754186, skeptical
pass at design and at lock, external FAIL at lock) to the digit, cured on the three points its external reviewer
raised: the North Star section 5 line was missing, the words "the design does not know n; the build records it"
beside a stated expectation of about thirty pairs were read as a count taken from the evidence table before lock,
and standing bar W was argued away rather than met. This design keeps the question, model, statistic, bars and
fixtures to the digit (DISCLOSURES at the end). It is committed before the kit is touched; nothing below changes
afterwards; a change is a new name.

The inspection history of this evidence cell, exactly. No count of the T = 1/2 mirror pairs in
data/ame2012/AME2012.txt has ever been taken by anyone in the programme, and no mass of those rows has been read
for this question: NUC-MIRROR-LEAN never ran and its kit was never built (its worker parked the draft at lock);
NUC-MIRROR-LEAN-2 never ran (its worker parked the draft at lock; the only smoke ran on the synthetic fixture
F1 in a temporary directory). The "about thirty pairs (A = 13 to about 71)" in NUC-MIRROR-LEAN's design was the
theorist's expectation from the textbook fact that mirror pairs with both masses measured run to the mid-70s in
A; it was not read from the table, and no design since states any expectation of n. The table has been read by
locked sessions for other rows (the Ca-40 row by every registered model's calibration; NUC-026 in absolute masses
at 2398 nuclides; NUC-BLIND-1 and -2 hold-outs; NUC-NEW-5's audit), and section 2 records that; those reads do not
touch the statistic here, which the table's mirror rows alone decide. The bars, the floor rule, the band, the
bootstrap seed and the fixtures were fixed in NUC-MIRROR-LEAN's design (sealed f754186, round two) and have not
moved since. No mass value of the evidence cell was read while writing this and none will be read before the lock:
the executor's sandbox ran one scratch script that imported benchmarks/lab/nuc_new_5/driver.py unchanged and
opened no table and no checkpoint. Every number here is a registered number, a value returned by that sealed
code, stated arithmetic on those, or a synthetic fixture.

## 0. WHY

The weights-of-atoms row's Coulomb cell reads "Coulomb term derived from winding charge and spacing (+9%)". The
+9% is a coefficient comparison: the derived uniform-sphere a_C = 0.7716 MeV (NUC-018, NUC-031) against the
empirical SEMF coefficient 0.711 that NUC-018 compares it with. The term has never been scored on a measurement by
itself: in every mass confrontation (NUC-BLIND-1, NUC-BLIND-2, NUC-NEW-5) the calibrated bond depth a_V (Ca-40),
the surface term and the symmetry term carry most of the number. On one channel all three cancel exactly: the
binding difference of a T = 1/2 mirror pair at odd A, B(Z_p - 1, Z_p) minus B(Z_p, Z_p - 1) with Z_p = (A + 1)/2.
In the registered models (NUC-018 three-term; NUC-A plus NUC-B four-term) the volume term a_V A, the surface term
(a_S/a_V) a_V A^(2/3) and the symmetry term a_A (N - Z)^2/A, with (N - Z)^2 = 1 for both members, are identical for
the two members; neither model has a pairing term; what remains is a_C [Z_p^2 - (Z_p - 1)^2]/A^(1/3) = a_C A^(2/3),
because 2 Z_p - 1 = A. The Ca-40 calibration does not enter (C-2 verifies this on the sealed code). So the mirror
displacement energies score the derived Coulomb term alone.

North Star row: Weights of atoms, the Coulomb cell. Gear: depth; the lead is the cell's own registered miss
(NUC-018: 0.772 against 0.711) and the registry's silence on the mirror channel. It moves no target from blocked
to derived and retires no input, and says so (section 7, with the section 5 line).

## 1. THE QUESTION

Q1, the only question. Does the registered uniform-sphere Coulomb term, a_C = 0.7716295 MeV on Z^2/A^(1/3) with
a_C from d0 = 2.026 fm and no constant fitted to any mass, reproduce the measured Coulomb displacement energies of
the AME2012 T = 1/2 mirror pairs at A >= 13 to within the coefficient's own registered offset (B1 = 0.085,
section 4)? U-AGREES would upgrade the cell's evidence from "coefficient within 9 percent of the SEMF's" to
"confirmed on a calibration-free channel at 8.5 percent". U-MISS-HIGH or U-MISS-LOW would add to the cell, on this
channel, a measured bias with its sign. U-OPEN-BAND would say the channel resolves neither side of the band at this
n and floor. U-NULL-FLOOR would say the channel cannot resolve the band. No answer changes a claim's status or a
grade (section 7). There is no Q2.

## 2. THE EVIDENCE SET

The table. data/ame2012/AME2012.txt in the repository, sha256
88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the pin NUC-NEW-5 CONFIG carries as
pins['ame2012_sha256']; NUC-031 and NUC-032 carry the same), rows 'Z N M' with M the atomic mass excess in MeV,
the table the blind draws NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 treat as experimental. No other table.

The rule (the one filter; no choice left to anyone, no draw, nature's set). A pair is every odd A >= 13 with
Z_p = (A + 1)/2 such that BOTH rows (Z, N) = (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present in the table. A >= 13
because the registered models' domain is A >= 12 (NUC-NEW-5 CONFIG min_a = 12) and 13 is the smallest odd A in it.
No upper limit on A; no other exclusion. Rows are parsed exactly as ca40_binding_from() parses them: a line splits
into three tokens, Z and N compared as integer strings, M read as float. NOBODY KNOWS n BEFORE THE RUN: this design
does not state it, the kit does not count it, the charter does not disclose it; the evidence unit records n at run
time and applies the count rule of section 4. The executor's expectation, stated and not leaned on: a few dozen
pairs.

Bar W, met as NUC-NEW-5 met it. The sector carries a calibration against a measured table (a_V on Ca-40), so the
standing blind hold-out bar applies as written: the test set is selected by a process other than the commission
(here the deterministic rule above on a table pinned by hash: nature's set, no seed, no choice), and the
prediction is frozen before the held-out values are read: the predict unit writes CDE_U(A) = a_c() A^(2/3) for
every odd A from 13 to 299 to analysis/NUC_MIRROR_LEAN_3_pred.txt, seals the array and records the file's sha256,
BEFORE the evidence unit opens the table; the evidence unit must reproduce the sealed file's hash and reads the
predictions it scores from that sealed array, never recomputing them. A model that cannot be re-fit after the
table is read (there is no constant in CDE_U to fit) is the bar's purpose, and the construction makes it a check
rather than an argument.

The one read. The evidence unit re-checks the file's sha256 against the pin, forms the label list (ascending A),
reads M for exactly the 2n labelled rows into one raw array that is sealed (sha256 of its bytes) before any
statistic is formed. Every later number derives from that one payload. The driver never prints a mass, a
displacement energy, a delta, a mean or n; the verdict prints the FORM line once (labkit's rule).

What the programme has and has not inspected, plainly. AME2012 as a whole has been inspected many times in
absolute masses (NUC-026 at 2398 nuclides; NUC-BLIND-1 and -2 drew hold-outs from it; NUC-NEW-5's audit read it).
The Coulomb displacement channel has never been formed, scored or printed in the registry or in any analysis
file; no constant of the model was fitted to any AME2012 mass except a_V on Ca-40, which cancels identically in
this channel. The channel is a confrontation of a frozen function with differences the programme never formed;
the record cannot externally verify the non-formation and the rider says so by its wording (section 7).

## 3. THE MODELS OR PREMISES

Frozen as registered, imported unchanged from benchmarks/lab/nuc_new_5/driver.py (the credentialed NUC-NEW-5
instrument; its a_c() and binding() are NUC-BLIND-1's constants, credentialed there by C-1 byte equality):

- a_c() = coulomb_factor / (r0_over_d0 * d0_fm), CONFIG coulomb_factor = 0.6 * 1.44 = 0.864 MeV fm, d0_fm = 2.026
  (NUC-017, adopted by NUC-018), r0_over_d0 = (3/(4 pi sqrt 2))^(1/3). THE SEALED CODE RETURNS a_c() =
  0.7716295256894924 MeV (scratch run; r0_over_d0 = 0.5526694571400057). The registry quotes 0.7716 (NUC-031) and
  0.772 (NUC-018); both agree with the code at the digits they quote. No hand value is used anywhere.
- The channel model: CDE_U(A) = a_c() * A^(2/3) MeV, the exact difference binding(A, Z_p - 1, ...) minus
  binding(A, Z_p, ...) for any (a_V, a_S/a_V, a_A) (C-2). Code values: A = 13, 4.266166; 17, 5.101620; 21,
  5.873384; 25, 6.597340; 33, 7.938738; 45, 9.762263; 61, 11.957179; 75, 13.723019 MeV.
- The measured channel: CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p), with d_n - d_h from CONFIG
  (code: 0.7823465499999998 MeV). This is B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) in the driver's own
  binding-from-excess convention (ca40_binding_from: B = Z d_h + N d_n - M).

Nothing is calibrated and nothing is re-fit. NUC-C (diffuseness and exchange) is NOT scored: it has no code in the
repository. The self-energy variant Z(Z - 1), i.e. CDE_U (1 - 1/A), is reported as one diagnostic line, no form.

## 4. THE STATISTICS AND BARS

For pair i (ascending A): delta_i = CDE_U(A_i) / CDE_meas,i - 1 (the fractional miss; positive means the sphere
overshoots). Recorded: mean_delta = (1/n) sum delta_i (equal weight per pair; the statistic Q1 is decided on);
rms_delta; min and max delta_i with their A; the diagnostic mean of delta'_i = CDE_U(A_i)(1 - 1/A_i)/CDE_meas,i - 1
(no form).

Floor. Two half-widths on mean_delta; the larger is the floor h:
- h_boot, the pair-scatter floor: bootstrap over pairs, 10000 resamples, seed 20261104, h_boot = the 99.0th
  percentile of |mean(delta*) - mean_delta| (resamples and percentile as NUC-NEW-5 CONFIG floor_resamples = 10000,
  floor_percentile = 99.0). The convention, fixed so C-3's fixture values reproduce to 1e-9: rng =
  numpy.random.default_rng(20261104); for each of the 10000 resamples, one call s = rng.choice(delta, size=n,
  replace=True) on the delta array in ascending-A order, dev = |mean(s) - mean_delta|; h_boot =
  numpy.percentile(dev, 99.0) with the default (linear) method.
- h_inst, the measurement allowance from a disjoint resource: NUC-NEW-5's registered mass tolerance class
  audit_tol_MeV = 0.100 per mass, sqrt 2 times that per difference, divided by the smallest model CDE in the domain,
  CDE_U(13) (the largest fractional sensitivity any pair can have, since CDE_U grows with A; to first order in the
  miss d delta / d CDE_meas = -1/CDE_meas), divided by sqrt n: h_inst = 0.1 sqrt 2 / CDE_U(13) / sqrt n =
  0.03314952113422842 / sqrt n (code value of the numerator). Said plainly: the AME2012 rows carry no uncertainty
  column in this table and 0.100 MeV is a tolerance class, not a per-mass standard deviation; the allowance treats
  the 2n mass errors as independent, which is why it is the larger-sensitivity, per-pair-worst construction; a
  coherent (common-mode) contribution to the channel such as charge-symmetry breaking of the nuclear force is NOT
  an error of measurement and is not in the floor: it is part of what the channel measures, and section 7's
  wording scores the uniform sphere against the measured displacement energies as they are, with that named as
  one of the causes the commission does not adjudicate.
h = max(h_boot, h_inst), computed inside the evidence unit from the sealed payload and sealed with it, read before
any sign is read, and read against the band edge, not against zero (house discipline 5: the effect scored here is
band membership, so the floor must clear the distance to B1).

Band B1 = 0.085: the coefficient's own registered offset, a_c()/0.711 - 1 = 0.08527 (code; NUC-018's derived
0.772 against the empirical 0.711, the scorecard's "+9%"), rounded to three figures. Fixed here from the registered
comparison, not from the cell.

Q1 rule, in this order (the first rule that holds decides):
1. h > B1: U-NULL-FLOOR (the floor is wider than the band; no sign is read).
2. |mean_delta| + h <= B1: U-AGREES (the whole floor-widened interval lies inside the band; an interval whose edge
   touches B1 from inside is inside).
3. mean_delta - h > B1: U-MISS-HIGH (the whole interval lies above the band).
4. mean_delta + h < -B1: U-MISS-LOW (the whole interval lies below the band).
5. Otherwise: U-OPEN-BAND (the floor straddles or touches a band edge from outside; no side is read). The
   diagnostic flag sign_resolved = |mean_delta| > h is recorded under every form and decides nothing.
Worked cases (scratch): mean 0.08 with h 0.07 and mean 0.09 with h 0.07 both render U-OPEN-BAND.

Count halt. n < 5 halts the evidence unit (INSTRUMENT-OPEN, before any M is read). Provenance: the bootstrap's
99th percentile needs at least 100 distinct resamples to be resolvable at the 1 percent level; the number of
distinct bootstrap samples of n items is C(2n - 1, n), 126 at n = 5 and 35 at n = 4. n is recorded whatever it is.
No other threshold exists; nothing is set after a preview, because there is no preview.

## 5. THE CREDENTIALS

All in the credential unit, run before the predict and evidence units; each halt-grade unless marked diagnostic. A
halt renders INSTRUMENT-OPEN and the evidence is never read.

- C-1 (halt): the imported a_c() equals 0.7716295256894924 to 1e-9. Diagnostic lines: |a_c() - 0.7716| < 1e-4 (the
  registered digits, NUC-031); CONFIG d0_fm = 2.026 and coulomb_factor = 0.864 to 1e-12; d_n - d_h = 0.78234655 to
  1e-8.
- C-2 (halt): the cancellation identity on the sealed binding(): for A in {13, 17, 21, 25, 33, 45, 61, 75},
  Z = (A - 1)/2, and the three triples (a_V, a_S/a_V, a_A) = (15.0, 1.34, 0.0), (17.77, 1.108, 19.85),
  (16.21, 1.34, 19.85): |binding(A, Z, ...) - binding(A, Z + 1, ...) - a_c() A^(2/3)| < 1e-9 (scratch: worst 3.0e-14).
- C-3 (halt): the filter, the statistic, the floor and the form rule on synthetic 'Z N M' tables written to a
  temporary directory (never under data/), with the same functions the evidence unit calls and no fixture-specific
  branch. Fixture T: planted pairs at A = 13, 17, 21, 25, 33, 45, 61, 75 (Z_p = 7, 9, 11, 13, 17, 23, 31, 38), each
  with M(Z_p - 1, Z_p) = 0 and M(Z_p, Z_p - 1) = CDE_U(A)/(1 + f_i) - (d_n - d_h) written with repr(float(M)), f_i
  the planted fractional miss per pair in ascending A; and distractors with M = 0: (6, 5) with (5, 6) [A = 11,
  below the domain]; (8, 7) alone [A = 15, partner absent]; (9, 6) with (6, 9) [A = 15, T_z = 3/2]; (20, 20);
  (8, 8). Labels must be exactly the eight planted pairs, ascending A, n = 8. Payloads and their expected values
  (the code's, scratch run; pinned halt-grade at 1e-9 unless stated; h_inst = 0.03314952113422842/sqrt 8 =
  0.011720125593549844 for all):

  | payload | f_i (ascending A) | mean_delta | h_boot | h | form |
  |---|---|---|---|---|---|
  | F1 | 1/0.9 - 1 for all (CDE_meas = 0.9 CDE_U) | 0.111111111111111 | 0 (to 1e-12) | 0.011720125593549844 | U-MISS-HIGH |
  | F2 | 0 for all | 0.0 | 0 (to 1e-12) | 0.011720125593549844 | U-AGREES |
  | F3 | 1/1.2 - 1 for all (CDE_meas = 1.2 CDE_U) | -0.166666666666667 | 0 (to 1e-12) | 0.011720125593549844 | U-MISS-LOW |
  | F4 | 0.05, 0.11 alternating (A = 13: 0.05) | 0.08 | 0.0225 | 0.0225 | U-OPEN-BAND |
  | F5 | 0.0, 0.5 alternating (A = 13: 0.0) | 0.25 | 0.1875 | 0.1875 | U-NULL-FLOOR |
  | T4 | F1's rows at A = 13, 17, 21, 25 only, plus the distractors | n = 4 | | | C-5 halt before any M is read |

  F4 decides by rule 5 (|mean| + h = 0.1025 > B1 and mean - h = 0.0575 < B1); F5 by rule 1 (h = 0.1875 > B1); F3
  by rule 4 (mean + h = -0.15494654 < -B1). C-3 passes only when all six expectations hold.
- C-4 (halt): before the evidence unit, sha256(data/ame2012/AME2012.txt) equals the pin in section 2. Diagnostic:
  the row count (recorded, not gated, and not printed by the driver).
- C-5 (halt): n >= 5, inside the evidence unit, before any M is read.
- C-6 (halt): the evidence unit reproduces the predict unit's sealed prediction file hash and finds every scored
  A in the sealed prediction array (bar W's binding).
- Manifest: labkit's manifest of the locked files (this design, the two kit files, benchmarks/lab/nuc_new_5/driver.py,
  benchmarks/lab/_kit/labkit.py, data/ame2012/AME2012.txt) taken at the first unit and re-verified at every later one.

Smoke (LAB_SMOKE=1): every unit in one process; the credential unit on the fixtures as in evidence; the predict unit
on the same frozen function (its file written under benchmarks/lab/nuc_mirror_lean_3/scratch/, never analysis/);
the evidence unit on fixture T's F1 table in a temporary directory (checkpoint analysis/nuc_mirror_lean_3_smoke.pkl);
the verdict withholds all forms in smoke. The smoke never opens data/ame2012/AME2012.txt and never touches the
evidence checkpoint.

## 6. THE FORMS

Q1, exhaustive, decided by section 4 alone: U-AGREES; U-MISS-HIGH; U-MISS-LOW; U-OPEN-BAND; U-NULL-FLOOR;
INSTRUMENT-OPEN (any halt, any exception, any credential failure, n < 5). Exactly one is rendered: rules 1 to 5
partition every (mean_delta, h) with h >= 0. INSTRUMENT-OPEN's reason names the unit that halted (credential,
predict or evidence), so a halt before any evidence was read is distinguishable from one after it; the results file
says which.

## 7. WHAT COUNTS

Each form yields one rider on NUC-018 (and a line in the Coulomb cell of NORTH_STAR section 2), worded:

- U-AGREES: "NUC-MIRROR-LEAN-3 (date, analysis/NUC_MIRROR_LEAN_3_results.md): the derived uniform-sphere Coulomb
  term, a_C = 0.7716 MeV from d0 = 2.026 fm with no constant fitted to a mass, scored on the n AME2012 T = 1/2 mirror
  displacement energies at A >= 13, the channel in which the calibrated bond depth, the surface term and the
  symmetry term cancel exactly, the predictions sealed before the table was read: mean fractional miss X, rms Y
  (floor h); the floor-widened interval |X| + h lies inside the coefficient's registered 8.5 percent band B1;
  U-AGREES. X is an equal-weight average over the pairs and says nothing about the light-A versus heavy-A
  behaviour, which this commission does not read; the measured displacement energies carry whatever
  charge-symmetry breaking nature puts in them, unadjudicated here. The channel's blindness rests on the
  programme's non-formation of the differences, which the record cannot externally verify. Grade D2 unchanged."
- U-OPEN-BAND: the same sentence with "mean fractional miss X, rms Y (floor h); the floor straddles the edge of the
  8.5 percent band; no side of the band is read and no sign is claimed against it; U-OPEN-BAND. Grade D2
  unchanged." A clean open result, full credit; the per-pair table is published.
- U-MISS-HIGH / U-MISS-LOW: the same sentence with "mean fractional miss X, rms Y (floor h); the whole floor-widened
  interval lies outside the registered 8.5 percent band; U-MISS-<HIGH/LOW>: on the calibration-free channel the
  uniform sphere <overshoots/undershoots> the measured displacement energies by X; the cell's '+9%' is a
  coefficient comparison and this is the term's own miss. Grade D2 unchanged." The cell's text gains "(mirror
  channel: X)". Kept at full weight; never re-chartered to rescue it.
- U-NULL-FLOOR: "... the floor h exceeds the 8.5 percent band; no sign read; U-NULL-FLOOR. Grade D2 unchanged."
- INSTRUMENT-OPEN: no rider on NUC-018; a line in the results file naming the unit that halted and whether any
  evidence had been read.

What moves. No grade: the Coulomb cell is D2 (exact given d0 = 2.026 fm, a measured scale) and every form leaves
it D2. None of the five numbers of NORTH_STAR 2b. Targets moved blocked to derived: 0; inputs retired: 0;
discriminators armed: 0. The result replaces one coefficient comparison with one measured bias on a
calibration-free channel: reconstruction work on a target row, and the release note says so in those words. It is
not a T1 prediction (AME2012 masses predate the model).

THE SECTION 5 LINE. This commission names none of (a), (b), (c): it is interior work under NORTH_STAR section 5.
It is permitted as written: the last locked session, NUC-NEW-5 (locked 6e7a56a on 2026-10-31, verdict
BLIND-AGREES / EXTRAPOLATES, promoted as NUC-031 in PR #11 on 2026-11-01), was target-facing, and no interior
session has locked since (NUC-MIRROR-LEAN and NUC-MIRROR-LEAN-2 were withdrawn before any lock and are not
sessions). The session after this one must be target-facing. The author's recorded reading of this commission against section 5 and bar W is
in NORTH_STAR section 5 under this name.

What it does NOT establish. Not the cause of a miss (self-energy, exchange, diffuseness, the odd nucleon's orbit,
charge-symmetry breaking: the Nolen-Schiffer literature names all of these and this design names none as found).
Not NUC-C's corrections (uncoded, unscored). Not the mass models' absolute accuracy (NUC-BLIND-2 and NUC-NEW-5
stand as they are). Not anything about A < 13, about T = 1 or T = 3/2 multiplets, or about any trend in A (no trend
statistic exists in this design; the per-pair table is published and a trend reading would be a new commission
with its own bars).

## 8. NOT ASSUMED

Not leaned on: the Director's registered expected form for NUC-MIRROR-LEAN (U-MISS-HIGH by roughly 15 to 30
percent). Not leaned on: the executor's prior, stated for the record: from the public Nolen-Schiffer literature the
Z^2 uniform sphere overshoots displacement energies, more at light A; the prior is U-MISS-HIGH; no measured value
has been computed and no bar depends on the prior. Not assumed: that every AME2012 row is experimental (the pin is
the hash; the row count is diagnostic). Not assumed: that the Z^2 form is the right form (it is the registered one;
Z(Z - 1) is a diagnostic, not a model). Not assumed: that B1 is a physical bar; it is the registry's own stated
precision for the coefficient and the only provenance-honest band available. Not assumed: charge symmetry of the
non-Coulomb terms beyond what the registered models already impose (their non-Coulomb terms depend on A and
(N - Z)^2 only, which is what C-2 checks).

## 9. AUTONOMY AND COMPUTE

No step waits on a person: the table is in the repository under a pinned hash, the filter is deterministic, the
seed is fixed in this file; no draw is needed and no beacon round is committed. The verdict runs once from the
sealed checkpoint.

Compute: under one cpu-minute; memory under 100 MB; wall time seconds per unit; a 600 s timeout per unit is ample.

Instruments that exist: benchmarks/lab/nuc_new_5/driver.py (a_c(), binding(), CONFIG, sha256_file; imported
unchanged; credentialed under NUC-NEW-5) and benchmarks/lab/_kit/labkit.py (Driver, Checkpoint, Halt, Verdict).

The kit, written by the executor after this design is committed, on the nuc_new_5 pair as template:
benchmarks/lab/nuc_mirror_lean_3/driver.py (units in the locked order: credential [C-1, C-2, C-3 on the fixtures in
a temporary directory]; predict [the sealed prediction file, bar W]; evidence [C-4, labels by the filter, C-5, C-6,
the one read, delta_i, mean, rms, the diagnostic, h_boot, h_inst, h, all sealed]) and
benchmarks/lab/nuc_mirror_lean_3/verdict.py (reads the checkpoint only; applies section 4; prints one FORM line;
writes analysis/NUC_MIRROR_LEAN_3_results.md once, with the per-pair table A, Z_p, CDE_meas, CDE_U, delta_i, and
mean_delta, rms_delta, the diagnostic mean, h_boot, h_inst, h, n, the hashes). The lab's worker files it under
author-kit mode: runs the smoke and the fixtures, checks the bars against this design, files it unchanged.

## DISCLOSURES (the cures, by death)

1. NUC-MIRROR-CDE and NUC-MIRROR-COULOMB died because C-1 pinned a hand value the sealed code does not return.
   Cure (kept from NUC-MIRROR-LEAN): every constant that sealed code computes was read from the code by a scratch
   run; C-1 pins the code's own value at 1e-9; no tolerance is tighter than the digits quoted.
2. NUC-MIRROR-DISPLACE died of its design budget; NUC-CDE-UNIFORM and NUC-MIRROR-UNIFORM died of the worker's turn
   limit. Cure (kept): one model, one channel, one question, two kit files, no trend statistic.
3. NUC-MIRROR-LEAN died at lock on three objections of the external reviewer: (i) no North Star section 5 line:
   cured by section 7's SECTION 5 LINE and the author's reading recorded in NORTH_STAR under this name; (ii) the
   words "the design does not know n; the build records it" beside a stated expectation of about thirty pairs,
   read by the reviewer as a count taken from the evidence table before lock (no count was taken; the header
   above tells the inspection history exactly): cured by section 2, nobody counts before the run, the design and
   the charter state no n and no expectation of n, and the kit is credentialed on fixtures whose n the fixtures
   plant; (iii) bar W argued away by the cancelling calibration: cured by section 2, the
   predictions are written and sealed before the table is read and the evidence unit is bound to them (C-6), and
   the set is nature's by a deterministic rule on a pinned table, as NUC-NEW-5's was. The reviewer's fourth point,
   the measurement floor, is answered in section 4 by saying exactly what h_inst is and is not and by putting a
   coherent charge-symmetry-breaking contribution where it belongs, in the measured channel and in the rider's
   wording, not in the floor; the author's reading of item E for this commission is recorded in NORTH_STAR
   section 5 beside the section 5 reading. The reviewer's fifth point, INSTRUMENT-OPEN not distinguishing a halt
   before evidence from one after, is cured in section 6.
4. The skeptical reviewer's round-one objections to NUC-MIRROR-LEAN (the floor-protected band rule, a fixture for
   every form, the U-AGREES wording) are kept as that design's round two left them.
5. NUC-MIRROR-LEAN-2 died at lock on two objections of the external reviewer (skeptical pass). (i) Its charter
   repeated the reviewer's reading of (3)(ii) as history, "a pair count taken from the evidence table at build
   time", and elsewhere stated that no cell was ever counted; the two cannot both stand. The executor wrote the
   false one: no count was ever taken, and this design's header says what was inspected and when the bars were
   fixed. Nothing is argued from a fresh sandbox; the cell is uninspected because nobody has read it, not because
   a sandbox was reset. (ii) Its kit converted every mass token in the table to float while parsing, before the
   labels were formed and the count rule applied, so T4 proved only that a halt was raised, not that it was raised
   before any M was read as section 2 and C-5 state. Cured in the kit, not in this text (the read order here is
   unchanged): the parser keeps the tokens, the labels and the count rule and the prediction coverage are applied
   to the tokens, and only the 2n selected tokens are converted; the row count comes from that same pass; a
   conversion counter in the kit records every float conversion of a mass token, and T4 passes only when the C-5
   halt is raised with the counter at zero. Re-credentialed on the synthetic fixtures only.
