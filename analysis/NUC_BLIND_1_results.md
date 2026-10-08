# COMMISSION NUC-BLIND-1 -- RESULTS (the PC, 2026-10-08; each verdict computed once)

Charter: analysis/NUC_BLIND_1_charter_LOCKED.md (locked 2026-10-07 after the author's draw and before any seal).
Draw: seed 92847574954767, drawn by palmer, 50 of 2397 eligible AME2012 rows (A >= 12, Ca-40 excluded); test sha256
4abe4099...; train sha256 7eda8723.... Predictions: benchmarks/nuclear/nuc_blind_1.py from train.txt's Ca-40 row
alone, sealed M1 f0cb0050..., M2 0823ad17... before the truth was read. Verdicts: tools/holdout_verdict.py on the
PC (the only machine holding sealed/test.txt), --unit mass, bars rms <= 0.25 and max <= 0.60 percent of mass;
analysis/holdout/NUC_BLIND_1/VERDICT_M1.json and VERDICT_M2.json kept. Sub-reading: nuc_blind_1_subreading.py.

## VERDICTS: M1 BLIND-AGREES; M2 BLIND-AGREES

| model | form | rms (% of mass) | max abs (% of mass) | worst rows (residual, +: overbound by the model) | sub-reading (N5) |
|---|---|---|---|---|---|
| M1 NUC-018 three-term (a_S/a_V 1.34, a_C 0.7716, a_V 17.770; asymmetry and pairing omitted) | BLIND-AGREES | 0.1209 | 0.2189 | Pu-246 +0.219, Cs-144 +0.207, Fr-224 +0.203, Te-135 +0.190, Ir-194 +0.178 | corr(residual, 23 (N-Z)^2/A) = +0.861 |
| M2 LAMED baseline four-term (a_S/a_V 1.108, a_C 0.7716, a_A 19.85 derived, a_V 15.987; pairing omitted) | BLIND-AGREES | 0.0113 | 0.0262 | O-16 -0.026, Se-87 +0.021, Cs-144 +0.021, As-80 +0.019, Mo-103 +0.019 | corr(residual, pairing indicator) = -0.180 |

50 of 50 held-out rows predicted by both models; nothing BLIND-INCOMPLETE.

## What the result is

The programme's first out-of-sample confrontation in the matter sector: both pre-registered models predict the
masses of 50 isotopes they were never inspected against, from one constant calibrated on Ca-40, inside the
registered accuracy. The scorecard row "Weights of atoms" may now carry "out-of-sample at 0.12/0.22 percent of
mass (M1) and 0.011/0.026 (M2) on 50 held-out isotopes"; its grade stays D3 by the charter (the row is a
calibrated reconstruction, and this commission tells the truth about it, it does not regrade it).

The prior (B-4) was wrong in M1's favour. It said the omitted asymmetry term would push some neutron-rich row of
a table that reaches the drip lines past 0.60 percent of mass. It did not: the worst held-out row (Pu-246,
N - Z = 58) sits at 0.22 percent, and the whole-table range NUC-018 registered (0.00 to 0.51) was an upper
envelope the fresh sample stayed well inside. The sub-reading says why the residual is there at all: it is
0.86 correlated with 23 (N - Z)^2/A, the declared omission (NUC-005), so M1's residual is the asymmetry
energy and nothing else of that size. M2, which carries the derived a_A = 19.85 MeV (NUC-A kinetic + NUC-B
potential), removes it: the residual falls by a factor ten in rms and twenty in max, and what remains is not
pairing-shaped (corr -0.18 with the even-even/odd-odd indicator), so the next omitted term is not the leading
one in what is left. O-16 is M2's worst row and the only negative one of size: the light doubly-magic nucleus
is underbound by the smooth model, as a liquid-drop form without shell terms must.

What this does not do. It is not external adjudication: the draw was the author's (section W1 allows it;
the five numbers' "externally adjudicated predictions" stays 0). It does not change what the models are:
one calibrated constant, derived coefficients, and no claim to the shell structure. It does not score
NUC-005 as registered (d0 = 1.9, ratio 1.108); it scores the two models the charter named.

## Consequences (riders on the author's word)

NUC-018: rider: scored blind under bar W on 50 held-out AME2012 isotopes (author's draw, seed 92847574954767):
  BLIND-AGREES at rms 0.121 and max 0.219 percent of mass; residual 0.86 correlated with the declared
  asymmetry omission; the inspected-table range 0.00 to 0.51 was an envelope the fresh sample stayed inside.
NUC-005: rider: the declared omission (about 23 (N-Z)^2/A overbinding of neutron-rich nuclei) is what the
  blind residual of the corrected model is (corr +0.86 on 50 held-out rows); the omission is confirmed as
  the leading missing term out of sample.
NUC-A and NUC-B: rider: the derived a_A = 19.85 MeV, scored for the first time off the inspected set
  (LAMED's baseline form, a_V on Ca-40 only): BLIND-AGREES at rms 0.0113 and max 0.0262 percent of mass on
  50 held-out isotopes; the residual is not pairing-shaped (corr -0.18).
docs/SM_EMERGENCE.md / scorecard row "Weights of atoms": add the out-of-sample line; grade D3 unchanged.
docs/NORTH_STAR.md 2b: five numbers unchanged (externally adjudicated 0; the draw was the author's).
No status change on any claim.

## Named next-order (not chartered)

NUC-BLIND-2: the same draw cannot be reused (one look); a second draw with a different seed held by someone
other than the author would turn this row's out-of-sample line into the programme's first externally
adjudicated prediction (the fifth of the five numbers, from 0 to 1). Cheap: the same two sealed models,
or M2 alone, at the same bars. The author decides who holds the seed.
