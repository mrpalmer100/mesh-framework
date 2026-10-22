# COMMISSION ELEC-CURRENT-1 -- THE CHARGE CURRENT AND MOMENTUM DENSITY OF A ROTATING PHASE PATTERN, FROM THE REGISTERED DICTIONARY
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-22; a DERIVATION commission on the harness kit; the
# derivation does not exist; the committed terminus enters only at evidence time through the harness; the smoke
# runs on synthetic profiles only)

## 0. Why this, now
ELEC-G-2 (verdict G-OTHER, ELEC-102 provisional) measured the committed terminus's charge-to-energy second-moment
ratio: 1.8209 with the charge at the edge, 1.1149 with the charge following the profile, neither Dirac's 2 nor
the classical 1. That ratio is the gyromagnetic ratio only under two laws the charter had to list as unregistered
assumptions: CL1, momentum density = energy density carried round at the phase rate; CL2, charge current =
rho_q Omega r. The write-up also recorded the edge: Omega x* = pi in units of c, so a literal rigid rotation of
the terminus is superluminal beyond r = x* / pi, and whatever the pattern does there it is not material motion.
ELEC-FF-SUB-1 and SUB-2 died on the same gap from the other side: no registered law says what an incident
transverse wave couples to at the terminus. One derivation supplies both: the current and momentum laws of a
rotating PHASE pattern in a medium with no material points. This commission asks for that derivation and judges
it by checks fixed here, not by what ratio it yields.

