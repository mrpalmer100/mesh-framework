# COMMISSION FINE-DISP-1 -- THE LONG-WAVELENGTH DISPERSION OF THE WOUND FINE MESH
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-21; a measurement on a credentialed instrument;
# the forms below were fixed at queue commit 5201dc8 BEFORE any wound number existed; on the author's instruction
# the executor then ran a PREVIEW on the same engine (analysis/FINE_DISP_1_preview.md, disclosed in section
# PREVIEW); the lab's sealed run is the record and the forms are not changed by the preview)

## WHERE IT STANDS (the honest sentence, before the question)
The photon sector's existence problem was resolved on 12 August 2026 by GRANT-SUBSTRUCTURE-TIGHT (FND-087): the
vacuum strand is a bundle of n_sub finer sub-strands with redistributed tension T0_f = T0 / n_sub, wound at two
levels at the derived angles psi_1 = 35.2644 deg and psi_2 = 59.4444 deg (FND-088), over-resolved to
a_f <= lambda / 4 at the highest carried photon energy m x 1.4 PeV. On that mesh the band ceiling is exhibited
at 2.99 PeV (FND-100) and the forced Lorentz-invariant, isotropic wave equation is re-derived at homogenized
level (FND-090). What that arc did not compute, and KNOWN_LIMITATIONS says so ("the discrete O((ka)^2) question
is FND-REL-004's"), is the next term: the coefficient beta_f in

    omega^2 = c^2 k^2 [1 - beta_f (k a_f)^2 + O((k a_f)^4)]

on the wound fine mesh. On the coarse straight strand FND-REL-004 derived beta = 1/12 - kb / (T0 a^2) exactly,
and the live gamma-ray-burst bound (B4 there: E_QG,2 > 7.3e11 GeV, LHAASO GRB 221009A) turns any beta of order
one into a bound a <= 9.3e-28 m. The same bound at the fine level reads a_f sqrt(beta_f) <= hbar c / E_QG,2 =
2.70e-28 m. At the grant's minimal choice a_f = lambda / 4 at 1.4 PeV, which is 2.21e-22 m, that requires
|beta_f| <= 1.5e-12; at any beta_f of order 1e-2 it requires a_f near 1e-27 m, which is n_sub of order 1e20 to 1e21
rather than the 1e10 the grant priced. The registry carries n_sub as an input (FND-110, irreducible-constant
class), so neither outcome is a contradiction; but one of them is a derived number where there is now a guess,
and the other is a statement that the winding does what no straight lattice can do. This commission computes
beta_f. Nothing about its value is predicted here.

## THE QUESTION
  Q1  THE COEFFICIENT. On the wound fine mesh at the derived angles, what is beta_f: its isotropic part, its
      direction dependence, and its dependence on the one registered fine-level knob, the bending stiffness kb
      in [0, 0.07909] T0_f a_f^2 (the FND-131 bound)?
  Q2  THE PRICE. Under FND-REL-004's live bound, what fine spacing a_f and what sub-strand count n_sub does the
      measured beta_f require, and how does that compare with the grant's priced n_sub ~ 4.6e9 to 1.3e10
      (FND-083)?

## WHAT IS GIVEN (registered inputs; no others enter)
- The SHIN6 instrument, benchmarks/foundations/shin6_3d_bloch.py, inherited verbatim: the 18-neighbour
  central-spring vector lattice with the g = 2 shell calibration, the tangent-projector weights, the two-level
  winding with f = 1/5 as the adjudicating member (f = 1/4 and 1/3 as context), the derived angles, the
  straight-medium acoustic normalization, the plane-wave band identification (FND-089, FND-090, FND-100).
- FND-REL-004's closed form on the straight chain, beta = 1/12 - kb / (T0 a^2), and its B4 bound,
  E_QG,2 > 7.3e11 GeV at 95 percent, read as hbar c / E_QG,2 = 2.70e-28 m.
- The fine-level bending bound kb <= 0.07909 T0_f a_f^2 (FND-131; docs/ROPE_PARAMETERS.md) and the fine-level
  derived constant k_f / T0_f = 8.09 (FND-110), read only.
- The grant's length ceiling a_f <= lambda / 4 at m x 1.4 PeV (FND-087), with m = 1 the registered value and
  lambda = h c / E; the M-point coarse spacing a = 6.0e-17 m (FND-MATTER-044); the priced n_sub window of
  FND-083. These enter Q2 only, as the comparison, after the verdict on Q1 is sealed.

## WHAT IS NOT ASSUMED
No new angle, no new weight, no new lattice. The instrument is SHIN6 plus one term it did not need before: the
bending channel (D2), which is credentialed on the straight medium against FND-REL-004's closed form before any
wound number is read. Whether beta_f cancels, is small, or is of order one is not predicted by the author, the
executor or the lab. The 1.5e-12 figure above is the consequence of the bound, not a target; it appears in no
file of this commission except the verdict script's price table.

## SCOPE (hard boundary)
The (k a_f)^2 coefficient of the two transverse plane-wave bands on the SHIN6 lattice, at the derived angles,
in the homogenization regime SHIN4/SHIN6 established (p <= lambda / 4 is the grant's regime; the fit window of
D3 stays inside it). OUT: the longitudinal sector; the (k a_f)^4 term beyond being reported; any re-derivation
of the angles, the ceiling or the isotropy theorem; the coarse mesh; any claim about m. A cancellation found on
this engine is a cancellation on this engine (Modeled); the charter says in section FORMS what further step a
Derived-grade statement would need and does not take it.

## DESIGN COMMITMENTS (locked at lock)
D1. THE DISPERSION FIT. The wound medium's structure length is the winding period p = P a_f (P = 5 at the
    adjudicating member), so the expansion variable is k p, not k a_f, and the coefficient is reported in both
    units: beta_p per (k p)^2 and beta_f = P^2 beta_p per (k a_f)^2. For each of SHIN6's 13 probe directions d
    and for k p in {0.02, 0.04, ..., 0.20} (ten values; k a_f = k p / P), the plane-wave band frequency
    omega(k d) from two_bands() on the inherited engine, both transverse bands; the quantity
    y = (omega / k)^2 fitted to c_d^2 [1 - beta_p (k p)^2 + gamma_p (k p)^4] by least squares with c_d the
    band's own k -> 0 phase speed (fitted jointly, so the direction-dependent speed factor of SHIN4/SHIN6 is
    absorbed and beta is a pure ratio). Reported per direction and per band: c_d, beta_p, gamma_p, the fit
    residual. beta_iso is the mean of beta_p over the 13 directions and both bands; the anisotropy
    A = (max beta_p - min beta_p) / 2; the band split B = |mean over directions of (beta_p band 0 - beta_p
    band 1)|, which is dispersion birefringence. On the straight control P = 1 and the two units coincide.
