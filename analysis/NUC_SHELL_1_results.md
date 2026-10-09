# COMMISSION NUC-SHELL-1 -- RESULTS (the PC, 2026-10-09; the table read once; verdict computed once)

Charter: analysis/NUC_SHELL_1_charter_LOCKED.md (locked 2026-10-09 after S1 and before the read). Driver
benchmarks/nuclear/nuc_shell_1.py --s2; log analysis/NUC_SHELL_1_verdict.log.

## VERDICT: SHELLS-FAIL

The locked form: SHELLS-PARTIAL needed hits >= 3 for both species with S1's first mismatch at 28; neutrons scored
hits 2 (8, 20), misses 5 (14, 16, 28, 50, 82), false 4 (34, 58, 92, 138); protons hits 2 (8, 20), misses 5 (6, 12, 14,
16, 28), false 3 (34, 58, 92). FAIL by the form.

## What the data say (kept whatever the form)

| closure | box? | J_n (MeV) | J_p (MeV) | nature |
|---|---|---|---|---|
| 8 | yes | +11.02 | +12.03 | closed |
| 20 | yes | +4.65 | +6.27 | closed |
| 28 | no | +5.24 | +6.67 | closed |
| 34 | yes | +1.95 | +3.00 | not closed |
| 50 | no | +4.71 | +5.72 | closed |
| 58 | yes | +0.83 | +2.03 | not closed |
| 82 | no | +4.50 | +3.71 | closed |
| 92 | yes | +0.68 | +1.84 | not closed |
| 126 | no | +3.60 | (out of range) | closed |
| 138 | yes | +0.48 | (out of range) | not closed |

Above N = Z = 20 the registered well and nature part company completely: every closure the box has (34, 58, 92,
138) shows a separation-energy drop of 0.5 to 2 MeV, the background level, and every closure nature has (28, 50,
82, 126) shows 3.6 to 6.7 MeV and is absent from the box. The light closures 8 and 20 are shared, and the bottom
(2) is outside S2's range by the locked rule.

## The honest reading of the FAIL

Two things produced FAIL rather than the stated prior PARTIAL, and they are different in kind.
(1) The physics: the spin-only box has no 28, 50, 82, 126, and carries 34, 58, 92, 138 that nature does not. This
    was the prior's content, and the data confirm it with the margins above. The registry's nucleus lacks the
    splitting that moves the j = l + 1/2 member of each l down into the gap below (1f7/2 closes 28, 1g9/2 closes
    50, 1h11/2 closes 82, 1i13/2 closes 126): a spin-orbit-class term. No registered mechanism supplies one.
(2) The rule: the SEEN set was the seven largest drops over even N or Z, and at the light end the drops are large
    in absolute MeV at subshell closures the box does not resolve (N = 14, 16 from 1d5/2 and 2s1/2; Z = 6, 12, 14,
    16 likewise), so five of the seven SEEN slots went to light subshells and 126 (J = 3.6 MeV) did not make the
    neutron list. With the hits capped at 2 by this, the PARTIAL form's "hits >= 3" could not be met even though
    the box does carry 8 and 20. The rule was locked before the read and stands; the results would read PARTIAL
    under a rule that normalised drops by the local scale, and that is recorded here as a property of the rule,
    not as a reason to re-read. The verdict is SHELLS-FAIL.

Either way the question the commission asked is answered, and in the harder direction: the registered well is not
merely missing the heavy magic numbers, it predicts closures where nature has none, so a shell correction built
from it (the withdrawn next-order) would have hurt above A = 40 as the prior said. NUC-A's ladder gave the
asymmetry coefficient because that is a smooth, counting-level property of the well; the shell structure is not.

## Consequences (riders on the author's word)

NUC-A: rider: the well's closed shells are on the record (2, 8, 20, 34, 58, 92, 138; rank rule, no constant) and
  confronted with the separation-energy drops of AME2012: closures shared at 8 and 20; the box's 34, 58, 92, 138
  show no closure in the data (0.5 to 2 MeV) and nature's 28, 50, 82, 126 (3.6 to 6.7 MeV) are absent from the box.
  SHELLS-FAIL. The ladder's smooth content (the asymmetry coefficient) is unaffected; its shell content is absent.
NUC-022: rider: the collective mode ladder's spherical-box realisation carries no spin-orbit-class splitting; the
  shell closures above 20 are not in it (NUC-SHELL-1).
docs/NORTH_STAR.md, scorecard row "Weights of atoms", "Blocked by": add "the shell closures above N = Z = 20: the
  registered well (NUC-A's spin-only box) closes at 34, 58, 92, 138 where nature shows none and lacks 28, 50, 82,
  126; a spin-orbit-class splitting is the named missing term (NUC-SHELL-1, SHELLS-FAIL)".
No status change; the five numbers unchanged; the scorecard row's grade D3 unchanged.

## Named next-order (not chartered)

The missing term, from the strand picture or not at all: does a rope's mode in the registered well carry a
coupling between its orbital winding and its intrinsic twist of the sign and size (about 20 A^(-2/3) MeV per unit
l dot s) that closes 28? That is a derivation in the ELEC/QB machinery (the half-angle law and the winding-charge
dictionary), not a nuclear fit; if the registry cannot produce it, the row's "Blocked by" cell is final at this
level and the shell correction is not the mesh's to make. Not chartered here.
