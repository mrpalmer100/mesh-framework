# COMMISSION NUC-SHELL-2 -- THE PRICE OF THE MAGIC NUMBERS IN THE MODE PATH'S TORSION
# (CHARTER, LOCKED 2026-10-09 by the author; only the tau R = 0 control had run; the scan runs after this line)

North Star line (section 5): (a) the scorecard target "Weights of atoms". NUC-SHELL-1 found the registered well
closes at 34, 58, 92, 138 where nature shows none and lacks 28, 50, 82, 126; ORBIT-TWIST found the registered
machinery's one handedness-times-sense term, the geometric rotation of the transverse frame along a path with
torsion tau, Delta k = sigma tau, with the sign structure of l . s and not its l-scaling, and the torsion of a
nucleon mode's path unregistered. This commission does not derive that torsion; it prices it. It applies the one
registered term to the registered ladder and asks: is there any torsion in the physical range at which the well
closes at nature's seven magic numbers? The whole scan is the result; nothing is fitted; no data is read.

## The term, as ORBIT-TWIST left it and as the massive dispersion carries it
For a mode of wavenumber k and handedness sigma on a path of torsion tau, Delta k = sigma tau (ORBIT-TWIST M2,
flat in the winding number). On NUC-A's dispersion e = hbar^2 k^2 / 2 m_N this is Delta e = hbar^2 k tau / m_N,
which in the box's units (hbar^2 / 2 m_N R^2, levels x_nl^2) is Delta = 2 x_nl (tau R): proportional to the level's
x, flat in l at fixed k. Applied as the j = l + 1/2 member (degeneracy 2l + 2) lowered by Delta/2 and the j = l - 1/2
member (degeneracy 2l) raised by Delta/2, l >= 1; l = 0 unsplit. The identification of handedness with j = l +/- 1/2
is the one the term's sign structure allows (sigma times the orbital sense); which of the two signs closes 28 is
reported, both are scanned, and the verdict is read on the sign that closes 28 (the sign is a reading, not a choice:
if only the "wrong" sign closes 28, that is recorded as such).

## Steps
  P1  CONTROL (run 2026-10-09 before this lock): at tau R = 0 the split ladder, with degenerate members merged, gives
      NUC-SHELL-1's closures 2, 8, 20, 34, 58, 92, 138 under the locked rank rule. Passed.
  P2  THE SCAN: tau R from 0 to 2.0 in steps of 0.02, both signs; at each tau R the closures by NUC-SHELL-1's locked
      rank rule (the bottom plus the six largest gap ratios at cumulative occupancy <= 184), the hits among
      2, 8, 20, 28, 50, 82, 126, and whether the first four are all present. The full table to
      analysis/nuc_shell_2_scan.json; the closures printed every 0.2.
  P3  THE PRICE: the tau R range (if any) at which all seven are closures; the range at which the first four are;
      the range at which 28 appears at all. In physical units tau = (tau R)/R with R = r0 A^(1/3), r0 = 1.1197 fm:
      at A = 56, tau R = 1 is tau = 1/(4.3 fm).

## Bars (to be LOCKED)
B-1  The ladder, the rank rule and the ranges are NUC-SHELL-1's, unchanged. The term is ORBIT-TWIST's, unchanged
     in form; its only free quantity is tau R, which is scanned, never chosen.
B-2  The scan range [0, 2] and step 0.02 are fixed here; no finer search around a near miss.
B-3  No data is read; the magic numbers 2, 8, 20, 28, 50, 82, 126 are the target as nature states them.
B-4  The prior, stated and not leaned on: PRICE-PARTIAL. A term growing with k but flat in l may bring 1f7/2 down
     to close 28 and 1g9/2 to close 50 at one tau R, but 82 and 126 need the next shell's intruder to drop by a
     full shell spacing, unlikely at the same tau R.
B-5  One scan; the verdict is the driver's printed line; failure kept. Near-degenerate members at small tau R
     distort the gap-ratio rule (a known property of the rule, not tuned around).

## Verdict forms (to be LOCKED)
PRICE-FOUND     some tau R in [0, 2] gives all seven magic numbers as the well's closures on the sign that closes
                28: the magic numbers are priced at one geometric number, the nucleon mode path's torsion, and the
                row's "Blocked by" cell names it; a registered geometry (FND-091's helix angles, the certified knots'
                torsion) can then be asked to supply it (a later charter).
PRICE-PARTIAL   the best tau R gives 2, 8, 20, 28 but not all seven: the flat-in-l term reaches the first missing
                shell and no further; the l-scaling is missing above 28.
PRICE-NONE      no tau R gives 28: the flat-in-l form cannot close the first missing shell; the l-scaling itself is
                the missing physics and the "Blocked by" cell is final at this level.
In every form: a rider on NUC-A (the scan on the record) and on FND-MATTER-019 or FND-091 only under PRICE-FOUND
(the torsion they would have to supply); no status change; the five numbers unchanged (a price is not a prediction).

## Instrument
benchmarks/nuclear/nuc_shell_2.py (imports NUC-SHELL-1's ladder and rule; --control for P1; the scan otherwise).
Seconds. The PC runs it so that the scan happens on the machine of record:
    python benchmarks\nuclear\nuc_shell_2.py | Tee-Object -FilePath analysis\NUC_SHELL_2_verdict.log

## Rules
No rescue; the scan range fixed; the sign read, not chosen; riders the author's; failure kept.

## Author's lock
LOCKED 2026-10-09 ("lock nuc-shell-2"). The term's form, the ladder and rule, the scan range and step, the forms and the prior
are fixed from this line; the scan runs once on the PC after it; nothing in this file or in the driver is edited after.
