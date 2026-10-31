# COMMISSION NUC-NEW-5 -- THE TWO ADJUDICATED NUCLEAR MASS MODELS ON THE 128 NUCLIDES FIRST MEASURED BETWEEN AME2012 AND AME2020
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-31; target-facing; the kit ships with it; the evidence
# design was sealed before the kit: analysis/NUC_NEW_5_design_SEALED.md, commit dc90f7d, which supersedes
# NUC_NEW_4's (076e183), NUC_NEW_3's (151ae8e), NUC_NEW_2's (46b6ec6) and NUC_NEW_1's (e38870c); the evidence set
# is pinned by hash and is in the repository)

## WHERE IT STANDS (the honest sentence, before the question)
The nuclear row has two registered mass models blind-scored twice on AME2012 and adjudicated once: M1, NUC-018's
three-term form (one constant calibrated on Ca-40, a derived surface ratio and a derived Coulomb coefficient,
asymmetry and pairing declared omitted), and M2, the four-term form whose symmetry energy a_A = 19.85 MeV is
derived (NUC-A kinetic, NUC-B potential) with no new constant. NUC-BLIND-2 (draw by mike, 2026-10-08) returned
BLIND-AGREES for both at rms 0.138 / max 0.227 (M1) and 0.016 / 0.035 (M2) percent of mass on 50 isotopes drawn at
random from the same AME2012 table the models were built against; its results file says a third random draw of
that table would add a digit, not a fact. This commission is not a third draw. Between AME2012 and AME2020 the
field measured for the first time the masses of 128 nuclides with A >= 12, almost all far from the valley of
stability (the neutron-rich and proton-rich edges, the superheavy elements up to Z = 109). Those measurements
(2012 to 2020) predate the models' registration (2026) but this programme has never inspected them: the
repository holds AME2012 only, and the labels are where a liquid-drop form built on the valley has the least
right to work. Nobody knows what the two models do there.

History of this charter, so the record is plain. NUC-NEW-1 (kit landed 2026-10-30 22:54 local) was proposed by
the Director within a minute, failed three lock-review rounds on objections that were right (steps waiting on a
person, no pins, incomplete verdict binding, no Q2 floor, no Q3 null, no real-file check beyond five anchors,
two wrong sentences) and was parked WITHDRAWN at 23:06, twelve hours before the hold-out was built. NUC-NEW-2's
design answered every objection and fixed, before the real-file audit ran, a C-6(b) bar of 0.99 of the shared
rows within 0.1 MeV; the audit returned 0.9752 (60 of 2421 AME2012 rows re-evaluated by more than 0.1 MeV in
AME2020, the largest by 1.36 MeV), so NUC-NEW-2 closed before any evidence was read, as its design requires.
NUC-NEW-3 restated that one bar as 0.90 and 5.0 MeV with the audit disclosed; both lock reviewers refused it in
two rounds (09:27 to 09:30 local): a halt-grade threshold chosen after a preview of the statistic it gates is
tuned to pass whatever the motive, and disclosure does not cure it. They were right; NUC-NEW-2's failure stands
at full weight. NUC-NEW-4 took the remedy the skeptical reviewer named: C-6(b) is a recorded diagnostic that
gates nothing, the parser's credential rests on checks fixed before any real file was seen, and a new credential
C-7 asks a different question on a fresh schedule (do the existing halt-grade checks catch a misparse of the
layout), with its rules fixed from arithmetic on the synthetic fixture written into the design (076e183) before
the kit. NUC-NEW-4 then went three rounds (10:03 to 10:11 local) in which the external reviewer passed in round
2 and the skeptical in round 3, never both, and the parking rule took the name. NUC-NEW-5 carries their last four
points, each accepted (design dc90f7d): C-6(c)'s count bands, written with the build counts known, are
diagnostics like (b), with only the audit-equals-manifest consistency check halt-grade; the audit's AME2012 hash
is checked against the pin as C-6(a) promised; C-1 is bound to the run (the credential unit records the Ca-40
binding and each a_V; the predict unit must equal them to 1e-12, on the seal gate), so "byte-identical to the
adjudicated models" is proved by the code, not asserted; and the rider is reworded as an out-of-sample
confrontation (WHAT COUNTS). Nothing about the set, the models or Q1 changed since NUC-NEW-1.

