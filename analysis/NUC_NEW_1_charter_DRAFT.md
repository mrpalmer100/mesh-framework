# COMMISSION NUC-NEW-1 -- THE TWO ADJUDICATED NUCLEAR MASS MODELS ON THE NUCLIDES MEASURED SINCE AME2012
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-31; target-facing; the kit ships with it; the evidence
# design was sealed before the kit was written: analysis/NUC_NEW_1_design_SEALED.md, commit e38870c)

## WHERE IT STANDS (the honest sentence, before the question)
The nuclear row has two registered mass models blind-scored twice on AME2012 and adjudicated once: M1, NUC-018's
three-term form (one constant calibrated on Ca-40, a derived surface ratio and a derived Coulomb coefficient,
asymmetry and pairing declared omitted), and M2, the four-term form whose symmetry energy a_A = 19.85 MeV is
derived (NUC-A kinetic, NUC-B potential) with no new constant. NUC-BLIND-2 (draw by mike, 2026-10-08) returned
BLIND-AGREES for both at rms 0.138 / max 0.227 (M1) and 0.016 / 0.035 (M2) percent of mass on 50 isotopes drawn at
random from the same AME2012 table the models were built against. Its results file says the blind line of the row
is finished: a third random draw of the same table would add a digit, not a fact. This commission is not a third
draw. Between AME2012 and AME2020 the field measured, for the first time, the masses of a few hundred nuclides,
almost all of them far from the valley of stability (the neutron-rich and proton-rich edges, the superheavy
elements). Those masses are a table the models have never seen in any form, and the labels are where a liquid-drop
form built on the valley has the least right to work. Nobody knows what the two models do there.

## THE QUESTION
Q1 (per model, the absolute question): do the frozen models predict the masses of the nuclides measured between
    AME2012 and AME2020 inside the registered accuracy (the section W bars)?
Q2 (per model, the extrapolation question): is the models' off-valley error distribution the one they showed on
    the valley (rms within a factor of 2 of the adjudicated in-sample rms), or does the form drift?
