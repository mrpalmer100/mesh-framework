# COMMISSION GRV-BARS-OC-1 -- THE OPERATING CHARACTERISTIC OF BAR W's BARS RULE ON THE SPARC TABLE
# (CHARTER, the author's DRAFT for the lab's lock; nothing has run; no number in this charter was read from the table)

Supersedes the withdrawn GRV-BLIND-OC (three lock rounds, 2026-10-15/16; the external reviewer's objections are
answered by construction below, not by argument). Same question key family; a different question from GRV-BLIND-2,
whose fail is kept and is not re-read here.

## 1. The question, and the North Star line

Question key: grv-bars-rule-operating-characteristic.

The bars rule B-1 of GRV-BLIND-1 and GRV-BLIND-2 (benchmarks/gravity/grv_blind_1.py, bars()) sets, for a draw of
n_test = 30 galaxies out of the 155 eligible, two bars from the 125 training galaxies the draw leaves behind: the
0.95 quantile, over 20,000 random 30-galaxy subsets of the training pool drawn without replacement, of the subset rms
of log10(g_obs) - log10(g_pred) at the predicted g_dagger, and the 0.95 quantile of the subset's worst per-galaxy
rms. A held-out draw passes if its rms is at or under the first and its worst galaxy at or under the second.

Q1 (the rms bar). Over many disjoint, uninspected train/test splits of the shipped table, how often does the held-out
rms exceed the rms bar computed from that split's own training complement? The rule's nominal rate is 5 percent.
Q2 (the worst-galaxy bar). The same for the worst-galaxy bar.
Q3 (the verdict rule). The same for the joint rule actually used to render BLIND-AGREES or BLIND-FAILS (either bar
exceeded), whose nominal rate the GRV-BLIND-2 charter stated as "about 5 to 10 percent" without measuring it.
Q4 (the fixed-bar alternative, recorded, not read). The same three rates for bars computed ONCE from all 155 eligible
galaxies by the same quantile rule and held fixed across every split. This is the candidate rule STRATEGIC_TARGETS
section AL names; this commission measures it beside the current rule and adopts nothing.

North Star line (section 5): an instrument charter under section W, serving the gravity row's D1 cell
(docs/NORTH_STAR.md section 2, "blind-scored under bar W"). It arms no new discriminator; it makes the existing one
readable by stating what a pass and a fail under B-1 mean. The five numbers cannot move; by section 2b this is
infrastructure, and the results write-up says so in those words.

What this commission does NOT do, stated first: it does not re-read, re-bar, re-draw or soften GRV-BLIND-2 (kept,
GRV-129); it does not change B-1 for any past verdict; it does not adopt a new rule (adoption is the author's act, at
promotion, after reading the table this commission produces); it reads no sealed truth, since no truth is sealed
here (every galaxy is public and was in GRV-030's whole-table run; bar W's one-read discipline does not apply to an
instrument study of the bar itself, and the charter says so rather than pretending otherwise).

## 2. The parts list (every input cited; nothing is chosen in this commission)

| part | what | source |
|---|---|---|
| the table | data/sparc_rotmod, 175 files; eligibility as the registered confrontation: at least three points with errV/Vobs < 0.1, r > 0, Vobs > 0; 155 eligible | tools/holdout_galaxies.py kept_mask; GRV-BLIND-1 manifest (155) |
| the prediction | g_pred = g_bar nu(g_bar/g_dagger), g_dagger = c H0 / 2 pi, H0 = 70; M/L gas, 0.5 disc, 0.7 bulge | GRV-030; benchmarks/gravity/grv_blind_1.py (nu_simple, G_DAGGER) |
| the per-galaxy statistics | for every eligible galaxy: the sum of squared residuals, the kept point count, the per-galaxy rms, at the predicted g_dagger | computed once at setup by the registered code path (grv_blind_1.bars reads them the same way) |
| the bars rule B-1 | 0.95 quantile over 20,000 subsets of 30 from the training pool, of subset rms and of subset worst-galaxy rms | GRV-BLIND-1 charter B-1; grv_blind_1.bars() |
| the draw rule | 30 of 155 uniformly without replacement, numpy default_rng(seed) | tools/holdout_galaxies.py draw() |
| the split schedule | seed_i = int(sha256("GRV-BARS-OC-1 split " + str(i))[:8], 16) & 0x7fffffff for i = 1..N, N = 1000 | this charter; fixed here, never run before by anyone, disjoint by construction from the 12 seeds the withdrawn GRV-BLIND-OC previewed and from 52525254 and 1083026663 |
| the synthetic control | residual vectors drawn iid Gaussian with the table's per-galaxy point counts and the table's pooled residual standard deviation; seed_c,i = seed_i + 10**9 | this charter |

