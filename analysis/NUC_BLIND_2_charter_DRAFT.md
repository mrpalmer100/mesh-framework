# COMMISSION NUC-BLIND-2 -- THE SAME MODELS, A SEED HELD BY SOMEONE OTHER THAN THE AUTHOR
# (CHARTER, DRAFT 2026-10-08 for the author's lock; no step has run; the draw is a third party's)

North Star line (section 5): (c) arms the discriminator a second time with one change of process, so that the
result can count where NUC-BLIND-1's could not. NUC-BLIND-1 (analysis/NUC_BLIND_1_results.md) returned
BLIND-AGREES for both pre-registered models on 50 isotopes drawn by the author; section 2b's "externally
adjudicated predictions" stayed 0 because the draw was the author's. This commission repeats the confrontation
with the seed chosen and the draw run by a person who is not the author and not the commission, so that a pass
is the programme's first externally adjudicated prediction (0 to 1) and a failure is a kept Failed. Nothing
about the models changes; the two already-sealed prediction scripts are reused unchanged.

## The models (B-2: fixed, the same two, nothing added)
  M1  NUC-018 three-term (a_S/a_V 1.34, a_C derived at d0 = 2.026 fm, a_V calibrated once on Ca-40 from the new
      training table; asymmetry and pairing omitted), exactly benchmarks/nuclear/nuc_blind_1.py's M1.
  M2  LAMED's baseline four-term (a_S/a_V 1.108, the same a_C, a_A = 19.85 MeV derived, a_V on Ca-40), M2 of the
      same script. The script is re-pointed at the new hold-out name and otherwise unchanged (diff recorded).

## The draw (W1; the adjudicator's, not the author's and not the sandbox's)
  The adjudicator (named at lock; a person who is not the author) chooses the seed without telling the author
  in advance, and runs on the author's PC or on any machine with the repo:
    python tools/holdout_draw.py --name NUC_BLIND_2 --seed <adjudicator's seed> --n 50 --drawn-by "<adjudicator>"
  The three sha256 lines and the adjudicator's name go into this charter at lock. Overlap with NUC-BLIND-1's
  test set is allowed and expected (about one isotope at random) and is recorded, not removed: removing rows
  after a draw is a leak. The sandbox never opens sealed/test.txt; NUC-BLIND-1's VERDICT files, which hold its
  50 truths, are not read by the N1 script (it reads train.txt and the manifest labels only, as before).

## Steps
  N1  (sandbox) nuc_blind_1.py with the hold-out name NUC_BLIND_2 (one constant changed, the name; the diff
      goes in the results file): predictions for M1 and M2 at the new labels from the new train.txt's Ca-40.
  N2  (sandbox) seal --label M1 and --label M2.
  N3  nothing.
  N4  (the adjudicator or the author, on the machine holding sealed/test.txt) verdict --label M1 / M2
      --unit mass --bar-rms 0.25 --bar-max 0.60, each once.
  N5  (sandbox) nuc_blind_1_subreading.py on the NUC_BLIND_2 VERDICT files (same correlations).

## Bars (to be LOCKED; identical to NUC-BLIND-1)
B-1  percent of mass; BLIND-AGREES rms <= 0.25 and max |r| <= 0.60; BLIND-FAILS otherwise; BLIND-INCOMPLETE on
     any unpredicted row.
B-2  both models scored, nothing added, no re-fit, no exclusion after the truth is read.
B-3  the sub-reading changes nothing.
B-4  the prior, stated and not leaned on, and now informed by NUC-BLIND-1: both AGREE (M1 near 0.12/0.22, M2
     near 0.011/0.026). A prior that is right is not a result; the draw is.
B-5  the seed is the adjudicator's; recorded; no redraw; the author does not see the seed before the draw.
B-6  what counts: a pass under this charter moves section 2b's "externally adjudicated predictions" from 0 to 1
     for the model(s) that pass, with the adjudicator named; a fail is registered Failed and kept, and the
     NUC-BLIND-1 riders are not withdrawn (they record a different draw).

## Verdict forms (to be LOCKED)
BLIND-AGREES (per model)   the model's claim takes a rider "externally adjudicated on 50 held-out isotopes drawn by
                           <adjudicator>: rms/max"; section 2b moves to 1; the scorecard row's grade column reads
                           "blind-scored, externally adjudicated".
BLIND-FAILS (per model)    kept; rider; section 2b stays 0; the row says "fails blind at <max> under external draw".
BLIND-INCOMPLETE           instrument fault, recorded.

## Rules
No rescue; the truth is read once after the seal; the sandbox never reads the sealed test file; riders the
author's; the adjudicator's name is in the record.

## Cost
Minutes. The only cost is the adjudicator's five minutes and the author's discipline about the seed.

## Author's lock
(pending; the adjudicator's name and the three sha256 lines go here)
