# Rope Parameters — the canonical card

*Every quantity that describes a strand in this framework, with its status,
provenance, and value. Compiled 1 August 2026; revised 7 August 2026 (M-point
promoted); revised 10 August 2026 (Σ pinned per FND-030, branch structure
retired to historical, κ₀ added per FND-031); **revised 17 August 2026 (§6
added: the fine level after the BLOCH-L arc — dynamical mapping, contact-free
grant, KBSAT executed, the winding as a rotating wave)**.*

**Read this before any session that uses a rope constant.** Values are verified
by `benchmarks/foundations/rope_parameter_card.py`, which recomputes every
derived relation and fails if the card drifts from the registry.

---

## The short version

A strand is a **thin, framed, very stiff but EXTENSIBLE rod** under tension, with
**no material points**. It has:

- **two independent lengths** — the spacing between strands, and the strand's own
  thickness — and the ratio between them is ~1000, which matters more than it
  looks;
- **one stiffness scale**, the vacuum stiffness Σ — **now pinned by
  measurement to 3.61–3.70e35 J/m³** (FND-030) — from which the tension
  follows;
- **a frame**, giving it twist and torsional rigidity — it is a rod, not a string;
- **two postulates rather than numbers**: near-inextensibility (a *limit*, not an
  exact property — see below), and no material points.

**On "inextensible" — the word is a trap and the card used to fall in it.** The
strand *does* stretch. It must: a perfectly rigid strand carries no longitudinal
wave, and the framework's entire superluminal channel **is** a longitudinal wave,
with c_L/c = √(k/T₀). Inextensibility is the k → ∞ idealisation, useful for
deriving the tension's role and wrong if taken literally.

Everything else is derived.

---

## 1. The independent quantities

| Quantity | Symbol | Pinned band | Historical Σ-route (demoted) | Status | Source |
|---|---|---|---|---|---|
| Tube tension density | Σ_eff | **3.61–3.70e35 J/m³** | 5.10e35 J/m³ | **pinned by measurement** | ELEC-052/081, FND-030 |
| Vacuum stiffness | Σ_vac | Σ_eff·κ_pack, **κ_pack ≥ 50 (5% CS) / ≥ 250 (continuum)** | — | Conjecture-grade floor, conditional on FND-037 | FND-037/040 |

**M-point as a function of κ_pack** (m_e-pinned solve a = (3K/Σ_vac)^⅓, T₀ = K/a,
K = 2.6065e-14 J; the v3.16.1 M-point a = 6.0e-17 m, T₀ = 434 J/m is the κ_pack = 1 row):

| κ_pack | Σ_vac [J/m³] | a [m] | T₀ [J/m] | Lorentz margin | l_q/a |
|---|---|---|---|---|---|
| 1 (historical) | 3.61e35 | 6.00e-17 | 434 | 1.7× | 43.0 |
| 50 (5% CS floor) | 1.81e37 | 1.63e-17 | 1599 | 6.1× | 82.6 |
| 250 (continuum floor) | 9.03e37 | 9.53e-18 | 2734 | 10.5× | 108.0 |
| EM normalization | κ₀ | **1.66–1.68e-4 m³/(s·C)** | ≤ 26–50 (stale bound, superseded) | derived: κ₀ = c/√(ε₀Σ) | EM-RECON-027/029, FND-031 |
| Strand thickness | d_c | 1.87e-19 m | 1.87e-19 m | measured (calibration) | HBAR-005 |


**l_q/a card sync (v3.17.0 arc, FND-041/042/044):** l_q rescales with the mesh by
R1's own registered form (l_q = √(4πα ħc/T₀)); the previously tabulated 158/271
used the stale κ=1 l_q and are corrected above (l_q/a = 43.0·κ_pack^(1/6)). The
1–100 window is retired as HALF-WINDOW (lower edge physics, upper edge grammar,
FND-042) — no κ_pack ceiling exists. The ratio g = l_q/a is the corpus's single
mesoscopic unknown (FND-044): λ = g²/(4π), A = 2.6348·l_q slaved; κ_lock = 2T₀/a
predicted at 1.96e20 (κ=50) / 5.74e20 (κ=250) J/m² awaiting any independent
determination; the energy-budget defect-log mechanism is EXCLUDED (FND-045,
Failed-and-kept; demand 2.2–3.2 m_ec² blind). κ_pack routes: the g-mechanism
(blocked), the PRED-003 drift ratio, and the adjoint Casimir ratio
(κ_pack = 1.25/(2|δ_A−δ_F|); current lattice bound gives ≥ 12.5, FND-047).

