# COMMISSION KIN-BREAKDOWN -- WHAT FIELD BREAKS THE MESH VACUUM, AND DOES IT AGREE WITH THE REGISTERED ONE?
# (CHARTER, LOCKED 2026-09-27 on the author's word ("lock KIN-BREAKDOWN"), before any number was computed)

North Star line (docs/NORTH_STAR.md section 5): serves the "Also carried" row with a number
against a known scale. KIN-DRIVE (FND-181) derived that the strand's vacuum ceases to exist
above a strain gradient of 1/c_L in the chain's units, because the lock's uniform torque
tilts the orientation potential past its maximum. The corpus already registers a vacuum
breakdown field on the electromagnetic side, E_crit = 2.0e23 V/m (FND-031, EM-021), and QED
has the Schwinger scale, 1.3e18 V/m. This commission converts the kink-vacuum breakdown to
volts per metre with registered objects only and confronts it with both, and with the
highest field ever applied to vacuum without breakdown. It either finds two independent
mesh routes agreeing (the strongest internal evidence the house recognizes), or it finds
one of the two readings of "the vacuum's electric limit" wrong, or it finds the number
already excluded by laser data. All three are results.

## The derivation, stated before computing

In the chain's units the drive on the azimuth is F = c_L eps' per site, the orientation
potential has unit amplitude, and sin(phi) = F has no solution above F = 1. In physical
units the on-site amplitude per unit length is V_0, so breakdown is at c_L eps'_c = V_0.
KIN-DRIVE also fixed the force on a winding, F_kink = 2 pi c_L eps', and a winding carries
charge e, so the electric field is E = 2 pi c_L eps' / e (joules per coulomb per metre).
Therefore

    E_c = 2 pi V_0 / e,

