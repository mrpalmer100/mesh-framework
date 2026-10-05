# Five Mesh Challenges

*Adopted 4 October 2026 on the author's word, from an external review's recommendation to invite
adversarial testing. Each challenge names one load-bearing derivation, the claims it rests on, the
frozen inputs, the one-command reproduction, the bar that counts as a found mistake, and what the
programme retires if the bar is met. Submissions by issue on the repository; see the last section.*

## What a challenge is

Each challenge names one load-bearing derivation, the registered claims it rests on, the
frozen inputs, the code that reproduces it from the repository as cloned, the bar that counts
as a found mistake, and what the programme retires if the bar is met. The invitation is to
break the derivation, not to improve it. A challenger who meets a bar is credited in the
registry by name on the claim that falls (the registry already keeps its failures; FND-175 is
the most recent), and the retirement is carried out under the house rules: the claim moves to
Failed and is kept, every dependent claim takes a rider, and the release note says so.

Reproduction is one command per challenge, with the environment of docs/WINDOWS_COMPUTE.md
or the Unix equivalent (`pip install numpy scipy sympy pyyaml`). Every challenge runs on a
laptop in minutes except Challenge 4, which replays a frozen checkpoint.

A challenge is not met by an alternative theory that also fits, by a complaint about
notation, or by pointing out something the registry already records as a limitation
(KNOWN_LIMITATIONS.md and docs/SM_EMERGENCE.md list those). It is met by a demonstrated
error in the derivation, a hidden calibration, or a numerical artefact in the result.

## Challenge 1: the homogenisation behind the vacuum stiffness (for condensed-matter theorists)

The claim. The weave's coarse-grained elasticity has one stiffness, Sigma, pinned to the
lattice band 3.61 to 3.70e35 J/m^3 (FND-030, COMMISSION MU), and every electromagnetic
magnitude is locked to it through kappa_0 = c/sqrt(eps0 Sigma) (FND-031, COMMISSION NU). The
coarse-graining from strands to continuum is in papers/_sources/rope_microscopic_mechanics
(the factor-of-three audit is inside it) and rope_renormalization_eft.

Frozen inputs. The strand tension T0 and spacing a on the registered degeneracy line
(docs/ROPE_PARAMETERS.md); the two-strand rope (ontology A2); the registered Poisson ratio
import (KNOWN_LIMITATIONS).

Reproduce. `python benchmarks/foundations/nu_downstream_sweep.py` (FND-031's sweep, both band
edges) and `python benchmarks/em/dalet2_sigma_provenance.py` (the provenance chain).

The bar. Show that the continuum limit of the registered weave does not have the elastic
form the papers assign it (a missing term at leading order, a wrong symmetry class, a
dependence on the coarse-graining cell that the audit missed), or that Sigma's pin to the
lattice band rests on a quantity that is itself calibrated to an electromagnetic measurement
(a circular pin).

What falls. FND-030 and FND-031 move to Failed; the magnitude column of the Maxwell dictionary
(EM-017 to EM-022) loses its scale; NORTH_STAR row "Strength of magnets" returns to blocked.
The structure of Maxwell's equations (Challenge 2) does not depend on this.

## Challenge 2: gauge emergence (for field theorists)

The claim. Maxwell's equations follow from the Bianchi identities, Chern-Weil and d = 3
(EM-003); gauge invariance is forced by phase-convention arbitrariness (GG-004); the
field-tensor dictionary is unique up to gauge and one global scale (EM-017: any mechanical
assignment predicting the same force on every test winding at every velocity yields the same
E and B pointwise); the potential's channel is forced by elimination over the closed
inventory of registered mechanical channels (EM-018) and the inertial term's form by the
symmetry that forbids the mass term (EM-019). This is the one Derived row of SM_EMERGENCE.

Frozen inputs. Ontology A1 and A2; the registered operational definition of E (force per
winding, EM-015 / EM-RECON-024); the channel inventory as listed in EM-018's benchmark.

Reproduce. `python benchmarks/em/em_structure.py`, `python benchmarks/em/aleph2_dictionary_uniqueness.py`,
`python benchmarks/em/bet2_phi_channel.py`, `python benchmarks/em/gimel2_inertial_term.py`.

The bar. Exhibit a second mechanical assignment that reproduces every registered test-winding
force and gives a different (E, B) (uniqueness fails); or a registered mechanical channel
outside EM-018's inventory that can carry the potential (elimination fails); or show that the
Chern-Weil step uses U(1) structure as an input rather than deriving it from the winding
topology (the derivation is circular).

What falls. The U(1) row of SM_EMERGENCE moves from Derived to Partial or Unexplained;
EM-003/EM-017 take Failed status; the scorecard's one derived structural row is gone.

## Challenge 3: the weak-field metric and the galactic acceleration scale (for relativists and astronomers)

The claim. The gapless transverse mode's wave operator carries exactly four coefficient
functions, a static metric carries exactly four, and the map between them is forced, giving
the weak-field metric with gamma = 1 and the full PPN table unconditionally (GRV-029, the
one-metric derivation); Newton's law and the Poisson equation are forced by 3D elastostatics
(GRV-005); the four classical tests take their GR values (GRV-002: 1.751 arcsec, 43.0
arcsec/century, Shapiro, redshift). Separately, g_dagger = cH0/2pi = 1.083e-10 m/s^2 at zero
free parameters sits 4.5 percent from the SPARC-fitted value on 155 galaxies (GRV-030; the
hierarchical M/L re-reading GRV-033 is registered and kept).

