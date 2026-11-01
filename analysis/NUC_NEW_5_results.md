# COMMISSION NUC-NEW-5 -- RESULTS (verdict rendered once, 2026-10-31, from sealed data; revision round 1 of the write-up)

Path note. The charter's PROCEDURE fixes the results path as analysis/NUC_NEW_5_results.md (the chartered path, used
in every citation below). The workspace for this write-up accepts writes only at analysis/NUC-NEW-5_results.md, so
this file is that same document filed at the path the harness allows; it should be placed at the chartered path on
promotion. The content is identical; there is one document.

Charter: analysis/NUC_NEW_5_charter_DRAFT.md (the author's draft, locked by the lab under author-kit mode; the
evidence design is analysis/NUC_NEW_5_design_SEALED.md, commit dc90f7d). Driver benchmarks/lab/nuc_new_5/driver.py;
verdict script benchmarks/lab/nuc_new_5/verdict.py; records analysis/holdout/NUC_NEW_1/VERDICT_M1.json and
VERDICT_M2.json (written once, computed_at_utc 2026-10-31T15:32:54Z). Predictions: analysis/NUC_NEW_5_pred_M1.txt
(sha256 ff061233...) and analysis/NUC_NEW_5_pred_M2.txt (sha256 1382170f...), sealed before the truth was read.
Every number below is copied from the verdict output or the two VERDICT_M*.json headers; nothing was recomputed
except the plain ratios marked as arithmetic.

## 1. What was asked

Target: the "Weights of atoms" row of docs/NORTH_STAR.md section 2, and its registered discriminator (bar W).
The two nuclear mass models that were blind-scored twice on AME2012 (NUC-BLIND-1; NUC-BLIND-2, adjudicated) were
frozen exactly as sealed for NUC-BLIND-2:

- M1: NUC-018's three-term form (a_S/a_V = 1.34, a_C = 0.7716 MeV, asymmetry and pairing omitted).
- M2: the four-term form with the derived symmetry energy a_A = 19.85 MeV (NUC-A kinetic, NUC-B potential), a_S/a_V =
  1.108, a_C = 0.7716 MeV, pairing omitted.

Both carry one constant, a_V, calibrated once on AME2012's Ca-40 (the run recorded a_V = 17.7703 MeV for M1 and
15.9871 MeV for M2). They were confronted with the 128 nuclides (A >= 12, experimental AME2020 mass excess, not a
row of data/ame2012/AME2012.txt) first measured between AME2012 and AME2020, labels A = 15 to 266, Z <= 109. The
programme had never inspected these values. Questions (charter, THE QUESTION):

- Q1 (per model): inside the section W bars, rms <= 0.25 and max <= 0.60 percent of atomic mass?
- Q2 (per model): is the rms on the 128 rows within the fixed ratio 2 of the adjudicated in-sample rms (read from
  analysis/holdout/NUC_BLIND_2/VERDICT_M1.json and VERDICT_M2.json: 0.13799 and 0.01600), and, if the ratio is above
  2, is it above the bootstrap sampling floor F (99th percentile)? Q2 is a fixed rms ratio; it is not a test of
  equality of error distributions.
- Q3 (per model): a sub-reading with no form and no claim.

## 2. What was computed

Residual per row r = 100 (B_pred - B_truth) / m_atom (percent of mass; + means overbound by the model). The
credential unit, manifest unit, predict unit, seal unit and truth unit ran in order; the truth file was read once.

Credentials and pins (all from the verdict output): C-1 PASS (byte equality with the sealed NUC-BLIND-2 predictions,
and the run binding for M1 and for M2); C-2 PASS; C-3 PASS; C-4 PASS; C-5 PASS; C-6(a) with counts equality PASS;
C-7 PASS. Scored rows plus missing labels equal the sealed label set: 128 of 128 predicted for both models
(missing_zn empty).

Diagnostics that gate nothing (printed as the charter requires): AME2020 3558 rows, 2550 experimental, 1008 from
systematics; AME2012 2438 rows, 17 absent from AME2020; 2421 shared rows, of which 0.9752 agree within 0.1 MeV (60
beyond; largest shift 1.360 MeV). This is the figure on which NUC-NEW-2's 0.99 bar failed; that failure stands
(NUC-NEW-2 closed before any evidence was read) and no threshold was applied to it here.

## 3. Verdict forms and the numbers behind them

| model | Q1 form | rms (% of mass) | max abs (% of mass) | bars | Q2 form | rho = rms / in-sample | floor F |
|---|---|---|---|---|---|---|---|
| M1 NUC-018 three-term | BLIND-AGREES | 0.1909 | 0.4976 | rms <= 0.25, max <= 0.60 | EXTRAPOLATES | 1.383 (0.1909 / 0.1380) | 1.178 (bootstrap median 1.001) |
| M2 four-term, a_A = 19.85 | BLIND-AGREES | 0.0203 | 0.0420 | rms <= 0.25, max <= 0.60 | EXTRAPOLATES | 1.271 (0.0203 / 0.0160) | 1.370 (bootstrap median 1.004) |

