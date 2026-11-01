# NUC-NEW-2 -- EVIDENCE DESIGN, SEALED BEFORE THE INSTRUMENT WAS AMENDED (2026-10-31)

Supersedes analysis/NUC_NEW_1_design_SEALED.md (commit e38870c) for the commission NUC-NEW-2. NUC-NEW-1 was
proposed by the Director on 2026-10-30 22:55 within a minute of the kit landing, failed three lock-review rounds
(skeptical and external) on the objections listed in section 0, and was parked WITHDRAWN at 23:06; under the lab's
rule a withdrawn name stays taken. The evidence set, the models, the Q1 statistics and the Q1 bars of the first
design are unchanged and are not restated as new; what this file changes is listed in section 0 and written out in
the sections that follow. Queue rule 3 holds: this file is committed before tools/ame2020_newset.py, the driver or
the verdict are touched for NUC-NEW-2; nothing below changes afterwards; a change is a new name.

## 0. What the review found, and what this design does about it

1. Autonomy: the first charter had steps waiting on a person (download, build, choose a variant, an expectation
   to be recorded at lock). The hold-out was built by the author on 2026-10-31 11:25 UTC (commit 7d23981) before
   this file; nothing in NUC-NEW-2 waits on anyone. The adjudicated variant and the VERDICT_M*.json ingestion
   path are deleted. Section 2b "externally adjudicated predictions" is unchanged by construction.
2. Pinning: the sha256 of the AME2020 file, of labels.txt and of sealed/test.txt, and |T|, are fixed here and in
   the driver's CONFIG; the manifest unit halts on any difference. The manifest's hashes are checked against the
   pins, never trusted.
3. Verdict binding: the sealed rows plus the missing labels must equal the sealed label set exactly (unique,
   disjoint); every scored prediction must equal its sealed prediction to 1e-9; the truth is read once as ONE raw
   payload, hashed against the pin and against the hash the manifest unit recorded, sealed raw, and both models'
   rows derive from that one payload. A missing prediction renders BLIND-INCOMPLETE on Q1 and on Q2 for that
   model (no statistic on the surviving subset; the all-missing case included).
4. Q2 floor: the factor 2 stays as the registered reading but no longer carries the decision alone. A sampling
   floor is computed before the truth is read, from a disjoint resource (section 6), and DRIFTS requires the
   observed ratio to exceed both 2 and the floor; a ratio above 2 but not above the floor renders WITHIN-FLOOR.
5. Q3: a permutation null (section 6) is computed beside each correlation, and Q3 carries no claim: no rider may
   quote a Q3 number. This is stated in the verdict output itself.
6. Real-file sanity: beyond the five anchors, the tool gains an audit of the real file (section 4, C-6) with bars
   fixed here before the audit runs: agreement of the shared AME2012 rows within a stated tolerance, counts in a
   stated band. The audit writes AUDIT.json beside the manifest; the manifest unit halts without it or on a bar
   failure (INSTRUMENT-OPEN).
7. Text: the AME2020 measurements (2012 to 2020) predate the models' registration (2026); they are measurements
   this programme has never inspected, not data that did not exist. Q2 tests a fixed rms ratio, not equality of
   error distributions; DRIFTS does not by itself identify NUC-026's mechanism. The 0.60 max bar was fixed for
   50-row samples and is applied unchanged to 128 rows, so a BLIND-FAILS driven by max alone is partly a
   sample-size effect; the results must say so.
8. Hygiene: sealed/test.txt was committed to the queue branch (7d23981) before the seal unit ran, as GRV-BLIND-2
   did. The defence is the models, not the order: M1 and M2 are frozen functions of (Z, N) and AME2012's Ca-40,
   credentialed byte for byte against NUC-BLIND-2's sealed predictions (C-1), so no reading of the truth could
   change a prediction without failing C-1. The sandbox excluded sealed/ from its working tree (sparse checkout)
   and holds labels and manifest only. The order is stated in the charter.

## 1. The question (unchanged in substance; wording corrected per 0.7)