**Σ_eff is pinned (FND-030); its promotion to the VACUUM stiffness is conditional
(FND-034/035, v3.16.1).** The Casimir profile data shows tube strands compress
(2.25× density at unchanged radius, adjoint vs fundamental), so the fundamental
tube's own packing factor κ_pack ≥ 1 is open and Σ_vac = Σ_eff/κ_pack. The provenance audit showed both former candidates were ONE relation,
Σ = 3T_tube/(n·a²), evaluated at two strand counts: the measured n = 152–156
(lattice, two independent estimators agreeing to 1.3%) and the dead n_t = 111
(killed twice — by its own requested derivation in the reconnection chain, and
structurally by the measured tube radius at +17–19%, one-signed). The 5.10e35
registration is **demoted to historical** by kill-inheritance. The pinned band
carries its dependences on the face: the strand-count-follows-energy-density
identification (ELEC-053), the sech² conversion model (2.2% profile spread),
and the same-data caveat — an independent lattice determination remains the
one external check, with Σ scaling as R_eq⁻². The downstream sweep at the
pinned band (FND-031, Commission NU) returned zero flipped verdicts.

**Working point (FND-MATTER-044).** For scale-sensitive work the corpus now uses
the **M-point** — the mesh point that solves the m_e-pinned scale calibration
jointly with the invariance theorem T₀ = Σa²/3 at the lattice-anchored Σ, giving
**a = 6.0e-17 m, T₀ = 434 J/m**. This is the working point in §2–§3 below; the
historical adoption values (a held at the Lorentz bound) are retained alongside
for provenance and for the branch-comparison invariants.

---

## 2. Derived lengths

**The working mesh point is now the M-point** (a = 6.0e-17 m; see §3 and the
M-point note below), fixed by solving the m_e-pinned combination jointly with the
invariance theorem (FND-MATTER-044). Use it for scale-sensitive work. The
historical adoption values below held a at the Lorentz bound by convention and are
retained for provenance and for the branch-comparison invariants.

| Quantity | Symbol | **M-point (working)** | Lattice-anchored (historical) | Σ-route (historical, demoted) | Relation |
|---|---|---|---|---|---|
| Strand spacing | a | **6.0e-17 m** | 9.999e-17 m | 1.000e-16 m | a = √(3T₀/Σ) |
| Coherence spacing | w | **3.46e-17 m** | 5.773e-17 m | 5.774e-17 m | **w = a/√3, exactly** |

The invariance theorem T₀/Σ = a²/3 holds **for any tube radius** (ELEC-053), so
w = a/√3 is exact on every branch and the M-point moves a and w together. The
historical branches land on the Lorentz bound a ≲ 1e-16 m to better than 0.1%; the
M-point sits at 60% of the bound (40% margin, no longer saturated).

**The thinness ratio r/a ≈ 9.4e-4** — the strand is roughly a thousand times
thinner than the distance to its neighbour. This is not decorative; see §5.

---

The M-point tension and line density are exact and given first. The elastic
constants (C, γ, E, G) below are quoted on the two historical branches, since their
derivation runs through the K₀ machinery (GRV-073) that has not yet been
re-evaluated at the M-point; the branch-independent ratios (γ/T₀, w/a) are exact on
every branch including the M-point.

| Quantity | Symbol | **M-point (working)** | Lattice-anchored (historical) | Σ-route (historical, demoted) | Status | Source |
|---|---|---|---|---|---|---|
| Tension | T₀ | **434 J/m** | 1203 J/m | 1700 J/m | **not independent**: T₀ = Σa²/3 | ELEC-053, FND-017, FND-MATTER-044 |
| Line density | μ | **4.83e-15 kg/m** | 1.339e-14 kg/m | 1.892e-14 kg/m | derived: μ = T₀/c² | FND-MATTER-033 |
| Stretch modulus | k | **magnitude open — see §5b** | | | k > T₀ required for nonlinear stability | EM-RECON-009, QB-008 |
| Torsional rigidity | C | *(re-eval pending)* | 4.21e-36 J·m | 5.95e-36 J·m | per strand, C = G·πr⁴/2 | GRV-009, GRV-073 |
| Couple-stress modulus | γ | *(re-eval pending)* | 4.21e-4 J/m | 5.95e-4 J/m | medium: γ = C/a² | GRV-073 |
| Young's modulus | E | *(re-eval pending)* | 8.76e40 Pa | 1.24e41 Pa | E = k/(πr²) | GRV-073 |
| Shear modulus | G | *(re-eval pending)* | 3.50e40 Pa | 4.95e40 Pa | G ≈ E/2.5 (ν = 0.25 registered import, GRV-073; carried at the fine level by NUN-GRV21/FND-131) | GRV-073 |

