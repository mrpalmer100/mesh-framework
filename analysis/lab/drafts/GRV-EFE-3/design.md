# GRV-EFE-3: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission GRV-EFE-3, kind discriminator, question key grv030-external-field-locality. Theorist's design, 2026-11-06.
The third attempt at this question and the first written as a sealed design. GRV-EFE-1 (author's draft of 2026-10-18,
analysis/queue/parked/GRV_EFE_1_charter_DRAFT.md) was abandoned by its worker ("I cannot make the sealed
environmental-field input credentialed from inside this sandbox"); GRV-EFE-2 was withdrawn before lock. Neither was a
try; no statistic pairing the environmental field with any residual has ever been computed by anyone in the programme.
This file is committed before the kit exists; nothing below changes afterwards; a change is a new name. Every number
here is a registered number, a value returned by the sealed code (quoted from the scratch runs
analysis/lab/drafts/GRV-EFE-3/scratch_constants.py and scratch_fixtures.py, which import benchmarks/gravity/grv_blind_1.py,
read the public SPARC table and never open data/sparc_efe/), stated arithmetic, a value fixed in the author's 2026-10-18
draft before the evidence file existed, or a synthetic fixture. The cures are in DISCLOSURES at the end.

## 0. WHY

The Director's proposal: the registered gravity sector owns exactly one galaxy-scale channel, the horizon coupling that
fixes g_dagger = c H0 / 2 pi (GRV-030, Modeled, D1 on the scorecard; no shape, GRV-031; no scalar, GRV-028/029). The
registry does not say what that coupling responds to. Two readings are live and untested:

- H-LOCAL: the medium at a point responds to the total field there, so the coupling acts on the galaxy's internal
  Newtonian field plus the environmental field of the surrounding structure. Prediction: at low internal
  acceleration the observed acceleration falls below the registered no-environment prediction, more so the stronger
  the environment.
- H-SOURCE: the coupling references the galaxy's own field (as the registered predictor grv_blind_1.py computes it).
  Prediction: low-acceleration residuals do not depend on the environment.

The commission decides between them on the SPARC galaxies with the environmental field e_env of Chae et al. 2020,
already in the repository under a hash written before anyone opened it. Row served: Gravitational force, the D1 cell
(g_dagger = c H0 / 2 pi). Gear: breadth (the last locked session, NUC-MIRROR-LEAN-3, was interior under the author's
named exception; the gravity row has gone longest without a lock). No lead is followed; the question is the author's
own (GRV-EFE-1 draft, section 1). It may also bear on why the two GRV-BLIND-2 misses (PGC51017, UGC04305, GRV-129) are
low-acceleration dwarfs; that is a sub-reading only.

## 1. THE QUESTION

Q1 (the effect, the discriminator). Over the matched low-acceleration SPARC galaxies of the beacon hold-out, do the per-galaxy mean residuals of
the registered no-environment prediction fall with the environmental field e_env (one-sided rank test at the locked
significance), with the effect absent where H-LOCAL itself says it must be absent (the high-acceleration placebo)?
- Would change: a rider on GRV-030 recording which reading of the coupling the data favour, a constraint any future
  derivation of the coupling (or of nu) must respect.
- Would not change: g_dagger, the grade D1, any number in NORTH_STAR section 2b; GRV-030, GRV-BLIND-1/2 and GRV-031
  stand as recorded.

Q2 (the form, read only when Q1 favours H-LOCAL). Does the zero-parameter one-dimensional local response (section 3),
with the registered g_dagger and nu, carry the effect at its own amplitude (regression slope of residual on predicted
shift consistent with 1 and excluding 0)?
- Would change: whether H-LOCAL's simplest algebraic form survives as the working form, or only its sign.
- Would not change: anything derived; the form is the algebra of H-LOCAL, not a mesh derivation (the author declined
  derivation commissions on this ground, GRV-EFE-DERIVE-2).

## 2. THE EVIDENCE SET

What is scored. The pairing of two things: (i) per-galaxy residuals from the public SPARC table data/sparc_rotmod
(175 Rotmod_LTG files, shipped since GRV-030, whole-table exposed: inputs and observed velocities have been read by
the programme many times); (ii) the column e_env of Chae, Lelli, Desmond, McGaugh, Li and Schombert 2020 (ApJ 904, 51;
arXiv:2009.11525v2, erratum-corrected Table 2), the Newtonian environmental field from large-scale structure in units of
the authors' a0 = 1.2e-10 m/s^2, NOT the column e fitted to each rotation curve (which would be circular).

How it is obtained with no person acting. The file data/sparc_efe/chae2020_eN.csv is already in the repository. It must
have sha256 f18ee3c7eac92b248a1e7eea0f62e4e706bb749c648ecdb9b8947570c54248e7, the value the author's 2026-10-18 draft
wrote (section 3 of that draft) when the file was produced by tools/extract_chae2020_eenv.py, whose current sha256 is
6623da6f494bccbc81d5eeef21f99781b9f3e15e6ca5ffb60a395a683558f288 (scratch_constants.py). The scored set is chosen by
the lab's public randomness beacon, not by the commission (bar W, below): a hold-out of 78 of the 155 eligible SPARC
galaxies, drawn after lock by the unchanged tools/holdout_galaxies.py from a drand round committed to the lab branch
before it exists. Within the hold-out, the cells are defined by rules taken from pre-evidence sources:
- eligible: at least three kept points (Vobs > 0, errV/Vobs < 0.1, r > 0). Provenance: the registered table rule of
  GRV-030 as coded in tools/holdout_galaxies.py and grv_blind_1.py, used by GRV-BLIND-1/2.
- low-acceleration galaxy: at least three kept points with 0 < g_bar < 0.3 g_dagger. Provenance: the author's
  2026-10-18 GRV-EFE-1 draft, section 2 ("kept points with 0 < g_bar < 0.3 g_dagger; galaxies with at least three such
  points"), written before the evidence file existed, adopted verbatim. Not changed here (see DISCLOSURES for the
  1537 versus 1524 count, which is two tallies of one rule, not two rules).
- high-acceleration placebo galaxy: at least three kept points with g_bar > g_dagger. Provenance: g_dagger is the
  model's only acceleration scale, and the placebo is the regime the section 3 form itself places furthest from the
  coupling's effect: computed on synthetic e (section 4, P1), H-LOCAL's mean predicted shift there is 0.130 of its
  low-acceleration shift. The three-point minimum is the same registered minimum as eligibility and the author's
  low-acceleration rule; it is used for symmetry, not tuned.
- matched: the galaxy's name appears in the file by exact string equality with the Rotmod file stem (the name with
  "_rotmod.dat" removed).
