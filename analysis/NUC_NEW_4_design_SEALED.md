# NUC-NEW-4 -- EVIDENCE DESIGN, SEALED BEFORE THE INSTRUMENT WAS AMENDED (2026-10-31)

Supersedes analysis/NUC_NEW_3_design_SEALED.md (151ae8e) for the commission NUC-NEW-4. Every section of the
NUC-NEW-2 design (46b6ec6) stands unchanged for NUC-NEW-4 except credential C-6, restated below with C-7 added;
NUC_NEW_3's restatement of C-6(b) is withdrawn. The evidence set, its pins, the models, the statistics, the Q1
and Q2 bars, the floor F, the Q3 null and the forms are those of 46b6ec6 and are not repeated. Queue rule 3
holds: this file is committed before the NUC-NEW-4 kit exists; nothing below changes afterwards; a change is a
new name.

## 0. Why a fourth name

NUC-NEW-3 restated the failed C-6(b) bar (0.99 of the shared rows within 0.1 MeV, fixed before the audit; the
audit returned 0.9752, 60 rows beyond, largest shift 1.36 MeV) as 0.90 and 5.0 MeV with the audit disclosed.
Both lock reviewers refused it on 2026-10-31 (two rounds, 09:27 to 09:30 local): a halt-grade threshold chosen
after a preview of the statistic it gates is tuned to pass whatever the motive, and disclosure does not cure it
(checklist items B and I). They are right. NUC-NEW-2's failure stays at full weight: its sealed bar failed and
the commission closed before any evidence was read.

The skeptical reviewer named the remedy taken here: demote C-6(b) to a recorded diagnostic that gates nothing,
rely on the checks fixed before any real file was seen for the parser's credential, and say so. The external
reviewer asked that any successor credential ask a different validation question, fix its rules from stated
arithmetic or a disjoint resource, and apply them to a fresh, uninspected schedule. C-7 below does that on the
synthetic fixture (AME2012 rows reformatted plus planted rows; no AME2020 value), asking not "how far did the
shared rows move" but "do the halt-grade checks that exist catch a misparse of the layout". Its arithmetic was
run on the fixture before this seal and is stated; no number of it comes from mass_1.mas20.

## 4. Credentials (C-1 to C-5 as in 46b6ec6; C-6 restated; C-7 added; all halt-grade unless marked)

C-6  Real-file audit, AUDIT.json (written once, 2026-10-31 13:10 UTC, commit 87c21e5, sha256 2a92fe6a...).
     (a) halt-grade: the audit is of the pinned file and this hold-out (its four hashes equal the pins).
     (b) DIAGNOSTIC, gating nothing: the shared-row agreement within 0.100 MeV (2361 of 2421; 0.9752), the
         count beyond (60) and the largest shift (1.3600 MeV) are read, recorded in the checkpoint and printed by
         the verdict as the NUC-NEW-2 audit result, labelled "diagnostic; NUC-NEW-2's 0.99 bar failed on it".
         No threshold is applied to them under this or any later name on this file.
     (c) halt-grade, unchanged from 46b6ec6: shared rows at least 2389; experimental rows between 2400 and 2700;
         AME2012 rows absent from AME2020 at most 50; the audit counts equal the manifest counts. (Disclosed
         there and here: the counts were printed by the build and were known when these bands were written.)

C-7  Perturbation credential of the parser's detectors (new; halt-grade; runs in the credential unit on the
     synthetic fixture only; reads no real file). The fixture text is perturbed in the mas20 layout and the
     tool's build() and audit() are applied; the rule for each perturbation is fixed here from the arithmetic
     run on the fixture before this seal:
       p1  unit: the mass-excess field written in MeV instead of keV (every value divided by 1000).
           Rule: build() must REFUSE (the anchor check fails: C-12's excess is 0 by definition and passes, the
           other four shift by MeV). On the fixture: refused, O-16 delta +4.7323 MeV.
       p3  flag convention inverted: experimental rows carry '#', flagged rows lose it.
           Rule: build() must REFUSE (the experimental-row floor of 2000: nearly every row becomes systematics).
           On the fixture: refused, 1 experimental row parsed.
       p4  N and Z columns swapped. Rule: build() must REFUSE (an asymmetric anchor, Fe-56 or Pb-208, is missing;
           the three symmetric anchors cannot catch this alone, which is why the five include two asymmetric
           ones). On the fixture: refused, Fe-56 missing.
       p5  the field shifted LEFT by two or three characters (the previous column's bytes enter the field).
           Rule: build() must REFUSE (anchor check). On the fixture: refused, Ca-40 delta +69.69 MeV (shift 2);
           O-16 +9.47 MeV (shift 3).
       p6  the field shifted by ONE character either way. Rule: build() SUCCEEDS and every shared value is
           within 0.001 MeV of the unperturbed parse (the shift truncates the sixth decimal only; this is not a
           misparse in effect and the design says so rather than pretending a detector catches it).
       p7  the field shifted RIGHT by two characters. Rule: the planted set is NOT recovered (a '#' at the end
           of a 'tail'-convention field falls outside the 15-character window and the row is read as
           experimental), so C-3's set equality fails; the credential requires that failure. Real AME2020 files
           use the 'point' convention ('#' in place of the decimal point, inside the field), which no shift of
           up to four characters moves out of the window; the tail convention is the older AME files'.
     A perturbation that behaves otherwise than its rule halts the credential unit (INSTRUMENT-OPEN).

C-1 to C-5 unchanged (C-1 byte reproduction; C-2 both blind sets' VERDICT rows and the floor F; C-3 build and
audit on the fixture; C-4 the five anchors within 0.010 MeV; C-5 the labels against the pins).
The pre-truth gate: C-1 to C-5, C-6(a), C-6(c) and C-7 pass in the checkpoint, else the seal and truth units
refuse and the truth is never read.

## Everything else

By reference to analysis/NUC_NEW_2_design_SEALED.md (46b6ec6): the question; the set and its pins (|T| = 128;
ame2020 e8599c6d...; labels 2387278...; test 71658bb6...); the models; the statistics; Q1 bars; Q2 with the
floor F (bootstrap, seed 20261031, 10000 resamples, 50 against 128, 99th percentile, on the 100 published
in-sample residuals per model, computed before any evidence file is opened); the Q3 permutation null and no-claim
rule; the forms BLIND-AGREES, BLIND-FAILS, BLIND-INCOMPLETE, EXTRAPOLATES, WITHIN-FLOOR, DRIFTS,
NEW-SET-TOO-SMALL, INSTRUMENT-OPEN; what counts; the rules. The hold-out directory keeps the name NUC_NEW_1. The
executor's prior, stated and not leaned on: Q1 both AGREE; Q2 open for both.
