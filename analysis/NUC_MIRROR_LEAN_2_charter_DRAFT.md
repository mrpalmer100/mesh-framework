# COMMISSION NUC-MIRROR-LEAN-2 -- THE DERIVED UNIFORM-SPHERE COULOMB TERM SCORED ALONE ON THE AME2012 MIRROR DISPLACEMENT ENERGIES
# (CHARTER, the author's DRAFT for the lab's lock, 2026-11-04; interior work under NORTH_STAR section 5, permitted
# as the one interior session after NUC-NEW-5, with the author's reading recorded in that section under this name;
# the kit ships with it; the evidence design was sealed before the kit: analysis/NUC_MIRROR_LEAN_2_design_SEALED.md,
# commit 97d5d8f, sha256 5112f290952bc77e...; kit commit ea32d5d)

## WHERE IT STANDS (the honest sentence, before the question)
The weights-of-atoms row's Coulomb cell reads "Coulomb term derived from winding charge and spacing (+9%)". That
+9% is a coefficient comparison, NUC-018's derived a_C = 0.772 MeV against the empirical SEMF 0.711, and the term has
never been scored on a measurement by itself: in NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 the calibrated bond depth,
the surface term and the symmetry term carry most of every mass. On one channel all three cancel exactly in the
registered models: the binding difference of a T = 1/2 mirror pair at odd A, which is a_C A^(2/3) and nothing else
(design section 0; C-2 proves it on the sealed code). The programme has never formed that difference.

History, so the record is plain. This is the eighth design of the question nuc-coulomb-mirror-displacement and
the first on the author's route. The lab's seven (NUC-MIRROR-CDE, NUC-MIRROR-COULOMB, NUC-MIRROR-DISPLACE,
NUC-CDE-UNIFORM, NUC-MIRROR-UNIFORM, NUC-MIRROR-LEAN and its round one) died before any lock: two of a hand
constant pinned tighter than the code returns, one of its design budget, two of the worker's turn limit, and
NUC-MIRROR-LEAN (sealed f754186, 4 November; skeptical pass at design and at lock) at the external lock review on
three points no kit could answer: no North Star section 5 line, a pair count taken from the evidence table at
build time and disclosed, and standing bar W argued away by the cancelling calibration. This charter keeps
NUC-MIRROR-LEAN's question, model, statistic, bars and fixtures to the digit and cures the three (design
DISCLOSURES 3): section 7 of the design carries the section 5 line; nobody counts n before the run; the
predictions are written and sealed before the table is opened and the evidence unit is bound to them by hash.

## THE QUESTION
Q1 (the only question): does the registered uniform-sphere Coulomb term, a_C = 0.7716 MeV on Z^2/A^(1/3) from
    d0 = 2.026 fm with no constant fitted to any mass, reproduce the measured Coulomb displacement energies of the
    AME2012 T = 1/2 mirror pairs at A >= 13 to within the coefficient's own registered offset, B1 = 0.085?