No exclusion after the file is read; a galaxy that misses is a miss. Galaxies outside the hold-out are not paired with
e at all.

What is pinned (from the public table and the code, not the evidence; whole-table values, before any draw): 155
eligible galaxies with 2788 kept points with g_bar > 0; the low-acceleration rule gives 136 galaxies, holding 1524
points, while 1537 kept points over all 155 galaxies satisfy 0 < g_bar < 0.3 g_dagger (the author's draft's tally); the
high-acceleration placebo set 39 galaxies, 652 points; the strict set (at least three points with
0 < g_bar < 0.1 g_dagger) 104 galaxies. All are code values (scratch_constants.py, scratch_rev1.py). The hold-out's own
counts are recorded at run time.

What is read once. The evidence file, by the driver's sealed-read unit, once; its values go to the checkpoint and to no
screen. The run records at run time the row count, the matched counts and the unmatched names; none of those is in this
design, and the halts of section 4 are rules the run applies to them.

What the programme has and has not inspected. Told exactly: on 2026-10-18 the executor ran the extractor on the authors'
LaTeX source; the extractor prints a row count, "names unique", "e_env in [0,1]", an erratum flag for NGC5033/NGC5055
and the sha256, and never a value. The parked GRV-EFE-1 draft records that row count and a statement that every row
matched a SPARC name. This design does not repeat that count, and no bar, halt or fixture uses it. No per-galaxy value
of e_env has been printed, read or computed on by anyone in the programme; nothing pairing e_env with a residual has run.
The author and the executor know the paper's headline (a detection of an external-field effect under the authors' MOND
fits); the theorist writing this knows the same and has not seen the table. The SPARC residuals are exposed, and
GRV-130 named the two low-acceleration dwarfs carrying GRV-BLIND-2's miss.

