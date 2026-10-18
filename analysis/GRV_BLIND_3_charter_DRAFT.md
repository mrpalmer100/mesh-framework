# COMMISSION GRV-BLIND-3 -- GRV-030's ZERO-PARAMETER PREDICTION ON A BEACON DRAW UNDER THE CALIBRATED FIXED BAR
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; nothing has run; the draw does not exist)

## 1. The question, and the North Star line

Question key: grv030-sparc-holdout-fixed-bar.

Q1. Does the registered zero-parameter prediction g_obs = g_bar nu(g_bar / g_dagger), g_dagger = c H0 / 2 pi = 1.083e-10
m/s^2 (GRV-030; H0 = 70 km/s/Mpc, a declared measured input), frozen before the observed velocities are read, agree
with 30 SPARC galaxies drawn from a public randomness beacon under a bar FIXED in this charter, whose false-fail rate
on this table is measured (GRV-130: 4.7 percent, [3.6, 6.2])?
Q2. Was the draw external by the mechanical rule of B-6 (a beacon round committed to the record before it existed)?

Why a third draw is a new question and not a rescue. GRV-BLIND-1 passed and GRV-BLIND-2 failed under rule B-1, whose
bar is recomputed from each draw's training complement. GRV-130 (analysis/GRV_BARS_OC_exploratory_results.md) measured
that rule on 1000 uninspected splits: it fails 11.8 percent of honest draws against its nominal 5, the excess being
the rule's construction (a quantile over the pool the held-out galaxies have just left), carried by two galaxies; the
rule applied once to all 155 galaxies and held fixed fails 4.7 percent. Both kept verdicts stand; neither is
re-read here. This commission asks the same physical question of a fresh draw with an instrument whose operating
characteristic is on the record, which GRV-BLIND-1 and GRV-BLIND-2 did not have. The prediction, the data, the draw
tool and the predictor are unchanged; only the bar's construction changes, to the one GRV-130 found calibrated, and
the bar's number is written here before the draw exists.

North Star line (section 5, rule (c)): a discriminator confronted, the programme's one D1 observable (gravity row,
docs/NORTH_STAR.md section 2). Section 2b: a BLIND-AGREES with DRAW-EXTERNAL is offered to the author as a blind pass
of a D1 observable under a calibrated bar; whether a beacon draw counts toward "externally adjudicated predictions"
(1 to 2) is the author's decision at promotion, as GRV-BLIND-2's charter already stated (a beacon is not a human
adjudication). A BLIND-FAILS is kept at full weight and is not re-chartered; the row would then read two fails in
three draws, one under a calibrated bar, and GRV-030's whole-table statement would stand as a whole-table statement.

What this commission does NOT do: it moves no target from blocked to derived, retires no input (H0 stays an input),
touches neither GRV-031 nor XSEC-001, changes GRV-030's status in neither direction, re-bars no past draw, and
renders no outlier form (the worst-galaxy statistic is recorded, not formed: GRV-130 found no calibrated fixed
version of it).

## 2. The parts list (every input cited; nothing is chosen in this commission)

| part | what | source |
|---|---|---|
| prediction | g_dagger = c H0 / 2 pi, H0 = 70; g_obs = g_bar nu(g_bar / g_dagger), nu(y) = 1/(1 - exp(-sqrt y)); M/L gas, 0.5 disc, 0.7 bulge | GRV-030; benchmarks/gravity/grv_blind_1.py (unchanged) |
| the table and eligibility | data/sparc_rotmod, 175 files; 155 eligible (three or more points with errV/Vobs < 0.1, r > 0, Vobs > 0) | tools/holdout_galaxies.py (unchanged) |
| the draw | 30 of 155 by tools/holdout_galaxies.py draw, seed from the beacon (section 3) | the lab's beacon (lab/beacon.py); GRV-BLIND-2 section 11 for the precedent |
| THE BAR (fixed here) | rms of log10(g_obs) - log10(g_pred) over all kept held-out points <= 0.171955 dex | GRV-130: B-1's rule (0.95 quantile over 20,000 random 30-galaxy subsets, at the predicted g_dagger) applied once to all 155 eligible galaxies, random stream seed 0 of the vectorised draw in benchmarks/gravity/grv_bars_oc_exploratory.py (analysis/GRV_BARS_OC_exploratory.json, fixed_bars.bar_rms) |
| the bar's operating characteristic | false-fail rate 4.7 percent, Wilson [3.6, 6.2], on 1000 uninspected splits of this table | GRV-130 |
| the floors | F-1 and F-2 as GRV-BLIND-2 locked them (section 5) | analysis/GRV-BLIND-2_charter_LOCKED.md section 5 |
| the excluded seeds | 777 (smoke), 52525254 (GRV-BLIND-1), 1083026663 (GRV-BLIND-2) | the kept records |

