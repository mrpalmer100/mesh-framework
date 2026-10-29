# COMMISSION RING-WAVE-STABILITY-4 -- IS THE g = 2 STATE A STABLE OBJECT? THE TRAVELLING-TWIST RING UNDER PERTURBATION
# (fourth name, 2026-10-28. -2 and -3 were withdrawn in review without a verdict. -3's round 3 was PASSED by the
# skeptical reviewer and failed by the external reviewer on NORTH_STAR section 5 alone (a second consecutive interior
# session) and on the breadth of the readings; both are settled here: the author's dated exception is on the page
# (docs/NORTH_STAR.md section 5, 28 October 2026) and the readings claim only what the runs measure. Every cure the
# worker made in -3's rounds 1 and 2 (its kit was not pushed) is written into this draft: S2 out of the form-bearing
# set; a saturating instability classes GROWS; a growing run that fails is a witness from its valid prefix; the
# production step credentialed on K2; a late-time floor for Q1; the half-step runs gate Q1 and Q1b's drift statistic;
# both amplitudes validity-bearing for every question; Q2's witnesses by Q1's own predicate with end marks from the
# prefix and a form for mixed availability; K6 F1b informative. Nothing else changed.)
# (CHARTER, the author's DRAFT for the lab's lock; a measurement by time integration with the outcome unknown to
# everyone; harness on benchmarks/lab/_kit/labkit.py; the executor's instruments credentialed on known answers only)

## WHERE IT STANDS (the honest sentence, before the question)
One registered mechanism class reaches the electron's g = 2 by mechanics with nothing tuned: a closed rope whose
one unit of twist travels along it at c, the static ring at R^2 = kappa / T where the wave's momentum flux holds
the ring against its tension (analysis/ELEC_MECH_1_legC_instrument.md; g = E / E_wave = 2 by the scale virial for
any static shape). Its first price, written on its face since Leg C, is stability: at equal kappa and J the ring-wave
sits 9 percent ABOVE the co-moving fold (the twist riding with the material, g about 0.9), and no registered
reason makes the twist travel rather than ride. Acceptance test A2 of the electron ledger (linear stability) has
never been run on any candidate (E2 record, F5). Two things could protect the ring: the conserved twist charge and
angular momentum, and the fact that the static ring is one member of a continuous family of stationary solutions
(R^2 = kappa (1 + beta^2) / 2T at twist phase speed beta, J = 2 pi kappa beta; Leg 0 part 2, section 7 ii). And one
thing is KNOWN before the lock, from Leg C's shape theorem and confirmed dynamically on the beta = 0.5 member
(Leg 0 part 2, K5): a static closed loop of the right length with its twist travelling is stationary for EVERY
shape, because the wave's momentum flux balances the tension locally (kappa Phi-dot Phi' = T at every point fixes
only L). So shape perturbations at fixed length are NEUTRAL at first order: a deformed ring does not move, to
O(epsilon^2) (K5: 1.4 epsilon^2 R over two periods). The stability question is therefore not "does the ring
spring back" (it does not; nothing pushes it) but two sharper ones: does a perturbation of the TWIST'S PHASE SPEED,
the channel from travelling to co-moving twist, grow or oscillate; and does the neutral shape manifold drift at
second order toward the fold or stay put. Nobody knows either answer. That is the question, and the answer decides
whether the class is a candidate free electron (its remaining price then being scale) or an excited state whose
g = 2 is a property of something that does not persist.

## THE PREMISE (disclosed; not a question; nothing here bears a form)
P1. THE ACTION. Two actions reduce to Leg C's static functional at small twist and differ at O(1) exactly at the
    ring-wave (kappa Phi'^2 / T = 1): (i) Nambu-Goto plus the twist as a massless scalar on the string's INDUCED
    metric, S = -Int sqrt(-h) [T + (kappa / 2) h^ab d_a Phi d_b Phi]; (ii) Nambu-Goto in five dimensions with the
    twist as a fifth target coordinate, S = -T Int sqrt(-det(dX . dX + (kappa / T) dPhi dPhi)). The registry does
    not fix the form of the twist's action on a moving rope (GRV-018, GRV-020, EM-RECON-012, EM-019, EM-008 state the
    static energy, the wave speed c and the momentum density; none states the covariant action). The instrument
    implements (i). EVERY dynamics decision below is conditional on action (i); the conditional travels on the face
    of every rendered form as the words "under action (i)". Whether the registry owes (i), (ii) or another form is
    the theorist's reading, not this commission's; RING-WAVE-STABILITY-2's Q0 tried to make it a form-bearing
    question by phrase classification of the five claim texts and the external reviewer was right that a rule
    written after its texts were read is not a blind determination. The wording inventory the worker built may be
    reproduced in the results file as DESCRIPTIVE BACKGROUND with no evidential weight and no form.

