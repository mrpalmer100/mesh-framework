# COMMISSION RING-WAVE-STABILITY-4 -- IS THE g = 2 STATE A STABLE OBJECT? THE TRAVELLING-TWIST RING UNDER PERTURBATION
# (fourth name. -2 and -3 were withdrawn in review without a verdict. Charter drafted by the domain worker from the
# author's draft analysis/RING_WAVE_STABILITY_4_charter_DRAFT.md; a measurement by time integration with the outcome unknown to
# everyone; harness on benchmarks/lab/_kit/labkit.py; the executor's instruments credentialed on known answers only.)

## 0. WORKER'S CORRECTIONS TO THE AUTHOR'S DRAFT (read first; each is a departure, each is stated with its reason)
1. THE ENERGY MARK OF Q2 IS UNREACHABLE AND IS NOT SCORED. The draft's Q2 asks whether a growing run's end state has "E
   within 5 percent of the fold's 8.144". Under action (i) the energy E is conserved, and bar v5 requires it conserved to
   1e-4 relative on every valid run. The unperturbed ring-wave has E = 2 pi sqrt(kappa) + 2 pi kappa / sqrt(kappa) =
   4 pi sqrt(0.5) = 8.886 (closed form; the instrument's K3 record reads 8.8826 at M = 48, analysis/ring_wave_dynamics_leg0.json),
   which is 1.0911 times 8.144 and above the draft's window ceiling of 1.05 x 8.144 = 8.551. A probe of amplitude 3e-3 changes
   E by O(1e-5) relative. So the draft's E mark is false for every v5-valid run, END-FOLD could never render, and Q2 would be
   END-OTHER or not triggered by arithmetic: a form that cannot be reached is manufactured information. The fix, written
   before any evidence run: the two shape-and-speed marks (R_end / R_mean > 1.3; mean twist phase speed beta < 0.5) are the
   scored fold marks, E is REPORTED beside them and never scored. A reader who wants "the fold" should read END-FOLD as
   "reached the fold's shape and speed marks at the ring-wave's own, higher, conserved energy". The author may reject this
   correction; if so Q2 reduces to END-OTHER / END-NOT-TRIGGERED by the arithmetic above and the lock should say so.
2. SMOKE IS STRICTER THAN THE DRAFT'S. The draft allowed one unperturbed beta = 1 integration (K3 at M = 16). The smoke run
   here runs no beta = 1 state at all: it uses the beta = 0.5 family member (K5's state) for every integration. One
   worker-side code-path check of the evidence-mode credential unit was run at M = 16 (disclosure 2); it carries no probe.
3. D3 DEVIATIONS, forced by the instrument (which is credentialed and not changed): the Newton iteration count is not
   exposed by ring_wave_dynamics.StringIntegrator.step(); a Newton failure is its RuntimeError and is the failure record.
   The n = 0 Fourier entry of the mean-subtracted fields is identically zero, so the series carry the means themselves
   (R_mean, mean z, mean Phi-dot) instead. The constraint violation is the equal-spacing spread of the segment lengths at
   each sample, v5's 1e-10 applied to it.
4. D_SHAPE IS COMPUTED IN A DRIVER UNIT, not in the verdict: one unit per shape run (dshape_<run>), from the SEALED node
   frames only, after all trajectories are sealed; the verdict reads the sealed D_shape arrays. Same arithmetic as the draft's
   "verdict unit", moved so a long verdict cannot burn the one-shot verdict reservation.
5. THE OPEN FORM. labkit's open form is one token for all questions, so the form list carries HARNESS-OPEN (the harness could
   not evaluate: checkpoint not terminal, a halt, a broken seal, an exception). It renders for Q1, Q1b and Q2 together. The
   per-question NO-CALL forms of the draft are kept for the cases the harness evaluated and the statistics could not decide.
6. PRECEDENCE AND PREDICATES the draft left open are fixed in section 6 (STATISTICS AS IMPLEMENTED) before any evidence run;
   notably D7 and gate g3 act on a witness probe's own class (an existential witness is not blocked by a disagreement of a
   different probe), and g1's slope part acts on drifting runs only.
7. D6 (the static cross-check) is run without the Coulomb term (kappa_C = 0) so that alpha enters nowhere, matching the dynamics.
   Its M is 48.