## THE QUESTION
Q1 (per model, the absolute question): do the frozen models predict the masses of the 128 nuclides inside the
    registered accuracy (the section W bars)?
Q2 (per model, the extrapolation question): is the off-valley rms within a fixed ratio (2) of the adjudicated
    in-sample rms, and is a ratio above 2 larger than sampling alone produces at these sizes (the floor F)?
    Q2 tests a fixed rms ratio; it is not a test of equality of error distributions.
Q3 (per model, a sub-reading, no form, no claim): do the residuals correlate with the declared omission channels
    (M1: the asymmetry term; M2: NUC-026's priced quartic companion and pairing), beside a permutation null? No
    rider quotes a Q3 number; the verdict prints the rule with the number.

## WHAT IS GIVEN (registered inputs; no others enter)
The two models exactly as sealed for NUC-BLIND-2 (benchmarks/nuclear/nuc_blind_1.py, M1 and M2): a_C derived at
d0 = 2.026 fm (NUC-017), a_S/a_V = 1.34 (NUC-016 sphere value; M1) or 1.108 (NUC-005 facet value; M2), a_A = 0 (M1)
or 19.85 MeV (M2; NUC-A + NUC-B), a_V calibrated once on Ca-40 from data/ame2012/AME2012.txt. The house unit:
percent of atomic mass, m_atom from NUC-005's constants. Nothing is re-fit; the calibrator is AME2012's Ca-40, not
AME2020's, so the models are byte-identical to the adjudicated ones: C-1 proves the arithmetic by byte equality
with the sealed NUC-BLIND-2 files, and the predict unit is bound to C-1 (its Ca-40 binding from AME2012.txt and
each a_V must equal the credentialed values to 1e-12, halt-grade, required at the seal gate).

## THE EVIDENCE SET (design section 2; deterministic; nature's draw, no seed; built; pinned)
T = every (Z, N) whose AME2020 mass excess is experimental (no '#' flag), with A >= 12, that is not a row of
data/ame2012/AME2012.txt (2438 experimental rows). Built once by the author on the lab machine, 2026-10-31 11:25
UTC, with tools/ame2020_newset.py on the AMDC file (served by the AMDC mirror at IMP Lanzhou, amdc.impcas.ac.cn;
the IAEA host sits behind a browser challenge that the tool refused as a 5 KB HTML page, writing nothing);
committed as 7d23981; audited 13:10 UTC (--audit; 87c21e5). The AME2020 file itself is not in the repository.
  |T| = 128.  AME2020: 3558 rows, 2550 experimental, 1008 from systematics; shared with AME2012: 2421 of 2438;
  AME2012 rows absent from AME2020: 17; new rows with A < 12: 1 (excluded by scope). Labels A = 15 to 266, Z <= 109.
  Anchors C-12, O-16, Ca-40, Fe-56, Pb-208: deltas 0.0000, -0.0000, -0.0000, -0.0007, -0.0004 MeV (all within 0.010).
  Audit of the shared rows: 2361 of 2421 within 0.100 MeV (0.9752); 60 beyond; largest shift 1.3600 MeV.
  ame2020 sha256 e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307  (mass_1.mas20, 472648 bytes)
  ame2012 sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13  (data/ame2012/AME2012.txt)
  labels  sha256 2387278737460b207fc8b4d5637ad5426cfe4f0981686ee187fac20f2012298a  (analysis/holdout/NUC_NEW_1/labels.txt)
  test    sha256 71658bb61b80507f68e2d1e19b5cc56fa4853447c848a4568137771b37b6534b  (analysis/holdout/NUC_NEW_1/sealed/test.txt)
  audit   sha256 2a92fe6ae4ee4a848230be1a8725d281c2378663c4d4be3351765aa50b9b54fe  (analysis/holdout/NUC_NEW_1/AUDIT.json)
The audit's shared-row agreement is a DIAGNOSTIC: NUC-NEW-2's sealed bar of 0.99 failed on it and that failure
stands; no threshold is applied to it under this name (design 076e183, C-6(b)). The verdict prints it as such.
These hashes and |T| = 128 are the PINS in the driver's CONFIG; the manifest unit halts on any difference and
never trusts MANIFEST.json's own fields. MANIFEST.json is not an instrument file because the seal unit writes the
two prediction hashes into it; its evidence fields are bound by the pins. The hold-out keeps the directory name NUC_NEW_1 (the design fixes the set,
not the commission name). The models and the sandbox read labels.txt (Z N only). No value of T has been read by
the executor or by any lab agent.

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
No row is removed after the truth is read; no model is re-fit, amended or added; no bar moves; no second verdict.
Nothing waits on a person: the hold-out and its audit are in the repository; there is no adjudicated variant, no
external verdict file, no ingestion path, no choice deferred to lock. Section 2b "externally adjudicated
predictions" is unchanged by construction (the author built a public, reader-reproducible set; no adjudicator
holds anything). The Director's expectation, if any, is the Director's to record in the proposal, not a step.