## THE QUESTION
  Q1  THE TWIST-SPEED CHANNEL under action (i). The discrete ring-wave at its own equilibrium (M nodes, winding 1,
      kappa_tw = 0.5, T = c = 1, beta = 1), perturbed in the twist's phase speed (probes W1, W2 of D2) or in its
      length mode (R0) at amplitude epsilon, integrated for N_per periods: is the perturbation bounded, or does it
      grow, and at what rate?
  Q1b THE NEUTRAL MANIFOLD under action (i). The same state perturbed in shape (S3, S4, Z2, Z3 form-bearing; S2 run
      and reported as DIAGNOSTIC ONLY, never a witness, because that channel was touched before the lock, disclosure
      2): does the deformed loop stay where the theorem puts it (shape change O(epsilon^2) and bounded), or drift at
      second order, and toward what?
  Q2  THE END STATE of any growing or drifting probe: does the shape at the end of the run approach the co-moving
      fold (E within 5 percent of the fold's 8.144 at this kappa and J, R_end / R_mean > 1.3, the twist's phase
      speed fallen below 0.5), or something else (described, not formed)? If nothing grows or drifts, Q2 is not
      triggered and says so (END-NOT-TRIGGERED), which is a determination, not an open verdict.

## WHAT IS GIVEN (registered inputs; no others enter)
- The action (i) as implemented in benchmarks/foundations/ring_wave_dynamics.py (Leg 0 part 2, credentialed on
  known answers K1 to K6 at the credential step and K2, K3 at the production step: the twist wave's dispersion to 5e-6, the Nambu-Goto pulsating circle to 2e-7, the
  unperturbed ring-wave's E, J, P and winding to 1e-11 over two periods, discrete Noether on generic data to 1e-13,
  the shape theorem on the beta = 0.5 member to O(epsilon^2), and the shape observable's known answers (K6, below);
  analysis/RING_WAVE_STABILITY_leg0.md section 7 and analysis/ring_wave_dynamics_leg0.json). The arc-length
  gauge's one collective sliding mode is pinned by a holonomic constraint on node 0 (the pin's torque is the J bar
  of every run, v5).
- The constrained-Hessian instrument benchmarks/foundations/ring_wave_stability.py (Leg 0 part 1: the Michell
  threshold sqrt 3 B / C from the spectrum to 1.6e-4; the stationarity measure S with its floor 9e-5; the fold a
  node-space minimum), used here for the static cross-check D6 only.
- FND-006 (mu = T / c^2); the Leg C record for the fold's energy at this kappa and J (8.144 at beta_p = 0, M = 48,
  elec_rope_wave form; 8.100 in the E2b Routhian form).
- Units: T = c = 1; kappa_tw = 0.5, so R_d = 0.707359 at M = 48 (the polygon's equilibrium; the continuum
  sqrt(kappa / T) = 0.707107) and J = 2 pi kappa = pi in the continuum. In these units kappa only sets R; the
  question is scale-free, so ONE kappa is run and the scan is over the probe content (D2), not over kappa. Because
  the question is scale-free, NO run at another kappa is a disjoint cell: nothing measured at kappa = 0.3 enters
  any bar below (round-2 finding, cured by sourcing every bar from stated arithmetic or the K-series bars).

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
- No linearization is assumed: the probe is integrated in the full nonlinear dynamics. The constrained Hessian
  (D6) is a cross-check at the static level, not the verdict.
- Forbidden: any change to the action, the gauge, the discretization or the integrator after the lock; any
  perturbation outside the locked probe set D2; reading growth from the unperturbed K3 run (two periods; it
  cannot show one); reseeding, reweighting or truncating a trajectory after seeing it.
- hbar, m_e, alpha and the measured g - 2 enter nowhere: this commission is about the mechanics of one class.

## SCOPE (hard boundary)
Stability of the beta = 1 static ring under action (i), at one kappa, for the locked probes, over N_per periods, at
two resolutions. Not: the ring's O(alpha) anomaly (RING-WAVE-ANOMALY, a reading on record), the scale wall (Leg C
section 6, HBAR-003, N1), the rope's kappa (ELEC-KAPPA-1, withdrawn), the fold's own stability (it is the
reference minimum; Leg 0 part 1 K3), or the form of the twist's action (P1).

