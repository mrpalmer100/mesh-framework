# COMMISSION RING-WAVE-STABILITY -- IS THE g = 2 STATE A STABLE OBJECT? THE TRAVELLING-TWIST RING UNDER PERTURBATION
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-26; the Director's RING-WAVE-STABILITY, advice memo
# 2026-10-25 #2, drafted by the executor on two instruments credentialed on known answers only; a measurement by
# time integration with the outcome unknown to everyone; harness on benchmarks/lab/_kit/labkit.py)

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
second order toward the fold or stay put. Nobody knows either answer. That is the question, and the answer decides whether
the class is a candidate free electron (its remaining price then being scale) or an excited state whose g = 2 is a
property of something that does not persist.

## THE QUESTION
  Q0  THE ACTION (a registry reading by quotation, before any run; D4). Two actions reduce to Leg C's static
      functional at small twist and differ at O(1) exactly at the ring-wave (kappa Phi'^2 / T = 1): (i) Nambu-Goto
      plus the twist as a massless scalar on the string's INDUCED metric, S = -Int sqrt(-h) [T + (kappa / 2)
      h^ab d_a Phi d_b Phi]; (ii) Nambu-Goto in five dimensions with the twist as a fifth target coordinate,
      S = -T Int sqrt(-det(dX . dX + (kappa / T) dPhi dPhi)). From GRV-018, GRV-020 (the Goldstone energy), EM-RECON-012
      (torsion waves at c), EM-019 (momentum density = energy flux / c^2) and EM-008, by quoted claim text: does the
      registry fix (i), fix (ii), or is it SILENT? The instrument implements (i).
  Q1  THE TWIST-SPEED CHANNEL under action (i). The discrete ring-wave at its own equilibrium (M nodes, winding 1,
      kappa_tw = 0.5, T = c = 1, beta = 1), perturbed in the twist's phase speed (probes W1, W2 of D2) or in its
      length mode (R0) at amplitude epsilon, integrated for N_per periods: is the perturbation bounded, or does it
      grow, and at what rate?
  Q1b THE NEUTRAL MANIFOLD. The same state perturbed in shape (S2, S3, S4, Z2, Z3): does the deformed loop stay
      where the theorem puts it (displacement O(epsilon^2) and bounded), or drift at second order, and toward what?
  Q2  THE END STATE of any growing probe: does the shape at the end of the run approach the co-moving fold
      (E within 5 percent of the fold's 8.144 at this kappa and J, R_end / R_mean > 1.3, the twist's phase speed
      fallen below 0.5), or something else (described, not formed)?

