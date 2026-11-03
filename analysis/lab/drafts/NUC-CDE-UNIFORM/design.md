# NUC-CDE-UNIFORM: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission NUC-CDE-UNIFORM, kind discriminator, question key nuc-coulomb-mirror-displacement. Theorist's design,
2026-11-03. The fourth design of this question and the first lean one: NUC-MIRROR-CDE and NUC-MIRROR-COULOMB were
abandoned by the worker because their halt-grade credential C-1 pinned a hand-computed a_C (0.771605, cube root
0.552687) that the sealed code does not return; NUC-MIRROR-DISPLACE was abandoned because the design task ran out
of budget. None of the three was a try; no evidence was ever read. This file is committed before the kit exists;
nothing below changes afterwards; a change is a new name. No mass value of the evidence cell was read while
writing it. Every number here is a registered number, a value returned by the sealed code (quoted from the scratch
run analysis/lab/drafts/NUC-CDE-UNIFORM/scratch_constants.py, which imports the driver and opens no table), stated
arithmetic on those, or a synthetic fixture. The cures are in the DISCLOSURES section at the end.

## 0. WHY

The Director's proposal, in my words. The weights-of-atoms row carries two frozen mass models: M1 (NUC-018's
three-term form, a_S/a_V = 1.34, a_V = 17.770286909889982 MeV) and M2 (the four-term form with NUC-A plus NUC-B's
a_A = 19.85 MeV, a_S/a_V = 1.108, a_V = 15.987072226683638 MeV), both calibrated on AME2012's Ca-40 and byte-bound
by NUC-032. They have been scored only on absolute masses (NUC-BLIND-1, NUC-BLIND-2, NUC-NEW-5), where the
calibrated constant, the surface term and the symmetry term carry most of the number and the derived Coulomb term
is a correction whose coefficient the registry records as 9 percent high (NUC-018: a_C = 0.7716 MeV against the
SEMF's empirical 0.711). On one channel every other term cancels identically: the binding difference of a T = 1/2
mirror pair, B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) at odd A. In both models the volume term a_V A, the surface term
(a_S/a_V) a_V A^(2/3) and the symmetry term a_A (N-Z)^2/A (with (N-Z)^2 = 1 for both members) are identical for the
two members; neither model has a pairing term; what remains is the Coulomb term alone, and the Ca-40 calibration
does not enter (section 5, C-2, proves this on the sealed code rather than on this paragraph). So the mirror channel
scores the derived, zero-constant Coulomb term by itself. The registry has never formed this difference (the
Director's search and the three earlier designs found no mirror-pair reading anywhere in the corpus).

North Star row served: Weights of atoms (docs/NORTH_STAR.md section 2), the cell "Coulomb term derived from winding
charge and spacing (+9%)". Rule of section 5: this charter names (c), a discriminator: it arms and adjudicates the
mirror-channel test of the sealed Coulomb form, and reads whether a miss is flat in A (a coefficient miss) or grows
with A (a shape miss). It moves no target from blocked to derived and retires no input; section 7 says so in those
words.

Gear: depth, by the Director's ruling (nothing is ready on the other rows: derivations are on hold, FND-106 waits on
external lattice data, GRV-EFE has no credentialed sealed input, the magnets lineages are blocked). The lead it
follows is the Director's own, the three unlocked designs of this question, whose cured content is the one thing on
the board that is measurable now. Leg U only: the uniform-sphere term of M1 and M2. The NUC-C leg (diffuseness plus
exchange, NUC-C) is dropped: the Director's condition for keeping it was that NUC-C's registered driver exposes its
Coulomb function for an unchanged import, and the earlier design's finding stands that NUC-C's code is not in the
repository (it ran in-package; nothing under benchmarks/ carries it), so no unchanged import exists and a new
integrator would need its own credential. That is a separate commission under a new name, if ever.