Exposure, stated: the whole table was in GRV-030's run; GRV-130 saw 1000 splits' statistics; the author knows which
two galaxies carry B-1's miscalibration. None of that can touch this draw: the held-out set is chosen by a beacon
round that does not yet exist, and the bar is one number written here. The fixed bar's value clears GRV-BLIND-2's
rms (0.1656); that is the arithmetic of a rule named in STRATEGIC_TARGETS section AL on 2026-10-13, before GRV-130
ran and before this charter, applied to the whole table; it was not chosen, and it does not apply to GRV-BLIND-2
(B-2: no re-barring of a read draw).

## 3. The draw (the lab's beacon; a precondition of the seal, not of the lock)

The seed is the lab's public-beacon rule exactly as lab/beacon.py fixes it and as GRV-BLIND-2's record disclosed it:
the lab commits a future drand round to the lab branch; when the round is published, seed = int(first 8 hex digits
of its randomness, base 16) AND 0x7fffffff, a 31-bit integer; drawn_by = "drand beacon round <round> (chain <hash>)".
The charter states the executed rule itself so the wording cannot differ from the code (the GRV-BLIND-2 lesson).

    python tools/holdout_galaxies.py draw --name GRV_BLIND_3 --seed {seed} --n 30 --drawn-by "{drawn_by}"