## WHAT IS GIVEN (registered inputs; no others enter)
- The action of Q0 (i) as implemented in benchmarks/foundations/ring_wave_dynamics.py (Leg 0 part 2, credentialed:
  the twist wave's dispersion to 5e-6, the Nambu-Goto pulsating circle to 2e-7, the unperturbed ring-wave's E, J,
  P and winding to 1e-11 over two periods, discrete Noether on generic data to 1e-13, the shape theorem on the
  beta = 0.5 member to O(epsilon^2); analysis/RING_WAVE_STABILITY_leg0.md section 7 and analysis/
  ring_wave_dynamics_leg0.json). The arc-length gauge's one collective sliding mode is pinned by a holonomic
  constraint on node 0 (the pin's torque is the J bar of every run, v5).
- The constrained-Hessian instrument benchmarks/foundations/ring_wave_stability.py (Leg 0 part 1: the Michell
  threshold sqrt 3 B / C from the spectrum to 1.6e-4; the stationarity measure S with its floor 9e-5; the fold a
  node-space minimum), used here for the static cross-check D6 only.
- GRV-020, GRV-018, EM-RECON-012, EM-019, EM-008 (Q0's inputs); FND-006 (mu = T / c^2); the Leg C record for the
  fold's energy at this kappa and J (8.144 at beta_p = 0, M = 48, elec_rope_wave form; 8.100 in the E2b Routhian form).
- Units: T = c = 1; kappa_tw = 0.5, so R_d = 0.707359 at M = 48 (the polygon's equilibrium; the continuum
  sqrt(kappa / T) = 0.707107) and J = 2 pi kappa = pi. In these units kappa only sets R; the question is scale-free,
  so ONE kappa is run and the scan is over the probe content (D2), not over kappa. (The Director's estimate said
  three kappa values; the executor's Leg 0 shows why one suffices, and D2 spends the budget on probes instead.)

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
section 6, HBAR-003), the rope's kappa (ELEC-KAPPA-1, withdrawn), or the fold's own stability (it is the
reference minimum; Leg 0 part 1 K3).

## DESIGN COMMITMENTS (locked at lock)
D1. THE STATE. The discrete ring-wave is built by ring_wave_dynamics.ring(M, R_d, winding = 1, phase_speed = -1)
    with R_d = discrete_ring_radius(M, kappa) (the polygon's own equilibrium, found by root find; the K3 start).
    Resolutions M = 48 (working) and M = 96 (check). Step h = 0.01 (2 pi R_d / M); N_per = 40 periods of
    2 pi R_d (about 180 time units; 20,000 steps at M = 48). Newton tolerance 1e-13 as in the credential.
D2. THE PROBES (the whole set; no others), each applied to the K3 state at t = 0, at two amplitudes
    epsilon = 1e-3 and 1e-2:
      S2, S3, S4   shape: in-plane radial displacement delta r = epsilon R_d cos(n theta), n = 2, 3, 4, then
                   re-equalized by ring_wave_dynamics.equalize (the constraint must hold at t = 0);
      Z2, Z3       shape: out-of-plane displacement delta z = epsilon R_d cos(n theta), n = 2, 3;
      R0           the radial kick: uniform radial velocity epsilon (the n = 0 mode at fixed J, since a radial
                   velocity carries no J_z);
      W1, W2       twist speed: delta Phi-dot = epsilon cos(n theta) / R_d, n = 1, 2 (a local change of the twist's
                   phase speed; the probe that opens the travelling-to-co-moving channel);
      WU           the uniform twist-speed change delta Phi-dot = epsilon / R_d (moves along the family direction
                   of section 7 ii: J changes by 2 pi kappa epsilon; this probe is EXPECTED to drift, not grow,
                   and is scored separately under D5 as the family check, not as an instability).
    Twelve probes times two amplitudes times two resolutions: 48 runs.
D3. THE OBSERVABLES, sealed per run at every 10th step: the Fourier amplitudes a_n(t) of the radial displacement
    r_i - mean(r), of z_i, and of Phi-dot_i - mean(Phi-dot), for n = 0..6; E, J, P, the twist charge Q, R_mean,
    R_end / R_mean, the mean twist phase speed beta(t) = -mean(Phi-dot) R_mean; the Newton iteration count.
D4. Q0 by quotation only: a form fires on quoted claim text; paraphrase or inference is SILENT.
D5. THE GROWTH STATISTIC, per probe and amplitude. For the Q1 probes (W1, W2, R0): A(t) = the amplitude of the
    probed mode (the a_n of Phi-dot for W; |R_mean - R_d| for R0). The envelope ratio rho = max_{t in second half}
    A(t) / max_{t in first 2 periods} A(t), and the rate sigma from a least-squares fit of ln(envelope of A) over
    the second half, in units of 1 / period. Linear-regime check: sigma at epsilon = 1e-3 and 1e-2 agree to 25
    percent or the probe is scored at epsilon = 1e-3 and the disagreement recorded.
    Thresholds, fixed here: GROWS if rho >= 10 AND sigma >= 0.05 per period at both resolutions; BOUNDED if
    rho <= 3 at both resolutions; SLOW otherwise (reported with rho and sigma; neither form).
    For the Q1b probes (S2, S3, S4, Z2, Z3): D(t) = the largest node displacement from the deformed initial shape
    X(0), in units of epsilon R_d (the first-order scale). NEUTRAL-HOLDS if max_t D(t) <= 0.1 over the run at both
    resolutions (the theorem's O(epsilon^2) with margin; K5 gives 0.014 at epsilon = 1e-2 over two periods);
    NEUTRAL-DRIFTS if D(t) exceeds 0.1 and its growth is monotone (fit of D over the second half, slope > 0 at
    3 sigma); NEUTRAL-WOBBLES if D exceeds 0.1 without monotone growth (reported). The end state of a drifting
    shape probe goes to Q2.
    WU is scored as FAMILY-DRIFT-AS-EXPECTED if its R_mean and beta move to the neighbouring family member
    (R^2 = kappa (1 + beta^2) / 2T to 1 percent) and stay there, else recorded as an anomaly of the instrument.
D6. STATIC CROSS-CHECK: the constrained spectrum of the Leg C static functional at the ring-wave (ring_wave_stability.
    rope_spectrum at beta = 1), with the stationarity measure S required below 1e-2 (the fold reads 8.7e-4) and the
    count of negative modes reported. It is a cross-check: the dynamics decide, and a disagreement between the
    two is recorded as a finding, not resolved by choosing.
D7. RESOLUTION: the form is decided only if M = 48 and M = 96 agree on GROWS / BOUNDED for every probe; otherwise
    NO-CALL (resolution-dependent).

## HARNESS (binding)
Driver and verdict on labkit (Driver / Verdict / Halt / Checkpoint); units in order: credential (the four Leg 0
part 2 bars re-run through the production instrument at M = 48, sealed; halt if any fails), static (D6, sealed),
evidence (the 48 runs of D2, each trajectory's D3 observables sealed to the checkpoint as it completes;
resumable), dictionary (Q0's quotations as data), verdict (the D5 statistics computed from the seals, the forms
rendered once). The driver imports benchmarks/foundations/ring_wave_dynamics.py and ring_wave_stability.py
and nothing else from benchmarks/; the manifest lists both. LAB_SMOKE=1 runs the credential unit at M = 16 for
two periods and ONE probe (S2 at epsilon = 1e-2, M = 16, 2 periods) printing no rho or sigma, only that the
trajectory completed. Memory: under 1 GB. The runner's environment needs JAX (pip install jax, the lab venv).

## VALIDATION BARS (halt-grade; the credential unit)
v1. K1: twist-wave period within 2e-3 of the chain's dispersion; E drift < 1e-6.
v2. K2: pulsating circle |R - R0 cos(t / R0)| < 1e-3 to R0 / 2; E drift < 1e-4.
v3. K3: the unperturbed ring-wave at R_d for two periods: E, J, Q drift < 1e-8; |P| < 1e-8; R_spread < 1e-6;
    R_mean drift < 1e-4.
v4. K4: P, J, Q conserved to 1e-9 on the generic datum WITHOUT the gauge pin; energy order > 1.8; the pinned
    run's J drift reported (the pin's torque; 1e-3 on fast generic data at M = 32, 1e-8 on the K5 probe).
v4b. K5: the deformed beta = 0.5 loop stays within 0.1 epsilon R of its initial shape over two periods; J to 1e-7.
v5. Every evidence run: Newton converged at every step (no run abandoned), E drift < 1e-4 relative, Q to 1e-8,
    J to 1e-7 (the gauge pin's torque is the only non-conservation; a run exceeding it is a NO-CALL on that probe,
    kept, not rerun with other settings), constraint violation < 1e-10.

## FORMS (exhaustive; pre-registered; anything else is NO-CALL)
Q0 (exactly one): ACTION-INDUCED (the registry fixes (i); the result is unconditional), ACTION-5D (the registry
    fixes (ii); the instrument is the wrong object and Q1's result is recorded as NOT ABOUT THE REGISTERED CLASS),
    ACTION-SILENT (the result is conditional on (i), and the registry owes the form of the twist's action).
Q1 (exactly one):
  RING-STABLE          W1, W2 and R0 all BOUNDED at both resolutions, WU FAMILY-DRIFT-AS-EXPECTED: the twist-speed
                       channel is closed at this order; the ring-wave oscillates about itself when its twist is
                       slowed locally.
  RING-UNSTABLE        W1, W2 or R0 GROWS at both resolutions: the mode and its sigma named; the travelling twist is
                       dynamically unstable toward co-moving (if END-FOLD) and the class is dead as a free object
                       unless a registered reason restores the twist's travel (none is proposed here; no-rescue).
  RING-SLOW            no Q1 probe GROWS and at least one is SLOW: rho and sigma on the face; the next step named as
                       a longer run at the same locked settings, not a different instrument.
  NO-CALL              v1 to v5 unmet, D7 resolution disagreement, or the import ban violated.
Q1b (exactly one):
  NEUTRAL-HOLDS        every shape probe holds (D <= 0.1 at both resolutions): the family of static shapes is a
                       flat valley the dynamics does not leave at second order over 40 periods; the ring is one
                       point of a continuum of g = 2 states of equal energy and equal length.
  NEUTRAL-DRIFTS       at least one shape probe drifts monotonically: the valley tilts at second order; the
                       direction (toward fold or other, Q2) named.
  NEUTRAL-WOBBLES      exceeds 0.1 without monotone growth; reported, neither of the above.
Q2 (if RING-UNSTABLE or NEUTRAL-DRIFTS): END-FOLD (the end state meets all three fold marks), END-OTHER (described).
Readings written on the results file's face, not formed: RING-STABLE with NEUTRAL-HOLDS means A2 passes for the
first time for any candidate, with the twist that the candidate is not one state but a flat continuum of equal-
energy shapes (a property the class must then explain or be charged for); RING-UNSTABLE with END-FOLD means the
g = 2 state decays into the g = 0.9 state and the class's g = 2 was a property of an excited configuration;
NEUTRAL-DRIFTS toward the fold with RING-STABLE means the decay is second order and slow, a metastable candidate
with a lifetime to be measured; ACTION-SILENT under any of these means the theorist owes the form before the
result is more than conditional.

## NO-RESCUE RULE
No probe added, removed or re-amplituded after the lock; no threshold moved; no run discarded for its outcome; a
Newton failure is a NO-CALL on its probe and stays one. If the result is RING-UNSTABLE, no follow-up may search
for a reason the twist should travel; that would be a grant, and grants are the author's.

## SMOKE DISCIPLINE (binding on the drafting worker)
The smoke run touches M = 16 for two periods and one probe, prints completion only. The drafting worker does not
run any evidence cell at M = 48 or 96, and does not run any probe for more than two periods, before the lock.

## SCHEDULING (budgets, not bars; measured from Leg 0 part 2)
M = 48: about 5 ms per step on the mini's class of machine (JIT compiled; 239 unknowns), 20,000 steps: about 2
minutes per run, 24 runs: 1 hour. M = 96 (479 unknowns): about 4 times per step, 24 runs: 4 hours. Credential and
static units: 5 minutes. cpu_hours 8 (with margin), mem_gb 1, usd 0 beyond drafting, the Q0 reading and review.
Results to analysis/RING_WAVE_STABILITY_results.md.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
The executor built both instruments and ran only known-answer cases: the Michell ring, the pulsating circle, the
frozen-ring twist wave, generic data, the co-moving fold (the competitor state, already on the record), the
UNPERTURBED ring-wave for two periods (K3; conservation to 1e-11, the circle kept to 8e-12), and the shape
theorem on the beta = 0.5 FAMILY MEMBER (K5: a radially deformed static loop, n = 3, epsilon = 1e-2, two periods,
moved 1.4 epsilon^2 R). Two further smoke runs on the beta = 0.5 member are disclosed: the n = 2 shape probe at
epsilon = 1e-2 for two periods (M = 16; it did not move, the same theorem), and the same run WITHOUT the gauge
pin, which ran away in the sliding mode (node speeds of 16 c by t = 1) and is the reason the pin exists. One run
touched the beta = 1 evidence state with a probe: the n = 2 shape probe at epsilon = 1e-2, M = 16, aborted by a
Newton failure at t = 1.28 (0.3 of a period) BEFORE the pin existed; its failure was the sliding runaway, not a
physical outcome, and nothing about stability was or could be read from 0.3 of a period of a diverging gauge
mode. It is disclosed as the checklist requires; the reviewers judge item I. No W probe, no R0 probe, no Z probe
and no run at M = 48 or 96 with any probe has been made. K3 and K5 are runs over spans that cannot show a growth
rate; this charter's N_per = 40 is twenty times that span. The executor's prior, disclosed so it cannot be
mistaken for a result: the shape probes will hold at first order (that is the theorem, already known) and the
executor has no expectation about the twist-speed channel or the second-order drift. The Director's expectation
(memo): RING-STABLE, low confidence.

## NORTH STAR ACCOUNTING
Interior work by its own account: it moves none of the five numbers and no scorecard row; it decides whether the
one class with g = 2 persists. The author approves it as the one interior session section 5 allows between
target-facing sessions, knowing the last completed session (ELEC-G-2, 2026-10-22) was also electron work and the
target-facing drafts since (GRV-2PI-DERIVE-2 and its two siblings) were withdrawn or declined on a derivation
obstruction that no lab commission can lift (analysis/GRV_2PI_derivation_reading.md). The reviewers apply section 5
as they read it.

## STANDING
Draft, 2026-10-26, on the queue branch for the Director's proposal under approval mode and the author's approval.

```lab
commission: RING-WAVE-STABILITY
target: "Electron sector (blocks the strength-of-magnets row, gap 4): whether the travelling-twist ring, the one registered mechanism class with g = 2 by mechanics, is a stable stationary state under shape and twist-speed perturbations over 40 periods in the full nonlinear dynamics of its action (Nambu-Goto plus the twist scalar on the induced metric), or decays toward the co-moving fold 9 percent below it; with the registry reading of which twist action it holds; moves no number in section 2b"
driver: benchmarks/lab/ring_wave_stability/driver.py
verdict_script: benchmarks/lab/ring_wave_stability/verdict.py
instrument:
  - benchmarks/foundations/ring_wave_dynamics.py
  - benchmarks/foundations/ring_wave_stability.py
  - benchmarks/foundations/elec_rope_wave.py
  - benchmarks/foundations/elec_rotator.py
  - benchmarks/lab/_kit/labkit.py
forms: [ACTION-INDUCED, ACTION-5D, ACTION-SILENT, RING-STABLE, RING-UNSTABLE, RING-SLOW, NEUTRAL-HOLDS, NEUTRAL-DRIFTS, NEUTRAL-WOBBLES, END-FOLD, END-OTHER, NO-CALL]
state: [analysis/ring_wave_stability_ckpt.pkl]
budget: {cpu_hours: 8, usd: 0}
mem_gb: 1
```