Read for this design: claims NUC-018 and NUC-032 in full; benchmarks/lab/nuc_new_5/driver.py lines 1 to 130 (the
CONFIG and the model functions); the withdrawn design analysis/lab/drafts/NUC-MIRROR-COULOMB/design.md sections 0
to 3 (which the worker reported built and smoked cleanly apart from C-1); the scratch run above.

## 1. THE QUESTION

Q1 (the Coulomb term as sealed, on the mirror channel). Does the uniform-sphere Coulomb term of M1 and M2 (form
F-U: E_C = a_C Z^2 / A^(1/3), a_C = a_c() = 0.7716295256894924 MeV) reproduce the measured Coulomb displacement
energies of the T = 1/2 mirror pairs of AME2012 at the coefficient's own registered precision (a mean fractional
bias within 0.0853; section 4)? U-AGREES upgrades the cell's evidence from "coefficient within 9 percent of the
SEMF's" to "within its registered precision on a calibration-free channel". U-MISS-HIGH or U-MISS-LOW names the
sealed Coulomb term, with its sign, as the registered miss on that channel. The two open forms (section 6) record
that the pairs' scatter did not permit a reading. No answer changes any claim's status or any grade.

Q2 (coefficient or shape). Is the fractional residual of F-U monotone in A above a permutation null? TREND-RISES or
TREND-FALLS says the A^(2/3) shape of the sealed term is wrong on this channel, not only its coefficient (a
coefficient miss alone is flat in A, since CDE_U(A) = a_C A^(2/3) exactly and a different r0 rescales every pair by
the same factor). TREND-FLAT says the shape is consistent with the pairs and any miss is a coefficient miss.
Q2 informs the "Blocked by" cell's wording; it moves nothing.

What no answer changes: the grade of the row (D3), the status of NUC-018, NUC-A, NUC-B or NUC-C, the five numbers of
NORTH_STAR section 2b, the shell, pairing and light-isotope cells, and the absolute-mass results (NUC-BLIND-1/2,
NUC-NEW-5), which scored the whole model and stand as scored.

## 2. THE EVIDENCE SET

The table. data/ame2012/AME2012.txt in the repository, sha256
88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the pin CONFIG['pins']['ame2012_sha256'] of
benchmarks/lab/nuc_new_5/driver.py, carried by NUC-NEW-5 and NUC-032), data rows 'Z N M' with M the mass excess in
MeV, the table NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 treat as experimental. No other table is used; nothing waits
on a publication or a person.

The rule (the build script tools/mirror_pairs.py, written by the worker to this rule, no choice left to it): a pair
is every odd A >= 13 (the models' registered domain is A >= 12, CONFIG min_a = 12; 13 is the smallest odd A in it)
with Z_p = (A+1)/2 such that BOTH rows (Z = Z_p, N = Z_p - 1) and (Z = Z_p - 1, N = Z_p) are in the table. No upper
limit on A; no exclusion by any other criterion; the rule selects what is there. The build reads the Z and N columns
only, never prints or stores a mass, writes analysis/holdout/NUC_CDE_UNIFORM/labels.txt ('A Z_p' rows, ascending A)
and MANIFEST.json (the AME2012 sha256, the labels sha256, the count n, the rule, the time), and refuses to overwrite.
Pinned by this design: the AME2012 hash and the rule. Recorded by the build, read by the manifest unit and never
trusted beyond equality with the build's record: the labels hash and n (this design does not know n).

The quantity scored, read once. For pair i, the measured Coulomb displacement energy
    CDE_meas,i = [M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p)] + (d_n - d_h),
with d_n = 8.07131714 and d_h = 7.28897059 MeV (CONFIG d_n, d_h of the driver), d_n - d_h = 0.78234655 MeV (the
code's own difference, scratch run). This equals B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) exactly, since B = Z d_h + N d_n - M.
The truth unit reads the two M values of every labelled pair once, seals the array, and nothing else reads the
table. The sealed prediction for every pair, from the sealed binding() with each model's sealed a_V (C-2 proves the
two models and any a_V give the same number):
    CDE_U(A) = a_c() [Z_p^2 - (Z_p - 1)^2] / A^(1/3) = a_c() (2 Z_p - 1) / A^(1/3) = a_c() A^(2/3).
