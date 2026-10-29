# RING-WAVE-STABILITY-4: results (write-up of a rendered verdict, revision round 2)

Charter: analysis/RING-WAVE-STABILITY-4_charter_LOCKED.md. Driver, statistics and verdict: benchmarks/lab/ring_wave_stability_4/driver.py, stats.py, verdict.py. Sealed checkpoint: analysis/ring_wave_stability_4_ckpt.pkl. Every statement below is under action (i) (charter P1: Nambu-Goto plus the twist as a massless scalar on the induced metric), and is interior work (docs/NORTH_STAR.md section 5, the author's exception of 28 October 2026).

## 1. Verdict, in one paragraph

The verdict ran once from the sealed checkpoint. The harness evaluated (it did not render HARNESS-OPEN). The three forms are:

| Question | Form | Reason on the face of the verdict |
|---|---|---|
| Q1 (twist-speed channel: W1, W2, R0) | **Q1-NO-CALL** | no valid RING-UNSTABLE witness; every M = 48 class UNAVAILABLE; the M = 96 scored runs of all three probes ended in a v5 breach whose valid prefix does not bear GROWS; all three probes half-blocked |
| Q1b (neutral manifold: S3, S4, Z2, Z3) | **Q1B-NO-CALL** | gate g1: control D_shape is inf (above the 0.02 bar) at M = 48, because the M = 48 control did not complete |
| Q2 (end state of a growing or drifting witness) | **END-NOT-TRIGGERED** | neither RING-UNSTABLE nor NEUTRAL-DRIFTS was rendered (the form does not assert that no witness existed) |

Plainly: the commission did not answer its question. No form that says something about the ring rendered. It does not say the ring is stable, it does not say the ring is unstable, and it does not say shape perturbations hold or drift. Of 48 trajectories, 13 completed 40 periods and 35 ended as failure records (section 3). The verdict's form is final; nothing below re-reads it.

## 2. What was asked

From the charter (sections 1 and 3): whether the travelling-twist ring-wave (M nodes, winding 1, kappa_tw = 0.5, T = c = 1, beta = 1), perturbed by the nine locked probes at epsilon = 3e-3 (scored) and 1e-3 (check), at M = 48 and M = 96, integrated for 40 periods at 500 steps per period, (Q1) has a bounded or growing twist-speed channel, (Q1b) keeps a deformed loop near its initial shape (D_shape at or below 0.1 in units of epsilon R_d) or drifts, and (Q2) what end state a growing or drifting witness reaches. The target named in the charter is the Strength of magnets row (the electron model, gap 4). The charter states that the work is interior, moves no scorecard row, retires no input, and does not adjudicate the electron ledger's acceptance test A2 (linear stability), which stays unrun.

## 3. What was computed

48 trajectories: 2 controls at the production step, 36 evidence runs (9 probes x 2 amplitudes x 2 resolutions), a half-step control and 9 half-step runs at M = 48. Each trajectory ended in one of two ways.

Complete (40 periods, v5 clean on the raw series): 13 runs.
- ctrl_M96.
- M = 96 scored: S2, S3, S4, Z2, Z3.
- M = 96 check: S2, S3, S4, Z2, Z3, W1, W2.

Failure records (kept, never rerun): 35 runs, verified by the verdict from the retained breach row or the clean prefix ("raw-series check: 13 complete runs scan v5-clean; 35 failure record(s) verified").
- 27 Newton/init failures, all at M = 48: the production-step control ctrl_M48; the seven scored probes S2, S3, S4, Z2, Z3, W1, W2; all nine check-amplitude probes; ctrl_M48_h and the nine half-step probes (S2, S3, S4, Z2, Z3, R0, W1, W2, WU). Failure steps, from the verdict output: 10186 to 10255 for the runs at h_p (500 steps per period, so 20.37 to 20.51 periods) and 10186 to 10239 for the half-step runs (1000 steps per period, so 10.19 to 10.24 periods). Every one has 1019 to 1026 valid samples kept, all before the failure, prefix v5-clean.
- 8 v5 breaches, all of the J (angular momentum, absolute range bar 2e-6) kind: R0_M48_s (step 5310, 10.62 periods), WU_M48_s (9370, 18.74 periods), R0_M96_s (2910, 5.82 periods), W1_M96_s (6770, 13.54 periods), W2_M96_s (7330, 14.66 periods), WU_M96_s (3350, 6.70 periods), R0_M96_c (4900, 9.80 periods), WU_M96_c (8190, 16.38 periods). The breach row is excluded from every statistic.

Observations from the verdict output about the pattern, stated as observations and not as a diagnosis:
(a) The unperturbed control ctrl_M48 itself ended in a Newton/init failure, at step 10186. This shows that a failure can occur at M = 48 with no probe applied. It does not show that every probed failure has the same cause: R0_M48_s and WU_M48_s ended in J breaches (steps 5310 and 9370), a different failure kind at different steps, and a probe's contribution to any probed-run failure is not excluded or measured by this verdict.
(b) The M = 48 Newton failures fall inside one 70-step window (10186 to 10255) at both h_p and h_p / 2, that is, at about the same step count and at two different physical times (about 20.4 and about 10.2 periods).
Why this happens was not computed. The sealed runs carry no Newton iteration count (charter section 0 item 3: the instrument does not expose it), so the checkpoint cannot say whether the iteration count rose before the failure. On credentialed span: the charter (section 12 disclosure 1) and the executor's production-step record (analysis/RING_WAVE_STABILITY_leg0.md section 10) give the unperturbed ring-wave run K3 as two periods. I did not open the driver to confirm the length of the credential unit's K3 in this run. If it is two periods, the control's failure at about 20.4 periods lies well beyond any span on which the unperturbed ring-wave was credentialed at M = 48; that is a statement about the credential's span, not a cause.

All eight credential bars (v1_K1, v2_K2, v2p_K2, v2p_K3, v3_K3, v4_K4, v4b_K5, v6_K6) printed PASS. The 54-fixture stat_credential result is not quoted in the verdict tail I was given; the verdict's evaluating (rather than HARNESS-OPEN) implies the harness's own halt-grade check was passed, and I state nothing further about it.

## 4. The numbers behind each form

### Q1 (twist-speed channel)

| Probe | M = 48 scored | M = 48 check | M = 96 scored | M = 96 check |
|---|---|---|---|---|
| W1 | UNAVAILABLE (control run not complete) | UNAVAILABLE (control run not complete) | UNAVAILABLE, failure record: v5 J breach at step 6770; prefix of 13 blocks, rho 0.9999, sigma -1.084e-05 per period | BOUNDED, rho 1, sigma -2.499e-05 per period |
| W2 | UNAVAILABLE (control run not complete) | UNAVAILABLE (control run not complete) | UNAVAILABLE, failure record: v5 J breach at step 7330; prefix of 14 blocks, rho 0.9975, sigma -1.189e-04 per period | BOUNDED, rho 0.9905, sigma -2.125e-04 per period |
| R0 | UNAVAILABLE (control run not complete) | UNAVAILABLE (control run not complete) | UNAVAILABLE, failure record: v5 J breach at step 2910; prefix of 5 blocks, rho 1, sigma -7.564e-06 per period | UNAVAILABLE, failure record: v5 J breach at step 4900; prefix of 9 blocks, rho 1, sigma -5.172e-06 per period |

Half-step runs. The verdict prints "Q1 half-blocked: {'W1': True, 'W2': True, 'R0': True}" and prints each half-step Q1 class as UNAVAILABLE with rho and sigma nan. It prints no reason for those UNAVAILABLE classes. What the sealed record shows (section 3) is that each of the three half-step probe runs ended in its own Newton/init failure (W1_M48_h at step 10201, W2_M48_h at step 10214, R0_M48_h at step 10198), and that the half-step control ctrl_M48_h also ended in a Newton/init failure (step 10239). Which of these failures the decision rule used to produce each UNAVAILABLE class is not printed, and I do not assign the block to the control alone or to the probes alone; I report only that all of these runs failed and that all three probes are marked half-blocked.

The only two Q1 classes computed at all are the two M = 96, check-amplitude BOUNDED classes (W1, W2). Under the locked rules they cannot witness (witnesses need the scored amplitude at both M), and RING-STABLE needs all three probes BOUNDED at both resolutions and both amplitudes. The prefix numbers of the failed M = 96 scored runs are as the verdict printed them (table above, rho 0.9999, 0.9975 and 1 over 13, 14 and 5 blocks). The locked rules make them failure records, not classes (the prefixes do not bear GROWS); no f1/f2 floor test is applied to them as classes, and I read no effect, growth or absence of growth, from them.

Reported, not scored. Which runs: benchmarks/lab/ring_wave_stability_4/verdict.py (lines 109 to 114) loads the SCORED-amplitude run `{probe}_M{M}_s` for each of W1, W2, R0 at M = 48 and M = 96, and computes both quantities over that run's sealed valid prefix (the retained breach row is not in it). The verdict lines themselves do not name the run; the code does. The span of each prefix therefore differs by run, and each ended before the failure step shown:

| Run | Failure kind and step | Prefix ends before (periods at 500 steps per period) | Largest Phi-dot mode, n = 1 to 6 | Max abs(beta - beta_0) |
|---|---|---|---|---|
| W1_M48_s | Newton/init, 10209 | 20.42 | 4.241e-03 | 1.673e-06 |
| W2_M48_s | Newton/init, 10197 | 20.39 | 4.240e-03 | 7.076e-04 |
| R0_M48_s | v5 J breach, 5310 | 10.62 | 3.976e-07 | 4.496e-06 |
| W1_M96_s | v5 J breach, 6770 | 13.54 | 4.242e-03 | 1.428e-06 |
| W2_M96_s | v5 J breach, 7330 | 14.66 | 4.242e-03 | 6.089e-04 |
| R0_M96_s | v5 J breach, 2910 | 5.82 | 5.011e-07 | 4.487e-06 |

For scale, the scored probe's initial Phi-dot amplitude is epsilon / R_d = 3e-3 / 0.707359, about 4.24e-03 (R_d from the charter, section 4, at M = 48). The W-probe largest modes equal that initial amplitude to the printed digits; the R0 values are of a different probe (a radial kick) and have no such reference. These are descriptions of the observed prefixes, with no floor test or class attached, and I draw no stability conclusion from them. The W2 beta deviations (7.076e-04 at M = 48, 6.089e-04 at M = 96) are about 400 times those of W1 at both M; the verdict does not explain this and neither do I.

WU (family check, reported only): anomaly (run incomplete) at all four of M = 48 and 96, scored and check. The check could not be made.

### Q1b (neutral manifold)

Gates: g4 met at both M (K6 F1b reading divided by 3e-3 R_d: 1.590e-03 at M = 48, 1.001e-04 at M = 96; bar 0.02). g1 met at M = 96 (control D_shape max 6.019e-09, control slope per block 1.908e-10; bar 0.02). **g1 failed at M = 48**: ctrl_M48 did not complete, so its control D_shape maximum is recorded as inf by the verdict, and the form is Q1B-NO-CALL.

All ten M = 48 shape runs (S2, S3, S4, Z2, Z3 at both amplitudes) are UNAVAILABLE (failed runs). The five M = 48 half-step shape runs (S2_M48_h, S3_M48_h, S4_M48_h, Z2_M48_h, Z3_M48_h) exist; each ended in a Newton/init failure (steps 10186, 10213, 10212, 10215, 10233) and is printed UNAVAILABLE with "g2 blocked". The M = 96 shape runs completed at both amplitudes and the verdict reported a class for each: all HOLDS (numbers in units of epsilon R_d, bar 0.1 for HOLDS). By charter S2 a shape probe bears a class at a resolution when both its amplitudes are valid; S3, S4, Z2 and Z3 therefore bear a class at M = 96 (S2 is diagnostic only).

| Probe | scored: max D_shape (second-half slope, se per block) | check: max D_shape (second-half slope, se per block) |
|---|---|---|
| S2 (DIAGNOSTIC ONLY) | 0.006623 (2.04e-06, 5.88e-08) | 0.008494 (5.72e-07, 1.89e-07) |
| S3 | 9.879e-05 (3.018e-09, 1.06e-09) | 0.004212 (2.596e-07, 7.64e-08) |
| S4 | 0.006278 (4.065e-06, 3.66e-07) | 0.001058 (5.189e-08, 3.24e-08) |
| Z2 | 0.002701 (4.593e-08, 1.21e-07) | 0.0009 (1.189e-08, 3.11e-08) |
| Z3 | 0.00608 (1.642e-07, 3.6e-07) | 0.002025 (2.631e-08, 7.34e-08) |

These M = 96 classes did not become a form. NEUTRAL-HOLDS needs every form-bearing probe to HOLD at both resolutions, gates met and none half-blocked (locked D7 and g2/g3). At M = 48 there is no shape class (all ten scored and check runs failed) and no available half-step class (the five half-step runs failed, g2 blocked); g1 also failed at M = 48. So no form could render, and the M = 96 classes carry no cross-resolution agreement. I also note, without explaining it, that for S3 the scored-amplitude maximum (9.879e-05 in units of its epsilon R_d) is far below the check-amplitude maximum (4.212e-03 in units of its epsilon R_d). Converted to absolute units by multiplying by epsilon (3e-3 and 1e-3 respectively), that is about 3e-07 R_d against about 4e-06 R_d (a derived comparison, section 9). The charter locks no amplitude-scaling test and none was computed, so I read nothing into it.

D6 static cross-check (Leg C functional, no Coulomb term, M = 48): stationarity measure S = 6.681e-04 against the bar of 0.01 (met); negative constrained modes 0, null modes 0, dimension 87. This is a static constrained-Hessian count at one M. It is not a dynamical spectrum and not acceptance test A2. No dynamical result existed to compare it with, so no agreement or disagreement is recorded.

### Q2

Not triggered: neither RING-UNSTABLE nor NEUTRAL-DRIFTS rendered. No fold marks (R_end / R_mean > 1.3; mean twist phase speed beta < 0.5) were scored. The form does not assert that no witness existed.

## 5. What this establishes

- Under action (i), at the locked settings (kappa_tw = 0.5, M = 48 and 96, h_p = 2 pi R_d / 500 and h_p / 2 at M = 48, Newton tolerance 1e-13, the gauge-pinned instrument), no form rendered for any of the three questions that says anything about the ring: Q1-NO-CALL, Q1B-NO-CALL, END-NOT-TRIGGERED. Some classes exist beneath the forms (two BOUNDED Q1 classes at M = 96 check amplitude; HOLDS classes for S3, S4, Z2, Z3, with S2 diagnostic, at M = 96 at both amplitudes), but locked rules (witness restriction to the scored amplitude, g1 at M = 48, g2, D7 cross-M agreement) leave them without a form. The charter (section 9, "What each form would establish") says of this case: "A NO-CALL or HARNESS-OPEN form is a clean open result: nothing about the class follows."
- Every M = 48 integration at the locked settings failed before 40 periods, the unperturbed control included: ctrl_M48 ended in a Newton/init failure at step 10186 (about 20.4 periods at h_p) and ctrl_M48_h at step 10239 (about 10.2 periods at h_p / 2). The M = 96 control completed 40 periods. The cause of the M = 48 failures is unassigned. The verdict does not distinguish among the discretization of the ring-wave at M = 48, the Newton solver at this state, the gauge pin, and a property of the discrete ring-wave itself, and I do not attribute it to any of them. The control failure establishes that failure occurs without a probe; it does not exclude probe contributions to the other M = 48 failures (the two J breaches R0_M48_s and WU_M48_s are of a different kind).
- At M = 96 the 6 runs (R0, W1, W2, WU scored; R0, WU check) that ended in a v5 J breach did so at steps 2910 to 8190 (5.82 to 16.38 periods at 500 steps per period), at a J range above the absolute bar of 2e-6. The charter's J bar is an extrapolation (20 times K5's two-period bar, assuming the pin's torque accumulates linearly; charter section 6 v5 and section 12 disclosure 4). Whether these breaches are growth of the probed mode, pin-torque accumulation, or step-size error was not computed. The only Q1 classes at M = 96 are the two completed check-amplitude W runs, which classed BOUNDED against a completed M = 96 control; that is a one-resolution, one-amplitude observation carrying no form. The rho values of the three failed scored prefixes are in the section 4 table; they are failure-record statistics with no floor test, and no reading is drawn from them.
- The static D6 check found no negative constrained mode at beta = 1, M = 48, kappa_C = 0.

## 6. What this does not establish

- It does not establish that the ring-wave is stable, and does not establish that it is unstable. It does not establish RING-STABLE, RING-SLOW, RING-UNSTABLE, NEUTRAL-HOLDS, NEUTRAL-WOBBLES or NEUTRAL-DRIFTS, and it does not exclude any of them for a different run set.
- It does not pass or fail the electron ledger's acceptance test A2 (linear stability), which stays unrun; no dynamical spectrum was computed. The D6 mode count is static.
- It says nothing about action (ii) (the five-dimensional form) or any other action, about other kappa, about probes outside the locked set, about the scale wall, the O(alpha) anomaly, hbar, m_e or alpha (none enters).
- It does not diagnose the M = 48 Newton failures or the M = 96 J breaches, and it does not say whether they belong to the instrument or to the ring-wave. The near-coincidence of the M = 48 failure steps is recorded as an observation; the cause is not computed.
- The M = 96 classes are not forms and are not a partial verdict (locked D7, g1, g2, g3 forbid reading them as one). The D_shape entries of S2 are diagnostic only by the charter and carry no weight at all.
- Correlation is not mechanism: nothing here bears on whether the twist should travel or ride (charter P2 stands, and the no-rescue rule applies).

## 7. North Star scorecard

Targets moved from blocked to derived: 0. Inputs retired by derivation: 0. Discriminators armed: 0. Strength of magnets row: unchanged (electron model unbuilt, gap 4). None of the five numbers moves. This is interior work, stated as such in the charter, and it produced an open result. ELEC-G-2 (registered as ELEC-102 in claims.yaml; verdict G-OTHER, charter and ELEC-102 both record it as interior) preceded it, so this is the second interior session in a row. By the author's exception in docs/NORTH_STAR.md section 5, the session after this one must be target-facing, and the exception covers no successor of RING-WAVE-STABILITY-4.

## 8. Natural next question

The question the commission asked is unanswered: does the g = 2 ring-wave hold under finite perturbation under action (i)? It stays open and is recorded as open. The commission also leaves an unassigned instrument-level observation: every M = 48 integration, the unperturbed control included, ended before 40 periods at the locked settings, while the M = 96 control completed. That observation is kept on the record; its cause is not known.

What the rules fix about the lab's next step: docs/NORTH_STAR.md section 5 requires the session after RING-WAVE-STABILITY-4 to be target-facing, and the exception of 28 October 2026 names this one commission and does not extend to any successor of -4. Any new run of this question, or an instrument-repair or diagnostic session for the M = 48 failures, would be such a successor (a new commission asking a different question, with its own lock, and the no-rescue rule of charter section 10 applies to this verdict's settings). It is therefore not an available next session under the current rules. The next session is target-facing work; this document does not choose which.