Do the two adjudicated nuclear mass models, frozen as sealed for NUC-BLIND-2 and calibrated once on AME2012's
Ca-40, predict the masses of the 128 nuclides whose masses were first measured between AME2012 and AME2020 (data
this programme has never inspected; the repository holds AME2012 only) inside the registered accuracy, and does
their off-valley rms stay within a fixed ratio of the adjudicated in-sample rms?

## 2. The evidence set (unchanged; now built and pinned)

T as defined in the first design, section 2 (AME2020 experimental, A >= 12, not an AME2012 row). Built once,
2026-10-31 11:25 UTC, by the author on the lab machine from the AMDC file served by the AMDC mirror at IMP
Lanzhou (the IAEA host sits behind a browser challenge), committed as 7d23981:
  |T| = 128.  AME2020: 3558 rows, 2550 experimental, 1008 from systematics; shared with AME2012: 2421 of 2438;
  AME2012 rows absent from AME2020: 17; new rows with A < 12: 1 (excluded by scope).
  ame2020 sha256 e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307  (mass_1.mas20, 472648 bytes)
  ame2012 sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13  (data/ame2012/AME2012.txt)
  labels  sha256 2387278737460b207fc8b4d5637ad5426cfe4f0981686ee187fac20f2012298a  (analysis/holdout/NUC_NEW_1/labels.txt)
  test    sha256 71658bb61b80507f68e2d1e19b5cc56fa4853447c848a4568137771b37b6534b  (analysis/holdout/NUC_NEW_1/sealed/test.txt)
The hold-out directory keeps the name NUC_NEW_1 (it is the same set; the design fixes the set, not the commission
name). These four hashes and |T| = 128 are the pins of 0.2. The labels run from A = 15 to A = 266 and Z up to 109.
No value of T has been read by the executor or by any lab agent.

## 3. The models (unchanged)

Exactly the first design's section 3: M1 (NUC-018 three-term) and M2 (four-term, a_A = 19.85 MeV derived), a_V
calibrated once on AME2012's Ca-40, credentialed byte for byte (C-1).

## 4. Credentials (C-1 to C-5 unchanged; C-6 added; all halt-grade, all before any prediction is sealed)

C-1  Reproduction of NUC-BLIND-2's sealed prediction files, byte equality (unchanged).
C-2  The residual rule reproduces NUC-BLIND-1's and NUC-BLIND-2's published VERDICT_M1/M2.json rows, rms and max
     to 1e-9 (NUC-BLIND-1 is added because section 6 draws on its rows).
C-3  The parser on the synthetic fixture (unchanged), and the audit mode of the tool on the same fixture: every
     shared row agrees exactly, the planted counts are recovered.
C-4  The five anchors within 0.010 MeV (unchanged; recorded in MANIFEST.json, re-verified by the manifest unit).
C-5  labels.txt: no AME2012 row, no A < 12, no duplicate, hash equal to the pin (unchanged, now against the pin).
C-6  Real-file audit, written by `tools/ame2020_newset.py --audit` on the machine holding the AME2020 file, read
     by the manifest unit, bars fixed here before the audit runs:
       (a) the file's sha256 equals the pin (the counts of section 2 are then fixed by the file);
       (b) among the shared rows (AME2012 experimental rows that are experimental in AME2020), the fraction whose
           AME2020 mass excess agrees with AME2012's within 0.100 MeV is at least 0.99. The tolerance is ten times
           the anchor tolerance, chosen so that a column or flag misparse (which shifts values by MeV or more)
           fails it while ordinary re-evaluation does not; it is not derived from any value of T, and the executor
           has not seen any shared-row shift beyond the five anchors. The audit records the count
           within, the count beyond, and the largest absolute shift among the shared rows (AME2012 rows, not
           evidence); it reads no new row;
       (c) shared rows at least 2389 (0.98 x 2438); experimental rows between 2400 and 2700; AME2012 rows absent
           from AME2020 at most 50. Disclosure: the counts were printed by the build and are known (2421, 2550,
           17); the bands are stated so that a re-run on a different file fails them; (b) is not known at this seal.
     The audit also records the labels and test hashes it finds, which must equal the pins. The audit writes
     AUDIT.json once and refuses a second write.
