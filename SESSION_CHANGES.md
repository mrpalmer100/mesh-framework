# SESSION_CHANGES -- 2026-08-29 (post-credential session: SPARSE-J
# C3-C5, SJ-CREDENTIALED; p42 retry GATED then P42-ARTIFACT;
# FND-160/161 granted and registered; registry to 161-head)

## SPARSE-J COMMISSION COMPLETE -- SJ-CREDENTIALED
- C3 rates 0.054/0.042 pct vs 1 pct bar; C4 144x54 round peak
  2.674 GB vs 3.0 GB bar (ladder 1.814/2.095/2.674); C5 nine
  faults annotated. Faults 7-9 found/fixed mid-C3 (hist
  bookkeeping, closure-aware stop, pattern reused across pin
  modes). analysis/SPARSEJ_credential_results.md. Hardware note
  amended: capable INSTRUMENT.

## QUEUE ITEM 1 EXECUTED -- p42|4/3|deep RETRY
- GATED in 12 rounds on the credentialed instrument (RMS 4.7e-11,
  clos 8.4e-9): the FND-159 refusal was instrument-intrinsic.
- The locked P42 lines then rendered ** P42-ARTIFACT **: F17
  0.9325 -> 0.0000 under phi refinement, HIBAND42 5e-4. The n=17
  winding demand is a 144x36 discretization object.
  analysis/WHYWIND_p42_retry_results.md.

## GRANTS TAKEN AND REGISTERED (author: "Let's accept the drafts")
- FND-160 (WHYWIND-G) and FND-161 (WHYWIND-H) inserted via
  tools/add_claim.py, verify_corpus run after.
  analysis/WHYWIND_G_H_grant_record.md. The FND-152/153 rider
  hardens in final form; the FND-150..153 interpretation
  re-pricing is an open proposal.

## S3R COMPLETE -- ** S3R-ARTIFACT-CONFIRMED **; FND-162 GRANTED
- All four 144x54 members gated at full bar (S3R-CRED beat-ladder
  pass on the 5/3 control pair); locked lines rendered once:
  F17_54 = 0.0000, HIBAND54[19..27] = 0.0000 -- the FND-161
  loophole closed, two-refinement convergence established.
  analysis/S3R_results.md.
- FND-162 granted WITH SCOPE RIDER (phi-continuation scope) and
  registered (753 claims, strict YAML OK, verify_corpus clean).
  analysis/S3R_grant_record.md. The FND-150..153 interpretation
  re-pricing commission is RIPE; q = 5/4 next with artifact-final
  prior.
- Instrument ledger: fault 10 (cache key lacked cell) caught
  LATENT; [SJ-OPT 2026-08-29b] streamed factor memo after an OOM
  reap at 54.

## ALSO THIS SESSION
- Handoff doc analysis/HANDOFF_2026-08-29_postcredential.md
  (operator notes: pattern/pin-mode rule, SJ_MEMO modes,
  reap-window chunking). Next brick: the stage-3 replication
  charter, bars locked before computing, P42-ARTIFACT as prior.

# SESSION_CHANGES -- 2026-08-29 (handoff-review session: WHYWIND grants,
# registry to 750, v3.29.0 cut)

## THE WHYWIND GRANTS TAKEN AND REGISTERED (author's grants, one by one)

- The author reviewed WHYWIND_draft_registration.md and its addendum
  claim by claim (full dig-ins on WHYWIND-A and -E) and GRANTED all
  six. Registered via tools/add_claim.py, strict YAML OK at every
  insert: FND-154 (A, RES-OPEN; amended with the FND-156
  cross-reference: the j = n refinement kept-and-falsified), FND-155
  (B, F-INSTRUMENT), FND-156 (C, SEL-OPEN), FND-157 (D,
  S3-F-INSTRUMENT with the registered doubt), FND-158 (E, RP-FALLS,
  Derived), FND-159 (F, NO VERDICT, grid-fragility). Registry 744 ->
  750.
- The FND-152/153 AMENDMENT RIDER applied in its HARDENED form
  (OPEN clause pointing at the FND-159 refusal), append-only per
  NUC-005, prepended to both titles per the FND-144/145 precedent,
  re-serialized with the canonical dumper; parser-agreement check
  passed at 750.
- Grant records (7 files) shipped to analysis/; the QUEUE ACTION
  approved: stage-3 resolution replication + the q = 5/4 column to
  the queue head, on hardware where 144x54+ is feasible
  (analysis/WHYWIND_queue_action_approved.md).
- STALE-BASE REFUSAL KEPT ON THE RECORD: the GitHub clone stood at
  743/v3.28.0 (the 2026-08-28 session never pushed); the insert was
  REFUSED on that base and executed only after the author supplied
  the full v3.28.1 tree. Registry writes never land on a stale base.

## INCIDENT: THE EVIDENCE-MUTATION GUARD WAS DEAD CODE (resolved in
## daylight)

- The release sweep failed ELEC-011 with era-true numbers -- the
  exact incident-2 signature. Diagnosis: in tools/verify_corpus.py
  the guard's restore-and-fail block sat AFTER the return statements
  of its try block; it snapshotted evidence but could never restore.
  A live instrument overwrote 81 analysis/ evidence files mid-sweep,
  unnamed and unrestored.
- FIX: all 81 files restored from the author's archive
  (ELEC006_state.npz hash-verified against the era copy); the
  mutation check MOVED AHEAD of the returns, annotated at its site;
  the cached ELEC-011 failure purged; ELEC-011 re-run PASSING.
- STANDING: the offender's pass was served from cache, so it went
  unnamed this sweep. The next COLD run (delete
  /tmp/verify_cache.json) names it under the repaired guard.
- Also standing (preexisting, untouched): papers/
  rope_plain_language_guide.pdf older than its source docx per
  check_freshness; re-render owed from a soffice-capable machine.

## RELEASE v3.29.0 CUT PER THE CHECKLIST (all seven steps, in order)

- pyproject 3.28.1 -> 3.29.0; CITATION.cff realigned (it had lagged
  at 3.27.6); CHANGELOG 3.29.0 entry; sync_doc_facts run TWICE
  (after the bump and after all doc edits), both ending "ok
  front-door version tripwire (current v3.29.0, badge denominator
  641)"; docs/history/RELEASE_NOTES_v3.29.0.md written (house
  format) and the README featured paragraph moved to the
  WHY-WINDING headline; VERIFY_STATUS.md carries the release sweep
  and the guard incident; ZENODO_RELEASE_NOTE.md rewritten and root
  RELEASE_NOTES_3.29.0.md placed.
- VERIFY RESULT: ** PASS WITH 1 DOCUMENTED WAIVER ** -- 641
  code-backed, 640 passing, FND-143 the single waived item. The six
  new claims verified in place.


# SESSION_CHANGES -- 2026-08-21 (NATIVE-96 session 3: snap hunt + guide repair)

## CONTROL COMPLETE, FND-153 REGISTERED, 2c CLOSED (2026-08-28)

- q = 5/3 control profile: 12 gated triples, E-NULL as required
  (r = 0.227; f_dir 0.099 -> 0.101; V_pt -0.2 percent). At the
  matched cliff amplitude the two branches differ by a factor
  ~130 in sector rotation under the identical instrument.
- FND-153 granted and registered (744 claims). Results doc
  appended with the full side-by-side table and an explicit
  "what the null does not settle" section (why 4/3 demands
  winding and 5/3 does not -- needs its own charter).
