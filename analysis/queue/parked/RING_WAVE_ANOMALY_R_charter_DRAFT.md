# COMMISSION RING-WAVE-ANOMALY-R -- THE RING-WAVE'S SELF-FIELD ANOMALY, REPLICATED CODE-INDEPENDENTLY, AND THE DICTIONARY QUESTION THAT DECIDES ITS FORM
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-25; a REPLICATION with a sealed target plus one registry
# question; the Director's RING-WAVE-ANOMALY (advice memo 2026-10-25) executed by the executor as a reading first,
# because its answer is a single pure number that whoever computes it has seen; the lab's part is to reproduce it
# without the executor's code and to settle the one registry decision that selects between two forms; harness on
# benchmarks/lab/_kit/labkit.py)

## WHERE IT STANDS (the honest sentence, before the question)
The one registered mechanism class that reaches g = 2 by mechanics (the closed rope with its twist travelling at c,
analysis/ELEC_MECH_1_reading.md M7b) was asked, by the Director, whether its own self-field gives the measured
O(alpha) excess. The executor computed it (analysis/RING_WAVE_ANOMALY_reading.md, instrument benchmarks/foundations/
ring_selffield.py): with mu = q c R / 2, m c^2 = 2 (E_wave + U_E + U_M) by the scale virial, and
J = E_wave R / c + L_field, the logarithms ln(8R/b) in the electric and magnetic self-energies cancel against the
field angular momentum (c L_field / R = 2 U_M at beta = 1), the tube constants cancel, and the inductance's
curvature constant survives:
    g - 2 = (2 alpha / pi)(c_E - c_M) = (2 alpha / pi)(1/4 + 7/4) = 4 alpha / pi = 9.29e-3,
cutoff-free over three decades of b / R and discretization-free. The measured value is alpha / pi = 2.32e-3. Right
form, coefficient 4 against 1. THE NUMBER IS ON THE RECORD; this commission does not pretend otherwise. What is
open: (Q1) whether an implementation that shares no code and no method with the executor's reproduces 4.000, and
(Q2) whether the registered field-tensor dictionary (EM-017 to EM-022, the twist as the mechanical form of the
field) already counts the magnetic self-energy inside the twist energy, in which case U_M must not be added to m,
the bracket becomes U_E - 2 U_M + ..., the logarithm returns, and the class's anomaly is ln-enhanced rather than
4 alpha / pi. Q2 is a registry reading that nobody has made; it decides the class's form at O(alpha).

## THE QUESTION
  Q1  REPLICATION. The coefficient A in g - 2 = A alpha / pi for the uniform-tube ring at beta = 1, from an
      implementation that (i) does not import or read benchmarks/foundations/ring_selffield.py, (ii) uses a
      DIFFERENT method for at least the field energies (the executor's is pair sums with elliptic-integral
      potentials and mutual inductances; the replication may use direct field integration on a convergent grid
      with a smooth source, or the energy-per-length route with an explicit curvature expansion, or any method
      the worker states), (iii) demonstrates convergence in its own discretization and cutoff-independence over
      at least two decades of b / R, and (iv) computes L_field by its own route (the quasistatic theorem, or the
      E x B integral, each acceptable if stated) with the beta = 1 identity c L / R = 2 U_M checked as a bar.
  Q2  THE DICTIONARY. From EM-017 to EM-022 (and EM-RECON-012, GRV-020) by citation: is the magnetic self-energy of
      the circulating winding (i) ADDITIONAL to the Goldstone twist energy (kappa / 2) Phi'^2 (two accounts of
      energy, both in m), or (ii) INCLUDED in it (the twist energy IS the field energy's mechanical form; counting
      both double-counts), or (iii) not settled by the registry (SILENT). The theorist answers with the claim text
      quoted; no computation.
  Q3  THE FORM THAT FOLLOWS (a computation only if Q2 is (ii)): the bracket with U_M removed from m but L_field
      kept in J, A(b) over the registered core range (d_c = 1.87e-19 m to a = 6.0e-17 m at R = lambda-bar_C) and
      the statement whether it is ln-enhanced; reported, not formed, unless Q2 is (ii), in which case it is the
      class's anomaly of record.

## WHAT IS GIVEN
- The class and its energetics: analysis/ELEC_MECH_1_legC_instrument.md (the virial, J = E_wave R / c), the
  reading analysis/RING_WAVE_ANOMALY_reading.md (the SEALED TARGET A = 4.000 and its derivation, read by the verdict
  only); EM-008 (the moving winding is the current), EM-019 (momentum density = energy flux / c^2), EM-RECON-012.
