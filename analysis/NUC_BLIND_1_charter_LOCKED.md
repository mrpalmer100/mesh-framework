# COMMISSION NUC-BLIND-1 -- THE REGISTERED NUCLEAR MASS MODEL SCORED ON A PRE-REGISTERED HOLD-OUT
# (CHARTER, LOCKED 2026-10-07 by the author after his draw and before any seal; the draw is the author's)

North Star line (section 5): (c) arms a discriminator of the programme's own method: the first
confrontation under the standing bar W (STRATEGIC_TARGETS section W). Scorecard row "Weights of atoms"
is graded D3 (whole-table, calibrated on Ca-40); this commission does not change the grade, it tells
the truth about it on isotopes the model was never inspected against. It is the fifth of the five
numbers' first candidate (externally adjudicated predictions) only if the hold-out is held by someone
other than the author; here it is held by the author's draw, so it counts as the programme's first
out-of-sample confrontation in the matter sector and not yet as external adjudication.

## The models, pre-registered (B-2: both scored, neither selected after)

  M1  NUC-018, both corrections: B = a_V A - 1.34 a_V A^(2/3) - a_C Z^2/A^(1/3), a_C = 0.772 MeV
      (derived from d0 = 2.026 fm, NUC-017), a_V calibrated once on Ca-40 (the registered calibration),
      asymmetry and pairing DECLARED OMITTED (NUC-005: they need Fermi statistics, i.e. hbar). The
      registered consequence of the omission is stated in NUC-005: neutron-rich nuclei overbound by
      about 23 (N - Z)^2/A MeV. M1 is the model as the scorecard cites it.
  M2  the four-term form LAMED used as its registered baseline (benchmarks/nuclear/lamed_residual_classifier.py):
      a_S/a_V = 1.108 (NUC-018's registered-best row), a_C derived at d0 = 2.026 fm, a_A = 19.85 MeV
      (NUC-A kinetic + NUC-B potential, derived), a_V calibrated once on Ca-40. Pairing omitted.
  Both are evaluated with Ca-40 from the TRAINING table (the draw excludes Ca-40 from the test set by
  construction, holdout_draw.py --exclude 20,20); nothing else is fitted to anything.

## The draw (W1; the author's, not the sandbox's)
  python tools/holdout_draw.py --name NUC_BLIND_1 --seed 92847574954767 --n 50 --drawn-by "palmer"
Run by the author on the PC, 2026-10-08T00:33:25Z (manifest). The author commits analysis/holdout/NUC_BLIND_1/ (train.txt, sealed/test.txt, MANIFEST.json),
and pastes the three sha256 lines into this charter at lock. The sandbox never opens sealed/test.txt;
the only reader is tools/holdout_verdict.py at step N4.

## Steps
  N1  (sandbox) benchmarks/nuclear/nuc_blind_1.py: reads train.txt only (for Ca-40), evaluates M1 and
      M2 at every (Z, N) listed in MANIFEST.json's test_zn (labels only, no masses), writes
      analysis/NUC_BLIND_1_pred_M1.txt and _M2.txt as 'Z N B_pred_MeV'.
  N2  (sandbox) tools/holdout_verdict.py seal --label M1 / --label M2, once per prediction file. Sha256 recorded
      in the manifest under per-label keys.
  N3  (sandbox) nothing. The predictions are frozen.
  N4  (the PC, the machine that holds sealed/test.txt; the sandbox never holds it) tools/holdout_verdict.py
      verdict --label M1 / --label M2 --unit mass --bar-rms 0.25 --bar-max 0.60, each once; VERDICT_M1.json and
      VERDICT_M2.json are kept.
  N5  (sandbox, benchmarks/nuclear/nuc_blind_1_subreading.py, written before the seal) the pre-registered
      sub-reading on the kept residual rows of the VERDICT files: for M1, the Pearson correlation of
      the mass residual with 23 (N - Z)^2/A over the 50 rows; for M2, with the pairing indicator
      (+1 even-even, 0 odd-A, -1 odd-odd). These say whether a failure is the declared omission.

## Bars (to be LOCKED before the draw is read)
B-1  Residuals in PERCENT OF MASS (the house unit for this row: binding is about 1 percent of mass).
     BLIND-AGREES: rms <= 0.25 and max |r| <= 0.60 (the registered whole-table range is 0.00 to 0.51 on
     the inspected isotopes; a fresh sample is allowed the same ceiling plus the rounding).
     BLIND-FAILS otherwise. BLIND-INCOMPLETE if any held-out row is unpredicted (none should be: both
     models are closed-form at every A >= 12).
B-2  Both models are scored; the results file reports both verdicts; no third model, no re-fit, no
     exclusion of rows after the truth is read (a drip-line isotope that misses is a miss).
B-3  The sub-reading (N5) is read after the verdict and changes nothing; a correlation >= 0.8 is reported
     as "FAILS AS DECLARED" and below as "FAILS FOR ANOTHER REASON"; it does not rescue the verdict.
B-4  The prior, stated and not leaned on: M1 BLIND-FAILS on the max bar (the omitted asymmetry on
     neutron-rich rows of a table that reaches the drip lines) with the sub-reading FAILS AS DECLARED;
     M2 is the open question (the derived a_A has never been scored off the inspected set).
B-5  The draw is the author's; the seed is recorded; no redraw.

## Verdict forms (to be LOCKED)
BLIND-AGREES (per model)   the model predicts untouched isotopes to the registered accuracy: the
                           scorecard row gains "out-of-sample at <rms>/<max> on 50 held-out isotopes"
                           and the model's claim takes a rider saying so.
BLIND-FAILS (per model)    kept; the claim takes a rider with the residual table's summary and the
                           sub-reading; the scorecard row says "whole-table only; fails blind at <max>".
BLIND-INCOMPLETE           a missing prediction: instrument fault, recorded.

## Rules
No rescue; the truth is read once by the verdict tool after the seal; the sandbox never reads the
sealed test file; riders the author's.

## Cost
Sandbox, minutes of compute; the author's draw first.

## Instrument notes before the seal (sandbox, 2026-10-07; recorded at lock)
tools/holdout_verdict.py gained two options before any seal: --unit mass (residual = 100 (pred - truth) / m_atom
with NUC-005's constants 938.272, 939.565, 0.511 MeV; the house unit of the row, matching NUC-018's 0.00 to 0.51
percent) and --label (per-model seal and verdict keys on one draw; each label sealed once, read once). Default
behaviour is unchanged. benchmarks/nuclear/nuc_blind_1.py reproduces the registered calibrations from train.txt's
Ca-40 row (B = 342.052 MeV): a_C 0.7716, M1 a_V 17.770 (NUC-018: 17.77), M2 a_V 15.987 (NUC-018's corrected-spacing
row: 15.99). Nothing is fitted.

## Author's lock
LOCKED 2026-10-07 ("lock NUC-BLIND-1"), after the author's draw and before any seal. The draw:
  table   sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13  (data/ame2012/AME2012.txt)
  train   sha256 7eda872326ea1d05eab3af44e60ceb0ab623c7306dc30f6aad5c5b4d24c6883a  (analysis/holdout/NUC_BLIND_1/train.txt)
  test    sha256 4abe4099897e5ae5e339a421522bb2cd172d9de7491cf1ee5bfffd064630466e  (analysis/holdout/NUC_BLIND_1/sealed/test.txt; NOT to be read)
  seed 92847574954767; drawn by palmer; 50 of 2397 eligible rows (A >= 12, Ca-40 excluded); no redraw.
The models, the bars (rms <= 0.25 and max <= 0.60 percent of mass), the forms, the prior and the sub-reading are
fixed from this line.