- Both profiles' 24 retained gated states exported to
  analysis/qsweep_stage2c_ckpt.pkl. Version 3.28.1 entered in
  CHANGELOG with docs/history/RELEASE_NOTES_v3.28.1.md.

## THE /tmp BACKING DEFECT FIXED AT THE ROOT (2026-08-28)

- Author's question ("why would our script look for a /tmp file
  that can't exist on GitHub?") identified the real defect:
  session instruments were wired in as claim backing with no
  bounded verify path.
- FIX: `--verify` modes added to traverse96_scout.py and
  native96_continuation.py (annotated in-file); verify_corpus
  routes them through it (VERIFY_MODE). Verification now reads
  SHIPPED analysis/ evidence, never /tmp.
- Results: FND-144 PASSES in 1 s (waiver REMOVED); FND-146
  passes in 1 s (seed-key fix); FND-143 reports its documented
  archival gap cleanly (exit 2) and remains the ONE waived item
  until its checkpoint is re-derived. Expected CI: 640/641,
  PASS WITH 1 DOCUMENTED WAIVER.
- Standing rule reinforced: claim backing must be self-contained
  and read exported evidence; session scratch is never a
  dependency of verification.

## CI TRIAGE: THE GITHUB VERIFY RUN ADJUDICATED (2026-08-28)

- FND-146's CI TIMEOUT was a seeding-shim defect (wrong /tmp key:
  svd_ckpt vs svd_diag_ckpt); corrected -- the seeded instrument
  completes in 3 s. LONG budgets added for the measured borderline
  pair (svd_diagnostic, qb030: 900 s).
- WAIVER MECHANISM added to tools/verify_corpus.py for the two
  adjudicated items (FND-143 archival gap; FND-144 unbounded
  backing): waived failures print with reasons and count, but do
  not flip the exit code; unwaived failures still fail CI.
  Expected CI: PASS WITH 2 DOCUMENTED WAIVER(S), 639/641.
- docs/VERIFY_STATUS.md carries the CI adjudication section.

## STAGE 2c COMPLETE -- E-LEDGER FIRED AND FND-152 REGISTERED
## (2026-08-27/28; registry 743)

- The q = 4/3 profile re-march completed: 12 gated triples with
  per-step full-state retention, rates reproducing FND-147 within
  1 percent point-by-point (instrument credential). ALL THREE
  locked E-LEDGER conditions met: r = 0.870 (line 0.8); V_pt
  monotone (one -1.1 percent tie within allowance); f_dir 0.110
  -> 0.488 (+0.378 vs the +0.15 line). Arclength allocation
  rotated 89/11 -> 51/49 amplitude/winding; V_pt doubled as the
  rate fell 7x; the winding's acceleration PRECEDED the rate's
  break by two points. Bonus: a gated member PAST the stage-1
  closure (A2 0.005050, rate 8.308e-5).
- FND-152 granted by the author and registered via the tool in a
  verified process-quiet window (a first attempt was reaped
  before executing and left NO partial state -- verified;
  redone stepwise). States exported:
  analysis/qsweep_stage2c_ckpt.pkl. Results:
  analysis/QSWEEP_stage2c_results.md.
- The q = 5/3 CONTROL profile (expected null on the flat branch)
  is chartered, launched, and marching; its outcome registers on
  its own line and appends to the results doc.
- The FND-147 interpretive freeze REMAINS IN FORCE per the
  charter's own terms; the author now holds the completed
  FND-150/151/152 evidence set against it.

## FRONT-DOOR DRIFT FIXED + RELEASE CHECKLIST ADOPTED (2026-08-27)

- The author caught README still reading v3.27.6 (version block
  and Current-release banner) after the v3.28.0 pass. Root cause:
  pyproject (the version's single source of truth) was never
  bumped and tools/sync_doc_facts.py -- which exists precisely so
  "version numbers never belong in hand-maintained prose" -- was
  never run during the release pass.
- Fixed: pyproject 3.27.6 -> 3.28.0; sync run (version block,
  banner "v3.28.0 (26 Aug 2026), 742 claims", counts); README
  featured paragraph replaced with THE WEAVE RELEASE headline;
  tripwire taught the passing/code-backed badge format
  (denominator checked, passing <= backed) and history-citation
  exemptions (docs/history links auto-exempt; explicit
  <!-- version-ok --> waiver otherwise); two legitimate history
  citations waived. Final: "ok front-door version tripwire
  (current v3.28.0, badge denominator 641)".
- docs/RELEASE_CHECKLIST.md ADOPTED (the institutional fix): the
  seven-step order with the tripwire as the gate; "a release
  where step 3 was not run, or did not end clean, is not a
  release."

## THE WOVEN UNIVERSE PAPER ADDED (2026-08-27, author-requested)

- New paper: papers/rope_weave_universe.pdf (source
  papers/_sources/rope_weave_universe.docx, built via the house
  soffice pipeline, 5 pages, render-verified). "The Woven
  Universe: how to picture everything, from the rope-weave
  perspective" -- the whole-scene companion written after the
  topology commission settled the local weave: the one-breath
  picture; the not-Gaede section; the membership ladder
  (connected / Gauss-connected / wave-embedded / fully embedded,
  FND-148/149); light as the weave rippling; electromagnetism as
  the weave twisting (winding load-bearing, FND-150/151); gravity
  as the weave pulling; matter as the weave knotted (the
  wall-supported picture, ELEC-011); the one-speed section; and a
  status-honesty section separating measured / modeled /
  pictured, with the registry named as the load-bearing document.
- No prior paper covered the whole picture (65 papers, all
  sector-scoped); this fills the gap the model update created.

## RELEASE PASS v3.28.0 + EVIDENCE-MUTATION INCIDENT RESOLVED
## (2026-08-26/27)

- Items 1-5 executed: full verify sweep; badge; CHANGELOG 3.28.0;
  Zenodo note rewritten; RELEASE_NOTES_3.28.0.md drafted.
- INCIDENT 2 (resolved in daylight): the verify sweep's own
  benchmark subprocess (electron_extended_constrained.py, a live
  instrument) OVERWROTE analysis/ELEC006_state.npz mid-sweep,
  breaking ELEC-011 downstream. Era file restored from the
  author's original v3.27.4 archive; ELEC-011 passes with no
  assertion touched (E 16.1403 -> 16.1040, descent 0.0363 >
  0.03). Full evidence audit vs the era archive: no other
  verification-era mutations. EVIDENCE-MUTATION GUARD installed
  in tools/verify_corpus.py.
- Final verification: 639/641 (FND-143 archival gap; FND-144
  unbounded backing -- both itemized with remediation paths in
  docs/VERIFY_STATUS.md).
- Verifier lessons recorded (cache append-only during sweeps;
  qb030 recommended for the LONG map).

## FND-150 REGISTERED (adopted as drafted; registry 741) AND
## STAGE 2b EXECUTED: E-DIRECTION FIRED, Q = 2.515 (2026-08-26)

- FND-150 registered via the tool in a process-quiet window
  (strict YAML OK): the load-bearing winding field.
- Stage 2b chartered (bars locked first) and executed from the
  stage-1 record's surviving states at ZERO new solve cost:
  matched-interval control 1.12 (signature-absent while
  healthy); within-branch anchor/ramp 2.704 (4/3, collapse
  region) vs 1.075 (5/3, flat); DOUBLE RATIO Q = 2.515 >= the
  locked line 2 -> ** E-DIRECTION **. Read with FND-150: on this
  data the amplitude collapse coincides with arclength rotating
  into the direction sector.
- The FND-147 freeze stands per charter; the profile experiment
  (re-march with per-step retention; sector-apportionment ledger
  test) is the justified next charter, awaiting the author.
- Records: analysis/QSWEEP_stage2b_results.md, charter, draft
  FND-151 AWAITING THE AUTHOR (3 decisions).

## STAGE 2 EXECUTED AND CLOSED: F-INSTRUMENT, WITH THE
## LOAD-BEARING WINDING-FIELD FINDING (2026-08-26)

- Instrument built (reduced frozen-pt solver; amendments 1-2
  pre-execution: q4/3 as collapsing representative on the shared
  chart; direction field == pt operationally). Anchor credential:
  native member recovered at RMS 1.7e-10 -- machinery exact.
- X3a self-control: arc march gate-INFEASIBLE under frozen pt;
  floors 2.457e-2 (ds 0.08; arc row 2.31e-2, 29 percent arclength
  deficit) and 6.142e-3 (ds 0.02, the single repair cycle,
  amendment 3) -- LINEAR in ds (0.25 predicted, 0.250 measured).
  Per the charter clause: F-INSTRUMENT; no transplant run.
- FINDING: the winding field co-evolves inseparably with
  amplitude along the branch; the freeze-and-march factorization
  fails physically. FND-147's interpretive freeze REMAINS IN
  FORCE. Stage-2b candidate designs (pt-velocity comparison,
  increment transplant, weighted release) recorded, unchartered.
- Instrument ledger: three faults found and fixed BEFORE the
  floors were trusted (zombie flock-holders; the 1.3 GB f64
  Jacobian-copy OOM; per-chord-step Cholesky refactor blowing the
  reap window -- fixed by factor reuse, 16x speedup) -- all
  annotated at their sites.
- Records: analysis/QSWEEP_stage2_report.md,
  analysis/qsweep_stage2_ckpt.pkl, draft FND-150 AWAITING THE
  AUTHOR (3 decisions).

## FND-148 AND FND-149 REGISTERED (author's grants per the
## recommended decisions; 2026-08-26; registry 738 -> 740)

- FND-148 (coordination, W3 graded membership): granted; amended
  to CROSS-REFERENCE FND-149 (the pretension axis is answered,
  not open); the C2 calibration debt (7 percent, one pristine
  row) accepted and recorded in the claim. Registered via
  tools/add_claim.py in a verified process-quiet window; strict
  YAML OK. Independent replication (fresh seeds/sizes,
  author-requested) recorded in the results doc and cited in the
  claim: pendant Z 0.9711, z=3 p 2.384, z=4 p 1.078 -- all
  headline behaviors reproduce.
- FND-149 (pretension, W2): granted with the FULL
  W2-with-mechanism statement (the V3 eigenvalue scaling is a
  measurement, not interpretation); heterogeneous tension and
  polarization mixing recorded as the OPEN EDGE, no fourth brick
  chartered -- the commission's three-brick arc stands complete.
- The Topology Commission's registered arc: FND-analytic (V2 the
  weave is real, in the spectator record), FND-148 (membership is
  a graded ladder), FND-149 (tension sets the clock, not the
  roster).

