# COMMISSION GRV-EFE-DERIVE-1 -- THE EXTERNAL-FIELD RESPONSE OF A LOCAL MEDIUM, DERIVED FROM THE REGISTERED PREMISES
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; a DERIVATION commission; the derivation does not exist;
# nothing here was read from any environmental-field data)

## 1. The target, and the North Star line

Question key: grv-horizon-coupling-locality-derivation.

GRV-EFE-1 (drafted the same day) asks the data whether the horizon coupling responds to a galaxy's own field or to
the total field at the galaxy, and tests the one-dimensional algebraic form that a local response implies. This
commission asks the theorist for the mechanism's own answer: given that the medium is local (GRV-005 derived Newton
from the static force balance of a local elastic medium) and that its registered galaxy-scale response is the
algebraic law g_obs = g_bar nu(g_bar / g_dagger) for an isolated source (GRV-030, nu registered as empirical), what
is the observed internal acceleration of a source embedded in a uniform external Newtonian field e, in three
dimensions, at any angle between the internal field and e?

TARGET. A function g_int(g_N, e; g_dagger), vector in, vector out, such that: it is what a LOCAL medium with the
registered response produces (local means the response at a point depends only on the total field at that point);
it reduces to the registered law when e = 0; it is Newtonian when |g_N + e| >> g_dagger; the field it describes is
consistent as a field of the medium (if the registered algebraic response is not curl-free in an external field,
which is a known property of algebraic responses, the theorist must say so and derive the consistent local form
from the medium's variational statics, GRV-005, or stop with that as the obstruction); and its aligned
one-dimensional limit is stated in closed form, so that GRV-EFE-1's locked form can be read as the same function,
a limit of it, or a different one.

North Star line (section 5, rule (c)): a discriminator's mechanism. The gravity row carries one D1 observable and
one channel; whether that channel is local is a property the row does not have, and GRV-EFE-1 will read it from
data. This commission supplies the thing a data reading alone cannot: the form a local medium predicts, so that
EFE-PRESENT-WRONG-FORM in GRV-EFE-1 has a derived candidate behind it rather than an algebraic guess. Moves no
number in section 2b. A NOT-DERIVED with the obstruction named is a result: it tells the gravity row what the
horizon coupling would have to be to have an external-field response at all.

What this commission does NOT do: it does not derive nu (the registered empirical nu is a premise, used only
through its values; deriving nu is a separate derivation charter); it does not derive g_dagger or its 2 pi; it reads
no data (section 3); it does not decide H-LOCAL against H-SOURCE (GRV-EFE-1 does, with data).

## 2. Premises (the only things the derivation may rest on) and forbidden inputs

Premises, by claim id:
- GRV-005: a mass-knot is a stressed defect; static force balance div(stress) = -f of a LOCAL elastic medium is the
  conservation law; the conditioning field is a static strain field and its scalar sector obeys the forced Poisson
  equation. (The locality and the variational character of the statics.)
- GRV-030: for an isolated source, g_obs = g_bar nu(g_bar / g_dagger), nu(y) = 1/(1 - exp(-sqrt y)), at zero
  parameters, g_dagger = c H0 / 2 pi. (The registered response; nu is empirical and enters as a given function.)
- GRV-028, GRV-029: no galaxy-scale scalar; the horizon coupling is the only galaxy-scale channel. (The derivation
  may not introduce a new field to carry the external-field dependence.)
- XSEC-001: g_dagger read as c^2 / 2 pi L_medium, a property of the medium, not of the source. (Locality of the
  scale itself.)
Forbidden: SPARC or any rotation-curve data; the environmental-field table of Chae et al. 2020 or any value from it;
any external-field formula from the MOND literature used as a premise (the theorist may cite one in the document
for COMPARISON after deriving, never as a step); any constant chosen to make a check pass.

## 3. The sealed input

None. This commission reads no data. Its later test is GRV-EFE-1 (locked separately), whose sealed input the
theorist never sees.

## 4. The interface the module must export (benchmarks/lab/grv_efe_derive_1/derivation.py)

- STATUS: "DERIVED" | "DERIVED-CONDITIONAL" | "NOT-DERIVED"; ASSUMPTIONS: list of sentences (empty if none);
  OBSTRUCTION: None or one sentence.
- FORMULATION: "algebraic" | "potential" | "none" (how the consistent local response is expressed).
- g_int(gN, e, gdag): gN and e numpy arrays of shape (..., 3) in m/s^2, gdag a float; returns the observed internal
  acceleration, shape (..., 3). For FORMULATION "potential" the module may solve its field equation numerically for
  a point source in a uniform field; the harness calls it on a grid of no more than 2000 points and allows 60 s.
- aligned_1d(gN, e, gdag): scalars (gN >= 0, e >= 0 along the same axis); returns the scalar internal acceleration
  in the aligned one-dimensional limit, in closed form.
- potential(x, M, e, gdag) when FORMULATION is "potential": the total potential at points x (shape (..., 3)) for a
  point mass M at the origin in uniform external Newtonian field e; the harness differentiates it numerically.

## 5. The checks (locked here; numeric; nothing read from any run)

C-1 reduction: with e = 0, g_int(gN, 0, gdag) equals gN nu(|gN|/gdag) with the registered nu, to relative 1e-9, on a
log grid of |gN| from 1e-3 gdag to 1e3 gdag (60 points, random directions, seed 7).
C-2 Newtonian limit: with |gN + e| >= 1e3 gdag, |g_int - gN| / |gN| <= 1e-3 on 60 points (seed 7), at angles 0, 90
and 180 degrees between gN and e.
C-3 strong-external-field limit (the defining property of an external-field response): with |e| >= 1e3 gdag and
|gN| <= 1e-2 gdag, |g_int - gN| / |gN| <= 2e-3 (the internal field becomes Newtonian when the environment is
strong), at the three angles, 60 points.
C-4 monotonicity: at fixed e (|e| = 0.1 gdag, 1 gdag, 10 gdag) and fixed angle, |g_int| is non-decreasing in |gN|
over the log grid (no decrease larger than 1e-9 relative).
C-5 homogeneity: g_int(k gN, k e, k gdag) = k g_int(gN, e, gdag) to relative 1e-9 for k in {0.5, 2, 10}.
C-6 consistency of the field: for a point source (M chosen so that |gN| = gdag at r = 1 unit) in a uniform external
field |e| = gdag at 45 degrees, the circulation of g_int (or of the gradient of the module's potential) around 20
closed square loops of side 0.5 unit placed at radii 0.5 to 5 units is at most 1e-6 times the mean |g_int| on the
loop times the loop's perimeter. (The registered algebraic response, applied to a non-uniform total field, generally
fails this; a module with FORMULATION "algebraic" that fails C-6 renders NOT-DERIVED with C-6 named, which is the
expected obstruction if the theorist stops at the algebra.)
C-7 the aligned limit: aligned_1d(gN, e, gdag) equals the magnitude of g_int(gN e_hat, e e_hat, gdag) to relative
1e-6 on a 30 x 30 grid of (gN, e) in [1e-2, 1e2] gdag.
C-8 import: the module imports in the sandbox with numpy only, in under 5 s, reading no file.

## 6. The harness and the verdict (locked; the driver and the verdict script)

The driver (benchmarks/lab/grv_efe_derive_1/driver.py) imports the module, runs C-8 then C-1 to C-7, records each
check's pass or fail with its worst-case number, the module's STATUS, ASSUMPTIONS, OBSTRUCTION and FORMULATION, and
the module's sha256, in analysis/grv_efe_derive_1_ckpt.pkl (atomic), and prints "GRV-EFE-DERIVE-1 COMPLETE -- run
the verdict". It never prints FORM lines. An import failure is recorded as C-8 failed with the traceback's last
line. The verdict script reads the checkpoint only and renders, in this order: NOT-DERIVED if STATUS is NOT-DERIVED
(printing OBSTRUCTION) or any check failed (printing the failed checks); DERIVED-CONDITIONAL if every check passed
and ASSUMPTIONS is non-empty (printing them); DERIVED if every check passed and ASSUMPTIONS is empty. Recorded, not
formed: FORMULATION; the closed form of aligned_1d as the document states it; whether it coincides with GRV-EFE-1's
section-6 form (the harness evaluates both on the C-7 grid and prints the maximum relative difference).

## 7. Verdict forms (exhaustive)

FORM (Q1): NOT-DERIVED / DERIVED-CONDITIONAL / DERIVED.
Readings: DERIVED with FORMULATION "potential" and C-6 passing is the local medium's own external-field law, ready
for GRV-EFE-2 as a locked form; DERIVED-CONDITIONAL names the assumption that bought it (a reader can then ask
whether the registry supplies it); NOT-DERIVED at C-6 says the registered algebraic response has no consistent
local extension to an external field without a potential formulation the registry does not yet have, which is a
precise statement about what the horizon coupling must be.

## 8. Smoke discipline (binding on the drafting worker)

The harness is smoke-tested on a stub module under benchmarks/lab/grv_efe_derive_1/scratch/ (never at the module's
path) that implements the registered law with e ignored, so that C-1 passes and C-3 fails by construction, proving
the checks discriminate; the stub is not committed. No run touches any data.

## 9. Budgets and disclosures

The derivation costs the theorist's turns (budget derive, section config); the harness runs in seconds (cpu_hours
0.1; mem_gb 1; usd 0). Disclosed: the author and the drafter know that algebraic MOND-like responses are not curl-free
in external fields and that potential formulations exist in the literature; the theorist is not told which, and
the charter forbids using them as premises. The checks test properties the target must have, not a known answer.

```lab
commission: GRV-EFE-DERIVE-1
kind: derivation
target: "Gravity row D1 (NORTH_STAR section 2): the mechanism behind GRV-EFE-1's discriminator, the external-field response a local medium with the registered horizon coupling predicts, derived from GRV-005/030/028/029/XSEC-001 or stopped at a named obstruction; moves no number"
premises: [GRV-005, GRV-030, GRV-028, GRV-029, XSEC-001]
driver: benchmarks/lab/grv_efe_derive_1/driver.py
verdict_script: benchmarks/lab/grv_efe_derive_1/verdict.py
derivation_module: benchmarks/lab/grv_efe_derive_1/derivation.py
derivation_doc: analysis/lab/derivations/GRV-EFE-DERIVE-1.md
instrument:
  - benchmarks/gravity/grv_blind_1.py
forms: [NOT-DERIVED, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/grv_efe_derive_1_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
