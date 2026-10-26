# RING-WAVE-STABILITY Leg 0: the stability instrument, credentialed on known answers (executor, sandbox, 2026-10-26)

Instrument: `benchmarks/foundations/ring_wave_stability.py`. Records: `analysis/ring_wave_stability_leg0.json`,
`analysis/ring_wave_stability_leg0.log`. Commission: the Director's RING-WAVE-STABILITY (advice memo
2026-10-25 #2), proposed under approval mode; this is the Leg 0 its compute estimate names ("credentials the
instrument against two known answers: the Michell threshold of a static twisted ring, and conservation over a
long run on the exact travelling-wave solution"). The first is done here. The second is not (section 5).

## 0. What this file does not contain
The ring-wave evidence cell (the travelling-twist ring of `elec_rope_wave.py` at beta_p = 1, any kappa_tw) was not
built, evaluated, or seeded by this instrument. The file has no code path that constructs it; `fold_reading` runs
`elec_rope_wave.solve` at beta_p = 0 only. The one rope state it reads is the co-moving fold, the competitor
whose energy is already on the record (E 8.100 in the Routhian form, E2b; 8.144 in the uniform-twist form here).
Checklist item I (anti-fishing) is to be judged on that.

## 1. The instrument
`constrained_spectrum(f, cons, x, length)`: for an energy f and hard constraints cons = 0 at a configuration x in
NODE coordinates (M points in R^3, never a Fourier truncation), (a) the multipliers by least squares,
(b) the stationarity measure S = |P grad f| L / f (the constraint-projected gradient, scaled by the length,
over the energy; the dimensionless form of the "gradient / E" that was 0.37 when ELEC-004A failed),
(c) the Hessian of the Lagrangian f - lambda . cons by symmetric finite differences with Richardson
extrapolation in the step ((4 H_h/2 - H_h) / 3, step h = 1e-3 times the segment length), (d) its restriction to
the constraint tangent space with the symmetry generators projected out (rigid motions; for a tension rope also
the M tangential node slidings, the discrete reparametrization), (e) the spectrum with the counts of negative,
null and positive modes and the lowest eigenvector. For the rope: `pieces_nodes` (the `elec_rope_wave` energetics
on a node polygon, line for line), `omega_nodes` (Omega eliminated by the J root find), `rope_functions`
(f = E + wall, cons = (Jvec_x, Jvec_y, P_x, P_y)), `rope_spectrum`.

Why node coordinates: a minimum in the record's 49-dimensional Fourier space (K = 8 modes) can be a saddle in
the 3M-dimensional node space, and a lock that inherited that hole would call a Fourier artifact a stability
verdict. Why the Richardson step: at M = 48 the plain FD Hessian moved the Michell threshold by 1.3e-3 between
h = 1e-3 and 5e-4 segment lengths, the same size as the discretization deficit it was meant to resolve
(2026-10-26, `scratchpad/michell_h.log` numbers: 1.7289, 1.7267 and 1.7379 at h / l0 = 1e-3, 5e-4, 2e-3); with the
extrapolated Hessian the M-sequence is clean (section 2).

## 2. K1, the Michell threshold (FND-STRAND-003's instability as a number)
A closed inextensible rod, bending stiffness B, torsional stiffness C, carrying link Lk entirely as twist on the
flat circle: E = (B / l) sum_i (1 - t_i . t_i+1) + 2 pi^2 C (Lk - Wr)^2 / L, Wr the EXACT polygon writhe (Klenin
and Langowski 2000, method 1a), constraints: every segment length fixed. The flat circle loses stability at
Lk_c = sqrt(3) B / C (Michell 1889; Zajac 1962; Le Bret 1979) in the n = 2 out-of-plane mode. At the circle Wr = 0
and grad Wr = 0 by reflection parity, so the Lagrangian Hessian is exactly linear in Lk; the instrument computes
it at Lk = 0 and 1 by the generic path, checks the linearity by a third generic Hessian at Lk = 2 (residual
7e-9 to 4e-8 at every M), and root-finds the lowest eigenvalue of the pencil.

Extrapolated Hessian, B / C = 1 (theory 1.732051):
    M    16        24        32        48
    Lk_c 1.678045  1.707653  1.718237  1.725639      deficits -3.12e-2, -1.41e-2, -7.98e-3, -3.70e-3
    successive ratios 2.21, 1.77, 2.16 against the M^-2 values 2.25, 1.78, 2.25
    fit v_inf + a M^-p over the four points: p = 1.98, rms 5.0e-5, Lk_c(inf) = 1.731780, relative -1.56e-4 to sqrt 3