Nothing in this charter was set by looking at any output of the table: the split count, the thresholds and the
control band below follow from the binomial arithmetic of N = 1000 at the nominal rates, and from nothing else.

## 3. Steps (one unit per invocation; checkpoint analysis/grv_bars_oc_1_ckpt.pkl, atomic; resumable)

S0 setup: read the table once; compute the per-galaxy statistics; write their sha256 and the kept point count into
the checkpoint; record the sha256 of benchmarks/gravity/grv_blind_1.py, tools/holdout_galaxies.py and this charter.
S1 credentials (C-1 to C-3 below); any failure writes status CREDENTIAL-FAIL and stops.
S2 the fixed bars (Q4): B-1's quantile rule applied once to all 155 galaxies; written to the checkpoint.
S3 the splits, in chunks of 100 (ten invocations): for each seed_i, the draw, the training-complement bars by B-1
(20,000 subsets, rng seeded seed_i, exactly as bars() seeds it from the manifest), the held-out rms and worst-galaxy
rms, the three exceedance indicators under the split bars and the three under the fixed bars; the held-out galaxy
list; written per split.
S4 the control: the same loop on the synthetic residuals for every seed_c,i (the real galaxies' point counts, iid
Gaussian residuals), recording the three exceedance indicators under split bars.
S5 terminal seal: status COMPLETE, the complete plan (N, the schedule rule, the chunk coverage), the digest of every
preceding checkpoint field, written last; the driver prints "GRV-BARS-OC-1 COMPLETE -- run the verdict".

## 4. Credentials (pass bars locked here; every one must pass before S2)

C-1 the bars rule reproduces GRV-BLIND-1's recorded bars from GRV-BLIND-1's recorded draw: 0.180044 and 0.632099
within 1e-6 (analysis/GRV_BLIND_1_bars.json; the draw from seed 52525254).
C-2 the same for GRV-BLIND-2: 0.158245 and 0.522359 within 1e-6 (analysis/GRV_BLIND_2_bars.json; seed 1083026663).
C-3 the draw rule reproduces both recorded held-out lists exactly (analysis/holdout/GRV_BLIND_1/MANIFEST.json,
analysis/holdout/GRV_BLIND_2/MANIFEST.json).
These read files already on the record; they expose nothing new. They are the only table-derived numbers this
charter cites, and they were set by those files, not by this commission.

## 5. The floor test (the control, computed in S4; a bar on the instrument, not on the rule)

Under iid Gaussian residuals with no galaxy structure, B-1's rms bar is a 0.95 quantile of subset rms over subsets
of the training pool, and the held-out rms is one more such subset from the complement; its exceedance rate is near
5 percent by construction (not exactly: the complement is excluded from the pool). The floor: the control's observed
rms-bar exceedance rate over N = 1000 lies in [3.0, 7.0] percent (the nominal 5 percent, plus or minus about 3
binomial standard deviations of 0.69 percent, widened to whole numbers before any run). CONTROL-FAIL if not; the
instrument is then not credentialed to read the real table and the verdict stops at that form.

## 6. The bars (locked here; from the binomial arithmetic of N = 1000 and the nominal 5 percent; no pilot)

