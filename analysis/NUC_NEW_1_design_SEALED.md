# NUC-NEW-1 -- EVIDENCE DESIGN, SEALED BEFORE THE INSTRUMENT WAS TOUCHED (2026-10-31)

Queue rule 3 (analysis/queue/README.md): the evidence set, the models, the statistics, the bars and the forms are
written here and committed BEFORE any instrument for this commission is written or run. The commit hash of this
file goes into the charter. Nothing below is changed afterwards; a change is a new name.

## 1. The question

The registered nuclear mass models (NUC-018's three-term form, and the four-term form with NUC-A + NUC-B's derived
symmetry energy, the two models NUC-BLIND-1 and NUC-BLIND-2 scored) were calibrated and blind-scored on the
AME2012 table, which is the only nuclear mass table in the repository. Between AME2012 and AME2020 the field
measured the masses of a few hundred nuclides for the first time, almost all of them far from stability (neutron-
rich and proton-rich isotopes at the edges of the measured region, and the superheavy elements). Those masses did
not exist in any form the models could have seen. The question: do the two models, frozen as adjudicated on
2026-10-08, predict the masses of the nuclides measured since AME2012 inside the registered accuracy, and do they
extrapolate off the measured region as well as they interpolate inside it?

Nobody knows the answer. The models have never been evaluated at these labels; the executor has not opened AME2020;
the sandbox never holds the AME2020 file.

## 2. The evidence set (deterministic; nature's draw, no seed)

Source: the AME2020 atomic mass evaluation (Huang et al. and Wang et al., Chinese Physics C 45 (2021) 030002 and
030003), the AMDC file mass_1.mas20 (or its equivalent mass20.txt), obtained by the author on the lab machine.
The sandbox does not download it and does not read it.

Test set T: every (Z, N) such that
  (a) the AME2020 row's mass excess is EXPERIMENTAL (no '#' flag; '#' marks a value from systematics), and
  (b) A = Z + N >= 12 (the registered scope of the nuclear row, NUC-005/018), and
  (c) (Z, N) is NOT a row of data/ame2012/AME2012.txt (the repository's AME2012 table, 2438 experimental rows,
      sha256 88c6272c...), and
  (d) (Z, N) is not the calibrator (20, 20) (it cannot be, by (c); stated for completeness).
Nothing else is excluded and nothing is added. The set is fixed by the two public tables; any reader can rebuild it.

The tool tools/ame2020_newset.py (to be written AFTER this seal) parses the AME2020 file, writes
  analysis/holdout/NUC_NEW_1/labels.txt           Z N only, sorted; the file the models are allowed to read
  analysis/holdout/NUC_NEW_1/sealed/test.txt      Z N M (mass excess, MeV; the AME2012.txt layout); read ONCE, by the
                                                  verdict, after the predictions are sealed
  analysis/holdout/NUC_NEW_1/MANIFEST.json        hashes of the AME2020 file, of AME2012.txt, of labels.txt and of
                                                  test.txt; the counts (AME2020 experimental rows, rows shared with
                                                  AME2012, rows of AME2012 absent from AME2020, new rows with A < 12,
                                                  new rows with A >= 12 = |T|); the anchor check (section 4); who ran
                                                  it and when
and prints the counts and the hashes only, never a mass of a new row. It refuses to overwrite an existing hold-out.

Minimum size: if |T| < 30 every question renders NEW-SET-TOO-SMALL and the commission is closed without a verdict
(the expectation is between 100 and 300 rows; the number is not known to the executor at this seal).

## 3. The models (fixed; the adjudicated ones; nothing added, nothing re-fit)

Exactly benchmarks/nuclear/nuc_blind_1.py's M1 and M2, the arithmetic reproduced in the driver and credentialed
against the sealed NUC-BLIND-2 prediction files byte for byte (section 4, C-1):
  M1  NUC-018 three-term: B = a_V A - 1.34 a_V A^(2/3) - a_C Z^2 / A^(1/3); a_C = 0.6 x 1.44 / (r0/d0 x d0) at
      d0 = 2.026 fm (NUC-017), r0/d0 = (3 / (4 pi sqrt 2))^(1/3); a_V calibrated ONCE on Ca-40's AME2012 binding
      (the registered calibration; B(Ca-40) = 20 D_H + 20 D_N - M with D_H = 7.28897059, D_N = 8.07131714, the
      house constants). Asymmetry and pairing omitted, as declared in NUC-005.
  M2  the four-term form: a_S/a_V = 1.108, the same a_C, a_A = 19.85 MeV (NUC-A kinetic 16.6 + NUC-B potential,
      derived, no new constant), a_V on Ca-40. Pairing omitted.
The calibrator is read from data/ame2012/AME2012.txt, NOT from AME2020, so the models are the same bytes-in,
bytes-out objects that passed NUC-BLIND-2. The models never read labels other than Z and N.

## 4. Credentials (known answers; every one must pass before any prediction is sealed; halt-grade)

C-1  Reproduction. The driver's model code, pointed at NUC-BLIND-2's labels (analysis/holdout/NUC_BLIND_2/
     MANIFEST.json test_zn) and its train.txt's Ca-40, writes files whose sha256 equal the sealed
     analysis/NUC_BLIND_2_pred_M1.txt (edb67e24...) and _M2.txt (a5f3f8e0...) exactly. Bar: byte equality.