## DESIGN COMMITMENTS (locked at lock; design sections 3 to 6, unchanged)
D1  Predictions for every label from the frozen models and AME2012's Ca-40 only; written as analysis/
    NUC_NEW_5_pred_M1.txt and _M2.txt in NUC-BLIND-2's layout; their sha256 sealed in the hold-out manifest and
    in the checkpoint before the truth is read.
D2  The residual per row in the house unit, 100 (B_pred - B_truth) / m_atom; rms; max |r|; the five worst rows
    with sign (+: overbound by the model).
D3  Q2's reference is the model's NUC-BLIND-2 adjudicated rms READ FROM analysis/holdout/NUC_BLIND_2/VERDICT_M1.json
    and VERDICT_M2.json by the credential unit (0.13799 and 0.01600), never typed. rho = rms(T) / that. The
    sampling floor F per model: a bootstrap (seed 20261031; 10000 resamples; each draws 50 residuals with
    replacement for a reference rms and 128 for a test rms from the model's pooled 100 published in-sample
    residuals, NUC-BLIND-1's 50 and NUC-BLIND-2's 50, disjoint from T) and F is the 99th percentile of the ratio;
    computed by the credential unit BEFORE any evidence file is opened and recorded in the checkpoint. From the
    published files the smoke computed F = 1.178 (M1) and 1.370 (M2), so the factor 2 clears sampling at these
    sizes by a wide margin and WITHIN-FLOOR cannot render on these numbers; the credential unit recomputes F at
    the run and the verdict uses the recorded value, not this sentence.
