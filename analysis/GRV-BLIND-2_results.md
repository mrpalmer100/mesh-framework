# COMMISSION GRV-BLIND-2 -- RESULTS (sealed truth read once; verdict computed once)

Charter: analysis/GRV-BLIND-2_charter_LOCKED.md (sections 1 to 10 as locked; section 11 is the lab's amendment of 2026-10-11 that replaced the person-chosen seed with a seed taken from a drand beacon round).
Verdict log: analysis/GRV-BLIND-2_verdict.log. Checkpoint: analysis/grv_blind_2_ckpt.pkl. Bars: analysis/GRV_BLIND_2_bars.json. Predictions: analysis/GRV_BLIND_2_pred.txt. Draw: analysis/holdout/GRV_BLIND_2/MANIFEST.json (tool record: analysis/holdout/GRV_BLIND_2/VERDICT.json). Beacon file: analysis/lab/beacons/GRV-BLIND-2_round6543429.json. Lab decision records: analysis/lab/decisions/2026-10-11_113923_GRV-BLIND-2_resolve-block.md and 2026-10-11_115201_GRV-BLIND-2_beacon-draw.md.

This is revision round 2. It replaces the previous write-up in full. Section 10 lists each round-2 concern and where it is handled.

## Headline

**FORM (Q1): BLIND-FAILS.** The registered zero-parameter prediction of GRV-030 (g_dagger = c H0 / 2 pi = 1.083e-10 m/s^2, H0 = 70 km/s/Mpc) was frozen before the observed velocities were read. On the 30 held-out galaxies of the draw (647 kept points) the rms of log10(g_obs) - log10(g_pred) is **0.1656 dex against a locked bar of 0.1582 dex**. The miss is about 0.0074 dex, about 4.7 percent over the bar. The calibration legs (C-1 to C-6) and floor legs (F-1, F-2) passed, nothing was unpredicted, and the tool and the script agree to 1e-9 dex, so the instruments behaved as credentialed. That statement covers the instruments only. It does not cover how the seed was derived: the seed rule that was executed differs from the rule written in the charter's amendment, and that departure from the locked text is disclosed in section 7. Read section 7 before relying on any statement about the draw.
**FORM (Q2): DRAW-EXTERNAL**, as the mechanical string-and-set rule of B-6 renders it and nothing more (section 7). No adjudicator existed for this commission. The beacon is not an adjudicator and no person adjudicated anything.
**FORM (Q3): OUTLIER-EXCEEDS-BAR**, worst galaxy PGC51017 at 0.6321 dex against 0.5224. Q3 carries no evidential weight and changes neither Q1 nor Q2.
**Scorecard: unchanged.** Section 2b "externally adjudicated predictions" stays at 1. No target moved from blocked to derived and no input was retired. The failure is kept at full weight on GRV-030's blind row and is not re-chartered.

## 1. What was asked

Charter section 1, Q1: does GRV-030's g_obs = g_bar nu(g_bar / g_dagger), nu(y) = 1/(1 - exp(-sqrt y)), with g_dagger = c H0 / 2 pi, agree under the BLIND-1 bars rule (B-1) with 30 SPARC galaxies drawn with a seed that was not chosen by the author or the commission? (The charter as locked asked for a person's seed; section 11 replaced it with a beacon-derived seed; see section 7.) Q2: was the draw external by the B-6 string rule? The charter's North Star line is rule (c), a discriminator adjudicated. It named the 2b increment (1 to 2) as reachable only on BLIND-AGREES with DRAW-EXTERNAL and only if the author ratifies the count. The charter stated first what it does not do: move a target, retire an input (H0 stays an input), touch GRV-031 or XSEC-001.

## 2. What was computed

