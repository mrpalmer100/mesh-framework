# COMMISSION ANTI-ARC-NYQ -- DOES THE ANTI-ALIGNED FAMILY MARCH FLAT ON CLEAN STATES?
# (CHARTER, LOCKED 2026-10-04 on the author's word, before any arc point)

North Star line (docs/NORTH_STAR.md section 5): retires an input. FND-174 (ANTI-FLAT, licensed)
is the anti-aligned sector's remaining continuum-facing claim after NYQ-CONTROL-2 refuted
FND-175 and retired the bordered corrector. Its caution rider (reopened 2026-10-04) says its
states carried an s-Nyquist weight of 8.7e-4 against the 1e-4 bar in force since 2026-09-23,
and that a re-march under the bar would settle it. This commission is that re-march. It ends
with FND-174 either licensed on clean states or refuted and kept; either way the caution is
gone and the sector's ration is spent. No successor is implied by any outcome.

## Question
Does the anti-aligned two-frequency family at q = 5/4 (FND-173's polished member, A2 = 0.02 R2,
om2 = -1.110632) march flat through the aligned collapse region on 144x36 when every point
must gate WITHOUT Nyquist content (wsNyq <= 1e-4), and does the family exist at all under that
bar?

## Instrument
The registered stage-2c arc march (FND-163/164 protocol, benchmarks/foundations/antiarc.py as
run for FND-174: ds 0.08, 144x36, the credentialed sparse instrument, cached 144x36:arc:n2=5
pattern, plain Gauss-Newton), with the gate's Nyquist flag applied as a BAR (the 09-23 rule).
Two arms, same seeds, same march, differing in one switch:
  A1  the registered march verbatim; wsNyq read and barred at the gate, nothing else changed.
  A2  the same march with each Gauss-Newton step projected onto s-harmonics |k| <= NS/3
      before acceptance (dealias_s, the FAULT-13 remedy credentialed by NYQ-CONTROL's c1 and
      c2: it does not disturb a smooth solution and reproduces the GN floor). No bordered
      corrector anywhere; no lam ladder changes; the sparse instrument untouched.
The driver runs one arc point per invocation, atomic checkpoint analysis/antiarc_nyq_ckpt.pkl,
the solver's round messages in the log; terminal line 'ANTI-ARC-NYQ COMPLETE -- run the
verdict'. One machine per job (the PC; the Mac keeps Leg B).

## Protocol
  c1  FND-173's polished member (analysis/antialigned_ckpt.pkl, d3|5/4|anti|polished) re-gated
      in place by plain GN at its own pin (a2, om2 free, 20 rounds): RMS, closure, wsNyq read.
      It gated at RMS 8.35e-10 before the bar existed; its wsNyq has never been a bar.
  c2  one aligned stage-2c arc point from the registered 4/3 waypoint-1 member (the aligned
      control FND-174 used), under A1 and under A2: must gate under the bar in both (aligned
      members carry wsNyq ~1e-7 to 1e-9).
  A1  20 arc points from s0, s1 as FND-174 (s1 = the a2-pinned member at 1.02 A2, re-made
      under plain GN if not on disk); per point SEALED: A2, rate, V_pt, f_dir, om2, RMS,
      closure, wsNyq, rounds, manner of stopping.
  A2  the same 20 points with the projection on.
Order: c1, c2 (A1 then A2), A1 points 1..20, A2 points 1..20.