Values the code returns (scratch run): 4.266165887 MeV at A = 13, 9.174831035 at A = 41, 13.723019467 at A = 75.

What the programme has and has not inspected, plainly. AME2012 is public and the programme has read it as ABSOLUTE
masses many times (NUC-005, NUC-018, the two 50-row blind draws, the whole-table regressions NUC-026/027); most
members of these pairs are in those readings. The programme has never formed a mirror difference and no registered
quantity was fitted to one: the Coulomb term's inputs are the winding charge (GG-006) and the spacing d0 = 2.026 fm
from the saturation density (NUC-017), not a mass. This is a calibration-free channel scored on a public table, NOT
a blind hold-out under NORTH_STAR section 5's bar W (bar W binds a model's calibration against the table; the
calibration cancels here). No rider will use the word blind. The AME2012 file carries no uncertainty column, so the
measurement error of each pair is not scored; the mirror masses at A <= 41 are known to well under 1 percent of the
displacement energy, and the bar of section 4 (8.53 percent on the mean) is far above any measurement error in the
set, so the omission cannot manufacture or hide a verdict. Expected size, for the record and not as a pin: at most
about 32 pairs (A = 13 to about 75). The halt-grade count floor is 15 (C-5): the pairs A = 13 to 41 (N-13/C-13
through Sc-41/Ca-41) are textbook nuclides in every evaluation for decades; a build that finds fewer has misparsed
the table. The floor is a misparse detector, not a statistical bar.

## 3. THE MODELS OR PREMISES

F-U, frozen as registered and sealed (NUC-018; constants carried by NUC-032; code benchmarks/lab/nuc_new_5/driver.py
functions a_c(), binding(), calibrate(), ca40_binding_from(), imported unchanged with CONFIG d0_fm = 2.026,
coulomb_factor = 0.6 x 1.44 = 0.864). a_C = 0.864 / r0, r0 = (3 / (4 pi sqrt 2))^(1/3) d0. The sealed code returns
(scratch run, quoted to the digits returned): (3 / (4 pi sqrt 2))^(1/3) = 0.5526694571400057, r0 = 1.1197083201656515 fm,
a_c() = 0.7716295256894924 MeV. Hand check: 4 pi sqrt 2 = 17.771532; 3 / 17.771532 = 0.1688097; cube root 0.552669;
0.864 / 1.119708 = 0.771630; consistent with the registered four-digit 0.7716 (NUC-018, NUC-032). The earlier designs'
0.552687 and 0.771605 were wrong in the fifth digit; no registered number is contradicted. M1 and M2 differ only in
terms that cancel on this channel; both are run through binding() so that the cancellation is a measured fact of the
kit, not an assumption. Nothing is calibrated, re-fit or re-derived here: a_V is read from the Ca-40 calibration only
to prove (C-3) that the imported driver is the sealed one, and then cancels.

NUC-C (diffuseness and exchange) is not instantiated: section 0.

## 4. THE STATISTICS AND BARS

Per pair i: the fractional residual f_i = (CDE_U(A_i) - CDE_meas,i) / CDE_meas,i (positive means the sealed term
overpredicts). Statistics: n; the mean bias b = mean_i f_i; the rms r = sqrt(mean_i f_i^2); the Spearman rank
correlation rho_A of f_i with A_i; and the two floors below. The verdict prints n, b, r, rho_A, the floor, the
permutation percentile, and the per-pair table (A, Z_p, CDE_meas, CDE_U, f), once.

Bar B1 (Q1), bias: |b| <= 0.0853. Provenance: a_c() / 0.711 - 1 = 0.0852736 (scratch run; the code's coefficient over
the SEMF empirical a_C = 0.711 MeV that NUC-018 records against it), rounded to four digits; the coefficient's own
registered offset, so U-AGREES means "no worse on this channel than the registry already says of the coefficient".
Not from the cell; fixed before any pair is read.