## DESIGN COMMITMENTS (locked at lock)
D1. THE STATE. The discrete ring-wave is built by ring_wave_dynamics.ring(M, R_d, winding = 1, phase_speed = -1)
    with R_d = discrete_ring_radius(M, kappa) (the polygon's own equilibrium, found by root find; the K3 start).
    Resolutions M = 48 (working) and M = 96 (check). The PRODUCTION STEP h_p = 2 pi R_d / 500 (500 steps per
    period, 8.9e-3 time units, about ten times the K-series credential step); N_per = 40 periods of 2 pi R_d
    (178 time units; 20,000 steps at every M). Newton tolerance 1e-13 as in the credential. The production step
    is credentialed on a large-amplitude known answer before any evidence run (v2p).
D2. THE PROBES (the whole set; no others), each applied to the K3 state at t = 0, at the SCORED amplitude
    epsilon = 3e-3 and the CHECK amplitude epsilon = 1e-3 (both run, both validated under v5 and the floors; the
    check amplitude is the linear-regime check and its validity is required, D5):
      S2, S3, S4   shape: in-plane radial displacement delta r = epsilon R_d cos(n theta), n = 2, 3, 4, then
                   re-equalized by ring_wave_dynamics.equalize (the constraint must hold at t = 0); S2 is run and
                   reported, diagnostic only (CONFIG shape_bearing = ('S3', 'S4', 'Z2', 'Z3'));
      Z2, Z3       shape: out-of-plane displacement delta z = epsilon R_d cos(n theta), n = 2, 3;
      R0           the radial kick: uniform radial velocity epsilon (the n = 0 mode at fixed J, since a radial
                   velocity carries no J_z);
      W1, W2       twist speed: delta Phi-dot = epsilon cos(n theta) / R_d, n = 1, 2 (a local change of the twist's
                   phase speed; the probe that opens the travelling-to-co-moving channel);
      WU           the uniform twist-speed change delta Phi-dot = epsilon / R_d (moves along the family direction
                   of section 7 ii: J changes by 2 pi kappa epsilon; this probe is EXPECTED to drift, not grow,
                   and is scored separately under D5 as the family check, not as an instability).
    Nine probes times two amplitudes times two resolutions: 36 evidence runs; plus the two unperturbed controls
    ctrl_M48 and ctrl_M96 (40 periods each; the control gates of D5); plus the half-step runs L6: the nine probes
    and the control at M = 48, scored amplitude, at h_p / 2 (10 runs; they GATE, D5). 48 trajectories in all.
D3. THE OBSERVABLES, sealed per run at every 10th step: the Fourier amplitudes a_n(t) of the radial displacement
    r_i - mean(r), of z_i, and of Phi-dot_i - mean(Phi-dot), for n = 0..6; E, J, P, the twist charge Q, R_mean,
    R_end / R_mean, the mean twist phase speed beta(t) = -mean(Phi-dot) R_mean; the Newton iteration count; and,
    at every 200th step, the node positions X(t) (for D_shape, computed in the verdict unit from the seals, never
    during the run).
D4. THE SHAPE OBSERVABLE. D_shape(t) = ring_wave_dynamics.shape_distance(X(t), X(0))['D_max'] / (epsilon R_d): the
    worst node residual between the loop at t and the reference shape through the deformed initial polygon,
    minimized over a continuous slide of the nodes along the shape, a rigid rotation and a translation (the
    reference polygon interpolated trigonometrically in its node index; registration by uniform shift and Kabsch,
    then per-node projection onto the curve and a joint least squares over the rigid motion and the curve
    parameters). It is correspondence-free: the arc-length gauge's sliding mode, which moves every node ALONG an
    unchanged shape by a fractional spacing, reads zero (K6 F1, F1b, F1c), where an indexed-node Procrustes reads
    up to half a spacing (0.068 = 0.096 R at M = 48, 32 epsilon R_d at the scored amplitude; K6 F4, the round-3 defect).
    Credentialed before any evidence run under v6.
D5. THE STATISTICS, per probe and amplitude, computed once from the seals.
    WINDOWS. The run is divided into 40 period-blocks. The first window is blocks 1 and 2; the second half is
    blocks 21 to 40 (exactly 20 blocks, never 19; a half-step run has the same 40 period-blocks at twice the
    samples). Block maxima A_k = max of A(t) over block k.
    Q1 PROBES (W1, W2, R0): A(t) = the amplitude of the probed mode (the a_n of Phi-dot for W; |R_mean - R_d| for
    R0). Beside it, reported and not scored: the deviation of beta(t) from its initial value and the largest
    non-probed Phi-dot mode (the uniform channel and leakage; named here so their absence from the score is on the
    face). FLOORS: (f1) first-window floor: max A over blocks 1 to 2 must exceed 10 times the control's same
    statistic over the same blocks at the same M, else BELOW-FLOOR (invalid); (f2) late-time floor: the control's
    max A over blocks 21 to 40 must be below 0.1 times the probe's first-window max, else the probe's class is
    NUMERICAL-FLOOR (invalid; late numerical growth cannot pass as physics). STATISTICS: rho = max_{k in 21..40} A_k
    / max_{k in 1..2} A_k; the GROWTH WINDOW is blocks 3 to k_sat, where k_sat is the first block in which A_k
    exceeds 0.1 of the base twist rate (|Phi-dot| = 1 / R_d for W; 0.1 R_d for R0), or block 20 if none does; sigma
    is the least-squares slope of ln A_k over the growth window (at least 3 blocks, else sigma is UNAVAILABLE), in
    units of 1 / period. This window is pre-stated so that a fast instability that saturates (sigma 0.3 per period
    reaches O(1) by period 19 and plateaus) is classed by its growth, not by its plateau (stat_credential fixture: a
    tanh-saturated exponential, pre-stated class GROWS). CLASSES at a resolution: GROWS if rho >= 10 AND sigma >=
    0.05; BOUNDED if rho <= 3; SLOW otherwise. The class is decided at the scored amplitude; RING-STABLE additionally
    requires BOUNDED at the check amplitude (so "neither amplitude grows" is measured, not inferred); the check
    amplitude's sigma is reported with the linear-regime statement (agreement to 25 percent, or the disagreement on
    the face). HALF-STEP GATE (h1): the L6 run at h_p / 2 must give the same class as the h_p run at M = 48; a
    disagreement marks the probe HALF-BLOCKED: it cannot witness any Q1 form and is reported (stat_credential
    fixture: step-dependent growth). VALIDITY: a Q1 probe is valid at a resolution only if BOTH its amplitudes are
    valid (v5 met, floors met, trajectory complete or a valid prefix below). An invalid or UNAVAILABLE check-
    amplitude run blocks every Q1 form at that resolution EXCEPT a scored-amplitude RING-UNSTABLE witness that is
    itself valid and not half-blocked (an existential witness; the missing linear check on its face).
    FAILED GROWING RUNS (pre-stated, not post-hoc truncation): if a run ends in a Newton failure or a v5 breach at
    step N_f, its VALID PREFIX is the sealed series before N_f. The prefix bears a GROWS class if it holds at least 4
    full period-blocks, rho computed with the prefix's last block in place of blocks 21 to 40 reaches 10 before N_f,
    and sigma over the available growth window is >= 0.05; such a run is a RING-UNSTABLE witness with the failure on
    its face, and its end state for Q2 is the LAST 2 PERIODS OF THE VALID PREFIX, never the samples after the breach.
    A prefix that does not meet this is a failure record (statistics UNAVAILABLE). Fixtures: a growing run failing at
    period 12 (witness), the same failing at period 3 (failure record), a full series whose post-breach tail gives
    different end marks from its prefix (the verdict must use the prefix).
    Q1b PROBES (S3, S4, Z2, Z3 form-bearing; S2 diagnostic): D_shape(t) of D4. Classes at a resolution, scored amplitude: HOLDS if
    max_t D_shape <= 0.1 (the theorem's O(epsilon^2) with margin: K5 gives 0.0142 epsilon R at epsilon = 1e-2 by the
    node displacement and D_shape reads the same 0.0142, the credential record); DRIFTS if max_t D_shape > 0.1 and the
    second-half block maxima have a positive least-squares slope at 3 sigma (monotone growth); WOBBLES if > 0.1
    without monotone growth. GATES, each applied before a class can bear a form: (g1) the control gate: the
    control's own D_shape at the same M, in the same units (epsilon R_d with epsilon = 3e-3), over the whole run
    must be <= 0.02, and over the second half its block-maxima slope must be below 0.1 of the probe's slope, else the
    shape question at that M is Q1B-NO-CALL (late numerical drift cannot pass as physics; the gate is tested on a
    synthetic control that is quiet early and drifts late, selftest); (g2) the half-step gate: the probe's h_p / 2
    run at M = 48 (L6) must agree with the h_p run on the CLASS, and when the class is DRIFTS also on the drift
    statistic (the second-half slope of the block maxima: same sign and agreement to 30 percent), else the probe is
    HALF-BLOCKED and cannot witness (stat_credential fixture: equal maxima, incompatible drift: one DRIFTS, one
    WOBBLES, must block); (g3) the resolution agreement D7; (g4) the observable's floor: K6 F1b's reading at that
    M, in units epsilon R_d at the scored amplitude, must be below 0.02 (it is 0.0016 at M = 48 and 0.0001 at
    M = 96 from the credential record, a number, not a bar; written here so the gate is arithmetic). VALIDITY: a
    shape probe bears a class at a resolution only if BOTH its amplitudes are valid under v5 (the check-amplitude
    run is validity-bearing though its D_shape is not scored; a failed or unavailable check run blocks that probe
    from HOLDS, WOBBLES and DRIFTS alike; fixture); the check amplitude's D_shape is reported, not scored, and no
    reading claims absence of drift at the check amplitude.
    WU is scored as FAMILY-DRIFT-AS-EXPECTED if its R_mean and beta move to the neighbouring family member and stay
    there: with beta_J = J(t) / J_ctrl (the ratio to the CONTROL'S OWN sealed J0 at the same M, so the polygon's
    convention cancels) the prediction is R_pred = discrete_ring_radius(M, kappa, 1, beta_J), and the run passes if
    |R_mean(second half) / R_pred - 1| <= 1e-2 and |beta(second half) / beta_ctrl / beta_J - 1| <= 2.5e-3 (where
    beta_ctrl is the control's sealed mean beta, the same convention; 0.25 of the probe's amplitude, i.e. the
    convention offset is removed by the ratio and the bar is set by the amplitude alone). Else WU is recorded as an
    anomaly of the instrument on the face; it bears no physics form and blocks none, since it is the family check.
    FAILED TRAJECTORIES. A Newton failure or a v5 breach is sealed as a probe-local failure record at the step it
    occurred; the statistics that need the missing samples are marked UNAVAILABLE for that run and the verdict
    proceeds with the other runs. Existential witnesses (a valid GROWS or DRIFTS elsewhere) are retained. A run
    with fewer than two samples does not halt the driver; it is a failure record.
