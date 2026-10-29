# COMMISSION ELEC-KAPPA-1 -- THE TWIST STIFFNESS OF THE REGISTERED ROPE, AND THE ANGULAR MOMENTUM IT QUANTIZES
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-25; a derivation from registered constants with a blind
# numeric confrontation whose outcome is not known to anyone; closed forms, no solver; harness on
# benchmarks/lab/_kit/labkit.py; hbar / 2 and m_e enter the verdict's last unit only)

## WHERE IT STANDS (the honest sentence, before the question)
The executor's reading of the electron mechanism classes (analysis/ELEC_MECH_1_reading.md, filed 2026-10-25 after
the lab rightly refused to lock it as a commission: its outcomes were closed forms) leaves one class that reaches
the electron's g = 2 by mechanics with nothing tuned: a closed rope carrying its one unit of twist as a torsion
wave at light speed, in which the scale virial puts half the energy in the wave and half in the tension, the
transported winding is the current, and g = E / E_wave = 2 for any shape. Its angular momentum is fixed by the
winding and ONE rope constant, J_1 = 2 pi kappa / c, where kappa is the stiffness of the rope's internal twist
(the Goldstone energy (kappa / 2)(dPhi/ds)^2 of GRV-020; the pitch energy kappa (dPhi/ds - tau_0)^2 of GRV-018).
The registry does not carry kappa as a number. It carries what kappa is made of: the per-strand torsional rigidity
C (a rod, GRV-009 / GRV-073; C = 4.21e-36 J m on the lattice branch, 5.95e-36 on the Sigma route, the M-point value
pending re-evaluation; docs/ROPE_PARAMETERS.md), the tension T0 = 434 J/m (M-point), and the pair's standoff d0
(EM-RECON-017/018, d0 / sigma0 in [0.40, 0.46]). The question nobody has answered is what J_1 is for the registered
rope, against hbar / 2. The executor's expectation, stated here so it cannot be mistaken for a result and never
computed as a cell: of order 1e3 to 1e4 short, the HBAR-003 wall (S_1 = pi T w^2 / 2 c is 3549-fold short of hbar)
reached by a second route. If the gap is small, the hbar bridge reopens with a named missing factor; if it is the
HBAR-003 number, the wall is confirmed independently and the g = 2 class is dead at scale; either way kappa_pair
joins the parameter card.

## THE QUESTION
  Q1  KAPPA AND J_1. From registered constants only: kappa_pair, the stiffness of the two-strand rope's internal
      twist Phi(s), as the sum of its registered contributions (D1), with the band each contribution's inputs
      carry; then J_1 = 2 pi kappa_pair / c; then the ratio F = (hbar / 2) / J_1, as a number with its band.
  Q2  THE LADDER. The g = 2 class at (J, m) = (hbar / 2, m_e) requires kappa* = hbar c / 4 pi and
      T* = m_e^2 c^3 / 4 pi hbar, hence kappa* / T* = lambda-bar_C^2 and a rope whose strands orbit their centreline at
      the Compton radius under a tension T* = 1.69e-2 J/m. Against the registered ladder (T0 at the M-point; the
      fine tension T_f = T0 / n_sub with n_sub as priced, FND-110; bundles of n ropes, QGATE-005 additivity): is
      there a registered object with kappa / T within a factor 10 of lambda-bar_C^2 AND T within a factor 10 of T*?
      A table of the registered objects with both factors, and one form.
  Q3  THE CARD (a registration, not a verdict): kappa_pair with its derivation and band, proposed for
      docs/ROPE_PARAMETERS.md beside C and gamma; the author registers or not.

## WHAT IS GIVEN (registered inputs; no others enter)
- docs/ROPE_PARAMETERS.md and its verifier benchmarks/foundations/rope_parameter_card.py: T0, mu, w, a, r, C, gamma,
  E, G, with their branches and status; the driver READS the card's benchmark, it does not retype numbers.
- GRV-073 (C = G pi r^4 / 2; G from E with the imported nu = 0.25; the M-point re-evaluation's formulae).
- EM-RECON-017 / 018 (the standoff band d0 / sigma0 in [0.40, 0.46] and what sigma0 is), FND-MATTER-004.
- GRV-018 / GRV-020 (the pitch energy and the Goldstone; the helical ground state tau_0).
- FND-006 (mu = T / c^2); EM-RECON-012 (torsion waves at c); analysis/ELEC_MECH_1_reading.md for J_1 = 2 pi kappa / c.
- FND-110 and the n_sub price sheet for the fine ladder; QGATE-005 for bundles.
- hbar, m_e, c as INPUTS to the comparison (verdict's last unit) and to Q2's kappa*, T*; alpha enters nowhere.
- NOT the PRED-003 chain's "kappa = 2T / a" (a locking stiffness in J/m^2, a different quantity with the same letter;
  the driver names it in a comment and does not use it).

## DESIGN COMMITMENTS (locked at lock)
D1. THE CONTRIBUTIONS to kappa_pair, each a closed form from the card: (i) the tension-geometric term, the extra
    length two strands at radius d0 / 2 acquire when the pair twists at rate Phi' (per strand (1 / 2)(d0 / 2)^2 Phi'^2
    per length, energy T0 times that, two strands): kappa_T = T0 d0^2 / 2 in the (kappa / 2) Phi'^2 convention;
    (ii) the strands' own torsion following the pair's twist: 2 C (both strands) if the frame follows (the rod
    primitive of GRV-009), 0 if it does not; both readings reported, the sum kappa_pair quoted under each;
    (iii) any further registered contribution the worker finds by registry search, named with its claim, or
    "none found" recorded. The convention (kappa / 2) Phi'^2 per length, Phi the pair's azimuth, is fixed.
