# COMMISSION CROSSING-PRICE-1 -- THE VACUUM CROSSING'S ENERGY IN JOULES, AND WHAT THE REGISTERED WINDING THEN IS
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-27; the successor of STRAND-MASS-SCALE, which refused
# at C1 for want of three inputs; a derivation of A_c from registered rod mechanics with a blind numeric
# confrontation whose outcome nobody knows; harness on benchmarks/lab/_kit/labkit.py)

## WHERE IT STANDS (the honest sentence, before the question)
The registry's charge carrier is a winding, a 2 pi kink of a strand's orientation angle, and the kink exists only
because an on-site orientation potential V_0 resists the azimuth. FND-184 gave V_0 a registered source (the contact
acts on surfaces, so a non-circular two-strand section feels its azimuth, period pi, amplitude V_sec / V_line of
0.035 to 0.48 over the swept range, T-1 run). STRAND-MASS-SCALE (2026-10-04) then carried V_0 as a symbol through an
exact chain, w^2 = kt / V_0, omega_min^2 = V_0 c^2 / (T0 a r^2), E_c = (4 pi / 5) V_0 / (e a), and refused at C1 because
three numbers are not on the registry: the crossing contact's amplitude A_c in joules, its range sigma in metres,
and the crossing density per node of the coarse weave. FND-184's first-use note narrowed it: sigma_0 = w is
registered (EM-RECON-018), n_x = 2 crossings per node is derived, A_c is bounded below, and ONE quantity remains,
the standoff of crossing strands in the vacuum weave in units of the strand width. NODE-STANDOFF (same day) wrote
V_0 = f T0 a / 2 per node and found the registered coasting regime (w in [0.8, 2.8]) implies f of order 1e-7 to 1e-4
on a single strand, with the face-holding tie priced at f about 3.5 as the alternative. Nobody knows f. Everything
downstream of it (FND-182's charge-creation field against the laser record and the Schwinger field; whether the
winding coasts or is pinned; the kink's rest energy, read in analysis/ELEC_KINK_reading.md) waits on that one
number. This commission computes it from registered rod mechanics and confronts it blind with the regime bars.

## THE QUESTION
  Q1  A_c IN JOULES. The crossing contact's amplitude is the elastic cost of two tensioned coarse strands passing
      each other at the registered just-in-contact standoff (EM-RECON-018: contact is the knee of the form, the
      surfaces touching, centre-line separation sigma_0 = w = 0.6272 a): each strand deflects by w / 2 over the
      tension-bending length l_b = sqrt(B / T0) (B = E pi r^4 / 4 from GRV-073's E, r = d_c / 2), and the crossing's
      energy is the sum of the two strands' tension and bending work, A_c(T0, B, w), a closed form from a variational
      minimum over the deflection profile (D1). Reported with its band over GRV-073's registered branches of E.
  Q2  THE CROSSING STANDOFF. The one unregistered quantity, d_x / w: in the registered weave a strand crossing another
      sits at the standoff that minimises the contact-plus-elastic energy (D2), computed on the same profile; if the
      minimum is at the knee (d_x = w) the identification of Q1 is self-consistent, if it is elsewhere A_c is
      re-evaluated there and both are reported.
  Q3  V_0, w AND f. From A_c and the registered chain: V_sec = (V_sec / V_line) A_c with the ratio at the registered
      rho / sigma (T-1's table), V_0 = n_x V_sec (n_x = 2, FND-184), f = V_0 / (T0 a / 2), w = sqrt(kt / V_0) on the rod
      route and the band route (both registered per-node stiffnesses, 2.5 apart; STRAND-MASS-SCALE), and E_c =
      (4 pi / 5) V_0 / (e a). The confrontation: w against the coasting regime [0.8, 2.8] and E_c against the two
      registered field marks (the laser record 9.1e14 V/m, Yoon et al. 2021; the Schwinger field 1.32e18 V/m),
      loaded in the verdict's last unit only.

## WHAT IS GIVEN (registered inputs; no others enter)
- T0, a, d_c (r = d_c / 2), E on its registered branches (docs/ROPE_PARAMETERS.md; GRV-073; FND-MATTER-044).
- The contact form's shape A_c / (1 + (r / sigma)^4) (EM-RECON-023) and sigma_0 = w, w / a = 0.6272 (EM-RECON-018, FND-068).
- FND-184 (the surface gap; V_sec / V_line versus rho / sigma from T-1, analysis/contact_section_t1.npz; n_x = 2).
- STRAND-MASS-SCALE's chain (exact, machine-checked) and NODE-STANDOFF's f convention.
- The coasting regime w in [0.8, 2.8] (FND-STRAND-002, FND-KIN-002); FND-182's E_c identity; the two field marks.
- NOT: any atomic-scale contact energy (FND-KIN-005's 13.8 eV plateau is a hydrogen-calibrated toy, excluded by
  STRAND-MASS-SCALE and excluded here); not m_e, hbar or the kink's mass, which enter nowhere.

## THE ONE IDENTIFICATION, STATED SO THE REVIEWERS CAN CALL IT
D1 identifies the crossing price with the elastic cost of the registered standoff. The registry's interpenetration
primitive says a crossing has a FINITE price and the contact form says its SHAPE; neither says its origin. FND-184
moved the contact to the strands' surfaces and EM-RECON-018 fixed the contact as "just touching at the knee"; the
step from there to "the price is what it costs the rods to stand off" is the natural reading of those two claims
together and is not itself registered. If the reviewers judge it a grant rather than a derivation, the commission
is a price sheet for GRANT-CANDIDATE-CROSSING-PRICE and the author decides; the computation is the same either way.

## DESIGN COMMITMENTS (locked at lock)
D1. THE PROFILE. Two straight tensioned rods (tension T0, bending stiffness B) crossing at right angles, each
    deflected transversely so that their centre lines are separated by d at the crossing point; the deflection
    y(s) minimises Int [T0 y'^2 / 2 + B y''^2 / 2] ds subject to y(0) = d / 2, y -> 0 at infinity: a closed form
    (the exponential-plus-linear profile of the tension-bending equation, length l_b = sqrt(B / T0)); A_c(d) is
    twice that minimum; A_c = A_c(w) is the crossing price at the registered standoff.
D2. THE STANDOFF. The crossing's total energy U(d) = A_c(d) + V_contact(d) with V_contact the registered form at
    amplitude A_c(w) and range w (self-consistently: the form's amplitude IS the price at the knee); d_x is the
    minimiser of U over d in [0, 3 w]; if d_x differs from w by more than 10 percent, A_c is re-evaluated at d_x and
    both values are carried as the band.
D3. THE BAND. E on both registered branches (8.76e40 and 1.24e41 Pa; the M-point re-evaluation if GRV-073's formula
    evaluates there); V_sec / V_line over T-1's swept range at the registered rho / sigma; kt on the rod and band
    routes. f, w and E_c are quoted as [min, max] over the whole band, and the forms are decided by the WHOLE band
    (a band straddling a boundary is the mixed form).
D4. THRESHOLDS, fixed here: COASTS if the whole w band lies in [0.8, 2.8]; PINNED if the whole band lies below 0.8;
    FREE-ROTOR if the whole band lies above 2.8 (the well too shallow to make a kink at all; V_0 below kt / 8);
    MIXED otherwise, with the sub-bands quoted. E_c: ABOVE-RECORD if the whole band exceeds 9.1e14 V/m, BELOW-RECORD
    if below (FND-184's falsifier F1 fires: the laser record would already have seen charge creation), BELOW-SCHWINGER
    / ABOVE-SCHWINGER by the same rule against 1.32e18, mixed forms by the band.
D5. NO SOLVER beyond the one-dimensional minimisation of D2 (brentq on a closed form); every other number is a
    closed form of card constants. Clean room: hbar, m_e and the electron enter nowhere; the field marks and the
    coasting bounds are loaded in the verdict unit only.

## HARNESS (binding)
Driver and verdict on labkit; units: inputs (the card read through rope_parameter_card.py, its verifier run; T-1's
sealed npz read; every constant sealed with its branch), profile (D1's closed form derived by sympy and checked
against a numerical minimisation on a grid of 1e4 points to 1e-6, sealed), standoff (D2, sealed), chain (Q3's
numbers over the band, sealed), verdict (forms from the seals; the field marks and the regime loaded here).
LAB_SMOKE=1 runs the profile unit on synthetic (T, B, w) fabricated to differ by orders from the card and prints
the closed-form check only, no A_c.

## VALIDATION BARS (halt-grade)
v1. The card's verifier passes before any constant is read.
v2. D1's closed form reproduces the numerical minimum to 1e-6 on the synthetic triple and on the card.
v3. The chain reproduces STRAND-MASS-SCALE's three identities symbolically (sympy equality) before any value enters.
v4. V_sec / V_line read from the sealed T-1 record, not retyped.
v5. Clean room: the verdict unit is the first to load 0.8, 2.8, 9.1e14 and 1.32e18.

## FORMS (exhaustive; pre-registered)
Q1 (one): PRICE-DERIVED (A_c with band), PRICE-UNDERSPECIFIED (an input not fixed to the precision D3 needs; named).
Q2 (one): STANDOFF-AT-KNEE, STANDOFF-ELSEWHERE (d_x / w quoted), STANDOFF-NONE (no minimum in [0, 3 w]).
Q3 (one each): COASTS / PINNED / FREE-ROTOR / MIXED; and ABOVE-RECORD / BELOW-RECORD / mixed with the Schwinger
sub-label. NO-CALL: v1 to v5 unmet.
Readings written on the results file's face, not formed: COASTS with ABOVE-RECORD means the registered winding is
a free kink and FND-182's discriminator is live in the next laser generation, with a number; PINNED means the
registered charge carrier cannot move in the registered weave, which is a kill of the winding-as-charge reading
unless a registered mechanism unpins it (none proposed; no-rescue); BELOW-RECORD fires FND-184's falsifier F1 and
the surface-contact grant retires by its own clause; FREE-ROTOR means the surface contact is too weak to make a
kink and gap 2 stays open with its source priced at zero.

## NO-RESCUE RULE
No change to D1's profile or D2's range after the lock; no branch chosen by preference; the band decides. If
PINNED, no follow-up may search for an unpinning mechanism; that is a grant.

## DISCLOSURES
The executor has not computed A_c, d_x, f, w or E_c from D1. The executor HAS computed, from the registered chain
alone and disclosed in analysis/ELEC_KINK_reading.md, what the kink weighs at either end of the coasting regime
(a keV object on the pair, an eV object on the strand) and its action (hbar / 7e4 on the pair); those are not
this commission's numbers and this commission does not score them. The prior, disclosed and not leaned on: the
executor expects A_c of order T0 w times a number of order one, which would put f near 1e-1 to 1 and the single
strand's w below 0.8 (PINNED) while the pair's w sits near the regime; the NODE-STANDOFF reading already recorded
that the coasting regime on a single strand needs f of 1e-7 to 1e-4, so PINNED on the strand would not surprise
the record. The Director's expectation is not on file.

## NORTH STAR ACCOUNTING
Target-facing through FND-182: the charge-creation field is a registered discriminator candidate against the
laser record and QED's Schwinger field, quantitative only as a three-order window until V_0 is pinned; this
commission pins it or retires its source. It also closes or prices closure gap 2 (FND-186).

## BUDGETS
Closed forms and one 1D minimisation; cpu_hours 1; mem_gb 1; usd 0 beyond drafting and review. Results to
analysis/CROSSING_PRICE_1_results.md.

```lab
commission: CROSSING-PRICE-1
target: "Closure gap 2 (the on-site orientation potential V_0) and FND-182's charge-creation discriminator: the vacuum crossing's energy A_c in joules from registered rod mechanics at the registered standoff, the crossing standoff self-consistently, then V_0, f, the kink width w against the registered coasting regime and E_c against the laser record and the Schwinger field, blind; decides whether the registered winding coasts, is pinned, or has no well; moves no number in section 2b"
driver: benchmarks/lab/crossing_price_1/driver.py
verdict_script: benchmarks/lab/crossing_price_1/verdict.py
instrument:
  - benchmarks/foundations/rope_parameter_card.py
  - benchmarks/foundations/strand_mass_scale.py
  - benchmarks/foundations/contact_section_t1.py
  - benchmarks/lab/_kit/labkit.py
forms: [PRICE-DERIVED, PRICE-UNDERSPECIFIED, STANDOFF-AT-KNEE, STANDOFF-ELSEWHERE, STANDOFF-NONE, COASTS, PINNED, FREE-ROTOR, MIXED, ABOVE-RECORD, BELOW-RECORD, NO-CALL]
state: [analysis/crossing_price_1_ckpt.pkl]
budget: {cpu_hours: 1, usd: 0}
mem_gb: 1
```
