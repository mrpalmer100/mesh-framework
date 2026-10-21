# COMMISSION ELEC-FF-SUB-2 -- DOES THE SUBSTRUCTURE GRANT SUPPLY THE COUPLING MECHANISM THE FORM-FACTOR TRILEMMA LACKED?
# (CHARTER, the author's STAGED successor to ELEC-FF-SUB-1, 2026-10-21, rewritten against the external
# reviewer's round-2 objections; a DERIVATION commission; the derivation does not exist; no experimental bound is
# a step. Staged, not a DRAFT: it enters the queue only if ELEC-FF-SUB-1 parks, under this new name.)

## 0. What changed from ELEC-FF-SUB-1, and why
The round-2 external review found that the harness checked tokens, citations and the agreement of two formulas
the module itself supplied, and called that DERIVED; its own positive fixture was accepted on a fabricated
separating sentence and an extent sqrt(2 a_f p) with no provenance. That is self-certification. This charter
makes the harness evaluate the evidence: the module does not report an extent or a verdict about separation; it
CONSTRUCTS the coupling density as a function on a grid from field primitives the harness supplies, and the
harness computes the normalization, the rms extent, the separation from the registered Poisson source, and the
density's actual dependence on each primitive, with negative controls that must fail. The null form is an
unsuccessful attempt, never a no-go.

