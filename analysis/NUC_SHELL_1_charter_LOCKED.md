# COMMISSION NUC-SHELL-1 -- DOES THE REGISTERED WELL CLOSE WHERE NATURE'S SHELLS CLOSE?
# (CHARTER, LOCKED 2026-10-09 by the author; S1 run as a pre-lock instrument check; the table not yet read)

North Star line (section 5): (a) the scorecard target "Weights of atoms". NUC-BLIND-1/2 left the four-term model M2
with a blind residual of 0.011 to 0.016 percent of mass whose largest rows are the light doubly-magic and
neutron-rich nuclei (O-16, O-14, Mg-31); what a smooth liquid-drop form leaves out is shell structure. The registry
owns exactly one single-particle well: NUC-A's infinite spherical box at the derived geometry r0 = 1.1197 fm (from
d0 = 2.026 fm, NUC-017), filled on separate proton and neutron ladders, which produced the kinetic part of the
asymmetry coefficient (NUC-A) and, with NUC-B, the a_A = 19.85 MeV that M2 carries. This commission asks the well
the next question in the same spirit: do its closed shells fall at 2, 8, 20, 28, 50, 82, 126? If they do, the row's
next term is a derivation away; if they do not, the registry learns by name what its nucleus lacks (a
spin-orbit-class splitting, which the strand picture must either supply from its own mechanics or admit as
missing). Either answer moves the row; neither adds a constant.

Why the blind bar W does not apply: nothing is fitted. The well's closures are a property of the ordering of the
Bessel zeros, computed before the table is read (S1); the table is read once (S2) to locate nature's closures by a
rank rule with no threshold, and the two lists are compared. There is no calibration to hold out.

## Steps
  S1  THE WELL'S CLOSURES (run 2026-10-09 before this lock, no data read): the bottom of the well is a closure by
      definition (2); above it, each level's gap to the next divided by the mean of its two neighbouring gaps ranks
      the closures, and the six largest ratios at cumulative occupancy <= 184 are the well's next six closed shells.
      Result, recorded here at lock: 2, 8, 20, 34, 58, 92, 138 (the textbook closures of the spin-only box); first
      mismatch with 2, 8, 20, 28, 50, 82, 126 at 28.
  S2  NATURE'S CLOSURES, from AME2012 (data/ame2012/AME2012.txt, sha256 88c6272c...), A >= 12, read once: for each
      even N the mean over isotopic chains of the drop in the two-neutron separation energy across N,
      J_n(N) = mean_Z [S_2n(Z,N) - S_2n(Z,N+2)], chains with the three masses present and at least three chains;
      likewise J_p(Z) with S_2p along isotonic chains. SEEN closures: the seven largest J_n over even N in [6, 160]
      and the seven largest J_p over even Z in [6, 100].
  S3  THE SCORE, per species: hits (box closures that are SEEN), misses (SEEN closures the box lacks), false (box
      closures not SEEN). The verdict from the locked forms below. The J values at every box closure and every magic
      number are printed and kept whatever they say.

## Bars (to be LOCKED)
B-1  The well is NUC-A's as registered: infinite spherical box, derived r0, spin degeneracy only. No spin-orbit, no
     diffuseness, no depth, no second well; a different well is a different commission.
B-2  The rank rules (six ratios for S1; seven largest drops for S2; the ranges) are fixed here and not tuned after
     the table is read. No MeV threshold anywhere.
B-3  No new constant; nothing is fitted; the table is read once, after this lock, by the driver's --s2 path.
B-4  The prior, stated and not leaned on: SHELLS-PARTIAL. The spin-only box matches nature at 2, 8, 20 and fails at
     28; S2 will see 28, 50, 82, 126 that the box does not have, and the box's 34, 58, 92 will not be seen.
B-5  One run; the verdict is the driver's printed line; failure kept.

## Verdict forms (to be LOCKED)
SHELLS-MATCH     for both species, misses = 0 and false <= 1: the registered well is nature's well; the shell
                 correction is the row's next derivation (chartered separately, with its own blind hold-out).
SHELLS-PARTIAL   hits >= 3 for both species and S1's first mismatch at 28: the well carries the light closures and
                 loses the heavy ones; the registry's nucleus lacks the splitting that moves 1f7/2 down to close
                 28, and the row's next question is whether the strand picture supplies a spin-orbit-class term
                 (named next-order, not chartered here).
SHELLS-FAIL      otherwise: the well's closures are not nature's even at the light end; NUC-A's ladder is a
                 counting device, not a nucleus.
In every form: riders on NUC-A (the well's closures on the record) and NUC-022 (the mode ladder's shell
structure, or its absence); the scorecard row's "Blocked by" cell gains the named missing term under PARTIAL or
FAIL; no status change; the five numbers unchanged.

## Instrument
benchmarks/nuclear/nuc_shell_1.py: --s1 (no data) and --s2 (the one read, prints the verdict). Seconds on any
machine; the PC runs it so that the read happens on the machine of record:
    python benchmarks\nuclear\nuc_shell_1.py --s2 > analysis\NUC_SHELL_1_verdict.log

## Rules
No rescue; rank rules fixed before the read; riders the author's; failure kept.

## Pre-lock instrument notes (sandbox, 2026-10-09; recorded at lock)
A first draft scored a Strutinsky shell correction against a fresh hold-out; the smoothing showed no plateau on
this ladder and the harmonic-oscillator control failed, so the step was withdrawn before any lock and before any
data was read; it is named as the next-order under SHELLS-MATCH only, with a solver that passes its control.
S1 was run (above). S2 has not been run.

## Author's lock
LOCKED 2026-10-09 ("lock NUC-SHELL-1"). The well (B-1), the rank rules and ranges (B-2), the forms and the prior are
fixed from this line; the table is read once, after this line, by --s2 on the PC. Nothing in this file or in
benchmarks/nuclear/nuc_shell_1.py is edited after the read.