Adjudicated in-sample reference (NUC-BLIND-2, 50 rows): M1 0.1380 / 0.2271; M2 0.0160 / 0.0350 (rms / max).

Worst five rows as printed by the verdict (+: overbound by the model; -: underbound), listed as printed and nothing
more:

- M1: Z=5 N=16 +0.4976; Z=5 N=15 +0.4532; Z=5 N=14 +0.4008; Z=4 N=11 +0.3466; Z=9 N=20 +0.3081.
- M2: Z=4 N=11 -0.0420; Z=5 N=16 -0.0391; Z=10 N=5 -0.0381; Z=23 N=39 +0.0363; Z=21 N=38 +0.0355.

Reading the forms:

- Q1-M1 BLIND-AGREES: rms 0.1909 is 76 percent of its bar (arithmetic: 0.1909 / 0.25), max 0.4976 is 83 percent of
  its bar (0.4976 / 0.6). The sample-size note in the charter (the 0.60 max bar was fixed for 50 rows and is applied
  unchanged to 128) concerns a BLIND-FAILS driven by max alone; no BLIND-FAILS rendered, so the note is not invoked.
- Q1-M2 BLIND-AGREES: rms 0.0203 and max 0.0420 are 8 percent and 7 percent of the respective bars (arithmetic).
- Q2-M1 EXTRAPOLATES: rho 1.383 <= 2, which fixes the form. The printed floor is F = 1.178. The numbers stand as
  printed: 1.383 > 1.178. Exceeding F while remaining at or below 2 has no verdict form of its own under the charter
  (WITHIN-FLOOR needs 2 < rho <= F; DRIFTS needs rho > 2 and rho > F), and no inference is drawn from the comparison.
- Q2-M2 EXTRAPOLATES: rho 1.271 <= 2, which fixes the form. The printed floor is F = 1.370. No inference is drawn
  from the comparison.
- WITHIN-FLOOR and DRIFTS could not have rendered for either model on these numbers, as the charter noted: both
  require rho > 2, and F is 1.178 and 1.370.
- Max ratios, arithmetic only, not a pre-registered statistic, no form attaches: M1 0.4976 / 0.2271 = 2.19; M2
  0.0420 / 0.0350 = 1.20. (For comparison, the rms ratios are 1.383 and 1.271.) No explanation of these ratios is
  offered or established by this verdict.

## 4. Q3 sub-reading (no form, no claim; no rider may quote these numbers)

Printed by the verdict with its permutation null (1000 label permutations, seed 20261031):

- M1: corr(residual, 23 (N-Z)^2 / A) = +0.892; null 99th percentile of |r| 0.223; observed at the 100.0th percentile.
- M2: corr(residual, (N-Z)^4 / A^3) = -0.252; null 99th percentile 0.224; observed at the 99.3rd percentile.
  corr(residual, pairing indicator) = +0.046; null 99th percentile 0.227; observed at the 41.2th percentile, not
  above the null floor.

These are recorded as the charter requires. They are not used anywhere in sections 5 to 8 and no claim draft
carries them.

## 5. What this establishes

- On these 128 rows, with one constant calibrated on Ca-40 from AME2012 and nothing re-fit, both frozen models land
  inside the section W bars: M1 at 0.1909 / 0.4976, M2 at 0.0203 / 0.0420 percent of mass (rms / max).
- The ratio of the 128-row rms to the adjudicated in-sample rms is 1.383 (M1) and 1.271 (M2), both at or below the
  pre-registered factor 2 (EXTRAPOLATES, both).
- The models were byte-identical to the adjudicated ones (C-1 and its run binding), so the result is a confrontation
  of those models and not of a variant.

## 6. What this does not establish

