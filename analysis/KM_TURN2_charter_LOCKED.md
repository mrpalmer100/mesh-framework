# COMMISSION KM-TURN-2 -- DOES THE RESONANT BRANCH CONTINUE PAST THE CROSSING?
# (CHARTER, LOCKED 2026-09-22 on the author's word; before any new solve)

## Question
KM-TURN found two branches crossing at A2 ~ 0.00733: R (resonant, f_dir ~0.60,
rate ~1.36e-3, om2 = -Om1/4) and N (non-resonant, f_dir ~0.45, rate ~0.93e-3,
om2 detuned). The forward march turned from R onto N there. Does R continue
beyond the crossing, and is it still flat?

## Protocol (the PC)
Seed pair: the sealed KERNEL-MARCH states p44 (A2 0.00702) and p45 (0.00713),
both on R below the crossing. First predictor: an extended tangent step so the
predictor lands on the far side of the singular point; then the ordinary
bordered arc march at ds 0.08 for 11 more points (12 total, to A2 ~0.0088),
measurements sealed. PLAIN-SOLVER CONTROL every 4th point (p3, p7, p11): 10 GN
rounds from the gated state, rms recorded.
THRESHOLDS, set from the sealed forward data's own scale (KM-TURN lesson):
  "on R"  = rate > 1.15e-3 AND f_dir > 0.53 AND |om2 + Om1/4| < 1.5e-4
  "on N"  = rate < 1.15e-3 AND f_dir < 0.53
  "flat"  = C1 f_dir rise (last 4 vs first 4) < +0.15

## Verdict forms (LOCKED)
R-CONTINUES-FLAT: the first point lands on R and >= 10 of 12 points gate on R
                  and flat.
R-CONTINUES-TURNS: lands on R, then leaves it or C1 rise >= +0.15.
R-NOT-FOUND:      the first point lands on N or refuses.
R-REFUSED:        fewer than 6 points gate.

## Rules
No rescue; q-sweep bars; the bordered solver (FND-175) and the plain solver
for controls; one machine; verdict once; FND-177 riders inherited.

## AMENDMENT (2026-09-22, before any solve): the first predictor step is 3 ds
## (0.24), not 2 ds. Measured from the sealed states: the 2 ds predictor
## (A2 0.00740) sits 2.97e-4 (one forward step) from the nearest N state; the
## 3 ds predictor (A2 0.00751) sits 4.83e-4 (1.5 steps) from N; 4 ds (0.00761)
## 7.1e-4 but begins to overshoot R's own curvature. 3 ds is the compromise.
## Forms unchanged.