Bar W, met by a beacon hold-out (committed; no conditional). The design does not argue W away. GRV-030's model was
confronted with this table and its interpolation nu was selected on it (the simple form preferred over the tanh family
by 0.0086 dex on the 2788 points, GRV-030), and the gravity sector has been scored under W before (GRV-BLIND-1,
GRV-BLIND-2). So W is applied as written: the scored set is a pre-registered hold-out selected by a process other than
the commission, and every prediction is frozen before the held-out pairing is read.
- The draw. At lock the lab commits a future drand round to the lab branch (a beacon_draw entry, as GRV-BLIND-2 section
  11). When the round is published, the lab runs, with the unchanged tool,
      python tools/holdout_galaxies.py draw --name GRV_EFE_3 --seed {seed} --n 78 --drawn-by "drand beacon round {round}"
  where {seed} is derived from the round's published randomness by the lab's beacon tool exactly as for GRV-BLIND-2 and
  recorded verbatim in the tool's analysis/holdout/GRV_EFE_3/MANIFEST.json. The kit reads only the held-out name list
  from that manifest and records the manifest's sha256; the tool's split files are not used (the residuals come from
  data/sparc_rotmod, which is whole-table exposed and says so). No redraw for any reason.
- Size. 78 = ceil(155/2), half the eligible table rounded up: the stated arithmetic is that half is held out and the
  power cost is accepted and measured (F-3 re-sized on the hold-out, section 4; synthetic power at this size in X-1).
- BLOCKED. If the manifest is absent (the round not yet published or the draw not yet run), the driver prints BLOCKED
  with the exact command and exits 2; this is not a form, it is the wait the lab's beacon resolves with no person
  acting. No unit that pairs e with a residual runs before the manifest exists and passes C-6.
- What the hold-out protects. The residuals are exposed and the cell rules were written by people who know the source
  paper's headline; the hold-out removes the commission's hand from which galaxies are scored. It does not make the
  residuals unseen, and the rider says so.

## 3. THE MODELS OR PREMISES

