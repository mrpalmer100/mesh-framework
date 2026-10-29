# The constants as constraints on mechanisms

Adopted by the author 29 October 2026; drafted by the executor. A companion to docs/SM_EMERGENCE.md row 11 and
docs/NORTH_STAR.md section 2b (the "unexplained dimensionless constants" number).

## 0. The rule this page lives under

This page uses the measured constants of the Standard Model and of gravity as INFORMATION ABOUT MECHANISMS and
never as targets. It records, for each parameter, what is known about its behaviour (how precisely it is known, how
it runs, what exact relations it obeys, what hierarchy it sits in, what it cancels against) and what KIND of
mechanism could produce a quantity that behaves that way. It then asks which registered mesh primitive, if any, is
of that kind.

Forbidden on this page and in any work that cites it: comparing a mesh-derived number with any value in the
tables below; searching for closed forms, integer relations or coincidences among the values; adjusting a mechanism
after reading a value. The numerology guard (ELEC-083), the no-hunt clause, the +178.8 ppm fence for rho and the
pure-numbers bar of NORTH_STAR section 2c (a dimensionless constant is D0 only as a proof-checked theorem with the
formalization sealed before the number is read) apply unchanged. The values are printed so the behaviour can be
stated exactly; a reader who finds a mesh number landing near one of them has found a hazard, not a result, and
files it as ELEC-083 filed the ratio test.

Why the page exists: guessing blindly is slow, and the constants are the universe's own description of what a
correct mechanism must do. A mechanism that produces a number of the wrong kind (a pure count where the quantity
runs; a linear ladder where the quantity spans six orders; a generic value where the quantity cancels to ten
decimal places) is wrong before any digit is compared. That test is free, it is blind, and the registry has never
run it systematically.

Values below are the executor's knowledge as of mid-2026 (CODATA 2022, PDG 2024 and later updates where known) and
are to be re-checked against the current CODATA and PDG tables at the next release; the behaviours are stable and
are what matters.

## 1. The ledger

Nineteen parameters of the Standard Model proper (three gauge couplings, two for the Higgs, nine charged-fermion
masses, four for the CKM matrix, theta_QCD), the neutrino sector beyond it (at least seven more), and the two of
gravity and cosmology. Grouped by behaviour, which is the useful grouping.

### 1a. The couplings (they run)

| Parameter | Value and precision | Behaviour the mechanism must reproduce | Kind of mechanism | Registered mesh primitive of that kind |
|---|---|---|---|---|
| alpha, electromagnetic, at zero momentum | 1/137.035999177(21) (CODATA 2022); the three most precise determinations disagree at the 5 sigma level among themselves (Berkeley Cs, Paris Rb, Northwestern g-2) | Runs: alpha(M_Z) about 1/127.95, logarithmically, with the QED beta function's coefficient set by the charged-particle content (vacuum polarization). Fixes the electron's anomaly through the Schwinger term alpha/2 pi and the full QED series, verified to 1e-13 in a_e. Charge is exactly quantized and exactly conserved | A dimensionless ratio of two stiffnesses or energies at a fixed geometry (a pure number) that is SCREENED: the effective ratio must depend on the scale probed because virtual pairs intervene. A count or a geometric ratio alone cannot run; a mechanism that gives alpha(0) and no q^2 dependence is incomplete at the first test | 1/alpha = 2 pi^2 rho^2 with rho the one mesoscopic unknown (FND-044; ELEC-083): a geometric ratio, the right kind at zero momentum only. Running requires a polarizable vacuum of winding pairs with the electron's threshold and Fermi statistics, i.e. gap 4 plus the quantum layer; the running measured through the lattice scale (hbar c / a about 3 GeV) is a second witness to the FND-REL-004 tension (analysis/RHO_RUNNING_reading.md, 2026-10-29). No rho mechanism is complete without a statement of what runs |
| alpha_s, strong, at M_Z | 0.1180(9) | Asymptotic freedom (grows toward low energy); dimensional transmutation: a pure number at one scale becomes a SCALE, Lambda_QCD about 200 MeV, which sets the proton mass; confinement | A coupling whose running has the opposite sign to QED's, which in field theory needs self-interacting carriers (non-abelian). A mechanism must produce a scale from a dimensionless number by exponentiation (Lambda = mu exp(-c / alpha_s)) | None. The registry has no SU(3) (FND-185, JOIN-SYMMETRY, THICK-ROPE-SYMMETRY readings) and models nuclear binding by bond counting without quarks (NUC-005/018, calibrated on eps). The proton mass is an INPUT (PM-005). Whatever the nucleon mass unit is in the mesh, it must be a transmuted scale, not a Yukawa |
| sin^2 theta_W, the weak mixing angle | 0.23122(4) in the MS-bar scheme at M_Z | Runs; M_W / M_Z = cos theta_W at tree level with the rho parameter 1.0004 (custodial symmetry: the Higgs is a doublet, not something else). G_F fixes v = 246.22 GeV | A ratio of two couplings g' / g of two different gauge factors; a mechanism needs both factors and a reason for their ratio (in unification it is a group-theory number at a high scale, 3/8, run down) | None (EW-001 Failed, kept; FND-185: no SU(2) seed). The one registered handedness effect is electromagnetic birefringence (EM-006) |