The pre-truth gate: C-1 to C-6 pass in the checkpoint, else the seal and truth units refuse and the truth is
never read. A credential failure is INSTRUMENT-OPEN.

## 5. The statistics (Q1 unchanged; the Q2 ratio stated; Q3 null added)

Per model, over the scored rows: r_i = 100 (B_pred - B_truth) / m_atom; rms; max |r_i|; the five worst rows.
Q2 ratio: rho = rms(T) / rms_ref, rms_ref the model's NUC-BLIND-2 adjudicated rms read from VERDICT_M*.json
(M1 0.13798832, M2 0.01599755).
Q3: Pearson r of r_i with the declared omission channels (unchanged), each beside a permutation null: 1000
label permutations of r_i against the channel, seed 20261031, the null's 99th percentile of |r|, and the
percentile of the observed |r| in the null.

## 6. The bars and the forms (Q1 unchanged; Q2 floor added; Q3 null; incomplete handling)

Q1 (per model): BLIND-AGREES (rms <= 0.25 and max <= 0.60 percent of mass); BLIND-FAILS; BLIND-INCOMPLETE (any
  label without a prediction, the all-missing case included).
Q2 (per model): BLIND-INCOMPLETE if any label is unpredicted. Otherwise:
  EXTRAPOLATES    rho <= 2
  WITHIN-FLOOR    2 < rho <= F
  DRIFTS          rho > 2 and rho > F
  F, the sampling floor, computed in the credential unit before the truth is read, from a disjoint resource: the
  model's 100 published in-sample residuals (NUC-BLIND-1's 50 and NUC-BLIND-2's 50, both AME2012 draws, disjoint
  from T by construction). Bootstrap, seed 20261031, 10000 resamples: each resample draws 50 residuals with
  replacement for a reference rms and 128 (= |T|) with replacement for a test rms, from the pooled 100; F is the
  99th percentile of test rms / reference rms. F answers "how large a ratio does sampling alone produce at these
  sizes when the residual distribution is the same"; it is fixed before any value of T is read and recorded in
  the checkpoint. If F exceeds 2, WITHIN-FLOOR is live; if not, it cannot render.
Q3 (per model): no form, no claim. Each correlation is printed with its null percentile and the phrase "Q3
  carries no claim; no rider may quote it", which binds the rider text.
NEW-SET-TOO-SMALL: |T| < 30 (cannot render: |T| = 128 is pinned; kept so the rule is complete).
INSTRUMENT-OPEN: the open form.
FORMS: BLIND-AGREES, BLIND-FAILS, BLIND-INCOMPLETE, EXTRAPOLATES, WITHIN-FLOOR, DRIFTS, NEW-SET-TOO-SMALL,
INSTRUMENT-OPEN. QUESTIONS: Q1-M1, Q1-M2, Q2-M1, Q2-M2.

## 7. What counts (locked)

Q1 BLIND-AGREES for a model: a rider on that model's claim (NUC-018; NUC-A and NUC-B): "blind-scored on the 128
  nuclides first measured between AME2012 and AME2020: rms/max"; the scorecard row's grade column adds
  "blind-scored on new measurements". A fail is kept as a rider with the numbers, with the sample-size note of
  0.7 when max alone fails. No status change either way; the NUC-BLIND riders stand.
Q2: a rider on the same claims with rho, F and the form. DRIFTS for M2 is recorded as an out-of-sample shortfall
  of the four-term form; it does not identify NUC-026's quartic or surface-symmetry companion, which stays a
  priced, uncommissioned item.
Q3: nothing. No rider quotes a Q3 number.
Section 2b: unchanged by construction (the author built the set; no adjudicator holds anything).
Target-facing (NORTH_STAR section 5): the "Weights of atoms" row and its discriminator.

## 8. Rules

No row removed after the truth is read; no re-fit; no second verdict; the sandbox never holds the AME2020 file;
the sandbox's working tree excludes sealed/. The executor's prior, stated and not leaned on: Q1 both AGREE; Q2
open for both.