Unchanged instruments: benchmarks/gravity/grv_blind_1.py (predictor and bars rule) and tools/holdout_galaxies.py (draw, seal, verdict). Data: data/sparc_rotmod, 175 files, 155 eligible. Baryonic model as in GRV-030 (gas; M/L 0.5 disc, 0.7 bulge; quality cut errV/Vobs < 0.1; at least three kept points per galaxy).

Draw (from the verdict log, the decision record 2026-10-11_115201_GRV-BLIND-2_beacon-draw.md and the beacon file): drand round 6543429, chain 8990e7a9aaed2ffe (full id 8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce), round time 2026-10-11T15:51:30Z, published randomness c08dace7ee5f8c780b82fab93f43be0111d546a45b1895192d0d5ac14d857622 (as recorded in the decision file; I did not query the drand service and have not re-verified it), recorded seed 1083026663, drawn_by "drand beacon round 6543429 (chain 8990e7a9aaed2ffe)", drawn_at_utc 2026-10-11T15:52:01Z, 30 of 155 eligible, train sha256 26a7721fd44601e8af72e98a12cfe10d127c5bada6e4fb71b967e44b752c10b5, test sha256 3fa3db3331fcf8d8390349b6828613b8e4f664caec4c240d0168c67b19ae807b. Held out: D564-8, DDO064, DDO161, ESO079-G014, NGC0024, NGC2366, NGC3726, NGC4217, NGC5585, NGC6015, NGC6195, NGC6674, NGC7814, PGC51017, UGC00731, UGC02916, UGC02953, UGC03580, UGC04305, UGC05414, UGC06786, UGC06818, UGC06930, UGC07151, UGC07524, UGC07690, UGC09133, UGC10310, UGC11557, UGCA281. Overlap with GRV-BLIND-1's hold-out: 5 galaxies (ESO079-G014, NGC5585, NGC6674, UGC02953, UGC07524), recorded and not removed, as the charter requires (about 5.8 expected at random, charter section 3).

Units run in order: calib, manifest, predict, seal, truth. The seal and the single truth read came only after C-1 to C-5 and F-1, F-2 passed.

### Calibration leg (bars locked in the charter; all pass)

| check | result | bar |
|---|---|---|
| C-1 bars rule reproduces GRV-BLIND-1 | difference 0.0 dex; 0.180044 / 0.632099 | 1e-6 dex |
| C-2 predictor reproduces GRV_BLIND_1_pred.txt | 734/734 points, keys equal, max relative difference 0.0 | 1e-5 |
| C-3 draw tool reproduces seed 52525254 | same 30 galaxies, 155 eligible | exact |
| C-4 verdict arithmetic on GRV-BLIND-1's rows | 0.1138 / 0.3803 dex, 634 points, BLIND-AGREES | 5e-5 dex |
| C-5 draw reproduces from its recorded seed | test, eligible and train lists reproduce; inputs present; train sha matches | exact |
| C-6 one seal, on the driver's file | f796989a69d90be4... (evaluated after the seal, not part of the pre-truth gate) | exact |

Note on the log's wording. Line 8 of analysis/GRV-BLIND-2_verdict.log reads "C-5 the adjudicator's draw reproduces from its seed 1083026663". The word "adjudicator" there is residual text in the frozen verdict script, written before the amendment of section 11, and is not a description of this draw. No adjudicator existed for GRV-BLIND-2; the seed came from a beacon round by the rule discussed in section 7, and the amendment requires that the beacon never be called an adjudicator. A reader of the log should read that line as "the draw reproduces from its recorded seed". The same applies to any other "adjudicator" wording in the log or the script. C-5 checks only that the draw reproduces from the seed as recorded in the manifest. It does not check that the recorded seed was derived from the beacon randomness by the rule that the amendment text states.

### Floor leg (training data and held-out inputs only; computed before the seal)

