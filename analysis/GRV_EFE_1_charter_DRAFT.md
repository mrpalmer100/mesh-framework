# COMMISSION GRV-EFE-1 -- DOES THE HORIZON COUPLING RESPOND TO A GALAXY'S OWN FIELD OR TO THE TOTAL FIELD AT ITS LOCATION?
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; nothing has run; the environmental-field table is not in the repository and no one in the programme has read it)

## 1. The question, and the North Star line

Question key: grv030-external-field-locality.

The registered gravity sector owns one galaxy-scale channel, the horizon coupling, which fixes the acceleration scale
g_dagger = c H0 / 2 pi (GRV-030; read as c^2 / 2 pi L_medium, XSEC-001/003) and nothing else: no shape (GRV-031) and
no scalar (GRV-028/029). The registry does not say what the coupling responds to. Two readings are live:

- H-LOCAL: the medium at a point responds to the total stress at that point, so the horizon coupling acts on the
  galaxy's internal Newtonian field PLUS the environmental field at the galaxy (the field of the surrounding
  large-scale structure). A local medium, which is what GRV-005 derived Newton from, has this reading as its natural
  one. It implies an external-field effect: a dwarf sitting in a strong environmental field is pushed toward the
  Newtonian regime and its observed acceleration falls BELOW the no-environment prediction at low internal g.
- H-SOURCE: the coupling references the source, the galaxy's own field alone (as the registered predictor, grv_blind_1.py,
  computes it). Then there is no external-field effect and the residuals at low acceleration do not depend on the
  environment.

Q1 (the effect). At low internal acceleration, do the residuals log10(g_obs) - log10(g_pred) of the registered
no-environment prediction decrease with the environmental Newtonian field e_N at the galaxy?
Q2 (the form). Does the zero-parameter local response, H-LOCAL's own algebraic form (section 6), with g_dagger =
c H0 / 2 pi and the registered nu, lower the residual rms at low acceleration against the no-environment prediction?

North Star line (section 5, rule (c)): a discriminator between two live readings of the one registered galaxy-scale
mechanism. Whichever reading survives, the gravity row's D1 content acquires a property it does not have today
(locality or source-reference of the horizon coupling), which any future derivation of the coupling must respect. It
moves no number in section 2b. Where the failures of GRV-BLIND-1/2 live: both carrying galaxies (PGC51017, UGC04305)
are low-acceleration dwarfs; their environmental field is recorded as a sub-reading, not read into any form.

What this commission does NOT do: it does not derive the coupling (section 6's form is the algebraic consequence of
H-LOCAL in one dimension, not a derivation of the mechanism); it does not re-read GRV-BLIND-1/2 or GRV-030 (kept);
it fits nothing (the form has no parameter; g_dagger and nu are the registered ones); it does not test MOND's
external field effect as such (the published detection is the prior, section 6, B-4, and is disclosed as known to
the author before this charter).

## 2. The parts list (every input cited; nothing is chosen in this commission)