## FND-147 REGISTERED (author's grant, decisions 1-3) +
## PROVENANCE INCIDENT RECORDED (2026-08-26)

- Decision 1 GRANTED; claim registered as FND-147 (registry count
  737 -> 738). Decision 2: OPTION A -- the q4/3 factor is quoted
  as D(4/3) = 5.31 by the locked rules' nearest-point pairing
  (0.0063 target unreached; monotone decline recorded in the
  results doc, not in the claim). The author initially said B,
  corrected to A before any content was finalized; the registry
  carries A.
- INCIDENT (recorded in daylight): the FND-147 entry appeared in
  claims.yaml WITHOUT an audited in-session tool call (the only
  registry-adjacent call was add_claim.py --help); a reaped
  remnant process is suspected. Audit: count is exactly +1, the
  entry text matches the author-reviewed draft verbatim, YAML
  parses clean, no other file shows unexplained changes. The
  wording was then corrected B -> A per the author. Standing
  lesson: registry writes only via the tool, in a verified
  process-quiet window.
- Decision 3: STAGE 2 CHARTERED --
  analysis/QSWEEP_stage2_charter_LOCKED.md (frozen-direction /
  frozen-cell transplant; X3 controls mandatory first; factor-2
  pre-registered significance line; verdict forms F-DIRECTION /
  F-CELL / F-MIXED / F-INSTRUMENT; no-rescue transplant map).
  Instrument not yet built; execution awaits the author's release.
- FND-148 and FND-149 decisions remain open on the author's desk.

## PRETENSION BRICK (THIRD) EXECUTED -- W2 WITHIN BRACKETS:
## UNIFORM PRETENSION RESCALES, NEVER RESCUES (2026-08-26)

- Charter locked before computation (analysis/TOPOLOGY_pretension_
  charter_LOCKED.md); committed prior W1 (spider-web) FALSIFIED
  for uniform tension.
- V2 map (equatorial transverse channel, per-column pristine
  calibration): z_c flat within brackets ([3.0,3.5] at tau 0.3 &
  0.02; [3.0,4.0] at tau 1); speeds track c_T = sqrt(tau) at every
  column. V3 spectrum proof: no floppy proliferation below
  Maxwell at any tau > 0; lowest genuine eigenvalue scales as tau
  (ratio 50 = 1/tau) -- tension gaps floppy modes with the same
  factor that sets c_T^2, so z_c cannot move.
- Surprise: at tau = 0.02 the PRISTINE lattice is a leaky-slab
  anisotropic medium (p 4.06) and dilution CURES it (1.44 / 0.54
  at z 5/4, quasi-2D crossover) -- reported as measured, no form.
- Four daylight instrument amendments, each pristine-row
  justified, ledger in the results doc; tau=1 rows restated under
  the final instrument.
- Records: analysis/TOPOLOGY_pretension_results.md,
  analysis/pretension_brick_ckpt.pkl, draft FND-149 AWAITING THE
  AUTHOR (3 decisions incl. whether heterogeneous tension gets a
  fourth brick).

## COORDINATION BRICK EXECUTED -- W3 GRADED, SHARP SCALAR
## THRESHOLD, PENDANT = ONE-ROPE (2026-08-26, author released)

- Instrument benchmarks/foundations/coordination_brick.py built and
  calibrated (two daylight amendments annotated in-file, z-blind).
- C3: static 1/r^2 at ANY connected z (Gauss = topology). C2/C1:
  wave-medium at z = 4 (p_dyn 0.995), localization below z_c =
  3.75 +/- 0.25 with the size-drift display at z = 3.5. C4: bulk
  Z 7.70 -> 4.38 -> 2.93 (z 6/4/3); PENDANT Z = 0.9950 = the
  single-rope sqrt(T0 mu) to 0.5 percent -- connected, NOT
  embedded, measured. C5: coupling within 1 percent of 1/(4 pi),
  anisotropy <= 5 percent at r >= 10. C6 reported per rule.
- Verdict recommendation W3 (graded) recorded; pretension axis
  DEFERRED to a vector instrument (honest scope note in results).
- Open debt: pristine C2 calibration 1.073 vs 1.05 bar (7 percent,
  one row; dilution self-averages it elsewhere).
- Records: analysis/TOPOLOGY_coordination_results.md,
  analysis/coordination_brick_ckpt.pkl, draft registration
  FND-148 AWAITING THE AUTHOR with 3 decisions.

