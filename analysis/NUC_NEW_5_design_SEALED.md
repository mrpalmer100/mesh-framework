# NUC-NEW-5 -- EVIDENCE DESIGN, SEALED BEFORE THE INSTRUMENT WAS AMENDED (2026-10-31)

Supersedes analysis/NUC_NEW_4_design_SEALED.md (076e183) for the commission NUC-NEW-5. The NUC-NEW-2 design
(46b6ec6) stands for everything not restated here or in 076e183 (whose C-6(b) demotion and C-7 stand). Queue
rule 3 holds: this file is committed before the NUC-NEW-5 kit exists; nothing below changes afterwards; a change
is a new name.

## 0. Why a fifth name

NUC-NEW-4 went through three lock rounds on 2026-10-31 (10:03 to 10:11 local): the external reviewer passed in
round 2 and the skeptical reviewer in round 3, but no round had both, and the parking rule took the name. The
objections, each accepted here:
1. C-6(c)'s count bands (shared >= 2389; experimental in [2400, 2700]; absent <= 50) were halt-grade and were
   written in 46b6ec6 with the build counts (2421, 2550, 17) known: the same defect as NUC-NEW-3's re-set bar,
   disclosed but not cured. Remedy: the bands become recorded diagnostics that gate nothing, like C-6(b). The
   equality "the audit's counts equal the manifest's counts" is kept as halt-grade; it is a consistency check,
   not a threshold.
2. C-6(a) promised that the audit's four provenance hashes equal the pins, but the driver checked three; the
   audit's ame2012_sha256 was not compared with the pin. Remedy: it is, halt-grade, with a halt on absence.
3. C-1 credentials the model arithmetic with the Ca-40 binding read from NUC_BLIND_2/train.txt, while the
   predict unit calibrates from data/ame2012/AME2012.txt; nothing tied the two, so "byte-identical to the
   adjudicated models" was asserted, not proved. Remedy: the credential unit records b_ca (from train.txt) and
   each model's a_V; the predict unit requires its b_ca (from AME2012.txt) and each a_V to equal the recorded
   values to 1e-12, halt-grade; the seal gate requires that record.
4. The BLIND-AGREES rider's phrase "blind-scored on new measurements" overstates the test: the 128 masses were
   published (2012 to 2020; AME2020 in 2021) before the models' registration (2026); the blindness rests on the
   programme's non-inspection, which the record cannot externally verify. Remedy: section 7 reworded below.

## 4. Credentials (as 46b6ec6 and 076e183, with these restatements)

C-1  Reproduction (byte equality with NUC-BLIND-2's sealed prediction files) AND binding to the run: the
     credential unit records b_ca2 (Ca-40 binding from NUC_BLIND_2/train.txt) and a_V per model; the predict
     unit halts unless its b_ca from data/ame2012/AME2012.txt equals b_ca2 to 1e-12 and each a_V equals the
     recorded one to 1e-12. The seal gate requires the record and the predict unit's pass.
C-6  (a) halt-grade: the audit's ame2020, ame2012, labels and test hashes each equal the pins (absence halts).
     (b) DIAGNOSTIC (076e183): shared-row agreement, count beyond, largest shift; no threshold.
     (c) DIAGNOSTIC: the counts (shared, experimental, systematics, AME2012 rows absent, new with A < 12) are
         recorded and printed; no band is applied to any of them. Halt-grade and kept: the audit's counts equal
         the manifest's counts, field by field (a consistency check between two records of the same build).
C-2 to C-5 and C-7 unchanged.
The pre-truth gate: C-1 (both parts), C-2, C-3, C-4, C-5, C-6(a), the C-6(c) equality and C-7.

## 7. What counts (46b6ec6 section 7 with the rider reworded)

Q1 BLIND-AGREES for a model: a rider on that model's claim (NUC-018; NUC-A and NUC-B): "scored on the 128 AME2020
  nuclides absent from AME2012, never inspected by the programme (published before registration): rms/max
  percent of mass; an out-of-sample confrontation of a frozen model, not a prediction of unmeasured
  quantities"; the scorecard row's grade column adds "scored out of sample on the 128 AME2020 nuclides absent
  from AME2012". A fail is a kept rider with the numbers and the sample-size note. No status change either way;
  the NUC-BLIND riders stand.
Q2, Q3, section 2b, target-facing: as 46b6ec6.

## Everything else

By reference to 46b6ec6 (the question, the set and its pins, the models, the statistics, Q1 and Q2 bars, the
floor F, the Q3 null and no-claim rule, the forms, the rules) and 076e183 (C-6(b) diagnostic; C-7). The hold-out
directory keeps the name NUC_NEW_1. The executor's prior, stated and not leaned on: Q1 both AGREE; Q2 open.
