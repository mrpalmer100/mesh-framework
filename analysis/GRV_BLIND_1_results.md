# COMMISSION GRV-BLIND-1 -- RESULTS (the PC, 2026-10-09; the sealed truth read once; verdict computed once)

Charter: analysis/GRV_BLIND_1_charter_LOCKED.md (locked after the author's draw, seed 52525254, and before the seal).
Prediction: GRV-030's g_obs = g_bar nu(g_bar/g_dagger), g_dagger = c H0 / 2 pi = 1.083e-10 m/s^2, nothing fitted;
734 points sealed (sha256 f15f0e37...) before the truth was read. Bars by the locked rule from the 125 training
galaxies: rms <= 0.1800 dex, worst galaxy <= 0.6321 dex (analysis/GRV_BLIND_1_bars.json). Verdict on the PC with
tools/holdout_galaxies.py; analysis/holdout/GRV_BLIND_1/VERDICT.json kept; log analysis/GRV_BLIND_1_verdict.log.

## VERDICT: BLIND-AGREES

| statistic | held-out (30 galaxies, 634 kept points) | bar | training (125) | whole table (GRV-030, 155) |
|---|---|---|---|---|
| rms residual, dex, at the predicted g_dagger | 0.1138 | <= 0.1800 | 0.1496 | 0.1423 |
| worst per-galaxy rms, dex | 0.3803 (F568-V1) | <= 0.6321 | | |
| mean residual, dex | +0.0333 | (sub-reading) | | |

Worst five galaxies: F568-V1 0.380, F571-8 0.245, UGC05721 0.239, UGC02487 0.182, UGC08286 0.179 (two low-surface-
brightness F-galaxies and three dwarfs, where the RAR scatter is known to be largest; none BLIND-INCOMPLETE).

## Sub-reading (G5; computed from the kept rows; changes nothing)
At the registered data-fitted g_dagger (1.134e-10) the held-out rms is 0.1117 dex against 0.1138 at the predicted
value: the same 0.002-dex indistinguishability GRV-030 reported on the whole table, reproduced out of sample. The
mean residual +0.033 dex is positive (the held-out galaxies sit a little above the prediction); the g_dagger that
would zero it on this subsample is 1.36e-10, 26 percent above the prediction, where the whole-table fit found 4.5
percent. The rms is nearly flat in g_dagger over that range, so the mean is a weak lever and the subsample's offset
is within what thirty galaxies can do; it is recorded, not read. Low-acceleration half (g_bar < g_dagger, 465
points) mean +0.036; high half +0.026: no trend across the relation.

## What the result is
The programme's best D1 content held under its own standing bar: a prediction with no free parameters, frozen
before the held-out observations were read, agrees with thirty galaxies it was not scored on, at an rms tighter
than the training set's. It is an out-of-sample confrontation, not external adjudication (the author's draw), so
section 2b stays at 1. The held-out rms being below the whole-table rms is sampling (the draw happened to take
better-behaved galaxies on average: the training rms rose to 0.150 as the held-out rms fell to 0.114; together
they are the whole table's 0.142); the bar was set from the training distribution precisely so that this cuts
neither way. What it does not do: it does not retire H0 as an input, does not touch Prediction 4's wounded shape
(GRV-030 R2), and does not change GRV-030's status (Modeled; the confrontation line is what moves).

## Consequences (riders on the author's word)
GRV-030: rider: blind-scored 2026-10-09 under bar W on 30 held-out SPARC galaxies drawn by the author (seed
  52525254; 634 kept points): BLIND-AGREES at rms 0.114 dex (bar 0.180 from the training bootstrap), worst galaxy
  0.380 (bar 0.632); at the data-fitted g_dagger the rms is 0.112, the same indistinguishability out of sample;
  mean residual +0.033 dex recorded. The first blind confrontation of a D1 claim.
docs/NORTH_STAR.md, "Gravitational force" row, grade column: "D1 (g_dagger on SPARC; blind-scored, GRV-BLIND-1)".
Section 2b unchanged (the author's draw). No status change.

## Named next-order (not chartered)
GRV-BLIND-2 with an adjudicator's seed, whenever one is at hand: the same sealed prediction form on a fresh draw
moves "externally adjudicated predictions" from 1 to 2, with a parameter-free observable as the second entry.
Five minutes of someone else's time; the tool, the bars rule and the predictor are all on the record.
