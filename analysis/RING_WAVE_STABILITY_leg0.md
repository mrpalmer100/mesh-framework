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

## 6. Status
Instrument credentialed on K1 to K4 for the shape-stability half of the commission; the dynamical half has no
instrument yet. The evidence cell is untouched. Nothing here is a result about the ring-wave.
