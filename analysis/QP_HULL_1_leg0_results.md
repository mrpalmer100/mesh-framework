# QP-HULL-1 Leg 0: the hull instrument's credential against the retained 13/9 cell members (executor, mini, 2026-10-21 to 24)

Status: instrument record (no commission, no verdict; QP-HULL-1's charter is parked and its successor QP-HULL-2
is charted on these numbers). Instrument: `benchmarks/foundations/qp_hull.py` (the two-phase hull u(theta1,
theta2, phi) with the spectral s-derivative K1 d/dtheta1 + K2 d/dtheta2) and the credential script
`benchmarks/foundations/qp_hull_leg0.py --part2`. Records: `analysis/qp_hull_leg0_part2.json`,
`analysis/qp_hull_leg0_part2.log` (the full solver log of the run of record on the machine of record, with its
three restarts). Per-solve pickles stay on the mini (`~/qp/analysis/qp_hull_leg0_part2_*.pkl`).

## 1. What was asked of the instrument

The charter's mechanism section says a rational cell aliases the two-frequency content (the lowest alias of the
mean field is (N2, -N1)) and that the hull, which keeps theta1 and theta2 independent, contains every cell as the
restriction to the line theta2 = q theta1. If that is right, then at a HIGH-order rational the hull and the cell
must agree, and agree better as the hull is refined, with no operator added. Part 2 tests exactly that at
q = 13/9 against COMPOSITE-SELECT Leg B's RETAINED members (432 x 36, from the sealed checkpoint on the mini):
the hull is solved INDEPENDENTLY (level-1 recovery, then the registered sub-pin ladder to waypoint 1 at
A2 = 0.0018792, then three rungs to the second member at 0.0046979), on two hull grids, 24 x 8 x 36 and
48 x 12 x 36, and compared with the cell in the cell's own metrics after restriction to the line. Nothing at
q = 1.492 is computed (v7).

The retained cell members (read-only inputs):
  A2 0.0018792: rms 7.7e-12, om1 4.4425470, om2 2.8519801, gam 0.5771997, Sigma_wave 2.598867
  A2 0.0046979: rms 5.3e-11, om1 4.4403099, om2 2.9228049, gam 0.5760610, Sigma_wave 2.604887

## 2. Results

Level-1 recovery on the hull (24 x 8 x 36, 587 s): rms 7.7e-15, theta 0.95531662, om1 4.4428829, gam 0.57735027.
These are the level-1 identities to machine precision: om1 = pi sqrt 2 = 4.44288294 (to 1e-15), gam = 1 / sqrt 3
(to 2e-15), theta = arccos(1 / sqrt 3) = 0.95531662 (to 3e-16), i.e. cos^2 theta = 1 / 3.

Hull against cell, both members, both grids (rel = hull / cell - 1; the restricted-state metrics are the cell's
max |dtheta|, |dpt|, |dT| and the cell-equation RMS of the restricted hull state):

  grid        A2        om2 hull    om2 cell    rel om2    rel om1   rel gam   rel price   dtheta   dpt      dT       cell rms of restricted
  24x8x36     0.0018792 2.8505475   2.8519801   -5.0e-04   1.0e-05   1.6e-05   2.2e-05     1.5e-03  1.1e-03  1.0e-02  5.5e-02
  24x8x36     0.0046979 2.8797675   2.9228049   -1.5e-02   8.5e-05   3.5e-04   4.3e-04     2.9e-02  2.1e-02  1.3e-01  5.0e-01
  48x12x36    0.0018792 2.8519316   2.8519801   -1.7e-05   9.8e-06   2.0e-05   2.6e-05     1.2e-04  8.6e-05  2.0e-04  1.4e-03
  48x12x36    0.0046979 2.9119786   2.9228049   -3.7e-03   3.8e-05   6.9e-05   8.4e-05     1.4e-02  1.1e-02  2.7e-02  8.7e-02

