# North Star: what the Mesh Programme is for

*Draft for the author's ratification, 27 September 2026 (registry 769, v3.31.0 plus
FND-170..177). Proposed home: docs/NORTH_STAR.md, listed read-first in HANDOFF so every
session opens on it. This page adds direction, not permission: bars, grants, kept
failures and the census stay exactly as they are.*

## 1. The goal, in the author's words

A physical model of nature that makes sense mechanically, with as few fitted parameters
as possible, that predicts what is measured: the weights of atoms, the gravitational
force, the strength of magnets. The Standard Model's formulas are accurate and its
parameter count is nineteen; its explanations of magnetism, electricity and gravity are
not intelligible as mechanism. The mesh must do better on intelligibility and on parameter
count without doing worse on accuracy.

Progress is measured by two numbers only: targets moved from blocked to derived, and
inputs retired by derivation. A registration that does neither is interior work. It may be
necessary; it is not progress on this page.

## 2. The scorecard (kept current at every release)

| Target | Derived today | Grade (2c) | Inputs it consumes | Blocked by | Nearest registered step |
|---|---|---|---|---|---|
| Weights of atoms | Nuclear masses C-12 to U-238 at 0.00 to 0.51% from bond counting (NUC-005/018); surface term derived from packing geometry (18% miss, NUC-016); Coulomb term derived from winding charge and spacing (+9%); OUT OF SAMPLE under bar W (NUC-BLIND-1, 2026-10-08, the author's draw): 0.12/0.22% of mass (three-term) and 0.011/0.026% (with the derived asymmetry a_A = 19.85, NUC-A/B) on 50 held-out isotopes, both BLIND-AGREES | D3 (whole-table, calibrated on Ca-40; the surface and Coulomb terms D2; blind-scored but not externally adjudicated) | The nucleon mass unit and m_e (PM-005, irreducible); one calibrated bond depth eps fixed on Ca-40 | Asymmetry and pairing need Fermi statistics, i.e. hbar; He-4 misses by 38% (zero-point); H-1 is inputs only; m_p/m_e = 1836 is spectrum-gated, not framework-bounded (FND-MATTER-066, kept) | Fence tests (b) and (c) below |
| Gravitational force | Newton's law forced by 3D elastostatics (GRV-005); weak-field metric, gamma = 1 and the PPN table (GRV-029); 1.751 arcsec deflection; SPARC g_dagger = cH0/2pi with zero parameters (GRV-030/031/033) | D0 (Newton's form, gamma = 1); D1 (g_dagger on SPARC); D3 (G itself, read from measurement) | Sigma (measured, FND-030); a (fixed at the M-point by m_e); G itself is read as the medium's rigidity c^4/4piG (GRV-006), with the Sakharov cutoff selected at Planck-class spacing (GRV-075/095) | The frame-dragging magnitude waits on the fine scale a_f (GRV-126, FND-110); G is not yet computed from a | Fence test (d) below |
| Strength of magnets | Maxwell's equations (EM-003) with a unique mechanical dictionary (EM-017..022); every electromagnetic magnitude locked to Sigma by kappa_0 = c/sqrt(eps0 Sigma) (FND-031, P31): fields of currents and forces between them follow | D0 (structure); D3 (magnitudes, Sigma measured) | Sigma | A permanent magnet's strength needs the electron's magnetic moment and exchange ordering: the electron model is unbuilt (the ELEC sector contributes nothing at any census tier; the spin-axis identification was falsified, ELEC-099/100) and both sit behind the quantum layer | COMMISSION CURRENT-AS-SPIN (chartered 2026-08-16); the electron model |
| Also carried | 1/alpha = 2 pi^2 rho^2 with rho = 2.6348 owed by one mechanism, blind, inside a +178.8 ppm fence (ELEC-083); the adjoint Casimir pin (FND-106, armed); the alpha-G drift ratio (PRED-003, clocked 2027 to 2030) | D2 (alpha's form, rho owed); D1 candidate (PRED-003, unadjudicated) | | | The alpha mechanism is the highest-reward item on the board and has no shape yet |
| Casimir force | pi^2 hbar c / (240 d^4) from the registered ledger, coefficient by universality on three registered closures (CASIMIR-F3, 2026-09-27; consistency-tier) | D3 (hbar imported) | hbar (imported, GRV-014) | The energy per light mode: the wave arc's rotation does not supply it (CAS-IDENTITY-SHORT-RANGE, FND-178, granted 2026-09-27) | Fence Task 1 in spectral form |

## 2b. The five numbers (adopted 4 October 2026; carried at the top of every release note)

The claim count measures reproducibility, not physics. These five measure the programme.
Each is read from a named page, so a release cannot move one by rewording.

| Number | Today | Read from | Direction wanted |
|---|---|---|---|
| Fundamental dimensional inputs | 6 (Sigma, a, d_c, the nucleon mass unit, eps, hbar) | Section 3 of this page | Down |
| Unexplained dimensionless constants | 4 named (alpha via rho = 2.6348; m_p/m_e; g = l_q/a; kappa_pack), plus every Standard Model coupling and ratio not yet on the board (SM_EMERGENCE row 11: none derived) | Section 3; docs/SM_EMERGENCE.md | Down |
| Imported physical laws | 1: the quantum layer (hbar as a constant, GRV-014; the guidance dynamics, QGATE-011). Isotropic elasticity's Poisson ratio is an imported constant, counted above | Section 3; SM_EMERGENCE row 12 | Down |
| Unique quantitative predictions (census T1) | 1 firm (PRED-003, the alpha-G drift ratio, clocked 2027 to 2030) and 1 armed pin (FND-106, the adjoint Casimir band) | ELEC-062/064; STRATEGIC_TARGETS section L | Up |
| Externally adjudicated predictions | 0. The k-string coefficient was adjudicated at its own pre-registered checkpoint and killed; that is self-adjudication, kept, and does not count here | WHERE_IT_STANDS | Up |

A release that moves none of the five is infrastructure, and its note says so in those words.
The Standard Model's structure is scored separately, in twelve rows, at docs/SM_EMERGENCE.md
(today 1 derived, 4 partial, 7 unexplained); a release that moves a row says which.

## 2c. Grades of "Derived" (adopted 4 October 2026 from external review)

The registry's Derived status covers results of different evidential weight. Every scorecard row
and every SM_EMERGENCE row carries a grade; the status field in claims.yaml is unchanged until a
reading commission re-grades the registry (named in STRATEGIC_TARGETS section Y, not chartered).

| grade | meaning | counts toward |
|---|---|---|
| D0 | a theorem: follows exactly from the axioms (A1, A2) and registered definitions, with no empirical input | SM_EMERGENCE "Derived" |
| D1 | a parameter-free physical derivation: an observable with no relevant empirical calibration, confrontable with data | the five numbers (predictions); "Derived" on the scorecard |
| D2 | a conditional derivation: exact given a registered mesh parameter or input that is itself unexplained (rho, w, f, hbar as an import) | nothing on the scorecard until the condition is discharged |
| D3 | a reconstruction: reproduces known physics using measured or calibrated quantities (whole-table fits, imported constants) | reproducibility; not evidence for the theory over the Standard Model |

D1 is the grade the North Star is for. Today the registry's D1 content is the SPARC g_dagger = cH0/2pi
(GRV-030) and PRED-003 pending adjudication, both filed as Modeled. The 121 Derived claims were graded on
7 October 2026 (docs/DERIVED_GRADES.md): 96 D0, 2 D1 (CHEM-GEO-002; GRV-031 by a lost confrontation), 18 D2,
2 D3, 3 not derivations. The Derived column is the model's mathematics; the evidence for the theory lives in the
handful of D1 rows, wherever their status field puts them. The machine side of the ledger
(tools/input_ledger.py, docs/INPUT_LEDGER.md) lists which benchmarks consume which measured
constants, so a D1 claim can be checked for a literal of the quantity it claims to derive.

## 3. The input ledger (the number to drive down)

| Input | Status today | Route to retire it | Gap (section 4) |
|---|---|---|---|
| Sigma, the vacuum stiffness | Pinned by measurement, 3.61 to 3.70e35 J/m^3 (FND-030) | None registered; kappa_pack (a floor, >= 50 or >= 250) would make it Sigma_vac | 1 |
| a, the mesh scale (equivalently m_e) | Fixed at the M-point, 6.0e-17 m (FND-MATTER-044); irreducibility theorem FND-MATTER-005 | Fence Task 2 | 1 |
| d_c, the strand thickness | Calibration, 1.87e-19 m (HBAR-005) | With a | calibration on the edge of 1 |
| The nucleon mass unit | Input (PM-005) | The 1836 road: kinetic/zero-point structure of the proton knot (FND-MATTER-066) | 5 |
| eps, the nuclear bond depth | One calibration, Ca-40 (NUC-005) | The one calibration the fence directive permits, unless the zero-point layer supplies it | calibration |
| hbar | Imported; the mesoscopic identification retired after six closures; ACTION-BRIDGE (FND-183, 2026-10-04): no registered mechanism bridges the snap action to it, and the postulates' only action carries two powers of a | Fence Task 1 restated: a pure number of order 1e21 from the registered Pi = 2 (2^70 and e^97 are the sizes; recorded as coincidences, not read), or an imported fork-invariant length; the LARGE-NUMBER slot is open and narrow | 1 |
| k/T0 = 2 | Adopted, theorem route closed (FND-129) | Re-opens only through GRANT-CONTACT's supersession clause | 1 (adopted) |
| The strand's Poisson ratio | Imported from isotropic elasticity | Moves gamma by a factor of a few, not orders | import |
| The contact convention (surfaces, not centre lines) | Adopted 2026-10-04 (FND-184, the fourth grant); replaces the centre-line convention of EM-RECON-023 | Retires into a theorem if a two-strand engine (Phase 2b) reproduces the period-pi dependence by itself | 2 |
| g = l_q/a | The single mesoscopic unknown (FND-044) | Whatever mechanism supplies rho = 2.6348 blind | 1 |

About ten named inputs, two of them (kappa_pack, g) not even pinned to a number. The
Standard Model's nineteen buy thousands of measured numbers at ppm precision; ours buy the
scorecard above. The count is not the point; the direction is.

## 4. Where every road goes: five gaps, one of them the fence

CLOSURE-MATRIX (2026-10-04; analysis/CLOSURE_MATRIX_results.md, the typed matrix in
analysis/closure_matrix.json) typed every registered relation between the programme's twenty
remaining primitives and its thirteen closure targets and counted the mutually independent gaps,
joining primitives only by registered identities and exponent laws, never by a blocked-by: FIVE.

(1) THE ACTION SCALE: hbar, a (m_e), T0, Sigma, g, alpha and the pure number N ~ 1e21 are one
class, joined by the constants ledger's identities (R1 hbar = T0 l_q^2/(4 pi alpha c), GRV-093; R2
G = c^3 a^2/(16 pi zeta hbar), GRV-095/075; the M-point, FND-MATTER-044), and that class is
registered as numerically inconsistent by seventeen orders (FND-MATTER-040) between the matter
sector's a = 6.0e-17 m and the Sakharov a = 1.3e-34 m. This is the fence of FND-BOUND-001 and
ACTION-BRIDGE: the four hardest residuals (frame-dragging magnitude, nuclear shell and pairing,
light-isotope masses, dispersion forces) name the zero-point layer that needs it, every scorecard
target is blocked behind it, and its next step is a primitive (a large-number mechanism from Pi, or
a fork-invariant length), not a computation.
(2) THE ON-SITE POTENTIAL V_0, with the kink width w, the junction fraction f and the contact
convention: the strand mass scale and FND-182's number depend on it and nothing else does; its
vacuum source is empty at the registered level (JUNCTION-LOCK, f = 0) and the fourth grant lives
in the matter sector.
(3) THE INTERNAL DIMENSION d: the gauge structure beyond U(1) depends on it and nothing joins it
to the rest (FND-185: one real dimension where SU(2) and SU(3) need three to eight).
(4) THE ELECTRON MODEL, blocked behind (1) and joined to nothing (ELEC-062).
(5) THE PROTON's topology, blocked behind (1) and joined to nothing (FND-MATTER-066).

