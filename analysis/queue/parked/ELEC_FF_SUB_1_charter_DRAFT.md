# COMMISSION ELEC-FF-SUB-1 -- DOES THE SUBSTRUCTURE GRANT SUPPLY THE COUPLING MECHANISM THE FORM-FACTOR TRILEMMA LACKED?
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-21; a DERIVATION commission; the derivation does not
# exist; no experimental bound is a step)

## 1. The target, and the North Star line
ELEC-036 quantified the electron sector's sharpest failure: the charge form factor computed from the model's
own Poisson source has rms radius 21.16 fm, against experiment seeing no electron structure below about 1e-3 fm,
a miss of 2.1e4 in size, and the two calibration anchors overdetermine that size so no optimization touches it.
It priced three branches and named branch C, "the medium-probe defense", as the only one that keeps both anchors:
the COUPLING density (what an external probe scatters from) would have to be pointlike at 1e-3 fm while the
FIELD-SOURCE density (what generates the binding Poisson field) has rms 21 fm; it was refused because "in
classical electrodynamics they are the same object tied by Gauss's law, so branch C requires a new coupling
mechanism the framework does not possess". That was 2026-08-01. On 2026-08-12 GRANT-SUBSTRUCTURE-TIGHT (FND-087)
made the vacuum strand a bundle of n_sub fine sub-strands, wound at two levels, and placed the carried photon on
the fine level (a_f <= lambda / 4 at the highest carried energy, FND-100's ceiling). A photon that rides the fine
strands scatters from whatever the terminus presents AT THE FINE LEVEL; the Poisson source of ELEC-036 is a
coarse-level object. Whether that difference is branch C's missing mechanism, or merely looks like it, is a
derivation question: does the registered substructure, with the registered dictionary, make the coupling
density and the field-source density different objects with different extents, and what is the coupling
extent in registered lengths? Nothing here is predicted; the North Star line is the electron row's gate.

## 2. Premises (the only things the derivation may rest on) and forbidden inputs
Premises, by claim id:
- ELEC-036: the trilemma, its branch C stated precisely, and the measured source rms 21.16 fm (model units
  calibrated by ELEC-034).
- FND-087, FND-088, FND-090, FND-100: the substructure grant, the derived winding, the Lorentz-invariant wave
  sector on wound carriers, the fine-level band ceiling (the photon is a fine-level wave).
- FND-110: single anchor; the fine level is suspended on n_sub and m; a_f and p carry only the lambda / 4
  ceiling.
- EM-023 (the orientation connection; B as strand-direction flux density), EM-008 / EM-014 (current as
  transported linking), GRV-020 corollary 1 (winding = charge): the dictionary by which a probe couples.
- ELEC-074, ELEC-090, ELEC-091: the terminus's hollow profile, its boundary as the locus where the strand
  tangent has turned through a right angle, and the azimuthal boundary tangent.
Forbidden: the experimental form-factor bound as a step (the document may compare after deriving); any new
coupling constant or length; any appeal to "the probe sees the fine level" without a registered dictionary step
that says what a fine-level transverse wave couples to at the terminus; branch A or B of ELEC-036 (out of scope).

## 3. The sealed input
None.

## 4. The interface the module must export (benchmarks/lab/elec_ff_sub_1/derivation.py)
- STATUS, ASSUMPTIONS, OBSTRUCTION as in the derivation kind.
- COUPLING_DENSITY: one sentence naming, by claim id, the registered object an incident fine-level transverse
  wave couples to at the terminus (the winding's phase, the boundary tangent, the strand-direction flux, or the
  Poisson source), and FIELD_SOURCE_DENSITY: the same for ELEC-036's Poisson source.
- SAME_OBJECT: bool, whether the two are the same registered object (branch C is then not supplied).
- coupling_extent_fm(a_f, p, R_star, r0): float, the rms extent of the coupling density in fm, as a function
  of the registered lengths only (the harness passes the registered values and also perturbed ones to check
  that nothing else enters), with the formula stated in the document.
- SOURCE_EXTENT_FM: float, ELEC-036's 21.16 reproduced from its registered inputs (the harness checks it).
- CHAIN: the ordered list of claim ids used, each with the one sentence it supplies.

## 5. The checks (locked here; numeric; nothing read from any run)
C-1 Every id in CHAIN is in the premises list; no other id appears in the module or the document's derivation
    section.
C-2 SOURCE_EXTENT_FM = 21.16 to 1 percent.
C-3 coupling_extent_fm depends on its arguments as the document states: the harness evaluates it at the
    registered values and at each argument doubled; the document's stated dependence (which arguments enter,
    and how) must match to 1e-6 relative.