D6. STATIC CROSS-CHECK: the constrained spectrum of the Leg C static functional at the ring-wave (ring_wave_stability.
    rope_spectrum at beta = 1), with the stationarity measure S required below 1e-2 (the fold reads 8.7e-4) and the
    count of negative modes reported. It is a cross-check: the dynamics decide, and a disagreement between the
    two is recorded as a finding, not resolved by choosing.
D7. RESOLUTION: a Q1 or Q1b form is rendered only if M = 48 and M = 96 agree on the class for every probe of that
    question; otherwise that question's NO-CALL (resolution-dependent), the classes on the face.

## HARNESS (binding)
Driver and verdict on labkit (Driver / Verdict / Halt / Checkpoint); units in order: credential (the Leg 0 part 2
bars K1 to K6 re-run through the production instrument at M = 48, sealed; halt if any fails), stat_credential (the
D5 statistics on synthetic sealed trajectories, each with its class or form pre-stated in the unit: a pure
exponential (GROWS), a tanh-saturated exponential at sigma 0.3 (GROWS), a bounded oscillation (BOUNDED), a quiet-
then-drifting control (g1 blocks), a late-noise control against a quiet probe (f2 blocks), step-dependent growth
(h1 half-blocks), a growing run failing at period 12 (prefix witness) and at period 3 (failure record), a full
series whose post-breach tail and prefix give different end marks (the prefix is used), equal maxima with
incompatible drift (g2 half-blocks), a failed check-amplitude run beside a valid scored run for a Q1 probe (blocks
all but a RING-UNSTABLE witness) and for a shape probe (blocks all classes), DRIFTS at the check amplitude only at
one M and at the scored amplitude only at the other (Q1b witness, Q2 qualifying set per probe), one witness beside
a half-blocked GROWS probe with different end marks (the half-blocked probe is not qualifying), two qualifying runs
with one mark unavailable (Q2-NO-CALL); generated from closed forms, not from the instrument; sealed), static (D6, sealed),
ctrl_M48, ctrl_M96, evidence (the 36 runs of D2, then the 10 half-step runs of L6, each trajectory's D3 observables
sealed to the checkpoint as it completes; resumable), verdict (the D5 statistics computed from the seals, the forms
rendered once, one FORM per question on every terminal verdict). The driver imports benchmarks/foundations/
ring_wave_dynamics.py and ring_wave_stability.py and nothing else from benchmarks/; the manifest lists both.
LAB_SMOKE=1 runs the credential unit at M = 16 for two periods (which includes K3, the UNPERTURBED beta = 1
ring-wave as a conservation known answer: this is the one beta = 1 integration before the lock, it carries no probe,
and it is disclosed here rather than denied) and ONE probe on the beta = 0.5 FAMILY MEMBER (S3 at epsilon = 3e-3,
M = 16, 2 periods; not the evidence state), printing no rho, sigma or D_shape, only that the trajectory completed
and that the plumbing path (checkpoint seal and read-back of the credential, static and control records) ran
without exception. Memory: under 1 GB. The runner's environment needs JAX and SciPy (the lab
venv).