Floor F1 (Q1), the pair-scatter floor, computed on the sealed residuals before any sign is read: centre the residuals,
g_i = f_i - b; draw 10000 bootstrap resamples of size n with replacement from {g_i} with numpy's default_rng seeded
20261103; F1 = the 99th percentile of |mean of a resample|. F1 is what the pairs' scatter alone, with no bias, puts on
the mean. A sign is read only if |b| > F1. Power: the design can only call U-AGREES when F1 <= 0.0853, i.e. when a
miss of the bar's size would have been seen.

Bar B2 (Q2), trend: |rho_A| > P2, with P2 the 99th percentile of |rho| over 10000 random permutations of the f_i
against the fixed A_i (default_rng seeded 20261103, drawn after F1 from the same generator, in that order). The sign
of rho_A gives the direction. Provenance: a permutation null at the house percentile; no number from the cell.

Halt bars (section 5): n >= 15; a_c() to 1e-9; cancellation to 1e-9 MeV; a_V to 1e-9 MeV; the fixture plants to 1e-9
on b and the pre-stated forms.

## 5. THE CREDENTIALS

All credentials run before any evidence file is opened; each is halt-grade (INSTRUMENT-OPEN for Q1 and Q2) unless
marked diagnostic.
C-1 (the sealed constant, halt): the imported a_c() equals 0.7716295256894924 to 1e-9 MeV; CONFIG d0_fm = 2.026,
    coulomb_factor = 0.864 (to 1e-12), d_n = 8.07131714, d_h = 7.28897059; CONFIG['pins']['ame2012_sha256'] equals
    the hash in section 2. The tolerance 1e-9 is on the code's own value, not on a hand restatement (the cure).
    Diagnostic: r0 = 1.1197083 fm to 1e-6, printed.
C-2 (the cancellation, halt): for every odd A from 13 to 75 and each of M1 and M2 with its sealed a_V
    (17.770286909889982 and 15.987072226683638 MeV, NUC-032) and also with a_V = 1.0,
    |binding(A, Z_p - 1, a_V, ...) - binding(A, Z_p, a_V, ...) - a_c() A^(2/3)| < 1e-9 MeV. The scratch run found the
    worst case below 1e-12, so the bar is three orders loose of the code's own behaviour and tight against any
    model edit.
C-3 (the sealed driver, halt): calibrate(ca40_binding_from(AME2012), model) returns each model's sealed a_V above to
    1e-9 MeV. This reads Ca-40's row (not a mirror member) and nothing else; it proves the import is the sealed
    arithmetic.
C-4 (the synthetic fixture, halt): tools/mirror_pairs.py and the whole kit run on a throwaway 'Z N M' table written
    in a temporary directory, with 20 planted pairs at A = 13, 15, ..., 51 (index i = 0..19), planted masses
    M(Z_p, Z_p - 1) = M_base,i + CDE_U(A_i)/(1 + off_i) - (d_n - d_h) and M(Z_p - 1, Z_p) = M_base,i (M_base,i = -10 - i,
    arbitrary), so that f_i = off_i exactly; plus decoys that the rule must exclude: A = 11 (both members), A = 27 with
    only the (14, 13) member, an even-A N = Z pair (12, 12) and (13, 11), and the (0, 1) and (1, 0) rows. The build
    must recover n = 20 and exactly the planted labels (halt). Five plants, each run as a separate throwaway
    hold-out, with s_i = 0.02 (-1)^i (mean zero over 20) unless stated:
      P1 off_i = +0.20 + s_i: b = 0.20 to 1e-9; form U-MISS-HIGH; TREND-FLAT.
      P2 off_i = -0.20 + s_i: b = -0.20 to 1e-9; U-MISS-LOW; TREND-FLAT.
      P3 off_i = +0.03 + s_i: b = 0.03 to 1e-9; U-AGREES; TREND-FLAT.
      P4 off_i = 0.30 (-1)^i: b = 0 to 1e-9; U-UNDERPOWERED (F1 is about 2.6 x 0.30 / sqrt 20 = 0.17 > 0.0853);
         TREND-FLAT.
      P5 off_i = 0.10 + 0.01 (i - 9.5): b = 0.10 to 1e-9; U-MISS-HIGH; TREND-RISES (rho_A = +1 exactly; P2 for
         n = 20 is about 0.59).
    For P1 to P3, F1 is about 2.6 x 0.02 / sqrt 20 = 0.012, below 0.0853 and below |b| for P1 and P2, so the forms
    are robust to the resampler's details; the alternating s_i has rho_A = 0.087 by rank arithmetic (ranks 5.5 and
    15.5 against 1..20: covariance 2.5 over sqrt(33.25 x 25)), far below P2. The pass bar is the b value and the two
    forms; the F1 and P2 values are printed as diagnostics.