the breakdown field is the orientation potential's amplitude per unit length, times 2 pi
over the charge. V_0 is fixed by the registered twist band: the gap is the strand mass
scale omega_min with omega_min^2 = V_0 / I_T (FND-STRAND-008: every mode has a mass, gap
exactly the strand mass scale), I_T = mu r^2 the rod's polar moment (FND-MATTER-047,
GRV-073), and the band's speed fixes omega_min through the kink width: c_t = w a omega_min
(the chain's kt = w^2 with c_t = w nodes per unit time, FND-STRAND-002), so

    V_0 = I_T v_t^2 / (w^2 a^2),   E_c = 2 pi mu r^2 v_t^2 / (e w^2 a^2) = 2 pi T0 r^2 / (5 e w^2 a^2)

with v_t = c/sqrt5 (FND-MATTER-047), mu = T0/c^2, r = d_c/2 (HBAR-005), a the node spacing
of the strand the kink lives on, and w the kink width in nodes. Every symbol is registered
except w, which the registry brackets by regime (w = 0.8 self-traps, w >= 2 coasts,
FND-STRAND-002/FND-KIN-002) but does not pin. The commission therefore reports E_c as a
function of w at each registered scale set, and the w that E_crit and the Schwinger field
would each require.

## Registered parts list (reads owed at lock marked [R])

  FND-181 (the breakdown gradient 1/c_L and the force 2 pi c_L eps'); FND-STRAND-008 [R]
  (the on-site potential's form and that its gap is the strand mass scale); FND-STRAND-002
  and FND-KIN-002 [R] (the w regimes and what a is on the strand: node spacing at the
  coarse level a = 6.0e-17 m, or the fine level a_f under FND-087's n_sub); FND-MATTER-047
  (v_t/c = 1/sqrt5) and GRV-073 (rods); HBAR-005 (d_c = 1.87e-19 m); EM-018 (E is the
  strain gradient's channel); FND-031 and EM-021 [R] (E_crit = 2.0e23 V/m: its provenance
  and what it is a breakdown OF, so the comparison is like with like); the three registered
  scale sets (ROPE_PARAMETERS: kappa_pack 1 / 50 / 250 with T0 434 / 1599 / 2734 J/m and
  a 6.0e-17 / 1.63e-17 / 9.53e-18 m). External, entered with sources at lock: the Schwinger
  field 1.32e18 V/m; the highest laser field applied to vacuum without observed breakdown
  (of order 1e15 V/m at the 1e23 W/cm^2 class; the exact record and source are entered at
  lock, not from memory).

## Protocol (sandbox; derivation and arithmetic, one session)

  S1. Derive E_c symbolically as above, with the chain-unit to physical-unit map written
      out and checked dimensionally by machine.
  S2. Evaluate E_c(w) at the three scale sets, coarse level; then at the fine level with
      T0_f = T0/n_sub, a_f, r_f for the registered n_sub bracket (display, since n_sub is
      an absolute-scale unknown).
  S3. Solve for the w that gives E_c = E_crit and E_c = E_Schwinger at each scale set.
  S4. Confront: is E_c(w) for any registered-regime w (w in [0.8, 2.8]) below the highest
      field applied to vacuum without breakdown? Is it within the scale-set spread of
      E_crit?
  S5. Accounting: the tier verdict by the census rule (a breakdown field that agrees with
      E_crit is an internal consistency; one that differs from QED's Schwinger field in a
      reachable range is a discriminator candidate; one below laser data is a kill).

## Bars (LOCKED before computing)

B-1  Dimensional check of E_c by machine (sympy units) passes, or REFUSED.
B-2  "Agrees with E_crit": E_c at some w in [0.8, 2.8] lies within the scale-set spread of
     E_crit (the kappa_pack 1 to 250 range of both numbers), at the same level (coarse or
     fine) for both.
B-3  "Below data": E_c at EVERY w in [0.8, 2.8] and every registered scale set is below
     the highest applied field entered at lock, by more than the scale-set spread.
B-4  No w is chosen to make a number land; the w-dependence is the report.

## Verdict forms (LOCKED)

BREAKDOWN-AGREES:      B-2 holds: two independent mesh routes to the vacuum's electric
    limit agree within the registered brackets; registered as an internal consistency with
    the w it implies, which becomes a registered bracket on the kink width.
BREAKDOWN-DISAGREES:   B-2 fails and B-3 fails: the kink-vacuum limit and E_crit are
    different numbers in a range no data yet reaches. One of the two readings is wrong or
    they are limits of different things; registered with both numbers and the difference
    named; if E_c lies between laser data and the Schwinger field, it is a DISCRIMINATOR
    CANDIDATE for the census (vacuum breakdown below QED's prediction).
BREAKDOWN-BELOW-DATA:  B-3 holds: the mesh vacuum, read as a kink chain at any registered
    regime, would already have broken down in fields that have been applied. Registered
    as Failed and kept; the reading that dies is named (the strand-level kink as the
    charge, at the coarse level; or the scale set).
BREAKDOWN-UNDETERMINED: the w-dependence spans all three outcomes across [0.8, 2.8]; the
    report is E_c(w) with the w that each outcome needs, and the pinning of w becomes the
    named next-order.
REFUSED:               B-1 fails.

## Rules

Bars are bars; no rescue; the formula is derived before any number is evaluated; external
values entered with sources at lock and never adjusted; failures kept; riders the author's.

## Reads owed at lock

FND-STRAND-008 (on-site potential form and gap); FND-STRAND-002 / FND-KIN-002 (w regimes,
node spacing); FND-031 / EM-021 (E_crit provenance: breakdown of what); FND-087 (n_sub
bracket); HBAR-005 (d_c). External: the Schwinger field; the laser record.

## Cost

Sandbox, one session, no machine time.

## Author's lock

Locked on the author's word on 2026-09-27. No number was evaluated before this line was written.

## READS AT LOCK (executed 2026-09-27 before any number)

1. FND-031 / EM-021: E_crit = 2.0e23 V/m is the field at which the MESH'S LINEAR RESPONSE
   FAILS (the Kerr-class nonlinearity onset, QGATE-009's confrontation 3: "the mesh remains
   linear through all known fields"), sitting 1.5e5 above the Schwinger field. It is NOT a
   charge-creation threshold. The kink-vacuum breakdown of FND-181 is a winding-creation
   threshold, the mesh analogue of pair creation. So E_crit and E_c are limits of DIFFERENT
   things; a mismatch between them is not a contradiction, and the like-with-like
   comparison is with the Schwinger field. Recorded before computing; bar B-2 is kept as
   written (it can still pass or fail) but the form BREAKDOWN-DISAGREES is read with this
   note on its face.
2. FND-STRAND-008: on-site orientation potential, gap exactly the strand mass scale,
   omega_min = 1 in engine units; band top sqrt(1 + 4 kt). As attributed. The unit map:
   energy per site V_0 (1 - cos phi) + (C/2a)(Delta phi)^2, so kt = C/(V_0 a); time unit
   sqrt(I_T a / V_0); torsion speed v_t = w sqrt(V_0 a / I_T); hence V_0/a = I_T v_t^2/(w^2 a^2).
3. FND-STRAND-002 / FND-KIN-002: w = 0.8 self-traps, w = 2.0 free drift (loss below 1e-3
   over 185 sites), w = 2.8 coasts; the registered regime bracket is w in [0.8, 2.8] with
   the physical charge-carrying regime w >= 2 (free). The node spacing at the coarse level
   is a; the fine level needs n_sub (FND-087, absolute-scale class): display only.
4. HBAR-005: d_c = 1.87e-19 m (thickness), r = d_c/2. As attributed.
5. FND-087: n_sub is an underived absolute-scale parameter; the fine-level value of E_c
   scales as T0_f r_f^2 / a_f^2 and is not evaluated beyond that statement.
6. External (entered here, from memory, sources named for verification at paper sync):
   Schwinger field E_S = m_e^2 c^3/(e hbar) = 1.32e18 V/m. Highest laser intensity applied
   to vacuum: 1.1e23 W/cm^2 (Yoon et al., Optica 8, 630, 2021, CoReLS), peak field
   E = sqrt(2 I/(c eps0)) = 9.1e14 V/m, no vacuum breakdown observed.
Outcome: one interpretive note (item 1), no bar moved, no form changed. Computation may begin.