C-4 If SAME_OBJECT is False, the document contains the dictionary step (by claim id) at which the coupling and
    the source separate, and that step is a premise, not an assumption in ASSUMPTIONS.
C-5 If STATUS is DERIVED, ASSUMPTIONS is empty; if DERIVED-CONDITIONAL, every assumption is one sentence naming
    a registered claim it would need and does not have.
C-6 Malformed metadata (non-list ASSUMPTIONS, non-string OBSTRUCTION, STATUS outside the three) renders
    NOT-DERIVED, never an exception (calibration cases in the harness).

## 6. The harness and the verdict
The driver runs C-1 to C-6 on the module and seals the result; the verdict script reads the sealed checkpoint
once and renders one form; the comparison of coupling_extent_fm against the experimental 1e-3 fm is the verdict's
last line, disclosed as the only place that number enters, and it does not change the form.

## 7. Verdict forms, and what follows
  DERIVED              STATUS DERIVED, C-1 to C-6 met: the registered substructure and dictionary make the coupling
                       density a different object from the source density, with a coupling extent in registered
                       lengths. Branch C is supplied (whether it passes experiment is the last line). The
                       successor is the form-factor computation on the fine level.
  DERIVED-CONDITIONAL  As above with named assumptions (each a registered claim the chain needs and lacks).
  NOT-DERIVED          STATUS NOT-DERIVED with the obstruction named (for instance: the dictionary gives the
                       probe's coupling at the coarse level only; or SAME_OBJECT is True and Gauss's law ties
                       them as ELEC-036 said), or any check failed. Branch C stays unsupplied; the trilemma
                       stands as priced.

## 8. Smoke discipline (binding on the drafting worker)
The harness's smoke run exercises C-1 to C-6 on a synthetic module fixture with each status and each malformed
case; the fixture is not committed; no derivation exists at lock.

## 9. Budgets and disclosures
The derivation is reading and one formula; the harness is checks. cpu_hours 0.1; usd: the theorist's attempt at
the derive budget. Disclosed: the executor's reading that "the photon rides the fine strands, so the probe sees
the fine level" is the reason the question is asked, and is exactly the step forbidden as an assumption; the
derivation must supply it from the dictionary or stop there and say so.

```lab
commission: ELEC-FF-SUB-1
kind: derivation
target: "Electron row gate (ELEC-036's priced trilemma): whether GRANT-SUBSTRUCTURE-TIGHT and the registered dictionary supply branch C's coupling mechanism, with the coupling extent in registered lengths, or stop at a named obstruction; moves no number"
premises: [ELEC-036, FND-087, FND-088, FND-090, FND-100, FND-110, EM-023, EM-008, EM-014, GRV-020, ELEC-074, ELEC-090, ELEC-091]
driver: benchmarks/lab/elec_ff_sub_1/driver.py
verdict_script: benchmarks/lab/elec_ff_sub_1/verdict.py
derivation_module: benchmarks/lab/elec_ff_sub_1/derivation.py
derivation_doc: analysis/lab/derivations/ELEC-FF-SUB-1.md
instrument:
  - benchmarks/foundations/electron_form_factor.py
forms: [NOT-DERIVED, DERIVED-CONDITIONAL, DERIVED]
state: [analysis/elec_ff_sub_1_ckpt.pkl]
budget: {cpu_hours: 0.1, usd: 0}
mem_gb: 1
```