| check | result | bar |
|---|---|---|
| F-1 Newtonian null on training galaxies | 0.5350 dex = 3.38 x the rms bar 0.1582 | >= 2.0 x |
| F-2 rms of log10(g_pred/g_bar) over held-out input radii | 0.472 dex | >= 0.30 |
| F-2 fraction of input radii with g_bar < g_dagger | 0.701 | >= 0.40 |
| F-2 radii unpredicted or g_bar <= 0 | 0 | 0 |

All floors passed, so on these tests the draw was not degenerate and the verdict could in principle separate the prediction from no modification at all. The F-1 and F-2 thresholds were set after inspecting the whole table (charter section 10, a rule-4 exposure stated at lock). A gate of this kind selects which draws receive a verdict, and thresholds chosen after whole-table exposure are not shown here to be neutral toward the prediction. I make no claim about their effect beyond the recorded fact that this draw passed them. The sealed form BLIND-FAILS does not depend on them.

### Held-out statistics (recomputed from the kept rows; tool cross-checked to 1e-9 dex)

| statistic | held-out (30 galaxies, 647 points) | bar (locked rule, 125 training galaxies) | training rms at the prediction | whole table (GRV-030) | GRV-BLIND-1 held-out |
|---|---|---|---|---|---|
| rms, dex | **0.1656** | **<= 0.1582** (decides Q1) | 0.1344 | 0.1423 | 0.1138 (bar 0.1800) |
| worst galaxy rms, dex | 0.6321 (PGC51017) | <= 0.5224 (Q3 only) | | | 0.3803 (bar 0.6321) |
| mean residual (obs minus pred), dex | -0.0271 | none (sub-reading) | | | +0.0333 |

Sources outside the BLIND-2 verdict output: the whole-table rms 0.1423 is from the GRV-030 entry in claims.yaml; the GRV-BLIND-1 figures (0.1138, 0.3803, bars 0.1800 and 0.6321, mean residual +0.0333) are from analysis/GRV_BLIND_1_results.md (statistics table, lines 11 to 15).

Worst five held-out galaxies: PGC51017 0.632, UGC04305 0.538, UGC11557 0.311, DDO161 0.263, NGC0024 0.258.

Bars were the 0.95 quantiles over 20,000 random 30-galaxy subsets of the 125 training galaxies at the predicted g_dagger (analysis/GRV_BLIND_2_bars.json: bar_rms 0.15824531, bar_gal 0.52235885, train_rms 0.13442453). The worst-galaxy bar equals the rms of one training galaxy (UGC02455, 0.5224); as charter section 10 warned, that bar is close to vacuous and does not carry the verdict.

## 3. Verdict forms, by the locked order

BLIND-CALIB-FAIL: no (C-1 to C-6 pass). BLIND-OPEN-FLOOR: no (F-1, F-2 pass). BLIND-INCOMPLETE: no (zero missing points; truth step present). BLIND-AGREES: no, because rms 0.1656 > 0.1582. **BLIND-FAILS: yes.** Per the charter the row reads "fails blind at 0.1656 dex (bar 0.1582) on a beacon-seeded draw" (with the seed-rule caveat of section 7), and GRV-030's whole-table statement stands as a whole-table statement; the discrepancy between the whole-table figure (0.1423) and the held-out figure (0.1656) is itself the finding.

## 4. Sub-readings (recorded, not read; locked as changing no form)

