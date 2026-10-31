# NUC-NEW-3 -- EVIDENCE DESIGN, SEALED BEFORE THE INSTRUMENT WAS AMENDED (2026-10-31)

Supersedes analysis/NUC_NEW_2_design_SEALED.md (commit 46b6ec6) for the commission NUC-NEW-3. Every section of
that design stands unchanged for NUC-NEW-3 except credential C-6(b), restated below; it is not repeated here. The
evidence set, its pins, the models, the statistics, the bars and the forms are those of the NUC-NEW-2 design
(sections 1 to 8), which in turn kept the set, the models and Q1 of the NUC-NEW-1 design (e38870c). Queue rule 3
holds: this file is committed before the NUC-NEW-3 kit exists; nothing below changes afterwards; a change is a
new name.

## 0. Why a third name

The NUC-NEW-2 design fixed, before the real-file audit ran, the bar C-6(b): at least 0.99 of the shared rows
(AME2012 experimental rows that are experimental in AME2020) agree within 0.100 MeV. The audit ran on
2026-10-31 13:10 UTC (tools/ame2020_newset.py --audit, by the author, commit 87c21e5; AUDIT.json sha256
2a92fe6a...) and returned: shared 2421; within 0.100 MeV 2361 (0.9752); beyond 60; largest absolute shift among
the shared rows 1.3600 MeV; counts equal to the manifest's. The bar fails as sealed. Under the NUC-NEW-2 design a
credential failure is INSTRUMENT-OPEN, and a sealed design is not amended, so NUC-NEW-2 is closed before any
evidence was read; the failure is recorded in analysis/queue/README.md and here.

The failure is the bar's, not the parser's. A column, unit or flag misparse shifts essentially every row by
tens of MeV; here 2421 of 2438 AME2012 rows are matched, the five anchors agree within a kilovolt, 0.9752 of the
shared rows agree within 0.1 MeV, and the sixty that moved further are AME2012 rows re-evaluated in AME2020
(the kind of shift the AME series records for nuclides whose earlier value rested on one measurement). The 0.99
was the executor's prior, taken from a reviewer's illustrative figure, with no basis in the tables.

## 4(b). Credential C-6(b), restated (the only change)

Disclosure first: this bar is fixed with the NUC-NEW-2 audit in view. The executor knows the shared-row
agreement (0.9752 within 0.1 MeV; 60 beyond; largest shift 1.36 MeV). The executor still knows no value of T,
and the audit reads no row of T; the shared rows are AME2012 rows the models already scored in-sample under
NUC-BLIND-1 and -2.

C-6(b)  Among the shared rows, the fraction whose AME2020 mass excess agrees with AME2012's within 0.100 MeV is
        at least 0.90, and the largest absolute shift among the shared rows is at most 5.0 MeV. The two numbers
        are set by what the check is for: a misparse of the AME2020 layout moves nearly every shared row by more
        than 0.1 MeV (failing the first) and the typical row by tens of MeV (failing the second); a
        re-evaluation of individual poorly measured nuclides does neither. The count beyond 0.1 MeV and the
        largest shift are recorded in AUDIT.json and printed by the verdict, so a reader sees them beside the
        bar.

C-6(a), (c) and the rest of the NUC-NEW-2 design's section 4 are unchanged (the file's sha256 equals the pin;
shared rows at least 2389; experimental rows between 2400 and 2700; AME2012 rows absent at most 50; the audit's
hashes equal the pins; the audit is written once).

## Everything else

By reference to analysis/NUC_NEW_2_design_SEALED.md: the pins (|T| = 128; ame2020 e8599c6d...; labels
2387278...; test 71658bb6...); the models; C-1 to C-5; the Q1 bars; the Q2 ratio with the sampling floor F
(bootstrap, seed 20261031, 10000 resamples, 50 against 128, 99th percentile, on the 100 published in-sample
residuals per model); the Q3 permutation null and no-claim rule; the forms BLIND-AGREES, BLIND-FAILS,
BLIND-INCOMPLETE, EXTRAPOLATES, WITHIN-FLOOR, DRIFTS, NEW-SET-TOO-SMALL, INSTRUMENT-OPEN; what counts; the
rules. The hold-out directory keeps the name NUC_NEW_1. The executor's prior, stated and not leaned on: Q1 both
AGREE; Q2 open for both.