Overlap with GRV-BLIND-1's and GRV-BLIND-2's held-out sets is allowed, recorded and not removed (about 5.8 of 30 each
at random). The driver's units before the draw (calib) read no GRV_BLIND_3 file; the units after it refuse to run
until analysis/holdout/GRV_BLIND_3/MANIFEST.json exists (exit 3, the runner's waiting code, not a failure).

## 4. Steps and the calibration leg (pass bars locked here; every one must pass before the seal)

U1 calib (reads no GRV_BLIND_3 file):
- C-1 the fixed bar reproduces: the rule of section 2 recomputed on all 155 galaxies equals 0.171955 within 1e-6.
- C-2 the predictor reproduces analysis/GRV_BLIND_1_pred.txt on GRV_BLIND_1's inputs (same keys, relative 1e-5).
- C-3 the draw tool reproduces GRV-BLIND-1's and GRV-BLIND-2's held-out sets from their recorded seeds, 155 eligible.
- C-4 the verdict arithmetic reproduces GRV-BLIND-2's recorded rms 0.1656 from analysis/holdout/GRV_BLIND_2/VERDICT.json's
  rows to 5e-5 dex (a kept past verdict, read as a number only).
U2 manifest: C-5 the beacon draw reproduces from the seed the manifest records (the same 30, 155 eligible, train.txt's
sha256 equal to the manifest's); drawn_by carries the committed round; the seed is not in the excluded list.
U3 predict: the unchanged predictor at every radius of every held-out inputs file, to analysis/GRV_BLIND_3_pred.txt;
the floors F-1 and F-2 of section 5 from training data and inputs only.
U4 seal: GATED on C-1 to C-5 and F-1, F-2 passing; tools/holdout_galaxies.py seal, once (C-6: sealed on the file the
driver wrote).
U5 truth: GATED the same way; the ONE read, through the unchanged tool's verdict with --bar-rms 0.171955 and --bar-gal
1e9 (the tool's galaxy bar made vacuous, since no outlier form is rendered; disclosed), or ingestion of the
VERDICT.json it wrote; verdict.py reads only the checkpoint, recomputes every held-out statistic from the kept rows
and cross-checks the tool to 1e-9 dex.

## 5. The floor test (before the truth; training data and inputs only; thresholds inherited, not chosen here)

F-1 the Newtonian null (g_pred = g_bar) on the training galaxies has rms >= 2.0 x 0.171955 = 0.3439 dex.
F-2 over all held-out input radii with g_bar > 0: rms of log10(g_pred / g_bar) >= 0.30 dex; fraction with
g_bar < g_dagger >= 0.40; zero radii with g_bar <= 0 or unpredicted.
Both thresholds are GRV-BLIND-2's, set there after a whole-table exploration (disclosed in that charter, section 5)
and locked before its draw; they are inherited unchanged. A floor failure renders BLIND-OPEN-FLOOR without a truth
step. The floors cannot change an outcome in favour of the prediction except by passing a non-degenerate draw.

## 6. The bars (the number locked here)

B-1 rms of log10(g_obs) - log10(g_pred) over all kept held-out points <= 0.171955 dex. One number, written before the
draw, from a rule named before the study that measured it.
B-2 one prediction, no re-fit, no exclusion after the truth; a galaxy that misses is a miss; H0 = 70 fixed.
B-3 the sub-readings of section 8 change nothing.
B-4 the prior, stated and not leaned on: BLIND-AGREES (the whole-table rms is 0.1423; the bar's measured false-fail
rate is 4.7 percent). A prior that is right is not a result; the draw is.
B-5 the draw is the beacon's; one draw; no redraw.
B-6 what counts: DRAW-EXTERNAL means drawn_by (case-insensitive) is not in {'', palmer, mark, mark palmer, mrpalmer100,
author, the author, lab, mesh lab, sandbox, commission, the commission, agent, worker, claude}, the seed is not in
{777, 52525254, 1083026663}, and the 30 galaxies are neither GRV-BLIND-1's nor GRV-BLIND-2's set. The form records
the mechanical fact; the beacon file's commit before the round is the evidence of advance commitment, and the
write-up cites that file and its commit rather than asserting independence in its own voice.

## 7. Verdict forms (exhaustive; reached in this order)

FORM (Q1): BLIND-CALIB-FAIL (any of C-1 to C-6) / BLIND-OPEN-FLOOR (F-1 or F-2) / BLIND-INCOMPLETE (a held-out kept
point without a prediction, or no truth step) / BLIND-AGREES (rms <= 0.171955) / BLIND-FAILS (rms > 0.171955).
FORM (Q2): DRAW-EXTERNAL / DRAW-NOT-EXTERNAL, by B-6.
Recorded, not formed: the worst per-galaxy rms, the mean residual, the overlap counts with the two earlier draws,
whether PGC51017 or UGC04305 is in the held-out set (a fact of the draw, recorded because GRV-130 named them; it
changes no form and no bar).

## 8. Sub-readings (recorded, not read; locked here; they change no form)

- The rms at the data-fitted g_dagger (1.134e-10), as GRV-BLIND-2 recorded it.
- The rms excluding the galaxies shared with GRV-BLIND-1 and with GRV-BLIND-2 (two numbers; the full-set rms decides).
- The held-out rms under the old rule B-1 computed from this draw's training complement, printed beside the fixed bar
  so the two rules' readings of the same draw are on one line. The old rule renders nothing here.

## 8a. Development and smoke discipline (binding on the worker; a lock-review item)

Before the lock nothing runs on any GRV_BLIND_3 file (none exists). LAB_SMOKE=1 runs the pipeline on a synthetic
fixture the driver generates (30 synthetic galaxies with the inputs' shape and iid residuals, seeded 4242) under the
name GRV_BLIND_SMOKE in a scratch directory, never under analysis/holdout/; it writes analysis/grv_blind_3_smoke.pkl
and no evidence checkpoint; the smoke verdict prints "smoke: forms withheld" and no FORM token. The credentials
C-1 to C-4 read kept records only and may run before the lock; nothing else may.

## 9. The verdict script (benchmarks/lab/grv_blind_3/verdict.py; frozen at lock)

Reads the checkpoint only. Order fixed: validate in full (status, every unit, the manifest of file hashes equal to
the lock record, every numeric finite, the bar equal to 0.171955), then create analysis/GRV-BLIND-3_verdict.log with
O_EXCL, then the forms in section 7's order, returning at the first instrument form rendered.

## 10. Budgets and disclosures

Seconds of compute; cpu_hours 0.1; mem_gb 1; usd 0. The exposure of section 2. The tool's galaxy bar is passed as
1e9 to make it inert; the tool otherwise unchanged. The GRV-BLIND-2 lesson on seed wording is answered by writing the
executed rule in section 3. The author wrote this charter without running anything against any GRV_BLIND_3 file;
the one new number in it, 0.171955, is read from GRV-130's record.

```lab
commission: GRV-BLIND-3
target: "Gravity row D1 (NORTH_STAR section 2): GRV-030's g_dagger = cH0/2pi confronted blind a third time, under a bar whose false-fail rate is measured (GRV-130); rule (c); a pass with a beacon draw offered to the author for section 2b"
driver: benchmarks/lab/grv_blind_3/driver.py
verdict_script: benchmarks/lab/grv_blind_3/verdict.py
instrument:
  - benchmarks/gravity/grv_blind_1.py
  - tools/holdout_galaxies.py
  - benchmarks/gravity/grv_bars_oc_exploratory.py
beacon_draw:
  command: python tools/holdout_galaxies.py draw --name GRV_BLIND_3 --seed {seed} --n 30 --drawn-by "{drawn_by}"
forms: [BLIND-CALIB-FAIL, BLIND-OPEN-FLOOR, BLIND-INCOMPLETE, BLIND-AGREES, BLIND-FAILS, DRAW-EXTERNAL, DRAW-NOT-EXTERNAL]
state: [analysis/grv_blind_3_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
