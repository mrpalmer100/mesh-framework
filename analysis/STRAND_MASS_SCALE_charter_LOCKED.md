# COMMISSION STRAND-MASS-SCALE -- V_0 IN JOULES, THE TWIST GAP IN eV, AND FND-182's NUMBER
# (CHARTER, LOCKED 2026-10-04 on the author's word, before any number)

North Star line (docs/NORTH_STAR.md section 5): arms a discriminator. ELEC-101 ruled that FND-182's
charge-creation window [1.1e15, 3.2e18] V/m is T2 until its one unpinned input, the kink width w,
is a number, and named the route: pin the strand mass scale in eV. The fourth grant (FND-184, the
contact acts on surfaces) gave the on-site orientation potential V_0 a registered source for the
first time. This commission walks the chain from that source to a number, with the grant's own
falsifier F1 as its kill: if the number lands below the laser record, the reading dies here.

## The chain, stated before computing

  C1  V_sec per crossing: the orientation-dependent part of the surface-gap contact at the
      registered pressing of a class-C contact (FND-129), from the registered contact law
      (A_c, sigma; EM-RECON-023) and the two-strand section's support function with rho the
      strand radius. T-1 gave V_sec/V_line as a function of rho/sigma; the commission evaluates
      it at the registered rho and sigma once each is identified with a registered length (the
      identification is a read owed at lock, not a choice).
  C2  V_0 per unit length: V_sec times the registered crossing density on the strand the kink
      lives on. READ OWED: FND-129 says the FINE weave is contact-free (coverage 7 to 20 percent
      of the tangibility onset); class-C contacts are coarse. The kink of FND-STRAND-002 and the
      charge of FND-182 must therefore live on the coarse strand for V_0 to be nonzero at all.
      If the registered level of the kink is the fine one, C2 returns ZERO and the commission
      renders UNDETERMINED (see forms) rather than moving the kink to a level where contacts
      exist.
  C3  The twist gap: omega_min^2 = V_0 / I_T with I_T = mu r^2 (GRV-073 rod class; mu = T0/c^2;
      r = d_c/2, HBAR-005), per unit length consistently; E_gap = hbar omega_min in eV (hbar
      imported, GRV-014; stated on the number's face).
  C4  The kink width: w^2 = kt / V_0 in the chain's units (FND-STRAND-002, kt = w^2 at unit V_0),
      with kt the registered twist stiffness per node (C_f or the coarse torsional stiffness,
      read owed). w is then a number, with the period-pi re-read of FND-184 applied (two wells
      per 2 pi of material twist).
  C5  FND-182 re-evaluated: E_c = 2 pi T0 r^2 / (5 e w^2 a^2) at the registered scale sets with
      the computed w; confronted with the laser record (about 1e15 V/m, source entered at lock)
      and the Schwinger field 1.32e18 V/m.

## Bars (LOCKED before any number)
B-1  Every length and stiffness in C1 to C4 is a registered value with its claim id, or the
     commission REFUSES at that step; no value is chosen to make a number land.
B-2  Dimensional check of the whole chain by machine (sympy units) before evaluation.
B-3  Scale-set spread carried through: the number is reported at kappa_pack 1 / 50 / 250 and the
     verdict reads the spread, not a point.
B-4  The period-pi re-read is applied before C4 and its effect on w stated.

## Verdict forms (LOCKED)
MASS-SCALE-PRICED      C1 to C5 complete on registered inputs: the strand mass scale is a number
                       in eV, w is a number, and FND-182's E_c is a number (with scale-set spread)
                       above the laser record and below the Schwinger field. Registered; FND-182
                       moves from T2 to a census re-read (ELEC-101 rider); the twist gap enters
                       FND-STRAND-008 as a value.
MASS-SCALE-KILL        E_c lands below the laser record at every scale set (the grant's F1): the
                       reading "the kink is the charge, on this strand, with this contact" dies.
                       Registered Failed and kept; FND-182 Failed; the grant FND-184 takes the
                       falsifier's rider (the grant itself survives only if the kill is traced
                       to the kink's level or the contact density rather than to the surface
                       convention; the commission says which).
MASS-SCALE-ABOVE-QED   E_c lands above the Schwinger field at every scale set: no discriminator
                       (QED breaks the vacuum first); registered as a number with no census
                       promotion; FND-182 stays T2 with the number on its face.
MASS-SCALE-UNDETERMINED C2 returns zero (the kink's registered level is contact-free) or a
                       registered input is missing (B-1): the chain is stated with the gap named;
                       no number is registered; the named next-order is the missing input.
REFUSED                B-2 fails.

## Rules
Bars are bars; no rescue; reads at lock before any number; the laser record entered with its
source; riders the author's; failure kept.

## Reads owed at lock
FND-129 (class-C contacts: level, pressing, coverage; the fine weave contact-free); EM-RECON-023
(A_c, sigma in registered units); HBAR-005 (d_c; rho = d_c/2 or the two-strand geometry's rho);
GRV-073 (I_T); FND-STRAND-002 and ROPE_PARAMETERS section 6 (kt, C_f, the kink's level);
FND-182 and KIN_BREAKDOWN_charter (the E_c chain as registered); the laser record's source.

## Cost
Sandbox; one session for the reads and the chain, one for the numbers.

## Author's lock
Locked on the author's word on 2026-10-04 ("lock STRAND-MASS-SCALE"). No number had been computed.

## READS AT LOCK (done before C1)

FND-129: the contact grant is class C alone; the FINE weave is contact-free (coverage 7 to 20
  percent of the f_c = 0.309 onset); single strands interpenetrate as a primitive (FND-KIN-005,
  magnetism 2.1) with tangibility a density effect at the coverage threshold (FND-MATTER-004).
  The coarse crossing is therefore a SOFT overlap, finite at zero separation, which is exactly
  the shape of EM-RECON-023's law A_c/(1 + (r/sigma)^4); the kink of FND-STRAND-002 and the
  charge of FND-182 are evaluated at the coarse scale sets, so C2 is not zero in principle.
EM-RECON-023 / commission_h_rerun_torsion.py: A_c and sigma are SYMBOLS; no registered value in
  joules or metres anywhere in the registry (searched). This decides C1 under B-1.
FND-KIN-005 / impenetrability_test.py: the "13.8 eV plateau" is a vortex-mode hopping overlap on
  an atomic grid with T = 13.6/S (hydrogen-calibrated); not the vacuum crossing; not used.
HBAR-005: d_c = 1.87e-19 m; r = d_c/2. GRV-073: I_T = mu r^2, C = G pi r^4/2 with G ~ E/2 and
  E = k/(pi r^2), k = 2 T0, giving C = T0 r^2/2 (standard rod mechanics imported, said so there).
FND-MATTER-047: v_t = c/sqrt5, the band route FND-182 used, giving C_band = I_T v_t^2 = T0 r^2/5.
  Two registered twist stiffnesses, ratio 2.5; both carried.
FND-STRAND-002 / FND-KIN-002: w in [0.8, 2.8] by regime; kt = w^2 in units of V_0.
FND-182: E_c = 2 pi T0 r^2/(5 e w^2 a^2) at the three scale sets.
Laser record: 9.1e14 V/m class (Yoon et al. 2021), entered as a class, to be confirmed at any
  registration that depends on it; Schwinger 1.32e18 V/m.
Crossing density per node at the coarse level: NOT registered as a number (FND-091 gives angles).
