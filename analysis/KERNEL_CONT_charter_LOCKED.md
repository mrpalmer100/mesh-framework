# COMMISSION KERNEL-CONT -- CONTINUING A RESONANCE ALONG ITS KERNEL
# (CHARTER, LOCKED 2026-09-12 on the author's word; before any sweep point)

## Question
The anti-aligned sector's continuum object is a resonance: at exact
resonance the a2-pinned linearization has a near-null direction c and
Gauss-Newton floors (FND-142's plateau; S288 at 1.3e-7; 3/2, 4/3, 5/3 at
144x36 at 4e-7 to 4e-6). Does a bordered continuation along c -- the
kernel coordinate b = c^T (x - x_ref) made an explicit parameter, the
second-order solvability condition found by sweeping b -- produce a
member at full bars where GN could not? If so, the anti-aligned
"members" are Lyapunov-Schmidt branches of the resonance, and the
sector can be marched.

## Instrument
benchmarks/foundations/kernel_continuation.py (built 2026-09-12; the
bordering algorithm on the credentialed banded solver; the near-null
direction found in the (1,1) harmonic subspace with the injection
direction and its phase partner projected out). Validation before this
charter: at the floored 4/3 anti-aligned state (RMS 6.6e-7 at b = 0), the
corrector at b = +0.05 descended to 1.5e-7 in 15 rounds and was still
descending; b held to 1e-12; om2 steady.

## Protocol
STAGE A (validation, 144x36, cell 4/3, the state aa|4/3|anti|-0.35|gate):
sweep b in {-0.20, -0.10, -0.05, +0.05, +0.10, +0.20, +0.30}, 40 corrector
rounds each, from the floored state; record RMS(b), om2(b), closure. Then
bisect on the two best b to a third level. CONTROL (c1): the b = 0 solve
must reproduce the GN floor (6.6e-7) -- the instrument adds nothing at
b = 0. CONTROL (c2): on an ALIGNED member (4/3 waypoint 1, which gates
under GN) the bordered solve at b = 0 must gate identically (the
instrument does not alter a non-degenerate solve).
STAGE B (the target, 288x36, cell 5/4, the S288 s0 state at RMS 1.3e-7):
the same sweep with the near-null direction recomputed at that state.

## Verdict forms (LOCKED)
KC-MEMBER:   at some b the solve meets the q-sweep bars (RMS < 1e-8,
             closure < 1e-6, pin held) at stage B -- a continuum anti-
             aligned member exists as a kernel branch; b* and om2* are
             the member's coordinates; the sector is marchable
             (a follow-on charter marches it with b carried).
KC-FLOOR:    RMS(b) has a minimum but the minimum stays above the bar at
             every b (stage B): the obstruction is not (only) along c;
             the second kernel direction or the om2 coupling is named
             as the next-order; no member.
KC-A-ONLY:   stage A finds a member, stage B does not (the 144 result is
             again grid-conditioned); reported as such.
KC-CONTROL-FAIL: c1 or c2 fails: the instrument is not credentialed; stop.
KC-REFUSED:  the near-null direction is not found (sigma > 1e-3 of the
             row norm) at either stage.

## Rules
No rescue; bars are the q-sweep bars; no bar relaxed; the sweep grid and
the bisection depth fixed above; local execution AFTER Leg B; verdict in
the session; FND-173's grid-condition rider inherited.