Gaps 2 to 5 are not the fence under other names: no registered identity connects them to it, and
supplying the action scale would leave each of them where it is. Four more inputs (d_c, eps,
kappa_pack, the Poisson ratio) are calibrations and imports with no target depending on them:
things to retire, not gaps to close. Leverage is recorded in the results file and is not a queue.

The standing plan is docs/technical/FUTURE_MODEL_PROMPT_one_fence.md (v2, 4 August 2026):

- Task 1, the quantum of action: derive the bridge from the medium's derived snap action
  to hbar, or prove at theorem grade that this postulate set cannot produce it.
- Task 2, the absolute scale: derive a (equivalently m_e) from internal consistency, or
  sharpen its irreducibility into a theorem.
- Five pre-committed acceptance tests: (a) London C6 for two noble-gas dimers with zero new
  constants; (b) nuclear saturation at ~8.8 MeV with the A = 12 alpha periodicity;
  (c) H-2/H-3/He-3/He-4 residuals closed by derived zero-point energies; (d) the derived a
  as the Sakharov cutoff yielding measured G; (e) the measurement dividend, optional.
- One calibration across the entire programme, named before it is spent.

A theorem-grade no-go is full credit. It would mean the postulate set is insufficient and a
new primitive must be priced as a grant, which is a result, not a failure.

