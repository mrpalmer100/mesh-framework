"""COMMISSION NUC-SHELL-2 -- a PRICE on the mode path's torsion: does the registered box, split by ORBIT-TWIST's one
handedness-times-sense term, close at nature's magic numbers for any torsion in the physical range?
Charter analysis/NUC_SHELL_2_charter_LOCKED.md. No data is read; no fit: the whole scan is the result.

The ladder is NUC-SHELL-1's (the infinite spherical box, levels x_nl^2 in units of hbar^2/(2 m_N R^2), degeneracy
2(2l+1)). ORBIT-TWIST's M2 term shifts a mode's wavenumber by sigma tau (sigma = +/-1 the handedness, tau the torsion
of the mode's path); for the massive dispersion e = hbar^2 k^2 / 2m that is an energy shift
    Delta e = hbar^2 k tau / m = 2 x (tau R)  in the box's units,
proportional to the level's x (not flat in energy, though flat in l at fixed k). Applied to each level with l >= 1 as
the j = l + 1/2 member (degeneracy 2l + 2) lowered by Delta/2 and the j = l - 1/2 member (degeneracy 2l) raised by
Delta/2 (the sign that closes 28 is the one tested; the opposite sign is scanned too and reported). l = 0 levels
(degeneracy 2) are not split. The scan: tau R from 0 to 2.0 in steps of 0.02. At each tau R the closures are read by
NUC-SHELL-1's locked rank rule (the bottom plus the six largest gap ratios at cumulative occupancy <= 184) and
compared with 2, 8, 20, 28, 50, 82, 126.
Verdict forms (locked): PRICE-FOUND   some tau R in [0, 2] gives all seven magic numbers as the well's closures:
                                      the price is that tau R (the range reported), on the record as the mode path's
                                      torsion the magic numbers demand;
                        PRICE-PARTIAL the best tau R gives 2, 8, 20, 28 (the first four) but not all seven;
                        PRICE-NONE    no tau R gives 28 at all: the flat-in-l form cannot close the first missing
                                      shell and the l-scaling itself is the missing physics.
Prior (stated, not leaned on): PRICE-PARTIAL. A splitting that grows with k but not with l may bring 1f7/2 down to
close 28 and 1g9/2 to close 50, but the heavier closures need the intruder from the next shell (1h11/2, 1i13/2) to
drop by a shell spacing, which a term flat in l at fixed k is unlikely to do for all of them at one tau R.
Usage: python benchmarks/nuclear/nuc_shell_2.py [--control]
"""
import json, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'nuclear'))
import nuc_shell_1 as S1                                   # the locked ladder and rank rule

MAGIC = [2, 8, 20, 28, 50, 82, 126]
TAUS = np.round(np.arange(0.0, 2.0001, 0.02), 2)


def split_ladder(tauR, sign=+1):
    """the box ladder with ORBIT-TWIST's term: Delta = 2 x tauR per level; j = l + 1/2 lowered for sign = +1."""
    lev = []
    for x2, g, lab in S1.LAD:
        l = (g // 2 - 1) // 2
        x = np.sqrt(x2); d = 2 * x * tauR
        if l == 0:
            lev.append((x2, 2, lab))
        else:
            lev.append((x2 - sign * d / 2, 2 * l + 2, lab + '+'))
            lev.append((x2 + sign * d / 2, 2 * l, lab + '-'))
    lev.sort()
    merged = []                                            # degenerate members (e.g. at tau R = 0) are one level for the rank rule
    for x2, g, lab in lev:
        if merged and abs(x2 - merged[-1][0]) < 1e-9:
            merged[-1] = (merged[-1][0], merged[-1][1] + g, merged[-1][2].rstrip('+-'))
        else:
            merged.append((x2, g, lab))
    return merged


def closures_of(lad):
    return [c for c, *_ in S1.closures(lad=lad)]


def main():
    if '--control' in sys.argv:
        c0 = closures_of(split_ladder(0.0))
        print(f"[ns2 control] tau R = 0: closures {c0} (NUC-SHELL-1's 2, 8, 20, 34, 58, 92, 138 expected)")
        return
    rows = []
    for sign, name in ((+1, 'j=l+1/2 lower'), (-1, 'j=l+1/2 higher')):
        for t in TAUS:
            cl = closures_of(split_ladder(float(t), sign))
            hits = [m for m in MAGIC if m in cl]
            rows.append(dict(sign=name, tauR=float(t), closures=cl, hits=hits, n_hits=len(hits), first_four=all(m in cl for m in MAGIC[:4])))
    (ROOT / 'analysis' / 'nuc_shell_2_scan.json').write_text(json.dumps(rows, indent=1))
    for sign in ('j=l+1/2 lower', 'j=l+1/2 higher'):
        sub = [r for r in rows if r['sign'] == sign]
        best = max(sub, key=lambda r: (r['n_hits'], -r['tauR']))
        print(f"[ns2 {sign}] best tau R = {best['tauR']:.2f}: closures {best['closures']}, hits {best['hits']} ({best['n_hits']}/7)")
        found = [r['tauR'] for r in sub if r['n_hits'] == 7]
        four = [r['tauR'] for r in sub if r['first_four']]
        has28 = [r['tauR'] for r in sub if 28 in r['closures']]
        print(f"[ns2 {sign}]   tau R with all seven: {found if found else 'none'}; with the first four (2, 8, 20, 28): "
              f"{(f'{min(four):.2f} to {max(four):.2f}' if four else 'none')}; with 28 at all: {(f'{min(has28):.2f} to {max(has28):.2f}' if has28 else 'none')}")
        # the closures as tau R moves, every 0.2
        for r in sub:
            if abs(r['tauR'] * 5 - round(r['tauR'] * 5)) < 1e-9:
                print(f"[ns2 {sign}]     tau R {r['tauR']:.2f}: {r['closures']}  hits {r['n_hits']}")
    pos = [r for r in rows if r['sign'] == 'j=l+1/2 lower']
    if any(r['n_hits'] == 7 for r in pos):
        v = 'PRICE-FOUND'
    elif any(r['first_four'] for r in pos):
        v = 'PRICE-PARTIAL'
    else:
        v = 'PRICE-NONE'
    print(f"[ns2] VERDICT: {v} (sign that closes 28: j = l + 1/2 lower)")
    return v


if __name__ == '__main__':
    main()