B / C = 0.6 (theory 1.039230): 1.006827, 1.024592, 1.030943, 1.035383; p = 1.98; Lk_c(inf) = 1.039068, relative
-1.57e-4. The relative deficits agree to four digits between the two ratios at every M, as the exact scaling
Lk_c = sqrt 3 (B / C) f(M) requires. Mode: n = 2 at every M (the writhing mode; 61 percent of its norm out of
plane, the rest the in-plane bending that accompanies it). No negative mode at Lk = 0 (the untwisted circle is
the bending minimum), zero null modes after the rigid generators are removed (dim 26, 42, 58, 90 = 3M - M - 6).
The plain-Hessian run kept beside it for comparison (`scratchpad/leg0_plainH.log`, not committed) gave
-1.82e-3 at M = 48 for both ratios, the FD bias section 1 describes.

Bar met: the extrapolated threshold is within 2e-4 of sqrt 3 B / C at both ratios (bar 1e-2), the order is 1.98,
the mode is n = 2. The constrained-Hessian machinery finds the classical instability from the spectrum alone.

## 3. K2, the stationarity ceiling reports what it is handed
On the twisted circle (Lk = 1, B / C = 1, M = 48) with an n = 3 out-of-plane ripple of amplitude a:
    a      0         1e-3      1e-2      1e-1
    S      9.0e-5    4.72e-2   0.470     3.55
S at a = 0 is the finite-difference floor (it scales as M times the step; 1.6e-5 at M = 16, 9.0e-5 at M = 48)
and is three to four orders below any ceiling a charter would lock. S is linear in the displacement through two
decades and saturates at a = 0.1. Calibration worth keeping: ELEC-004A's 0.37 corresponds on this ring to a
relative displacement of about 1e-2 from the stationary point, which is not a converged state.

## 4. K3 and K4, the wiring and the writhe
K3. `pieces_nodes` reproduces `elec_rope_wave.pieces` on the same non-circular polygon at beta = 0, 0.6, 1 and
Omega = 0, 0.3 to 6.7e-16 (every energy piece, J, mu, L, Jvec, Pm).
The co-moving fold (beta_p = 0, kappa_tw = 0.5, J = pi, kappa_C = pi / 137, M = 48; re-minimized from the flat seed
in the record's Fourier space, 949 iterations): E 8.14414 (tension 5.632, wave 2.496, Coulomb 0.016), Omega 0.7185,
R_end 1.180, edge speed 0.848, g 0.862. Read in node space: S = 8.7e-4 (ten times the FD floor: the Fourier
minimum is stationary in node space to 1e-3, which is the residual a K = 8 truncation leaves), constraint
violation at the 1e-7 level, spectrum of dimension 86 (144 - 4 constraints - 6 rigid - 48 tangential): 0 negative,
0 null, 86 positive, lowest eigenvalue 0.036, highest 123. The fold is a constrained minimum in node space, as
a converged free minimization must be; the instrument's reading of the reference state is clean. (The 8.144
against E2b's 8.100 is the uniform-twist form against the Routhian form of the co-moving twist, both on the
record; g 0.862 against 0.916 likewise.)
K4. The exact polygon writhe is 0.0 on a planar polygon and agrees with the registered midpoint Gauss integral
(`strand_calugareanu.writhe`) on a chiral closed curve to O(M^-2): differences -9.6e-4, -2.4e-4, -6.0e-5, -1.5e-5
at M = 48, 96, 192, 384 (the registered routine converges to the exact one).

