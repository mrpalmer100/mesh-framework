# COMMISSION TERMINAL-TWIST -- RESULTS (executed 2026-09-27, sandbox; charter analysis/TERMINAL_TWIST_charter_LOCKED.md)

Verdict once from the sealed output analysis/terminal_twist.npz by
benchmarks/foundations/terminal_twist_verdict.py; log analysis/TERMINAL_TWIST_verdict.log;
instrument benchmarks/foundations/terminal_twist.py (GRV-045's engine used as registered).

## Form rendered (registered as FND-180, granted 2026-09-27; GRV-045 amended the same day)

    TERMINAL-RECON-WRONG-VARIABLE

## T1: what the registered reconnection actually hands over

The candidate (a terminal is a reconnection site; each event hands 2 pi of winding into the
conductor's azimuth) rested on GRV-045's F2: "the punch-through exchanges exactly one 2 pi
quantum of frame winding". Read at lock, the registered engine carries no material azimuth
field and computes its F2 observable, the integrated Frenet-frame rotation of the centre-line
curve, on the FINAL configuration only. T1 read it before and after, and read the writhe,
which Calugareanu's ledger converts into material twist under linking conservation:

| run | Frenet phi/2pi before -> after | writhe before -> after | material twist change |
|---|---|---|---|
| L = 4, asymmetric seed (GRV-045's generic case) | -1.217 -> -1.006 (change +0.21) | -0.028 -> 0.000 | -0.028 x 2pi |
| L = 6, asymmetric seed | -1.217 -> -1.012 (change +0.21) | -0.028 -> 0.000 | -0.028 x 2pi |
| L = 4, symmetric seed (control) | +1.000 -> +1.000 (change 0) | 0 -> 0 | 0 |

The 2 pi is a property of the curve's geometry, present in the seeded initial state before
any event (and, in the planar control, exactly the Frenet inflection count of a plane curve,
which the Frenet frame reports as 2 pi with no twist anywhere). The change across the
punch-through is 0.21 x 2 pi in that observable and 0.028 in writhe, so the material azimuth
changes by about 0.03 x 2 pi. No quantum enters the screw sector. Bar T1 (1.00 +/- 0.05)
FAILS at 0.03.

## Consequence for the terminal

The registered reconnection is not the terminal. A terminal that spins current remains a NEW
PRIMITIVE, now with a sharper specification than FND-179 left it: it must hand an integer
2 pi of MATERIAL twist (linking) per charge into the conductor's azimuth, and no registered
event does that; the registered punch-through moves writhe by three percent of a turn. The
supply demand of T4 stands as arithmetic: one ampere is 6.2e18 handovers per second per
terminal, whatever object performs them.

T2 was run as a display only (the candidate's dynamics if a quantum existed): FND-179's
chain does carry 2 pi steps at rate R into whole-strand rotation, with the mean rate 8 to 43
percent above 2 pi R from undamped ringing; transport is not the obstacle, the source is.
T3 did not run (T1 failed; charter reads-at-lock).

## FLAG for the author: GRV-045 (Derived) needs an amendment

Not a bar of this commission; a registered instrument re-read that the commission could not
avoid. GRV-045's F2 states an EXCHANGED quantum but the benchmark measures the final state's
Frenet rotation without subtracting the seed's; the before/after exchange is 0.21 x 2 pi, and
the planar control's "2 pi" is an inflection artifact of the Frenet frame (the claim's own
log reports the symmetric seed as zero; this engine, run as registered, reports +1.000; the
difference is worth a look at lock of any amendment). What stands: F1 (continuous passage,
no break) and F3's conclusion, which becomes STRONGER, since a bounded exchange of 0.03 of a
turn cannot flip an extensive sign either; charge survives reconnection. What does not
survive the reading: "quantized at 2 pi", the length-independence claim as stated (it is the
seed's geometry that is length-independent), and F4's belt-trick resonance. Amending a
Derived claim is the author's act; the amendment text is drafted in fnd180_claim.yaml's note.

## NORTH_STAR scorecard (row "Strength of magnets")

Nearest step: the terminal primitive, now specified (an integer 2 pi of material twist per
charge handed into the azimuth), or the electron model. Targets moved 0; inputs retired 0;
one candidate identification refuted and kept; one Derived claim flagged for amendment.

## Shakedown notes

1. The writhe integral uses every second node of the engine's curve (stride 2) for speed;
   the values are three-percent-class, far from the bar, so the stride is immaterial.
2. The engine and its seed are GRV-045's verbatim; only the initial state is kept and the
   three observables read on it. No parameter was changed.
