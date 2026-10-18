# COMMISSION GRV-NU-DERIVE-1 -- THE INTERPOLATION FUNCTION nu(y) FROM THE HORIZON COUPLING
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; a DERIVATION commission; the derivation does not exist;
# no rotation-curve data is read by this commission)

## 1. The target, and the North Star line

Question key: grv-nu-shape-derivation.

The gravity row's D1 content is the acceleration scale g_dagger = c H0 / 2 pi (GRV-030), carried by the horizon
channel alone (GRV-028/029). The SHAPE of the response, nu(y) with y = g_bar / g_dagger, is empirical: GRV-030
found the paper's tanh family underoperationalized, GRV-031 stated the corpus-natural candidate first (strand
alignment against horizon-scale randomization, the Langevin saturation law mu(x) = coth(3x) - 1/(3x), the 3 fixed
by the deep-MOND asymptotic) and it lost to the simple interpolation nu(y) = 1/(1 - exp(-sqrt y)) by 0.0151 dex,
crossing the locked RETIRE bar, so Prediction 4 is retired and the registered nu is the one the data chose. That
is where the sector stands: the scale is predicted, the shape is fitted. This commission asks the theorist for the
shape, derived.

TARGET. A function nu(y), y > 0, computed from a stated construction in the registered medium (the horizon
coupling of a local elastic medium of fixed extent L = c / H0, XSEC-001, in which the galaxy-scale response is the
medium's reaction to a source's conditioning field, GRV-005, with no galaxy-scale scalar, GRV-028/029), with no
free parameter beyond g_dagger itself, such that: nu(y) -> 1 as y -> infinity (Newtonian); y nu(y) -> sqrt y as
y -> 0 (the deep limit that gives g_dagger its meaning, g_obs -> sqrt(g_bar g_dagger), which GRV-030/031 used to
fix constants and which the registered nu obeys); nu is monotone decreasing and smooth; and the construction is
one the harness can evaluate numerically at increasing resolution and see converge to the closed form. Whether the
derived nu beats the registered one on SPARC is NOT this commission's question; it is the successor measurement
commission GRV-NU-TEST-1 (section 7), locked only if this one renders DERIVED or DERIVED-CONDITIONAL.

North Star line (section 5, rule (c)): the gravity row's D1 observable is the scale; a derived shape that then
survives GRV-NU-TEST-1 would be a second D1 number from the same channel. Moves no number in section 2b. A
NOT-DERIVED with the obstruction named is a result: it says what the horizon coupling's statics do not yet fix.

What this commission does NOT do: it does not derive g_dagger or its coefficient (GRV-2PI-DERIVE-1); it reads
no data; it does not re-test the retired candidates (GRV-031 stands); it does not decide the shape against
SPARC.

## 2. Premises (the only things the derivation may rest on) and forbidden inputs

Premises, by claim id:
- GRV-005: local elastostatics; the conditioning field of a mass-knot is a static strain field whose scalar sector
  obeys the forced Poisson equation; 1/r far field.
- GRV-029: the medium dictionary (T = AB, mu = B^3 / A, c_local = A / B) and the exact bijection between the
  transverse wave operator's four coefficient functions and the static metric; no fifth function.