| part | what | source |
|---|---|---|
| the internal prediction | g_pred = g_bar nu(g_bar / g_dagger), nu(y) = 1/(1 - exp(-sqrt y)), g_dagger = c H0 / 2 pi, H0 = 70; M/L gas, 0.5, 0.7 | GRV-030; benchmarks/gravity/grv_blind_1.py (unchanged) |
| the table | data/sparc_rotmod, 155 eligible galaxies (kept_mask as the registered confrontation) | tools/holdout_galaxies.py |
| the low-acceleration set | kept points with 0 < g_bar < 0.3 g_dagger; galaxies with at least three such points (136 galaxies, 1537 points on the shipped table; read as inputs only, no g_obs) | this charter, from the table's inputs |
| the environmental field | e_N per SPARC galaxy, the Newtonian acceleration from the surrounding large-scale structure, in units of the authors' a_0 = 1.2e-10 m/s^2, from Chae, Lelli, Desmond, McGaugh, Li and Schombert 2020, ApJ 904, 51, Table 1 (arXiv:2009.11525) | data/sparc_efe/chae2020_eN.csv, to be placed in the repository by the author AFTER the lock (section 3); not read by anyone in the programme before the verdict |
| the conversion | e_N [m/s^2] = (value) x 1.2e-10 (the authors' unit), then e = e_N / g_dagger with the registered g_dagger | this charter |
| the H-LOCAL form | section 6 | the algebra of a local algebraic response in one dimension |

## 3. The sealed input (the analogue of section W's draw; a precondition of the verdict, not of the lock)

After the lock the author downloads the authors' Table 1, writes data/sparc_efe/chae2020_eN.csv with the header
"galaxy,eN_a0" (one row per galaxy as the authors name them; SPARC names, e.g. NGC3198), and commits it with its
sha256 in the commit message, WITHOUT reading its values beyond what the download shows. The driver's units before
U3 read no file under data/sparc_efe/; U3 reads the file ONCE, records its sha256 and row count in the checkpoint,
and no unit after U3 reopens it. The author's own exposure is disclosed: he knows the paper reports a detection.
If the file has fewer than 100 galaxies matched to the 155, or fewer than 30 matched among the low-acceleration
set, the form is EFE-OPEN (section 7) and the commission ends without a Q2 reading.

## 4. Steps (one unit per invocation; checkpoint analysis/grv_efe_1_ckpt.pkl, atomic; resumable)

U1 calib (reads nothing under data/sparc_efe/): C-1 the predictor reproduces analysis/GRV_BLIND_1_pred.txt on
GRV_BLIND_1's inputs (same keys, relative 1e-5); C-2 the whole-table rms at the predicted g_dagger over all kept
points equals GRV-030's recorded 0.1423 within 5e-4 dex; C-3 the low-acceleration set is 136 galaxies and 1537 points
exactly (the counts of section 2).
U2 residuals: per galaxy in the low-acceleration set, the mean residual D_g = mean over its low-g points of
log10(g_obs) - log10(g_pred) (one number per galaxy, so galaxies are the units and points are not pseudo-replicated);
also the per-galaxy rms. Written to the checkpoint.
U3 the sealed read: data/sparc_efe/chae2020_eN.csv once; sha256 and row count; e per matched galaxy; refuses (exit 3,
waiting) while the file is absent.
U4 the statistics of section 6: S1, its permutation null (10,000 shuffles of e across the matched galaxies, seed
20261018), S2 and its control; the sub-readings of section 8. Terminal line "GRV-EFE-1 COMPLETE -- run the verdict".

## 5. The floor test (before any statistic that touches g_obs is read against e)

F-1 leverage: the matched low-acceleration galaxies' log10 e spans at least 0.7 dex between its 10th and 90th
percentiles (an external field that is the same for every galaxy cannot be tested); otherwise EFE-OPEN.
F-2 coverage: at least 30 matched low-acceleration galaxies; otherwise EFE-OPEN.
Both are read from e alone (U3) and the inputs; neither touches g_obs.

## 6. The bars (locked here; no pilot; nothing read from the sealed file)

S1 (Q1): Spearman rank correlation rho between D_g and log10 e over the matched low-acceleration galaxies, with the
permutation p-value (fraction of 10,000 shuffles with rho at least as negative). EFE-PRESENT if rho < 0 and p < 0.01;
EFE-ABSENT if p >= 0.05 or rho >= 0; EFE-OPEN if 0.01 <= p < 0.05 (the charter declines to read the gap).
S2 (Q2): the H-LOCAL form. In one dimension, with the internal Newtonian field g_N and an aligned environmental
field e_N, a local algebraic response gives a total observed field nu(z) (g_N + e_N) with z = (g_N + e_N)/g_dagger,
of which nu(e) e_N (e = e_N/g_dagger) is the environment's own; the galaxy's internal observed acceleration is the
difference,
    g_pred_local = g_N nu(z) + e_N [nu(z) - nu(e)],
which reduces to the registered prediction when e_N = 0 and has no parameter. The rms over the low-acceleration
points of log10(g_obs) - log10(g_pred_local) is compared with the same rms for the registered no-environment
prediction on the same points: EFE-LOCAL-FORM if the local form lowers the rms by at least 0.010 dex; otherwise
(a smaller improvement, no change, or a worsening) the form is not supported. 0.010 dex is set from the registry's
own entry threshold for shape candidates (0.003 dex, GRV-031's named residue) raised by a factor of three because
this form is a zero-parameter structural claim rather than a shape; it is not derived from any run.
Control for S2 (locked): the same comparison with e shuffled across galaxies (the median over the 10,000 shuffles);
the local form's real improvement must exceed the shuffled median by at least 0.005 dex, else the improvement is
attributed to the form's generic downward shift and S2 is not supported.
B-2 one prediction per form, nothing fitted, no exclusion after the file is read; a galaxy that misses is a miss.
B-3 the sub-readings of section 8 change nothing.
B-4 the prior, stated and disclosed, not leaned on: the source paper reports a detection of the external field effect
on SPARC (the authors' own analysis, with their MOND forms); so EFE-PRESENT is the expected Q1 and is a replication,
not a mesh prediction. The mesh content is Q2: whether the zero-parameter local form with the registered g_dagger and
nu carries the effect. The author's prior for Q2 is EFE-LOCAL-FORM, because a local medium has no other natural
reading; the charter is written so that the data can refuse it.

## 7. Verdict forms (exhaustive; reached in this order)

FORM (instrument): CALIB-FAIL (C-1 to C-3) / EFE-OPEN (section 3 coverage, F-1, F-2, or the S1 gap) / INCOMPLETE-OPEN.
FORM (Q1): EFE-PRESENT / EFE-ABSENT.
FORM (Q2, rendered only on EFE-PRESENT): EFE-LOCAL-FORM / EFE-PRESENT-WRONG-FORM.
On EFE-ABSENT the Q2 line prints "Q2 not read (no effect to carry)" and no token. Readings: EFE-PRESENT with
EFE-LOCAL-FORM supports H-LOCAL; EFE-PRESENT with WRONG-FORM says the environment matters but the one-dimensional
local algebra does not carry it (H-LOCAL survives as a reading, its form does not); EFE-ABSENT supports H-SOURCE and
makes the two carrying dwarfs' misses something other than environment. None of the three moves a number.

## 8. Sub-readings (recorded, not read; locked here; they change no form)

- e for PGC51017 and UGC04305 and their D_g, printed beside the matched sample's median e.
- The same S1 and S2 on the stricter set g_bar < 0.1 g_dagger (galaxies with at least three such points), printed.
- The per-galaxy rms under both predictions for the ten galaxies with the largest e.

## 8a. Development and smoke discipline (binding on the worker; a lock-review item)

Before the lock nothing may run against any file under data/sparc_efe/ (none exists). LAB_SMOKE=1 runs the pipeline
on a synthetic e table the driver generates (155 values, log-uniform over one decade, seeded 4242) under a scratch
name, writes analysis/grv_efe_1_smoke.pkl and no evidence checkpoint, and prints "smoke: forms withheld" and no FORM
token. U1 and U2 read the shipped table only (whole-table exposed since GRV-030; inputs and g_obs both public) and may
be exercised in smoke; the coupling of residuals to e, which is the question, is never computed on real e before the
verdict.

## 9. The verdict script (benchmarks/lab/grv_efe_1/verdict.py; frozen at lock)

Reads the checkpoint only. Order fixed: validate in full (status, the four units, the sealed file's sha256 and row
count, every numeric finite, the manifest of file hashes equal to the lock record); then create
analysis/GRV-EFE-1_verdict.log with O_EXCL; then the instrument forms, each returning at once; then Q1, then Q2.

## 10. Budgets and disclosures

Seconds of compute (10,000 shuffles over about 130 galaxies); cpu_hours 0.2; mem_gb 1; usd 0. Disclosed: the author
knows the source paper's headline (a detection) and has not seen its table; the drafter (the sandbox executor)
likewise; the SPARC table is whole-table exposed and GRV-130 named the two low-acceleration dwarfs; the H-LOCAL form
is the standard one-dimensional algebra of an external field in an algebraic MOND-like response and is used here
because it is what H-LOCAL implies, not because it is the mesh's derived law (the mesh has none yet). The author
wrote this charter without running anything against any environmental-field data.

```lab
commission: GRV-EFE-1
target: "Gravity row D1 (NORTH_STAR section 2): a discriminator (rule c) between two live readings of the registered horizon coupling, local (responds to the total field at the galaxy) or source-referenced (the galaxy's own field only), read on SPARC's low-acceleration galaxies against their environmental field; moves no number"
driver: benchmarks/lab/grv_efe_1/driver.py
verdict_script: benchmarks/lab/grv_efe_1/verdict.py
instrument:
  - benchmarks/gravity/grv_blind_1.py
  - tools/holdout_galaxies.py
forms: [CALIB-FAIL, EFE-OPEN, INCOMPLETE-OPEN, EFE-PRESENT, EFE-ABSENT, EFE-LOCAL-FORM, EFE-PRESENT-WRONG-FORM]
state: [analysis/grv_efe_1_ckpt.pkl]
budget: {cpu_hours: 0.2, usd: 0}
mem_gb: 1
```
