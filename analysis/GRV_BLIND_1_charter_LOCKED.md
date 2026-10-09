# COMMISSION GRV-BLIND-1 -- THE SPARC CONFRONTATION UNDER THE BLIND BAR
# (CHARTER, LOCKED 2026-10-09 by the author after his draw and before the seal)

North Star line (section 5): (c) a discriminator adjudicated, and the programme's best D1 content brought under its
own standing bar. GRV-030 (Modeled): g_dagger = c H0 / 2 pi = 1.083e-10 m/s^2 predicts the radial-acceleration
relation of 155 SPARC galaxies at zero free parameters (rms 0.1423 dex at the predicted value against 0.1421 at the
data-fitted value). It was run on the whole table. Bar W (STRATEGIC_TARGETS section W) says a confrontation on the
North Star page holds out a sealed test set drawn before the lock and freezes the prediction before the held-out
values are read. The prediction here has nothing to fit, so the hold-out costs nothing physically and buys the
procedure: the first blind confrontation of a D1 claim. If the draw is run by someone who is not the author, a pass
is the second externally adjudicated prediction (section 2b, 1 to 2), this time of a parameter-free observable.

## The prediction (fixed; GRV-030's, unchanged)
g_obs = g_bar nu(g_bar / g_dagger), nu(y) = 1 / (1 - exp(-sqrt y)) (the registered simple interpolation),
g_dagger = c H0 / 2 pi with H0 = 70 km/s/Mpc (a measured input, declared as GRV-030 declares it; on the input ledger),
g_bar from the registered mass-to-light convention (gas; 0.5 disk; 0.7 bulge), the registered quality cut
errV/Vobs < 0.1 at verdict time. No number is chosen in this commission.

## The draw (W1; the author's or an adjudicator's, not the sandbox's)
  python tools/holdout_galaxies.py draw --name GRV_BLIND_1 --seed <chosen> --n 30 --drawn-by "<who>"
Thirty of the eligible galaxies (those the registered confrontation keeps: at least three points passing the cut);
each held-out galaxy is SPLIT by the tool: its inputs (r, Vgas, Vdisk, Vbul) to analysis/holdout/GRV_BLIND_1/inputs/
and its observed velocities (r, Vobs, errV) to sealed/, read once by verdict. The commission reads train.txt, the
training galaxies' files whole, and the inputs of the held-out ones. The manifest records the seed, the drawer,
every file's sha256 and the hash of the concatenated sealed truth; the three lines go into this charter at lock.

## Steps
  G1  (sandbox) benchmarks/gravity/grv_blind_1.py GRV_BLIND_1: the prediction at every radius of every held-out
      galaxy's inputs file, to analysis/GRV_BLIND_1_pred.txt; in the same run, THE BARS by the rule below, from the
      training galaxies only, to analysis/GRV_BLIND_1_bars.json.
  G2  (sandbox) tools/holdout_galaxies.py seal.
  G3  nothing.
  G4  (the PC, or wherever the author runs it) tools/holdout_galaxies.py verdict with the bars from G1, once.
  G5  (sandbox) sub-reading on the kept residuals: the mean residual (a sign of a g_dagger offset) and the rms at
      the registered data-fitted g_dagger (1.134e-10) for comparison; recorded, changes nothing.

## Bars (to be LOCKED as a RULE; the numbers come from the training set after the draw and before the seal)
B-1  rms of log10(g_obs) - log10(g_pred) over all kept held-out points <= the 95th percentile of the same rms over
     20,000 random 30-galaxy subsets of the TRAINING galaxies at the predicted g_dagger (the sampling distribution
     the held-out set is one draw from; a 30-galaxy rms varies by tens of percent, as a five-galaxy instrument
     check showed, so a fixed number would test the draw, not the prediction). Likewise the worst per-galaxy rms
     <= its 95th percentile. The quantile, the subset count and the seed of the bootstrap (the draw's seed) are
     fixed here. BLIND-AGREES if both hold; BLIND-FAILS otherwise; BLIND-INCOMPLETE if any kept point is unpredicted.
B-2  One prediction, no re-fit, no exclusion after the truth is read (a galaxy that misses is a miss).
B-3  The sub-reading changes nothing.
B-4  The prior, stated and not leaned on: BLIND-AGREES (the prediction has already been seen to hold on the whole
     table; the bar is set at the 95th percentile of its own sampling distribution, so a fair draw fails one time
     in twenty by chance, and that is the price of a bar that can fail at all).
B-5  The draw is the drawer's; the seed recorded; no redraw.
B-6  What counts: a pass with the author's draw is an out-of-sample confrontation of a D1 claim (the row's grade
     column gains "blind-scored"); a pass with an adjudicator's draw moves section 2b from 1 to 2.

