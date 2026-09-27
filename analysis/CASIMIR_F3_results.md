# COMMISSION CASIMIR-F3 -- RESULTS (executed 2026-09-27, sandbox; charter analysis/CASIMIR_F3_charter_LOCKED.md)

Verdict computed once from the sealed outputs (analysis/casimir_f3_part1.npz,
analysis/casimir_f3_part2.npz) by benchmarks/foundations/casimir_f3_verdict.py; the
log is analysis/CASIMIR_F3_verdict.log. Instrument: benchmarks/foundations/casimir_f3.py.

## Forms rendered

    Q1  CAS-LEDGER-CONSISTENT
    Q2  CAS-IDENTITY-SHORT-RANGE

## Q1: the registered zero-point ledger predicts the measured Casimir force, given hbar

1a. Derivation (registry-only, three closures read at verdict level at lock): the medium
between two plates carries two transverse polarizations, isotropic and gapless at speed c
(FND-089 SHIN6 engine; FND-090 Derived: the homogenized acoustic tensor at the FND-088
angles is exactly isotropic, machine 2.6e-15); the dark longitudinal channel decouples from
matter at linear order exactly, so a plate imposes no boundary condition on it
(EM-RECON-011/012); the twist band is gapped at the strand mass scale (FND-STRAND-008), so
its plate term is exp(-2 m d), zero at any laboratory separation. Under the FND-109
convention (the half-sum of carried-mode frequencies, lattice-regulated), the plate energy
per area is therefore

    E/A = -pi^2 hbar c / (720 d^3),   F/A = pi^2 hbar c / (240 d^4)   [hbar imported per GRV-014],

with lattice corrections O((a_f/d)^2), of order 1e-20 at d = 100 nm. The excluded control
(the longitudinal channel pinned as if matter coupled to it) would add at least 0.707 of one
polarization's worth (c_L >= sqrt2 c), +35 percent on the two-polarization value: displayed,
not adopted, and already excluded by the percent-level measurements.

1b. Known-answer instrument (bar B0). The lattice ledger on the scalar cubic lattice with
Dirichlet planes, one polarization, hbar = c = a = 1, evaluated exactly per transverse
wavevector (half-sum minus the elliptic-integral bulk term minus the surface term; the
remainder matched an independent Fourier-remainder evaluation to 2.6e-10 in shakedown) and
integrated over the zone by polar Gauss-Legendre quadrature:

| d (sites) | E_cas d^3 / (-pi^2/1440) |
|---|---|
| 8 | 1.01312 |
| 12 | 1.00576 |
| 16 | 1.00323 |
| 24 | 1.00143 |
| 32 | 1.00080 |
| 48 | 1.00036 |

Fit E d^3 = C (1 + c2/d^2): C = -0.0068537 against the continuum -0.0068539, deviation
-0.003 percent (bar 1 percent); c2 = +0.839 (the lattice makes the force slightly stronger
at finite d/a, vanishing as (a/d)^2); the quadrature changed by 2e-9 relative under doubling
(bar 0.1 percent). B0 PASSES with three orders of margin; the instrument is credentialed.

Display: the SHIN6 wound slab (f = 1/5 member, 25 sites per layer, planes pinned, d = 12,
k_perp = 0) carries its lowest Dirichlet modes as pairs (0.2125/0.2178, 0.4193/0.4241,
0.6068/0.6162 in the engine's speed units, n = 1..3), two per n with a 2.5 percent split
inside SHIN6's registered 5 percent polarization bar, against the straight slab's exactly
degenerate pairs (0.2611, 0.5177); the singles (0.3627, 0.708) are the longitudinal-like
branch at speed ratio 1.7. The mode count is the count universality needs.

Tier verdict, applied mechanically (charter 3a): consistency-tier. hbar is imported at the
conversion to joules exactly where GRV-021/025 import it; QED predicts the same number; no
discriminator; no "hbar derived". Value: the scorecard row exists with a computed number and
the closures shown to be registered rather than assumed.

## Q2: the winding's rotation carries no plate force

2a. Derivation. The level-1 rotating-wave state (FND-130/131/132) is a classical
configuration: one frequency (sqrt2 pi c/a_f, above the transverse band, FND-166), constant
modulus (the material orbit at c on R_1), uniform energy per unit length (2.598 T0 per
coarse strand). The energy of a classical configuration is a LOCAL functional of the fields:
a plate that pins the coarse strand changes it within a boundary layer of fixed thickness
and nowhere else, so E(d) = e d + 2 E_surf + (terms periodic in d with the pitch) with no
term that is scale-free in d. The Casimir term is not local: it is the d-dependence of a
SPECTRAL sum over all carried modes, and a single-frequency state has no spectral sum.
Moreover the plate's registered coupling is to the coarse transverse field (winding charge,
EM-017..022), while the rotation is fine-level structure; at the registered couplings the
plate does not touch the rotation at all. Registered expectation before computing: NONE.

2b. Control (bar B2), exact energies. A chain carrying a fixed-frequency travelling helical
wave (constant modulus, the one-dimensional analogue of the level-1 state) has pins inserted
at 0 and d; the pinned segment's energy, conserved thereafter, was computed for 160 values of
d over three decades (10 to 1000 sites) at three pitches (5, 7 and 2 sqrt3 sites):

| run | e per site | boundary constant | max residual after extensive + boundary |
|---|---|---|---|
| helix, pitch 5 | 1.381966 | -1.072949 | 2.3e-13 |
| helix, pitch 7 | 0.753020 | -0.129531 | 1.6e-13 |
| helix, pitch 2 sqrt3 | 2.481237 | -2.721856 | 2.3e-13 |
| linear wave, pitch 5 (contrast) | 0.690983 | -0.459220 | 2.5e-01 bounded, period-average 1.1e-13 |