## 9. Disclosures

- Numbers not printed in the verdict output, derived here by arithmetic and named: the period conversions (failure step divided by 500 steps per period, or by 1000 for half-step runs, charter D1 and section 6); epsilon / R_d = 3e-3 / 0.707359, about 4.24e-03; the absolute-unit S3 comparison (D_shape values multiplied by epsilon, about 3e-07 R_d and about 4e-06 R_d); the ratio of about 400 between the W2 and W1 beta deviations. Run-count totals (13 complete, 35 failures, 27 Newton, 8 v5 breaches) are tallies of the failure records in the verdict output.
- Which run the reported-not-scored numbers come from is read from verdict.py lines 109 to 114 (scored-amplitude runs), not from the verdict output; the failure steps used for their spans are from the verdict output's failure records.
- The verdict output prints no reason for the half-step UNAVAILABLE classes; section 4 reports the failure records of the half-step runs and does not infer which one the decision rule used.
- The charter quotations (section 9, "A NO-CALL or HARNESS-OPEN form is a clean open result"; section 12 disclosure 1, K3 for two periods) were checked against analysis/RING-WAVE-STABILITY-4_charter_LOCKED.md. The two-period length of K3 at the production step is also from analysis/RING_WAVE_STABILITY_leg0.md section 10.
- ELEC-102 was confirmed in the registry as the claim for ELEC-G-2 before being cited; it is cited here for session sequencing only and is not a dependency of the claim draft.
- I did not open the sealed arrays (analysis/ring_wave_stability_4_ckpt.pkl) beyond what the verdict output reports, and I did not run any instrument.
- Claim draft: analysis/lab/drafts/RING-WAVE-STABILITY-4/claim_1.yaml.

## Review record (written by the lab)

| Stage | Reviewer | Model | Result |
|---|---|---|---|
| lock r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| lock r1 | external | openai/gpt-6-astra | not passed |
| lock r2 | skeptical | anthropic/claude-opus-5-5 | pass |
| lock r2 | external | openai/gpt-6-astra | pass |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | not passed |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | pass |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| verdict r1 | external | openai/gpt-6-astra | pass |