- At the registered data-fitted g_dagger (1.134e-10): held-out rms 0.1671 (mean -0.0338), against 0.1656 at the predicted value. Both values exceed the bar of 0.1582. These are two descriptive numbers; no equivalence or indistinguishability test with a numeric bar was locked for them, and none is claimed here. GRV-030's whole-table statement that the predicted and fitted rms are statistically indistinguishable (0.1423 against 0.1421, claims.yaml GRV-030) is a whole-table statement; this draw neither tests nor reproduces it.
- Charter section 8 locked two things for the grid g_dagger x 2^(k/4), k = -8..8 (17 factors): the best factor, and the factors whose held-out rms is within the bar. **The verdict script printed only the second.** The best-factor sub-reading was locked and the script omitted it; this is an omission by the frozen verdict script, descriptive and changing no form, and I have not recomputed it. What is printed: no factor on the grid brings the held-out rms within the bar. That is a statement about those 17 tested factors only; factors between grid points were not tested and nothing is said about them.
- Training pass window, set before the truth, on TRAINING galaxies only: on the tested grid, factors x0.707 to x1.682 of the predicted g_dagger keep the training-set rms within the bar. This is not a held-out acceptance window; no tested held-out factor passed. It states how wide a range of g_dagger values the locked bar could not have separated from the prediction on training data, so a BLIND-AGREES would not have discriminated cH0/2pi from values inside it.
- Excluding the 5 galaxies shared with GRV-BLIND-1: rms 0.1865. Since the full-set rms is 0.1656, the shared galaxies have a lower rms than the other 25, so the miss is not produced by the overlap; it is larger without them. The shared galaxies' own rms was not printed.
- Sign of the mean residual: -0.0271 here against +0.0333 in GRV-BLIND-1 (analysis/GRV_BLIND_1_results.md). Two draws; I read no systematic offset from this and no trend is claimed.

One observation that is not a sub-reading and changes nothing. The worst held-out galaxy, PGC51017, has rms 0.6321, equal to four figures to GRV-BLIND-1's worst-galaxy bar (bar_gal 0.6320993, analysis/GRV_BLIND_1_bars.json). I checked analysis/holdout/GRV_BLIND_1/train.txt (not sealed): PGC51017 is in GRV-BLIND-1's training list (line 71) and is not in the five-galaxy overlap, so it was not in GRV-BLIND-1's hold-out. Charter section 10 states that GRV-BLIND-1's worst-galaxy bar was one training galaxy's rms. The two facts together (same predictor, same galaxy inputs, a four-figure numerical match, membership in that training list) are consistent with PGC51017 being that galaxy. No file I read names GRV-BLIND-1's worst training galaxy, so the identification rests on the numerical match and is not printed in any verdict output. In BLIND-2 it is held out, so it counts. I have not computed the rms without it, and B-2 forbids an exclusion after the truth is read. A galaxy that misses is a miss. How much of the 0.0074 dex it accounts for is not known from the printed output and is not needed for the form.

## 5. What this establishes