The helix residual is at machine noise at every d: E(d) is exactly extensive plus a
constant, for the reason the derivation gives (constant modulus makes the pinning cost
phase-independent). The linearly polarized wave, run as the contrast, shows what a
commensurability term looks like: bounded (0.25 in units of R^2), periodic in d with the
pitch, averaging to noise over one period, no secular part. Neither run has a term with
p <= 4 and a stable coefficient; B2 renders SHORT-RANGE, and in the registered (helical)
case NO TERM. Three-dimensional check: the SHIN6 wound slab's local bond sum is exactly
linear in d (93 per layer, residual 5e-15 relative), the three-dimensional structure creating
nothing the string lacks. B3 does not fire.

## Consequence: the corpus's two zero-points are distinct objects

The corpus uses "zero-point" for two things: (A) the spectral object, the FND-109 ledger's
half-sum over carried modes, which Sakharov induction (GRV-021/025) and the Casimir force act
on and which carries hbar by import; (B) the budget object, the dynamical share of the
vacuum's energy bill (FND-MATTER-041's window, FND-132's identity "the vacuum's zero-point
energy IS the winding's rotation"). This commission shows (B) does not produce the force
that (A) produces: they are not one object. Per the EM-020 precedent the collision is
flagged now and the riders below are drafted for the author.

The magnitude question, restated and NOT adjudicated here: per mode the ledger's zero-point
at the lattice scale is hbar c/a = 5.3e-10 J, while the cell's mechanical energy is
T0 a = 2.6e-14 J (T0 = 434 J/m, a = 6.0e-17 m); the ratio, 2e4, is the GRV-093 ratio of the
quantum area l_q^2/(4 pi alpha) to the cell cross-section, the same object in energy form.
That ratio is exactly what the fence's Task 1 owes; nothing here moves it.

## The fence's Task 1, restated in spectral form (charter 3c)

Supply, from the postulates plus the three priced grants, an energy per carried light mode
proportional to its frequency with one universal constant, epsilon(omega) = hbar omega / 2,
on the gapless transverse band. The forced rotating-wave state is not that object: it is a
single-frequency classical configuration with a local energy. The geometric form of the same
question is GRV-093's: what selects the quantum area over the cell cross-section, a factor
of order 1e4 to 1e5 cells. A theorem that the postulate set cannot supply it is full credit
(docs/technical/FUTURE_MODEL_PROMPT_one_fence.md).

## Riders (drafted here; APPLIED 2026-09-27 on the author's word, "Let's accept the grant with riders"; registered as FND-178)

FND-132: [RIDER (CASIMIR-F3, 2026-09-27): the identity "the vacuum's zero-point energy IS the
winding's rotation" is a BUDGET identity (the energy bill inside FND-MATTER-041's window).
It is not the spectral zero-point (the FND-109 half-sum over carried light modes) that
Casimir and Sakharov induction act on: a fixed-frequency, constant-modulus rotating state
has no scale-free plate term (analysis/CASIMIR_F3_results.md). The two zero-points are
distinct objects; the naming collision is flagged per the EM-020 precedent.]

FND-MATTER-041: [RIDER (CASIMIR-F3, 2026-09-27): the zero-point share window (< 0.889) is a
window on the vacuum's energy BUDGET; the spectral zero-point that the Casimir force
measures is a different object (see the FND-132 rider).]

STRATEGIC_TARGETS F3: EXECUTED. "Computable in principle" is removed from F3's face: the
coefficient is universality's, consistency-tier, and the mechanical identity does not carry
the force. F3's "strongest potential external confrontation" is therefore not one; the
external confrontation the wave arc still owns is Prediction 32's lower edge.

## NORTH_STAR scorecard row (to enter under "Also carried" when the file is renamed)

| Casimir force | pi^2 hbar c / (240 d^4) from the registered ledger, coefficient by
universality (CASIMIR-F3, consistency-tier) | hbar (imported, GRV-014) | the energy per
light mode: the wave arc's rotation does not supply it (CAS-IDENTITY-SHORT-RANGE) | Fence
Task 1 in spectral form |

Delta line for the next release: targets moved blocked to derived: 0; inputs retired: 0;
one input's retirement route stated more sharply (hbar); one naming collision flagged
before it collided.

## Named next-order

None chartered by this commission. The result points at the fence's Task 1 and at nothing
cheaper. CURRENT-AS-SPIN (chartered 2026-08-16, never run) remains the queued magnet-facing
item per docs/NORTH_STAR.md section 6.

## Shakedown notes (instrument, not physics; recorded before the verdict was read)

1. Part 1 ran once; the sealed file holds both the base and the doubled quadrature. The
   per-k remainder formula was checked against an independent Fourier-remainder evaluation
   (2.6e-10 relative) in a scratch run before the sealed run.
2. Part 2's period average was first computed on the log-spaced d grid, where a window of
   one pitch held a single point at large d and averaged nothing; it was replaced by a dense
   window of exactly one period of consecutive integer d (and the boundary constant taken
   over exactly one period at the top of the range) before the verdict script was run. Part
   2 was re-run three times for this; the helix residual, the bar-bearing number, was at
   machine noise (1e-13 to 3e-13) in every run; only the contrast display changed.
3. The wound-slab display at k_perp = 0 folds the 5 x 5 supercell's transverse modes into
   the listed spectrum; the pair structure is read on n = 1..3 only.
4. hbar appears in this commission only in the phrase "hbar imported per GRV-014" and in
   the measured target; no computed number contains it.