D4  Q3's channels: M1 residual against 23 (N-Z)^2 / A / m_atom; M2 residual against (N-Z)^4 / A^3 / m_atom and
    against the pairing indicator (+1 even-even, -1 odd-odd, 0 odd-A). Pearson correlations with sign; each beside
    a permutation null (1000 label permutations, seed 20261031, the null's 99th percentile of |r|, the observed
    |r|'s percentile in the null); no fit; no form; no claim; no rider.

## HARNESS (binding)
Driver and verdict on labkit (Driver / Checkpoint / Halt / Verdict); CONFIG shared; units in order:
credential (C-1 to C-3, C-7 and the floor F; the Ca-40 binding and each a_V recorded; a failure halts, the
verdict renders INSTRUMENT-OPEN, the truth is never read), manifest (pins, including the audit's four hashes;
C-4; C-5; the C-6 consistency equality; the C-6(b) and (c) diagnostics recorded; sealed/ never opened; a missing
file is a halt, not a wait), predict (M1, M2 at the labels from AME2012's Ca-40, which must equal the credentialed
binding, each a_V the credentialed a_V, to 1e-12; arrays sealed), seal (gated on C-1 to C-7, the C-1 run binding
and the recorded floors; one seal per model), truth
(the ONE read of sealed/test.txt: its sha256 must equal the pin and the hash the manifest unit recorded; parsed
once into one raw array (Z, N, M); labels unique and equal to the sealed label set; sealed raw; both models' rows
derive from that payload; VERDICT_M*.json written as a record only). The verdict binds before it computes: scored
rows plus missing labels equal the sealed label set (unique, disjoint); every scored prediction equals its sealed
prediction to 1e-9; every truth excess equals the sealed raw payload's; the recomputed residual equals the
driver's record to 1e-9. Then it decides the four tokens, then publishes the table and Q3. The driver prints no
residual, rms or max. LAB_SMOKE=1 runs every unit on a throwaway hold-out built and audited by the tool from a
synthetic fixture in a temporary directory (five planted rows with synthetic excesses; the pins are the fixture's
own hashes), withholding forms. Run: seconds. Memory: trivial. numpy only.

## VALIDATION BARS (halt-grade unless marked; all passed in the smoke of 2026-10-31; C-4, C-5, C-6(a) and the C-6
## equality also pass on the real hold-out in a dry run of the manifest unit that opened labels.txt, MANIFEST.json
## and AUDIT.json only)
C-1  byte equality with analysis/NUC_BLIND_2_pred_M1.txt (edb67e24...) and _M2.txt (a5f3f8e0...); and the run
     binding: the predict unit's Ca-40 binding (AME2012.txt) equals the credentialed one (NUC_BLIND_2/train.txt)
     and each a_V equals the credentialed a_V, to 1e-12; required at the seal gate.
C-2  rms and max of NUC-BLIND-1's and NUC-BLIND-2's published VERDICT_M1/M2.json rows reproduced to 1e-9; the
     pooled 100 residuals per model sealed; F computed and recorded.
C-3  planted set and counts recovered exactly from the synthetic fixture by the tool's build and audit (both '#'
     conventions planted; one AME2012 row removed; one A < 12 row planted).
C-4  five anchors (AME2012 rows, not evidence) within 0.010 MeV, recorded by the tool, re-verified by the driver.
C-5  labels disjoint from AME2012, A >= 12, unique, count 128, hash equal to the pin; the calibrator not a label.
C-6  (a) the audit is of the pinned file, the pinned AME2012 table and this hold-out (its four hashes, ame2020,
     ame2012, labels and test, each equal the pins; absence halts); (b) DIAGNOSTIC, gating nothing: the
     shared-row agreement (0.9752 within 0.100 MeV; 60 beyond; largest shift 1.36 MeV) is recorded and printed
     as the NUC-NEW-2 audit result, on which NUC-NEW-2's 0.99 bar failed; (c) DIAGNOSTIC, gating nothing: the
     counts (3558 rows; 2550 experimental; 1008 systematics; 2421 shared; 17 AME2012 rows absent; 1 new row with
     A < 12) are recorded and printed; no band is applied to any of them (46b6ec6's bands, written with these
     counts known, are withdrawn). Halt-grade and kept: the audit's counts equal the manifest's counts, field
     by field, a consistency check between two records of the same build, not a threshold.
C-7  the perturbation credential (design 076e183 section 4; fixture only; rules fixed from arithmetic stated in
     the design before the kit): p1 unit error (keV written as MeV), p3 inverted flag convention, p4 N and Z
     swapped, p5 the field shifted left by two or three characters: build() must REFUSE each (anchors, the
     experimental-row floor, a missing asymmetric anchor); p6 a one-character shift either way: build() succeeds
     and every shared value is within 0.001 MeV of the unperturbed parse (not a misparse in effect; said so
     rather than claimed caught); p7 a right shift of two: C-3's set equality must FAIL (a tail-convention '#'
     leaves the window). Any other behaviour halts.