## 1. The target, and the North Star line
ELEC-036 quantified the electron sector's sharpest failure: the charge form factor computed from the model's own
Poisson source (Gaussian-smeared samples, width 0.24 model units, along the two curves of the registered clasp,
ELEC-020's state decoded by electron_calibration.curves16) has rms radius 0.9485 model units = 21.16 fm, against
experiment seeing no electron structure below about 1e-3 fm. It priced three branches and refused branch C ("the
coupling density pointlike while the field-source density is 21 fm") because in classical electrodynamics the
two are one object tied by Gauss's law and the framework had no mechanism to separate them. GRANT-SUBSTRUCTURE-
TIGHT (FND-087, 2026-08-12) then placed the carried photon on the fine level. Whether the registered dictionary,
applied to the registered clasp, makes the object a fine-level transverse wave couples to a DIFFERENT density
from the Poisson source, with a smaller extent, is a derivation question. The North Star line is the electron
row's gate; nothing is predicted.

## 2. Premises (the only things the derivation may rest on) and forbidden inputs
Premises, by claim id: ELEC-036 (the trilemma and the source density's construction); ELEC-020 (the registered
clasp state) and ELEC-021 (curves16 and the calibration lengths); FND-087, FND-088, FND-090, FND-100 (the
substructure, its winding, the fine-level wave sector and ceiling); FND-110 (single anchor; a_f and p carry only
the lambda / 4 ceiling); EM-023 (B is minus kappa_0 times the strand-direction flux density; the orientation
connection), EM-008 and EM-014 (current is transported linking), GRV-020 corollary 1 (winding = charge);
ELEC-074, ELEC-090, ELEC-091 (the hollow profile, the boundary, the azimuthal tangent) as the radial reading.
Forbidden: the experimental bound as a step; any new length or coupling constant; any density that is not a
function of the supplied primitives; any statement that the probe "sees the fine level" that is not a dictionary
step by claim id; branches A and B.

## 3. The sealed input
None. The primitives are computed by the harness from registered files at lock (their hashes in the manifest).

## 4. The interface
The HARNESS supplies, as arrays on one 3D grid (N^3 points, N = 96, box 6 model units, fixed at lock):
  P1 the two clasp curves (positions and unit tangents, M = 256 samples each, from ELEC-020's z_final through
     curves16); P2 the Poisson source rho_s on the grid (ELEC-036's Gaussian smearing, width 0.24, normalized
     to 1); P3 the strand-direction flux density of EM-023 built from the tangents (the harness's construction,
     documented in the driver); P4 the winding phase gradient along each curve (EM-008's transported linking);
     P5 the fine lengths a_f and p as numbers (the registered ceilings, FND-087, m = 1); P6 the radial reading
     (ELEC-074's profile and ELEC-091's tangent on the same grid, centred on the clasp's centroid).
The MODULE (benchmarks/lab/elec_ff_sub_2/derivation.py) exports:
  STATUS, ASSUMPTIONS, OBSTRUCTION as in the derivation kind;
  coupling_density(prims) -> array on the grid: the density an incident fine-level transverse wave couples to,
     built from the primitives and nothing else (no file access, no constants beyond pure numbers the document
     derives); the document states, per primitive, whether and how it enters and which premise makes it the
     coupling of a transverse wave;
  SEPARATION_STEP: the one claim id at which the coupling density and the Poisson source become different
     objects in the dictionary, with the sentence; or "none" (then STATUS cannot be DERIVED).

## 5. The checks (locked; the harness evaluates everything; nothing read from any run)
C-1 Normalization: Int rho_c = 1 to 1e-6 (charge is winding; q = 1); rho_c >= 0 or the document derives why
    it is signed, in which case |rho_c| is normalized and the sign structure reported.
C-2 Extent: rms_c = sqrt(Int rho_c r^2 / Int rho_c), computed by the harness; rms_s recomputed from P2 and
    required to reproduce 0.9485 to 1 percent (the instrument control).
C-3 Separation: the L2 distance between normalized rho_c and rho_s, D = ||rho_c - rho_s|| / ||rho_s||; DERIVED
    requires D >= 0.1 AND rms_c / rms_s <= 0.5. A relabelled Poisson source (D < 1e-6) is NOT-DERIVED.
C-4 Dependence: the harness perturbs each primitive in turn (curves displaced by 1e-3, tangents rotated by
    1e-3 rad, P3 scaled by 1 + 1e-3, P4 by 1 + 1e-3, a_f and p by 1 + 1e-3, P6 by 1 + 1e-3) and records the
    response of rms_c and of rho_c; the document's stated dependence must match the measured one (a primitive
    the document says enters must move rho_c by more than 1e-9 relative; one it says does not must not); a
    density that responds to no primitive (an arbitrary extent) is NOT-DERIVED.
C-5 Provenance: SEPARATION_STEP is a premise id; the document's chain cites only premises; ASSUMPTIONS empty
    for DERIVED, each a named registered claim for DERIVED-CONDITIONAL.
C-6 Negative controls, run by the harness before the module is evaluated and sealed first: (a) the Poisson
    source relabelled; (b) a delta at the clasp's outer radius depending on no primitive; (c) a Gaussian of
    width sqrt(2 a_f p) attached to the centroid with a one-sentence document (the ELEC-FF-SUB-1 fixture);
    (d) rho_s scaled by 0.5 in radius with no dictionary step. Each must render NOT-DERIVED; a positive control
    (e), rho_s itself with SEPARATION_STEP "none" and STATUS NOT-DERIVED, must render NOT-DERIVED cleanly.
    The controls credential the gate, not the physics; no positive fixture receives DERIVED.
C-7 Execution: the module is statically scanned (imports: numpy only; no open, os, sys, subprocess, pathlib,
    np.load/save/memmap/savetxt/fromfile); a module failing the scan is not imported and renders NOT-DERIVED-
    OPEN with the scan result; evaluation runs in a subprocess with a 300 s limit and the grid as its only
    input; malformed metadata renders NOT-DERIVED without exception (calibration cases).
C-8 Sealing: four units (controls; primitives and their hashes; module evaluation; verdict), each bound to the
    manifest's hashes of driver, verdict script, instrument files and the module and document as evaluated;
    the verdict refuses an incomplete or mixed-version checkpoint and is written once, exclusively.
C-9 Attempt budget: the theorist's attempt is bounded at the derive budget (cfg task_budget_usd['derive'], 80
    turns) and two attempts; an absent deliverable after that renders NOT-DERIVED-OPEN with the attempt record.

## 6. The harness and the verdict
The driver runs C-6 (controls), then builds and seals the primitives, then evaluates the module under C-7 and
seals C-1 to C-5; the verdict script reads the completed checkpoint once and renders one form; the comparison of
rms_c (in fm, through ELEC-021's L0 = 22.31 fm per model unit) against 1e-3 fm is its last line, disclosed as the
only place that number enters, and does not change the form.

## 7. Verdict forms, and what follows
  DERIVED              STATUS DERIVED and C-1 to C-9 met: the registered dictionary applied to the registered
                       clasp yields a coupling density distinct from the Poisson source (D >= 0.1, extent at most
                       half) by a named dictionary step. Branch C is supplied; the last line says whether the
                       extent passes experiment; the successor is the fine-level form factor proper.
  DERIVED-CONDITIONAL  As above with named registered assumptions.
  NOT-DERIVED          An unsuccessful attempt: STATUS NOT-DERIVED with the obstruction named, or a check failed.
                       Branch C stays unsupplied. This is NOT a no-go on branch C; a no-go is a theorem with its
                       own commission.
  NOT-DERIVED-OPEN     Infrastructure: the module failed the scan, the deliverable is absent after the attempt
                       budget, or a control or primitive unit failed; the derivation was not evaluated.

## 8. Smoke discipline (binding on the drafting worker)
The smoke run executes C-6's five controls and the primitive build on a coarse grid (N = 32) and prints the
control outcomes; no module exists at lock; the fixture modules live in the harness's test directory and are
never a deliverable.

## 9. Budgets and disclosures
Harness: cpu_hours 0.5 (the N = 96 grid, six perturbations), mem_gb 2, usd 0. The derivation attempt: the
derive budget, two attempts, included in the commission's dollar budget below. Disclosed: the executor's reading
"the photon rides the fine strands, so the probe sees the fine level" is the reason the question is asked and is
exactly the step that must arrive as a dictionary step or not at all; the harness's own construction of P3 and
P4 from the tangents is documented in the driver and is an instrument, not a result.

```lab
commission: ELEC-FF-SUB-2
kind: derivation
target: "Electron row gate (ELEC-036's priced trilemma): whether the substructure grant and the registered dictionary, applied to the registered clasp, yield a coupling density distinct from the Poisson source, with the harness computing the extent and the separation from a density the module constructs; or an unsuccessful attempt recorded; moves no number"
premises: [ELEC-036, ELEC-020, ELEC-021, FND-087, FND-088, FND-090, FND-100, FND-110, EM-023, EM-008, EM-014, GRV-020, ELEC-074, ELEC-090, ELEC-091]
driver: benchmarks/lab/elec_ff_sub_2/driver.py
verdict_script: benchmarks/lab/elec_ff_sub_2/verdict.py
derivation_module: benchmarks/lab/elec_ff_sub_2/derivation.py
derivation_doc: analysis/lab/derivations/ELEC-FF-SUB-2.md
instrument:
  - benchmarks/foundations/electron_form_factor.py
  - benchmarks/foundations/electron_calibration.py
  - rope_solver/topology/linking.py
forms: [NOT-DERIVED, NOT-DERIVED-OPEN, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/elec_ff_sub_2_ckpt.pkl]
budget: {cpu_hours: 0.5, usd: 30}
mem_gb: 2
```
