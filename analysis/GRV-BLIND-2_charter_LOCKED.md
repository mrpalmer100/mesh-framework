# COMMISSION GRV-BLIND-2 -- GRV-030's ZERO-PARAMETER PREDICTION ON A SEED HELD BY SOMEONE OTHER THAN THE AUTHOR
# (CHARTER, DRAFT for the author's lock; no BLIND-2 step has run; the draw is the adjudicator's and does not yet exist)

## 1. The question, and the North Star line

Question key: grv030-sparc-holdout-adjudicated.

Q1. Does the registered zero-parameter prediction g_obs = g_bar nu(g_bar / g_dagger), g_dagger = c H0 / 2 pi = 1.083e-10 m/s^2
(GRV-030; H0 = 70 km/s/Mpc, a declared measured input), frozen before the observed velocities are read, agree with 30 SPARC
galaxies drawn with a seed chosen and run by an adjudicator who is neither the author nor the commission, under the bars rule
of GRV-BLIND-1 (analysis/GRV_BLIND_1_charter_LOCKED.md, B-1)?

Q2. Was the draw external (so that a pass counts toward NORTH_STAR section 2b)?

North Star line (section 5, rule (c)): a discriminator adjudicated. Number moved (section 2b): "externally adjudicated
predictions", 1 to 2, only on a BLIND-AGREES with a DRAW-EXTERNAL, and only when the author ratifies the count. This is the
first external adjudication of a D1 observable (GRV-030; GRV-BLIND-1 was the author's draw and is recorded as a rider only).

What this commission does NOT do, stated first: it moves no target from blocked to derived, retires no input (H0 stays an
input on the ledger), does not touch the retired shape claim (GRV-031) or the XSEC-001 no-evolution prediction, and changes
GRV-030's status (Modeled) in neither direction; the confrontation line is what moves. A failure is kept as Failed on
GRV-030's blind row and is not re-chartered (a follow-up would ask a different question and say so).

## 2. The parts list (every input cited; nothing is chosen in this commission)

| part | what | source |
|---|---|---|
| prediction | g_dagger = c H0 / 2 pi, H0 = 70 km/s/Mpc; g_obs = g_bar nu(g_bar/g_dagger), nu(y) = 1/(1 - exp(-sqrt y)) | GRV-030 (Modeled); H0 an input (docs/NORTH_STAR.md section 3 ledger) |
| the interpolation nu | the simple function; EMPIRICAL, selected on the whole table (GRV-030 R2); the tanh family wounded (GRV-030) and the Langevin candidate retired (GRV-031) | GRV-030, GRV-031 |
| structural reason g_dagger is the whole registered MOND content | no galaxy-scale scalar; the horizon channel alone | GRV-028/029 (via GRV-030) |
| baryonic model | gas; M/L 0.5 disc, 0.7 bulge; quality cut errV/Vobs < 0.1; at least three kept points per eligible galaxy | benchmarks/gravity/sparc_rar_confrontation.py (GRV-030) |
| predictor and bars rule | benchmarks/gravity/grv_blind_1.py, CALLED UNCHANGED (sha256 4c407e9e732c431909b3bf8bc0e6abcf214083f8fe2c480c526ae921503aa634 at drafting) | GRV-BLIND-1 |
| draw / seal / verdict instrument | tools/holdout_galaxies.py, CALLED UNCHANGED (sha256 87fa200c1145f9d8b87922f272544b6c18a09bab1cd657ff59f99e3f87e25d7a at drafting) | GRV-BLIND-1; STRATEGIC_TARGETS section W |
| data | data/sparc_rotmod, 175 files, concatenated sorted sha256 469f4f556dc813b2343187f525c120b66f36c696ac814a0426e12ce4c83aae3d at drafting; 155 eligible | GRV-030 |
| precedent for the process | NUC-BLIND-1 to NUC-BLIND-2 (analysis/NUC_BLIND_2_charter_LOCKED.md) | NORTH_STAR section 2b |

The hashes are checked at lock. If any instrument file differs at lock, the diff goes in this charter and C-1 to C-4 below
adjudicate whether it matters.

## 3. The draw (a precondition of the lock; W1)

The adjudicator (a person who is not the author and not the commission; named at lock) chooses the seed without telling the
author in advance and runs, on the author's PC or any machine with the repo:

    python tools/holdout_galaxies.py draw --name GRV_BLIND_2 --seed <adjudicator's seed> --n 30 --drawn-by "<adjudicator>"

The seed must differ from 52525254 (GRV-BLIND-1's) and from 777 (the smoke's throwaway draw, disclosed in section 10). The
three lines (train sha256, test sha256, held-out list), the seed, the drawer's name and the time go into this charter at lock.
The overlap with GRV-BLIND-1's 30 galaxies is allowed and expected (about 5.8 of 30 at random: 30 x 30 / 155) and is
recorded, not removed: removing galaxies after a draw is a leak. The overlap galaxies' observed velocities are in the shipped
SPARC table and were confronted in GRV-030's whole-table run; see section 7. The author does not see the seed before the draw.
The driver refuses to start the BLIND-2 units (exit 2, no terminal line) while analysis/holdout/GRV_BLIND_2/MANIFEST.json is absent.

## 4. Steps and the calibration leg (pass bars locked here, before any computation; every one must pass)

The driver does one unit per invocation (state analysis/grv_blind_2_ckpt.pkl, atomic, resumable):

U1 calib. Reads no BLIND-2 file. Credentials the instruments against GRV-BLIND-1's recorded answers:
- C-1 bars rule: run the unchanged grv_blind_1.py on GRV_BLIND_1's own train.txt and seed in a scratch copy; the 0.95-quantile
  bars must equal analysis/GRV_BLIND_1_bars.json (0.180043771626121 dex rms, 0.6320993156052539 dex worst galaxy) to within 1e-6 dex.
- C-2 predictor: its 734 predictions on GRV_BLIND_1's inputs must have the same (galaxy, radius) keys as
  analysis/GRV_BLIND_1_pred.txt and agree to within a relative 1e-5 (the file's sha256 f15f0e37... equality is informational).
- C-3 draw tool: re-drawing seed 52525254 must return GRV-BLIND-1's 30 galaxies exactly and 155 eligible.
- C-4 verdict arithmetic: the rms, worst-galaxy rms, point count and form recomputed from the recorded rows of
  analysis/holdout/GRV_BLIND_1/VERDICT.json must match the tool's recorded numbers (0.1138 and 0.3803 dex, 634 points,
  BLIND-AGREES under the BLIND-1 bars) to within 5e-5 dex.
U2 manifest. Reads the adjudicator's MANIFEST.json (never sealed/). C-5: the draw reproduces from its recorded seed (the same
  30 galaxies, the same eligible count, the same training list), every held-out inputs file exists, n_test = 30, and train.txt's
  sha256 equals the manifest's.