**On the tension — corrected 1 Aug 2026 (FND-021).** T₀ behaves as a **Lagrange
multiplier** *in the inextensible limit*, and in that limit stores no energy, from
which follows the useful no-go that **no local derivation of T₀ can succeed**
(FND-017).

But **the medium is not exactly inextensible, and must not be** — a perfectly
inextensible strand has no longitudinal wave at all, and the framework's
superluminal channel exists precisely *because* k is finite. The longitudinal
speed is

    c_L / c = √(k/T₀)

so "inextensible" is the k → ∞ idealisation. At finite k there **is** stored
elastic energy, of order T₀²/2k per unit length.

**On the wave speed.** c = √(T₀/μ) is satisfied identically on both branches, by
construction of μ. It is a consistency check, not an independent input.

---

## 4. Postulates, not numbers

- **P-VOL / near-inextensibility** — FND-STRAND-001 works with "literal
  inextensible elastic curves", and that is an **idealisation adopted for
  tractability**, not a claim that k is infinite. It is what makes T₀ behave as a
  multiplier *in the limit*. Taken literally it would forbid the fast channel
  (FND-021).
- **No material points** — FND-REL-002 (Derived). Longitudinal displacement is
  *gauge*; only its gradient (the strand density perturbation) is physical. This
  forbids the Galilean convective term, forces the wave sector into
  Lorentz-invariant form, and selects the lab parametrization over arclength.
- **Framed** — every strand carries a material frame with an explicit twist field
  and a conserved Calugareanu ledger, Lk = Tw + Wr (FND-STRAND-002/003). This is
  what makes the medium a **Cosserat continuum**.
- **The medium is a reservoir** — infinite and pre-tensioned. Without it a closed
  medium absorbs transverse displacement at *zero* energy cost and carries no
  waves at all (ELEC-080), so **the optics sector depends on this premise**.

---

## 5. Two facts worth carrying into every session