C-5 (the count floor, halt): n >= 15 in the evidence manifest (section 2). Diagnostic: n printed; no upper band.
C-6 (the floors recorded, halt): F1 and P2 are computed and written to the checkpoint by the floor unit, which runs
    after the truth unit seals the residuals and before the verdict unit; the verdict refuses to run without them.
The smoke run (LAB_SMOKE=1): C-1 to C-4 and the full unit chain on plant P1 only, in a temporary directory, checkpoint
analysis/nuc_cde_uniform_smoke.pkl; it never opens data/ame2012/AME2012.txt beyond C-3's Ca-40 row and never touches
analysis/holdout/NUC_CDE_UNIFORM/ or the evidence checkpoint.

## 6. THE FORMS

Q1, decided by B1 and F1 alone:
  U-AGREES:        |b| <= 0.0853 and F1 <= 0.0853.
  U-UNDERPOWERED:  |b| <= 0.0853 and F1 > 0.0853 (the scatter is too large for the bar to have bitten; open form).
  U-MISS-HIGH:     b > 0.0853 and b > F1.
  U-MISS-LOW:      b < -0.0853 and |b| > F1.
  U-SCATTER-OPEN:  |b| > 0.0853 and |b| <= F1 (a bias outside the bar that the pairs' scatter alone could produce;
                   no sign is read; open form).
  INSTRUMENT-OPEN: any halt of C-1 to C-6.
Q2, decided by B2 alone (rendered whenever Q1 is not INSTRUMENT-OPEN):
  TREND-RISES:     rho_A > P2.   TREND-FALLS: rho_A < -P2.   TREND-FLAT: |rho_A| <= P2.
The five Q1 cases are exhaustive and exclusive. Any Q1 form may pair with any Q2 form; INSTRUMENT-OPEN renders both
open. The Director's expected form, registered before any compute: U-MISS-HIGH (15 to 30 percent); nothing in the
bars was set from it (section 8).

## 7. WHAT COUNTS

Each form yields one rider on NUC-018 (and, by reference, on NUC-032's constants), worded in full:
U-AGREES: "RIDER, NUC-CDE-UNIFORM (analysis/NUC_CDE_UNIFORM_results.md): the sealed uniform-sphere Coulomb term
  a_C = 0.7716 MeV, scored by itself on the n T = 1/2 mirror pairs of AME2012 (A = 13 to A_max), where the Ca-40
  calibration, the surface and the symmetry terms cancel exactly, has mean fractional bias b (rms r), within its
  registered offset 0.0853 against the SEMF's 0.711, above a pair-scatter floor F1; A-trend: <TREND form>. A
  calibration-free consistency reading on a public table, not a blind confrontation. Grade D3 unchanged."
U-MISS-HIGH / U-MISS-LOW: the same rider with "overpredicts / underpredicts the measured Coulomb displacement
  energies by a mean fraction b (rms r), outside the registered offset 0.0853 and above the pair-scatter floor F1;
  the Coulomb cell's '+9%' is restated as 'misses the mirror displacement energies by <b> percent, <flat in A /
  growing with A / falling with A>'. The miss is kept at full weight." The scorecard cell "Coulomb term derived from
  winding charge and spacing (+9%)" gains that clause; a MISS with TREND-RISES or TREND-FALLS names the uniform-sphere
  shape, not only r0, as the registered deficiency on this channel.
U-UNDERPOWERED / U-SCATTER-OPEN: "the mirror channel at n pairs does not resolve the sealed Coulomb term at the 0.0853
  bar (b, F1 recorded); no sign is read." No cell changes.
INSTRUMENT-OPEN: no rider; the halt and its unit are recorded in the results file.
Grades and numbers: no form moves the row's grade (D3, the term consumes the measured saturation spacing and the
nucleon mass unit), no status changes, none of the five numbers of NORTH_STAR section 2b moves, no SM_EMERGENCE row
moves; this is a discriminator on a cell's wording. The release note says so in those words.
What it does NOT establish: nothing about the absolute-mass results, which scored the whole model and stand; nothing
about NUC-C's form (not instantiated); nothing about the shell, pairing or light-isotope cells (odd-A mirror pairs
have identical shell and pairing content on both members only to the extent isospin symmetry holds, which is the
premise of the channel, and the known isospin-breaking residue of order a few percent is below the bar); no unique
prediction (every standard mass model reproduces this channel better); nothing beyond the odd-A T = 1/2 pairs
present in AME2012.