Frozen inputs. The transverse wave operator as registered (FND-STRAND-001); H0 as imported
and named in GRV-030's benchmark; the SPARC Rotmod_LTG data shipped in data/sparc_rotmod.

Reproduce. `python benchmarks/gravity/one_metric_physical.py`, `python benchmarks/gravity/zero_point_and_poisson.py`,
`python benchmarks/gravity/sparc_rar_confrontation.py`, `python benchmarks/gravity/rar_hierarchical_ml.py`.

The bar. Show that the four-coefficient counting admits a second metric map consistent with
the same wave operator (gamma is not forced); or that the Poisson equation needs an input
beyond 3D static force balance; or, on SPARC, that the 4.5 percent agreement depends on a
choice (quality cut, M/L convention, H0 value) that the benchmark fixed after seeing the data.

What falls. GRV-029 and GRV-002 to Failed and the "Gravitational force" row of the North Star
scorecard returns to blocked; or GRV-030 to Failed and the SPARC line leaves the scorecard.
The two parts are independent and may be met separately.

## Challenge 4: the solvers (for numerical analysts)

The claim. The registered anti-aligned two-frequency members and the families marched from
them (FND-173, FND-174; FND-170 to FND-172, FND-176, FND-177) were gated by a sparse
Gauss-Newton corrector at RMS below 1e-8 with closure below 1e-11 on 144x36 and 288x36 charts.
The programme has already retired one corrector from this lineage: the bordered continuation
of FND-175 gated members that did not reproduce from bit-identical inputs (NYQ-CONTROL-2:
predictor step differed by 40 percent, the bordered solve at lam 1e-9 against sigma^2 ~ 1.5e-9
is conditioning-limited; FND-175 Failed and kept; the Fault-13 signature recorded). The open
question is whether the surviving members are gates or artefacts.

Frozen inputs. The frozen 09-16 corrector `benchmarks/foundations/kernel_continuation_0916.py`
(sha256 bfe24d2d2b1b3250c8b4f0ec22ae2bc78032f62c11f840eb16b6af82c5e92009); the sealed
checkpoints in analysis/ (kernel_march_ckpt.pkl, nyq_control_ckpt.pkl, nyq_control_v3_ckpt.pkl)
with phase and point counts only readable from them; the sparse-Jacobian instrument
`benchmarks/foundations/sparsej_instrument.py`.

Reproduce. `python benchmarks/foundations/nyq_control_2_verdict.py` and
`python tools/nyq2_forensics.py` (the irreproducibility, from the sealed checkpoints);
`python benchmarks/foundations/antiarc_nyq_verdict.py` once ANTI-ARC-NYQ completes (the
registered family re-marched under a Nyquist bar, wsNyq <= 1e-4).

The bar. Show that a gated member of FND-173 or FND-174 is a discretisation artefact: that its
residual floor moves with the chart (144x36 to 288x36) in a way the registered convergence
claim excludes, that the Nyquist-band weight wsNyq of a gated member exceeds the 1e-4 bar
(the ANTI-ARC-NYQ control c1 is already expected to fail this, and the charter says so), or
that the sparse Gauss-Newton gate at RMS 1e-8 is reachable by a spurious solution of the
discretised operator with no continuum counterpart.

What falls. FND-173/174 to Failed and the anti-aligned sector's input retirement reverses;
FND-176/177 take riders as artefact records. This is the challenge most likely to be met,
and the programme says so: it has already lost one solver here.

## Challenge 5: the sole firm prediction (for anyone with a clock)

The claim. PRED-003: d ln alpha = -2 d ln G, the coupling-drift ratio, with both couplings
expressed in the same medium primitives (alpha from the medium's locking chain, G as the
medium's rigidity c^4/4piG, GRV-006), the -2 reassigned to the spacing channel by
PRED-003-LOCK (the registered model has no on-site locking; kappa is enslaved by two
registered claims), and the constitutive derivation of e_eff^2 in PRED-003-CONST. It is the
programme's one census-T1 prediction (ELEC-062/064), confronted and surviving at 1.74 sigma,
clocked 2027 to 2030 on the Yb+ E3/E2 clock and the quasar many-multiplet determinations.

Frozen inputs. The chain's primitives as registered (T0, a, kappa = 2T/(eta a) with eta = 1,
FND-044; Pi = 2); no measured alpha or G enters the ratio.

Reproduce. `python benchmarks/foundations/pred_alpha_g_drift.py`, `python benchmarks/foundations/pred003_locking.py`,
`python benchmarks/foundations/pred003_constitutive.py`.

The bar. Find a step in the chain where a measured value of alpha or G, or a quantity fitted
to one, enters the -2 (a hidden calibration makes the ratio a fit, not a prediction); or
show that the two couplings' dependence on the spacing channel is not as the chain states
(the exponent is not -2); or show that the registered medium admits a second drift channel
the chain does not account for (the ratio is not unique).

What falls. PRED-003 moves from T1 to T4 or Failed; the fourth of the five numbers
(NORTH_STAR 2b) goes to zero firm, one armed pin; the programme has no prediction nature can
choose over the Standard Model's until another is built.

## How to submit

A challenge is met by a reproducible demonstration: a script or notebook against the
repository at a named commit, with the bar it meets stated. The author adjudicates against the
bar as written here, not against a judgment of importance, and records the outcome in the
registry either way (a challenge that fails to meet its bar is recorded too, as a confrontation
survived, with the challenger credited). Submissions by issue on the repository.