## 5. What is NOT credentialed, and what the charter must settle before the lock
(a) Dynamics. The Director's second known answer, conservation over a long run on the exact travelling-wave
solution, needs a time integrator for the rope with its twist field, and that does not exist. The static
functional of `elec_rope_wave.py` holds beta_p (the twist's travel speed) as a PARAMETER. A Hessian at fixed
beta_p = 1 answers shape stability only; the decay channel the commission is about, travelling twist going
co-moving (beta_p from 1 toward 0 while the shape relaxes to the fold), is a perturbation of the twist field's
time dependence and is invisible to it. The honest object is the worldsheet action of a string carrying a
Goldstone field, S = -int d^2 sigma sqrt(-h) [T + (kappa / 2) h^ab d_a Phi d_b Phi], with the ring-wave as a
stationary solution (its virial R^2 = kappa / T is the centripetal balance of the wave momentum kappa Phi-dot
Phi' / c^2 against the tension), and the linear stability is that action's second variation in BOTH x(s, t)
and Phi(s, t). Building and credentialing that integrator (conservation of E, J and winding on the exact
solution; recovery of the twist wave equation on a fixed ring) is a second Leg 0 item. Until it exists the
charter can lock only the shape-stability question at fixed beta_p, and must say so.
(b) The stationarity ceiling. The record's Fourier minima are node-stationary to about 1e-3. A ceiling of 1e-2
on S would pass them with a decade to spare and fail ELEC-004A's state by a factor 40; the charter should lock
a number of that order, measured on the fold as here, before any Hessian of the evidence cell is formed.
(c) The tangential projection. Removing the M tangential slidings assumes reparametrization is a symmetry of
the discrete energy only approximately (the polygon's segment lengths change under sliding, at second order).
For the rope those modes are soft, not null, and their eigenvalues carry discretization sign noise; projecting
them out is the right reading for a tension rope and is stated as a design commitment, not a theorem.
(d) The Michell credential uses an inextensible rod with bending stiffness; the rope model has tension and no
bending term. The machinery is the same; the physics of the threshold is not the rope's, and the credential
claims only that the instrument finds a known constrained instability from the spectrum with the right mode
and convergence.

## 6. Status (revised in section 7)
Both halves now have a credentialed instrument: the constrained Hessian (sections 1 to 4) and the dynamics
(section 7). The evidence cell is untouched. Nothing here is a result about the ring-wave.

## 7. Part 2 (added 2026-10-26): the dynamics instrument, credentialed
Section 5(a) said the dynamical half had no instrument. It now does: `benchmarks/foundations/ring_wave_dynamics.py`
(records `analysis/ring_wave_dynamics_leg0.{json,log}`; needs JAX, `pip install jax`).

The action is the one Leg C's static functional is the Routhian of: Nambu-Goto plus a massless scalar on the
string's induced metric, S = -Int sqrt(-h) [T + (kappa / 2) h^ab d_a Phi d_b Phi], in static gauge and ARC-LENGTH
gauge (equal segment lengths as holonomic constraints), so the reparametrization freedom is gone and every
remaining coordinate is physical: 2M + 1 for the shape and M for the twist. The twist gradient energy is the
three-point form (no checkerboard mode); the twist field is stored unwrapped with its winding fixed, so the
winding is conserved by construction. The integrator is the constrained variational (discrete Euler-Lagrange,
midpoint discrete Lagrangian, SHAKE structure) scheme solved by Newton with JAX Jacobians. Because the discrete
Lagrangian carries the continuous symmetries exactly, the DISCRETE Noether momenta (translations, rotations
about every axis, the twist charge Phi -> Phi + const) are conserved to roundoff, and the energy oscillates
boundedly at O(h^2). The static ring with its twist travelling at c is a stationary solution at R^2 = kappa / T
(dL / dR = 2 pi [-1 + kappa / R^2]), Leg C's virial, and the polygon's own equilibrium radius (M = 48: 0.707359
against sqrt(kappa / T) = 0.707107) is found by a root find on the discrete Lagrangian before any run.

Known answers, M = 48 (bars in the file):
  K1  Twist wave on a frozen ring, mode n = 3: period 2.106420 against the three-point chain's exact dispersion
      2.106409 (5e-6; the continuum 2.094395 is 0.6 percent away, the M^-2 discretization); energy to 2e-15.
  K2  The Nambu-Goto pulsating circle (kappa = 0, the twist frozen, the sliding gauge pinned, which is
      torque-free by symmetry): R(t) = R0 cos(t / R0) followed from R0 to R0 / 2 with worst error 2e-7; E0 = 6.27870
      (the 48-gon's perimeter against 2 pi), drift 2e-11; the circle kept to 3e-13.
  K3  The exact ring-wave, unperturbed, two periods: E0 8.882595 (closed form at the continuum radius 8.885766;
      the 3e-4 is the polygon), J0 = 2 pi kappa to 1e-13, |P| 3e-11, E drift 1e-11, J drift 3e-11, twist charge
      drift 8e-11, the circle kept to 6e-12 and R_mean to 7e-11, the spacing to 2e-14. Conservation only. Two
      periods of an unperturbed state cannot show a growth rate and none is read.
  K4  Generic smooth data (a wobbly twisted loop with transverse velocity and a twist pulse), h = 0.04, 0.02, 0.01:
      |dP|, |dJ|, dQ below 1e-12 at every h; energy drift 1.8e-4, 4.9e-5, 1.3e-5, order 1.90.

Three things the charter now has to settle, found while building this:
(i)  WHICH ACTION. "Scalar on the induced metric" (this instrument, Leg C) and "Nambu-Goto in five dimensions
     with the twist as a fifth coordinate", S = -T Int sqrt(-det(dX . dX + (kappa / T) dPhi dPhi), agree at first
     order in kappa Phi'^2 / T and differ at O(1); the ring-wave sits at kappa Phi'^2 / T = 1 exactly. The lab's
     theorist must say from GRV-020, EM-RECON-012 and EM-019 which form the registry holds, by quotation. If the
     registry is SILENT, the stability verdict is conditional on the form and the charter says so.
(ii) THE FAMILY. The static ring with twist at phase speed beta is a stationary solution for EVERY beta, at
     R^2 = kappa (1 + beta^2) / 2T with J = 2 pi kappa beta: a one-parameter family (Leg C's beta_p scan was a walk
     along it). The ring-wave at beta = 1 is one member. Its spectrum therefore has a neutral direction along the
     family (changing beta and R together at fixed winding), which is not an instability and must be projected
     out, or the question posed at fixed J, where the family is a point. Also the obvious zero modes: rotations,
     translations, the twist shift.
(iii) THE STATIONARITY CEILING for the dynamics: the polygon's equilibrium radius differs from the continuum's by
     O(M^-2) (3.6e-4 at M = 48), and a run started at the continuum radius breathes at that amplitude. A charter
     that perturbs the ring-wave by epsilon must start from the polygon's own equilibrium (as K3 does) and keep
     epsilon well above the O(M^-2) offset or well below it, stated which.

What the evidence run would be (NOT run here, and this file has no code path that runs it): the discrete
ring-wave at fixed kappa and winding, perturbed by a small-amplitude mode (n = 2, 3, ... in shape, and in the
twist's phase speed), integrated for tens of periods; the growth or oscillation of each mode amplitude read from
the sealed trajectory; the forms RING-STABLE / RING-UNSTABLE (with the rate and the mode) / NO-CALL fixed before
the run. Three values of kappa_tw as the Director's estimate says, though in these units kappa only sets R and the
question is scale-free; the real variable to scan is the perturbation's content (shape versus twist speed).

Section 5(a) is superseded by this section; 5(b) to (d) stand.

## 8. Part 2 addenda (2026-10-26, later): the gauge pin and the shape theorem seen dynamically
(a) THE SLIDING MODE. The arc-length gauge leaves one collective sliding of all nodes along the loop. In the
continuum it is pure gauge; the discrete Lagrangian gives it a tiny inertia through the twist's transport term,
and on perturbed data it ran away: on the beta = 0.5 family member with an n = 2 shape probe (M = 16) the node
speeds reached 16 c by t = 1 and Newton failed. It is now pinned by one holonomic constraint on node 0
((x_0 - centroid) . y = const), on by default. The pin exerts a torque at the discretization level: J drifts
1e-3 on fast generic data at M = 32 (K4, both pinned and unpinned now reported) and 1e-8 on the slow K5 probe.
J is therefore a bar on every run rather than an identity, and the unpinned K4 remains the demonstration that
the discrete symmetries are exact. The cleaner cure, the conformal gauge of the induced metric (where the twist
scalar decouples into a free wave and the sliding is fixed by the gauge condition itself), is noted for a later
version; it is not needed for a lock whose runs are slow and whose J bar is 1e-7.
(b) THE SHAPE THEOREM, DYNAMICALLY (K5). Leg C's theorem (g = 2 for ANY static shape with travelling twist)
has a dynamical face: the local balance kappa Phi-dot Phi' = T between the wave's momentum flux and the tension
holds at every point of any shape of the right length, so EVERY such loop is a stationary solution and shape
perturbations at fixed length are neutral at first order. On the beta = 0.5 member a radial n = 3 deformation of
epsilon = 1e-2 moved 1.4 epsilon^2 R over two periods (first order would be epsilon R, 70 times more). The
charter (analysis/RING_WAVE_STABILITY_charter_DRAFT.md) is written around this: the live question is the
twist-speed channel (W probes) and the length mode (R0); the shape probes test the second-order fate of a flat
valley, scored as NEUTRAL-HOLDS / DRIFTS / WOBBLES.
(c) ONE EVIDENCE-STATE CONTACT, disclosed: before the pin existed, the n = 2 shape probe at epsilon = 1e-2 was
started on the beta = 1 state at M = 16 and aborted by the sliding runaway at t = 1.28 (0.3 of a period). Nothing
about stability was read or readable from it; it is in the charter's disclosures for the reviewers to judge.
