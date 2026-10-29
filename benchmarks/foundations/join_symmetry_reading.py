"""JOIN-SYMMETRY reading (2026-10-29): what symmetry group a JOIN of registered strands carries.

The question, in the form Chain Theory (A. Wissner-Gross, October 2026) poses it: a gauge group can arise at a join as
the stabilizer of the joined state under the product of the local symmetry groups of the two ends (there, U(3) x U(2)
acting on a maximally entangled qutrit-qubit pair). The mesh's version: each strand's local internal group is the
azimuth SO(2) (FND-185, the only continuous internal symmetry; the rest finite), and the registered two-strand contact
(FND-184) is an energy on the two azimuths, period pi in each, flat lying preferred. The join's group is the subgroup of
SO(2) x SO(2) (x the strand swap, the strands being identical) that leaves the contact energy invariant.

Two contact forms are scored, the registered one and the one that WOULD carry a continuous phase at the join:
  (R) FND-184's form, separable, period pi in each azimuth:     V = -A [cos 2 phi_1 + cos 2 phi_2]  (flat lying preferred)
  (H) a hypothetical relative-azimuth contact (Josephson-like):  V = -A cos 2 (phi_1 - phi_2)
For each, the symmetry group is found by brute force on a fine grid of the torus (shifts (alpha, beta) and the swap), and
its identity component read off. No number is compared with measurement; the output is a group."""
import math, itertools, numpy as np

A = 1.0
def V_R(p1, p2): return -A * (np.cos(2 * p1) + np.cos(2 * p2))
def V_H(p1, p2): return -A * np.cos(2 * (p1 - p2))

def symmetries(V, n=96):
    """All torus shifts (alpha, beta) on an n x n grid, with and without the strand swap, leaving V invariant to 1e-12."""
    g = 2 * math.pi * np.arange(n) / n; P1, P2 = np.meshgrid(g, g, indexing='ij'); V0 = V(P1, P2)
    found = []
    for i, j in itertools.product(range(n), repeat=2):
        a, b = g[i], g[j]
        for swap in (False, True):
            Q1, Q2 = (P2 + a, P1 + b) if swap else (P1 + a, P2 + b)
            if np.max(np.abs(V(Q1, Q2) - V0)) < 1e-12:
                found.append((i, j, swap))
    return found, n

def describe(found, n):
    shifts = sorted({(i, j) for i, j, s in found if not s}); swaps = sorted({(i, j) for i, j, s in found if s})
    # identity component: is there a continuous one-parameter family of shifts? (consecutive grid shifts all present)
    cont = any(all(((i + k) % n, (j + k * dj) % n) in set(shifts) for k in range(n)) for (i, j) in shifts for dj in (-1, 0, 1) if (i, j) != (0, 0))
    return dict(n_shifts=len(shifts), n_with_swap=len(swaps), shifts_in_units_of_2pi_over_n=shifts[:8], continuous_component=cont)

if __name__ == '__main__':
    for name, V in (('R: registered contact, FND-184 form (separable, period pi each)', V_R), ('H: hypothetical relative-azimuth contact', V_H)):
        f, n = symmetries(V); d = describe(f, n)
        print(name)
        print(f"  invariant torus shifts on the {n}x{n} grid: {d['n_shifts']} (plus {d['n_with_swap']} with the strand swap); continuous one-parameter family: {d['continuous_component']}")
        if not d['continuous_component']:
            print(f"  shifts (units 2 pi / {n}): {d['shifts_in_units_of_2pi_over_n']}  -> the group is finite")
    print()
    print('READ: (R) the registered join keeps only the shifts by pi in each azimuth and the swap: (Z_2 x Z_2) x| Z_2, order 8,')
    print('      finite, abelian up to the swap; no continuous phase survives the join (both azimuth circles are broken by the contact).')
    print('      (H) a contact depending only on the RELATIVE azimuth would keep the common azimuth as a U(1) at the join; that U(1)')
    print('      is the pair\'s common azimuth, the Goldstone GRV-020 already spends on electromagnetism, and it is not registered')
    print('      as a contact form. No join of registered strands generates a continuous non-abelian group: the product of the')
    print('      ends\' groups is a torus, and a stabilizer inside a torus is abelian. FND-185\'s count stands at the join too.')