## VALIDATION BARS (halt-grade; the credential unit)
v1. K1: twist-wave period within 2e-3 of the chain's dispersion; E drift < 1e-6.
v2. K2: pulsating circle |R - R0 cos(t / R0)| < 1e-3 to R0 / 2; E drift < 1e-4.
v2p. THE PRODUCTION STEP on a large-amplitude known answer: K2 and K3 re-run at h_p = 2 pi R / 500 at M = 48 under
    the K2 and K3 bars above (the executor's record, analysis/RING_WAVE_STABILITY_leg0.md section 10: K2 worst
    |R - exact| 2.0e-5, E drift 3e-12; K3 drifts at 1e-13); halt if either fails. v5's E bar is thereby
    credentialed at the step the evidence runs use, in the nonlinear regime.
v3. K3: the unperturbed ring-wave at R_d for two periods: E, J, Q drift < 1e-8; |P| < 1e-8; R_spread < 1e-6;
    R_mean drift < 1e-4.
v4. K4: P, J, Q conserved to 1e-9 on the generic datum WITHOUT the gauge pin; energy order > 1.8; the pinned
    run's J drift reported (the pin's torque).
v4b. K5: the deformed beta = 0.5 loop stays within 0.1 epsilon R of its initial shape over two periods by node
    displacement; J to 1e-7; D_shape reported.
