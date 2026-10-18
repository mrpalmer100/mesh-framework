# GRV-BARS-OC (EXPLORATORY) -- THE OPERATING CHARACTERISTIC OF BAR W's BARS RULE ON THE SPARC TABLE

Instrument study, no lock, no verdict forms. Script benchmarks/gravity/grv_bars_oc_exploratory.py; record
analysis/GRV_BARS_OC_exploratory.json (every split's seed, held-out set, bars and statistics). Run in the sandbox,
2026-10-18, 66 seconds. The sandbox is not a machine of record for sealed verdicts; nothing here is sealed.

## Exposure, stated first

The cell (the exceedance rate of rule B-1 on this table) was previewed before any lock could be written: the
withdrawn GRV-BLIND-OC's 60-split pilot and 12 previewed seeds (2026-10-15/16) and the round-1 GRV-BARS-OC-1 smoke
on six real splits whose forms were printed (2026-10-17), both on the lab's record. The lab's external reviewer
ruled that no fresh schedule could make a lock on this cell a prospective adjudication, the author agreed, and the
commission was withdrawn (2026-10-18). This study is the exploratory record that ruling asked for. Its seed schedule
is the one fixed in the author's draft of 2026-10-16 (sha256 of a fixed string, 31-bit), and no threshold is read
here: the numbers are reported with intervals and compared with the rule's nominal 5 percent in prose.

## What was run

The registered rule B-1 (grv_blind_1.bars): for a draw of 30 of the 155 eligible galaxies, the 0.95 quantile over
20,000 random 30-galaxy subsets of the 125 training galaxies of the subset rms of log10(g_obs) - log10(g_pred) at
the predicted g_dagger (the deciding bar in GRV-BLIND-1 and GRV-BLIND-2) and of the subset's worst per-galaxy rms
(the recorded outlier form). 1000 disjoint, uninspected splits; the same under bars computed once from all 155
galaxies by the same rule and held fixed (the candidate rule named in STRATEGIC_TARGETS section AL on 2026-10-13,
before this run); a synthetic control (iid Gaussian residuals, the table's per-galaxy point counts, the pooled sd)
on 1000 further splits. Credentials passed first: the registered loop reproduces GRV-BLIND-1's bars 0.180044 /
0.632099 and draw (seed 52525254) and GRV-BLIND-2's bars 0.158245 / 0.522359 and draw (seed 1083026663) exactly.

## The measurement (nominal rate 5 percent; 95 percent Wilson intervals)

| bar | rule | exceeded in 1000 splits | rate | interval |
|---|---|---|---|---|
| rms (the deciding bar) | B-1, from each split's training complement | 118 | 11.8% | [10.0, 14.0] |
| worst galaxy (recorded form) | B-1, from each split's training complement | 183 | 18.3% | [16.0, 20.8] |
| either | B-1 | 266 | 26.6% | [24.0, 29.4] |
| rms | fixed once from all 155 (0.1720) | 47 | 4.7% | [3.6, 6.2] |
| worst galaxy | fixed once from all 155 (0.6321 = the largest per-galaxy rms) | 0 | 0.0% | [0.0, 0.4] |
| rms, synthetic control | B-1 | 98 | 9.8% | [8.1, 11.8] |
| worst galaxy, synthetic control | B-1 | 185 | 18.5% | [16.2, 21.0] |

Mean split rms bar 0.1708 (sd 0.0055); mean held-out rms 0.142; its 95th percentile 0.1717.

## What the record says

1. **The deciding bar fails honest draws 2.4 times as often as it says.** 11.8 percent against a nominal 5; the
   interval excludes 5 by a wide margin. The synthetic control, with no galaxy structure at all, gives 9.8 percent:
   the excess is a property of the rule's construction, not of the galaxies. A bar computed from the training
   complement is a quantile over subsets of a pool from which the held-out galaxies have been removed; when the
   draw takes high-residual galaxies into the test, the pool's quantile falls at the same moment the test's rms
   rises. The two move against each other by construction.
2. **The outlier bar is not a 5 percent bar at all** (18.3 percent, control 18.5): a quantile of subset maxima over
   a pool that lacks the test's own maximum.
3. **The coupling is two galaxies.** The worst-galaxy bar was set by PGC51017 in 817 splits and by UGC04305 in 147;
   their rms (0.632, 0.538) are the top of the table. When either sits in the test set (339 splits) the rms bar is
   exceeded 28.0 percent of the time [23.5, 33.0]; when both sit in training (661 splits), 3.5 percent [2.3, 5.2],
   under the nominal. When both sit in the test (36 splits) the rms bar is exceeded 22 times in 36.
4. **The fixed-bar rule is calibrated at the nominal** for the rms (4.7 percent, [3.6, 6.2] contains 5). Its
   worst-galaxy bar is vacuous (the quantile of maxima over all 155 is the table's maximum), so a fixed outlier
   form would need a different statistic (a per-galaxy quantile, say); that is not proposed here.

## What this does and does not do to the kept verdicts

GRV-BLIND-1 (BLIND-AGREES, 0.1138) and GRV-BLIND-2 (BLIND-FAILS, 0.1656 against 0.1582) stand as rendered; nothing
here re-reads them. What the record adds: GRV-BLIND-2's draw put both PGC51017 and UGC04305 in its test set, the
configuration in which this rule fails 22 of 36 honest draws, and the fail was 4.7 percent over a bar that moved
down because they left the pool. Under the rule's measured false-fail rate the pair (one pass, one fail) is what two
draws of an unbiased prediction look like about a quarter of the time. The fixed rms bar on this table is 0.1720;
GRV-BLIND-2's 0.1656 lies under it and GRV-BLIND-1's 0.1138 well under it. That sentence is a reading of the
instrument, not a verdict: B-2 forbids re-barring a draw after its truth was read, the fixed bar was computed after
GRV-BLIND-2's rms was known, and its value clearing 0.1656 is the arithmetic of a rule named five days earlier, not a
choice. The rule's adoption, for future draws only, is the author's act.

## Named next (the author decides)

GRV-BLIND-3: a fresh beacon draw of GRV-030's prediction under the fixed-bar rule (rms bar 0.1720 from all 155, locked
before the draw), the outlier form dropped or re-specified, exposure of this study disclosed in the charter. That is
a new question with a calibrated instrument, not a rescue: the prediction, the data and the draw are the same kind
as before; only the bar's construction changes, to one whose false-fail rate is now measured.