## Bars (LOCKED before any point)
gate: RMS < 1e-8 and closure < 1e-6 (the q-sweep bars, as FND-174). Nyquist bar: wsNyq <=
1e-4. "gated clean" = all three. C1 rule: f_dir rise over the span, collapse if >= +0.15
(FND-174's own rule). Licence span: A2_max >= 0.0052 (ANTI-ARC-X). Minimum for a verdict: 8
points gated clean in the arm read.

## Verdict forms (LOCKED)
ANTI-NYQ-CONTROL-FAIL  c2 fails under either arm, or c1 fails the RMS/closure gate: stop.
ANTI-FLAT-CLEAN        some arm has >= 8 points gated clean with C1 rise < +0.15 and the licence
                       span covered: the anti-aligned family exists and marches flat on clean
                       states. FND-174 is RE-LICENSED on clean states (rider; caution closed);
                       the arm that did it is named. If only A2 does it, the de-aliasing
                       projection becomes part of the registered protocol for this family.
ANTI-COLLAPSE-CLEAN    some arm has >= 8 points gated clean and C1 rise >= +0.15: the collapse
                       is handedness-blind on clean states. FND-174 REFUTED (Failed, kept);
                       the handedness contrast of 2026-09-07 was Nyquist-conditioned.
ANTI-FLAT-NYQ          no arm reaches 8 points gated clean, but A1 gates >= 8 points on RMS and
                       closure alone (as FND-174 did) with wsNyq > 1e-4: the family's flatness
                       at 144x36 exists only with grid-scale content. FND-174 REFUTED as a
                       continuum statement (Failed, kept); the instrument fact of 2026-09-07
                       stands as a record of this grid. FND-173 takes a rider if c1 reads
                       wsNyq > 1e-4 (its member carries the content; it gated under its own
                       bars and is not refuted by a bar that postdates it).
ANTI-NYQ-REFUSED       no arm gates 8 points even on RMS and closure: the march itself does not
                       reproduce; recorded; FND-174 takes a reproducibility rider.
Sub-readings recorded with any verdict and changing none: whether A2's clean points are the
same states as A1's (|dx|/|x| per point), and c1's wsNyq.

## What this commission does not ask
Whether the family exists at 288x36 (ANTI-ARC-S288: GN floors at exact resonance there; the
bordered corrector that was built for it is retired). Whether the handedness contrast is
physical or a discretization fact. Nothing about the kernel.

## Rules
No rescue; the bars are the bars; the registered march is not altered except by the one switch
in A2 and the bar at the gate; verdict once from the sealed checkpoint by antiarc_nyq_verdict.py;
riders and status changes on the author's word; failure kept whichever way it goes.

## Reads owed at lock
FND-174 (seeds, ds, bars, the 20-point licence, the wsNyq 8.7e-4 diagnostic); FND-173 (the
polished member's pin and om2); FND-163/164 (the stage-2c arc protocol as registered);
NYQ-CONTROL c1/c2 (the de-aliasing credential); the aligned 4/3 waypoint-1 member's location
on disk.

## Cost
The PC. 42 solves on 144x36 (2 controls, 40 arc points); FND-174's 20 points ran in one
session on the author's laptop. Expect a day. Sandbox: the driver and verdict script,
delivered as a zip before lock.

## Author's lock
Locked on the author's word on 2026-10-04 ("lock ANTI-ARC-NYQ"). No arc point existed.

## READS AT LOCK

FND-174: seeds s0 = FND-173's polished member (analysis/antialigned_ckpt.pkl, d3|5/4|anti|polished),
  s1 = a2-pinned member at 1.02 A2 under plain GN; ds 0.08; 144x36 cell 5/4; bars RMS 1e-8,
  closure 1e-6; C1 rule +0.15; ANTI-ARC-X licence A2_max >= 0.0052; 20 points; diagnostic
  wsNyq 8.7e-4 on its states. The repository's antiarc_ckpt.pkl holds the 12-point stage; the
  20-point extension's checkpoint is on the author's Mac; neither is read by this commission.
FND-173: the member's pin is its own A2 (0.0020880 class at 5/4), om2 -1.110632, RMS 8.35e-10.
FND-163/164: the stage-2c arc protocol is antiarc.py's arc_point verbatim (tangent from the last
  two states, 'arc' pin mode with (xb, t, ds), gn_sparse 60 rounds, measurements A2, rate, V_pt,
  f_dir, om2, RMS, closure); the new driver copies it and adds the wsNyq read and the bar.
NYQ-CONTROL c1/c2 (2026-10-02): the de-aliasing projection reproduces the GN floor at b = 0 and
  leaves the aligned member gated clean in one round; that is the credential A2 rests on.
Aligned control source: analysis/qsweep_stage1_ckpt.pkl, q4/3 members[0] (the waypoint-1 member
  FND-175's c2 and NYQ-CONTROL's c2 used), A2 0.0018792.

## INSTRUMENT DISCLOSURE AT LOCK

benchmarks/foundations/sparsej_instrument.py gains one keyword on gn_sparse, project=None,
applied to every candidate step (normal and lsmr fallback) before the acceptance ladder. With the
default the solver's behaviour is unchanged (no code path differs); arm A2 passes
kernel_continuation.dealias_s. The three insertion sites are annotated [SJ 2026-10-04]. This is
the only change to a credentialed file and it is inert for every other caller.

## SMOKE TEST (sandbox, 144x36, scratch checkpoint, discarded; recorded before the run)

c1 ran to completion in the sandbox: FND-173's member as stored reads RMS 8.3e-10, closure
5.1e-12, wsNyq 8.7e-4; re-gated by plain GN in one round, unchanged. The sub-reading the forms
name is therefore already visible: the member itself carries Nyquist content above the bar
(8.7 times), the same 8.7e-4 FND-174's diagnostic reported for its states. This is recorded here
so the PC's sealed c1 cannot be read as a surprise; it does not change any form. The aligned c2
cell's s1 seed gated in one round; its arc point began (fresh 144x36:arc:n2=4 pattern build) and
was cut by the sandbox's time limit; the driver resumes it from the sparse instrument's own
persistence. No anti-aligned arc point was computed.

## SHAKEDOWN NOTE (instrument, 2026-10-04, before any arc point)
The first PC invocation accepted the aligned control's s1 seed on RMS and closure alone (the
driver's own read), where antiarc.py gates s1 with q1.gate(pin=...) and its PIN_TOL of 1e-8.
gn_sparse's internal stop (RMS under the bar and A2 within 5 percent of the pin) therefore
returned the unmoved member as s1, the seed pair was identical, and the arc tangent divided by
zero (NaN; the solver's log showed 'invalid value in divide'). The driver now gates both s1
seeds exactly as antiarc.py does and refuses to march from a zero tangent. The checkpoint of
that invocation held c1 and the degenerate c2A1 seed only; it was discarded and the run
restarted from nothing. No arc point of either arm existed. Forms, bars and protocol unchanged.

## VERDICT DRY RUN (2026-10-04, before any arc point was sealed)
tools/aan_verdict_dryrun.py builds eleven synthetic checkpoints in the driver's exact layout and
runs the verdict against each form: FLAT-CLEAN (A2 only; both arms), COLLAPSE-CLEAN, FLAT-NYQ
(A2 halted), REFUSED (both arms; s1), CONTROL-FAIL (c2; c1), the provisional-by-scope sub-case,
and an unfinished arm. All ten writable states read correctly. The eleventh fixture carried a
halted point without the driver's halt flag, a state the driver cannot write; the verdict read it
as non-terminal, which is the right refusal. The verdict script is unchanged by the dry run.

## SHAKEDOWN NOTE 2 (2026-10-04): the PC's disk filled (745 MB free, Windows temporary files) during
the aligned control's seed; the Tee log write failed and the next invocation died inside a
checkpoint write. The checkpoint is atomic (temp file then rename) and was intact; c1 and c2A1's
seed survived. The driver now refuses to start with under 2 GB free, with a message, instead of
dying mid-write. No arc point of either arm had been computed. Forms, bars and protocol unchanged.