- Scope: 128 nuclides, AME2020 experimental values, A >= 12 (labels A = 15 to 266, Z <= 109), the house unit percent
  of atomic mass. The unit matters: binding is a small part of mass and the nucleon rest mass is an input
  (NUC-018's mass-versus-binding note). No binding-energy-relative accuracy was scored or is claimed here; not
  computed.
- It is an out-of-sample confrontation of a frozen model, not a prediction of unmeasured quantities. The values were
  published (2012 to 2020) before the models were registered (2026); the blindness rests on the programme's
  non-inspection, which the record cannot externally verify. It is not an externally adjudicated prediction (the
  author built the set; no adjudicator holds anything), and NORTH_STAR section 2b "externally adjudicated predictions"
  is unchanged by construction.
- It does not move the grade. The row stays D3: whole-table calibration on Ca-40, nucleon mass unit and m_e as
  inputs.
- It does not test the shell structure, the He-4 and light-isotope zero-point misses, the m_p/m_e gate, or any of the
  items in the row's "Blocked by" cell. Fermi statistics, asymmetry and pairing remain behind hbar.
- The hold-out has no pre-registered regional split (the charter forbids regional re-scoring), so nothing is claimed
  about where within the 128 the models do better or worse. The worst-five lists in section 3 are the verdict's own
  printout of ten specific rows and are not a regional pattern.
- Nothing is claimed about whether the 128-row errors and the AME2012 errors share a distribution (Q2 is a fixed rms
  ratio), nor about why the ratios are what they are.
- It does not identify what causes M1's residual or M2's; Q3 carries no claim. In particular it does not identify
  NUC-026's quartic or surface-symmetry companion.
- The 0.9752 shared-row agreement shows AME2020 re-evaluated 60 AME2012 rows by more than 0.1 MeV (largest 1.360 MeV).
  Whether re-evaluation touches the 128 new rows is not computed here; the comparison is against AME2020 values as
  published.

## 7. North Star scorecard

- Targets moved from blocked to derived: 0. Inputs retired: 0. The five numbers of section 2b: none move. Section
  2b "externally adjudicated predictions" unchanged (1).
- Riders, as the charter's WHAT COUNTS fixes them (no status change on any claim; the NUC-BLIND riders stand). Each
  is written out in full:
  - NUC-018 (M1): "RIDER 2026-10-31, NUC-NEW-5 (analysis/NUC_NEW_5_results.md): scored on the 128 AME2020 nuclides
    absent from AME2012, never inspected by the programme (published before registration): rms 0.1909, max 0.4976
    percent of mass, BLIND-AGREES under bar W; rho = 1.383 against the adjudicated in-sample rms 0.1380, floor F
    1.178, EXTRAPOLATES; an out-of-sample confrontation of a frozen model, not a prediction of unmeasured
    quantities. The blindness rests on the programme's non-inspection, which the record cannot externally verify."
  - NUC-A (M2): "RIDER 2026-10-31, NUC-NEW-5 (analysis/NUC_NEW_5_results.md): the derived a_A = 19.85 MeV in the
    four-term form, scored on the 128 AME2020 nuclides absent from AME2012, never inspected by the programme
    (published before registration): rms 0.0203, max 0.0420 percent of mass, BLIND-AGREES under bar W; rho = 1.271
    against the adjudicated in-sample rms 0.0160, floor F 1.370, EXTRAPOLATES; an out-of-sample confrontation of a
    frozen model, not a prediction of unmeasured quantities. The blindness rests on the programme's non-inspection,
    which the record cannot externally verify."
  - NUC-B (M2): "RIDER 2026-10-31, NUC-NEW-5 (analysis/NUC_NEW_5_results.md): the combined derived a_A = 19.85 MeV
    (NUC-A kinetic plus NUC-B potential) in the four-term form, scored on the 128 AME2020 nuclides absent from
    AME2012, never inspected by the programme (published before registration): rms 0.0203, max 0.0420 percent of
    mass, BLIND-AGREES under bar W; rho = 1.271 against the adjudicated in-sample rms 0.0160, floor F 1.370,
    EXTRAPOLATES; an out-of-sample confrontation of a frozen model, not a prediction of unmeasured quantities. The
    blindness rests on the programme's non-inspection, which the record cannot externally verify."
  - The scorecard row's grade column adds "scored out of sample on the 128 AME2020 nuclides absent from AME2012".
- Plain statement: both frozen models landed inside their pre-registered bars on a set the programme had not
  inspected. This is not progress on the two numbers of the North Star; it is evidence for the existing D3
  reconstruction's reach on these 128 rows. The executor's recorded expectation (charter, DISCLOSURES 3) was Q1
  BLIND-AGREES for both, with no expectation on Q2; Q1 rendered as expected.

## 8. Natural next question (not chartered)

The verdict printed worst-five rows for each model (section 3); M1's five are Z=5 N=16, Z=5 N=15, Z=5 N=14, Z=4 N=11
and Z=9 N=20, and M2's are Z=4 N=11, Z=5 N=16, Z=10 N=5, Z=23 N=39 and Z=21 N=38. This write-up draws no pattern from
them (no regional reading is pre-registered). The registered next-order for the row is not further blind scoring
(NUC-BLIND-2's results already said a third random draw of AME2012 would add a digit, not a fact) but the misses a
liquid-drop form is already recorded as unable to reach: the He-4 binding miss of 38 percent and the H-2/H-3/He-3/He-4
light-isotope zero-point residuals (docs/NORTH_STAR.md section 2, scorecard row and fence test (c); NUC-008, which
names the missing zero-point kinetic term) and the shell closures above 20 (NUC-SHELL-1, NUC-SHELL-2), which wait on the
action-scale fence. Any model amended in response to these residuals and scored on this set would not be a
confrontation under this name (charter, NO-RESCUE RULE); an amended model needs a fresh hold-out.

## Review record (written by the lab)

| Stage | Reviewer | Model | Result |
|---|---|---|---|
| lock r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| lock r1 | external | openai/gpt-6-astra | pass |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | not passed |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| verdict r1 | external | openai/gpt-6-astra | pass |
