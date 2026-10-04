# COMMISSION STRAND-MASS-SCALE -- RESULTS (sandbox, 2026-10-04; verdict computed once)

Charter: analysis/STRAND_MASS_SCALE_charter_LOCKED.md (locked 2026-10-04 before any number). Instrument:
benchmarks/foundations/strand_mass_scale.py (sympy chain, dimensional check, displays); log
analysis/STRAND_MASS_SCALE_run.log; sealed analysis/strand_mass_scale.npz.

## VERDICT: MASS-SCALE-UNDETERMINED

C1 is refused under B-1. The surface-contact grant gives V_0 a registered SOURCE (the orientation
part of the crossing contact summed over a strand's crossings), but the registry does not hold
the three numbers the source needs: the contact law's amplitude A_c in joules and range sigma in
metres (both are symbols in EM-RECON-023 and in commission_h_rerun_torsion.py; they were never
given physical values), and the crossing density per node of the coarse weave. The one registered
contact energy with a number, FND-KIN-005's "13.8 eV plateau", is a vortex-mode overlap in an
atomic-scale toy calibrated to hydrogen's 13.6 eV; it is not the vacuum crossing and the
commission did not use it. No value was chosen (B-4). V_0 is carried as a symbol through C2 to
C5, and the chain below is exact.

## What the chain established (exact, dimensionally checked by machine)

With I_T = mu r^2 per unit length (mu = T0/c^2, r = d_c/2) and the twist stiffness per node
kt_node = C/a:

  w^2 = kt_node / V_0 = T0 r^2 / (2 a V_0)      (rod route, GRV-073: C = T0 r^2/2)
  omega_min^2 = V_0 / (I_T a) = V_0 c^2 / (T0 a r^2)
  E_c = 2 pi T0 r^2 / (5 e w^2 a^2) = (4 pi / 5) V_0 / (e a)

The last line is the commission's one new identity: the charge-creation field is the orientation
well depth per node divided by the charge times the node spacing, times 4 pi/5. FND-182's "one
unpinned input w" and the grant's "V_0 to be priced" are the same unknown, and the field reads
it directly: E_c e a = (4 pi/5) V_0, the work the field does on one charge over one spacing equals
0.8 pi times the well it must lift the strand's face out of. Two registered twist stiffnesses
per node exist (rod route T0 r^2/(2a), GRV-073; band route T0 r^2/(5a), FND-MATTER-047, the one
FND-182 used); they differ by 2.5 and both are carried in the displays.

## Displays (no claim; the registered w bracket re-expressed; hbar imported on the eV line)

| scale set | route | w | V_0 per node | hbar omega_min | E_c (V/m) |
|---|---|---|---|---|---|
| kappa_pack 1 | rod | 0.8 to 2.8 | 0.31 to 0.025 eV | 2.9 to 0.83 GeV | 1.3e16 to 1.1e15 |
| kappa_pack 1 | band | 0.8 to 2.8 | 0.12 to 0.010 eV | 1.8 to 0.53 GeV | 5.2e15 to 4.2e14 |
| kappa_pack 50 | rod | 0.8 to 2.8 | 4.2 to 0.34 eV | 10.7 to 3.1 GeV | 6.5e17 to 5.3e16 |
| kappa_pack 250 | rod | 0.8 to 2.8 | 12.2 to 1.0 eV | 18.3 to 5.2 GeV | 3.2e18 to 2.6e17 |

Read at face value and nothing more: if the strand's kink lives in the registered coasting regime
(w in [0.8, 2.8]), the orientation well is a fraction of an electron-volt to a dozen electron-volts
per node (against 1.6e5 eV per node of tension energy, T0 a, at kappa_pack 1), and the twist gap,
with hbar imported, is a GeV-class frequency. That the strand mass scale lands in the GeV class,
the nucleon's class, is RECORDED and NOT READ (the price-sheet rule: a number that lands is not a
mechanism; here nothing even landed, since V_0 is unpinned and the display merely re-expresses the
registered w bracket). What a discriminator would need: V_0 between 0.022 eV (E_c at the laser
record) and 31.5 eV (E_c at Schwinger) per node at kappa_pack 1. The window FND-182 registered
survives unchanged; what changed is that it is now a window on a contact energy with a registered
source rather than on a kink width with none.

## What is missing, named (the next-order is these three inputs, nothing else)

  1. A_c, the crossing overlap energy of two vacuum strands at the coarse level, in joules. The
     registered contact law has the shape; the amplitude was never priced. Route: the registered
     interpenetration energetics (FND-KIN-005's form, FND-MATTER-004's density reading) evaluated
     for two coarse strands with the registered tension, not an atomic calibration.
  2. sigma, the range of that contact, in metres (the candidate identifications are d_c and a;
     a read, then a registration, not a choice inside a commission).
  3. The crossing density per node of the coarse weave (FND-091's angles give the geometry; the
     count per spacing is a derivation from them).
With all three, V_sec/V_line from T-1 at rho/sigma gives V_0 in joules and the chain above closes
to a number in one afternoon; falsifier F1 of the grant record (E_c below the laser record) is
then live.

## Consequences (riders on the author's word)

FND-182: rider carrying the identity E_c = (4 pi/5) V_0/(e a) and the restatement of its unpinned
input (V_0, sourced by FND-184, three registered inputs short). FND-STRAND-008: rider carrying
omega_min^2 = V_0 c^2/(T0 a r^2) and the display class. FND-184: rider recording the first use and
the three inputs it needs to cash out. ELEC-101: FND-182 stays T2; the window is unchanged.
No new claim registered unless the author wants the identity on its own id.