## 1. The target
For a stationary, axisymmetric, rotating phase pattern of the registered two-strand medium, described in the
solver's variables (a radial profile f(r), its derivative f'(r), a phase advancing at rate Omega, winding q), derive
from the premises below:
  (T1) the momentum density p(r) (the quantity whose integral against r is the pattern's angular momentum),
  (T2) the charge-current density j(r) (the quantity whose half-integral against r is the magnetic moment under
       the registered dictionary, EM-016/EM-017),
each as an explicit functional of (f, f', Omega, q, r), with its treatment of the region r > c / Omega stated
(a cut, a saturation, a different law, or a proof that the pattern carries nothing there), and from them the
ratio G = (mu / L)(2 m / q) with m the pattern's energy over c^2. CL1 and CL2 are admissible OUTCOMES of the
derivation, not premises: a derivation that arrives at them must arrive at them from the premises and must say
what happens at the edge.

## 2. Premises (the only things the derivation may rest on) and forbidden inputs
- FND-006: Lorentz invariance of the wave sector fixes mu = T / c^2 (the inertia of the medium is its tension).
- FND-REL-002: no material points; no convective term; the wave equation is forced to Lorentz-invariant form.
- EM-019: the inertial term is the rate of change of a gauge label; a label's rate is observable, the label is
  not; the only two-derivative scalars are the registered stiffness and the inertial term (the locked bars there
  rule out the material-velocity shortcut).
- EM-008, EM-014: current is transported linking (no wind-up, continuity, closed loop are one condition); the
  screw mechanism transports linking and delivers power consistently with continuity.
- EM-016, EM-017 (with EM-018, EM-022): the field-tensor dictionary, unique up to gauge and one global scale:
  charge and current, (phi, A), F, (E, B), the Lorentz force.
- GRV-020: the internal azimuth, G = R x SO(2), one circle-valued Goldstone; winding = charge (corollary 1).
- EM-023: the orientation connection A = -rho kappa_0 (s x z); B is minus kappa_0 times the strand-direction flux.
- ALPHA-DE-CHAIN, as the definition of the pattern only: the EL-BVP solution of explorations/w_dressing_phase1c.py
  at k / T0 = 2, Omega = pi / x*, x* = e^{pi^2}, q = 1 (its numbers are not premises of the laws).
Forbidden: the measured electron g, mu_B, alpha, the Schwinger term; ELEC-102's numbers (1.8209, 1.1149) and Gate
2b's pi mu_B or 1 / pi as a target or a step; any constant chosen so that G lands on a value; any law whose form
is selected by what it gives on the committed terminus (the checks below are what select).

## 3. The sealed input
None. The committed terminus is recomputed by the harness at evidence time (five (r_min, tol) cells as in ELEC-G-2,
sealed before use); the derivation module never reads it.

## 4. The interface (benchmarks/lab/elec_current_1/derivation.py)
- STATUS, ASSUMPTIONS, OBSTRUCTION as in the derivation kind.
- momentum_density(r, f, fp, Omega, q, c): array on the harness's grid (the solver's measure dA = 2 pi r dr).
- current_density(r, f, fp, Omega, q, c): array on the same grid.
- EDGE: one of 'cut', 'saturate', 'law', 'none', with EDGE_NOTE one sentence; for 'cut' or 'saturate' the radius
  r_c at which it acts as a function of (Omega, c); for 'law' the functional form beyond r_c; for 'none' the
  premise that forbids content there.
- REDUCTIONS: the two registered cases the laws reduce to (section 5, C-2 and C-3), each as a claim id and the
  limiting form.
- DEPENDS: for each of f, fp, Omega, q, whether the two densities depend on it (the harness probes this).

## 5. The checks (locked here; numeric or symbolic; the harness evaluates everything)
C-1 Continuity: on a grid of axisymmetric patterns, the charge density implied by the current (through EM-008's
    one condition) is time-independent and div j = 0 to 1e-10 relative; Int rho = q to 1e-8.
C-2 Reduction to the screw current (EM-014): on a uniformly twisted two-strand helix rotating at Omega (the
    registered mechanism's own configuration, built by the harness from EM-014's parameters), current_density
    reproduces EM-014's transported-linking current to 1e-6 relative.
C-3 Reduction of the momentum density to the inertial term (EM-019): for a uniform phase rate on a flat profile,
    momentum_density reduces to the EM-019 inertial term's momentum (mu times the label rate, mu = T / c^2) to
    1e-6; and the shift symmetry holds: f -> f + const changes neither density (1e-12).
C-4 Causality: for r Omega > c the module's EDGE treatment is applied and the densities are finite; a module
    declaring 'none' must have both densities vanish identically beyond c / Omega; 'cut' or 'saturate' must give
    r_c = c / Omega to 1e-12; any infinite or non-finite value is a check failure.
C-5 Dependence probes (the kit): each of f, fp, Omega, q perturbed by 1e-3 relative on a synthetic profile; the
    measured dependence matches DEPENDS; densities that depend on nothing are a failure.
C-6 Gauge: the densities are invariant under the registered gauge freedom of the dictionary (EM-017: the
    potentials' gauge), tested by the harness's two representatives, to 1e-12.
C-7 Dimensional consistency: scaling r by lambda, Omega by 1 / lambda, f by lambda^a as the solver's scaling
    relations register (ELEC-074's size-linear, energy-cubic scaling), the integrated L and mu scale as the
    dictionary requires (L as energy x length^2 / c^2 x rate; mu as charge x rate x length^2), to 1e-10.
C-8 Negative controls, sealed first: (a) CL1 and CL2 written as laws with EDGE 'none' and no cut must fail C-4
    (they carry content beyond c / Omega); (b) a module whose densities ignore Omega must fail C-5; (c) a module
    returning the ELEC-G-2 second-moment construction directly must fail C-2 (it does not reduce to the screw
    current); (d) malformed metadata renders NOT-DERIVED without exception.
C-9 Evidence (last, after C-1 to C-8 are sealed): the harness evaluates the module on the five sealed terminus
    cells, computes L, mu, m, q and G per cell, requires the five G to agree to 1e-5 absolute, and seals them.

## 6. The harness and the verdict
Both on benchmarks/lab/_kit/labkit.py. Units: controls (C-8); credential of the harness's own constructions
(the helix of C-2, the flat profile of C-3, the synthetic profiles of C-5, each with a known answer); scan and
isolated evaluation of the module on the checks C-1 to C-7; the terminus cells (sealed solves); C-9. The smoke
run builds only synthetic profiles (Gaussian and polynomial f on a random grid) and a stub module under
benchmarks/lab/elec_current_1/scratch/; it never calls the terminus solver. The verdict script recomputes G from
the seals, decides the form, and prints as its last line the comparison of G with 2, 2.0023193, 1 and 2 pi at
5e-4 absolute, disclosed as the only place those numbers enter and with no bearing on the form.

## 7. Verdict forms, and what follows
  DERIVED              STATUS DERIVED, C-1 to C-9 met, ASSUMPTIONS empty: the current and momentum laws of a
                       rotating phase pattern are registered consequences of the dictionary, with the edge
                       treatment derived; G is then the terminus's gyromagnetic ratio and is registered as such,
                       whatever its value. If the derived laws are CL1 and CL2 with a derived cut, ELEC-102's
                       numbers become conditional no longer; if they differ, ELEC-102 stands as the second-moment
                       diagnostic it says it is and G supersedes it as the physical ratio.
  DERIVED-CONDITIONAL  As above with named registered assumptions (each a claim the chain needs and lacks; the
                       edge treatment stated as an assumption is the expected one).
  NOT-DERIVED          An unsuccessful attempt: the obstruction named (for instance: EM-019 fixes a momentum for a
                       label rate but the dictionary assigns no momentum to the pattern's rotation; or the
                       dictionary's current requires a two-strand linking the single-profile pattern does not
                       carry). Not a no-go.
  NOT-DERIVED-OPEN     Infrastructure: scan failed, deliverable absent after the attempt budget, a control or
                       credential unit failed.

## 8. Smoke discipline (binding on the drafting worker)
LAB_SMOKE=1 runs the controls and the credential on synthetic profiles with a stub module from scratch/, writes
the smoke checkpoint only, and prints no G. The terminus solver is not imported in a smoke run. A smoke run that
touches explorations/w_dressing_phase1c.py is a preview and is refused by the charter.

## 9. Budgets and disclosures
Harness cpu_hours 1 (five BVP solves at evidence time, minutes each; the checks are grid arithmetic); mem_gb 2;
the derivation attempt at the derive budget, two attempts; usd 30 for the commission. Disclosed: the author's
executor expects the derivation to be hard at the edge and to end NOT-DERIVED or DERIVED-CONDITIONAL on the first
attempt; that expectation is not a bar and appears nowhere in the checks. ELEC-102's numbers are known to everyone
and are forbidden as targets; the checks C-2, C-3 and C-4 are what tie the laws to the registry.

```lab
commission: ELEC-CURRENT-1
kind: derivation
target: "Strength of magnets row (the electron model) and the electron row's gate: the charge-current and momentum-density laws of a rotating phase pattern derived from the registered dictionary (FND-006, FND-REL-002, EM-008/014/016/017/019/023, GRV-020), with the superluminal edge treated, judged by reduction to the registered screw current and inertial term, continuity, causality, gauge and scaling; supplies the laws ELEC-102 was conditional on and the coupling law the form-factor line lacked; moves no number"
premises: [FND-006, FND-REL-002, EM-019, EM-008, EM-014, EM-016, EM-017, EM-018, EM-022, GRV-020, EM-023, ALPHA-DE-CHAIN, ELEC-074]
driver: benchmarks/lab/elec_current_1/driver.py
verdict_script: benchmarks/lab/elec_current_1/verdict.py
derivation_module: benchmarks/lab/elec_current_1/derivation.py
derivation_doc: analysis/lab/derivations/ELEC-CURRENT-1.md
instrument:
  - explorations/w_dressing_phase1c.py
  - benchmarks/lab/_kit/labkit.py
forms: [NOT-DERIVED, NOT-DERIVED-OPEN, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/elec_current_1_ckpt.pkl]
budget: {cpu_hours: 1, usd: 30}
mem_gb: 2
```