D2. THE BANDS: d0 over EM-RECON-018's band; C on both registered branches and, if GRV-073's formulae evaluate at
    the M-point, there too; the quoted F carries the full band as [F_min, F_max], and the form is decided by the
    WHOLE band (a band straddling a boundary is the mixed form).
D3. THRESHOLDS, fixed here: KAPPA-MATCH if the whole band of F lies in [0.5, 2]; KAPPA-NEAR if in [0.1, 10] but
    not MATCH; KAPPA-GAP otherwise, with F quoted; KAPPA-HBAR003 is the sub-label of GAP when F lies within a
    factor 3 of 3549 under reading (i) alone (the second route to the same wall). Q2: LADDER-HAS-IT if one registered
    object meets both factor-10 bars; LADDER-LACKS-IT with the two nearest factors otherwise.
D4. NO SOLVER: every number is a closed form of card constants; the only "computation" is arithmetic with bands.

## HARNESS (binding)
Driver and verdict on labkit (Driver / Verdict / Halt); units: inputs (the card read through its benchmark, its
verifier run, every constant sealed with its branch), kappa (D1 i to iii, sealed), confrontation (J_1 and F, the
comparison constants loaded in this unit and nowhere earlier), ladder (Q2's table), verdict (forms from the seals;
the card line of Q3 rendered). CONFIG holds the bands and thresholds. LAB_SMOKE=1 runs the whole path on a
SYNTHETIC card (fabricated constants, different by orders from the registered ones) and prints the bars, no F.

## VALIDATION BARS (halt-grade)
v1. The card's verifier passes (its three invariants) before any constant is read.
v2. D1 (i) reproduces, for a synthetic (T, d0), the closed form T d0^2 / 2 to 1e-12 through the production path;
    D1 (ii) reproduces C = G pi r^4 / 2 from the card's (G, r) to 1e-12.
v3. J_1 = 2 pi kappa / c reproduces, on a synthetic kappa, the ring-wave instrument's J (elec_rope_wave.pieces on
    a ring at Omega = 0, beta_p = 1) to the 48-gon tolerance, so the formula and the instrument agree.
v4. CLEAN ROOM: hbar and m_e appear in the confrontation and ladder units only; the kappa unit's sealed record
    contains neither.

## FORMS (exhaustive; pre-registered)
Q1 (exactly one): KAPPA-MATCH, KAPPA-NEAR, KAPPA-GAP (with the sub-label KAPPA-HBAR003 when D3 says so),
KAPPA-UNDERSPECIFIED (d0 or C not fixed by the registry to within the band D2 needs: the missing item named).
Q2 (exactly one): LADDER-HAS-IT (the object named), LADDER-LACKS-IT (the two factors), LADDER-UNDERSPECIFIED
(n_sub or the bundle rule not fixed enough to score).
Q3: a card line, no form. NO-CALL: v1 to v4 unmet.
Readings written on the results file's face, not formed: MATCH would mean the registered rope already carries the
electron's spin as a winding, a result nobody expects and the author reads before anyone says it aloud; NEAR means
the hbar bridge has a named factor; GAP with HBAR003 means the g = 2 class meets the registry's known wall and the
electron sector's next question is the wall itself, not another candidate.

## NO-RESCUE RULE
No contribution added to D1 after the lock except by registry citation under (iii) found during the inputs unit
and sealed before the kappa unit runs. No band widened. No branch chosen by preference: both branches and the
M-point are reported and the form is decided by the whole band.

## DISCLOSURES
The executor has not computed kappa_pair, J_1 or F from the card; the expectation in WHERE IT STANDS is an
order-of-magnitude judgement from HBAR-003's S_1 and is disclosed as a prior, not a preview. The executor's
instrument elec_rope_wave.py was credentialed with dimensionless kappa_tw values and no registered constant.
The skeptical reviewer judges checklist item I on that.

## BUDGETS
Arithmetic; cpu_hours 1; mem_gb 1; usd 0 beyond drafting and review. Results to analysis/ELEC_KAPPA_1_results.md.

```lab
commission: ELEC-KAPPA-1
target: "Electron sector (blocks the strength-of-magnets row): the twist stiffness kappa_pair of the registered two-strand rope assembled from the parameter card, the angular momentum J_1 = 2 pi kappa / c it quantizes for the one mechanism class that gives g = 2, confronted blind with hbar / 2; and whether any object on the registered tension ladder has kappa / T = lambda-bar_C^2 at the required tension; registers kappa_pair on the card; moves no number in section 2b, and says whether the g = 2 class lives or dies at scale"
driver: benchmarks/lab/elec_kappa_1/driver.py
verdict_script: benchmarks/lab/elec_kappa_1/verdict.py
instrument:
  - benchmarks/foundations/rope_parameter_card.py
  - benchmarks/foundations/elec_rope_wave.py
  - benchmarks/lab/_kit/labkit.py
forms: [KAPPA-MATCH, KAPPA-NEAR, KAPPA-GAP, KAPPA-UNDERSPECIFIED, LADDER-HAS-IT, LADDER-LACKS-IT, LADDER-UNDERSPECIFIED, NO-CALL]
state: [analysis/elec_kappa_1_ckpt.pkl]
budget: {cpu_hours: 1, usd: 0}
mem_gb: 1
```