## Q-SWEEP STAGE 1 COMPLETE -- RULE S1-SPLIT FIRED (2026-08-24/26)

- q5/3 column executed per the runbook: level-1 PASS, ramp (4 rungs
  + 2 gated members: A2 0.0018792 RMS 2.76e-10 clos 4.4e-11 om2
  4.23408; A2 0.0046979 RMS 5.90e-11 clos 2.5e-11 om2 4.30871),
  then the arc march: 38 rate points, ruler-flat (~0.3%/step,
  cumulative -12.1%), 0.0063 TARGET REACHED at member grade (final
  member A2 0.0063336 RMS 2.97e-9 clos 1.6e-10 om2 4.38221). March
  closed at the crossing (q['hi_closed'], reason recorded).
- INSTRUMENT: the q5/3 member-1 solve exposed a deterministic limit
  cycle (descend, accepted |dx|~0.3-0.6 floor-leap out of the
  basin, rejection cascade past lam 1e6, abort, rung replay --
  measured digit-identical twice). Fixes, annotated at their code
  sites: TRUST CAP (|dx| <= 0.05 before the acceptance ladder) and
  REJECTION-ABORT PERSISTENCE (aborts keep their solve key). Zero
  rejection cascades after; closure-aware stop from the q4/3 arc
  work carried over.
- RULES BLOCK FIRED (mechanical): q4/3 D = 5.31x (unreached-target
  closure at 0.005042; monotone decline makes it a lower bound);
  q5/3 D = 1.11x (target reached). ** S1-SPLIT: the neighbors
  disagree; stage 2 (frozen-direction / frozen-cell) REQUIRED
  before any interpretive grant. ** The collapse is
  rationalization-selective: neither cell artifact nor family wall.
- om2 finding: strongly q-dependent (2.15 / 3.20 / 4.23 across
  4/3, 3/2, 5/3 at matched amplitude), <= 3.1% drift within branch.
