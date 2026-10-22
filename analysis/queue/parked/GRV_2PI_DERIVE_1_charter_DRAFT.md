# COMMISSION GRV-2PI-DERIVE-1 -- THE COEFFICIENT IN g_dagger = kappa c^2 / L FROM THE GEOMETRY OF A MEDIUM OF FIXED EXTENT
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; a DERIVATION commission; the derivation does not exist;
# no rotation-curve data is read by this commission)

## 1. The target, and the North Star line

Question key: grv-gdagger-coefficient-derivation.

The predictions paper states Prediction 1 as g_dagger = c H0 / 2 pi = c^2 / (2 pi R_H) and says in the same breath,
as an honest caveat, that "the 2 pi is motivated by horizon-sphere geometry but is not uniquely forced; the
alternative c H0 / 6 performs comparably against SPARC", and lists the coefficient among the inputs that "rest on
empirical choices, not derived". XSEC-001 then read g_dagger as c^2 / (2 pi L) with L the medium's FIXED extent,
and XSEC-002 found it universal across SPARC. So the sector's best number carries one undefended pure number. This
commission asks the theorist to derive it: the dimensionless coefficient kappa in g_dagger = kappa c^2 / L, from
the registered statics of a local elastic medium of finite extent L, as the limit of a computation.

TARGET. A pure number kappa, with the construction that produces it: the registered response's acceleration scale
is where the source's conditioning field (GRV-005) meets the medium's finite extent (XSEC-001); the theorist must
state what geometric or mechanical quantity of a medium of extent L sets the crossover acceleration (a sphere's
circumference, a solid angle, a mode count, a mean path, a boundary condition of the Poisson problem at r = L, or
something else), compute kappa from it with no fitted input, and show that the result is independent of every
lattice-scale quantity (kappa may depend on nothing but the construction's pure geometry). Reference values the
harness records, not forms: 1/(2 pi) = 0.159155 (the paper's choice) and 1/6 = 0.166667 (the paper's named
alternative), and the g_dagger each implies at H0 = 67.4 and 73.0 km/s/Mpc.

North Star line (section 5, rule (c)): the gravity row's D1 number has a coefficient the paper itself marks as
chosen; deriving it, or showing it cannot be derived from the registered statics, changes the row's standing
without moving any number in section 2b. A NOT-DERIVED with the obstruction named is a result.

What this commission does NOT do: it does not derive nu (GRV-NU-DERIVE-1); it does not test kappa against SPARC
(the predicted g_dagger has been tested, GRV-030, GRV-BLIND-1/2, and the two candidates are known to perform
comparably there, so a data test discriminates nothing at present scatter); it does not choose between 2 pi and 6.

## 2. Premises (the only things the derivation may rest on) and forbidden inputs

Premises, by claim id:
- GRV-005: local elastostatics; forced Poisson equation for the scalar sector; the 1/r conditioning field.
- GRV-006: G is the medium's rigidity c^4 / (4 pi G); the medium's stiffness enters only through G.
- GRV-029: the medium dictionary and the metric bijection.
- GRV-028/029: no galaxy-scale scalar.
- XSEC-001: g_dagger = kappa c^2 / L with L the medium's fixed extent; g_dagger does not evolve.
- GRV-030: the deep limit g_obs -> sqrt(g_bar g_dagger) (the meaning of the scale) and that g_dagger's measured
  value is c H0 / 2 pi to 4.5 percent (the theorist may use that the coefficient is of order 1/(2 pi); it may NOT
  choose kappa to match it).
Forbidden: SPARC or any rotation-curve data; any literature argument that sets a_0 ~ c H0 (the theorist may
compare in the document after deriving); any constant chosen to land on 1/(2 pi) or 1/6; the measured value of
g_dagger as a step.

## 3. The sealed input

None.

## 4. The interface the module must export (benchmarks/lab/grv_2pi_derive_1/derivation.py)

- STATUS, ASSUMPTIONS, OBSTRUCTION as in the derivation kind.
- KAPPA: float, the derived coefficient.
- kappa_from_construction(n): the coefficient computed from the stated construction at resolution n (modes,
  shells, integration points, lattice sites, as the document defines), converging to KAPPA as n grows.
- g_dagger(c, L, a): the acceleration scale for light speed c, extent L and lattice spacing a, computed from the
  construction (a is accepted so the harness can check it does not enter).
- CONSTRUCTION: one sentence naming the geometric or mechanical quantity kappa is, and what n counts.

## 5. The checks (locked here; numeric; nothing read from any run)

C-1 form: g_dagger(c, L, a) = KAPPA c^2 / L to relative 1e-9 for (c, L) in a 3 x 3 grid of c in {1, 3e8, 1e9}
and L in {1, 1.32e26, 1e30}, at a = 1e-35 (homogeneity of degree 2 in c and -1 in L).
C-2 lattice independence: g_dagger(3e8, 1.32e26, a) varies by less than 1e-9 relative over a in {1e-40, 1e-35,
1e-30, 1e-20}.
C-3 convergence: d_n = |kappa_from_construction(n) / KAPPA - 1| over n in {16, 64, 256, 1024, 4096} is decreasing
and d_4096 <= 1e-4.
C-4 positivity and range: 0.01 <= KAPPA <= 10.
C-5 no parameter: the module reads no file, environment variable or argument beyond those in section 4; the
harness imports it in an empty directory with numpy only; the construction names every constant as a pure number
(the derivation reviewer audits this; the harness cannot).
C-6 the reference distances (RECORDED, NOT FORMED): |KAPPA - 1/(2 pi)| / (1/(2 pi)) and |KAPPA - 1/6| / (1/6);
the implied g_dagger at H0 = 67.4 and 73.0 km/s/Mpc with L = c / H0.
C-7 import: numpy only, under 5 s; kappa_from_construction(4096) under 120 s.

## 6. The harness and the verdict

The driver (benchmarks/lab/grv_2pi_derive_1/driver.py) imports the module, runs C-7 then C-1 to C-6, records each
check's result with its worst number, STATUS, ASSUMPTIONS, OBSTRUCTION, CONSTRUCTION, KAPPA, the C-6 distances
and implied values, and the module's sha256 in analysis/grv_2pi_derive_1_ckpt.pkl (atomic), and prints
"GRV-2PI-DERIVE-1 COMPLETE -- run the verdict"; it never prints FORM lines. The verdict script reads the
checkpoint only and renders NOT-DERIVED if STATUS is NOT-DERIVED or any of C-1 to C-5, C-7 failed (naming them);
DERIVED-CONDITIONAL if all passed and ASSUMPTIONS is non-empty; DERIVED if all passed and ASSUMPTIONS is empty.
It prints KAPPA and the C-6 lines, adding "coincides with 1/(2 pi) to <d>" or "coincides with 1/6 to <d>" when a
distance is below 1e-3, and otherwise "a third value", recorded, not formed.

## 7. Verdict forms, and what follows

FORM (Q1): NOT-DERIVED / DERIVED-CONDITIONAL / DERIVED.
Readings: DERIVED at 1/(2 pi) retires the paper's caveat; DERIVED at 1/6 or at a third value is a prediction that
differs from the registered one by a factor the present SPARC scatter cannot resolve (the paper says so), so the
registered value stands until a sharper instrument exists and the derived value is filed beside it as the
framework's own; NOT-DERIVED says the registered statics do not fix the crossover's coefficient, which is what the
paper already says, now with the obstruction named.

## 8. Smoke discipline (binding on the drafting worker)

The harness is smoke-tested on a stub under benchmarks/lab/grv_2pi_derive_1/scratch/ with KAPPA = 1/(2 pi),
kappa_from_construction(n) = KAPPA (1 + 1/n), g_dagger = KAPPA c^2 / L, so that C-1 to C-4 pass and C-6 reports
coincidence; and on a second stub whose g_dagger carries a factor (a / 1e-35)^0.01, so that C-2 fails; both
uncommitted. No run touches any data.

## 9. Budgets and disclosures

Theorist budget derive; harness cpu_hours 0.1; mem_gb 1; usd 0. Disclosed to the theorist: the paper's caveat in
full, including the 1/6 alternative and that both perform comparably; XSEC-001's extent reading. The theorist is
told that landing on either reference value by choice renders nothing (C-5, the reviewer's audit), and that a
third value is an acceptable outcome.

```lab
commission: GRV-2PI-DERIVE-1
kind: derivation
target: "Gravity row D1 (NORTH_STAR section 2): the coefficient kappa in g_dagger = kappa c^2 / L derived from the registered statics and the medium's fixed extent (GRV-005/006/029/028/XSEC-001) as the limit of a computable construction, or stopped at a named obstruction; moves no number"
premises: [GRV-005, GRV-006, GRV-029, GRV-028, XSEC-001, GRV-030]
driver: benchmarks/lab/grv_2pi_derive_1/driver.py
verdict_script: benchmarks/lab/grv_2pi_derive_1/verdict.py
derivation_module: benchmarks/lab/grv_2pi_derive_1/derivation.py
derivation_doc: analysis/lab/derivations/GRV-2PI-DERIVE-1.md
instrument:
  - benchmarks/gravity/grv_blind_1.py
forms: [NOT-DERIVED, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/grv_2pi_derive_1_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