The fence's shape (ACTION-BRIDGE, FND-183, 2026-10-04): the postulate set {T0, a, c, Pi} has a
full-rank dimension matrix, so its only action is T0 a^2 g(Pi)/c, which carries two powers of
the lattice spacing where hbar carries zero. "Derive hbar" is therefore not a calculation waiting
to be done; it is a demand for a mechanism that manufactures a pure number of order 1e21 (at the
adopted Planck-class spacing) from the single coupling, with a then fixed by the result. Task 1
and Task 2 are one equation. Nothing registered does this (six candidates refused, blocked or
excluded at enumeration grade), and three roads (the bridge, the strand mass scale in eV,
FND-182's window) stop at one registered gap: nothing in the registry resists a strand's
azimuth at a contact (V_0 unsourced; FND-179 B). The two grants that would move the fence are
named: a cross-section-aware contact form; a candidate large-number mechanism from Pi.
[2026-10-04, evening: the first was adopted as the fourth grant, FND-184 (the contact acts on
surfaces). Night: the chain STRAND-MASS-SCALE, CROSSING-PRICE, NODE-STANDOFF, JUNCTION-LOCK found
that source EMPTY in the registered vacuum (crossings do not press, the junction is a point bond,
f = 0); the extension that would fill it is priced at f ~ 3.5 and not granted; FND-182 moved to T4.
V_0 is gap (2) above. The second grant is priced and open (Pi = 2 is registered and clean).]

The wave arc (FND-130..132, COMPOSITE-SELECT, the anti-aligned sector FND-172..177) is the
fence attacked from the vacuum side: zero-point energy read mechanically as the winding's
rotation, the rotating-wave state forced by three registrations. Its cash-out is F3: the
Casimir coefficient pi^2/240 computed from the boundary-modified winding spectrum, success
and failure pre-named (off by orders falsifies FND-132's mechanical identity). Until F3 is
computed, the wave arc has produced interior consistency only.

## 5. The rule (proposed amendment to STRATEGIC_TARGETS section C)

Before bars are locked, every charter names one of:

- (a) the scorecard target it moves, and how the verdict would move it;
- (b) the input it retires;
- (c) the discriminator it arms or adjudicates.

A charter that names none is interior work: at most one such session between
target-facing sessions, and never a lineage of them. An instrument fault is repaired to the
point where the pending verdict can be read, then the lineage stops. Every release note
carries the scorecard delta, including when it is zero.

Standing bar, blind hold-out (adopted 4 October 2026, STRATEGIC_TARGETS section W): in any
sector whose model carries a calibration or a fit against a measured table (today the
nuclear masses, NUC-005/018), the next confrontation holds out a pre-registered test set,
selected and sealed before the fit by a process other than the commission, and the
prediction is frozen before the held-out values are read. The locked charter names the
hold-out file by hash. Inspecting the whole table and fitting to part of it is no longer a
confrontation on this page.

## 6. The queue as of 27 September 2026 (proposed, author decides)

Delta since this page was written (2026-09-27, CASIMIR-F3): targets moved blocked to
derived 0; inputs retired 0; one retirement route (hbar) stated more sharply; one naming
collision (spectral vs budget zero-point) flagged before it collided. F3 is closed at this
instrument class; item 2 below is discharged.

Delta at the v3.32.0 cut (2026-10-04): targets moved blocked to derived 0; inputs retired 1
(the anti-aligned continuum family, FND-175 refuted on reproducibility); discriminators armed
0, the route to a third named (pin the strand mass scale in eV; collapses FND-182's window to
a number); one derived claim corrected on the record (GRV-045); one instrument retired (the
bordered kernel corrector). Casimir row: consistency-tier, hbar imported, zero fitted.

Delta 2026-10-04 (ACTION-BRIDGE, FND-183): targets moved 0; inputs retired 0; the hbar input's
retirement route restated from "a bridge to compute" to "a primitive to price", with the number
the primitive must produce written down (1e21 at F-SAK; 1e3 to 1e4 at F-LOR). One registered
gap (V_0) identified as blocking three roads at once.

1. Finish the two pending verdicts; the compute is sunk. NYQ-CONTROL on the PC decides
   whether FND-175/176/177 stand or become refute-and-keep. [DONE 2026-10-04: NYQ-CONTROL
   rendered CONTROL-FAIL; NYQ-CONTROL-2 rendered IRREPRODUCIBLE; FND-175 refuted and kept,
   FND-176/177 artifact records, FND-174 caution reopened. Input retired from "Also carried":
   the anti-aligned continuum family.] COMPOSITE-SELECT Leg B on the Mac is the composite
   build itself, which F3 needs. [Leg B still running at 11/7.]
2. Then F3: Casimir from the winding spectrum, pi^2/240 pre-named. The first external
   number the wave arc can produce, zero parameters. Charter to be written once Leg B seals.
3. In parallel on the PC: CURRENT-AS-SPIN, the magnet-facing commission already chartered
   and never run.
4. Then the fence, Task 1: the snap-action-to-hbar bridge, under the acceptance tests above.

Not chartered further: KERNEL-MARCH / KM-TURN successors. The bordered instrument is retired
(NYQ-CONTROL-2: conditioning-limited at the resonance, gates not reproducible from identical
inputs) and the lineage names no scorecard target. The kernel question stays open; a
credentialed route to it would start by gating a known member (FND-173) under any new
corrector before touching the resonance.