## FORMS (exhaustive; pre-registered; one per question on every terminal verdict)
Q1-M1, Q1-M2:  BLIND-AGREES (rms <= 0.25 and max <= 0.60 percent of mass; the section W bars, identical to
               NUC-BLIND-1 and -2) / BLIND-FAILS / BLIND-INCOMPLETE (any label without a prediction, the
               all-missing case included; no statistic on the remainder).
Q2-M1, Q2-M2:  BLIND-INCOMPLETE (as Q1) / EXTRAPOLATES (rho <= 2) / WITHIN-FLOOR (2 < rho <= F) / DRIFTS (rho > 2
               and rho > F).
NEW-SET-TOO-SMALL (every question; |T| < 30; cannot render, |T| = 128 is pinned; kept for completeness).
INSTRUMENT-OPEN (the open form: a credential, pin, binding or harness failure; C-6(b) and (c) cannot cause it).
Sample-size note, binding on the results: the 0.60 max bar was fixed for 50-row samples and is applied unchanged
to 128 rows; a BLIND-FAILS driven by max alone with rms inside its bar is partly a sample-size effect and the
verdict says so in its reason. The bar does not move.

## WHAT COUNTS (B-6; locked; design section 7)
Q1 BLIND-AGREES for a model: a rider on that model's claim (NUC-018 for M1; NUC-A and NUC-B for M2): "scored on
  the 128 AME2020 nuclides absent from AME2012, never inspected by the programme (published before registration):
  rms/max percent of mass; an out-of-sample confrontation of a frozen model, not a prediction of unmeasured
  quantities"; the scorecard row's grade column adds "scored out of sample on the 128 AME2020 nuclides absent
  from AME2012". The blindness rests on the programme's non-inspection, which the record cannot externally
  verify; the rider says so by its wording. A fail is a kept rider with the numbers and the sample-size note
  where it applies. No status change either way; the NUC-BLIND riders stand.
Q2: a rider on the same claims with rho, F and the form. DRIFTS for M2 is recorded as an out-of-sample shortfall
  of the four-term form; it does not by itself identify NUC-026's quartic or surface-symmetry companion, which
  stays a priced, uncommissioned item.
Q3: nothing moves; no rider quotes a Q3 number.
Section 2b: unchanged by construction. North Star numbers: none move.

## NO-RESCUE RULE
No row excluded for its residual; no regional re-scoring (none is pre-registered); no amended model scored on T
afterwards under this name. A DRIFTS or a BLIND-FAILS is kept at full weight on the row.

## HYGIENE (the order of the evidence, stated)
sealed/test.txt was committed to the queue branch at 7d23981, before the seal unit runs, as GRV-BLIND-2's was.
The defence is the models, not the order: M1 and M2 are frozen functions of (Z, N) and AME2012's Ca-40,
credentialed byte for byte against NUC-BLIND-2's sealed predictions (C-1) at every run, so no reading of the
truth could change a prediction without failing C-1. The sandbox that drafted this charter excluded sealed/ from
its working tree (git sparse-checkout) and holds labels.txt, MANIFEST.json and AUDIT.json only; the executor has
read no value of T. The worker runs LAB_SMOKE=1 only and does not open sealed/ before the lock.

## PROCEDURE (nothing waits on a person)
1. The lab locks under author-kit mode; the driver runs its five units on the lab machine, where the hold-out is
   in the clone; the truth unit reads sealed/test.txt once.