- Classical electrodynamics of thin rings as the replication's own credential: thin-ring capacitance and
  inductance slopes in ln b (the worker derives or cites them; they are not the executor's).
- alpha enters only through the final conversion (g - 2 = 4 bracket-hat alpha); the measured g - 2 enters the
  verdict's last line only.

## DESIGN COMMITMENTS (locked at lock)
D1. The replication's deliverable is A with its band from its own convergence; the band must be at most 2 percent.
D2. Bars (halt-grade) on the replication's own path: d U_E / d ln b = -q^2 / 2 pi R and d U_M / d ln b =
    -beta^2 q^2 / 2 pi R to 1e-3; c L_field / R = 2 U_M at beta = 1 to 1e-3; cutoff-independence of A over two
    decades to 1e-2; the theorem Int E x B / 4 pi c = Int rho A / c reproduced on a charge-plus-solenoid fixture
    to 1e-2 if the E x B route is used.
D3. THRESHOLD: REPLICATES if |A - 4.000| <= 0.08 (2 percent); otherwise REPLICATION-FAILS with both numbers kept.
D4. Q2 is answered by quotation; a form fires only on quoted claim text; paraphrase is SILENT.

## HARNESS (binding)
Driver and verdict on labkit; units: credential (D2 bars on the worker's implementation, sealed), evidence (A at
three b / R values and two discretizations, sealed before any comparison), dictionary (Q2's quotations as data),
form_if_included (Q3, run only if Q2 (ii)), verdict (the sealed target loaded last; forms from the seals). The
driver MUST NOT import benchmarks/foundations/ring_selffield.py or elec_rope_wave.py; the manifest forbids them;
the verdict checks the import graph. LAB_SMOKE=1 runs the credential bars on a synthetic fixture (a different R,
beta = 0.3) and prints no A.

## FORMS (exhaustive; pre-registered)
  ANOMALY-4            REPLICATES and Q2 (i): the class's self-field anomaly is 4 alpha / pi, cutoff-free; the class
                       predicts the Schwinger form with coefficient 4 against the measured 1; registered as a precise
                       miss at O(alpha) (a kill of the class as the free electron unless a registered factor 4 is
                       later found; none is proposed here).
  ANOMALY-LOG          REPLICATES and Q2 (ii): U_M is not additional; the class's anomaly is Q3's ln-enhanced form,
                       reported with its number at the registered core range; the class fails at O(alpha) by a
                       cutoff-dependent amount.
  ANOMALY-UNDECIDED    REPLICATES and Q2 (iii): the number 4 alpha / pi stands as the additive reading and the
                       registry owes the field / twist split; the next commission is the dictionary's, not this
                       class's.
  REPLICATION-FAILS    |A - 4| > 0.08 with the replication's bars met: the executor's instrument or the worker's is
                       wrong; both numbers kept, the discrepancy is the result, and the executor's reading is
                       flagged until resolved.
  NO-CALL              D2 bars unmet on the replication, or the import ban violated.

## NO-RESCUE RULE
No change to the target, the threshold or the bars after the lock. The replication does not consult the
executor's code at any stage; if the worker reads it, the commission is NO-CALL and says so.

## DISCLOSURES
The executor computed and published A = 4.000 before this draft (analysis/RING_WAVE_ANOMALY_reading.md), by design:
a single pure number cannot be tested blind, and a replication is the honest test of it. The reading also
contains the executor's own list of possible reasons for the factor 4; the worker is not to use it. The
instrument's grid form failed its own credential on near-field resolution and was dropped; that failure is in
the record and is a warning to any replication that uses a grid.

## BUDGETS
Closed forms and small numerical integrals; cpu_hours 2; mem_gb 2; usd 0 beyond drafting, the theorist's Q2 and
review. Results to analysis/RING_WAVE_ANOMALY_R_results.md.

```lab
commission: RING-WAVE-ANOMALY-R
target: "Electron sector (blocks the strength-of-magnets row): code-independent replication of the travelling-twist ring's self-field anomaly g - 2 = 4 alpha / pi (the executor's reading), and the registry decision on whether the magnetic self-energy is additional to or included in the twist energy, which selects between a cutoff-free 4 alpha / pi and a ln-enhanced form; moves no number in section 2b; registers the class's O(alpha) prediction as a precise miss or a cutoff-dependent one"
driver: benchmarks/lab/ring_wave_anomaly_r/driver.py
verdict_script: benchmarks/lab/ring_wave_anomaly_r/verdict.py
instrument:
  - benchmarks/lab/_kit/labkit.py
forms: [ANOMALY-4, ANOMALY-LOG, ANOMALY-UNDECIDED, REPLICATION-FAILS, NO-CALL]
state: [analysis/ring_wave_anomaly_r_ckpt.pkl]
budget: {cpu_hours: 2, usd: 0}
mem_gb: 2
```
