# COMPOSITE-SELECT Leg B: verdict tooling built and dry-run ahead of LADDER COMPLETE (2026-10-04)

Built: benchmarks/foundations/composite_legB_verdict.py (QB and the QC table from the sealed
checkpoint, once); tools/legb_verdict_dryrun.py (five synthetic ladders, one per form). All five
forms read as expected on the new cells alone. The price route (truestate_stage2.Grid.price on
QTGrid.to_stage2) was checked on the registered 4/3 member: Sigma_wave = 2.5987 T0 (the level-1
value Leg A reported, 2.598 to 2.609). The share formula 1 - T0/Sigma_wave reproduces the exact
lower edge 0.615 at 2.598 (FND-132's "excess over booked / total"). Nothing in the Leg B
checkpoint was read beyond phase and point counts; the repository copy is the stale 7/5-ramp
checkpoint, not the Mac's.

## A finding about the locked statistic, reported before the data exist

D4 reads QB by Spearman rho of D against q and against N1 "over all cells", and D3 says the
ladder is the six new cells "plus the four existing cells as data". The existing cells' D values
are registered: 3/2 at q 1.500 D 9.56x, 4/3 at q 1.333 D 5.31x, 5/3 at q 1.667 D 1.11x (5/4's D at
the matched definition is not on disk here and must be entered from FND-163/164's records). Those
three points are themselves non-monotone in q (a peak at 3/2) and anti-ordered in N1 (N1 = 2, 3, 3
carry D 9.56, 5.31, 1.11).

Consequence, by brute force over every ranking the six new cells could take with the three
existing cells fixed: the largest |rho(D, q)| attainable is 0.767, below the 0.8 the RAT-SMOOTH
form requires. A ladder that tracks the order perfectly (D set by N1 alone) gives |rho(D, N1)| of
about 0.51 once the existing cells are in. So, with the ladder as locked, RAT-SMOOTH cannot fire
at all, RAT-RESONANT can fire only barely, and the likely readings are RAT-MIXED or the charter's
"anything else: NO CALL". Adding 5/4 (q 1.25) moves these numbers somewhat and is included in the
script when its D is entered; it does not lift the 0.8 ceiling for a D that peaks near 3/2.

This is not a reason to change anything now. The charter's NO-RESCUE rule forbids a re-choice of
the rank statistics and of the cell set after Leg B opened, and that rule is correct: a statistic
re-chosen after the ladder exists is a statistic chosen to fit it. The honest course is to run the
verdict as locked, record RAT-MIXED or NO CALL if that is what comes, and let the finding above be
the explanation on the results file's face: the form was under-powered by its own inclusion of
non-monotone registered cells, discovered in a dry run before the data. A successor charter can
state the order test on the new cells alone, or on a longer ladder, with that lesson in hand.

The same dry run shows the QC table is independent of this: rows (ii) and (iii) price whatever
the ladder gated, and Prediction 32's upper edge follows from the price alone.

## What remains for LADDER COMPLETE day

1. Copy the Mac's analysis/composite_legB_ckpt.pkl into the tree (the Mac is the one machine for
   this job; the verdict can run there or here on the copied file).
2. If 5/4's matched-definition D is to enter the ladder, write it into
   analysis/composite_legB_existing_D.json as {"5/4": {"D36": <value>, "source": "FND-163/164"}}
   from the registered records, before the verdict runs; otherwise the script says it is out.
3. Run: python benchmarks/foundations/composite_legB_verdict.py | tee analysis/COMPOSITE_SELECT_legB_verdict.log
4. Leg D: the results doc and analysis/SIGMA_WAVE_decision_memo.md with hold and retreat both
   priced; no draft claim before the author reads.