2. The verdict renders once; results to analysis/NUC_NEW_5_results.md with the riders of WHAT COUNTS.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
1. The executor has not opened AME2020 in any form and the sandbox holds no copy; the executor knows |T| = 128,
   the labels, the counts, the anchor deltas and the shared-row audit (all AME2012-row or count quantities), and
   no value of T.
2. The design was sealed before each kit (e38870c, 46b6ec6, 151ae8e, 076e183, dc90f7d); the kit was credentialed on
   NUC-BLIND-1's and -2's published files and on a synthetic fixture; the smoke's throwaway truth is five planted
   synthetic numbers. No evidence cell was computed. The NUC-NEW-2 C-6(b) failure stands; NUC-NEW-3's re-set bar
   was refused and is withdrawn; C-7's rules were fixed from fixture arithmetic before the kit, not from the
   audit.
3. Expectations, stated so they cannot be mistaken for results: the executor expects Q1 BLIND-AGREES for both and
   has no expectation on Q2 (M1's omitted asymmetry grows off the valley; M2 faces the quartic channel and a
   Coulomb coefficient 9 percent high at Z^2 / A^(1/3) values no stable row reaches).

## NORTH STAR ACCOUNTING
Target-facing: section 1 row "Weights of atoms" and its discriminator; a confrontation of registered predictions
with measurements this programme has never inspected. Satisfies section 5 after RING-WAVE-STABILITY-4's interior
exception (the next session had to be target-facing). Moves no number in section 2b.

## STANDING
Draft, 2026-10-31, on the queue branch for the Director's proposal under author-kit mode.

```lab
commission: NUC-NEW-5
target: "Weights of atoms row (section 1) and its registered discriminator: whether the two adjudicated nuclear mass models (NUC-018 three-term; NUC-A + NUC-B four-term), frozen as sealed for NUC-BLIND-2 and calibrated once on AME2012's Ca-40, predict the masses of the 128 nuclides first measured between AME2012 and AME2020 (pinned hold-out analysis/holdout/NUC_NEW_1, in the repository) inside the section W bars, and whether their off-valley rms stays within twice the adjudicated in-sample rms above a locked sampling floor; target-facing; moves no North Star number; nothing waits on a person; NUC-NEW-2's failed audit bar and the build counts kept as diagnostics, no threshold set with a statistic in view; C-1 bound to the run"
driver: benchmarks/lab/nuc_new_5/driver.py
verdict_script: benchmarks/lab/nuc_new_5/verdict.py
instrument:
  - benchmarks/lab/_kit/labkit.py
  - tools/ame2020_newset.py
  - benchmarks/nuclear/nuc_blind_1.py
  - data/ame2012/AME2012.txt
  - analysis/NUC_NEW_5_design_SEALED.md
  - analysis/NUC_NEW_4_design_SEALED.md
  - analysis/NUC_NEW_3_design_SEALED.md
  - analysis/NUC_NEW_2_design_SEALED.md
  - analysis/NUC_NEW_1_design_SEALED.md
  - analysis/holdout/NUC_NEW_1/labels.txt
  - analysis/holdout/NUC_NEW_1/AUDIT.json
  - analysis/holdout/NUC_BLIND_2/MANIFEST.json
  - analysis/holdout/NUC_BLIND_2/train.txt
  - analysis/NUC_BLIND_2_pred_M1.txt
  - analysis/NUC_BLIND_2_pred_M2.txt
  - analysis/holdout/NUC_BLIND_1/VERDICT_M1.json
  - analysis/holdout/NUC_BLIND_1/VERDICT_M2.json
  - analysis/holdout/NUC_BLIND_2/VERDICT_M1.json
  - analysis/holdout/NUC_BLIND_2/VERDICT_M2.json
forms: [BLIND-AGREES, BLIND-FAILS, BLIND-INCOMPLETE, EXTRAPOLATES, WITHIN-FLOOR, DRIFTS, NEW-SET-TOO-SMALL, INSTRUMENT-OPEN]
state: [analysis/nuc_new_5_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