- GRV-028/029: no galaxy-scale scalar; the horizon coupling is the only galaxy-scale channel.
- XSEC-001/002: g_dagger = c^2 / (2 pi L), L the medium's FIXED extent, universal across galaxies.
- GRV-030: the empirical nu and the deep-MOND asymptotic as the registered meaning of g_dagger (the theorist may
  use the asymptotics as targets; it may NOT use the registered nu's functional form as a step).
- GRV-031: the Langevin candidate and the tanh family are retired; the alignment-versus-randomization picture
  that produced the Langevin law is on the record as a construction that gives the wrong shape, and the theorist is
  told so (disclosure, section 9), so that a derivation ending at coth(3x) - 1/(3x) knows it has re-derived a
  retired result (recorded, not formed, section 6).
Forbidden: SPARC or any rotation-curve data; any MOND interpolation function from the literature used as a step
or a target (comparison in the document after deriving is permitted); any constant chosen to make a check pass;
the registered nu's closed form as an input.

## 3. The sealed input

None.

## 4. The interface the module must export (benchmarks/lab/grv_nu_derive_1/derivation.py)

- STATUS, ASSUMPTIONS, OBSTRUCTION as in the derivation kind.
- nu(y): numpy array in, array out; the derived function in closed form (or as a numerically solved function of
  y alone, with no parameter).
- nu_from_construction(y, n): the same function evaluated from the stated construction at resolution n (a
  number of modes, strands, lattice sites, integration points, or iterations, as the document defines it), so that
  nu_from_construction(y, n) -> nu(y) as n grows. This is the anti-manufacture requirement: the closed form must be
  the limit of a computation the harness can run, not a formula typed in.
- CONSTRUCTION: one sentence naming what n counts.

## 5. The checks (locked here; numeric; nothing read from any run)

C-1 Newtonian limit: |nu(y) - 1| <= 1e-3 at y = 1e4 and <= 1e-4 at y = 1e6.
C-2 deep limit: |y nu(y) / sqrt y - 1| <= 2e-2 at y = 1e-4 and <= 5e-3 at y = 1e-6.
C-3 monotone and smooth: on a log grid of 400 points in [1e-6, 1e6], nu is non-increasing (no increase larger
than 1e-10 relative) and finite, with no NaN.
C-4 convergence of the construction: at y in {0.01, 0.1, 1, 10, 100}, the sequence
d_n = max_y |nu_from_construction(y, n) / nu(y) - 1| over n in {16, 64, 256, 1024} is decreasing and d_1024 <= 1e-3.
C-5 no parameter: the module must not read any file, environment variable or argument beyond y and n; the harness
imports it in an empty directory with numpy only; the document's construction must name every constant and each
must be a pure number fixed by the construction (the harness cannot check this; the derivation reviewer must).
C-6 distance from the registered nu (RECORDED, NOT FORMED): max over the C-3 grid of |nu(y) / nu_reg(y) - 1| with
nu_reg = 1/(1 - exp(-sqrt y)); and the same against the retired Langevin law (coth(3 sqrt y) - 1/(3 sqrt y))^-1
form as GRV-031 wrote it in the nu convention (the harness states the convention it used).
C-7 import: numpy only, under 5 s, reads no file; nu on 400 points under 10 s; nu_from_construction at n = 1024 on
5 points under 120 s.

## 6. The harness and the verdict

The driver (benchmarks/lab/grv_nu_derive_1/driver.py) imports the module, runs C-7 then C-1 to C-6, records each
check's pass or fail with its worst number, STATUS, ASSUMPTIONS, OBSTRUCTION, CONSTRUCTION, the C-6 distances, and
the module's sha256 in analysis/grv_nu_derive_1_ckpt.pkl (atomic), and prints "GRV-NU-DERIVE-1 COMPLETE -- run
the verdict"; it never prints FORM lines. The verdict script reads the checkpoint only and renders NOT-DERIVED if
STATUS is NOT-DERIVED or any of C-1 to C-5, C-7 failed (naming them); DERIVED-CONDITIONAL if all passed and
ASSUMPTIONS is non-empty; DERIVED if all passed and ASSUMPTIONS is empty. It prints the C-6 distances with the
sentence "coincides with the registered nu to <d>" or "coincides with the retired Langevin law to <d>" when either
distance is below 1e-3, recorded, not formed.

## 7. Verdict forms, and the successor

FORM (Q1): NOT-DERIVED / DERIVED-CONDITIONAL / DERIVED.
Successor: on DERIVED or DERIVED-CONDITIONAL, the author or the lab drafts GRV-NU-TEST-1, a measurement commission
that scores the derived nu at the predicted g_dagger on the 2788 SPARC points against the registered nu's 0.1421
dex, with the predictions paper's standing bar (a shape enters the paper only if it beats 0.1421 + 0.003 dex) and
GRV-031's PAID / RETIRE bars carried unchanged; the derived nu is frozen by this commission's commit before that
charter is written. A derived nu that coincides with the registered nu to 1e-3 would make GRV-NU-TEST-1 moot and
the registered shape a derived one; a derived nu that coincides with the retired Langevin law has re-derived a
result the data already rejected, and GRV-NU-TEST-1 is not drafted.

## 8. Smoke discipline (binding on the drafting worker)

The harness is smoke-tested on a stub under benchmarks/lab/grv_nu_derive_1/scratch/ that returns the registered nu
with nu_from_construction(y, n) = nu(y) (1 + 1/n), so that C-1 to C-4 pass and C-6 reports coincidence; and on a
second stub returning a constant 1, so that C-2 fails; both uncommitted. No run touches any data.

## 9. Budgets and disclosures

Theorist budget derive; the harness runs in seconds (cpu_hours 0.1; mem_gb 1; usd 0). Disclosed to the theorist in
the charter: GRV-031's retired candidates and their shapes; the asymptotics the registered nu obeys. Not disclosed
beyond the registry: nothing; the MOND literature's interpolation functions are forbidden as steps and the theorist
is not pointed at them.

```lab
commission: GRV-NU-DERIVE-1
kind: derivation
target: "Gravity row D1 (NORTH_STAR section 2): the shape nu(y) of the horizon coupling's response derived from GRV-005/029/028/XSEC-001 with the GRV-030/031 asymptotics as targets, as the limit of a computable construction, or stopped at a named obstruction; moves no number; the SPARC test is the successor GRV-NU-TEST-1"
premises: [GRV-005, GRV-029, GRV-028, XSEC-001, XSEC-002, GRV-030, GRV-031]
driver: benchmarks/lab/grv_nu_derive_1/driver.py
verdict_script: benchmarks/lab/grv_nu_derive_1/verdict.py
derivation_module: benchmarks/lab/grv_nu_derive_1/derivation.py
derivation_doc: analysis/lab/derivations/GRV-NU-DERIVE-1.md
instrument:
  - benchmarks/gravity/grv_blind_1.py
forms: [NOT-DERIVED, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/grv_nu_derive_1_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