## WHAT IS GIVEN (registered inputs; no others enter)
a_c() and binding() of benchmarks/lab/nuc_new_5/driver.py, imported unchanged (NUC-BLIND-1's constants,
credentialed there by byte equality and bound to NUC-NEW-5's run): coulomb_factor = 0.864 MeV fm, d0 = 2.026 fm
(NUC-017), r0/d0 = (3/(4 pi sqrt 2))^(1/3); the code returns a_c() = 0.7716295256894924 MeV. The binding-from-excess
convention of ca40_binding_from (B = Z d_h + N d_n - M; d_n - d_h = 0.78234655 MeV). The channel model
CDE_U(A) = a_c() A^(2/3). Nothing is calibrated, nothing is re-fit, no constant of CDE_U can be fitted after the
table is read. NUC-C (diffuseness and exchange) is not scored: it has no code in the repository.

## THE EVIDENCE SET (design section 2; deterministic; nature's set, no seed; pinned)
data/ame2012/AME2012.txt, sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the NUC-NEW-5
pin), rows 'Z N M', parsed exactly as ca40_binding_from parses them. The rule: every odd A >= 13 with
Z_p = (A + 1)/2 such that both (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present. No upper limit, no other exclusion,
no choice, no draw. NOBODY KNOWS n BEFORE THE RUN: the design states no n, this charter states no n, the kit was
credentialed on fixtures whose n the fixtures plant (8, and 4 for the count halt), and the executor's sandbox has
not opened the table. The evidence unit records n and applies the count rule (n < 5 halts before any M is read).

Bar W, met as NUC-NEW-5 met it. The nuclear sector carries a calibration (a_V on Ca-40), so the standing blind
hold-out bar applies as written. The set is selected by a process other than the commission (the deterministic
rule on a table pinned by hash); the prediction is frozen before the held-out values are read: the predict unit
writes CDE_U(A) for every odd A from 13 to 299 to analysis/NUC_MIRROR_LEAN_2_pred.txt, seals the array in the
checkpoint and records the file's sha256, before the evidence unit opens the table; the evidence unit must
reproduce that hash (C-6) and scores from the sealed array, never recomputing a prediction.

The one read: the evidence unit checks the table's sha256 against the pin (C-4), forms the label list (ascending
A), checks n >= 5 (C-5), reads M for exactly the 2n labelled rows into one raw array sealed before any statistic.
The driver never prints a mass, a displacement energy, a delta, a mean or n.

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
Not leaned on: the Director's expected form for NUC-MIRROR-LEAN (U-MISS-HIGH by 15 to 30 percent) and the
executor's prior (U-MISS-HIGH, more at light A, from the public Nolen-Schiffer literature); no bar depends on
either. Not assumed: that every AME2012 row is experimental (the pin is the hash); that Z^2 is the right form
(Z(Z - 1) is one diagnostic line, no form); that B1 is a physical bar (it is the registry's stated precision for
the coefficient). Forbidden: any read of the table before the lock; any statistic set after a preview (there is
no preview); any re-fit; any exclusion of a pair for its residual; any trend reading (no trend statistic exists).