v5. Every evidence run, BOTH amplitudes: Newton converged at every step, E drift < 1e-4 relative, Q to 1e-8,
    constraint violation < 1e-10, and J drift <= 2e-6: the arithmetic is 20 times K5's two-period J bar of 1e-7
    (40 periods against 2), the pin's torque accumulating linearly; no fixture number entered this bar. A breach
    is a failure record on that run (D5), kept, not rerun with other settings.
v6. K6, the shape observable on known answers at M = 48 and 96 (exact answers 0, 0, 0, 0, a): F1 an unchanged
    noncircular polygon (r = R (1 + 0.05 cos 3 theta), equalized) under a cyclic relabeling by 7 nodes, D_max <
    1e-10 R; F1b the same polygon with its nodes slid along the shape by 0.37 of a spacing and re-equalized by the
    instrument's piecewise-linear equalize (nodes moved onto the chords, an O(spacing^2) change made by the
    equalizer, not by the dynamics), INFORMATIVE, no bar (its first bar had been set after a reading, which is not
    a credential bar, so it bears none; its reading is gate g4's number); F1c the same slide
    with the equal-chord nodes kept ON the smooth curve (equalize_spectral), D_max < 1e-8 R; F2 the relabeling of F1
    plus a rigid rotation (0.7 rad in plane, 0.1 rad tilt) plus a translation, D_max < 1e-10 R; F3 a genuine
    deformation, radial a = 1e-3 R cos 5 theta re-equalized, D_max within [0.5, 1.5] a. F4, informative: the
    indexed-node Procrustes on F1 and F1b. The halt-grade K6 bars are F1, F1c, F2, F3, all written before their
    fixtures ran; locked in the instrument's docstring; the credential record is analysis/ring_wave_dynamics_leg0.json.

## FORMS (exhaustive; pre-registered; exactly one per question on every terminal verdict; every form "under action (i)")
Q1 (exactly one):
  RING-STABLE          W1, W2 and R0 all BOUNDED at both resolutions AND at both amplitudes, none half-blocked, WU FAMILY-DRIFT-AS-
                       EXPECTED or its anomaly on the face: the twist-speed channel is closed at this order; the
                       ring-wave oscillates about itself when its twist is slowed locally.
  RING-UNSTABLE        W1, W2 or R0 GROWS at both resolutions at the scored amplitude (full run or valid prefix),
                       not half-blocked: the mode and its sigma named; a growing channel under action (i), with Q2
                       saying whether the end state carries the fold's marks; the class's standing as a free object
                       is then the author's reading, and no follow-up may search for a reason the twist should
                       travel (no-rescue).
  RING-SLOW            no Q1 probe GROWS and at least one is SLOW, all valid: rho and sigma on the face; the next
                       step named as a longer run at the same locked settings, not a different instrument.
  Q1-NO-CALL           v1 to v6 unmet, a Q1 probe invalid at either amplitude without a valid RING-UNSTABLE witness,
                       every Q1 probe half-blocked, D7 disagreement, or the import ban violated; the reason on the face.
Q1b (exactly one):
  NEUTRAL-HOLDS        every form-bearing shape probe (S3, S4, Z2, Z3) HOLDS at both resolutions, gates g1 to g4 met: the family of static shapes
                       is a flat valley the dynamics does not leave at second order over 40 periods; the ring is one
                       point of a continuum of g = 2 states of equal energy and equal length.
  NEUTRAL-DRIFTS       at least one shape probe DRIFTS at both resolutions (at its own amplitude at each; the witness
                       need not be the same amplitude at both M), gates met: the valley tilts at second order; the
                       direction (toward fold or other, Q2) named.
  NEUTRAL-WOBBLES      no probe DRIFTS and at least one WOBBLES at both resolutions, gates met; reported.
  Q1B-NO-CALL          a gate failed, D7 disagreement, or every shape probe invalid; the reason on the face.
Q2 (exactly one):
  END-FOLD             triggered by RING-UNSTABLE or NEUTRAL-DRIFTS; the WITNESSES are exactly the probes that
                       rendered the Q1 or Q1b form by that question's own predicate (valid, GROWS or DRIFTS, not
                       half-blocked, at both M; the verdict takes the witness list from the Q1 and Q1b deciders,
                       never re-derives it); the qualifying runs are every valid, gated GROWS or DRIFTS run of a
                       witness at its own resolution and amplitude, with a prefix witness's end state read from the
                       last 2 periods of its valid prefix; EVERY qualifying run's three fold marks are AVAILABLE and
                       met.
  END-OTHER            triggered; at least one qualifying run has a KNOWN failed fold mark; described on the face.
  END-NOT-TRIGGERED    neither RING-UNSTABLE nor NEUTRAL-DRIFTS was rendered; a determination, and it never asserts
                       that no witness existed when Q1b rendered one.
  Q2-NO-CALL           triggered, no known failed mark, and at least one qualifying run's mark UNAVAILABLE
                       (mixed-availability fixture: two qualifying runs, one with all marks met and one with a mark
                       missing, must render Q2-NO-CALL, not END-FOLD).