**The strand is a ROD, not a string.** It has a stretch modulus and an r⁴ torsion
law (GRV-009's primitives, `torsion~r^4`). A tensioned string with no shear
modulus would have *no torsional stiffness whatever*, and the framework's twist
sector would not exist. This was registered inside a claim marked **Failed** —
GRV-009 failed for the wrong sign of spatial curvature, and its *primitives* were
never in dispute.

**The thinness ratio does real work.** Axial stiffness carries r² (a
cross-sectional area); torsional rigidity carries r⁴ (a polar moment). Their
ratio therefore leaves one factor of (r/a)² ≈ 8.7e-7 — which is why γ/T₀ ≈ 3.5e-7
rather than order unity. **A dimensional estimate using only T₀ and a cannot find
this**, because the whole suppression lives in the second length that estimate
discards. It was found only by locating the registered elastic constants.

---

## 5a. ⚠ TWO DIFFERENT "FAST CHANNELS" (FND-022)

The corpus uses one name for two objects that want **opposite limits of k**:

| | What it is | Needs | Used by |
|---|---|---|---|
| **(a) Longitudinal elastic wave** | a real propagating mode at c_L = c√(k/T₀) ≈ 1.4e4·c | k **finite** — an infinitely stiff strand has no wave at all | EM-RECON-011/012, ELEC-067 |
| **(b) Instantaneous constraint** | not a wave; no speed; the rigidity of the k → ∞ limit | k → **infinity** — Bancal's theorem excludes *all finite speeds* | QB-007, QB-008, QB-012, QB-023, ELEC-079 |

**The finite-speed wave cannot supply Bell correlations**, however large √(k/T₀)
is — that is precisely why QB-008 forced the conjecture onto the
instantaneous-constraint limb.

**Resolved (FND-023).** They are *not* the same modulus. **P-VOL is volume
conservation of the MEDIUM**; **k is the STRAND's stretch modulus** — independent
constraints on different objects. A strand can stretch while the medium conserves
volume.

And **incompressible elasticity is the standard precedent**: an elliptic,
instantaneous pressure multiplier coexisting with hyperbolic, finite-speed shear
waves in one action. Textbook, and not paradoxical.

Bancal's theorem doesn't apply either: its argument runs through relativity of
simultaneity as *fundamental*, while FND-REL-001 makes Lorentz invariance
**emergent** and FND-REL-002 forces only the **wave sector** into Lorentz form. A
constraint is not a wave.

*Still open:* nobody has written the constrained action with the volume
multiplier explicit — and whether that multiplier is the right **carrier** for
the nonlocal conditional is unestablished, since QB-007 needs spacelike
*depletion of a wave amplitude*.

## 5b. ⚠ THE k/T₀ MAGNITUDE — eight orders, still open

**This is a different question from §5a.** §5a settled the *conceptual* confusion
(FND-023): the strand stretch modulus k and the medium's volume constraint P-VOL
are separate constraints on separate objects, so there is no paradox in a strand
stretching while the medium conserves volume. What remains open — and what §5b is
about — is the *numerical magnitude* of k/T₀ itself, on which two registered
claims still disagree by eight orders, and neither cites the other:

| Source | k/T₀ | Basis |
|---|---|---|
| EM-RECON-009, GRV-009 | **2** | fitted to nuclear and chemical spacings; k > T₀ for nonlinear stability |
| QB-008 | **≥ 1.9e8** | forced by Bell timing, v_dep > 1.38e4 c; and √(1.9e8) = 1.38e4 confirms c_L/c = √(k/T₀) |

**Everything downstream of k inherits this.** The couple-stress modulus is
γ = 4.21e-4 J/m at k/T₀ = 2, and **3.996e+04 J/m** at the Bell-timing value —
eight orders apart, and the sign of the comparison with T₀ *inverts* (γ/T₀ =
3.5e-7 versus 33).

This is reported, not adjudicated. Choosing by preference is the failure mode
this corpus spent 1 August correcting.

## 5b. The medium's electric limits (two different objects; added 27 Sep 2026)

- **Linearity limit, E_crit = 2.0e23 V/m** (FND-031, at the pinned Σ): the field at which the
  mesh's linear response fails, the Kerr-class nonlinearity onset. Not a breakdown of the
  vacuum; the earlier habit of calling it "the vacuum breakdown field" is retired by rider.
- **Charge-creation field, E_c = 2π T0 r²/(5 e w² a²)** (FND-182): the field at which the
  lock's torque tilts the strand's orientation potential past its maximum and the vacuum
  creates windings, the mesh analogue of pair creation. One unpinned input, the kink width
  w (registered regime 0.8 to 2.8): window [1.1e15, 3.2e18] V/m across the three scale sets,
  above the highest field applied to vacuum (9.1e14 V/m), below QED's Schwinger field
  (1.32e18 V/m) over most of the range. Census tier T4 since 4 Oct 2026 (was T2 under ELEC-101): the
  one input, the on-site orientation potential, has no registered source in the vacuum weave (the
  junction is a point bond, f = 0; crossings do not press; JUNCTION-LOCK), so the window is a
  constraint on that source, not a prediction. Returns to T2 when a registered source gives V_0,
  and to T1 candidacy when it gives V_0 in electronvolts inside the window.

## 6. What is *not* registered

- **The strand's Poisson ratio.** G ≈ E/2.5 is imported from isotropic elasticity.
  This is the one unpinned quantity in the mechanical chain and can move γ by a
  factor of a few — not by orders.
- **A matter-to-rotation coupling.** GRV-005's source is a static force density
  with no torque, spin or angular-momentum term. See GRV-071.
- **A metric map with a shift slot.** GRV-029's dictionary is an exact
  *four-to-four* bijection for a static diagonal metric; g_0i has nowhere to live.
- **Fundamental masses.** The lepton spectrum is an irreducible input (PM-004).

---

*Branch note (revised 10 Aug 2026): the two-branch structure is RETIRED —
Σ is pinned (FND-030) and the Σ-route columns below are historical provenance
only, retained because mixing branches produced errors before and the record
of both must stay legible. All new work uses the pinned band with the M-point.
The ratio γ/T₀ = 3.50e-7 is branch-independent, as is w/a = 1/√3.*

---

## The M-point — provenance and status (FND-MATTER-044)

**Now the working mesh point** (promoted into §1–§3 above as of this revision).
Solving the m_e-pinned combination T₀a = m_e c²/L (the scale campaign's single
spent calibration, FND-MATTER-040/041) jointly with the invariance theorem
T₀ = Σa²/3 at the lattice-anchored Σ gives the m_e-consistent mesh point:

- **a = 6.0e-17 m** (Lorentz bound satisfied with 40% margin, no longer
  saturated — the historical §2 values held a at the bound by adoption)
- **T₀ = 434 J/m**  (μ = T₀/c² = 4.83e-15 kg/m)

All pairwise EM comparisons land inside the zero-point band (factor ≤ 3); see
analysis/MATTER044_whisper_pricing_results.md. n_q is invariant under this move
(proven), so the snap-band shortfall is a genuine residual interrogating the
core thickness h.

**Downstream work now rests on it.** The directional-share question that was the
last open piece around this construction closed after the M-point was fixed
(FND-MATTER-059 registered the surviving half; FND-MATTER-060 returned the
terminal negative, λ stays Open, the displaced-mode route registered as a
near-miss at 2.08× against a 2.00× bar and **not** promoted). The first derived
G exponent pair (GRV-073/074/075) uses these constants. The M-point is therefore
load-bearing, not tentative.

**Elastic-constant re-evaluation still pending.** The §3 elastic constants
(C, γ, E, G) run through the K₀ machinery (GRV-073) and are quoted only on the
historical branches until that chain is re-evaluated at the M-point;
`rope_parameter_card.py` verifies the historical-branch values and the
branch-independent ratios, which is what it checks today.


---

## 6. The fine level (added 17 Aug 2026, v3.26.77 — the BLOCH-L arc, FND-126 → FND-132)

The photon sector's granted substructure (GRANT-SUBSTRUCTURE, FND-084) makes
each coarse strand a bundle of n_sub finer fibres, two-level wound at the
derived angles. The 17 Aug arc determined this level's mechanics end to end.

**The fibre (granted rod class, FND-118 — one modulus, circular section):**

| Quantity | Symbol | Value / bound | Status | Source |
|---|---|---|---|---|
| Fibre tension | T_fibre | **3/2 T0_f exactly** | derived (dynamical anchor solve) | FND-126 |
| Fine stretch ratio | k_f/T0_f | **9 exactly** at k/T0 = 2 (read 9.008) | derived: k_f/T0_f = 6(k/T0) − 3 | FND-126/127 |
| Fine longitudinal speed | c_L,f | **3.00 c, FINAL at this instrument class** | derived; non-affine channel = 0 by grant | FND-126/129 |
| Bending stiffness | kb | **≤ 0.07909 T0_f a_f²** | bound-with-named-gap (dynamical-background correction unpriced) | FND-121 cond. 1 fired, FND-131 |
| Fibre radius | r_s | **≤ 0.1874 a_f** | bound (rod identity at k_f = 9) | FND-131 |
| Torsional stiffness | C_f | **kb/(1+ν) = 0.8 kb** | derived (granted class + registered ν) | FND-131 |
| Twist density | ω | 0 (wound-born) or −1.5332/a_f (Lk-conserving) | both formation readings computed | FND-131 |
| Fine frame-drag coupling | (G I_p)_f | **≤ 0.0633 T0_f a_f²** | bound (reverted from KBSAT value) | FND-131 |
| Contact rule | — | **contact-free, sub-threshold** (coverage at 7–20% of tangibility onset) | Author-granted, three registered legs, supersession clause armed | FND-129 |

**The winding is a wave (forced, not adopted — FND-130/131):** the static
winding is unreachable across the entire admissible (ν, kb, ω) box, so the
two-level winding is a **rotating-wave state**:

| Quantity | Value | Status |
|---|---|---|
| Level-1 wave speed (along fibre) | **√(3/2) c = 1.2247 c exactly**, kb-free | derived (bending-neutrality theorem) |
| Level-1 material orbital speed | **c exactly** — sin²θ × T_fibre = (2/3)(3/2) = 1 | derived; ARMED TRIPWIRE on T_fibre |
| Level-2 wave speed | √(3/2 + 17.926 kb) c = 1.5–1.7 c at the bound | derived, kb-dependent |
| Energy bill (dynamical share) | **[0.615, 0.779]** — inside FND-MATTER-041's zero-point window (< 0.889) | priced-and-payable |

**The magic angle's triple duty** (one angle, three unrelated derivations —
the standing open question): sin²ψ₁ = 1/3 is simultaneously isotropy-exact
(FND-088), bending-force-neutral (τ² = κ²/2 identically, FND-130), and
c-orbital (FND-132).

**Dead and kept:** KBSAT (kb = 0.126 as a value) was executed by its own
condition 1 on 17 Aug (FND-131) — the extremal principle and the against-case
stand as the record. The multiplicative coarse→fine factorization (4.046 ×
per-level compensations) is superseded in form; the 4.046 core-existence
floor survives flagged, its dynamical test chartered.
