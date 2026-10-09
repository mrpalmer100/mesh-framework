"""COMMISSION NUC-SHELL-1 -- do the registered well's closed shells fall where nature's do? No new constant.
Charter analysis/NUC_SHELL_1_charter_LOCKED.md. Scorecard target: "Weights of atoms" (the He-4/O-16 class of misses:
what M2's smooth form leaves out is shell structure, and the registry owns a well that either has it or does not).

The registered well is NUC-A's (explorations/nuc_a_asymmetry.py): the infinite spherical box of radius R = r0 A^(1/3)
at the DERIVED geometry r0 = (3/(4 pi sqrt 2))^(1/3) d0, d0 = 2.026 fm (NUC-017); single-particle levels e = x_nl^2 in
units of hbar^2 c^2/(2 m_N R^2) with x_nl the zeros of the spherical Bessel functions, degeneracy 2(2l+1) (spin only;
the registry has no spin-orbit term). The closures are a property of the dimensionless ladder alone (no hbar, no scale
enters S1 or S2): the ordering of the Bessel zeros.

S1  THE WELL'S CLOSED SHELLS. The bottom of the well is a closure by definition (N = 2). Above it, each level's gap to
    the next, divided by the mean of its two neighbouring gaps, ranks the closures; the SIX largest ratios at
    cumulative occupancy <= 184 are the well's next six closed shells (a rank rule: no threshold, no energy scale).
    Compared in order with 2, 8, 20, 28, 50, 82, 126; the first mismatch is named. Computed before the table is read.
S2  NATURE'S CLOSED SHELLS, read once from AME2012 after the lock. For each even N the shell signal is the mean over
    isotopic chains of the drop in the two-neutron separation energy across N: J_n(N) = mean_Z [S_2n(Z, N) - S_2n(Z, N+2)],
    S_2n(Z, N) = B(Z, N) - B(Z, N-2), chains with all masses present, A >= 12 (the registered scope); likewise
    J_p(Z) with S_2p along isotonic chains. A closure is SEEN at N when J_n(N) is among the SEVEN largest J_n over even
    N in [6, 160] (rank rule again; and the same for Z in [6, 100]). Nothing is fitted; no MeV threshold is chosen.
    The box's closures (S1) are then scored against the SEEN set for neutrons and for protons:
      hits    = box closures that are SEEN;      misses = SEEN closures the box does not have;
      false   = box closures that are not SEEN.
Verdict forms (locked): SHELLS-MATCH   if, for both species, misses = 0 and false <= 1 (the well is nature's well);
                        SHELLS-PARTIAL if hits >= 3 for both species but the first mismatch of S1 is at 28 (the well
                                       carries the light closures and loses the heavy ones);
                        SHELLS-FAIL    otherwise.
Prior (stated, not leaned on): the infinite box without spin-orbit closes at 2, 8, 20, 34, 40, 58, 92, 132, 138; it
matches nature at 2, 8, 20 and fails at 28; S2 will see 28, 50, 82, 126 that the box lacks: SHELLS-PARTIAL at best.
Usage:
    python benchmarks/nuclear/nuc_shell_1.py --s1              # the well's closures (no data read; run before the lock)
    python benchmarks/nuclear/nuc_shell_1.py --s2              # reads the table ONCE after the lock; prints the verdict
"""
import pathlib, sys
import numpy as np
from scipy.special import spherical_jn
from scipy.optimize import brentq
ROOT = pathlib.Path(__file__).resolve().parents[2]
TABLE = ROOT / 'data' / 'ame2012' / 'AME2012.txt'
D_H, D_N = 7.28897059, 8.07131714
MAGIC = [2, 8, 20, 28, 50, 82, 126]
NRANK, NMAXS1 = 6, 184
NSEEN, N_RANGE, Z_RANGE, AMIN = 7, (6, 160), (6, 100), 12


def bessel_zeros(l, n):
    zs, x0 = [], l + 1.5
    while len(zs) < n:
        x1 = x0 + 0.5
        if spherical_jn(l, x0) * spherical_jn(l, x1) < 0:
            zs.append(brentq(lambda x: spherical_jn(l, x), x0, x1))
        x0 = x1
    return zs


def ladder(nmax=200):
    lev = []
    for l in range(0, 40):
        for k, x in enumerate(bessel_zeros(l, 12), 1):
            lev.append((x ** 2, 2 * (2 * l + 1), f'{k}{"spdfghijklmnoqrtuvwxyz"[l] if l < 22 else "l" + str(l)}'))
    lev.sort()
    return lev[:nmax]


LAD = ladder()


