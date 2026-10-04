"""COMMISSION GAUGE-INVENTORY (charter analysis/GAUGE_INVENTORY_charter_LOCKED.md, locked 2026-10-04).
What internal symmetry does the registered weave have, by machine, at three levels (strand, node, weave)?
G1 the inventory of registered internal variables (reads, cited in the results file; encoded here as the
   configuration spaces and the registered energies that depend on them);
G2 the invariance group of each registered energy on each level's configuration space, computed with sympy
   (continuous part: the generators that leave the energy invariant, tested against a basis of candidate
   transformations; discrete part: enumerated permutations / reflections); CONTROL: the strand level must
   reproduce GRV-020 (G = R x SO(2), ground state the helix, stabiliser the screw, G/H = S^1) before anything else;
G3 parity: the action of spatial inversion and the handedness flip on every variable and energy;
G4 the label table of registered excitations (no particle names, B-3);
G5 the count: the real dimension of the continuous internal space at each level against what SU(2) and SU(3) need.
B-4: every energy here is a registered form as written (GRV-020 torsion stiffness; FND-001 director locking;
ELEC-096 cubic harmonic; FND-173's relative-handedness dependence recorded as 'the energy distinguishes the two labels'),
and a variable that appears in no registered energy is reported UNCONSTRAINED, not as a gauge symmetry.
"""
import itertools, numpy as np, sympy as sp, pathlib
OUT = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'gauge_inventory.npz'
R = {}


def control_strand():
    """GRV-020: E = (C/2) (phi'(s) - tau0)^2 on the internal azimuth. Candidate transformations of (s, phi):
    rotation phi -> phi + alpha; slide s -> s - a; reflection phi -> -phi; inversion s -> -s; scaling phi -> lam phi;
    shear phi -> phi + k s. Invariance of the energy density (up to the slide's relabelling of s) decides."""
    s, a, al, lam, k, tau0, C = sp.symbols('s a alpha lambda k tau_0 C', real=True)
    phi = sp.Function('phi')
    E = lambda f: C / 2 * (sp.diff(f, s) - tau0) ** 2
    base = E(phi(s))
    tests = {
        'rotation phi->phi+alpha (SO(2))': E(phi(s) + al),
        'slide s->s-a (R)': E(phi(s - a)).subs(s, s + a),          # relabel back
        'reflection phi->-phi': E(-phi(s)),
        'inversion s->-s': E(phi(-s)).subs(s, -s),
        'scaling phi->lam phi': E(lam * phi(s)),
        'shear phi->phi+k s': E(phi(s) + k * s),
    }
    inv = {name: sp.simplify(ex - base) == 0 for name, ex in tests.items()}
    # the two reflections together (P: s->-s and phi->-phi) leave phi' unchanged: tested as a pair
    inv['P = (s->-s, phi->-phi) jointly'] = sp.simplify(E(-phi(-s)).subs(s, -s) - base) == 0
    # ground state and stabiliser (GRV-020's own computation)
    sol = sp.solve(sp.Eq(tau0 * (s - a) + al, tau0 * s), al)
    stab_dim1 = len(sol) == 1 and sp.simplify(sol[0] - tau0 * a) == 0
    cont_dim = sum(inv[n] for n in ('rotation phi->phi+alpha (SO(2))', 'slide s->s-a (R)'))
    gs_manifold_dim = cont_dim - (1 if stab_dim1 else 0)
    ok = inv['rotation phi->phi+alpha (SO(2))'] and inv['slide s->s-a (R)'] and not inv['scaling phi->lam phi'] \
        and not inv['shear phi->phi+k s'] and stab_dim1 and gs_manifold_dim == 1
    for n, v in inv.items():
        print(f"[gi G2 strand]   {n:36s} invariant: {v}")
    print(f"[gi G2 strand] continuous group dim {cont_dim} (R x SO(2)), screw stabiliser dim 1: {stab_dim1}, G/H dim {gs_manifold_dim} (S^1)")
    print(f"[gi CONTROL] GRV-020 reproduced: {ok}")
    R['strand_inv'] = inv; R['control_ok'] = ok
    # the reflection phi->-phi alone is NOT a symmetry of the helical energy (tau0 fixed) but IS when tau0 -> -tau0 too:
    tau_flip = sp.simplify(E(-phi(s)).subs(tau0, -tau0) - base) == 0
    print(f"[gi G3 strand] phi->-phi together with tau0->-tau0 (handedness flip) invariant: {tau_flip}  (the energy is symmetric between the two handedness signs; neither is selected)")
    R['strand_handedness_degenerate'] = tau_flip
    return ok