Readings written on the results file's face, not formed, and claiming only what the runs measure. This
experiment integrates selected finite-amplitude probes for 40 periods under action (i) with no Coulomb coupling; it
computes no dynamical spectrum, so NO form here passes or fails the electron ledger's acceptance test A2 (linear
stability), which remains unrun. RING-STABLE with NEUTRAL-HOLDS: the locked probes neither grow nor drift over 40
periods at the scored amplitudes, at both resolutions; the candidate is, on this evidence, a flat continuum of
equal-energy shapes rather than one state (a property the class must then explain or be charged for), and A2 is the
next test, not this one. RING-UNSTABLE: a locked observable grows under action (i) at the stated rate; whether the
end state is the fold is Q2's two marks (the fold's energy to 5 percent and R_end / R_mean > 1.3 with the phase
speed below 0.5), which identify a neighbourhood, not the fold uniquely and not an end-state g. NEUTRAL-DRIFTS
with RING-STABLE: a second-order drift at the measured slope, direction per Q2. Every reading is under action (i);
the theorist owes the form of the twist's action before any of them is more than conditional (P1).

## NO-RESCUE RULE
No probe added, removed or re-amplituded after the lock; no threshold moved; no run discarded for its outcome; a
Newton failure is a failure record on its run and stays one. If the result is RING-UNSTABLE, no follow-up may search
for a reason the twist should travel; that would be a grant, and grants are the author's.

