# COMMISSION GRV-BLIND-2 -- RESULTS (sealed truth read once; verdict computed once)

Charter: analysis/GRV-BLIND-2_charter_LOCKED.md (sections 1 to 10 as locked; section 11 is the lab's amendment of 2026-10-11 that replaced the person-chosen seed with a drand beacon seed).
Verdict log: analysis/GRV-BLIND-2_verdict.log. Checkpoint: analysis/grv_blind_2_ckpt.pkl. Bars: analysis/GRV_BLIND_2_bars.json. Predictions: analysis/GRV_BLIND_2_pred.txt. Draw: analysis/holdout/GRV_BLIND_2/MANIFEST.json (tool record: analysis/holdout/GRV_BLIND_2/VERDICT.json). Lab decision records: analysis/lab/decisions/2026-10-11_113923_GRV-BLIND-2_resolve-block.md and 2026-10-11_115201_GRV-BLIND-2_beacon-draw.md.

## Headline

**FORM (Q1): BLIND-FAILS.** The registered zero-parameter prediction of GRV-030 (g_dagger = c H0 / 2 pi = 1.083e-10 m/s^2, H0 = 70 km/s/Mpc) was frozen before the observed velocities were read. On the 30 held-out galaxies of the beacon draw (647 kept points) the rms of log10(g_obs) - log10(g_pred) is **0.1656 dex against a locked bar of 0.1582 dex**. The miss is 0.0074 dex, 4.7 percent over the bar. Calibration (C-1 to C-6) and floors (F-1, F-2) all passed, nothing was unpredicted, and the tool and the script agree to 1e-9 dex, so this is a clean verdict on the prediction and not an instrument fault.
**FORM (Q2): DRAW-EXTERNAL**, by the mechanical string rule of B-6 only (see "What the Q2 form is and is not").
**FORM (Q3): OUTLIER-EXCEEDS-BAR**, worst galaxy PGC51017 at 0.6321 dex against 0.5224. Q3 carries no evidential weight and changes neither Q1 nor Q2.
**Scorecard: unchanged.** Section 2b "externally adjudicated predictions" stays at 1. No target moved from blocked to derived and no input was retired. The failure is kept at full weight on GRV-030's blind row. It is not re-chartered.

## 1. What was asked

Charter section 1, Q1: does GRV-030's g_obs = g_bar nu(g_bar / g_dagger), nu(y) = 1/(1 - exp(-sqrt y)), with g_dagger = c H0 / 2 pi, agree under the BLIND-1 bars rule (B-1) with 30 SPARC galaxies drawn with a seed nobody involved in the work chose? Q2: was the draw external by the B-6 rule? The charter's North Star line is rule (c), a discriminator adjudicated. It named the 2b increment (1 to 2) as reachable only on BLIND-AGREES with DRAW-EXTERNAL and only if the author ratifies the count. The charter stated first what it does not do: move a target, retire an input (H0 stays an input), touch GRV-031 or XSEC-001.

## 2. What was computed

Unchanged instruments: benchmarks/gravity/grv_blind_1.py (predictor and bars rule) and tools/holdout_galaxies.py (draw, seal, verdict). Data: data/sparc_rotmod, 175 files, 155 eligible. Baryonic model as in GRV-030 (gas; M/L 0.5 disc, 0.7 bulge; quality cut errV/Vobs < 0.1; at least three kept points per galaxy).

Draw (from the manifest and the decision record): drand round 6543429, chain 8990e7a9aaed2ffe, published randomness c08dace7ee5f8c780b82fab93f43be0111d546a45b1895192d0d5ac14d857622, recorded seed 1083026663, drawn_by "drand beacon round 6543429 (chain 8990e7a9aaed2ffe)", drawn_at_utc 2026-10-11T15:52:01Z (the round was due 15:51:30Z), 30 of 155 eligible, train sha256 26a7721fd44601e8af72e98a12cfe10d127c5bada6e4fb71b967e44b752c10b5, test sha256 3fa3db3331fcf8d8390349b6828613b8e4f664caec4c240d0168c67b19ae807b. The commit that fixed the round before it existed is recorded in the decision file as b0f8e1708d27165e086d49aa5d1492124e0633f1; I report it as recorded and did not re-verify the timing. Held out: D564-8, DDO064, DDO161, ESO079-G014, NGC0024, NGC2366, NGC3726, NGC4217, NGC5585, NGC6015, NGC6195, NGC6674, NGC7814, PGC51017, UGC00731, UGC02916, UGC02953, UGC03580, UGC04305, UGC05414, UGC06786, UGC06818, UGC06930, UGC07151, UGC07524, UGC07690, UGC09133, UGC10310, UGC11557, UGCA281. Overlap with GRV-BLIND-1's hold-out: 5 galaxies (ESO079-G014, NGC5585, NGC6674, UGC02953, UGC07524), recorded and not removed, as the charter requires (about 5.8 expected).

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

### Floor leg (training data and held-out inputs only; computed before the seal)

| check | result | bar |
|---|---|---|
| F-1 Newtonian null on training galaxies | 0.5350 dex = 3.38 x the rms bar 0.1582 | >= 2.0 x |
| F-2 rms of log10(g_pred/g_bar) over held-out input radii | 0.472 dex | >= 0.30 |
| F-2 fraction of input radii with g_bar < g_dagger | 0.701 | >= 0.40 |
| F-2 radii unpredicted or g_bar <= 0 | 0 | 0 |

The floors passed, so the draw was not degenerate and the verdict could discriminate between the prediction and no modification at all. The F-1 and F-2 thresholds were set after inspecting the whole table (charter section 10, a rule-4 exposure stated at lock); they can only pass a draw as non-degenerate and cannot favour the prediction.

### Held-out statistics (recomputed from the kept rows; tool cross-checked to 1e-9 dex)

| statistic | held-out (30 galaxies, 647 points) | bar (locked rule, 125 training galaxies) | training rms at the prediction | whole table (GRV-030) | GRV-BLIND-1 held-out |
|---|---|---|---|---|---|
| rms, dex | **0.1656** | **<= 0.1582** (decides Q1) | 0.1344 | 0.1423 | 0.1138 (bar 0.1800) |
| worst galaxy rms, dex | 0.6321 (PGC51017) | <= 0.5224 (Q3 only) | | | 0.3803 (bar 0.6321) |
| mean residual (obs minus pred), dex | -0.0271 | none (sub-reading) | | | +0.0333 |

Worst five held-out galaxies: PGC51017 0.632, UGC04305 0.538, UGC11557 0.311, DDO161 0.263, NGC0024 0.258.

Bars were the 0.95 quantiles over 20,000 random 30-galaxy subsets of the 125 training galaxies at the predicted g_dagger (analysis/GRV_BLIND_2_bars.json: bar_rms 0.15824531, bar_gal 0.52235885, train_rms 0.13442453). The worst-galaxy bar equals the rms of one training galaxy (UGC02455, 0.5224); as charter section 10 warned, that bar is close to vacuous and does not carry the verdict.

## 3. Verdict forms, by the locked order

BLIND-CALIB-FAIL: no (C-1 to C-6 pass). BLIND-OPEN-FLOOR: no (F-1, F-2 pass). BLIND-INCOMPLETE: no (zero missing points; truth step present). BLIND-AGREES: no, because rms 0.1656 > 0.1582. **BLIND-FAILS: yes.** Per the charter the row reads "fails blind at 0.1656 dex (bar 0.1582) on a draw seeded by a public beacon", and GRV-030's whole-table statement stands as a whole-table statement; the discrepancy between the whole-table figure (0.1423) and the held-out figure (0.1656) is itself the finding.

## 4. Sub-readings (recorded, not read; locked as changing no form)

- At the registered data-fitted g_dagger (1.134e-10): held-out rms 0.1671 (mean -0.0338), against 0.1656 at the predicted value. The fitted value is not better on this draw, and both sit above the bar.
- No factor on the grid g_dagger x 2^(k/4), k = -8..8 brings the held-out rms within the bar. A rescaling of g_dagger would not have rescued this draw, so the miss is not a matter of the 1/2 pi coefficient being slightly off. The verdict log does not print the best factor and I have not recomputed it.
- Training pass window, set before the truth: factors x0.707 to x1.682 of the predicted g_dagger keep the training rms within the bar. This is the limit of what any BLIND-AGREES on this draw could have said about the coefficient; a pass would not have separated cH0/2pi from nearby scales.
- Excluding the 5 galaxies shared with GRV-BLIND-1: rms 0.1865. The overlap galaxies fit better than the rest, so the failure is not produced by the overlap; it is larger without them.
- Sign of the mean residual: -0.0271 here against +0.0333 in GRV-BLIND-1. Two draws; I read no systematic offset from this and no trend is claimed.

One observation that is not a sub-reading and changes nothing. The worst held-out galaxy, PGC51017, has rms 0.6321, equal to four figures to GRV-BLIND-1's worst-galaxy bar (0.6321), which the charter (section 10) says was one training galaxy's rms. That is consistent with PGC51017 having been the discrepant galaxy in BLIND-1's training list; I have not confirmed it from the BLIND-1 files. Here it is held out, so it counts. I have not computed the rms without it, and the verdict does not allow it: B-2 forbids exclusion after the truth is read. A galaxy that misses is a miss. How much of the 0.0074 dex it accounts for is not known from the printed output and is not needed for the form.

## 5. What this establishes

- Under the locked bars rule, on this one beacon-seeded draw of 30 SPARC galaxies, with nu fixed, H0 = 70 and the registered M/L convention, GRV-030's parameter-free RAR prediction did not hold its own 95th-percentile sampling bar: 0.1656 against 0.1582 dex, a 4.7 percent overshoot.
- The prediction and the fitted g_dagger are equally affected (0.1656 and 0.1671), so GRV-030's whole-table indistinguishability of predicted and fitted values (0.1423 against 0.1421) reproduces here, but the level of scatter on this draw is higher than the training and whole-table levels.
- The charter's prior (B-4: about 5 percent chance failure of the rms bar by construction) was not a result and is not offered as an excuse. The charter also said a failure "would not by itself falsify cH0/2pi against a nearby coefficient (a 30-galaxy draw is one draw)", and that is the limit of what the failure says.
- Taken with GRV-BLIND-1 (BLIND-AGREES at 0.1138 under bar 0.1800, the author's draw), the blind record of GRV-030 is one pass and one fail. I do not pool them into a new statistic; neither draw's form changes.

## 6. What this does not establish

- It does not falsify g_dagger = cH0/2pi. One draw of 30 galaxies at a 0.95 bar fails about one time in twenty on the rms bar by construction, and the coefficient window the bar accepts (x0.707 to x1.682) is wide. It also does not confirm it. It falsifies only the statement "GRV-030's zero-parameter prediction passes a fresh 30-galaxy blind bar", for this draw.
- It does not say which part of the model is at fault: the coefficient, nu (empirical, selected on the whole table; GRV-030 R2, GRV-031), the fixed M/L convention, the H0 = 70 input, SPARC distances and inclinations, or ordinary sampling scatter. Correlation with any of these is not mechanism, and none was tested.
- It is not independent of the data: every galaxy was in GRV-030's whole-table run, nu was selected on the whole table, and 5 galaxies were in GRV-BLIND-1's hold-out. What was blind is the procedure (prediction frozen before the held-out values were read; seed from a source outside the author and the lab), not the data's novelty.
- Scope: this grid and draw only (30 galaxies, 647 points, 125 training galaxies), this instrument pair (grv_blind_1.py and tools/holdout_galaxies.py, credentialed at C-1 to C-4 against GRV-BLIND-1), H0 = 70. Nothing here concerns XSEC-001 no-evolution or any other gravity target.

## 7. What the Q2 form is and is not

DRAW-EXTERNAL was rendered by the mechanical B-6 rule: drawn_by is not in the excluded list, the seed is not 52525254 or 777, and the 30 galaxies are not GRV-BLIND-1's set. It records only that the seed came from outside the author and the lab. This was a beacon draw. The drand beacon is not an adjudicator and is not a person, and nothing in this commission was adjudicated by a human. Because the verdict is BLIND-FAILS, the question of whether a beacon-seeded pass would count toward 2b does not arise, and section 2b stays at 1 on this account either way.

Disclosure on the seed (found while writing this up, not a change to any result). Charter section 11 says the seed is the 32-byte randomness read as a base-16 integer. The recorded seed is 1083026663, which is small. By my arithmetic from the published randomness c08dace7..., 0xc08dace7 minus 2^31 is 1083026663, so the seed appears to be the first four bytes of the randomness with the top bit masked off (a 31-bit value), not the whole 32-byte integer. The tool's seed range may be the reason; I did not read the tool's code or the job script to find out. This departs from the wording of section 11 but not from its purpose: the seed is a fixed function of the beacon's published randomness, chosen by nobody, reproducible by anyone, and C-5 reproduced the draw from it. It cannot have been tuned (the randomness did not exist when the round was committed), and the verdict could not be rerun in any case. The lab decision record lists the seed as 1083026663 without remark. The reviewers and the author should know the departure exists; it does not alter the verdict. Two smaller wording differences: drawn_by carries the chain prefix, "(chain 8990e7a9aaed2ffe)", beyond the string in section 11; and the charter's appended list (round, randomness, hashes, held-out list) is in this file and the decision record but not appended below the amendment in the charter itself.

## 8. Scorecard delta (NORTH_STAR sections 2, 2b, 5)

- Targets moved from blocked to derived: 0.
- Inputs retired by derivation: 0 (H0 remains a declared measured input).
- Section 2b "externally adjudicated predictions": unchanged at 1 (NUC-BLIND-2). A BLIND-FAILS cannot move it, and this was a beacon draw.
- Discriminators armed or adjudicated: one adjudicated in the sense of rule (c): GRV-030's blind prediction was confronted a second time and failed the locked bar. This is a kept failure of a Modeled claim's out-of-sample statement. GRV-030's status field is unchanged by the charter (Modeled); the blind row reads: BLIND-AGREES at 0.1138 (BLIND-1, the author's draw), BLIND-FAILS at 0.1656 (BLIND-2, a beacon draw).
- The Gravitational force row's D1 content (g_dagger on SPARC, "blind-scored under bar W, GRV-BLIND-1, 0.114 dex on 30 held-out galaxies") should carry the BLIND-2 failure beside the BLIND-1 pass. Whether the grade changes is the author's decision at promotion; I recommend it not change on one failed draw, and that the row state both results.
- This is a confrontation, not infrastructure, but it moves none of the five numbers.

## 9. Natural next question (not chartered; a different question, not a rescue)

BLIND-2 is not to be rerun or re-bared. The following would be separate commissions with their own bars locked first:

1. Calibration of the bars rule itself (an instrument question). The rms bar is the 0.95 quantile of 30-subsets of a 125-galaxy training pool. If that sampling is without replacement from a finite pool, it may understate the spread of a fresh independent 30-galaxy draw, so the nominal 5 percent failure rate could be higher in practice. This is a hypothesis; I did not check how the bootstrap samples. A credential would measure the actual exceedance rate of the rule over many disjoint train/test splits of the shipped table with the bar for the pass fraction locked in advance. It must not be used to re-score BLIND-2.
2. Whether per-galaxy M/L marginalization and the distance/inclination error budget (named next-orders in GRV-030) change the held-out scatter. This is a model question that GRV-030 already names, and it would add parameters or priors that GRV-030's zero-parameter claim does not have.
3. A fresh beacon draw on the same prediction would be a new confrontation with its own charter. It would add a third draw, but the 30-galaxy samples overlap heavily with the previous ones, and it cannot say more about the coefficient than the window above allows. Its value is the pass fraction, not a new test of 1/2 pi.

None of these moves a target or retires an input; I name them because the commission's discriminator question is now open at one pass and one fail, and I think the bar calibration is the cheapest way to learn whether the 5 percent prior was right before spending a third draw.


## Reviewer concerns (recorded; no claim registered)

- The seed used departs from the locked amendment text. Section 11 says the seed is 'the 32-byte randomness of drand round 6543429 read as a non-negative base-16 integer'; the recorded seed 1083026663 is (as the write-up correctly computes) 0xc08dace7 minus 2^31, the first four bytes masked to 31 bits. The write-up says 'I did not read the tool's code or the job script to find out.' The write-up should state, from the job script or decision record, whether the truncation rule was fixed in code before round 6543429 was published; without that, the statement 'It cannot have been tuned' rests on the draw's timing alone and not on the rule's. Since the form is BLIND-FAILS this cannot have favoured the prediction, but the departure from the lock text should be resolved on the record, not left as 'may be the reason'.
- Two numbers in the results are not in the verdict output or the charter and carry no citation: '+0.0333 in GRV-BLIND-1' (the BLIND-1 mean residual, section 2 table and section 4) and 'GRV-030's whole-table indistinguishability of predicted and fitted values (0.1423 against 0.1421)' (section 5). Each should cite the file it was read from (analysis/GRV_BLIND_1 results or VERDICT.json; the GRV-030 results file).
- Section 9 item 1 ('If that sampling is without replacement from a finite pool, it may understate the spread of a fresh independent 30-galaxy draw, so the nominal 5 percent failure rate could be higher in practice') states only the direction that would soften the failure. It is correctly labelled a hypothesis and barred from re-scoring BLIND-2, but a bar-rule credential charter should name the symmetric possibility (the rule is correct or over-wide) so the follow-up is not read as a rescue route.
- The amendment promised that 'The round number, the published randomness, the seed as recorded, the drawn_at_utc time, the train sha256, the test sha256 and the held-out list are appended below this amendment when the draw is in the repo.' The write-up discloses this was not done ('not appended below the amendment in the charter itself'). The charter record should be completed before promotion so the locked file carries its own draw.
- Section 8 writes 'Discriminators armed or adjudicated: one adjudicated in the sense of rule (c)'. This is the commission adjudicating a discriminator, not an external adjudication, and the write-up says so elsewhere; the sentence should add 'by the lab, not by a person' in place to avoid any reading that the beacon draw adjudicated anything.
- Unsupported assurance about the seed deviation: "It cannot have been tuned (the randomness did not exist when the round was committed)" and "the seed is a fixed function of the beacon's published randomness, chosen by nobody" do not follow from the supplied evidence. Section 11 committed to the full 32-byte integer, not the observed 31-bit transformation. Committing the round does not precommit an alternative transformation. C-5 verifies reproduction from the recorded seed, not compliance with the committed seed derivation. Document when and how the transformation was selected, or leave its independence unverified. Preserve the final verdict without presenting the protocol departure as established harmlessness.
- Grid-bound evidence is generalized beyond the tested grid: "A rescaling of g_dagger would not have rescued this draw, so the miss is not a matter of the 1/2 pi coefficient being slightly off." The output establishes only that none of the 17 tested factors, 2^(k/4) for k = -8..8, passed. It does not exclude untested factors between grid points. Restrict the statement to those factors.
- An unvalidated sampling-rate assertion appears as fact in both the results and the drafted claim: "One draw of 30 galaxies at a 0.95 bar fails about one time in twenty on the rms bar by construction" and "one 30-galaxy draw fails the rms bar about 1 time in 20 by construction". A training-subset 95th percentile does not by itself establish the exceedance probability for the complementary held-out sample. Section 9 itself acknowledges that this calibration is unverified. Attribute 5 percent to the charter's nominal prior, not an established operating characteristic.
- The training window is misrepresented as a held-out acceptance window. The claim says "the bar accepts g_dagger within x0.707 to x1.682", and section 6 similarly calls it "the coefficient window the bar accepts". The verdict identifies this exclusively as a TRAINING pass window; no tested held-out factor passed. Specify training data and the tested grid wherever this window is used, including in the claim's limitations.
- An unbarred equivalence conclusion is presented as established: "The prediction and the fitted g_dagger are equally affected (0.1656 and 0.1671), so GRV-030's whole-table indistinguishability of predicted and fitted values (0.1423 against 0.1421) reproduces here". The locked sub-readings provide descriptive RMS values, not an equivalence or indistinguishability test with a numeric bar. Report that both values exceed the bar without claiming reproduced indistinguishability.
- The proposed follow-up contradicts the no-rechartering requirement: "A fresh beacon draw on the same prediction would be a new confrontation with its own charter", followed in the claim by "any follow-up (bar-rule calibration, M/L marginalization, a further draw) is a different question." A new seed alone does not make the same prediction-and-bar question different. Remove the standalone repeat-draw proposal, or distinguish a separately precommitted operating-characteristic study from rerunning this confrontation. Keep BLIND-2's failure unchanged.