U3 predict. The unchanged predictor at every radius of every held-out inputs file to analysis/GRV_BLIND_2_pred.txt; the bars by
  the BLIND-1 rule from the training galaxies only (0.95 quantile over 20,000 random 30-galaxy subsets of the training galaxies, at
  the predicted g_dagger, the bootstrap seed the draw's seed) to analysis/GRV_BLIND_2_bars.json; the floor tests of section 5;
  the descriptive training pass window of section 8.
U4 seal. GATED. tools/holdout_galaxies.py seal, once. C-6: sealed on the file the driver wrote. The driver refuses to seal unless
  the checkpoint shows that C-1 to C-5 PASS and F-1 and F-2 PASS with the locked tolerances.
U5 truth. GATED. The ONE read of the sealed truth, through the unchanged tool's verdict with the bars from U3, or ingestion of the
  VERDICT.json that tool wrote (the NUC-BLIND-2 pattern: the tool refuses a second read). If sealed/ is not on the machine and no
  VERDICT.json exists the driver prints BLOCKED (exit 2, not COMPLETE) with the exact command for the machine that holds sealed/.
  The driver refuses to take the truth unless the checkpoint shows that C-1 to C-5 PASS and F-1 and F-2 PASS. verdict.py reads only
  the checkpoint, recomputes every held-out statistic from the kept rows, and cross-checks the tool's numbers to 1e-9 dex.

Gate shape and exposures: C-1..C-4 use only GRV-BLIND-1's recorded files (a kept past verdict); C-5 uses only the adjudicator's
MANIFEST.json and the shipped table; F-1 and F-2 use only training data and held-out inputs. No sealed file is ever opened before
the gate passes. The gate does not weaken a verdict and cannot change an outcome in favour of the prediction except by passing a
non-degenerate draw. The worst-galaxy bar carries no evidential weight (section 7).

## 5. The floor test (computed before the truth is read, from training data and inputs only)

The BLIND-1 lesson (a five-galaxy rms of 0.177 against a whole-table 0.142) is why the rms bar is a sampling-distribution
quantile and not a number. The floor tests ask whether the verdict can discriminate at all:
- F-1 (power against the null). The Newtonian null (g_pred = g_bar, no g_dagger) on the training galaxies must have rms
  >= 2.0 x bar_rms. (Whole-table figures from the drafting exploration, analysis/lab/drafts/GRV-BLIND-2/scratch_explore.py:
  Newtonian 0.517 dex against 0.142 for the prediction, a ratio near 2.9 against the bar near 0.18.)
- F-2 (the draw sits where the prediction differs from the null; inputs only, no truth). Over all held-out input radii with
  g_bar > 0: the rms of log10(g_pred / g_bar) >= 0.30 dex, the fraction with g_bar < g_dagger >= 0.40, and zero radii with
  g_bar <= 0 or an unpredicted value. (Drafting exploration, 5000 random 30-galaxy subsets of the whole table: the 1st
  percentile of the separation is 0.407 dex and of the fraction 0.597, so 0.30 and 0.40 are set well below the chance range; a
  failure means a degenerate draw, not a hard one.) These two thresholds were set after that whole-table exploration, which
  is not the adjudicated cell (the draw did not exist); the exploration is disclosed and the file kept. They are floors for
  discrimination and cannot change an outcome in favour of the prediction except by passing the draw as non-degenerate.
If F-1 or F-2 fails the driver refuses to seal or to read the truth (exit 2, no COMPLETE line); the verdict, reading only the
checkpoint, renders BLIND-OPEN-FLOOR without any truth step.

## 6. The bars (rule locked here; numbers come from the training galaxies after the draw and before the seal)

B-1 rms of log10(g_obs) - log10(g_pred) over all kept held-out points <= the 0.95 quantile of the same rms over 20,000 random
    30-galaxy subsets of the TRAINING galaxies at the predicted g_dagger; and the worst per-galaxy rms <= its 0.95 quantile. The
    same rule, code and seed convention as GRV-BLIND-1 (bars 0.1800 and 0.6321 dex there; the BLIND-2 numbers will differ
    because the training list differs).
B-2 one prediction, no re-fit, no exclusion after the truth is read; a galaxy that misses is a miss. H0 = 70 is fixed (a different
    H0 would be chosen after seeing data).
B-3 the sub-readings of section 8 change nothing.
B-4 the prior, stated and not leaned on: BLIND-AGREES. GRV-BLIND-1 passed (0.1138 dex, bar 0.1800) and the whole-table rms is
    0.1423. By construction a fair draw exceeds the 0.95-quantile rms bar about one time in twenty, so the chance failure rate of
    the rms bar is about 5 percent; the worst-galaxy bar adds at most another 5 percent (the union is at most about 10 percent).
    A prior that is right is not a result; the draw is.
B-5 the draw is the adjudicator's; seed recorded; no redraw.
B-6 what counts: BLIND-AGREES with DRAW-EXTERNAL is offered to the author for NORTH_STAR section 2b, 1 to 2, with the adjudicator
    named; the author decides whether it counts (the count definition is his). DRAW-EXTERNAL means: drawn-by (case-insensitive)
    is not in {'', palmer, mark, mark palmer, mrpalmer100, author, the author, lab, mesh lab, sandbox, commission, the commission,
    agent, worker, claude}, the seed is not one of {52525254, 777}, and the 30 galaxies are not GRV-BLIND-1's set. The adjudicator's
    identity beyond that string is the author's attestation at lock; nothing in the machinery verifies it. Seed 777 is excluded
    by the locked list; it is requested only for the smoke.

## 7. Verdict forms (exhaustive; each reached by the rule below, in this order)

Q1:
- BLIND-CALIB-FAIL: any of C-1 to C-6 fails, or the script and the tool disagree on the held-out statistics. Instrument fault,
  recorded; no verdict on the prediction. If a calibration pass bar fails, the driver never seals or reads the truth.
- BLIND-OPEN-FLOOR: calibration passes, F-1 or F-2 fails. The draw or the instrument cannot discriminate; open, no verdict on
  the prediction; not a pass and not a fail. The driver never seals or reads the truth on a failed floor.
- BLIND-INCOMPLETE: calibration and floor pass but any kept held-out point is unpredicted, or the checkpoint has no truth step.
- BLIND-AGREES: calibration and floor pass, nothing missing, rms <= bar_rms. The worst-galaxy bar is recorded as Q3 only and
  carries no evidential weight in Q1 (its 0.95-quantile is almost always the worst training galaxy's rms under this rule).
- BLIND-FAILS: as above, with rms > bar_rms. Kept as Failed; the row would read "fails blind at <rms> under an external draw";
  GRV-030's whole-table statement stands as what it is, and the discrepancy between whole-table and held-out is the finding.
  No rescue, no re-chartering.
Q2: DRAW-EXTERNAL or DRAW-NOT-EXTERNAL by B-6.
Q3: OUTLIER-WITHIN-BAR | OUTLIER-EXCEEDS-BAR | OUTLIER-OPEN records the worst-galaxy bar relative to the held-out worst; Q3 never
    changes Q1 or Q2 and carries no evidential weight.

What each form would establish and not:
- BLIND-AGREES + DRAW-EXTERNAL establishes: with the interpolation function fixed, H0 = 70 and the registered M/L convention,
  the parameter-free RAR prediction, frozen before the values were read, has held-out rms inside its own 95th-percentile
  sampling bar on 30 galaxies chosen by someone else. It does NOT establish: the coefficient 1/2 pi (see section 8: the window
  of g_dagger values the bar accepts is wide); that cH0/2pi is derived rather than a numerical coincidence of the right order
  (GRV-030 itself carries the 2 pi versus 6 caveat); independence of the data (every SPARC galaxy was in GRV-030's whole-table
  run, the interpolation function was selected on the whole table, GRV-030 R2, and about 6 galaxies were also in GRV-BLIND-1's
  hold-out); the nu shape (empirical, GRV-031); that H0 is derived (it is an input); no-evolution at high redshift (XSEC-001);
  any other gravity target. What is blind is the procedure (prediction frozen before the held-out values were read, draw by
  another person), not the data's novelty.
- BLIND-AGREES + DRAW-NOT-EXTERNAL: a second out-of-sample confrontation; section 2b unchanged.
- BLIND-FAILS: the zero-parameter statement does not survive a fresh draw at the pre-set bar; GRV-030's whole-table result is
  a whole-table result only. It would not by itself falsify cH0/2pi against a nearby coefficient (a 30-galaxy draw is one draw;
  the failure rate by chance is about 5 to 10 percent), and the charter does not read it as more than the locked bar says.
- BLIND-OPEN-FLOOR / BLIND-INCOMPLETE / BLIND-CALIB-FAIL: no physics established either way.

## 8. Sub-readings (recorded, not read; locked here; they change no form)

- the held-out rms at the registered data-fitted g_dagger (1.134e-10) and the mean residual;
- the best factor on the grid g_dagger x 2^(k/4), k = -8..8, and the factors whose held-out rms is within the bar;
- the TRAINING pass window, set before the truth: the contiguous range of factors around 1 (grid 2^(k/4), k = -16..16) at which
  the training rms stays <= bar_rms. At drafting, on the whole table, the rms is 0.1814 at x0.5, 0.1554 at x0.7, 0.1498 at x1.4 and
  0.1783 at x2 (whole-table rms 0.1423 at x1), so the window is roughly x0.5 to x2 and a pass cannot distinguish cH0/2pi from
  cH0/6 (a factor 1.047 away) or from the fitted 1.134e-10 (1.047 away). The F-1 floor tests power against NO modification;
  this window states the limit of the discrimination against nearby scales. The verdict prints it with every pass;
- the rms excluding the galaxies shared with GRV-BLIND-1.

## 9. Budgets

CPU: well under 0.1 hour (the 20,000-subset bootstrap and the credential legs ran in about one second each in the smoke); memory
under 1 GB; no GPU; usd 0. The only real cost is the adjudicator's five minutes and the author's discipline about the seed.

## 10. Disclosures (instrument and process)

- Smoke (LAB_SMOKE=1) runs every unit once against a throwaway draw (seed 777, drawn by "smoke-adjudicator") in a temporary
  directory, reads that throwaway draw's truth (30 galaxies, all already in the whole-table GRV-030 run), writes
  analysis/grv_blind_2_smoke.pkl and analysis/GRV-BLIND-2_smoke_verdict.log, and never the evidence checkpoint or log. It is not
  evidence. Its output is in the drafting record only; the adjudicator is asked not to use seed 777.
- C-4 reads GRV-BLIND-1's recorded VERDICT.json (a kept past verdict). That file holds the truths of GRV-BLIND-1's 30 galaxies, so
  it contains the observed velocities of about 6 galaxies that may recur in BLIND-2's held-out set. The predictor never reads
  them (it reads inputs/ only), and nothing is fitted, so no number can be tuned from them; it is disclosed because the
  hold-out discipline of section W is about what the prediction can see.
- analysis/lab/drafts/GRV-BLIND-2/scratch_explore.py, scratch_floor.py and scratch_hashes.py are drafting scratch; they read the
  whole shipped table (nothing sealed) to pick the floor thresholds and to record hashes. F-1 (x2.0) and F-2 (0.30 dex, 0.40)
  were set after inspecting that table. This is a rule-4 exposure and is stated in the lock text. The thresholds are floors for
  discrimination and cannot change an outcome in favour of the prediction except by passing the draw as non-degenerate.
- The worst-galaxy bar, by the BLIND-1 rule, was 0.6321 in GRV-BLIND-1 and again 0.6321 in the smoke's different training set:
  when a single very discrepant galaxy sits in the training list, the 0.95 quantile of the subset maximum is that galaxy's rms.
  So the worst-galaxy bar is nearly vacuous in practice and the rms bar does the discriminating. The rule is reused unchanged
  by design (B-1), and this is stated rather than repaired. Verdict.py records the worst-galaxy check as Q3 and it carries no
  evidential weight in Q1.
- The lab's driver is the reader of the truth in the evidence run (through the unchanged tool, once, after the seal, with the
  bars from the checkpoint), unless the tool was already run on the machine that holds sealed/.

```lab
commission: GRV-BLIND-2
target: "NORTH_STAR section 2b, externally adjudicated predictions 1 to 2, by adjudicating GRV-030's parameter-free g_dagger = cH0/2pi (the Gravitational force row's D1 content) on an adjudicator's draw; no target moved to derived, no input retired"
driver: benchmarks/lab/grv_blind_2/driver.py
verdict_script: benchmarks/lab/grv_blind_2/verdict.py
instrument: [benchmarks/gravity/grv_blind_1.py, tools/holdout_galaxies.py]
forms: [BLIND-AGREES, BLIND-FAILS, BLIND-INCOMPLETE, BLIND-OPEN-FLOOR, BLIND-CALIB-FAIL, DRAW-EXTERNAL, DRAW-NOT-EXTERNAL, OUTLIER-WITHIN-BAR, OUTLIER-EXCEEDS-BAR, OUTLIER-OPEN]
state: [analysis/grv_blind_2_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```

## LAB AMENDMENT (2026-10-11 11:41 EDT; decided by the lab without the author, reviewed by both reviewers; record under analysis/lab/decisions/)

## 11. Amendment (lab decision, appended after the lock; the draw replaced by the lab's public randomness beacon)

What changed. Section 3 required a person who is neither the author nor the commission to choose the seed and run the draw. No such person is available to the lab, and the autonomy rule (no step waits on a person) applies. The seed is instead supplied by the lab's public randomness beacon: drand round 6543429 was committed to the lab branch before that round existed, and its published randomness is the seed. The draw is run exactly as section 3 prescribes, with the unchanged tool:

    python tools/holdout_galaxies.py draw --name GRV_BLIND_2 --seed {seed} --n 30 --drawn-by "{drawn_by}"

where {seed} is the 32-byte randomness of drand round 6543429 read as a non-negative base-16 integer (the tool and the bars bootstrap seed numpy's default_rng, which accepts an integer of that size; the manifest records it verbatim, so C-5 reproduces the draw from it) and {drawn_by} is the string "drand beacon round 6543429". The round number, the published randomness, the seed as recorded, the drawn_at_utc time, the train sha256, the test sha256 and the held-out list are appended below this amendment when the draw is in the repo. No redraw (B-5 unchanged): if the beacon seed were by chance 52525254 or 777, or the draw reproduced GRV-BLIND-1's 30 galaxies, the frozen verdict renders DRAW-NOT-EXTERNAL and the commission proceeds on that draw; nothing is redrawn.

Why. Every other part of this charter is already fixed and credentialed (unit calib passed C-1 to C-4 before this amendment and read no BLIND-2 file). The seed is the only thing the absent person was to supply, and the beacon supplies it with the property the charter protects: the author and the lab cannot know it before the draw, and anyone can verify it afterwards.

What is NOT changed. The verdict script (benchmarks/lab/grv_blind_2/verdict.py), its forms, the bars rule B-1, the floors F-1 and F-2, the gate, the predictor, the data and the one-read truth discipline are all unchanged; nothing about what is measured or how it is judged moves. Unit calib's recorded result stands.

What this does NOT establish. A beacon draw is independent of the author and the lab, but it is not a human adjudication. The frozen verdict will render Q2 from the manifest by the mechanical rule of B-6, and a drawn_by of "drand beacon round 6543429" satisfies that rule; that form records only that the seed came from outside the author and the lab. The count this charter defines by external human adjudication, NORTH_STAR section 2b 'externally adjudicated predictions' 1 to 2, stays the author's to grant (B-6: the author decides whether it counts), and a BLIND-AGREES under this draw is offered to him as 'a beacon-seeded blind confrontation', not as an adjudicated one. The results file and the GRV-030 row must say 'beacon draw' and must never call the beacon an adjudicator. Everything section 7 lists as not established by a pass (the coefficient 1/2pi, data novelty, the nu shape, H0, no-evolution) remains not established.

Committed beacon: drand round 6543429 (chain 8990e7a9aaed2ffe), due 2026-10-11 15:51:30Z. Draw command: `python tools/holdout_galaxies.py draw --name GRV_BLIND_2 --seed {seed} --n 30 --drawn-by "{drawn_by}"`.
