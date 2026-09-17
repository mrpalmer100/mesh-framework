# COMMISSION KERNEL-MARCH-2 -- THE ANTI-ALIGNED FAMILY TO THE REGULARIZATION POINT
# (CHARTER, LOCKED 2026-09-17 on the author's word; before any point beyond p29)

## Question
KERNEL-MARCH-X (KM-FLAT, licensed) found the anti-aligned 5/4 family flat to
A2 0.0054 on the s-resolved chart, with the kernel's residual norm sigma
rising smoothly 2.7e-4 -> 2.4e-3 (x8.7) and no sign of saturating. The
sealed trend extrapolates to sigma ~ 1e-2 (a regular, GN-gateable branch)
near A2 ~ 0.012. Two questions, in order:
  Q1 Does the branch REGULARIZE -- does sigma reach 1e-2, and does a plain
     Gauss-Newton solve gate there without bordering?
  Q2 Once regular, does the family COLLAPSE (the aligned collapse happens
     on a regular branch), or stay flat?

## Protocol
The same march continued: 288x36, ds 0.08, bordered arc solves with c_n
recomputed per point and the kernel coordinate carried, measurements sealed
(A2, rate, V_pt, f_dir, om2, RMS, closure, b_step, sigma). Budget: 60 more
points (p30-p89; ~0.0120 at the current spacing). GN CONTROL, every 10th
point (p39, p49, ...): from the gated bordered state, a plain gn_sparse
arc solve on the same pinned problem, 10 rounds, RECORDED (rms_gn): the
regularization is real when the plain solver gates where it used to floor.
Verdict once on the full 90-point profile.

## Verdict forms (LOCKED)
KM2-REGULAR-FLAT:     sigma >= 1e-2 reached AND a GN control gates at or
                      after that point AND C1 rise (last 10 vs first 10 of
                      the extension) < +0.15: the branch regularizes and
                      stays flat -- handedness selectivity holds on a
                      regular branch; the collapse mechanism is not "any
                      regular branch collapses".
KM2-REGULAR-COLLAPSE: sigma >= 1e-2 reached AND C1 rise >= +0.15 at or
                      after regularization: the anti-aligned family
                      collapses once regular -- the resonance's degeneracy
                      was what protected it; handedness selectivity is
                      re-read as degeneracy selectivity.
KM2-COLLAPSE-EARLY:   C1 rise >= +0.15 before sigma reaches 1e-2.
KM2-NOT-REGULAR:      90/90 gated, sigma < 1e-2 at p89 (the trend saturates
                      or slows): flat, still degenerate; the regularization
                      prediction FAILS as stated (recorded as such).
KM2-REFUSED:          fewer than 20 of the 60 extension points gated.
Display: sigma(A2) fit (linear vs saturating); the GN-control rms per
decade; om2 detuning growth; Sigma_wave and max|v| at p89.

## Rules
No rescue; q-sweep bars; the bordered solver as credentialed (FND-175);
one machine (the PC); verdict in the session; FND-172..176 riders inherited.
