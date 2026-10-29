"""THICK-ROPE-SYMMETRY reading (2026-10-29): the internal freedoms a rope of finite thickness carries beyond its azimuth,
and the symmetry group of each one's energy. The question (the author's, after the JOIN-SYMMETRY reading): the registered
strand's internal space has real dimension 1 (the azimuth, FND-185), but a rope is not a line; its cross-section can
deform, its core can sit off-centre, it carries twist, a bundle has the positions of its strands. Does thickness supply
the 3 (SU(2)) or 8 (SU(3)) internal dimensions FND-185 counts as missing, AND a non-abelian symmetry on them?

Method: for each internal freedom, its state space V, the transformations that act on V (rotations of the rope's local
frame about its tangent t, reflections, strand relabelings, and for a freedom not tied to the section the full SO(3) or
U(2)), and the subgroup that leaves a generic axis-respecting energy invariant, found NUMERICALLY by sampling random
states and random group elements. No number is compared with measurement; the output is a group per freedom."""
import math, numpy as np
rng = np.random.default_rng(7)

def rot(axis, th):
    a = axis / np.linalg.norm(axis); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + math.sin(th) * K + (1 - math.cos(th)) * K @ K

T = np.array([0.0, 0.0, 1.0])                      # the rope's tangent; the section is the xy plane

def invariant_generators(apply, energy, sample_state, acting, n_states=40):
    """Which one-parameter rotation subgroups of the ACTING group leave the energy invariant on sampled states.
    acting = 'axis' (rotations about the tangent only: all that acts on a freedom defined in the section, since a
    rotation tilting the section plane does not map the state space to itself) or 'so3' (a freedom not tied to the
    section). The stabilizer's Lie algebra is a subalgebra of so(3), so its dimension is 0, 1 or 3; it is read from the
    three basis generators (about t, x, y) and the diagonal (x + t) to catch a one-dimensional stabilizer off the axis."""
    states = [sample_state() for _ in range(n_states)]
    gens = {'t': T, 'x': np.array([1.0, 0, 0]), 'y': np.array([0, 1.0, 0]), 'x+t': np.array([1.0, 0, 1.0]) / math.sqrt(2)} if acting == 'so3' else {'t': T}
    inv = {}
    for k, ax in gens.items():
        inv[k] = all(abs(energy(apply(rot(ax, th), s)) - energy(s)) < 1e-9 for s in states for th in (1e-3, 0.37, 2.1))
    if acting == 'axis':
        return 'SO(2) about the tangent' if inv['t'] else 'finite only', 'rotations about the tangent (the section is defined by the axis)'
    if inv['x'] and inv['y'] and inv['t']:
        return 'SO(3)', 'all rotations'
    if inv['t'] or inv['x+t']:
        return 'SO(2) about the tangent' if inv['t'] else 'SO(2) off-axis', 'all rotations'
    return 'finite only', 'all rotations'

modes = []
# 1. the azimuth (registered): a unit vector in the section plane; E constant (GRV-020's Goldstone)
modes.append(('azimuth phi (registered)', 1, 'axis', lambda g, s: g @ s, lambda s: 0.0, lambda: np.array([math.cos(a := rng.uniform(0, 2 * math.pi)), math.sin(a), 0.0])))
# 2. elliptical section: a traceless symmetric 2x2 tensor in the plane (eps, psi); E = f(eps^2) (elastic)
def ell_state():
    e = rng.uniform(0, 0.3); p = rng.uniform(0, math.pi); Q = np.zeros((3, 3)); Q[:2, :2] = e * np.array([[math.cos(2 * p), math.sin(2 * p)], [math.sin(2 * p), -math.cos(2 * p)]]); return Q
modes.append(('elliptical section (eps, psi)', 2, 'axis', lambda g, Q: g @ Q @ g.T, lambda Q: float(np.sum(Q * Q)) + 0.3 * float(np.sum(Q * Q)) ** 2, ell_state))
# 3. core offset in the sheath: a vector u in the plane; E = f(|u|)
modes.append(('core offset u in the section', 2, 'axis', lambda g, u: g @ u, lambda u: float(u @ u) + 0.5 * float(u @ u) ** 2, lambda: np.array([*rng.normal(size=2) * 0.2, 0.0])))
# 4. the twist rate (a scalar along the axis): E = f(tau^2); nothing continuous acts on a scalar
modes.append(('twist rate tau (scalar)', 1, 'axis', lambda g, s: s, lambda s: float(s[0] ** 2), lambda: np.array([rng.normal() * 0.2, 0.0, 0.0])))
# 5. n strands at positions in the bundle's section: E = pairwise function of distances; the relabeling S_n is finite
def bundle_state():
    return rng.normal(size=(5, 3)) * np.array([0.3, 0.3, 0.0])
def bundle_E(P):
    D = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=2); return float(np.sum(D ** 2)) + float(np.sum(P ** 2))
modes.append(('5 strand positions in a bundle section', 10, 'axis', lambda g, P: P @ g.T, bundle_E, bundle_state))
# 6. two section amplitudes of DIFFERENT stiffness (the generic case for two modes): E = a x^2 + b y^2
modes.append(('two section amplitudes, different stiffness (x, y)', 2, 'axis', lambda g, s: g @ s, lambda s: 1.0 * s[0] ** 2 + 1.7 * s[1] ** 2, lambda: np.array([*rng.normal(size=2) * 0.2, 0.0])))
# 7. a 3D director d tied to the axis by its energy: E = f(d . t)  (a tilted core direction; acts: SO(3))
modes.append(('3D director d, energy depends on the tilt d.t', 2, 'so3', lambda g, d: g @ d, lambda d: float(d @ T) ** 2, lambda: (v := rng.normal(size=3)) / np.linalg.norm(v)))
# 8. a 3D director d BLIND to the axis: E = const (not registered; what SU(2)/Z2 would need)
modes.append(('3D director d, energy blind to the axis (hypothetical)', 2, 'so3', lambda g, d: g @ d, lambda d: 0.0, lambda: (v := rng.normal(size=3)) / np.linalg.norm(v)))

if __name__ == '__main__':
    print('freedom                                                 | dim | what acts on it                                            | connected symmetry of its energy')
    for name, dim, acting, apply, energy, samp in modes:
        grp, acts = invariant_generators(apply, energy, samp, acting)
        print(f'{name:56s}| {dim:3d} | {acts:58s} | {grp}')
    print()
    print('READ: every freedom a thick rope carries IN ITS SECTION (ellipticity, core offset, twist, strand positions in a bundle,')
    print('      any number of section amplitudes) has an energy whose only continuous symmetry is the rotation about the tangent,')
    print('      SO(2), the same circle as the azimuth; two section amplitudes of unequal stiffness have none at all. Thickness raises')
    print('      the DIMENSION count (two per section mode) and never the symmetry: rotations about one axis commute. A non-abelian')
    print('      group needs an internal freedom whose energy is blind to the rope\'s axis (the hypothetical director: SO(3) = SU(2)/Z2),')
    print('      which no geometric mode of the section is, because the section is defined by the axis. That freedom would be a new')
    print('      internal field with its own registered energy: FND-185\'s price, in rope language.')