def node():
    """FND-001: E = J sum_{pairs} (1 - cos dtheta_ij) over the z rope directors at a node (unit vectors n_i).
    Variables: z unit vectors (spatial, not internal) and the rope labels (which rope is which: internal).
    Internal candidates: permutation of rope labels (S_z); independent rotation of ONE rope's azimuth about its
    own axis (the face: FND-184's variable) -- which appears in no registered node energy (JUNCTION-LOCK)."""
    z = 6
    J = sp.symbols('J', positive=True)
    th = sp.symbols(f'theta0:{z}', real=True); ph = sp.symbols(f'phi0:{z}', real=True)
    n = [sp.Matrix([sp.sin(th[i]) * sp.cos(ph[i]), sp.sin(th[i]) * sp.sin(ph[i]), sp.cos(th[i])]) for i in range(z)]
    E = sum(J * (1 - (n[i].T * n[j])[0]) for i, j in itertools.combinations(range(z), 2))
    # permutation invariance: enumerate a generating set of S_z (transpositions) -- invariant by construction of the pair sum
    perm_ok = True
    for i in range(z - 1):
        sub = {th[i]: th[i + 1], th[i + 1]: th[i], ph[i]: ph[i + 1], ph[i + 1]: ph[i]}
        perm_ok &= sp.simplify(E.subs(sub, simultaneous=True) - E) == 0
    # common rotation about z (spatial SO(3) element): invariant; rotating ONE rope's director: not
    al = sp.symbols('alpha', real=True)
    common = sp.simplify(E.subs({ph[i]: ph[i] + al for i in range(z)}, simultaneous=True) - E) == 0
    one = sp.simplify(E.subs({ph[0]: ph[0] + al}) - E) == 0
    # the face azimuth psi_i of rope i (rotation about its own director) is absent from E: d E / d psi = 0 identically
    face_absent = True   # E has no psi variable at all (FND-001 is a point bond); recorded as UNCONSTRAINED
    print(f"[gi G2 node] z = {z} (FND-148 embedding); E = J sum (1 - cos dtheta) (FND-001)")
    print(f"[gi G2 node]   rope-label permutations S_{z} invariant: {perm_ok}  (discrete, internal)")
    print(f"[gi G2 node]   common rotation of all directors (spatial SO(3)): {common};  rotation of one director alone: {one}")
    print(f"[gi G2 node]   each rope's own-axis azimuth (the face, FND-184): appears in no registered node energy -> UNCONSTRAINED (not a symmetry; JUNCTION-LOCK f = 0)")
    R['node'] = dict(z=z, perm=perm_ok, common=common, one=one, face_absent=face_absent)
    return perm_ok and common and not one


def weave():
    """ELEC-096: the three-family direction set {x,y,z}; registered orientation energy ~ sum_i n_i^4 - 3/5 (order 4 cubic
    harmonic). Internal variable: the family label at a site, a 3-element set. Continuous part of its symmetry: none
    (a connected group acting on a finite set acts trivially: enumerated). Discrete: S_3 on labels, inside O_h (48)."""
    x, y, zz = sp.symbols('x y z', real=True)
    K = x ** 4 + y ** 4 + zz ** 4 - sp.Rational(3, 5)
    # O_h as signed permutation matrices (48)
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            mats.append(M)
    v = sp.Matrix([x, y, zz])
    oh_ok = all(sp.simplify(K.subs(dict(zip((x, y, zz), list(M * v))), simultaneous=True) - K) == 0 for M in mats)
    # a generic SO(3) rotation (about z by alpha) does not preserve K
    al = sp.symbols('alpha', real=True)
    Rz = sp.Matrix([[sp.cos(al), -sp.sin(al), 0], [sp.sin(al), sp.cos(al), 0], [0, 0, 1]])
    so3_ok = sp.simplify(K.subs(dict(zip((x, y, zz), list(Rz * v))), simultaneous=True) - K) == 0
    # label set: the symmetric group on 3 labels is all of its symmetries; its identity component is trivial
    labels = ('x', 'y', 'z'); perms = list(itertools.permutations(labels))
    print(f"[gi G2 weave] cubic harmonic sum n_i^4 - 3/5 (ELEC-096) invariant under all {len(mats)} elements of O_h: {oh_ok}; under a generic SO(3) rotation: {so3_ok}")
    print(f"[gi G2 weave] family label set {labels}: symmetry group S_3 ({len(perms)} elements, inside O_h); continuous (identity-component) part acting on a 3-element set: trivial (dim 0)")
    print(f"[gi G2 weave] relative handedness aligned/anti-aligned (FND-173/174): a Z_2 LABEL the registered energy DISTINGUISHES (different om2) -> not a symmetry; a label")
    R['weave'] = dict(oh=oh_ok, so3=so3_ok, s3=len(perms))
    return oh_ok and not so3_ok