## 8. NOT ASSUMED

The design does not lean on: the Director's expectation (U-MISS-HIGH, 15 to 30 percent, from general literature
on Coulomb displacement energies and the Nolen-Schiffer anomaly), which the theorist shares as a prior and which set
no bar (B1 comes from the registry's own 0.711; F1 and P2 from null resamples); the exact pair count n; the
measurement uncertainties (not in the file); isospin symmetry beyond its use as the channel's premise; any mass
value of any mirror member. The theorist's prior, stated and not leaned on: a miss that is largest at the lightest
pairs and shrinks with A, i.e. U-MISS-HIGH with TREND-FALLS, because a uniform sphere overstates the Coulomb energy
of a light, diffuse nucleus most. If the evidence says otherwise the forms say so.

## 9. AUTONOMY AND COMPUTE

No step waits on a person: the table is in the repository at a pinned hash; the build is a rule; no draw is needed
(the rule selects every eligible pair, so no beacon round is committed). Compute: the whole kit is arithmetic on at
most a few dozen pairs plus 20000 resamples; under 1 cpu minute, under 100 MB, wall time under 5 minutes including
the five fixture plants; one invocation per unit in the locked order (credential, build, manifest, predict, truth,
floor, verdict), resumable through the checkpoint analysis/nuc_cde_uniform.pkl.
Instrument files that exist: benchmarks/lab/nuc_new_5/driver.py (a_c, binding, calibrate, ca40_binding_from, CONFIG;
imported unchanged), benchmarks/lab/_kit/labkit.py (Driver / Checkpoint / Halt), data/ame2012/AME2012.txt.
Files the worker must write: tools/mirror_pairs.py (the build, section 2), benchmarks/lab/nuc_cde_uniform/driver.py
and verdict.py (the units above, following the nuc_new_5 pattern: the driver never prints a FORM line, a residual, a
bias or a floor; the verdict does, once), the hold-out analysis/holdout/NUC_CDE_UNIFORM/ by the build, and
analysis/NUC_CDE_UNIFORM_results.md after the verdict.

## DISCLOSURES

Cure for NUC-MIRROR-CDE and NUC-MIRROR-COULOMB: C-1 pins the sealed function's own return value, 0.7716295256894924,
at 1e-9, obtained by importing the driver in a scratch script and not by hand; the hand arithmetic in section 3 is
corrected (cube root 0.552669, r0 = 1.119708 fm) and is a check, not a pin. Cure for NUC-MIRROR-DISPLACE: the design
was written from two claims, 130 lines of the driver, 170 lines of the prior design and one scratch run, with one
leg, two questions and five fixture plants, inside the theorist budget. The NUC-C leg is dropped for the reason in
section 0 and is not a try on NUC-C. Numbers in this file that the sealed code computes were all quoted from the
scratch run; no evidence table or checkpoint was opened.