## 1. WHERE IT STANDS (the honest sentence, before the question)
One registered mechanism class reaches the electron's g = 2 by mechanics with nothing tuned: a closed rope whose one unit
of twist travels along it at c, the static ring at R^2 = kappa / T where the wave's momentum flux holds the ring against its
tension (analysis/ELEC_MECH_1_legC_instrument.md; g = E / E_wave = 2 by the scale virial for any static shape). Its first
price, written on its face since Leg C, is stability: at equal kappa and J the ring-wave sits 9 percent ABOVE the co-moving
fold (the twist riding with the material, g about 0.9), and no registered reason makes the twist travel rather than ride.
Acceptance test A2 of the electron ledger (linear stability) has never been run on any candidate. Two things could protect
the ring: the conserved twist charge and angular momentum, and the fact that the static ring is one member of a continuous
family of stationary solutions (R^2 = kappa (1 + beta^2) / 2T at twist phase speed beta, J = 2 pi kappa beta; Leg 0 part 2,
section 7 ii). One thing is KNOWN before the lock, from Leg C's shape theorem and confirmed dynamically on the beta = 0.5
member (Leg 0 part 2, K5): a static closed loop of the right length with its twist travelling is stationary for EVERY shape
(kappa Phi-dot Phi' = T at every point fixes only L). Shape perturbations at fixed length are therefore NEUTRAL at first
order. The stability question is two sharper ones: does a perturbation of the TWIST'S PHASE SPEED, the channel from
travelling to co-moving twist, grow or oscillate; and does the finite-amplitude shape distance of a deformed loop from its
initial shape stay small or grow over 40 periods. Nobody knows either answer. The answers say whether the locked probes
grow or drift under action (i); they do not decide whether the class is a candidate free electron: that needs the electron
ledger's acceptance test A2 (linear stability) and the scale wall, neither of which this commission runs.

NORTH STAR ACCOUNTING (house rule 6, stated plainly). This is INTERIOR work. It moves no scorecard row (strength of magnets,
gap 4: the electron model stays unbuilt) and none of the five numbers, retires no input, and arms no registered discriminator.
It measures whether locked finite-amplitude probes of the one class with g = 2 grow or drift under action (i). It does NOT
adjudicate the electron ledger's A2. ELEC-G-2 (22 October 2026) was interior and no target-facing session has completed since,
so under docs/NORTH_STAR.md section 5 as written this would be a second consecutive interior session; it locks only under the
author's dated exception on that page ("Exception, recorded by the author on 28 October 2026"), which names this commission,
covers one commission and one lock, and requires the session after it to be target-facing. No successor of -4 is covered.

## 2. THE PREMISE (disclosed; not a question; nothing here bears a form)
P1. THE ACTION. Two actions reduce to Leg C's static functional at small twist and differ at O(1) exactly at the ring-wave
    (kappa Phi'^2 / T = 1): (i) Nambu-Goto plus the twist as a massless scalar on the string's INDUCED metric,
    S = -Int sqrt(-h) [T + (kappa / 2) h^ab d_a Phi d_b Phi]; (ii) Nambu-Goto in five dimensions with the twist as a fifth
    target coordinate. The registry does not fix the covariant form of the twist's action on a moving rope (GRV-018, GRV-020,
    EM-RECON-012, EM-019 state the static energy, the wave speed c and the momentum density). The instrument implements (i).
    EVERY dynamics decision below is conditional on action (i); the conditional travels on the face of every rendered form as
    the words "under action (i)". Whether the registry owes (i), (ii) or another form is the theorist's reading, not this
    commission's.
P2. THE CLAUSE IN TENSION. GRV-020's Corollary 1 clause "torsion dynamics = light" carries a registry flag: it is "in computed
    tension with the carrier channel-map (EM-RECON-022/023)" and was split to GRV-102 (Open). This commission does not take a
    side: it assumes the twist travels at c because Leg C's class does, and measures what follows. The twist wave speed c and the
    gauge-label (no mass term) character of the field are EM-RECON-012 and EM-019; mu = T / c^2 is FND-006.

## 3. THE QUESTION
  Q1  THE TWIST-SPEED CHANNEL under action (i). The discrete ring-wave at its own equilibrium (M nodes, winding 1,
      kappa_tw = 0.5, T = c = 1, beta = 1), perturbed in the twist's phase speed (probes W1, W2) or in its length mode (R0) at
      amplitude epsilon, integrated for 40 periods: is the perturbation bounded, or does it grow, and at what rate?
  Q1b THE NEUTRAL MANIFOLD under action (i). The same state perturbed in shape (S3, S4, Z2, Z3 form-bearing; S2 run and reported
      as DIAGNOSTIC ONLY, never a witness, because that channel was touched before the lock, disclosure 3): does the deformed
      loop stay near its initial shape (D_shape at or below 0.1 in units of epsilon R_d, the theorem's O(epsilon^2) with margin), or
      does D_shape exceed that and grow monotonically over the second half of the run? This is finite-amplitude shape evolution over
      the stated window only; no amplitude-scaling test is part of this commission, so no form says "second order" or "tilt".
  Q2  THE END STATE of any growing or drifting witness: does it carry the co-moving fold's marks (section 0 item 1: R_end /
      R_mean > 1.3 and mean twist phase speed beta < 0.5; E reported), or something else (described, not formed)? If nothing
      grows or drifts, Q2 is not triggered and says so (END-NOT-TRIGGERED), a determination.

## 4. PARTS LIST (registered inputs; no others enter)
- The action (i) as implemented in benchmarks/foundations/ring_wave_dynamics.py (Leg 0 part 2; credential record
  analysis/ring_wave_dynamics_leg0.json; analysis/RING_WAVE_STABILITY_leg0.md sections 7 and 10). The arc-length gauge's one
  collective sliding mode is pinned by a holonomic constraint on node 0 (the pin's torque is the J bar of every run, v5).
- The constrained-Hessian instrument benchmarks/foundations/ring_wave_stability.py (Leg 0 part 1), used for the static
  cross-check D6 only. It imports benchmarks/foundations/elec_rotator.py, elec_rope_wave.py and strand_calugareanu.py, all hashed.
- FND-006 (mu = T / c^2); EM-RECON-012 and EM-019 (wave speed c; momentum density of the twist); GRV-020 (the single circle-
  valued Goldstone with energy (kappa / 2) Phi'^2); GRV-018 (static energy). The Leg C record for the fold's energy at this
  kappa and J (8.144 at beta_p = 0, M = 48; analysis/ELEC_MECH_1_legC_instrument.md), used for the reported E ratio only.
- Units T = c = 1; kappa_tw = 0.5, so R_d = 0.707359 at M = 48 (the polygon's equilibrium; the continuum sqrt(kappa / T) =
  0.707107) and J = 2 pi kappa = pi in the continuum. The question is scale-free: ONE kappa is run, the scan is over probe content.
- labkit (benchmarks/lab/_kit/labkit.py), and the locked statistics benchmarks/lab/ring_wave_stability_4/stats.py.
- hbar, m_e, alpha and the measured g - 2 enter nowhere.

## 5. DESIGN COMMITMENTS (locked at lock)
D1. THE STATE. ring_wave_dynamics.ring(M, R_d, winding = 1, phase_speed = -1) with R_d = discrete_ring_radius(M, kappa). M = 48
    (working) and M = 96 (check). Production step h_p = 2 pi R_d / 500 (500 steps per period); 40 periods = 20,000 steps at every
    M. Newton tolerance 1e-13 (the instrument's). The production step is credentialed on large-amplitude known answers before
    any evidence run (v2p).
D2. THE PROBES (the whole set; no others), applied at t = 0 at the SCORED amplitude epsilon = 3e-3 and the CHECK amplitude
    epsilon = 1e-3 (both run; both must be valid):
      S2, S3, S4  in-plane radial displacement delta r = epsilon R_d cos(n theta), n = 2, 3, 4, then ring_wave_dynamics.equalize;
                  S2 diagnostic only;
      Z2, Z3      out-of-plane displacement delta z = epsilon R_d cos(n theta), n = 2, 3, then equalize;
      R0          uniform radial velocity epsilon (the n = 0 mode);
      W1, W2      delta Phi-dot = epsilon cos(n theta) / R_d, n = 1, 2 (a local change of the twist's phase speed);
      WU          uniform delta Phi-dot = epsilon / R_d (moves along the family direction; EXPECTED to drift, scored only as the
                  family check, never as an instability).
    Nine probes x two amplitudes x two resolutions = 36 evidence runs; two controls (ctrl_M48, ctrl_M96); the half-step runs L6:
    the nine probes and a control at M = 48, scored amplitude, at h_p / 2 (10 runs; they GATE). 48 trajectories.
D3. OBSERVABLES, sealed per run every 10th step (columns in stats.COLS): the Fourier amplitudes a_n = (2 / M)|FFT_n| for n = 1..6 of
    the radial displacement r_i - mean(r), of z_i - mean(z) and of Phi-dot_i - mean(Phi-dot) (evaluated at the step midpoint);
    E, J_z, |P|, the twist charge Q, R_mean, R_end / R_mean (R_end the largest node radius about the centroid), the mean twist
    phase speed beta(t) = -mean(Phi-dot) R_mean, the segment-length spread, the loop length, and the means (section 0 item 3).
    Node positions X are sealed at every 200th step (and X(0) as the reference frame). The sample at index m (the step interval
    from step m to m + 1) belongs to period-block min(40, m // spp + 1), spp = 500 (1000 for half-step runs).
D4. THE SHAPE OBSERVABLE. D_shape(t) = ring_wave_dynamics.shape_distance(X(t), X(0))['D_max'] / (epsilon R_d): correspondence-free
    (registration over a continuous slide, rigid rotation and translation), credentialed by K6 (bars F1, F1c, F2, F3; F1b
    informative) at M = 48 and 96 before any evidence run. D_shape(0) = 0 by construction.
D5, D6, D7: section 6.

## 6. STATISTICS AS IMPLEMENTED (stats.py is the locked text; this section is its plain statement)
S0. Block maxima A_k = max of A(t) over the samples of period-block k (k = 1..40). First window: blocks 1 and 2. Second half:
    blocks 21 to 40 (exactly 20). A half-step run has the same 40 blocks at twice the samples.
S1. Q1 probes (W1, W2, R0). A(t) = the amplitude of the probed mode (a_1 or a_2 of Phi-dot; |R_mean - R_d| for R0). Reported,
    not scored: the deviation of beta(t) from its initial value and the largest Phi-dot mode over n = 1..6.
    FLOORS: (f1) max A over blocks 1-2 must exceed 10 times the same-M control's statistic, else BELOW-FLOOR (invalid); (f2) the
    control's max A over blocks 21-40 must be below 0.1 times the probe's first-window max, else NUMERICAL-FLOOR (invalid).
    STATISTICS: rho = max_{k in 21..40} A_k / max_{k in 1..2} A_k. The GROWTH WINDOW is blocks 3 to k_sat inclusive, k_sat the first
    block among 1..20 whose A_k exceeds 0.1 of the base scale (1 / R_d for W; R_d for R0), else block 20; sigma is the least-squares slope of
    ln A_k over the window in 1 / period (UNAVAILABLE with fewer than 3 blocks). CLASSES: BOUNDED if rho <= 3; GROWS if rho >= 10
    and sigma >= 0.05; SLOW if otherwise and sigma is available; UNAVAILABLE if rho > 3 and sigma is not. A saturating
    exponential is classed by its growth window (pre-stated fixture, section 8).
    FAST-GROWTH BRANCH (stats.fast_growth; added after review; pre-stated). The block window needs k_sat >= 5, which a growth faster than
    about 0.9 per period does not give (W probes: threshold 0.1414 against a first-window amplitude of 4.2e-3, 3.5 e-folds). When the
    threshold is crossed in a block below 5 (cfg fast_k = 5), the run is classed as follows. t_cross is the first sample above the
    threshold; sigma_fast is the least-squares slope of ln (running maximum of A) against t in periods over the samples with t in
    [t_cross - 2, t_cross] and positive running maximum (so A(0) = 0 for the radial kick is excluded); rho_fast = (max over blocks
    21..40, or the last full block of a failed run's prefix) / A_ref, A_ref the maximum of A over t <= 0.05 period (the probe's own
    initial amplitude, not the first-window maximum that a saturating run has already reached). GROWS iff sigma_fast >= 0.05, rho_fast
    >= 10 and that late (or last-prefix) maximum is still at or above the threshold (the excursion did not return). Otherwise the
    standard rules apply unchanged (an excursion above the threshold that returns to the initial amplitude is BOUNDED by rho <= 3).
    Arithmetic behind the fixtures: a pure exponential from 4e-3 crosses the W threshold at t = ln(35.4) / sigma = 3.565 / sigma periods:
    1.78 at sigma 2, 2.38 at 1.5, 5.09 at 0.7. Also corrected to match this text: k_sat is searched in blocks 1..20 only (the earlier
    code let a crossing in blocks 21..40 set k_sat above 20).
    HALF-STEP GATE h1: the L6 run's class (against the half-step control) must equal the M = 48 scored run's class, else the
    probe is HALF-BLOCKED at both M and cannot witness.
    FAILED RUNS. A Newton failure, or a v5 breach at a sample, ends the run at step N_f; the sealed series before N_f is the VALID
    PREFIX. The prefix bears GROWS by either of two routes. (a) Slow route: it holds at least 4 full blocks (n_full = N_f // spp),
    rho with block n_full in place of blocks 21-40 is >= 10, and sigma over blocks 3..min(k_sat, n_full) is available and >= 0.05
    (so in practice n_full >= 5). (b) Fast route (the fast-growth branch above): the threshold is crossed inside the prefix in a block
    below 5, sigma_fast >= 0.05, rho_fast >= 10 against the last full prefix block, and that block is at or above the threshold; this
    needs only n_full >= 2 (a run at sigma 1.5 per period failing at period 4 or period 3 is a prefix witness; failing at period 2,
    before the crossing at 2.38, it is a failure record). Such a run is a RING-UNSTABLE witness with the failure on its face; its end
    state for Q2 is the last 2 full periods of the prefix. Any other failed run is a failure record: class UNAVAILABLE, invalid. A run
    with under 2 full blocks is a failure record.
    THE BREACH SAMPLE IS RETAINED. The driver no longer discards a v5-breaching sample: it is sealed apart (seal breach/<run>, one row)
    from the valid prefix (seal ser/<run>, which excludes it); fail_step in the run record is the breach step and fail_reason carries the
    kind. The verdict (verdict.verify_runs, before any statistic) replays the v5 check from the retained raw rows (stats.v5_scan): a
    complete run must scan clean; a failed run must show its breach row at exactly fail_step with the recorded kind, a prefix that scans
    clean and excludes it, and no kept sample at or after fail_step (a Newton failure: no breach row). Any mismatch halts and the open
    form renders.
    v5 (every run, both amplitudes), checked at every sample: (max - min) / |E_0| < 1e-4; Q range < 1e-8; J_z range <= 2e-6
    (absolute; 20 times K5's two-period 1e-7 bar for 40 periods, the pin's torque accumulating linearly); segment-length spread
    < 1e-10; all finite. A breach is a failure record kept, never rerun.
    VALIDITY: a Q1 probe is valid at a resolution only if BOTH amplitudes are valid. An invalid check run blocks every Q1 form at
    that resolution EXCEPT a scored-amplitude RING-UNSTABLE witness that is itself valid and not half-blocked.
S2. Q1b probes (S3, S4, Z2, Z3 form-bearing; S2 diagnostic). Per run, D_shape in units of the run's own epsilon R_d. HOLDS if
    max_t D_shape <= 0.1; DRIFTS if max > 0.1 and the least-squares slope of the second-half block maxima exceeds 3 times its
    standard error (and is positive); WOBBLES otherwise. A failed or incomplete shape run is UNAVAILABLE (no prefix witness rule
    for shapes). A shape probe bears a class at a resolution only if BOTH its amplitudes are valid.
    GATES. (g1) per M, the control's own D_shape over the whole run, in units of 3e-3 R_d, is <= 0.02; and for every valid DRIFTS
    run at that M the control's second-half block-maxima slope (in that run's units) is below 0.1 of the run's slope; else
    Q1B-NO-CALL. (g2) the L6 run must agree with the M = 48 scored run on the class and, when DRIFTS, on the slope (same sign,
    within 30 percent), else the probe is HALF-BLOCKED. (g3) the resolution agreement: a witness must DRIFT at the SCORED
    amplitude at BOTH M (the same probe, the same amplitude: a matched resolution check); for the HOLDS and WOBBLES forms the scored class
    of every probe agrees at both M. WITNESSES ARE RESTRICTED TO THE SCORED AMPLITUDE after review: only the scored amplitude has the
    scheduled half-step comparison g2, so a DRIFTS at the check amplitude (validity-bearing, reported) never witnesses and, if it occurs
    without a scored-amplitude witness, the question renders Q1B-NO-CALL with the reason on the face. The Q2 qualifying runs of both
    Q1 and Q1b witnesses are likewise the scored-amplitude runs only. Known limit, kept: no half-step run exists at M = 96, so the
    witness's resolution support is g2 at M = 48 plus the M = 48 / 96 agreement at one amplitude, v5, and the unperturbed-control gates. (g4) K6 F1b's reading at that M, divided by
    3e-3 R_d, is below 0.02, else Q1B-NO-CALL.
    WU (family check, reported only): beta_J = mean J_z(WU) / J_z(0)(control); R_pred = discrete_ring_radius(M, kappa, 1, beta_J);
    FAMILY-DRIFT-AS-EXPECTED iff |mean R_mean(second half) / R_pred - 1| <= 1e-2 and |mean beta(second half) / mean beta(control,
    second half) / beta_J - 1| <= 2.5e-3; else an anomaly of the instrument on the face; it blocks nothing. (The expected
    equilibrium shift is d ln R = -epsilon / 2 = 1.5e-3 at the scored amplitude, so the 1e-2 bar on R is loose: it is the author's
    bar, kept; the beta bar is the informative one.)
S3. D6 static cross-check: ring_wave_stability.rope_spectrum at beta = 1, M = 48, kappa_C = 0, with the stationarity measure S
    required below 1e-2 (the fold reads 8.7e-4) and the count of negative constrained modes reported. A disagreement with the
    dynamics is recorded as a finding, not resolved by choosing; the unit never halts on it.
S4. Q2 marks, over the last 2 periods (blocks 39-40; for a prefix witness the last 2 full blocks of the prefix): mark R = mean R_end /
    R_mean > 1.3; mark B = mean beta < 0.5; E_mean reported with its ratio to 8.144. Unavailable if no samples or not finite.
D7. RESOLUTION. A form that needs agreement across M (RING-STABLE, RING-SLOW, NEUTRAL-HOLDS, NEUTRAL-WOBBLES) is rendered only if
    M = 48 and M = 96 agree on the scored class of every probe of that question; otherwise that question's NO-CALL, classes on
    the face. RING-UNSTABLE and NEUTRAL-DRIFTS are existential: a witness probe must show the class at both M by its own runs.

## 7. HARNESS (binding)
Units in order (benchmarks/lab/ring_wave_stability_4/driver.py, 80 units; each run also seals its retained breach row, empty when none): credential, setup, stat_credential, static, ctrl_M48,
ctrl_M96, the 36 evidence runs (M = 48 scored, M = 48 check, M = 96 scored, M = 96 check), ctrl_M48_h, the 9 half-step runs, then
dshape_<run> for the 28 shape and control runs. Each trajectory seals its series, node frames and frame indices as it completes; no
statistic is computed during a run. The driver imports ring_wave_dynamics.py and ring_wave_stability.py and nothing else from
benchmarks/ beyond labkit and stats.py; the manifest binds all nine files. The verdict recomputes every statistic from the seals
and renders one FORM per question once.
LAB_SMOKE=1 (about 15 seconds): the credential unit at M = 16 (K1, K2, K5 on the beta = 0.5 member, K6; bars recorded and NOT
enforced at M = 16), setup, the stat_credential fixtures in full (closed forms; 54 fixtures), the static unit at M = 8 on the
beta = 0.5 member, one control and one S3 probe on the beta = 0.5 member at M = 16 for 2 periods (100 steps per period), their
D_shape unit; the other units record "skipped". It writes analysis/ring_wave_stability_4_smoke.pkl only, prints no rho, sigma or
D_shape, and reads nothing under data/. The runner's environment needs JAX and SciPy (the lab venv); memory under 1 GB.

## 8. VALIDATION BARS (halt-grade; the credential and stat_credential units; every run is recorded before a statistic is read)
v1. K1: twist-wave period within 2e-3 of the chain's discrete dispersion; E drift < 1e-6.
v2. K2: pulsating circle |R - R0 cos(t / R0)| < 1e-3 to R0 / 2; |E0 - 2 pi R0| / (2 pi R0) < 1e-3; E drift < 1e-4.
v2p. THE PRODUCTION STEP: K2 (with h = 2 pi R0 / 500) and K3 (with h = h_p) re-run at M = 48 under the K2 and K3 bars; halt if either
    fails (the executor's record, analysis/RING_WAVE_STABILITY_leg0.md section 10: K2 worst |R - exact| 2.0e-5, E drift 3e-12; K3
    drifts at 1e-13).
v3. K3 at M = 48, instrument step: E, J, Q drift < 1e-8; |P| < 1e-8; R_spread < 1e-6; R_mean drift < 1e-4; E0 and J0 within 1e-3 of
    the closed forms.
v4. K4: P, J, Q conserved to 1e-9 on the generic datum without the gauge pin; energy order > 1.8.
v4b. K5 (beta = 0.5 member): worst node displacement < 0.1 epsilon R; J drift < 1e-7.
v6. K6 at M = 48 and 96: F1 < 1e-10 R, F1c < 1e-8 R, F2 < 1e-10 R, F3 within [0.5, 1.5] of its exact value; F1b informative (its reading is
    gate g4's number); F4 informative.
STAT-CREDENTIAL (halt-grade): the statistics and deciders reproduce the pre-stated answer on 54 closed-form fixtures: a pure exponential
(GROWS); a tanh-saturated exponential at sigma 0.3 (GROWS); a bounded oscillation (BOUNDED); a slow exponential (SLOW); a late-noise control
against a quiet probe (f2 blocks: NUMERICAL-FLOOR); a probe at the floor (f1: BELOW-FLOOR); step-dependent growth (h1 half-blocks); a growing
run failing at period 12 (prefix witness GROWS) and at period 3 (failure record); a full series whose post-breach tail gives different end
marks than its prefix (the prefix is used); shape HOLDS, DRIFTS, WOBBLES; equal maxima with incompatible drift (g2 half-blocks) and an agreeing
pair; a quiet-then-drifting control (g1 blocks); a failed check run beside a valid scored run for a Q1 probe (RING-UNSTABLE witness kept,
every other form blocked) and for a shape probe (all classes blocked); DRIFTS at the scored amplitude at both M (NEUTRAL-DRIFTS, qualifying set
exactly the two scored runs, the check-amplitude DRIFTS not qualifying); DRIFTS at the check amplitude at one M and at the scored amplitude at the
other, at the scored amplitude at one M only, and at the check amplitude at both M with the scored amplitude HOLDS (each: no witness, Q1B-NO-CALL);
the fast-growth fixtures (exponential at sigma 2 per period: GROWS; tanh saturation at sigma 2: GROWS; an exponential from A(0) = 0 with saturation,
the radial-kick shape: GROWS; sigma 0.7 crossing at 5.09 periods: GROWS; a transient excursion that returns: BOUNDED; a run at sigma 1.5 failing at
period 4 or 3 after the crossing at 2.38: prefix GROWS; failing at period 2, before the crossing: failure record), their answers derived by
arithmetic (crossing time ln(0.1414 / 4e-3) / sigma = 3.565 / sigma periods), not from instrument runs; the retained-breach fixtures (a closed-form
series breaching v5 by E drift at sample 61: the replay scan agrees with the driver's incremental check; the breach is verified from the retained row;
a wrong breach step, a removed breach row, a prefix containing the breach, and a wrong recorded kind are each rejected; a Newton failure with a clean
prefix is verified); one witness beside a half-blocked GROWS probe with different end marks (the
half-blocked probe does not qualify); two qualifying runs with one mark unavailable (Q2-NO-CALL); a known failed mark (END-OTHER); the g4 floor.
The fixtures call the same functions the verdict calls, on series generated from closed forms, never from the instrument.

## 9. FORMS (exhaustive; exactly one per question on every terminal verdict; every form is "under action (i)")
Q1 (exactly one), evaluated in this order:
  RING-UNSTABLE        W1, W2 or R0 GROWS (valid, full run or valid prefix) at the scored amplitude at BOTH resolutions, not half-blocked;
                       the mode and its sigma are named; a growing channel under action (i); Q2 says whether the end state carries the fold's
                       marks; the class's standing as a free object is then the author's reading, and no follow-up may search for a reason
                       the twist should travel (no-rescue).
  RING-STABLE          W1, W2, R0 all BOUNDED at both resolutions and both amplitudes, all valid, none half-blocked: the twist-speed channel is
                       closed at this order. (WU's result is on the face.)
  RING-SLOW            all valid at both amplitudes and resolutions, none half-blocked, classes agree across M, no probe GROWS at either
                       amplitude, at least one SLOW at the scored amplitude: rho and sigma on the face; the next step named as a longer run at
                       the same locked settings.
  Q1-NO-CALL           any other case, with the reason on the face: an invalid run without a valid witness, a half-blocked probe, a class
                       disagreement across M, or scored and check amplitudes in disagreement.
Q1b (exactly one), evaluated in this order:
  NEUTRAL-DRIFTS       gates g1 and g4 met at both M and at least one of S3, S4, Z2, Z3 (both amplitudes valid at both M, g2 met at M = 48 so not half-blocked) DRIFTS
                       at the SCORED amplitude at BOTH resolutions (the same probe at the same amplitude at both M, a matched resolution check; a DRIFTS at the check amplitude never witnesses). It establishes only that, at the scored amplitude, the finite-amplitude shape distance from the initial shape exceeds 0.1 epsilon R_d and grows over the second half of the run at the stated 3-sigma criterion, at both M, with the M = 48 half-step agreeing. It does NOT establish second-order scaling or a tilt of the valley (no amplitude-scaling test is part of this commission); the former wording is withdrawn:
                       no valley-tilt reading is formed. Q2 names the end state.
  NEUTRAL-HOLDS        every form-bearing probe HOLDS (scored) at both resolutions, gates met, none half-blocked, no DRIFTS anywhere.
  NEUTRAL-WOBBLES      no DRIFTS at any resolution or amplitude, at least one WOBBLES (scored), all valid, classes agree across M, gates met.
  Q1B-NO-CALL          a gate failed, an invalid run, D7/g3 disagreement, a half-blocked probe, or a DRIFTS that does not satisfy the witness predicate;
                       the reason on the face.
Q2 (exactly one):
  END-FOLD             triggered by RING-UNSTABLE or NEUTRAL-DRIFTS; the witnesses are exactly the probes the Q1 or Q1b decider named (never
                       re-derived); the qualifying runs are every valid GROWS (Q1 witnesses) or DRIFTS (Q1b witnesses) run of a witness at its own
                       resolution, at the SCORED amplitude only; EVERY qualifying run's two scored marks (R, B) are available and met.
  END-OTHER            triggered; at least one qualifying run has a KNOWN failed mark; the marks and E on the face.
  END-NOT-TRIGGERED    neither RING-UNSTABLE nor NEUTRAL-DRIFTS was rendered; a determination; it never asserts that no witness existed when only
                       one of the two was rendered.
  Q2-NO-CALL           triggered, no known failed mark, at least one qualifying run's mark UNAVAILABLE (or no qualifying run found).
HARNESS-OPEN (the open form, all three questions): the harness could not evaluate (halt, absent or broken seal, configuration or manifest
change, any exception in the decision rule).

WHAT EACH FORM WOULD ESTABLISH, AND WHAT IT WOULD NOT. Every reading is under action (i) and claims only what the runs measure: selected finite-
amplitude probes (3e-3 and 1e-3 in the units of D2) integrated for 40 periods at one kappa, M = 48 and 96, with no Coulomb coupling. No
dynamical spectrum is computed, so NO form here passes or fails the electron ledger's acceptance test A2 (linear stability), which stays
unrun. RING-STABLE with NEUTRAL-HOLDS: the locked probes neither grow nor drift over 40 periods; the candidate is, on this evidence, a flat
continuum of equal-energy shapes rather than one state (a property the class must then explain or be charged for); A2 is the next test, not
this one; it says nothing about the scale wall (Leg C section 6, HBAR-003), the O(alpha) anomaly, or probes outside D2. RING-UNSTABLE: a
locked observable grows under action (i) at the stated rate; Q2's marks identify a neighbourhood of the fold (shape and speed), not the fold
uniquely, not an end-state g, not an end energy. NEUTRAL-DRIFTS with RING-STABLE: finite-amplitude shape evolution at the measured scored-amplitude slope over this window; not a second-order drift (no scaling test), not a tilt of the valley. A NO-CALL or
HARNESS-OPEN form is a clean open result: nothing about the class follows. The theorist owes the form of the twist's action before any form is
more than conditional (P1). Correlation is not mechanism; a numerical instability of the discretization that survives h, h / 2 and M, 2M
checks is still a statement about this discretization of action (i).

## 10. NO-RESCUE RULE
No probe added, removed or re-amplituded after the lock; no threshold moved; no run discarded for its outcome; a Newton failure or v5 breach is a
failure record on its run and stays one. If the result is RING-UNSTABLE, no follow-up may search for a reason the twist should travel; that would
be a grant, and grants are the author's. A verdict runs once, from the sealed checkpoint.

## 11. BUDGET
cpu_hours 8, usd 0, mem_gb 1. Estimate (the author's measured 5 ms per step at M = 48; M = 96 about 4 times): 39 M = 48 run-equivalents of 20,000 steps
(about 65 minutes); 19 runs at M = 96 (about 2.5 hours); D_shape from 100 frames per shape run (about 30 minutes in all); credential and
stat_credential about 15 minutes; D6 static at M = 48 about 20 to 60 minutes (the finite-difference Hessian scales as M^4). The evidence
checkpoint holds roughly 40 MB of sealed arrays. Results go to analysis/RING_WAVE_STABILITY_4_results.md. No beacon draw: the commission has no
hold-out set.

## 12. DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
1. The executor built the instruments and ran only known-answer cases: the Michell ring, the pulsating circle, the frozen-ring twist wave, generic
   data, the co-moving fold, the UNPERTURBED ring-wave for two periods (K3), the shape theorem on the beta = 0.5 member (K5) and the K6 fixtures.
2. THE DRAFTING WORKER'S RUNS (this session): (a) the smoke run described in section 7, on the beta = 0.5 member at M = 16, plus synthetic
   fixtures; (b) one code-path check of the evidence-mode credential unit at M = 16 (K1, K2, K3 and K3 at the production step on the UNPERTURBED
   beta = 1 ring-wave at M = 16, K4, K5, K6 at M = 16 and 24; no probe; bars not expected to pass at that resolution, and the worker read only
   which bars passed, the code path completing); (c) a synthetic-checkpoint check of the verdict's evidence branch on closed-form series. No probe
   was integrated on the beta = 1 state at any M. No number from any of these runs enters the charter. The scratch scripts are in
   analysis/lab/drafts/RING-WAVE-STABILITY-4/ (reset_smoke.py, credential_path_check.py, fixture_check.py) and are not part of the commission.
3. The one run that touched the beta = 1 evidence state before this charter, disclosed in -2 and -3 and judged in both: the n = 2 shape probe at
   epsilon = 1e-2, M = 16, aborted by a Newton failure at 0.3 of a period BEFORE the gauge pin existed. S2 is therefore out of the form-bearing set
   and reported as diagnostic only. The remaining schedule (W1, W2, R0, WU, S3, S4, Z2, Z3 on the beta = 1 state) is uninspected.
4. Bar provenance. Every dynamics bar is the author's draft bar or stated arithmetic (v5's J bar: 20 times K5's). K6 F1b bears no bar (its first bar
   had been set after a reading); F1c's bar of 1e-8 R was written before it ran. Bars added by this charter and not in the draft: the E0 closed-form
   checks inside v2 and v3 (the instrument's own credential bars), the Q drift bar in v4 (the draft stated it), and every predicate of section 6
   that the draft left open; none was chosen after seeing evidence-cell data (none exists).
5. The workers' -2 and -3 kits were never pushed; the cures recorded in their reviews are written into this charter from the review transcripts.
6. Expectations, disclosed so they cannot be mistaken for results: shape probes will hold at first order (the theorem); the executor has no
   expectation about the twist-speed channel or the second-order drift. The Director's expectation (memo, 2026-10-25): RING-STABLE, low confidence.
7. Known weakness kept on the face: at M = 48 the block maxima of D_shape rest on 2 or 3 frames per period-block (frames every 200 steps, 500 steps
   per period), so the second-half slope statistic is noisy; the 3-sigma criterion uses the residual scatter and a noisy series is classed WOBBLES,
   never DRIFTS. WU's R bar is loose (section 6, S2).
8. REVIEW OBJECTIONS ANSWERED IN THIS REDRAFT (objection: what changed), none chosen after any evidence-cell data (none exists):
   - skeptical, Q1 cannot classify a fast instability (block fit needs k_sat >= 5): stats.fast_growth and the fast-growth branch of
     stats.q1_class, stated in section 6 S1; the prefix rule has a fast route needing only n_full >= 2 with the crossing inside the prefix.
     Halt-grade stat_credential fixtures with answers derived from arithmetic: exponential at sigma 2 per period (GROWS), tanh saturation at
     sigma 2 (GROWS), a run at sigma 1.5 failing at period 4 (prefix GROWS), and the companions listed in section 8.
   - skeptical, exhaustive_forms (same ceiling, files the likeliest strong instability as open): same change; no fast growth now renders Q1-NO-CALL
     through the window arithmetic. Q1-NO-CALL remains for invalid runs, half-blocking and D7 disagreement.
   - external, retain the v5-breaching sample (driver rows.pop()): driver.integrate keeps the popped row and the run unit seals it as breach/<run>,
     apart from ser/<run>; the breach step and kind are in the run record; the prefix excludes it; stats.v5_scan and stats.verify_failure replay the
     check from the retained raw rows and verdict.verify_runs halts (HARNESS-OPEN) on any mismatch; fixtures in section 8.
   - external, half-step comparison for every amplitude eligible to witness NEUTRAL-DRIFTS: witnesses restricted to the scored amplitude (the one with
     the scheduled h_p / 2 run, g2), and the same probe at the same amplitude must DRIFT at both M (stats.decide_q1b, the form text in section 9, the
     g3 clause in section 6 S2, and fixtures). Known limit kept: no half-step run at M = 96 (section 6 S2).
   - external, NEUTRAL-DRIFTS must not claim second order or a tilting valley: those words are removed from the form, the readings and the
     decider's text; the form establishes finite-amplitude shape evolution at the scored amplitude over 40 periods only.
   - external, narrow the statement that the answer decides candidacy as a free electron: section 1 already says the answers do not decide candidacy
     (A2 and the scale wall are not run); the form readings repeat that A2 stays unrun.
   - external, exhaustive_forms (interpretation unestablished) and floor_test (check-amplitude witness never half-step tested; different amplitudes
     at the two M not a matched check): both resolved by the scored-amplitude, same-amplitude-at-both-M witness rule above.
   - external, verdict_sealed (breach not reconstructible from sealed outputs): resolved by the retained breach row above.

```lab
commission: RING-WAVE-STABILITY-4
target: "Strength of magnets row, gap 4 (the electron model): whether locked finite-amplitude shape and twist-speed probes of the travelling-twist ring, the one registered mechanism class with g = 2 by mechanics, grow or drift over 40 periods in the full nonlinear dynamics of action (i) (a disclosed premise), and whether a growing run's end state carries the co-moving fold's shape and speed marks; interior work locking under the author's dated section 5 exception (docs/NORTH_STAR.md, 28 October 2026); moves no scorecard row and none of the five numbers"
driver: benchmarks/lab/ring_wave_stability_4/driver.py
verdict_script: benchmarks/lab/ring_wave_stability_4/verdict.py
instrument:
  - benchmarks/foundations/ring_wave_dynamics.py
  - benchmarks/foundations/ring_wave_stability.py
  - benchmarks/foundations/elec_rope_wave.py
  - benchmarks/foundations/elec_rotator.py
  - benchmarks/foundations/strand_calugareanu.py
  - benchmarks/lab/ring_wave_stability_4/stats.py
  - benchmarks/lab/_kit/labkit.py
forms: [RING-STABLE, RING-UNSTABLE, RING-SLOW, Q1-NO-CALL, NEUTRAL-HOLDS, NEUTRAL-DRIFTS, NEUTRAL-WOBBLES, Q1B-NO-CALL, END-FOLD, END-OTHER, END-NOT-TRIGGERED, Q2-NO-CALL, HARNESS-OPEN]
state: [analysis/ring_wave_stability_4_ckpt.pkl]
budget: {cpu_hours: 8, usd: 0}
mem_gb: 1
```