## SMOKE DISCIPLINE (binding on the drafting worker)
The smoke run touches M = 16 for two periods (K3's unperturbed calibration included) and one probe on the beta = 0.5
member, prints completion only. The
drafting worker does not run any evidence cell at M = 48 or 96, does not run any probe on the beta = 1 state, and
does not run any probe for more than two periods, before the lock. The stat_credential's synthetic trajectories are
generated from closed forms, not from the instrument.

## SCHEDULING (budgets, not bars; measured from Leg 0 part 2)
M = 48: about 5 ms per step on the mini's class of machine (JIT compiled; 239 unknowns), 20,000 steps: about 2
minutes per run; 18 evidence runs plus the control: 40 minutes. The 10 half-step runs at M = 48: 4 minutes each,
40 minutes. M = 96 (479 unknowns): about 4 times per step, 19 runs: 2.5 hours. D_shape in the verdict unit: 100
frames per shape run, about 0.3 s each at M = 48 and 1 s at M = 96, 15 minutes in all. Credential, stat_credential
and static units: 10 minutes. cpu_hours 8 (with margin), mem_gb 1, usd 0 beyond drafting and review.
Results to analysis/RING_WAVE_STABILITY_4_results.md.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
1. The executor built the instruments and ran only known-answer cases: the Michell ring, the pulsating circle, the
   frozen-ring twist wave, generic data, the co-moving fold (the competitor state, already on the record), the
   UNPERTURBED ring-wave for two periods (K3), the shape theorem on the beta = 0.5 FAMILY MEMBER (K5: n = 3,
   epsilon = 1e-2, two periods), and the K6 fixtures (static polygons, no dynamics).
2. The one run that touched the beta = 1 evidence state, disclosed in -2 and -3 and judged in both: the n = 2 shape
   probe at epsilon = 1e-2, M = 16, aborted by a Newton failure at 0.3 of a period BEFORE the gauge pin existed (the
   sliding runaway); the pin was added after it. It stands as an EXPLORATORY record with its failure. The cure both
   reviewers asked for in -3 round 1 is APPLIED here, not offered: S2 is out of the form-bearing set (CONFIG
   shape_bearing = ('S3', 'S4', 'Z2', 'Z3')); its runs are made and reported as diagnostic only. The remaining
   schedule (W1, W2, R0, WU, S3, S4, Z2, Z3 on the beta = 1 state) is uninspected: no probe of it has been integrated
   at any M or amplitude.
3. Bar provenance. Every dynamics bar is the author's draft bar or stated arithmetic (v5's J bar: 20 times K5's;
   v2p's bars are K2's and K3's). K6 F1b's first bar (5e-5 R, -3) had been set after the fixture's first run read
   2.8e-5 R; both -3 reviewers held that a credential bar must be prospective, and the cure is the plain one: F1b
   bears no bar (informative), and the slide reading is credentialed by F1c, whose bar of 1e-8 R was written before
   it ran, was missed by the first version of the projection (5.6e-8 R) and met after the joint least squares was
   added (5.3e-9 R) with the bar unmoved. F1b's reading enters only as gate g4's number.
4. The workers' -2 and -3 kits (benchmarks/lab/ring_wave_stability_2/, _3/) were never pushed to any branch. The
   cures recorded in their reviews are written into this charter from the review transcripts (analysis/queue/
   parked/README.md); none of their numbers are on any branch and none enter here.
5. Expectations, disclosed so they cannot be mistaken for results: the shape probes will hold at first order (that
   is the theorem, already known); the executor has no expectation about the twist-speed channel or the second-
   order drift. The Director's expectation (memo, 2026-10-25): RING-STABLE, low confidence.

## NORTH STAR ACCOUNTING
Interior work by its own account: it names no section 5(a) target, retires no input and arms no registered
discriminator; it moves none of the five numbers and no scorecard row; it measures whether locked finite-amplitude
probes of the one class with g = 2 grow or drift under action (i). It does not adjudicate the electron ledger's
A2. ELEC-G-2 (2026-10-22) was interior (its locked charter, section 0), and no target-facing session has completed
since, so under section 5 as written this is a second consecutive interior session. It locks under the AUTHOR'S
EXPLICIT EXCEPTION, recorded on the page itself: docs/NORTH_STAR.md, section 5, the paragraph "Exception, recorded
by the author on 28 October 2026", which names this commission, states the reason (every target-facing draft since
ELEC-G-2 was withdrawn or declined on a derivation obstruction no lab commission can lift, analysis/
GRV_2PI_derivation_reading.md, so no target-facing work is displaced), limits itself to one commission and one
lock, and requires the next session to be target-facing. The reviewers apply the rest of section 5 as written.

## STANDING
Draft, 2026-10-28, on the queue branch for the Director's proposal under approval mode and the author's approval.

```lab
commission: RING-WAVE-STABILITY-4
target: "Electron sector (blocks the strength-of-magnets row, gap 4): whether locked finite-amplitude shape and twist-speed probes of the travelling-twist ring, the one registered mechanism class with g = 2 by mechanics, grow or drift over 40 periods in the full nonlinear dynamics of its action, conditional on action (i) (a disclosed premise), and whether a growing run's end state carries the co-moving fold's marks; interior work locking under the author's dated section 5 exception (docs/NORTH_STAR.md); moves no number in section 2b"
driver: benchmarks/lab/ring_wave_stability_4/driver.py
verdict_script: benchmarks/lab/ring_wave_stability_4/verdict.py
instrument:
  - benchmarks/foundations/ring_wave_dynamics.py
  - benchmarks/foundations/ring_wave_stability.py
  - benchmarks/foundations/elec_rope_wave.py
  - benchmarks/foundations/elec_rotator.py
  - benchmarks/lab/_kit/labkit.py
forms: [RING-STABLE, RING-UNSTABLE, RING-SLOW, Q1-NO-CALL, NEUTRAL-HOLDS, NEUTRAL-DRIFTS, NEUTRAL-WOBBLES, Q1B-NO-CALL, END-FOLD, END-OTHER, END-NOT-TRIGGERED, Q2-NO-CALL]
state: [analysis/ring_wave_stability_4_ckpt.pkl]
budget: {cpu_hours: 8, usd: 0}
mem_gb: 1
```