Q3 (per model, a sub-reading, informative, no form): do the residuals correlate with the declared omission
    channels (M1: the asymmetry term; M2: NUC-026's priced quartic companion and pairing)?

## WHAT IS GIVEN (registered inputs; no others enter)
The two models exactly as sealed for NUC-BLIND-2 (benchmarks/nuclear/nuc_blind_1.py, M1 and M2): a_C derived at
d0 = 2.026 fm (NUC-017), a_S/a_V = 1.34 (NUC-016 sphere value; M1) or 1.108 (NUC-005 facet value; M2), a_A = 0 (M1)
or 19.85 MeV (M2; NUC-A + NUC-B), a_V calibrated once on Ca-40 from data/ame2012/AME2012.txt. The house unit:
percent of atomic mass, m_atom from NUC-005's constants. Nothing is re-fit; the calibrator is AME2012's Ca-40, not
AME2020's, so the models are byte-identical to the adjudicated ones (credential C-1 proves it).

## THE EVIDENCE SET (design section 2; deterministic; nature's draw, no seed)
T = every (Z, N) whose AME2020 mass excess is experimental (no '#' flag), with A >= 12, that is not a row of
data/ame2012/AME2012.txt (2438 experimental rows). Built once by tools/ame2020_newset.py on the machine holding the
AME2020 file (AMDC mass_1.mas20), which writes labels.txt (Z N only), sealed/test.txt (read once by the truth
unit) and MANIFEST.json (hashes, counts, the anchor check). The sandbox never holds the AME2020 file; the models and
the sandbox read labels.txt only. If |T| < 30 every question renders NEW-SET-TOO-SMALL.
BUILT 2026-10-31 11:25 UTC by the author on the lab machine (commit 7d23981 on queue; the author's-draw variant):
  |T| = 128 (new, experimental, A >= 12). AME2020: 3558 rows, 2550 experimental, 1008 from systematics; shared with
  AME2012 2421; AME2012 rows absent from AME2020 17 (they are AME2012 rows, not T; recorded, nothing done); new rows
  with A < 12: 1 (excluded by scope). Anchors C-12, O-16, Ca-40, Fe-56, Pb-208: deltas 0.0000, -0.0000, -0.0000,
  -0.0007, -0.0004 MeV, all within 0.010 (C-4 pass).
  ame2020 sha256 e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307  (mass_1.mas20, from the AMDC
                 mirror at IMP Lanzhou, amdc.impcas.ac.cn; the IAEA host sits behind a browser challenge)
  ame2012 sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13  (data/ame2012/AME2012.txt)
  labels  sha256 2387278737460b207fc8b4d5637ad5426cfe4f0981686ee187fac20f2012298a  (analysis/holdout/NUC_NEW_1/labels.txt)
  test    sha256 71658bb61b80507f68e2d1e19b5cc56fa4853447c848a4568137771b37b6534b  (analysis/holdout/NUC_NEW_1/sealed/test.txt; read once, by the truth unit)

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
No row is removed after the truth is read; no model is re-fit, amended or added; no bar moves; no second verdict.
A reading of any AME2020 value of a new nuclide by the executor or the drafting worker before the lock removes that
row from T (queue rule 3; none has occurred). The AME2012 table's own extrapolated values are not in the repository
(the table holds experimental rows only), so no preview of the new rows exists in the sandbox.

## DESIGN COMMITMENTS (locked at lock; design sections 3 to 6, unchanged)
D1  Models M1 and M2 as given. Predictions at every label of T; files analysis/NUC_NEW_1_pred_M1.txt and _M2.txt
    in NUC-BLIND-2's layout; their sha256 sealed in the hold-out manifest before the truth is read.
D2  Statistics, per model, from the sealed rows: r_i = 100 (B_pred - B_truth) / m_atom; rms; max |r|; the five
    worst rows with sign (+: overbound by the model).
D3  Q2's reference is the model's NUC-BLIND-2 adjudicated rms READ FROM analysis/holdout/NUC_BLIND_2/VERDICT_M1.json
    and VERDICT_M2.json by the credential unit (0.13799 and 0.01600), never typed; the bar is 2 x that.
D4  Q3's channels: M1 residual against 23 (N-Z)^2 / A / m_atom; M2 residual against (N-Z)^4 / A^3 / m_atom and
    against the pairing indicator (+1 even-even, -1 odd-odd, 0 odd-A). Pearson correlations with sign; no fit.

## HARNESS (binding)
Driver and verdict on labkit (Driver / Checkpoint / Halt / Blocked / Verdict); CONFIG shared; units in order:
credential (C-1 the model code reproduces NUC-BLIND-2's sealed prediction files byte for byte; C-2 the residual
rule reproduces NUC-BLIND-2's published rms and max from the VERDICT rows to 1e-9; C-3 the set tool on a synthetic
mas20-layout fixture recovers the planted set and counts exactly; a failure halts, the verdict renders
INSTRUMENT-OPEN, the truth is never read), manifest (Blocked until analysis/holdout/NUC_NEW_1/ exists; C-4 the
recorded anchor deltas within 0.010 MeV; C-5 labels are new, A >= 12, unique, hashed; sealed/ never opened),
predict (M1, M2 at the labels; arrays sealed), seal (gated on C-1 to C-5; one seal per model), truth (the one
read of sealed/test.txt, residual rows sealed; or ingestion of VERDICT_M*.json written on the adjudicator's
machine, checked against the seals). The verdict recomputes every statistic from the seals, decides all four
tokens, then publishes the table and Q3. The driver prints no residual, rms or max. LAB_SMOKE=1 runs every unit on
a throwaway hold-out built from the synthetic fixture in a temporary directory (five planted rows with synthetic
excesses; no AME2020 value exists anywhere in the sandbox), withholding forms. Run: seconds. Memory: trivial. No
JAX; numpy only.

## VALIDATION BARS (halt-grade; the credential unit; all passed in the smoke of 2026-10-31)
C-1  byte equality with analysis/NUC_BLIND_2_pred_M1.txt (edb67e24...) and _M2.txt (a5f3f8e0...).
C-2  rms and max of the published VERDICT_M1/M2.json rows reproduced to 1e-9.
C-3  planted set and counts recovered exactly from the synthetic fixture (both '#' conventions planted).
C-4  five anchors (C-12, O-16, Ca-40, Fe-56, Pb-208; AME2012 rows, not evidence) within 0.010 MeV of AME2012.txt,
     checked by the tool before anything is written and re-verified from the manifest by the driver.
C-5  labels disjoint from AME2012, A >= 12, no duplicate, hash equal to the manifest's; the calibrator not a label.

## FORMS (exhaustive; pre-registered; one per question on every terminal verdict)
Q1-M1, Q1-M2:  BLIND-AGREES (rms <= 0.25 and max <= 0.60 percent of mass; the section W bars, identical to
               NUC-BLIND-1 and -2) / BLIND-FAILS / BLIND-INCOMPLETE (a row of T without a prediction).
Q2-M1, Q2-M2:  EXTRAPOLATES (rms <= 2 x the adjudicated in-sample rms: 0.2760 for M1, 0.0320 for M2) / DRIFTS.
               On rms only: a max over 100 to 300 rows is not comparable with a 50-row max and bears no bar.
               Why 2: the two in-sample draws differed by 1.14x (M1) and 1.45x (M2); 2 is outside draw-to-draw
               variation and inside any real failure of the form off the valley. Set before any number of T is known.
NEW-SET-TOO-SMALL (every question; |T| < 30). INSTRUMENT-OPEN (the open form).

## WHAT COUNTS (B-6; the author's riders)
Q1 BLIND-AGREES: a rider on NUC-018 (M1) and on NUC-A and NUC-B (M2): "blind-scored on the |T| nuclides measured
  between AME2012 and AME2020: rms / max"; the scorecard row's grade column adds "blind-scored on new measurements".
  A fail is a kept rider with the numbers. No status change either way; the NUC-BLIND riders stand.
Q2: a rider on the same claims. DRIFTS for M2 is the out-of-sample price of NUC-026's named quartic / surface-
  symmetry companion, recorded here and not chartered here.
Section 2b "externally adjudicated predictions": 1 -> 2 only if a named person who is not the author runs the set
  tool and holds sealed/ on a machine the author does not use, and runs the truth step there (the driver ingests
  VERDICT_M*.json); if the author runs the tool on the lab machine, the result is the author's draw of a public,
  reader-reproducible set and 2b is unchanged. CHOSEN: the author's-draw variant (the author ran the tool on the lab
  machine, 2026-10-31); 2b is unchanged by this commission.

## NO-RESCUE RULE
No row excluded for its residual; no regional re-scoring that was not pre-registered (none is); no amended model
scored on T afterwards under this name. A DRIFTS or a BLIND-FAILS is kept at full weight on the row.

## SMOKE DISCIPLINE (binding on the drafting worker)
The worker runs LAB_SMOKE=1 only. It does not download AME2020, does not run the set tool on a real file, does not
open analysis/holdout/NUC_NEW_1/sealed/ if it exists, and does not run the predict unit against the evidence labels
before the lock (predictions are not evidence, but the order is the rule).

## PROCEDURE (who does what)
1. DONE (author's-draw variant). The author, on the lab machine, in the queue clone:
       curl -sSL -o mass_1.mas20 https://amdc.impcas.ac.cn/masstables/Ame2020/mass_1.mas20
       python3 tools/ame2020_newset.py --ame2020 mass_1.mas20 --run-by "author"
   The first attempt against the IAEA host fetched a 5 KB browser-challenge page; the tool refused it ("parsed only
   0 experimental rows") and wrote nothing. The mirror's file (472648 bytes, AME2020 header dated 3 Mar 2021)
   parsed and passed the anchors. Committed analysis/holdout/NUC_NEW_1/ (labels.txt, MANIFEST.json, sealed/test.txt,
   as GRV-BLIND-2 did) as 7d23981 on queue. The .mas20 file is not in the repository.
2. The lab locks; the driver runs its units on the lab machine, where sealed/ exists; the truth unit reads
   sealed/test.txt once. (In the adjudicated variant, not chosen, the truth unit would be Blocked until the
   adjudicator, holding sealed/ and the sealed MANIFEST.json the lab pushed, runs the standing tool where sealed/ lives
   (python tools/holdout_verdict.py verdict --name NUC_NEW_1 --predictions analysis/NUC_NEW_1_pred_M1.txt --label M1
   --unit mass --bar-rms 0.25 --bar-max 0.60, and the same for M2) and sends back VERDICT_M1.json and VERDICT_M2.json,
   which the driver ingests after checking their prediction and test hashes against the seals.)
3. The verdict renders once; results to analysis/NUC_NEW_1_results.md.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
1. The executor has not opened AME2020 in any form; the sandbox cannot reach the AMDC site and holds no copy. After
   the build the sandbox fetched 7d23981 with analysis/holdout/NUC_NEW_1/sealed/ excluded from the working tree
   (git sparse-checkout); it holds labels.txt (Z N only; sha256 verified against the manifest) and MANIFEST.json,
   which carries counts, hashes and the five anchor deltas (AME2012 rows) and no mass of any new row. The executor
   knows |T| = 128 and the labels, and no value of T. The AME2012 table in the repository holds experimental rows only.
2. The design was sealed (commit e38870c) before the set tool, the driver and the verdict were written; the kit was
   then credentialed on NUC-BLIND-2's published files (C-1, C-2) and on a synthetic fixture (C-3); the smoke's
   throwaway truth is five planted synthetic numbers. No evidence cell was computed.
3. Expectations, stated so they cannot be mistaken for results: the executor expects Q1 BLIND-AGREES for both and
   has no expectation on Q2 (M1's omitted asymmetry grows off the valley; M2 faces the quartic channel and a Coulomb
   coefficient 9 percent high at Z^2 / A^(1/3) values no stable row reaches). The Director's expectation: to be
   recorded at lock.

## NORTH STAR ACCOUNTING
Target-facing: section 1 row "Weights of atoms" and its discriminator; a confrontation of registered predictions
with measurements the models have never seen, the first on data that did not exist when the models were built.
Satisfies section 5 after RING-WAVE-STABILITY-4's interior exception (the next session had to be target-facing).
Moves no number in section 2b unless the adjudicated variant is chosen and passes.

## STANDING
Draft, 2026-10-31, on the queue branch for the Director's proposal under author-kit mode.

```lab
commission: NUC-NEW-1
target: "Weights of atoms row (section 1) and its registered discriminator: whether the two adjudicated nuclear mass models (NUC-018 three-term; NUC-A + NUC-B four-term), frozen as sealed for NUC-BLIND-2 and calibrated once on AME2012's Ca-40, predict the masses of the nuclides measured between AME2012 and AME2020 inside the section W bars, and whether their off-valley rms stays within twice the adjudicated in-sample rms; target-facing; moves 2b only in the adjudicated variant"
driver: benchmarks/lab/nuc_new_1/driver.py
verdict_script: benchmarks/lab/nuc_new_1/verdict.py
instrument:
  - benchmarks/lab/_kit/labkit.py
  - tools/ame2020_newset.py
  - benchmarks/nuclear/nuc_blind_1.py
  - data/ame2012/AME2012.txt
  - analysis/NUC_NEW_1_design_SEALED.md
forms: [BLIND-AGREES, BLIND-FAILS, BLIND-INCOMPLETE, EXTRAPOLATES, DRIFTS, NEW-SET-TOO-SMALL, INSTRUMENT-OPEN]
state: [analysis/nuc_new_1_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