### 1b. The Higgs sector (a scale and a near-criticality)

| Parameter | Value | Behaviour | Kind of mechanism | Mesh primitive |
|---|---|---|---|---|
| v, the electroweak scale | 246.22 GeV (from G_F) | Sets every fermion mass through Yukawa couplings; the hierarchy v / M_Planck about 2e-17 is unexplained and radiatively unstable in field theory | A condensate scale: something must condense, and the scale of condensation must be insensitive to the highest scale in the theory, or the two scales must be tied | The M-point: a = 6.0e-17 m fixed by m_e (FND-MATTER-044). The mesh ties the electron's scale to a lattice length by calibration; it has no condensation and no separate electroweak scale |
| m_H, and the quartic lambda | 125.20(11) GeV; lambda about 0.129 at M_Z | lambda runs DOWN and passes near zero around 1e10 to 1e11 GeV: the vacuum is near-critical (metastable or at the edge). The top Yukawa drives this | A self-coupling whose running takes it near zero at a high scale: a mechanism that produces lambda must produce the near-criticality, which smells like a boundary condition at a high scale rather than a low-energy accident | None |

### 1c. The fermion masses (a hierarchy and one exact relation)

| Parameter | Value | Behaviour | Kind of mechanism | Mesh primitive |
|---|---|---|---|---|
| m_e, m_mu, m_tau | 0.51099895000(15), 105.6583755(23), 1776.93(9) MeV | KOIDE: (m_e + m_mu + m_tau) / (sqrt m_e + sqrt m_mu + sqrt m_tau)^2 = 0.666661(7), i.e. 2/3 to 1e-5, for the POLE masses. Ratios mu/e = 206.77, tau/mu = 16.82: not a geometric ladder | Three masses that are squares of three amplitudes whose vector (sqrt m_1, sqrt m_2, sqrt m_3) sits at 45 degrees to (1, 1, 1): that is what Koide says, exactly. A mechanism in which mass is the square of an amplitude and three generations are three components of one object with that angle fixed by geometry would produce the relation blind; one that produces three masses separately and hits 206.77 without Koide is a fit | Mass as mode energy (PM-005) is a square of an amplitude already, the right kind; FND-185's S_3 families hold the Z_3 a one-object triplet needs; the open condition is a geometric reason for the triplet's modulation ratio sqrt 2, with the phase left to the mechanism and never read from the masses (analysis/KOIDE_KIND_reading.md, 2026-10-29). PM-001 (Failed, kept) is the registered example of the wrong kind. A proposal that builds the muon and tau as separate objects is declined on sight |
| m_u, m_d, m_s (MS-bar, 2 GeV) | 2.16(7), 4.70(7), 93.5(8) MeV | m_u < m_d (proton lighter than neutron; the hydrogen atom stable); m_d / m_u about 2.2; m_s / m_d about 20. Isospin is a good symmetry because both are small against Lambda_QCD, not because they are equal | Two light masses of the SAME order but NOT equal, with the lighter carrying the larger charge magnitude ratio (2/3 against 1/3). A mechanism giving m_u = m_d (Chain Theory's "up/down = 1") fails the stability of hydrogen | None registered. NUC-003 (fractional sub-knots) is Open |
| m_c, m_b, m_t | 1.273(5) GeV, 4.183(7) GeV, 172.6(3) GeV (pole) | The Yukawas span y_u about 1e-5 to y_t about 0.99: SIX orders, roughly geometric by generation within each charge, with y_t of order one (the top is the only fermion coupled at full strength). m_b / m_tau is about 2.4 at low energy and near 1 at high scales | Exponential sensitivity to an integer or to an overlap: mass proportional to exp(-n) or to the overlap of two localized profiles, with the generation index n or the separation entering the exponent. A linear or polynomial ladder cannot span six orders with small integers | FND-110's ladder is multiplicative between LEVELS (a, a_f, the rope), the right kind for hierarchies between sectors; nothing registered gives a ladder WITHIN a sector (generations) |

### 1d. Mixing (two matrices that look nothing alike)

| Parameter | Value | Behaviour | Kind of mechanism | Mesh primitive |
|---|---|---|---|---|
| CKM: lambda, A, rho-bar, eta-bar | 0.2250(7), 0.826(12), 0.159(10), 0.348(10) (Wolfenstein) | Nearly the identity, hierarchical in lambda: V_us about lambda, V_cb about lambda^2, V_ub about lambda^3. One CP phase; the Jarlskog invariant J = 3.1e-5 is small. The empirical Gatto-Sartori-Tonin relation tan theta_C about sqrt(m_d / m_s) holds to 10 percent: the Cabibbo angle knows the light-quark mass ratio | Mixing as OVERLAP between generation structures that are nearly orthogonal, with the overlap tied to the mass hierarchy (small mass ratio, small angle). CP violation needs a phase that cannot be rotated away: at least three generations and a complex structure in the mechanism | None. The registry's vacuum is P-even (FND-185) and NOTHING registered violates CP: the mesh has no seed for J or for the baryon asymmetry. Constraint, stated as a tension to keep: a mesh that stays CP-even predicts J = 0 and no baryogenesis |
| PMNS: theta_12, theta_23, theta_13, delta | 33.4, 49, 8.6 degrees (within a degree or two); delta poorly known | LARGE angles, nothing like the CKM; near "anarchy" or near tribimaximal; the two mass-squared splittings 7.4e-5 and 2.5e-3 eV^2 differ by a factor 34 only (a MILD hierarchy against the charged fermions' six orders); the absolute scale below 0.1 eV (cosmology), the ordering (normal or inverted) and the Dirac or Majorana character unknown | The same overlap mechanism with nearly DEGENERATE inputs gives large angles: the contrast CKM-small, PMNS-large is the single strongest structural fact in the flavour sector and says the neutrino mass mechanism is a different kind from the charged one (a seesaw, a Majorana mass, a scale far above v) | None |

### 1e. The cancellations (numbers that are zero or nearly so)

| Parameter | Value | Behaviour | Kind of mechanism | Mesh primitive |
|---|---|---|---|---|
| theta_QCD | below 1e-10 (neutron electric dipole moment) | Could be anything in [0, 2 pi) in the Standard Model; is zero to ten decimal places while the CKM phase is order one. The strong CP problem | A symmetry (P or CP exact in the strong sector), a relaxation (an axion field whose minimum is at zero), or a massless up quark (excluded by lattice QCD). A generic mechanism assigns theta a generic value and is wrong at once | FND-185: the registered vacuum is P-even with inversion acting on windings as charge reversal. A P-even medium naturally gives theta_QCD = 0: the ONE constraint in this table the mesh meets for free, and it meets it for the same reason it fails CKM's phase (no CP violation anywhere). The two facts are one fact |
| Lambda, the cosmological constant | rho_Lambda = (2.26 meV)^4, about 5.4e-10 J/m^3; in Planck units about 1e-122; Omega_Lambda = 0.685(7) | Positive, tiny against every particle-physics scale (the Higgs condensate alone contributes 1e55 times more in field theory), and of the same order as the present matter density (the coincidence problem). Dark energy's equation of state w = -1 within a few percent (DESI 2024-2025 hints at evolution, not settled) | A cancellation to 120 decimal places, or a mechanism in which vacuum energy does not gravitate, or a relaxation. A mechanism that computes Lambda from its own vacuum energy gets 1e120 unless it says why that energy is not a source | Does not gravitate, by construction: GRV-004 (a uniform network of any tension density is flat; only deviations source) covers Sigma and the mode bath's mean zero-point stress alike, and under GRV-029's dictionary the induced channel's a^-4 volume term (the m^3 locus GRV-028/029 left unaddressed) is the same uniform prestress, hence flat (analysis/SIGMA_LAMBDA_reading.md, 2026-10-29). Price: homogeneity on cosmological scales. Consequence of kind: an observed cosmological term is a deviation (a tension gradient or drift, PRED-003's channel), a relaxation and not a vacuum energy, so w is not exactly -1; its size is unchartered |
| G, Newton's constant | 6.67430(15)e-11; M_Planck = 1.22e19 GeV; M_Planck / v about 5e16 | Known to 2e-5 only (the worst-measured constant); the hierarchy against v is the other face of the Higgs problem; PRED-003 ties its drift to alpha's | A rigidity of the medium: G as c^4 / (4 pi x rigidity) (GRV-006). The hierarchy is then a ratio of two stiffnesses or of two lengths | GRV-006/075/095: G read as the medium's rigidity with a Planck-class cutoff; D3 (G read from measurement). The ratio M_Planck / v would be, in the mesh, a / l_Planck or Sigma against a matter stiffness: a stated route, not derived |

### 1f. Not parameters, but constraints of the same kind

- Charge quantization and anomaly cancellation: the hypercharges of one generation are the unique rational set that
  cancels all gauge anomalies; charges are integers in units of e/3. The mesh has the integer (FND-008) and no
  thirds (NUC-003 Open).
- Three colours: from the R ratio and pi0 to two photons; the mesh has no colour.
- Three generations, no fourth light one (Z width); the mesh scopes generations out (PM-005).
- Lorentz invariance to 1e-20 and better in some channels; the mesh's (ka)^2 dispersion bound a <= 9.3e-28 m
  (FND-REL-004) is in registered tension with a = 6.0e-17 m from the matter sector. Kept, not resolved.
- The electron's anomaly a_e to 1e-13 and the muon's to 2e-10 (the 2025 Standard Model prediction with lattice
  hadronic vacuum polarization is consistent with the Fermilab measurement; the earlier 4 to 5 sigma discrepancy
  rested on the data-driven HVP and is no longer the headline): any mechanism for alpha must reproduce the QED
  series structure, not just its first term.
- The baryon asymmetry eta = 6.1e-10: needs CP violation and departure from equilibrium; the mesh has neither
  registered.

## 2. What the ledger says, read as a whole

1. The mesh's primitives are of the right KIND for exactly two entries: alpha at zero momentum (a geometric ratio)
   and the inter-sector hierarchies (a multiplicative ladder). They are of the wrong kind, or absent, for the running
   of any coupling, for SU(2) and SU(3), for mixing, for CP violation, and for the Higgs sector. The registry's
   SM_EMERGENCE tally (1 derived, 4 partial, 7 unexplained) says the same thing in different words; this page says
   WHY, entry by entry, in terms of the behaviour each quantity has.
2. Two constraints are met for free and should be written down as such: theta_QCD = 0 from a P-even vacuum, and
   charge quantization from winding. The first is paid for by the absence of CP violation, which the CKM phase and
   the baryon asymmetry then charge back. Keep both faces.
3. Three free tests were named here on 29 October 2026 and read the same day (analysis/SIGMA_LAMBDA_reading.md,
   RHO_RUNNING_reading.md, KOIDE_KIND_reading.md): Sigma does not gravitate on either registered face and the
   induced channel's cosmological locus is discharged for a homogeneous medium, with the observed term then a
   relaxation; rho cannot run without the electron, the quantum layer and Fermi statistics, and the measured
   running through the lattice scale is a second witness to FND-REL-004; Koide fixes the SHAPE of any generation
   mechanism (one Z_3 object, mass the square of an amplitude, modulation sqrt 2 by geometry) and the registry holds
   the first two pieces.
4. The flavour sector's structure (hierarchical masses with small quark mixing, mild neutrino hierarchy with large
   mixing) is the richest information in the table and the mesh has no object to receive it. A three-generation
   object that is one thing with three components (Koide's geometry) is the shape any proposal must have.

## 3. How this page is used

A proposal for a mechanism cites the rows it claims to address and states, before any computation, how its output
BEHAVES against the behaviour column: runs or not, exact relation or not, exponential or polynomial in its integer,
generic or cancelled. A proposal whose kind is wrong is declined on that ground without a number being computed.
A proposal whose kind is right proceeds under the ordinary bars. The values column is never cited in a charter.