For an observed rate p_hat over N = 1000 splits, the 95 percent Wilson interval has half-width about 1.35 percent at
5 percent. The thresholds:
- CALIBRATED: the Wilson 95 percent interval of p_hat contains 5.0 percent.
- TOO-NARROW: the whole interval lies above 5.0 percent (the rule fails honest draws more often than it says).
- OVER-WIDE: the whole interval lies below 5.0 percent.
Q3 (the joint rule) is read against its own nominal band: CALIBRATED if the interval contains any value in
[5.0, 10.0] percent (the GRV-BLIND-2 charter's stated prior); TOO-NARROW if wholly above 10.0; OVER-WIDE if wholly
below 5.0.
Q4 is recorded (the three rates and intervals under the fixed bars) and read by no form.
Sub-reading, recorded, not read: among the splits whose worst-galaxy bar is exceeded, the fraction in which the
held-out set contains at least one of the two galaxies that set the top of the training distribution in the splits
that exclude them (the identity of those galaxies is an OUTPUT of S3, the two most frequent setters of the
worst-galaxy bar across splits; the charter names none).

## 7. Verdict forms (exhaustive; reached in this order)

FORM (instrument): CREDENTIAL-FAIL (any of C-1 to C-3), CONTROL-FAIL (section 5), CHECKPOINT-INVALID (section 8),
INCOMPLETE-OPEN (status not COMPLETE, or chunk coverage short of N).
FORM (Q1): RMS-BAR-CALIBRATED / RMS-BAR-TOO-NARROW / RMS-BAR-OVER-WIDE.
FORM (Q2): GAL-BAR-CALIBRATED / GAL-BAR-TOO-NARROW / GAL-BAR-OVER-WIDE.
FORM (Q3): RULE-CALIBRATED / RULE-TOO-NARROW / RULE-OVER-WIDE.
Q4 and the sub-reading are printed, not formed. The three Q forms are independent; each is read from its own
interval; none is read from another's. A TOO-NARROW on any form says only that the rule's nominal rate understates
its false-fail rate; it says nothing about the size of GRV-BLIND-2's miss, which this commission does not measure
and the write-up must not characterise.

## 8. The verdict script (benchmarks/lab/grv_bars_oc_1/verdict.py; frozen at lock)

Reads the checkpoint only. Before any statistic: refuses (exit 2, CHECKPOINT-INVALID) unless the checkpoint carries
status COMPLETE with every field of the plan present (N = 1000 seeds, each equal to the schedule rule's value for its
index, all distinct; chunk coverage 1..N with no gap; the control's N entries; the fixed bars; the credential results;
the file hashes equal to those recorded at lock in analysis/lab/locks/); a checkpoint with status CREDENTIAL-FAIL or
CONTROL-FAIL renders that form and nothing else. The verdict log analysis/GRV-BARS-OC-1_verdict.log is created with
O_EXCL before evaluate() runs; an existing log refuses the run (one verdict, kept); an interrupted run leaves the
log and the refusal stands. Every number the forms read is printed with the interval that produced it.

## 9. Budgets

Setup under a minute. Each split: 20,000 subsets of 30 from 125 (sums of precomputed per-galaxy statistics;
vectorised, no file reads). Estimate 0.2 to 1 s per split, so 1000 splits in 4 to 20 minutes, the control the same
again; declared cpu_hours 2 to leave room for an order of magnitude; mem_gb 1; usd 0.

## 10. Disclosures (instrument and process)

The withdrawn GRV-BLIND-OC ran a 60-split pilot on this table and previewed 12 evidence seeds before its lock; its
thresholds were set with those results in view, and the external reviewer rejected it three times for that. This
charter is written by the author without running anything; its seed schedule is a fresh deterministic rule; its
thresholds and the control band come from binomial arithmetic at the nominal rates; the only table-derived numbers
cited are the two recorded bar pairs and two recorded draws, already on the record. The executor's reading in
STRATEGIC_TARGETS section AL (that one galaxy set GRV-BLIND-1's worst-galaxy bar and moved into GRV-BLIND-2's test)
is a reading of kept files, not a run; the sub-reading in section 6 asks the table to name the setters itself and
reads no form from them. Whether the result changes the gravity row's reading of GRV-BLIND-1 or GRV-BLIND-2 is a
question for the author at promotion; the forms here are about the rule.

```lab
commission: GRV-BARS-OC-1
target: "Gravity row D1 cell (NORTH_STAR section 2): an instrument charter under section W that makes bar W's verdicts readable by measuring the bars rule's false-fail rate; arms no discriminator, moves no number"
driver: benchmarks/lab/grv_bars_oc_1/driver.py
verdict_script: benchmarks/lab/grv_bars_oc_1/verdict.py
instrument:
  - benchmarks/gravity/grv_blind_1.py
  - tools/holdout_galaxies.py
forms: [CREDENTIAL-FAIL, CONTROL-FAIL, CHECKPOINT-INVALID, INCOMPLETE-OPEN, RMS-BAR-CALIBRATED, RMS-BAR-TOO-NARROW, RMS-BAR-OVER-WIDE, GAL-BAR-CALIBRATED, GAL-BAR-TOO-NARROW, GAL-BAR-OVER-WIDE, RULE-CALIBRATED, RULE-TOO-NARROW, RULE-OVER-WIDE]
state: [analysis/grv_bars_oc_1_ckpt.pkl]
budget: {cpu_hours: 2, usd: 0}
mem_gb: 1
```