## Verdict forms (to be LOCKED)
BLIND-AGREES    rider on GRV-030 with the held-out rms and the drawer; the row's grade column; 2b per B-6.
BLIND-FAILS     kept; rider; the row says "fails blind at <rms>"; GRV-030's whole-table statement stands as what it
                is (whole-table), and the discrepancy between whole-table and held-out is the finding.
BLIND-INCOMPLETE instrument fault, recorded.

## Rules
No rescue; the truth read once after the seal; the sandbox never reads sealed/; riders the author's.

## Instrument notes before the draw (sandbox, 2026-10-09; recorded at lock)
tools/holdout_galaxies.py is new (the AME tools hold out rows of one file; a galaxy table is one file per galaxy
with the truth beside the inputs, so the tool splits each held-out file). Self-tested on a throwaway five-galaxy
draw (seed 1: DDO168, NGC5005, NGC5985, UGC05986, UGC11455): draw, predict, seal, verdict once, refused twice; the
throwaway was deleted. That check read five galaxies' truth, all of which GRV-030 had already confronted on the
whole table; they are not excluded from the draw (the draw is seeded and had not happened), and the fact is
disclosed here. The five-galaxy rms was 0.177 dex against the whole-set 0.142, which is why B-1 is a rule and
not a number.

## Instrument note at lock
The draw was made on the PC; its files carry Windows line endings, so their sha256 differ from the same content
written here (the sandbox reproduced the draw from the seed: the same thirty galaxies, the same inputs, byte-different
files). The PC's manifest is the record; the seal and the verdict run on the PC. tools/holdout_galaxies.py now writes
LF on every platform for future draws (declared; this draw stands as made). The sandbox deleted its regenerated
sealed/ copies before the predictor ran and read only inputs/ and the training galaxies' files.
The bars by B-1's rule, from the 125 training galaxies at the predicted g_dagger (analysis/GRV_BLIND_1_bars.json):
  training rms 0.1496 dex; bar_rms = 0.1800 dex; bar_gal = 0.6321 dex (95th percentiles over 20,000 30-galaxy subsets).
The prediction file analysis/GRV_BLIND_1_pred.txt (734 points in 30 galaxies) sha256
f15f0e37883c185e55c560f6424d02878a3dee2d310a62dd344ce2c6515a74b5, written before the seal.

## Author's lock
LOCKED 2026-10-09 ("lock grv-blind"), after the author's draw and before the seal. The draw (the PC's manifest):
  seed 52525254; drawn by palmer; 30 of 155 eligible galaxies (175 files)
  train   sha256 8801ef86918ae20ce01c406563ae7c762dd38f288db00945b03540f0c53bd1a1  (analysis/holdout/GRV_BLIND_1/train.txt)
  test    sha256 b7e25cfd67f4e5c6509ce9525ee89dae0945ce874e186b1c6e34537252767f23  (the concatenated sealed truth; NOT to be read)
  held out: ESO079-G014, F568-V1, F571-8, F579-V1, NGC0247, NGC0891, NGC1003, NGC2903, NGC2955, NGC3769, NGC3877,
  NGC3917, NGC4013, NGC5585, NGC6674, NGC7793, UGC01281, UGC02487, UGC02885, UGC02953, UGC04483, UGC05716, UGC05721,
  UGC05999, UGC06446, UGC06787, UGC06923, UGC07524, UGC08286, UGC11820
The prediction, the bar rule and its numbers above, the forms and B-6 are fixed from this line. The author's draw:
a pass is an out-of-sample confrontation of a D1 claim, not external adjudication (2b unchanged).