## DESIGN COMMITMENTS (locked at lock; design sections 3 to 6, unchanged)
delta_i = CDE_U(A_i)/CDE_meas,i - 1 with CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p). mean_delta
(equal weight per pair, the decided statistic), rms_delta, min and max with their A, the Z(Z - 1) diagnostic mean.
Floor h = max(h_boot, h_inst): h_boot the 99.0th percentile of |mean(delta*) - mean_delta| over 10000 pair
bootstraps, seed 20261104, convention written in design section 4 (default_rng, one rng.choice per resample on the
ascending-A delta array, numpy.percentile linear); h_inst = 0.100 MeV sqrt 2 / CDE_U(13) / sqrt n =
0.03314952113422842 / sqrt n (NUC-NEW-5's audit tolerance class, the per-pair-worst sensitivity, independent
errors; what it is and is not is written in design section 4, and a coherent charge-symmetry-breaking contribution
is part of the measured channel, named in the rider, not of the floor). Band B1 = 0.085 = a_c()/0.711 - 1 to three
figures (NUC-018's registered comparison). Q1 rule in the locked order: (1) h > B1 U-NULL-FLOOR; (2) |mean| + h <= B1
U-AGREES; (3) mean - h > B1 U-MISS-HIGH; (4) mean + h < -B1 U-MISS-LOW; (5) otherwise U-OPEN-BAND. sign_resolved =
|mean| > h is recorded and decides nothing.

## HARNESS (binding)
benchmarks/lab/nuc_mirror_lean_2/driver.py (sha256 0cdac0f2a450bee6...) and verdict.py (1dfaafb83fc037fe...) on
benchmarks/lab/_kit/labkit.py: one CONFIG shared, every locked number in it; MANIFEST of the six locked files bound
at the first unit and re-verified at every later one; units credential, predict, evidence, one per invocation,
resumable; any exception a recorded halt (INSTRUMENT-OPEN); the verdict reads the checkpoint only, fails closed,
recomputes mean, rms, h_boot, h_inst, h and every delta from the sealed raw payload and the sealed predictions and
requires them to equal the driver's record to 1e-12, prints one FORM line, writes
analysis/NUC_MIRROR_LEAN_2_results.md once (the per-pair table A, Z_p, CDE_meas, CDE_U, delta; the statistics;
the hashes) under the kit's one-shot reservation. Smoke (LAB_SMOKE=1): every unit in one process; the credential
unit as in evidence; the predict file under benchmarks/lab/nuc_mirror_lean_2/scratch/; the evidence unit on
fixture T's F1 table in a temporary directory; checkpoint analysis/nuc_mirror_lean_2_smoke.pkl; forms withheld; the
AME2012 table never opened.

## VALIDATION BARS (halt-grade unless marked; all passed in the executor's smoke of 2026-11-04 on the fixtures only)
C-1  a_c() = 0.7716295256894924 to 1e-9 (the sealed code's own value). Diagnostic: |a_c() - 0.7716| < 1e-4; d0 and
     coulomb_factor to 1e-12; d_n - d_h = 0.78234655 to 1e-8.
C-2  for A in {13, 17, 21, 25, 33, 45, 61, 75}, Z = (A - 1)/2, three (a_V, a_S/a_V, a_A) triples:
     |binding(A, Z) - binding(A, Z + 1) - a_c() A^(2/3)| < 1e-9 (smoke: worst 3.0e-14).
C-3  fixture T (eight planted pairs, five distractors) under payloads F1 (CDE_meas = 0.9 CDE_U: mean 0.111111,
     h_boot 0, U-MISS-HIGH), F2 (0: U-AGREES), F3 (1.2 CDE_U: mean -0.166667, U-MISS-LOW), F4 (0.05/0.11 alternating:
     mean 0.08, h_boot 0.0225, U-OPEN-BAND), F5 (0.0/0.5 alternating: h_boot 0.1875, U-NULL-FLOOR), each to 1e-9
     (h_boot = 0 to 1e-12), h_inst = 0.011720125593549844 at n = 8; and T4 (four pairs) which must raise the C-5
     halt before any M is read. Through the same functions the evidence unit calls; no fixture-specific branch.
C-4  sha256(data/ame2012/AME2012.txt) equals the pin. Diagnostic: the row count, recorded, not gated, not printed.
C-5  n >= 5, inside the evidence unit, before any M is read.
C-6  the evidence unit reproduces the predict unit's recorded prediction-file sha256 and finds every scored A in
     the sealed prediction array.

## FORMS (exhaustive; pre-registered; one on every terminal verdict)
Q1: U-AGREES / U-MISS-HIGH / U-MISS-LOW / U-OPEN-BAND (the floor straddles or touches a band edge from outside; no
side read; a clean open result) / U-NULL-FLOOR (h > B1; no sign read) / INSTRUMENT-OPEN (any halt, credential
failure, exception or n < 5; its reason names the unit that halted, so a halt before any evidence was read is told
from one after it). Rules 1 to 5 partition every (mean, h) with h >= 0.

## WHAT COUNTS (locked; design section 7)
Each form yields one rider on NUC-018 and a line in the Coulomb cell of NORTH_STAR section 2, worded in full in
design section 7: U-AGREES, the term confirmed on a calibration-free channel at 8.5 percent, with the equal-weight
caveat, the charge-symmetry-breaking caveat and the non-formation caveat in the sentence; U-MISS-HIGH or -LOW, the
term's own measured bias with its sign on this channel, kept at full weight, the cell's text gaining "(mirror
channel: X)"; U-OPEN-BAND and U-NULL-FLOOR, clean open and null results with full credit and the per-pair table
published; INSTRUMENT-OPEN, no rider. Grade D2 unchanged under every form. Targets moved 0, inputs retired 0,
discriminators armed 0; the release note says so in those words. Not a T1 prediction (AME2012 predates the model).

## NO-RESCUE RULE
No pair excluded for its residual; no regional re-scoring; no amended term scored under this name. A miss is kept
at full weight on the row.

## HYGIENE (the order of the evidence, stated)
The table has been in the repository since before the model; the defence is the construction, not the order: the
predictions are a frozen function with no constant to fit, written and sealed before the table is opened, and the
evidence unit is bound to that file by hash. The executor's sandbox ran one scratch script that imported the sealed
instrument for the constants in the design and opened no table and no checkpoint, then the smoke on the fixtures;
the executor has read no mass of any mirror pair and does not know n. The worker runs LAB_SMOKE=1 only.

## PROCEDURE (nothing waits on a person)
1. The lab locks under author-kit mode; the driver runs its three units on the lab machine; the evidence unit
   reads the table once.
2. The verdict renders once; results to analysis/NUC_MIRROR_LEAN_2_results.md with the rider of WHAT COUNTS.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
1. No evidence cell was computed, previewed or counted. The constants in the design are the sealed code's returns
   from a scratch script that opened no table; the fixture values are planted arithmetic on those constants and
   the code's own bootstrap on the fixed seed; the smoke scored fixture T's F1 payload only.
2. The seven earlier designs of this question measured nothing (none locked). NUC-MIRROR-LEAN's external lock
   objections are cured as stated in WHERE IT STANDS and design DISCLOSURES 3; its skeptical round-one objections
   (the floor-protected band rule, a fixture for every form, the U-AGREES wording) are kept as its round two left
   them.
3. Expectations, stated so they cannot be mistaken for results: the executor expects U-MISS-HIGH; no bar depends
   on it.

## NORTH STAR ACCOUNTING
Interior work under section 5 (names no target moved, no input retired, no discriminator armed; reconstruction
work on the weights-of-atoms row's Coulomb cell). Permitted as the one interior session after NUC-NEW-5 (locked
6e7a56a, 31 October 2026, target-facing, promoted as NUC-031, PR #11); no interior session has locked since; the
session after this one must be target-facing. The author's reading for this one commission (section 5, bar W, the
floor item) is recorded in NORTH_STAR section 5 under this name. Moves no number in section 2b.

## STANDING
Draft, 2026-11-04, on the queue branch for the Director's proposal under author-kit mode.

```lab
commission: NUC-MIRROR-LEAN-2
target: "Weights of atoms row (section 1), the Coulomb cell: whether the derived uniform-sphere Coulomb term a_C = 0.7716 MeV (d0 = 2.026 fm, no constant fitted to a mass), scored alone on the AME2012 T = 1/2 mirror displacement energies at A >= 13, the channel in which the Ca-40 calibration, the surface term and the symmetry term cancel exactly, with the predictions sealed before the table is read, lies inside the coefficient's registered 8.5 percent band above a locked floor; interior work, the one interior session after NUC-NEW-5 under NORTH_STAR section 5 with the author's reading recorded there; moves no North Star number; nothing waits on a person; no count, no preview, no draw"
driver: benchmarks/lab/nuc_mirror_lean_2/driver.py
verdict_script: benchmarks/lab/nuc_mirror_lean_2/verdict.py
instrument:
  - benchmarks/lab/_kit/labkit.py
  - benchmarks/lab/nuc_new_5/driver.py
  - data/ame2012/AME2012.txt
  - analysis/NUC_MIRROR_LEAN_2_design_SEALED.md
forms: [U-AGREES, U-MISS-HIGH, U-MISS-LOW, U-OPEN-BAND, U-NULL-FLOOR, INSTRUMENT-OPEN]
state: [analysis/nuc_mirror_lean_2_ckpt.pkl]
budget: {cpu_hours: 0.05, usd: 0}
mem_gb: 1
```