D2. THE BENDING CHANNEL. One term added to dyn_matrix(): for each site and each stencil direction b, a
    second-neighbour coupling to the sites at +2b and -2b with the fibre-bending second-difference form
    (stiffness kb / a_f^2 in the engine's units, so that on a straight chain along b it is exactly the kb term of
    FND-REL-004's operator) weighted by the bond's alignment with the local tangent, (b . T)^4 averaged over the
    two end sites, so that bonds across the fibre carry none. The acoustic sum rule holds by construction
    (the term is a difference operator). kb is swept over {0, 0.02, 0.04, 0.06, 0.07909} T0_f a_f^2.
D3. THE FIT WINDOW stays at k p <= 0.20 (k a_f <= 0.04 at P = 5), inside the supercell's zone by a factor 15,
    so the plane-wave weight is above 0.95 at every point (recorded; a point with weight below 0.5 is dropped
    and the drop is disclosed). A direction and band whose fit residual exceeds 1e-8 is a band crossing inside
    the window: it is reported as such, excluded from beta_iso, A and B, and disclosed; more than two such
    directions at the adjudicating member is NO-CALL.
D4. THE PRICE (Q2, computed by the verdict script from the sealed beta_f, not by the driver): with
    beta_min = min over the kb sweep of |beta_iso| and beta_ceil = |beta_iso| at the kb ceiling,
    a_f(required) = 2.70e-28 m / sqrt(beta), n_sub(required) = (a / a_f)^2 for each, beside the grant's
    a_f = 2.21e-22 m and n_sub window. A table, not a verdict form.

## VALIDATION BARS (halt-grade; the credential, run first, sealed before any wound number)
v1. STRAIGHT CONTROL, NO BENDING: on the straight medium (wound = False, P = 1) at kb = 0, the (k a_f)^2
    coefficient of the inherited engine has a closed form (the 18-neighbour cubic lattice's expansion, derived
    in the verdict script by sympy from dyn_matrix()'s own weights with KX = 0.08 and g = 2); the fitted
    beta_d agrees with it to 1e-6 absolute in every direction. This is the instrument's beta resolution and it
    sets the floor in section FORMS.
v2. STRAIGHT CONTROL, BENDING: on the straight medium with the D2 term, the fitted beta along the fibre (z)
    shifts by -kb / (T0 a^2) relative to v1 (FND-REL-004's form) to 1e-4 absolute, at every kb of the sweep
    (the next-nearest bonds of the engine's straight medium move the shift at the 1e-5 level; that residue is
    reported).
v3. ISOTROPIC NULL: the engine's own isotropic null (the g = 2 calibration case of SHIN6) gives A <= 1e-6.
v4. FIT QUALITY: residual of the D1 fit below 1e-8 at every direction, band and kb on the straight control and
    the null; on the wound member the D3 crossing rule applies; gamma_p finite and reported.
v5. FRESH PATTERN: every number from a fresh eigensolve; no cached dispersion table enters; the checkpoint seals
    omega(k) per point before any fit.

## FORMS (exhaustive; thresholds fixed here from registered numbers and the v1 floor, not from any wound number)
  DISP-CANCELS       Some kb in the admissible box gives |beta_iso| <= 1e-6 (the v1 floor) AND A <= 1e-6 at that
                     kb, AND the verdict script's sympy expansion of the wound dynamical matrix at f = 1/5
                     (the same code path as v1, on the wound cell) shows the (k a_f)^2 coefficient vanishing
                     identically at that kb. Modeled on this engine; the Derived-grade step (the same identity on
                     the registered fibre operator rather than the spring engine) is named and not taken.
  DISP-NUMERIC-ZERO  |beta_iso| <= 1e-6 and A <= 1e-6 at some admissible kb, but the symbolic expansion does
                     not vanish identically (a numerical cancellation at the fit's resolution). The price table
                     is computed at beta = 1e-6.
  DISP-FLOOR         min |beta_iso| over the box > 1e-6 and A <= 0.1 |beta_iso| there: the winding does not
                     cancel the dispersion; the price (D4) is the result, n_sub(required) registered as the
                     grant's price under the live bound.
  DISP-ANISOTROPIC   A > 0.1 |beta_iso| or B > 0.1 |beta_iso| at the kb of minimum |beta_iso|: the leading
                     correction is direction-dependent or polarization-dependent, separately bounded
                     signatures (vacuum anisotropy and birefringence bounds are tighter than the time-of-flight
                     bound); the price table is computed from the largest |beta_p| and the form says so.
  INSTRUMENT-OPEN    v1 to v5 not all met; nothing wound is read.
  NO-CALL            Any point of the wound fit dropped under D3 in more than two directions at the adjudicating
                     member, or the two bands disagree in beta_iso by more than 0.1 |beta_iso|.

## PREVIEW (disclosed; the executor's run of 2026-10-21 on the author's instruction, after the forms were fixed)
benchmarks/foundations/fine_disp_preview.py, results in analysis/FINE_DISP_1_preview.md. The straight credential
passed (v1 to 4e-8; v2 to 2e-5). The wound adjudicating member, in the k p window of D3, gave beta_p of order
+5e-3 per (k p)^2, positive in every direction and band, with a tenfold spread across directions and a factor
two to three between the two bands, and the bending sweep moving it by a third at most; one direction showed a
band crossing inside the window at kb = 0 and none at the kb ceiling. Read against the forms as they stood, that
is DISP-ANISOTROPIC with a floor, not a cancellation. The preview is NOT the verdict: the lab's run on the
locked harness, with the symbolic check of DISP-CANCELS and the sealed checkpoint, is. The drafting worker and
the reviewers should treat the preview's numbers as the author's disclosure of what the executor saw, and the
charter's bars as unchanged by them (the bars and thresholds above are those of commit 5201dc8, amended only in
D1/D3 for the expansion variable and in v2 for the tolerance, both instrument facts the preview exposed).

## SMOKE DISCIPLINE (binding on the drafting worker)
The smoke run (LAB_SMOKE=1) executes v1 to v4 on the straight medium and the isotropic null only, prints
PASS/FAIL per bar and no wound number; it writes its own checkpoint under a smoke name the verdict script
refuses. The full run adds the wound sweep. The driver does one unit per invocation (credential; wound sweep per
kb; price) with an atomic checkpoint; the verdict script reads the completed checkpoint once, renders one FORM,
and refuses a second rendering.

## BUDGETS AND DISCLOSURES
Dense eigensolves of 375 x 375 matrices (P = 5): 13 directions x 10 k x 5 kb x 2 bands, minutes on any
machine; cpu_hours 2; mem_gb 2; usd 0 beyond the lab's drafting and review. Disclosed: the engine is the SHIN
spring lattice, not the registered fibre operator; its beta is the lattice's plus the winding's plus the D2
bending channel's, and the charter's forms grade the result Modeled for that reason. Results to
analysis/FINE_DISP_1_results.md.

```lab
commission: FINE-DISP-1
target: "SM_EMERGENCE row 2 (Lorentz invariance, Partial, D2): the (k a_f)^2 dispersion coefficient of the wound fine mesh, the one falsifiable remnant, computed on the credentialed SHIN6 engine with the registered bending channel; prices the substructure grant's n_sub under the live LHAASO bound or shows the winding cancels the dispersion; moves no number in section 2b"
driver: benchmarks/lab/fine_disp_1/driver.py
verdict_script: benchmarks/lab/fine_disp_1/verdict.py
instrument:
  - benchmarks/foundations/shin6_3d_bloch.py
forms: [DISP-CANCELS, DISP-NUMERIC-ZERO, DISP-FLOOR, DISP-ANISOTROPIC, INSTRUMENT-OPEN, NO-CALL]
state: [analysis/fine_disp_1_ckpt.pkl]
budget: {cpu_hours: 2, usd: 0}
mem_gb: 2
```