def closures(lad=LAD, nrank=NRANK, nmax=NMAXS1):
    gaps = [lad[i + 1][0] - lad[i][0] for i in range(len(lad) - 1)]
    rows, cum = [], 0
    for i in range(len(gaps) - 1):
        cum += lad[i][1]
        if cum > nmax:
            break
        if i == 0:
            continue                                        # the bottom closure (2) is by definition, not by rank
        rows.append((cum, lad[i][2], lad[i + 1][2], gaps[i] / np.mean([gaps[i - 1], gaps[i + 1]])))
    top = sorted(rows, key=lambda r: -r[3])[:nrank]
    return [(2, '1s', '1p', float('nan'))] + sorted(top)


def s1():
    cl = closures()
    found = [c for c, *_ in cl]
    print(f"[ns1 S1] registered well: infinite spherical box, levels by Bessel zeros; the bottom plus the {NRANK} largest gap ratios below {NMAXS1}")
    print("[ns1 S1] the well's closed shells: " + ', '.join(f"{c} ({a}|{b}{'' if np.isnan(r) else f', {r:.1f}x'})" for c, a, b, r in cl))
    first_miss = None
    for mg in MAGIC:
        if mg in found:
            print(f"[ns1 S1]   {mg}: MATCH")
        else:
            print(f"[ns1 S1]   {mg}: MISS; first mismatch at {mg}"); first_miss = mg; break
    return found, first_miss


def read_table():
    B = {}
    for l in TABLE.read_text().splitlines()[1:]:
        t = l.split()
        if len(t) < 3:
            continue
        z, n, m = int(t[0]), int(t[1]), float(t[2])
        if z + n >= AMIN:
            B[(z, n)] = z * D_H + n * D_N - m
    return B


def seen(B, species):
    """J over even N (species 'n') or even Z ('p'); returns dict value -> J and the SEEN set (top NSEEN)."""
    J = {}
    lo, hi = N_RANGE if species == 'n' else Z_RANGE
    for k in range(lo, hi + 1, 2):
        drops = []
        for (z, n) in B:
            key = n if species == 'n' else z
            if key != k:
                continue
            a = (z, n)
            b = (z, n - 2) if species == 'n' else (z - 2, n)
            c = (z, n + 2) if species == 'n' else (z + 2, n)
            if b in B and c in B:
                drops.append((B[a] - B[b]) - (B[c] - B[a]))      # S_2 at k minus S_2 at k+2
        if len(drops) >= 3:
            J[k] = float(np.mean(drops))
    top = sorted(J, key=lambda k: -J[k])[:NSEEN]
    return J, sorted(top)


def s2():
    found, first_miss = s1()
    B = read_table()
    print(f"[ns1 S2] table read once: {len(B)} nuclides with A >= {AMIN}")
    tally = {}
    for sp, label in (('n', 'neutrons'), ('p', 'protons')):
        rng = N_RANGE if sp == 'n' else Z_RANGE
        J, S = seen(B, sp)
        box = [c for c in found if rng[0] <= c <= rng[1]]
        hits = [c for c in box if c in S]; misses = [c for c in S if c not in box]; false = [c for c in box if c not in S]
        tally[sp] = dict(hits=hits, misses=misses, false=false)
        print(f"[ns1 S2 {label}] SEEN closures (the {NSEEN} largest S_2 drops): {S}")
        print(f"[ns1 S2 {label}]   J at the box's closures: " + ', '.join(f"{c}: {J.get(c, float('nan')):+.2f} MeV" for c in box))
        print(f"[ns1 S2 {label}]   J at nature's magic numbers: " + ', '.join(f"{c}: {J.get(c, float('nan')):+.2f} MeV" for c in MAGIC if c in J))
        print(f"[ns1 S2 {label}]   hits {hits}; misses {misses}; false {false}")
    ok_match = all(len(t['misses']) == 0 and len(t['false']) <= 1 for t in tally.values())
    ok_partial = all(len(t['hits']) >= 3 for t in tally.values()) and first_miss == 28
    verdict = 'SHELLS-MATCH' if ok_match else ('SHELLS-PARTIAL' if ok_partial else 'SHELLS-FAIL')
    print(f"[ns1 S2] VERDICT: {verdict} (S1 first mismatch at {first_miss}; neutrons hits/misses/false "
          f"{len(tally['n']['hits'])}/{len(tally['n']['misses'])}/{len(tally['n']['false'])}; protons "
          f"{len(tally['p']['hits'])}/{len(tally['p']['misses'])}/{len(tally['p']['false'])})")
    return verdict


if __name__ == '__main__':
    if '--s2' in sys.argv:
        s2()
    else:
        s1()