C-2  Verdict arithmetic. The verdict's residual rule (--unit mass: 100 (B_pred - B_truth) / m_atom with
     m_atom = Z 938.272 + N 939.565 + Z 0.511 - B_truth, the house unit) applied to the published NUC-BLIND-2
     VERDICT_M1/M2.json rows reproduces their rms and max to 1e-9 (M1 0.13798832 / 0.22709641; M2 0.0160 / 0.0350
     as published, read from the files, not typed).
C-3  Parser. tools/ame2020_newset.py on a SYNTHETIC file in the mas20 fixed-width layout, built by the fixture
     from AME2012 rows plus planted rows (new experimental rows with A >= 12, new rows with A < 12, new rows
     flagged '#', and one AME2012 row removed), recovers exactly the planted set T and the planted counts. Bar:
     set equality. The fixture never contains an AME2020 value.
C-4  Anchor check (runs inside the tool on the lab machine, recorded in the manifest, re-verified by the driver's
     manifest unit): for the five anchors C-12, O-16, Ca-40, Fe-56, Pb-208, all in AME2012, the AME2020 mass excess
     agrees with AME2012.txt within 0.010 MeV. If any anchor fails, the parse is refused and nothing is written.
     These five values are not evidence (they are AME2012 rows); no other AME2020 value is printed or compared.
C-5  Manifest. The driver's manifest unit verifies that labels.txt has no row in AME2012.txt, no row with A < 12,
     no duplicate, and that its sha256 is the manifest's; it never opens sealed/.
The pre-truth gate: C-1 to C-5 pass in the checkpoint, else the seal and truth units refuse (exit 2) and the
truth is never read. A credential failure is INSTRUMENT-OPEN, not a verdict.

## 5. The statistics (computed once, from sealed arrays, by the verdict script)

Per model, over the predicted rows of T: the residual r_i = 100 (B_pred - B_truth) / m_atom (percent of atomic
mass, the house unit of the scorecard row); rms = sqrt(mean r_i^2); max = max |r_i|; the five worst rows by |r|
with the sign convention "+ : overbound by the model" (the NUC-BLIND-2 convention).

## 6. The bars and the forms (locked here)

Q1 (per model), the absolute question, the standing section W bars, identical to NUC-BLIND-1 and -2:
  BLIND-AGREES    rms <= 0.25 and max <= 0.60 percent of mass
  BLIND-FAILS     otherwise
  BLIND-INCOMPLETE  any row of T without a prediction (a missing row is a miss, kept)
Q2 (per model), the extrapolation question, on rms only (rms is sample-size free; max over a set two to six times
  larger than 50 rows is not comparable with a 50-row max and bears no bar here):
  EXTRAPOLATES    rms <= 2 x the model's NUC-BLIND-2 adjudicated rms, read from VERDICT_M1/M2.json
                  (M1: 2 x 0.13799 = 0.27598; M2: 2 x 0.01600 = 0.03200 percent of mass)
  DRIFTS          rms > that
  Why 2: the two in-sample draws (the author's and mike's) differed by 1.14x (M1) and 1.45x (M2) on rms; a factor
  of 2 is outside the draw-to-draw variation of the same residual distribution and inside any real failure of the
  form off the valley of stability. Set before any number of T is known.
Q3 (per model), a sub-reading, informative, no bar, pre-registered so it cannot be chosen afterwards:
  the Pearson correlation of r_i with the declared omission channels: M1 with 23 (N-Z)^2 / A / m_atom (the
  asymmetry omission; NUC-BLIND-2 read +0.83 in-sample); M2 with (N-Z)^4 / A^3 / m_atom (NUC-026's priced quartic
  companion, coefficient about -47 MeV in-sample) and with the pairing indicator (+1 even-even, -1 odd-odd, 0
  odd-A). Reported with its sign. Nothing is fitted; no coefficient is read from T.
NEW-SET-TOO-SMALL  |T| < 30 (every question).
INSTRUMENT-OPEN    the harness could not evaluate (the open form).

## 7. What counts (B-6; locked)

Q1 BLIND-AGREES for a model: a rider on that model's claim (NUC-018; NUC-A and NUC-B) "blind-scored on the |T|
  nuclides measured between AME2012 and AME2020: rms/max"; the scorecard row's grade column adds "blind-scored on
  new measurements". A fail is kept as a rider with the numbers; no status change either way; the NUC-BLIND riders
  stand (they record a different set).
Q2 EXTRAPOLATES / DRIFTS: a rider on the same claims; a DRIFTS for M2 is the out-of-sample price of NUC-026's named
  surface-symmetry / quartic companion, recorded, not chartered here.
Section 2b "externally adjudicated predictions": moves from 1 to 2 only if a named person who is not the author
  runs tools/ame2020_newset.py and holds analysis/holdout/NUC_NEW_1/sealed/ on a machine the author does not use,
  and the verdict is run there (the NUC-BLIND-3 form named in NUC_BLIND_2_results.md). If the author runs the tool
  on the lab machine, the result counts as the author's draw of a public set, reproducible by any reader, and 2b
  is unchanged. The author decides which before the lock; the charter records it.
Target-facing (NORTH_STAR section 5): the scorecard row "Weights of atoms" (section 1) and its discriminator; a
  confrontation of registered predictions with measurements the models have never seen.

## 8. Rules

No row removed after the truth is read; no re-fit; no second verdict; the sandbox never holds AME2020 or
sealed/test.txt; the labels file is the only AME2020-derived file the models and the sandbox see, and it carries no
mass. The executor's prior, stated and not leaned on: Q1 both AGREE; Q2 open for both (M1's omission grows off the
valley; M2 faces the quartic channel and the superheavy Coulomb term, 9 percent high in a_C, at Z^2 / A^(1/3)
values AME2012's stable rows never reach).