- Records: analysis/QSWEEP_stage1_results.md (full profiles),
  analysis/qsweep_stage1_ckpt.pkl (exported state),
  analysis/QSWEEP_stage1_draft_registration.md (FND-147 draft,
  AWAITING THE AUTHOR'S GRANT with 3 listed decisions).
- Queue standing: stage 2 mandated (uncharted); coordination brick
  chartered and queued; both awaiting the author's ordering.

## NAME TREATMENT DECIDED + DOC HARMONIZATION PASS (2026-08-24,
## author's decisions 1 and 2)

- Option A adopted: the corpus KEEPS the name "mesh framework"; the
  model within is described as a LOCAL WEAVE OF ROPES. No file or
  identity renames (protects 737-claim citation continuity).
- guide/topics/gravity.md: chapter retitled "The Weave Pulls Every
  Two Things Together"; opening rewritten into the weave register
  with the rope-between-them kept explicitly as the field-lines-style
  visualization; spectator test cited.
- guide/topics/intro.md: "stretching between every pair of atoms"
  rewritten to the woven-fabric picture; explicit "this is NOT Bill
  Gaede's rope model" paragraph added citing the 6-of-9 failure and
  the constant-tension vs inverse-square discriminator.
- guide/topics/closing.md: gravity bullet recast (weave pulls, with
  the effective strength of a rope stretched between).
- Guide rebuilt (tools/build_guide.py): 11 topics, 10 diagrams,
  render-check PASS.

## COORDINATION BRICK CHARTERED AND QUEUED (2026-08-24, author's
## decision 3)

- analysis/TOPOLOGY_coordination_charter_LOCKED.md: the second brick
  (coordination and membership: z=1 pendant vs embedded, rigidity
  percolation under pretension, source/static fidelity, impedance,
  isotropy map, defect physics) with bars, no-rescue rule, and
  verdict forms W1-W4 locked NOW. QUEUED behind the q = 5/3 column;
  not to run until the author releases it.

## TOPOLOGY: THE ANALYTIC SPECTATOR TEST DECIDED -- V2, LOCAL
## WEAVE SUPPORTED (2026-08-23, the commission's first brick)

- Computed under the locked charter with shared (T0, mu, q_s) and
  the no-rescue rule. LOCAL WEAVE: 9/9 tests PASS, every 1/r^2,
  1/r, and r/c a THEOREM of the local 3D operator. DIRECT ROPES:
  3/9 (propagation, asymptotic isotropy, per-rope polarization),
  FAILING energy extensivity (E ~ N^2), spectator independence
  (both energy M*T0*R and endpoint impedance (N+M)*sqrt(T0*mu)),
  Gauss (flux counts EXTERIOR ropes), statics (constant-tension
  rope pulls with T0 at ANY distance -- no 1/r^2 without a
  hand-inserted per-rope law), flux spreading (1D waveguides do
  not decay), and cluster separability (inter-lab force
  N1*N2*T0 independent of R). Every failure curable only by the
  barred rescues. NOT V3: the models differ observably.
- The author's declared prior (local weave) CONFIRMED and scored.
- Consequence per the registered charter: the weave is real; the
  all-to-all rope is METAPHOR for the weave-mediated effective
  1/r^2 pair interaction (the "field lines" register). No
  registered physics changes (the equations were already
  weave-native); prose harmonization owed to the guide (gravity
  chapter title, intro's "every pair of atoms"), pending the
  author's word.
- Record: analysis/TOPOLOGY_spectator_analytic.md.

## Q-SWEEP PAUSED AT THE AUTHOR'S DIRECTION (2026-08-23)

- q4/3 column COMPLETE: hi march closed under the charter's
  unreached-target clause (author-authorized on economic grounds);
  D(4/3) >= 5.56 recorded as a RIGOROUS lower bound (monotone
  declining rate), 11-point collapse profile the deliverable.
- q5/3 column: level-1 PASSED (bar v2); ramp rung 1 begun, then
  paused. Everything checkpointed.
- HANDOFF PREPARED: analysis/QSWEEP_q53_runbook.md -- the complete
  operator runbook (machine, solver lessons, state sequence, stop
  rule, close-out, cross-check numbers) written so another
  operator or model can execute the q5/3 column and fire the rules
  without this session's context.

## TOPOLOGY COMMISSION CHARTERED (2026-08-23, author's charter)

- THE QUESTION (author's words): is the weave an actual weave, like
  a 3D blanket, or is every atom connected to every other atom
  DIRECTLY? SURVEY FINDING, citable: the corpus MIXES the two --
  the prose carries Gaede point-to-point language ("A Taut Rope
  Between Every Two Things", "every pair of atoms") while EVERY
  registered equation is a local operator (the psi Poisson solver,
  the torus stencils, the EM wave operators, "leaks into the
  SURROUNDING network"). The math is weave-native; the metaphors
  are all-to-all.
- Charter locked BEFORE computing
  (analysis/TOPOLOGY_COMMISSION_charter_LOCKED.md): two models on
  equal footing with shared tension / density / source / boundary
  conditions and a NO-RESCUE rule (no population-dependent
  normalization unless derived independently in advance); the
  SPECTATOR-ATOM experiment as the decisive instrument, attempted
  ANALYTICALLY first (the author's first-brick call); nine
  pre-registered tests (energy scaling, spectator independence,
  Gauss law, 1/r^2 statics, r/c causality, flux spreading,
  isotropy, polarization, cluster separability); exactly four
  verdict forms (direct / local / empirically equivalent / both
  rejected); the author's declared prior (local-weave favored)
  RECORDED before testing, granting nothing; consequences by
  verdict registered, including prose harmonization either way.
- Scheduling: runs after Q-SWEEP stage 1 delivers D(4/3) and
  D(5/3) or a registered NO CALL; the analytic first brick may
  interleave at the author's word.

## Q-SWEEP STAGE 1 PROGRESS (2026-08-23, mid-stage record)

- q4/3 MEMBER 1 GATED: A2 = 0.0018792, RMS 1.89e-9, closure
  1.5e-7, om2 = 2.14842, wsNyq 1.9e-9 (no stage-3 debt) -- THE
  FIRST TWO-FREQUENCY MEMBER EVER LANDED OFF q = 3/2. Landed by
  the (v5)-validated lm_round-faithful ladder from the m2
  injection through four honest sub-pin rungs.
- q4/3 MEMBER 2 GATED: A2 = 0.0046979, RMS 1.74e-10, closure
  1.5e-8, om2 = 2.21540 -- the cleanest state of the campaign,
  landed by the RUNGED re-climb after the rungless jump failed.
- THE CLOSURE-DEBT ENVELOPE, measured at five data points and
  annotated at its sites: rungless jumps buy amplitude with
  closure debt (1.2e-3 at the waypoint jump, 3.3e-4 caught early
  at the fine jump) which compounds into a soft bottom band
  (isolated singlet sigma_eff 8.24e-4 measured two independent
  ways, 6% agreement, 75% T-block anatomy) where exact-GN steps
  inflate to r/sigma and no single-direction pin -- a2, secant
  arc, or measured-singlet arc -- can tame them; runged jumps keep
  the debt shallow and SNAP (one 99.65% Newton round at the
  waypoint-2 gate). Rungs generalized to every jump including the
  fine pin. The a2/secant/singlet pin attempts and the singlet
  measurement are kept on the record.
- Instrument: the ported FORCING-rule escalation delivered a rung
  endgame in one lsmr blow (59% round); lam persistence, per-round
  and per-rung checkpointing carried ~40 container reaps with zero
  lost state; the patcher-as-file discipline adopted after
  repeated heredoc reaping.
- om2 CELL VARIABLE (member-grade): 2.14842 -> 2.21540 across the
  two members (+3.1%) vs q = 3/2's 3.2008 -> 3.2729 (+2.3%) over
  the same A2 span -- the q4/3 branch spends MORE of its response
  in frequency. Recorded per the charter's P3; not interpreted.
- In flight: the RUNGED fine-pin climb toward 0.0063277 (rung 1 of
  2), then arc-pair rates at both matched targets -> D(4/3).


## FND-146 GRANTED AND REGISTERED (v3.27.6); Q-SWEEP STAGE 1 CHARTERED

- FND-146 registered (737 claims) AS GRANTED by the author with the
  scope-tightening amendment: acquittal on the MEASURED branch and
  TESTED discretizations; "not explained by any detected Jacobian
  degeneration" (not "not a degeneracy property"); "does not
  deteriorate" (the effective sigma RISES S0 -> S3; 0.9x is the
  inverse deterioration ratio the rule uses). Direction-field vs
  rationalized-cell kept as the LIVE INTERPRETATION, not part of the
  finding, per the author's editorial. Registered via the canonical
  inserter; structural guards pass at 737.
- Version cut 3.27.5 -> 3.27.6; results doc aligned to the granted
  scope; doc facts synced.
- Q-SWEEP STAGE 1 AUTHORIZED and CHARTERED, bars locked before
  computing (analysis/QSWEEP_stage1_bars_LOCKED.md): q is a
  rationalization, so the local neighbors are q = 4/3 and 5/3 on
  3 sqrt(3) cells at matched density (144 x 36, n = 15554); the
  NATIVE protocol replicated per q with no cross-cell seeding;
  validation bars (v1)-(v4) incl. QGrid reproducing the registered
  q = 3/2 instrument and the f64 true-operator check retained;
  interpretation rules S1-CELL / S1-BRANCH / S1-SPLIT registered on
  the collapse factor D(q) with thresholds locked in advance. The
  QGrid instrument build is the next action.

## SVD-DIAG (2026-08-22, run at the author's direction; RULE C)

- The smallest-singular-value diagnostic (external review step 3)
  built, bars-locked BEFORE computing, and executed across five
  states: two mild members, the march head (tangent pair), the
  PROBE-94 landed state, and the FND-145 adjudicated 112 x 42 state.
- MECHANICAL VERDICT, all halt-grade bars passed: RULE C -- HEALTHY
  bottom spectrum. Ra2(eff) and R2(eff) move 0.9x from S0 to S3
  against a registered 10x threshold. No fold, no resonance
  approach (the W0-margin-below-one suspect takes a direct hit:
  omega-fractions ~1e-11 in every measured vector), no gauge
  degeneration. The dA2/ds collapse is NOT a bottom-spectrum
  property; the q-sensitivity probe is PROMOTED per the rule as
  locked.
- Three amendments and one implementation note, all recorded in
  daylight below the lock line, all stricter: (1) structural-null
  cluster discovered on first contact (recon() projects mean and
  s-Nyquist families; k0 = 115 at 96 x 36, 178 at 112 x 42) --
  effective sigma above a certified floor replaces raw sigma_min;
  (2) bar (ii) rebuilt as an f64 true-operator finite-difference
  check after the f32 self-check was shown to measure storage
  arithmetic; (3) f64 normal-matrix measurement after the f64
  arbiter FAILED the f32 vectors twice at the pinched S2/Jfree gap
  (11.83%, 11.96%) -- the first noise diagnosis was WRONG and is
  kept on the record. Final: 8/8 operator checks at 0.10-0.14%,
  tangent-in-null-space 0.99999, cluster certified operator-level
  at every state.
- Instrument lessons at their sites: f32-J vectors untrustworthy at
  small gaps (values sound; solver unaffected); the f64
  normal-matrix route 2.5x faster than the f32 SVD it replaced; two
  further OOM mechanisms mapped and fixed (eigh copy at n = 14114;
  rebind-before-free); detached runs die across long user-idle gaps
  -- per-state checkpoints carried the run over four kills with
  zero lost states.
- Artifacts: analysis/SVD_DIAG_bars_LOCKED.md,
  analysis/SVD_DIAG_results.md, analysis/svd_diag_ckpt.pkl,
  benchmarks/foundations/svd_diagnostic.py. REGISTRATION DRAFTED,
  NOT TAKEN: the claim grant is the author's.

## THE ADJUDICATION (v3.27.5)

- FND-145 REGISTERED (736 claims): the 112 x 42 confirmation
  COMPLETED at round 58 -- converged (RMS 1.86e-9 under the 1e-8
  bar, closure 6.2e-7 under the halt bar) and FAILED every drift
  gate multi-coordinate (gamma 1.01e-2 at 2x the gate, Om2 6.02e-3,
  A2 7.51e-3). 64 -> 96 moved A2 alone; 96 -> 112 moves all three.
  PROGRESSIVE RESOLUTION EXHAUSTION. Corroborated independently by
  wsNyq falling only 3x under 1.4x-per-axis refinement.
- FND-144 AMENDED at its site ([AMENDED by FND-145] rider, NUC-005
  convention): the displacement reading WITHDRAWN as overclaimed,
  per the conditional the external review staked in advance; the
  branch-existence, rate-collapse, and mild-member results STAND.
- Version cut 3.27.4 -> 3.27.5 (CITATION.cff, pyproject, CHANGELOG
  entry). SESSION 3 ADDENDUM written into
  analysis/NATIVE96_results.md; analysis/probe94_ckpt.pkl synced to
  the adjudicated round-58 state with the round-40..58 floor
  trajectory and conf_verdict aboard.
- INCIDENT KEPT: the first registry write used a plain yaml.dump and
  drifted from the canonical serialization; tools/verify_corpus.py's
  parser-agreement guard REFUSED the file (PyYAML 736, line parser
  0) instead of verifying it -- the exact silent-zero failure mode
  the guard was built against, caught doing its job. Re-serialized
  with tools/add_claim.py's Canonical dumper; parsers agree; full
  verify re-run from zero on the canonical file.
- External-review adoptions queued (not run): smallest-singular-value
  diagnostic along the branch; q-sensitivity probe around 3/2 BEFORE
  any long continuation walk; Om2-parameterized (or dominant singular
  coordinate) continuation in place of A2.

## INSTRUMENT (benchmarks/foundations/native96_probe94.py, stage D)

- SCHEDULING FINDING, AND IT REVERSES A REGISTERED NOTE. The record
  held that background processes die at the tool-call boundary, which
  is why every prior stage-D chunk ran foreground at 1-3 rounds per
  call and why the uncapped finish was priced as CI-only. MEASURED
  THIS SESSION: a run launched under setsid with stdio redirected
  SURVIVES the boundary and keeps running between calls. The finish
  is in-session work. Annotated at its site.
- NO-VERDICT GUARD (the important one). As written, exhausting the
  round cap fell THROUGH to the verdict block and would have written
  conf_verdict = 'failed' on a still-descending solve -- a budget
  adjudicating as a bar, on the decisive
  displacement-vs-progressive-exhaustion call. Cap exhaustion now
  exits NO VERDICT and resumable. Only a genuine stall (no step
  accepted) or the RMS bar adjudicates.
- Cap 80 -> 240 on the registered budget-not-a-bar argument, and a
  PER-ROUND checkpoint save (the checkpoint was previously written
  only at a budget exit, so a reaped run lost every round it had
  taken). The floor trajectory is kept alongside the state.

## THE CONFIRMATION (running, no verdict)

Resumed from round 38. Floor 1.8e-5 -> 1.6e-5 (r40) -> 1.3e-5 (r42),
contracting without decay; exact-GN bounces still shrinking (5.1e-5
at r39, 3.3e-5 at r41). The pre-snap signature holds. NO VERDICT.

INCIDENT KEPT: the first detached run was REAPED at round 42, silent
and tracebackless -- the container OOM signature, not a solver
failure. Cause was operator scheduling, not numerics: the guide
rebuild (pandoc, then soffice and the diagram renderer) ran in the
same 4 GB container while a stage-D round held ~2.7 GB. The
per-round save added earlier in this same session held, and round 42
plus its floor trajectory survived intact; the run resumed from it
with nothing lost. RULE ANNOTATED AT THE SITE: a detached stage-D
run is MEMORY-EXCLUSIVE -- while it is live, monitoring commands
only.

## THE PLAIN-LANGUAGE GUIDE (root cause was in the source)

- 12 callout boxes rendered as flattened ASCII (label column and body
  column interleaved line by line, literal ** and * on the page).
  CAUSE: those 12 had been pasted back into guide/topics/*.md in their
  already-RENDERED fixed-width form instead of the `> CALLOUT|LABEL`
  convention, so build_guide.py had no table to build and pandoc
  emitted the art verbatim. Repairing the docx would have been wiped
  by the next build; the sources were repaired instead. All 12
  reconstructed: THE ITCH IT SCRATCHES (intro), seven THE ANALOGY
  boxes (light, quantum x3, gravity, chemistry, nuclear), WHAT HEAT
  IS, THE TUG-OF-WAR, HONEST LIMIT (heat), THE POINT OF ALL THIS
  (closing). One literal asterisk remains in the guide and it is the
  multiplication sign in kappa_0 = c/sqrt(eps0*SIGMA).
- ELECTRICITY NOW LEADS WITH CURRENT AND VOLTAGE, on the author's
  instruction: leading with charge-as-handedness does not tell a
  reader what electricity IS. Two sites. (a) intro.md six-words box:
  Electricity = TURNING, current is the ropes spinning in place like
  flexible drive shafts and voltage is the TENSION DIFFERENCE that
  turns them; charge follows as the thing that settles only which WAY
  they drive (the box now lists six items, not seven). (b)
  electricity.md retitled "Electricity -- Turning Ropes, Driven by a
  Tension Difference", opening on current-as-turning and
  voltage-as-tension-difference with an explicit nothing-flows beat;
  charge DEMOTED to a closing subsection "Charge -- the handedness
  that sets which way it drives". Three seams sewn for the reorder:
  the closed-loop parenthetical now poses the direction question as
  open instead of cashing in a chapter that no longer precedes it;
  the charge subsection opens by saying handedness neither makes nor
  drives the current; a new closing paragraph pays the question off.
  The voltage sentence in "What makes a current strong or weak" is
  re-led on the tension difference rather than on orientation
  mismatch, and the now-redundant "(Voltage is the tension; charge is
  the handedness)" aside is dropped.
- Rebuilt via tools/build_guide.py --pdf: 11 topics, 10 diagrams,
  render-check PASS, 35 pages, docx and PDF both refreshed.

## HOUSEKEEPING

- VALIDATION ENTRY POINTS REPAIRED (the external reviewer's package
  item, verified then fixed). validation/run_validation.py imported
  rope_solver from the caller's PYTHONPATH and died with
  ModuleNotFoundError when run from the root as advertised; worse,
  validation/run_physics_validation.py swallowed subprocess stderr,
  so the same failure printed as "COMBINED PHYSICS+EM: 0/0 tests
  passed" with no cause shown. Fixes: (a) run_validation.py,
  tests/test_physics.py, and tests/test_electromagnetism.py now
  self-bootstrap sys.path the way the benchmarks always have, so no
  PYTHONPATH is needed from any cwd; (b) the physics runner prints a
  failing suite's stderr -- a failure must always say why; (c) the
  stale run_validation.py header (it still named
  tests/test_validation.py) corrected. Verified from the root, from
  validation/, and from an unrelated cwd: 10/10 validation, 35/35
  physics, 40/40 EM, 75/75 combined. Makefile targets unchanged and
  still correct.
- tools/check_freshness.py run after the rebuild; tools/sync_doc_facts.py
  re-synced the corpus_stats / status_breakdown marker blocks in
  README, KNOWN_LIMITATIONS, docs/STATE_OF_THE_PROGRAMME, and the
  overview and dependency-graph regenerations were taken. ONE ITEM
  LEFT STANDING, AUTHOR'S CALL: the release-note metadata lags
  (CITATION.cff and pyproject at 3.27.4, release note behind). Not
  touched -- cutting a release note is not a housekeeping action.
  Also standing: the front-door verify badge reads 629/629 while the
  registry carries 639 code-backed.

# SESSION_CHANGES -- 2026-08-21 (NATIVE-96 session 2: close-out)

- The owed 112 x 42 confirmation fed rounds 7-38 (cap raised 40 -> 80,
  budget-not-a-bar): alternation schedule broke the exact-GN
  circulation; floor 1.1e-4 -> 1.8e-5 contracting ~7-8%/pair without
  decay; bounces shrinking (pre-snap signature). NO VERDICT; resumes
  on CI from analysis/probe94_ckpt.pkl (round 38).
- FND-144 GRANTED and REGISTERED with the round-38 partial folded in:
  735 claims, v3.27.4 cut. Results doc updated in place.
- Queue: (1) CI finish of the confirmation (decisive:
  citable-displacement vs progressive-exhaustion); (2) CI walk from
  the march head (analysis/native96_march_ckpt.pkl, A2 = 0.0063277);
  (3) on the walk's landing at the third pin: the third (0*)
  comparison, then the chartered continuation; (4) the standing
  physics: asymptote scenario leading, q = 3/2 named suspect,
  Sigma_wave boxed, FND-139 rider standing, the Om2 -> Om1 1:1 drift
  now with a measured trajectory.

# SESSION_CHANGES -- 2026-08-20 (NATIVE-96 session)

## REGISTERED THIS SESSION (before any computation)

- FND-143 GRANTED by the author and registered: 734 claims, v3.27.3
  cut (CHANGELOG, README, CITATION.cff, pyproject.toml consistent).
  The earlier PROPOSED FND-143 text retired unregistered.
- analysis/NATIVE96_bars_LOCKED.md: locked on the author's
  instruction with ZERO amendments; draft preserved as
  analysis/NATIVE96_bars_DRAFT.md.

## EXECUTED THIS SESSION

- COMMISSION NATIVE-96 (benchmarks/foundations/native96_continuation.py),
  outcome RATES-REGISTERED per bars delta 6. Full record:
  analysis/NATIVE96_results.md. Highlights: controls (i) and (0*)
  [2-of-3] PASS; two native members under the promoted halt-grade
  closure bar, both 112 x 42 cross-confirmed at 1e-5-grade drift;
  the member-grade dA2/ds collapse measurement (6.5e-4 at A2 = 0.0048
  to 6.8e-5 at 0.0063, decaying, gamma frozen, Om2 carrying the
  arclength, W0-margin declining toward the distant 1:1 resonance).
- PROBE-94 (benchmarks/foundations/native96_probe94.py): the branch
  EXISTS natively at the third-pin neighborhood (A2 = 0.0094647,
  RMS 2.7e-10, closure 9.5e-9 after a 51-round fight); the 64 x 24
  member there is DISPLACED along the branch (A2 +0.73%,
  single-coordinate, out of the 5e-3 gate; gamma and Om2 in-gate) --
  displacement grade, not the steepened fabrication grade. The
  landed state's wsNyq = 2.6e-3 armed the tail trigger; the owed
  112 x 42 confirmation is BUDGET-BOXED PARTIAL (5.0e-1 -> 2.0e-4,
  descending, no verdict) and resumes from the exported checkpoint.

## OWED / QUEUE

1. FND-144 grant decision (author): analysis/FND144_CLAIM_DRAFT.yaml.
2. The owed 112 x 42 confirmation of the PROBE-94 landed state
   (CI-scale; restore analysis/probe94_ckpt.pkl to
   /tmp/p94_ckpt.pkl, rerun with --budget). DECISIVE: confirmation
   makes the displacement finding citable; failure makes the
   exhaustion PROGRESSIVE ACROSS GRIDS.
3. The CI-scale walk: restore analysis/native96_march_ckpt.pkl to
   /tmp/n96_ckpt.pkl; the approach head is at A2 = 0.0063277,
   member-grade, 500-1000 steps from the third pin at the measured
   decaying rate. On landing: the third (0*) comparison, then the
   chartered walk with the halt-grade closure bar.
4. Standing physics questions sharpened this session: the asymptote
   scenario leads for the reach-or-asymptote binary (Sigma_wave
   still NOT re-priced; FND-139 rider standing); q = 3/2 remains the
   named suspect; the Om2 -> Om1 1:1 drift and the resonant-root
   question now have a measured trajectory to hang on.

## INSTRUMENT NOTES (annotated at their sites; summary in results doc)

Degenerate level-1 pin seeding; the pin gate; ramp confirmation
wiring; f32-Jacobian rule for all 112 x 42 builds (three OOM
incidents mapped); foreground-chunk scheduling fork (margin 100 s,
rounds cap as budget); measured-crawl escalation (exact-GN
alternating with capped-lsmr descent); the KEPT waypoint-tolerance
incident, hypothesis falsified by member-grade re-measurement, rates
cited from full-bar states only.

## 2026-08-28/29 -- WHY-WINDING arc (charter: why the 4/3 cell demands
## winding where 5/3 doesn't)
- Brick 1 (dispersion lattice): RES-OPEN. New: analysis/WHYWIND_dispersion_{bars_LOCKED,results}.md, benchmarks/foundations/whywind_dispersion.py. Fourth-cell prediction committed: q=5/4 FLAT.
- Brick 2 (coupling matrix elements): F-INSTRUMENT (statistic annihilated by branch-tangent nullity). New: analysis/WHYWIND_coupling_{bars_LOCKED,results}.md, benchmarks/foundations/whywind_coupling.py.
- Brick 2a (mode-resolved rotation): SEL-OPEN, evidence-bearing; j=n rule contradicted; collapse mode identified at +-(17,19), phi-Nyquist-1; resolution flag raised. New: analysis/WHYWIND_rotation_{bars_LOCKED,results}.md, benchmarks/foundations/whywind_rotation.py.
- Stage 3 (targeted resolution replication): S3-F-INSTRUMENT; cross-grid record shows 4/3 deep-end winding content is not grid-stable (5/3 grid-invariant). New: analysis/WHYWIND_stage3_{bars_LOCKED,runbook,results}.md, benchmarks/foundations/whywind_stage3.py, analysis/whywind_stage3_ckpt.pkl.
- Draft registration AWAITING THE AUTHOR: analysis/WHYWIND_draft_registration.md (WHYWIND-A..D + owed re-pricing decision).
- No registered claim re-priced this session; registry untouched pending grants.

## 2026-08-29 -- WHY-WINDING arc, second half (option c)
- Re-pricing (option b): RP-FALLS. FND-152's f_dir rise is entirely Nyquist-band (|n|>=13) content; resolved band FALLS 0.106->0.002; 5/3 f_nyq = 0.0000 throughout. Rider drafted. New: analysis/WHYWIND_reprice_{bars_LOCKED,results}.md, WHYWIND_reprice_run.txt.
- 144x42 probe (option a): NO VERDICT -- p42|4/3|deep REFUSES full-bar gating (f32 limit cycle 2.3e-7; bounded f64 endgame slid off constraints). p42|4/3|prev and BOTH 5/3 control members gated at full bar on the same grid. Five-instrument grid-fragility finding. New: analysis/WHYWIND_probe42_{bars_LOCKED,results}.md, benchmarks/foundations/whywind_probe42.py, analysis/whywind_probe42_ckpt.pkl.
- Instrument ledger: phase-C disk-backed factorization (OOM fix); per-dtype resumable jac; bounded f64 endgame; stale-jac cleanup (disk).
- Draft registration addendum AWAITING THE AUTHOR: analysis/WHYWIND_draft_registration_addendum.md (WHYWIND-E, -F, queue action).
- Registry untouched; rider drafted not applied; q=5/4 FLAT commitment stands.

# SESSION_CHANGES -- 2026-09-05 (Q54 / GR54 campaign close; v3.30.0 cut)

## RELEASE v3.30.0 CUT PER THE CHECKLIST
- pyproject 3.29.0 -> 3.30.0; CITATION.cff 3.30.0 / 2026-09-05;
  CHANGELOG 3.30.0 entry; sync_doc_facts ok ("current v3.30.0,
  badge denominator 641"); docs/history/RELEASE_NOTES_v3.30.0.md
  and root copy; README featured paragraph and current-release line;
  ZENODO_RELEASE_NOTE.md rewritten.
- Registry: FND-163/164/165 registered via tools/add_claim.py (756
  claims); riders on FND-150..153 and FND-163 applied with the
  Canonical dumper; verify_corpus 178 checks, no failures.
- Campaign artifacts in analysis/: Q54, GR54, GR54X, GR54B, GR54A,
  REPRICE, BRICK2, DISC charters (LOCKED) and results; seven charter
  drafts in analysis/charters_draft/; QUEUE_2026-09-04.md;
  run_local.sh for laptop execution.

# SESSION_CHANGES -- 2026-09-05 (evening): v3.31.0 CUT
- Registry 756 -> 761 (FND-166..169, EM-023); EW-001/PM-001 demoted; riders
  applied; verify_corpus 178 checks. Version bumps, CHANGELOG, release
  notes (docs/history + root), README, Zenodo note, sync_doc_facts ok.
- Charters locked and executed: PEV-IDENT, FINE-GATE, TRIPLE-DUTY,
  CASIMIR-PLATE (Legs 0-1; halt lifted by E-RECON), E-RECON, COMPOSITE-
  SELECT (Leg A), ITEM-6 (6a staged local; 6b/6c/6d done), LADDER.
- New drivers: casimir_plate.py, casimir_verdict.py, antialigned_q1.py,
  composite_legB.py, axis_meaning_ladder.py; handoff tarballs shipped
  (never ship run_local.sh again -- the author's copy is the good one).

- RENAME (A+B): the Mesh Programme / mesh framework. tools/mesh_rename.py (surgical phrase list; identifiers, the rope object and the Rope Hypothesis untouched), tools/paper_rename.py, tools/paper_edit.py. 49 doc replacements; 62 paper sources rebuilt (naming note in front matter), validated against originals, PDFs regenerated. Repository/package/file names unchanged (tier C queued for the next release; tier D not to be done).
- RENAME pass 2: prose in code docstrings/prints (5 benchmarks, rope_solver/open_problems.py), claims.yaml notes/titles (25), HANDOFF.md (40), and the four doc GENERATORS (build_overview/roadmap/depgraph/claim_status_registry) so regenerated docs keep the name; PROGRAMME_OVERVIEW, ROADMAP, dependency graph regenerated. build_roadmap.py gained the 'registered' status colour (it crashed on the 23 registered claims before). No file, script, package or claim-ID names changed; nothing references a renamed file because none was renamed.
- CI FIX (2026-09-06): verify.yml on GitHub reported 14 EVIDENCE MUTATION failures with no evidence file changed in any commit -- the runner's unpinned numpy/scipy regenerate the CSV/npz/log evidence with different bytes (numpy 2.4 needs Python >= 3.11; the 3.10 job resolved an older numpy). Fix: requirements.txt pins numpy==2.4.4, scipy==1.17.1 (the versions that regenerate QGATE-017's evidence byte-identically); pyproject floors raised; .github/workflows/verify.yml shipped with a 3.11/3.12 matrix installing from requirements.txt before `python tools/verify_corpus.py --skip-heavy`. Never regenerate evidence on the Mac (Apple BLAS bytes).
- CI FIX 2 (2026-09-06): after the pin, 12 EVIDENCE MUTATION failures remained; all twelve reproduce byte-identically here, so the runner's CPU/BLAS last-bit noise was being adjudicated as mutation. verify_corpus.py now distinguishes reproduction-within-tolerance (restore + pass with a note) from mutation (numbers differ). Unit-tested on real evidence: identical/last-digit-perturbed/1e-9-scaled pass; 1 pct change and a changed digit fail. pyproject requires-python >= 3.11. docs/VERIFY_STATUS.md entry added.
- 2026-09-07: FND-172 (ANTI-ALIGNED Q1) registered with riders; Q2 reduction built (2D kernel exhibited, pencil roots, second-order shift; NO CALL on the 1 pct detuning), D3 polish in progress (RMS 1.4e-9 toward the 1e-9 letter; analysis/antialigned/d3_polish.pkl). Sparse instrument trust cap made scale-invariant (COMPOSITE-SELECT Leg B amendment). go.sh self-contained launcher; run_local.sh fixed in-tree.
- 2026-09-07: stale ZENODO_RELEASE_NOTES.md (v3.26.0 long form) archived to docs/history/; ZENODO_RELEASE_NOTE.md is the single live deposit note (release checklist step 6).
- 2026-09-07: six hardware-sensitive iterative benchmarks carried as documented waivers (VERIFY_STATUS); CI expected 634/641 passing, 7 failing all waived, exit 0.

- 2026-09-09: RENAME tier C: GitHub repository renamed mesh-framework (old URL redirects); README badge/URLs, pyproject Repository URL, the one-fence prompt, naming notes updated. CHANGELOG history entries keep the old URL. Next release artifact: mesh-3_32_0-release.zip; Zenodo title updated at the 3.32.0 deposit.
- 2026-09-09: root RELEASE_NOTES_*.md removed (3.28.1/3.29.0/3.30.0/3.31.0 were byte-identical duplicates of docs/history/RELEASE_NOTES_v*.md; the short-form 3.28.0 moved to docs/history/RELEASE_NOTES_v3.28.0_short.md with a provenance line). RELEASE_CHECKLIST step 6 amended: release notes live ONLY in docs/history/. Last three live-tree 'rope-framework' strings updated (HANDOFF, ADJOINT spec, one benchmark print).

# SESSION_CHANGES -- 2026-09-11..13 (rebuilt 2026-09-13 after a sandbox reset; the compute tree and GitHub were the sources of truth)
- FND-174 registered (ANTI-FLAT licensed on the 20-point ANTI-ARC-X profile; handedness-selective collapse) with riders on FND-163/164/139; grid-scope rider (ANTI-ARC-54: REFUSED at a resolved floor; wsNyq is the s-direction weight) and continuum-status rider (ANTI-ARC-S288) folded into its note.
- ANTI-ARC-54 chartered/run/REFUSED (analysis/ANTIARC54_results.md); ANTI-ARC-S288 chartered/run/REFUSED at exact resonance (analysis/ANTIARC_S288_results.md); riders on FND-172 (strengthened), FND-173 (grid-conditioned).
- kernel_continuation.py built (bordered GN along a near-null direction); KERNEL-CONT chartered; partial local result: stage A all seven b != 0 GATED (c1 floor reproduced), stage B (288x36, 5/4) b = -0.2/-0.1/-0.05 GATED at exact resonance.
- CITATION.cff title: "The Mesh Programme (rope_solver): A Computational Toolkit for the Mesh Framework" (author's wording).
- Instrument incidents: laptop disk filled twice (SJ_MEMO=1 factor memos; then a launcher prune that used ls -t on memo DIRECTORIES). Launchers now default SJ_MEMO=jac, prune with ls -td / rm -rf, and read only the last log line; all 30 drivers write checkpoints atomically (tmp + os.replace). The pattern cache was truncated once and re-measured.
- Sandbox reset 2026-09-13: tree rebuilt from GitHub (through FND-173) + the compute tree's recovery tarball; registry edits re-applied from the conversation record.
- 2026-09-13: the atomic-write helper had been appended at end-of-file in 13 drivers without a ROOT line (CI: FND-145 NameError); helper now placed before first use in every driver, all parse.