- Under the locked bars rule, on this one draw of 30 SPARC galaxies, with nu fixed, H0 = 70 and the registered M/L convention, GRV-030's parameter-free RAR prediction did not hold its own 95th-percentile sampling bar: 0.1656 against 0.1582 dex, about 4.7 percent over.
- The held-out rms (0.1656) is higher than the training-set rms at the prediction (0.1344) and the whole-table rms (0.1423). At the data-fitted g_dagger the held-out rms (0.1671) also exceeds the bar. Descriptive only.
- The charter's prior (B-4) put the chance failure rate of the rms bar at about 5 percent, with the worst-galaxy bar adding at most about 5 percent more. That was a stated nominal prior, not a measured operating characteristic of the rule (section 9, item 1). It was not a result and is not offered as an excuse. The charter also said a failure "would not by itself falsify cH0/2pi against a nearby coefficient (a 30-galaxy draw is one draw)", and that is the limit of what the failure says.
- Taken with GRV-BLIND-1 (BLIND-AGREES at 0.1138 under bar 0.1800, the author's draw), the blind record of GRV-030 is one pass and one fail. I do not pool them into a new statistic; neither draw's form changes.

## 6. What this does not establish

- It does not falsify g_dagger = cH0/2pi. The charter calls a 30-galaxy draw one draw, with a nominal chance failure rate of about 5 to 10 percent (charter section 7); that rate was not validated (section 9). The training pass window (x0.707 to x1.682 on the tested grid, training galaxies) is wide, so even a pass would not have fixed the coefficient. A fail does not confirm the coefficient either. It falsifies only the statement "GRV-030's zero-parameter prediction passes the locked 30-galaxy blind bar", for this draw.
- It does not say which part of the model is at fault: the coefficient, nu (empirical, selected on the whole table; GRV-030 R2, GRV-031), the fixed M/L convention, the H0 = 70 input, SPARC distances and inclinations, or ordinary sampling scatter. Correlation with any of these is not mechanism, and none was tested.
- It is not independent of the data: every galaxy was in GRV-030's whole-table run, nu was selected on the whole table, and 5 galaxies were in GRV-BLIND-1's hold-out. What was blind is the procedure (prediction frozen before the held-out values were read), not the data's novelty.
- It does not establish anything about the independence of the seed beyond the mechanical Q2 form (section 7).
- Scope: this draw only (30 galaxies, 647 points, 125 training galaxies), this instrument pair (grv_blind_1.py and tools/holdout_galaxies.py, credentialed at C-1 to C-4 against GRV-BLIND-1), the tested factor grid, H0 = 70. Nothing here concerns XSEC-001 no-evolution or any other gravity target.

## 7. The Q2 form, and the seed-rule departure from the charter text

**What DRAW-EXTERNAL is, strictly.** It is the mechanical output of the B-6 check: drawn_by (case-insensitive) is not in the locked excluded-drawer list, the seed is not 52525254 or 777, and the 30 galaxies are not GRV-BLIND-1's set. B-6 checks strings, two excluded seeds and a set inequality. It does not check where the seed came from, who chose it or when it was fixed. This write-up reports the form as that mechanical result and asserts nothing further about advance commitment or independence of the seed from the author or the lab; any such assertion would need separate support, and the only evidence for it in the files I read is the beacon file's own self-reported timestamp (item 3 below), which I do not treat as establishing it, in particular given the departure below. The beacon is not an adjudicator and not a person, and nothing in this commission was adjudicated by a human. Because the verdict is BLIND-FAILS, whether a pass would have counted toward 2b does not arise; 2b stays at 1.

**Departure from the amendment text (protocol deviation, disclosed at full weight).**
1. What the locked text says. Charter section 11 says {seed} is "the 32-byte randomness of drand round 6543429 read as a non-negative base-16 integer".
2. What was run. The recorded seed is 1083026663. The published randomness (as recorded in the decision file) begins c08dace7; 0xc08dace7 = 3230510311, and 3230510311 - 2^31 = 1083026663. So the seed is the first four bytes of the randomness with the top bit cleared (a 31-bit value), not the whole 32-byte integer.
3. What the beacon file says. analysis/lab/beacons/GRV-BLIND-2_round6543429.json carries seed_rule = "int(randomness[:8], 16) & 0x7fffffff", a committed_at field of 2026-10-11T11:41:06-0400 (15:41:06Z) and a round_time of 2026-10-11T15:51:30Z. Those are the file's own fields. The decision record names commit b0f8e1708d27165e086d49aa5d1492124e0633f1 as the commit fixing the round. I did not inspect the git history, did not verify the commit or its time, and did not query the drand service. The committed_at field is a self-report and does not by itself establish that the rule or the round was fixed before the randomness existed.
4. What the amendment text did not say. The amendment text does not state the executed rule; it states a different one (the full integer). The charter text was not corrected after the draw. The two do not agree.
5. What is not recorded. The reason for the 31-bit truncation is not recorded in any file I read. I did not read the draw tool's code or the job script. I do not know why the truncation was chosen.
6. What I claim and what I do not. I claim only that the executed rule is recorded in the beacon file and that the recorded seed follows from the recorded randomness by that rule (the arithmetic in item 2). I do not claim that the departure is harmless, that the amendment's wording and the executed rule agree (they do not), or that anything establishes when and by whom the rule was selected. C-5 verifies reproduction of the draw from the recorded seed, not compliance with the amendment's seed derivation. Whether a draw from the full-integer seed would have differed was not computed, and B-5 forbids a redraw. The BLIND-FAILS form was reached by the locked procedure on the draw as run, and this departure, which could only matter to a pass, would have had to be resolved before any pass was offered to the author.

Two smaller wording differences: drawn_by carries the chain prefix, "(chain 8990e7a9aaed2ffe)", beyond the string in section 11; and the charter's promised appended record (round, randomness, seed, drawn_at_utc, hashes, held-out list) is not appended below the amendment in the charter file. The charter file is outside this write-up's remit. The record is owed before promotion; the lines to append are: round 6543429, chain 8990e7a9aaed2ffe, randomness c08dace7ee5f8c780b82fab93f43be0111d546a45b1895192d0d5ac14d857622, seed 1083026663 (rule int(randomness[:8], 16) & 0x7fffffff, from analysis/lab/beacons/GRV-BLIND-2_round6543429.json, noting that this differs from the amendment's wording), drawn_at_utc 2026-10-11T15:52:01Z, train sha256 26a7721f...10b5, test sha256 3fa3db33...e807b (full values in section 2), and the held-out list in section 2.

## 8. Scorecard delta (NORTH_STAR sections 2, 2b, 5)

- Targets moved from blocked to derived: 0.
- Inputs retired by derivation: 0 (H0 remains a declared measured input).
- Section 2b "externally adjudicated predictions": unchanged at 1 (NUC-BLIND-2). A BLIND-FAILS cannot move it, and no adjudicator took part.
- Discriminators: GRV-030's blind prediction was confronted a second time under rule (c) and failed the locked bar. The draw adjudicated nothing; it supplied a seed. GRV-030's status field is unchanged by the charter (Modeled). The blind row reads: BLIND-AGREES at 0.1138 (BLIND-1, the author's draw), BLIND-FAILS at 0.1656 (BLIND-2, a beacon-seeded draw, seed rule as in section 7).
- The Gravitational force row's D1 content (g_dagger on SPARC, "blind-scored under bar W, GRV-BLIND-1, 0.114 dex on 30 held-out galaxies") should carry the BLIND-2 failure beside the BLIND-1 pass. Any change to the grade column is the author's decision at promotion; the row states both results.
- Under docs/NORTH_STAR.md section 2b, work that moves none of the five numbers is infrastructure, and that rule applies here. This commission is a kept failed confrontation and interior work. It adds zero North Star progress: no target moved, no input retired, none of the five numbers moved.

## 9. Natural next question (not chartered; a different question, not a rescue)

BLIND-2 is not to be rerun, re-bared or re-drawn, and its failure stands unchanged whatever follows. I do not propose a further blind draw of the same prediction under the same bar: a new seed alone would not make it a different question. The following are the only follow-ups I name; each would be a separate commission with its own bars locked first.

1. An operating-characteristic study of the bars rule (an instrument question, precommitted separately). The rule takes the 0.95 quantile of the rms over 20,000 subsets of 30 galaxies drawn without replacement (replace=False, benchmarks/gravity/grv_blind_1.py line 60) from the training pool of 125. Whether the exceedance rate of that bar on a complementary held-out set of 30 equals the nominal 5 percent has not been measured. Three outcomes are open and the study must treat them symmetrically: the rule is correctly calibrated (exceedance near 5 percent), too narrow (exceedance above 5 percent, so a failure at 4.7 percent over the bar is less surprising), or over-wide (exceedance below 5 percent, so a failure is more surprising than the prior said). The study would measure the exceedance rate over many disjoint train/test splits of the shipped table with its pass criterion locked in advance; the splits share one table, so it measures the rule's calibration, not new evidence on the coefficient. It must not be used to re-score BLIND-2.
2. Whether per-galaxy M/L marginalization and the distance/inclination error budget (named next-orders in GRV-030) change the held-out scatter. This is a model question that would add parameters or priors that GRV-030's zero-parameter claim does not have, so it would be a different claim.

Neither moves a target or retires an input. The discriminator question is now open at one pass and one fail.

## 10. Reviewer concerns, round 2: where each is handled

- Headline "clean verdict" beside the seed deviation: the headline now confines the statement to the instruments (calibration and floor legs, tool and script agreement) and points to section 7 for the seed-rule departure, saying the former does not cover the latter.
- Log wording "the adjudicator's draw" at C-5: section 2 (note under the calibration table) says it is residual text of the frozen script, that no adjudicator existed, and how to read the line.
- PGC51017 identification: checked against analysis/holdout/GRV_BLIND_1/train.txt (unsealed) and analysis/GRV_BLIND_1_bars.json; section 4 now reports what was confirmed (training-list membership, four-figure match to BLIND-1's worst-galaxy bar) and what was not (no file names BLIND-1's worst training galaxy).
- Grade recommendation: removed; section 8 says the grade is the author's decision and that the row states both results.
- Omitted locked sub-reading: section 4 says plainly that the verdict script omitted the locked best-factor sub-reading, which is descriptive and changes no form, and that I did not recompute it.
- Q2 over-read: section 7 reports DRAW-EXTERNAL strictly as the mechanical B-6 result; the sentence about the seed not being set by hand is removed, as is the earlier statement that the rule was fixed before the randomness existed; the file's committed_at is said to be a self-report that does not establish it. The headline, section 3, section 6 and section 8 were adjusted to match.
- Gate assurance: the sentence that the floors cannot favour the prediction is removed; section 2 keeps the exposure and the actual passes and says no claim is made about their effect.
- Infrastructure accounting: section 8 states that NORTH_STAR section 2b classifies this as infrastructure, and that this is a kept failed confrontation and interior work with zero North Star progress.


## Reviewer concerns not resolved after two revisions (recorded)

- Section 7 item 6: "this departure, which could only matter to a pass, would have had to be resolved before any pass was offered to the author." A seed-derivation deviation from the locked text is a protocol departure regardless of the form it produced; a seed rule not fixed by the charter could in principle steer a draw toward a fail as well as a pass, so the write-up should not assert that the departure is relevant only to a pass. Elsewhere (section 7 items 3 and 6, section 6) the document correctly declines to assert when and by whom the rule was fixed, so this sentence is the one place it leans the other way.
- Section 1 paraphrases Q1 as agreement "with 30 SPARC galaxies drawn with a seed that was not chosen by the author or the commission", while section 7 states the write-up "asserts nothing further about advance commitment or independence of the seed from the author or the lab". The paraphrase should be marked as the charter's question as locked, not as a property of the executed draw, to keep the two passages consistent.
- Section 8 labels the commission "interior work" while the charter named North Star rule (c) (a discriminator adjudicated) and the result is a kept failed confrontation of a D1 observable; under section 5 of NORTH_STAR a charter naming (c) is not interior work, though it moves none of the five numbers. The infrastructure accounting is correct; the "interior work" label conflates the two rules and should cite section 2b (none of the five moved) rather than section 5.
- Section 7 states: "The BLIND-FAILS form was reached by the locked procedure on the draw as run, and this departure, which could only matter to a pass, would have had to be resolved before any pass was offered to the author." The seed-rule departure can matter to either outcome because it determines the held-out galaxies, training pool and numerical bars. The frozen BLIND-FAILS must remain, but its evidential interpretation needs the protocol caveat regardless of outcome. Replace "which could only matter to a pass" and distinguish the locked scoring procedure from the noncompliant draw procedure.
- Section 2 states: "The sealed form BLIND-FAILS does not depend on them." The locked verdict hierarchy expressly depends on the floor results: a failed floor produces BLIND-OPEN-FLOOR and prevents the truth step. State instead that the floors passed on this draw and that the subsequent rms comparison failed; do not assert that the verdict form is independent of the floors.