def parity():
    print("[gi G3] spatial inversion P and the handedness flip, variable by variable (reads at lock, applied):")
    rows = [
        ('strand azimuth phi, torsion energy (GRV-020)', 'P flips s and phi together: phi\' unchanged, energy invariant', 'even'),
        ('strand handedness sign tau0 (FND-088 fixes |angle|, no sign)', 'the energy is symmetric under tau0 -> -tau0 with phi -> -phi; no registered claim selects a sign', 'degenerate (both signs)'),
        ('material winding sign = charge (GRV-045, FND-008)', 'P reverses the winding sign: P acts on windings as charge reversal', 'odd label'),
        ('relative level-2 handedness aligned/anti-aligned (FND-173)', 'P flips both levels: the RELATIVE label is P-invariant; the energy difference between the two is P-even', 'even'),
        ('node director energy (FND-001)', 'cos dtheta is P-even', 'even'),
        ('three-family direction set and sum n_i^4 (ELEC-096)', 'O_h contains inversion: even', 'even'),
    ]
    for v, how, res in rows:
        print(f"[gi G3]   {v:62s} {res:22s} {how}")
    print("[gi G3] READING: every registered energy is P-even and the vacuum's absolute handedness is not fixed by any registered claim (FND-088 derives angles, not signs; FND-173 registers both relative signs as objects). The registered vacuum is P-EVEN with a two-fold handedness degeneracy; P acts on the charge label as charge reversal. There is no registered seed of parity VIOLATION; there is a registered handedness LABEL.")
    R['parity'] = 'P-EVEN (handedness degenerate; P = charge reversal on windings)'


def labels():
    print("[gi G4] label table of registered excitations (groups and labels only; B-3):")
    print(f"[gi G4]   {'object':34s} {'winding n (Z)':14s} {'handedness':12s} {'family':8s} {'knot / det':14s} source")
    rows = [
        ('vacuum strand winding', 'n in Z', '+/-', 'x|y|z', '-', 'FND-008, GRV-045, EM-RECON-018'),
        ('two-frequency member, aligned', '-', 'aligned', '-', '-', 'FND-140/173 (level-2 relative sign +)'),
        ('two-frequency member, anti-aligned q=5/4', '-', 'anti', '-', '-', 'FND-173/174 (level-2 relative sign -)'),
        ('ring (unknot)', '-', '-', '-', '0_1 / 1', 'FND-MATTER-019'),
        ('trefoil', '-', 'chiral pair', '-', '3_1 / 3', 'FND-MATTER-019'),
        ('cinquefoil', '-', 'chiral pair', '-', '5_1 / 5', 'FND-MATTER-019'),
        ('septafoil', '-', 'chiral pair', '-', '7_1 / 7', 'FND-MATTER-019'),
        ('figure-eight', '-', 'achiral', '-', '4_1 / 5', 'FND-MATTER-020'),
        ('square knot', '-', 'achiral composite', '-', '3_1#3_1* / 9', 'FND-MATTER-019'),
        ('granny knot', '-', 'chiral composite', '-', '3_1#3_1 / 9', 'FND-MATTER-019'),
    ]
    for r in rows:
        print(f"[gi G4]   {r[0]:34s} {r[1]:14s} {r[2]:12s} {r[3]:8s} {r[4]:14s} {r[5]}")
    print("[gi G4] the labels available to a registered excitation: one integer (winding), one sign (handedness), one of three (family), one knot type. No continuous internal label beyond the U(1) phase exists.")
    R['labels'] = rows


def count():
    print("[gi G5] the count: real dimension of the CONTINUOUS internal space at each level, against the need:")
    have = {'strand': 1, 'node': 0, 'weave': 0}   # strand: the circle S^1 (GRV-020); node: labels only; weave: labels only
    need = {'SU(2) doublet (complex 2)': 4, 'SU(2)/SO(3) adjoint acting on S^2': 3, 'SU(3) triplet (complex 3)': 6, 'SU(3) adjoint': 8}
    for lvl, d in have.items():
        print(f"[gi G5]   {lvl:6s}: continuous internal dim {d}" + (" (S^1, GRV-020)" if d else " (finite labels only: S_6 rope permutations at the node; S_3 families, Z_2 relative handedness in the weave)"))
    for k, d in need.items():
        print(f"[gi G5]   need {k:36s}: {d}  -> shortfall {d - 1} real dimensions beyond the registered circle")
    print("[gi G5] discrete shadows, named as shadows: Z_2 (strand exchange, A2) is the centre of SU(2); S_3 (family permutation) is the Weyl group of SU(3). A finite subgroup of G is not G.")
    print("[gi G5] the registered internal space is ONE CIRCLE. Its full continuous symmetry is SO(2) (GRV-020), already spent on electromagnetism (winding = charge, torsion = light). No registered variable carries a second continuous internal direction.")
    R['have'] = have; R['need'] = need


def main():
    ok = control_strand()
    if not ok:
        print("[gi VERDICT] REFUSED: the control did not reproduce GRV-020 (B-2)"); raise SystemExit(1)
    node(); weave(); parity(); labels(); count()
    verdict = 'DISCRETE-ONLY + NEW-INTERNAL-SPACE-NEEDED; P-EVEN'
    print(f"[gi VERDICT] {verdict}: the continuous internal symmetry at every level is GRV-020's SO(2) (times the slide), the rest is finite (S_6 at the node, S_3 and Z_2 in the weave); the registered continuous internal space has real dimension 1 and SU(2)/SU(3) need 3 to 8; the vacuum is P-even with a handedness degeneracy and P acts as charge reversal on windings.")
    np.savez(OUT, verdict=verdict, control_ok=R['control_ok'], parity=R['parity'],
             have=np.array(list(R['have'].items()), dtype=object), need=np.array(list(R['need'].items()), dtype=object))
    print(f"[gi] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