- The registered no-environment prediction (H-SOURCE's predictor), GRV-030 as implemented in
  benchmarks/gravity/grv_blind_1.py (sha256 4c407e9e732c431909b3bf8bc0e6abcf214083f8fe2c480c526ae921503aa634),
  imported unchanged: g_bar = (sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2)/r; g_pred = g_bar nu(g_bar/g_dagger),
  nu(y) = 1/(1 - exp(-sqrt y)); G_DAGGER = 1.0830375259007784e-10 m/s^2 (code value; registry 1.083e-10).
- The residual: r_i = log10(g_obs,i) - log10(g_pred,i), g_obs = Vobs^2/r, on kept points.
- The conversion: e_N = eN_a0 x 1.2e-10 m/s^2 (the authors' unit); e = e_N/g_dagger, so e = 1.1079948 x eN_a0
  (code: 1.2e-10/G_DAGGER = 1.1079948490260687).
- H-LOCAL's form, frozen here (the author's draft section 6): with internal Newtonian field g_N and an aligned
  environmental field e_N, a local algebraic response gives total observed field nu(z)(g_N + e_N), z = (g_N + e_N)/g_dagger,
  of which nu(e) e_N is the environment's own; the galaxy's internal observed field is
      g_local = g_N nu(z) + e_N [nu(z) - nu(e)],
  which equals the registered prediction at e_N = 0 and is positive for e_N > 0 (x nu(x) is increasing). For e_N = 0 the
  kit uses the registered prediction directly. Per galaxy, the predicted shift is
      Delta_g = mean over its low-acceleration points of [log10(g_local) - log10(g_pred)]  (negative for e_N > 0).
- Premise carried by provenance, not checked in the sandbox: the extractor's cell index 3 of the authors' nine-column
  table is e_env and not the fitted e. The authors' TeX source is not in the repository; this premise is stated in
  every form's wording (section 7).
- Disclosed nature of e_env: the authors build it from 2M++ dynamical masses with LCDM infill of unrecorded halos, so it
  estimates the total external field under LCDM, not a baryonic Newtonian field. Q1 (a rank statistic) does not depend
  on that reading; Q2 uses e_env as e_N, which overstates the baryonic field if the medium's response or dark halos are
  in it; a Q2 slope below 1 is read with that caveat.

Nothing is calibrated, fitted or re-fit.

## 4. THE STATISTICS AND BARS

Seeds: s(label) = int(sha256(label)[:8], 16) & 0x7fffffff, labels "GRV-EFE-3 S1", "GRV-EFE-3 F3", "GRV-EFE-3 P1",
"GRV-EFE-3 Q2", "GRV-EFE-3 FIX" (rule written here; the strings are the seeds' only source). Ranks: average ranks for
ties (scipy.stats.rankdata, method "average"); rho = Pearson correlation of the ranks.

Per-galaxy quantities, over the beacon hold-out only. For each matched held-out low-acceleration galaxy g:
D_g = mean of r_i over its points with 0 < g_bar < 0.3 g_dagger; Delta_g as in section 3; e_g from the file. For each
matched held-out placebo galaxy h: H_h = mean of r_i over its points with g_bar > g_dagger. Galaxies are the units;
points are not pseudo-replicated.

Halts (rules the run applies; values recorded at run time, not here). Disclosed first: the parked GRV-EFE-1 draft
records the extractor's row count and that every row matched a SPARC name. That record makes these halts foregone in
practice: with full matching, the hypergeometric probability that a 78-galaxy draw holds fewer than 30 of the 136
low-acceleration galaxies is below 1e-15, and fewer than 10 of the 39 placebo galaxies 6.9e-5 (scipy.stats.hypergeom,
scratch_rev1.py). H-1 and H-2 are therefore retained only as fail-closed guards against a broken join or a corrupted
file; they carry no evidential weight and are not cited as checks. Their thresholds were fixed by a writer aware of that
record.
- H-1 coverage: matched held-out galaxies >= 50 and matched held-out low-acceleration galaxies >= 30, else
  EFE-OPEN-COVERAGE. Provenance: the author's 2026-10-18 draft (matched eligible >= 100, low-acceleration >= 30); the
  first scaled to the hold-out, 100 x 78/155 = 50.3, floored to 50; the second kept as the author wrote it.
- H-2 placebo coverage: matched held-out placebo galaxies >= 10, else EFE-OPEN-COVERAGE. Provenance: stated
  arithmetic; the veto at p < 0.01 is attainable only from n = 5 (5! = 120 > 100), and 10 is twice that minimum. (The
  earlier 15 is replaced because a half-table draw falls below 15 placebo galaxies with probability 0.029 even under
  full matching, which would close the question by the draw alone.)

Floor (principle 5), read before any statistic pairs e with residuals:
- F-3 power of H-LOCAL's own predicted effect above the noise floor, re-sized on the hold-out (computed only over the
  matched held-out low-acceleration galaxies). The S1 null: 10,000 permutations of e across those galaxies, seed s("GRV-EFE-3 S1"), giving rho_perm; rho_crit = its 1st percentile. Then 2,000
  replicates, seed s("GRV-EFE-3 F3"): D_syn = Delta + (D permuted across galaxies, which destroys any pairing with e);
  power = fraction of replicates with rho(D_syn, e) <= rho_crit. Bar: power >= 0.80, else EFE-OPEN-UNDERPOWERED.
  Provenance: the conventional design power 0.80 at the test's own alpha 0.01; not from data. F-3 reads e, Delta and the
  multiset of D (exposed), never the pairing of D with e, and is computed before rho_obs.

S1 (Q1): rho_obs = rank correlation of D_g with e_g. p_minus = (1 + #{rho_perm <= rho_obs})/10,001;
p_plus = (1 + #{rho_perm >= rho_obs})/10,001, on the same 10,000 permutations. Bars: effect present if p_minus < 0.01;
reversed if p_plus < 0.01; absent if p_minus >= 0.05 and p_plus >= 0.01; the gap 0.01 <= p_minus < 0.05 is not read.
Provenance: the author's 2026-10-18 draft, section 6 (0.01 and 0.05), adopted unchanged; the reversed branch is new
here and uses the same 0.01.

P1 (placebo, a veto on Q1's present branch): rho_hi = rank correlation of H_h with e_h over matched placebo galaxies;
10,000 permutations, seed s("GRV-EFE-3 P1"); p_hi = (1 + #{perm <= rho_hi})/10,001. Fires if p_hi < 0.01. Reason,
computed rather than asserted: H-LOCAL's own form predicts a shift at g_bar > g_dagger too, Delta_hi_h = mean over the
placebo galaxy's high points of [log10(g_local) - log10(g_pred)]. On synthetic e (log10 e_N/a0 uniform on [-2, -0.5],
200 draws, seed s("GRV-EFE-3 FIX"), scratch_rev1.py) the ratio of the mean |Delta_hi| over the 39 placebo galaxies to
the mean |Delta| over the 136 low-acceleration galaxies is 0.130 on average (largest 0.152). So a true H-LOCAL world
does trip the veto at a small rate, which X-1 measures and bounds (section 5): with both shifts planted at hold-out size
78, 0.044 of 2,000 synthetic replicates render EFE-CONFOUNDED (scratch_rev1.py). That is the price of the veto, stated:
about one true effect in twenty-three is converted to CONFOUNDED. A significant decline at high acceleration at the same
alpha is read as a systematic (distance, inclination, sample selection) correlated with e. A non-firing placebo does not
exclude every confound; it is underpowered by design and said so.

Q2 slope: OLS of D_g on Delta_g with intercept over the matched held-out low-acceleration galaxies; 10,000 bootstrap resamples of
galaxies with replacement, seed s("GRV-EFE-3 Q2"); interval [L, U] = the 0.5th and 99.5th percentiles of the slope.
Bars: CARRIES if L > 0 and L <= 1 <= U; UNDER if L > 0 and U < 1; OVER if L > 1; FORM-OPEN if L <= 0. Provenance: 1 is
H-LOCAL's own amplitude and 0 is no response; the 99 percent level matches S1's alpha. Nothing from any run.

## 5. THE CREDENTIALS

All halt-grade unless marked diagnostic. A halt renders EFE-INSTRUMENT-OPEN and stops. Units C and X read nothing under
data/sparc_efe/.

- C-0 hashes: grv_blind_1.py and tools/extract_chae2020_eenv.py equal the sha256 values in sections 2 and 3.
- C-1 G_DAGGER from the imported module: |G - 1.083e-10| <= 5e-14 (the registry's four digits).
- C-2 the whole-table rms at the predicted g_dagger over all kept points with g_bar > 0 of the 155 eligible galaxies
  equals GRV-030's 0.1423 within 1e-4 (code value 0.14225775).
- C-3 counts, exact integers (code values, whole table): 155 eligible; 2788 kept points with g_bar > 0;
  low-acceleration rule 136 galaxies holding 1524 points, and 1537 kept points over all 155 galaxies with
  0 < g_bar < 0.3 g_dagger (the author's draft's tally of the same rule); placebo set 39 galaxies, 652 points; strict
  set 104 galaxies.
- C-6 the hold-out (before any pairing): analysis/holdout/GRV_EFE_3/MANIFEST.json exists (else BLOCKED, exit 2), names
  the committed drand round, n = 78, 78 distinct names all among the 155 eligible; the draw is reproduced from the
  manifest's recorded seed by the unchanged tool in a scratch directory and gives the same 78 names; its sha256 is
  recorded in the checkpoint.
- C-4 the local form: Delta at e_N = 0 is exactly 0; at a synthetic point g_N = 0.1 g_dagger, e_N = 0.05 g_dagger,
  log10(g_local/g_pred) = -0.22922 within 1e-4 (code -0.2292214260).
- C-5 conversion factor 1.2e-10/G_DAGGER = 1.10799 within 1e-4.
- Sealed-read structural checks (on the evidence unit, harness-only; the harness prints pass/fail and counts, never a
  value): S-1 sha256 equals f18ee3c7...248e7 in full (else exit 3, EFE-INSTRUMENT-OPEN); S-2 header exactly
  "galaxy,eN_a0"; S-3 row count in [150, 175] (the extractor's own range); S-4 names unique; S-5 every value parses as a
  finite float in [0, 1] (the extractor's own range); S-6 the name join is computed and its counts recorded.
- Synthetic fixtures (unit X, before the evidence; synthetic e tables written under a scratch path, the SPARC multiset
  of D as noise, seed s("GRV-EFE-3 FIX"); each runs the whole form logic and must return the pre-stated token or rate):
  - X-1 planted, a true H-LOCAL world at the hold-out size: each replicate draws a synthetic 78-of-155 subset (seed
    s("GRV-EFE-3 FIX")), e_N in a0 units log-uniform on [10^-2, 10^-0.5] per galaxy (one value per galaxy, shared by its
    low and high points), D = Delta + (D permuted across the subset's low-acceleration galaxies) and
    H = Delta_hi + (H permuted across the subset's placebo galaxies), Delta_hi from the section 3 form (section 4, P1);
    400 replicates; the whole form logic runs. Bars: (i) rate of EFE-LOCAL-FAVOURED >= 0.90; (ii) rate of
    EFE-CONFOUNDED <= 0.08; (iii) among EFE-LOCAL-FAVOURED, rate of Q2 CARRIES >= 0.90. Provenance: scratch_rev1.py and
    scratch_rev1b.py at size 78 give 0.9455 FAVOURED and 0.044 CONFOUNDED over 2,000 replicates, and CARRIES 1.00 among
    199 present of 200; at 400 replicates the binomial sd is sqrt(0.9455 x 0.0545/400) = 0.011 and
    sqrt(0.044 x 0.956/400) = 0.0103, so 0.90 is the measured rate less 4 sd and 0.08 is the measured rate plus 3.5 sd
    (0.044 + 0.036). Bar (ii) bounds the rate at which the veto turns a real effect into CONFOUNDED.
  - X-2 null: same e law and synthetic 78-galaxy subsets, D permuted with no Delta added; 400 replicates. Bar: rate of
    p_minus < 0.01 <= 0.03. Provenance: the nominal rate is 0.01; at 400 replicates its binomial sd is
    sqrt(0.01 x 0.99/400) = 0.005, and 0.03 is the expectation plus 4 sd (scratch: 0.015 at size 136 over 400
    replicates; 0.000 at size 78 over 200).
  - X-3 reversed: D = -Delta + permuted D; one replicate; pre-stated token EFE-REVERSED.
  - X-4 confound: planted as X-1 and the placebo residuals given H_h = (H permuted across placebo galaxies) - 0.3 x (average rank of e_h)/n_placebo; one
    replicate; pre-stated token EFE-CONFOUNDED.
  - X-5 coverage: only 20 synthetic names match; pre-stated EFE-OPEN-COVERAGE.
  - X-8 hold-out gate: with no synthetic manifest present the driver exits 2 printing BLOCKED and runs no pairing unit;
    with a synthetic manifest whose recorded seed does not reproduce its names, C-6 fails and the token is
    EFE-INSTRUMENT-OPEN.
  - X-6 underpowered: every e_N = 1e-6 a0; pre-stated EFE-OPEN-UNDERPOWERED.
  - X-7 tamper: one byte of a copy of a synthetic file changed against its recorded hash; pre-stated
    EFE-INSTRUMENT-OPEN.
- Diagnostic (recorded, not a halt): the extractor's git history if git is available in the sandbox.
- Smoke (LAB_SMOKE=1): runs C-0 to C-5 and X-3 to X-8 on synthetic tables and synthetic manifests, writes analysis/grv_efe_3_smoke.pkl, prints
  "smoke: forms withheld" and no form token, and never opens data/sparc_efe/.

## 6. THE FORMS

Reached in this order; the first that applies is rendered for its line.

Instrument line: EFE-INSTRUMENT-OPEN (any halt-grade credential, structural check or fixture fails) /
EFE-OPEN-COVERAGE (H-1 or H-2) / EFE-OPEN-UNDERPOWERED (F-3 power < 0.80 on the hold-out) / INCOMPLETE-OPEN (a unit
did not finish). BLOCKED (exit 2, no manifest yet) is a wait for the beacon, not a form.

Q1 line (only if the instrument line is clean):
- EFE-REVERSED: p_plus < 0.01 (residuals rise with e; against both readings).
- EFE-CONFOUNDED: p_minus < 0.01 and P1 fires.
- EFE-LOCAL-FAVOURED: p_minus < 0.01 and P1 does not fire.
- EFE-SOURCE-FAVOURED: p_minus >= 0.05 and p_plus >= 0.01.
- EFE-OPEN-GAP: 0.01 <= p_minus < 0.05 and p_plus >= 0.01.
(p_minus < 0.01 and p_plus < 0.01 cannot both hold.)

Q2 line (only on EFE-LOCAL-FAVOURED; otherwise "Q2 not read" and no token): EFE-FORM-CARRIES / EFE-FORM-UNDER /
EFE-FORM-OVER / EFE-FORM-OPEN, by section 4's bars.

Possible combinations: one instrument-line form alone; or a clean instrument line with one of five Q1 forms, and with
EFE-LOCAL-FAVOURED exactly one of four Q2 forms. The Director's expected form is EFE-LOCAL-FAVOURED.

## 7. WHAT COUNTS

Rider texts (on GRV-030; the scope clause "on the 78 SPARC galaxies drawn by drand round {round} (whose residuals the
programme had seen on the whole table; the draw removed the commission's choice of galaxies, not that exposure), with
Chae et al. 2020's e_env taken as the environmental field by the committed extractor's cell index, under the
registered g_dagger, nu and mass-to-light convention" ends each):

- EFE-LOCAL-FAVOURED: "GRV-EFE-3: the low-acceleration residuals of the registered prediction fall with the
  environmental field (Spearman rho_obs, p_minus, n galaxies), with no decline at high acceleration at the same alpha;
  the data favour H-LOCAL (the horizon coupling responds to the total field at the galaxy) over H-SOURCE." Plus the Q2
  sentence: CARRIES "and the zero-parameter one-dimensional local form carries the effect at its own amplitude (slope
  interval [L, U] contains 1)"; UNDER "but the effect is smaller than the local form predicts (U < 1), which the total-
  field nature of e_env may account for"; OVER "and the effect exceeds the local form's amplitude (L > 1)"; FORM-OPEN
  "and the amplitude is not resolved (L <= 0)".
- EFE-SOURCE-FAVOURED: "GRV-EFE-3: at a power of at least 0.80 to detect H-LOCAL's own predicted effect, the
  low-acceleration residuals do not fall with the environmental field (p_minus >= 0.05); the data favour H-SOURCE, and
  the low-acceleration misses of GRV-BLIND-2 are not environmental at this test's reach."
- EFE-CONFOUNDED: "GRV-EFE-3: residuals fall with the environmental field at low acceleration and also at high
  acceleration, where H-LOCAL predicts no effect; the correlation is attributed to a systematic shared with e_env and
  neither reading is favoured."
- EFE-REVERSED: "GRV-EFE-3: low-acceleration residuals rise with the environmental field (p_plus < 0.01), contrary to
  both readings; recorded as an anomaly, neither favoured."
- EFE-OPEN-GAP, EFE-OPEN-COVERAGE, EFE-OPEN-UNDERPOWERED, EFE-INSTRUMENT-OPEN, INCOMPLETE-OPEN: "GRV-EFE-3 did not read the
  question (reason, with the failing number)"; no reading favoured.

Grades and numbers. No form moves a grade (GRV-030 stays D1, Modeled) or any of the five numbers of NORTH_STAR section
2b: no target moves from blocked to derived, no input is retired, no prediction is externally adjudicated (the hold-out
is drawn by a public beacon, which is not an adjudicator). Said plainly: neither of the two progress numbers moves. What
any form does NOT establish: a mechanism (correlation is not mechanism; the form in section 3 is H-LOCAL's algebra, not a
mesh derivation); that e_env is the baryonic Newtonian field; that the extractor read the right column (a provenance
premise); anything beyond SPARC's 2788-point sample; anything about MOND's external field effect as such (the source
paper's detection is the prior, not this result); anything about the 77 eligible galaxies outside the hold-out. Bar W
is met by the beacon hold-out of section 2 as written; no form is downgraded after the fact, and no form is
exploratory.

SECTION 5 LINE: this commission names (c), the discriminator it adjudicates, between H-LOCAL and H-SOURCE, the two live
readings of the horizon coupling behind the Gravitational force row's D1 cell (GRV-030); the last locked session,
NUC-MIRROR-LEAN-3, was interior under the author's named exception, and this session is the target-facing one that
section 5 requires after it.

## 8. NOT ASSUMED

- Not assumed that the effect exists: the published detection used the authors' MOND fits with a fitted external
  field per galaxy; this test uses only e_env and the registered prediction, and the null is live.
- Not assumed that e_env is the right field for the mesh (it includes LCDM halo infill); hence Q2's UNDER is a named,
  not a rescued, outcome.
- Not assumed that the extractor's column index is right; carried as a premise in every rider.
- Not assumed that a non-firing placebo excludes confounds.
- No re-run, no alternative cut (0.1 g_dagger is a sub-reading only), no exclusion of galaxies after the read.
- Priors, stated and not leaned on: the Director expects EFE-LOCAL-FAVOURED; the theorist expects Q1 present (the
  source paper) and, if so, Q2 UNDER (total-field overstatement), at no better than even odds on Q2.

Sub-readings (printed after the forms; change no form; over held-out galaxies only): e and D for PGC51017 and UGC04305
against the matched held-out median e, if either is held out (otherwise "not drawn"); S1 on the held-out strict set (0 < g_bar < 0.1 g_dagger, at least three points); the low-acceleration point rms under the
registered and the local prediction; the ten galaxies of largest e with their D and Delta.

## 9. AUTONOMY AND COMPUTE

No step waits on a person. The one independent choice, the hold-out, is a beacon draw: at lock the lab commits a future
drand round (beacon_draw entry); when it is published the lab runs the section 2 command; until then the driver exits 2
with BLOCKED. The evidence file is already committed. Units, one per invocation, checkpoint analysis/grv_efe_3_ckpt.pkl
(atomic, resumable): U0 credentials C-0 to C-5 and fixtures X-1 to X-8 (no file under data/sparc_efe/); U1 SPARC
residuals D, H and inputs for Delta, whole table; UH the hold-out (C-6; BLOCKED, exit 2, if no manifest); U2 sealed read
(S-1 to S-6 on the whole file, H-1, H-2 on the hold-out; e of held-out galaxies only to the checkpoint, no value
printed, the rest discarded); U3 F-3; U4 S1, P1, Q2, sub-readings; terminal line "GRV-EFE-3 COMPLETE:
run the verdict". The verdict script reads the checkpoint only: validates status, units, hashes and finiteness, creates
analysis/GRV-EFE-3_verdict.log with O_EXCL, then renders the instrument line, Q1, Q2 in that order.
Compute: about 1e4 permutations and 2e3 power replicates over at most 78 galaxies, 1e4 bootstrap fits, fixtures about
800 replicates; under 0.3 cpu hours, 1 GB, under 45 minutes wall (scratch: 2,000 X-1 replicates in under 10 s).
Existing files: tools/holdout_galaxies.py and the lab's beacon tool (the GRV-BLIND-2 path), benchmarks/gravity/grv_blind_1.py,
tools/extract_chae2020_eenv.py, data/sparc_rotmod/, data/sparc_efe/chae2020_eN.csv, benchmarks/lab/_kit/labkit.py. The
worker writes benchmarks/lab/grv_efe_3/driver.py and benchmarks/lab/grv_efe_3/verdict.py.

## DISCLOSURES (the cures)

- GRV-EFE-1's death (the sealed input could not be credentialed from inside the sandbox): cured by redefining the
  credential as what the sandbox can check and stating the rest as a premise. Checked: the file's sha256 against the
  value written before anyone opened it; the extractor's sha256; header, row range, uniqueness, value range and name
  join, harness-only. Not checkable, and therefore carried in every rider: that the extractor's cell index is e_env.
  The gate itself is credentialed on seven synthetic fixtures with stated answers, including a planted effect that must
  be found and a null that must not.
- A count in the record: the parked GRV-EFE-1 draft records the extractor's printed row count. This design does not use
  it as a bar.

Revision 1 (answers to the skeptical review):
- Bar W conditional (objections 1, 7, 9): the conditional is removed and option (b) is taken. The scored set is a
  78-of-155 beacon hold-out (section 2), with the beacon_draw entry, the BLOCKED / exit 2 path, C-6 and X-8 added, F-3
  re-sized on the hold-out, and H-1 and H-2 restated for it. The NUC-NEW-5 / NUC-MIRROR-LEAN reading is no longer cited.
  Option (a) was not taken because GRV-030's nu was selected on this table (simple over tanh), so "no fit against
  SPARC" could not be argued cleanly. Section 7 now commits: no form is exploratory, and the section 5 line stands.
- The 0.3 g_dagger cut (objections 2, 8(i)): the cut is the author's draft rule verbatim and was never changed. The
  1537 versus 1524 difference is two tallies of the same rule: 1537 counts every kept point with 0 < g_bar < 0.3 g_dagger
  over all 155 galaxies; 1524 counts those points in the 136 galaxies with at least three of them (scratch_rev1.py
  reproduces both, and both with g_dagger at the code value or at 1.083e-10). C-3 now pins both.
- Placebo cut and three-point minimum (objections 3, 8(ii), 8(iii)): provenance stated in section 2 (the registered
  eligibility minimum, the author's low-acceleration rule, g_dagger as the model's only scale, and the computed ratio
  0.130).
- The veto under a true H-LOCAL (objections 4, 9): the high-acceleration shift is computed from the section 3 form on
  synthetic e (ratio 0.130 mean, 0.152 largest, section 4 P1); X-1 now plants it into the placebo residuals, and bar
  (ii) caps the rate of EFE-CONFOUNDED under a true H-LOCAL at 0.08, above the measured 0.044 by 3.5 sd at 400
  replicates. The reviewer's example ceiling of 0.05 was not used because the measured rate, 0.044, sits within one sd
  of it at 400 replicates and the fixture would halt by chance; the measured price of the veto is stated in section 4.
- H-1 and H-2 foregone (objection 5): section 4 now states that the GRV-EFE-1 record makes both halts foregone, that
  they are fail-closed guards with no evidential weight and are not cited as checks, and that their thresholds were
  fixed by a writer aware of that record. H-2 is 10 (twice the attainability minimum) rather than 15, because a
  half-table draw falls below 15 with probability 0.029 even under full matching.
- X-2's 0.03 (objections 6, 8(iv)): the binomial arithmetic is written out (0.01 + 4 x 0.005).
- Scratch: analysis/lab/drafts/GRV-EFE-3/scratch_rev1.py and scratch_rev1b.py read only data/sparc_rotmod and
  synthetic e; neither opens data/sparc_efe/.
- Constants are code values from the scratch scripts, pinned no tighter than the registry's digits (C-1, C-2) or at
  1e-4 where the design quotes five or six digits.
- No evidence was opened while writing this design; the scratch scripts read only data/sparc_rotmod and synthetic e.