Every hull solve converged to field RMS 5e-14 or better with closure below 5e-11 and all pins met. The member-2
rungs on 48 x 12 ran om2 = 2.8678993, 2.8887039, 2.9119786 at pins 0.0028187, 0.0037583, 0.0046979; each rung
took 52000 to 61000 s on the mini (14 to 17 hours), member 1 with the level-1 prolongation 32000 s.

## 3. Reading

R1. The hull reproduces the cell at the high-order rational and converges onto it with refinement, with no
    operator added: at member 1 the om2 gap falls from 5.0e-4 to 1.7e-5 (a factor 30) between the two grids,
    and the restricted state's cell-equation residual from 5.5e-2 to 1.4e-3; om1, gam and FND-135's price agree
    at 1e-5 to 1e-4 on both grids. This is the charter's mechanism statement passing its first test: the cell is
    the hull's restriction, the hull adds nothing.

R2. The second member (A2 2.5 times larger) converges more slowly: om2 gap 1.5e-2 to 3.7e-3 (a factor 4) and the
    restricted residual 0.50 to 0.087. The gap scales as NT2^(-3.4) between NT2 = 8 and 12, so the second
    member's level-2 content is under-resolved in theta2 at 12 points and the next refinement should go to
    NT2 = 24 (projected om2 gap of order 4e-4) rather than to NT1. The price agrees to 8.4e-5 even where om2 is
    off 3.7e-3, because Sigma_wave is quadratic in the amplitudes and the pin fixes A2.

R3. Against the charter's bars as written: v1 (level-1 identity) is met at 24 x 8 x 36 to 1e-14 in the three
    identities (the bar named 48 x 48 x 36, a grid not run; the identities are theta2-independent and the result
    cannot depend on NT2). v2 (cell reproduction to RMS 1e-9 from the lifted cell state as seed) was NOT run as
    written; what was run is the stronger-but-coarser independent march, which meets 1.7e-5 at member 1 and
    3.7e-3 at member 2 in om2. The 1e-9 bar is the right bar for the seeded form of the test and remains to be
    run; the independent form has no 1e-9 to offer at any finite hull grid and should not be scored against it.
    v3 (price to 1e-4): met on both members on 48 x 12 (2.6e-5, 8.4e-5), against the retained members at 0.0019
    and 0.0047 rather than Leg B's deepest member (not in this run). v4 (level-1 moment 1/3): the level-1 angle
    gives cos^2 theta = 1 / 3 to 3e-16; the torus-averaged moment itself was not computed as a separate number.
    v5 (closure below 1e-6): met on every solve by three or more orders. v6 (memory at 48 x 48 x 54): not
    measured; the grids run were far smaller. v7: kept; no number at 1.492.

R4. Cost: a 48 x 12 x 36 rung is 14 to 17 hours on the mini. The projected NT2 = 24 grid is 2 to 3 times that per
    rung, so a convergence credential on member 2 is a week of the mini; the lab's one-job-per-machine rule
    makes this the whole machine for that week.

## 4. What QP-HULL-2 should be charted on (the executor's input to the author's draft; not a charter)

- The credential as the hull's CONVERGENCE onto the cell at 13/9, stated as a rate: om2 gap at member 2 on grids
  (48, 12), (48, 24) and, if affordable, (96, 24), with the bar that the gap falls at least as NT2^(-3) and is
  below 1e-3 at NT2 = 24. The seeded v2 (lifted cell state, RMS 1e-9) as the second, cheaper credential.
- Q1 at q = 1.492 read at the grid that met the bar, with the convergence rate carried onto the result as its
  uncertainty, and Q2 at 3/2 on the same grid.
- The memory and time per rung measured on the credential grids (R4) as the booking, not an estimate.
- The restricted-state residual (cell rms of restricted) kept as the per-member diagnostic of resolution, since
  it moves by a factor 40 where om2 moves by 30 and is available without a cell to compare against at 1.492
  (the hull state restricted to the 1.492 line and evaluated in the cell operator of the nearest rational
  neighbour is not a bar, but a resolution indicator; QP-HULL-2 should say whether it is used and how).
