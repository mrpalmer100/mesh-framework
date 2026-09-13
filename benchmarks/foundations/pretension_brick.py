"""THIRD BRICK -- the vector pretension instrument.

Charter: analysis/TOPOLOGY_pretension_charter_LOCKED.md (bars
locked before this file computed anything). Reuses the network
builder from the coordination brick. Linearized pretensioned
dynamical matrix per bond:
  K_bond = k b b^T + (T0/L) (I - b b^T),  k = m = a = 1,
  tau = T0/(k a) the single shared control.
Checkpoint: /tmp/pret_ckpt.pkl.
"""
import numpy as np
import pickle
import pathlib
import sys
import scipy.sparse as sp

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from coordination_brick import cubic_network  # noqa: E402

CKPT = pathlib.Path('/tmp/pret_ckpt.pkl')


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def load():
    if CKPT.exists():
        return pickle.loads(CKPT.read_bytes())
    return {}


def vector_K(pos, bonds, tau):
    """Sparse 3n x 3n linearized stiffness for unit springs with
    uniform tension tau (T0/L with L = bond length; on the unit
    cubic lattice L = a = 1 for lattice bonds; the pendant bond
    uses its own L)."""
    n = len(pos)
    rows, cols, vals = [], [], []
    for (i, j) in bonds:
        d = pos[j] - pos[i]
        L = np.linalg.norm(d)
        b = d / L
        Kb = np.outer(b, b) + (tau / L) * (np.eye(3)
                                           - np.outer(b, b))
        for a_ in range(3):
            for c_ in range(3):
                v = Kb[a_, c_]
                if v == 0.0:
                    continue
                rows += [3 * i + a_, 3 * j + a_,
                         3 * i + a_, 3 * j + a_]
                cols += [3 * i + c_, 3 * j + c_,
                         3 * j + c_, 3 * i + c_]
                vals += [v, v, -v, -v]
    K = sp.coo_matrix((vals, (rows, cols)),
                      shape=(3 * n, 3 * n)).tocsr()
    return K


def v1_classify(z=6.0, tau=1.0, L=33, seed=0, omega=None,
                steps=460, dt=0.16, tag=None):
    """V1: transverse drive at the center; Fourier-projected steady
    transverse amplitude; p_dyn fit on the annulus + front speed.
    Identical at every (z, tau) per the locked bar."""
    # INSTRUMENT AMENDMENT (2026-08-26, daylight, justified on the
    # PRISTINE z=6 tau=0.02 row): a fixed drive frequency falls
    # ABOVE the transverse band as tau shrinks (band top ~
    # 2*sqrt(tau)*..., 0.49 < 0.5236 at tau=0.02), so the fixed-
    # omega instrument measured evanescent decay, not medium-vs-
    # localization. Drive at FIXED WAVENUMBER instead:
    # omega = k0 * c_T(tau), c_T = sqrt(tau) (pristine transverse
    # speed), k0 = 0.5236 -- the same wavelength inside every
    # cell's own band. tau- but never z-dependent; identical for
    # every network at a given tau (no rescue). dt scales with the
    # period for constant resolution.
    if omega is None:
        omega = 0.5236 * np.sqrt(tau)
        # dt stays governed by the tau-independent longitudinal band
    st = load()
    key = tag or f'v1-z{z}-t{tau}-L{L}-s{seed}'
    if key in st:
        return st[key]
    pos, bonds, _ = cubic_network(L, None if z >= 6 else z, seed)
    n = len(pos)
    K = vector_K(pos, bonds, tau)
    ctr = np.array([L // 2] * 3, dtype=float)
    src = int(np.argmin(((pos - ctr) ** 2).sum(1)))
    r = np.sqrt(((pos - pos[src]) ** 2).sum(1))
    R = L // 2
    sponge3 = np.repeat(
        np.clip((r - (R - 5.0)) / 5.0, 0.0, 1.0) ** 2 * 0.9, 3)
    u = np.zeros(3 * n)
    v = np.zeros(3 * n)
    arr = np.full(n, -1.0)
    per = 2 * np.pi / omega
    t0 = steps * dt - 2.0 * per
    cs = np.zeros(3 * n)
    sn = np.zeros(3 * n)
    nsamp = 0
    di = 3 * src + 2          # drive along z-hat (transverse pol)
    for kstep in range(steps):
        t = kstep * dt
        a = -K.dot(u) - sponge3 * v
        a[di] += np.sin(omega * t)
        v += dt * a
        u += dt * v
        w = np.abs(u[2::3])
        newly = (arr < 0) & (w > 1e-3)
        arr[newly] = t
        if t >= t0:
            cs += u * np.cos(omega * t)
            sn += u * np.sin(omega * t)
            nsamp += 1
    amp = 2.0 * np.sqrt(cs ** 2 + sn ** 2) / max(nsamp, 1)
    env = amp[2::3]           # transverse (drive-parallel) channel
    lo, hi = 6.0, R - 7.0
    # AMENDMENT 3 (2026-08-26, daylight, pristine-row justified): at
    # low tau the lattice is STRONGLY anisotropic for a z-polarized
    # source (u_z rides the stiffness-1 longitudinal channel along
    # the z-columns at c = 1, but the tension channel at sqrt(tau)
    # in the equatorial plane). Spherical-shell medians over a 7:1
    # anisotropic field produce meaningless exponents (measured:
    # p ~ 4 on the PRISTINE lattice). The transverse-membership
    # classifier therefore reads the EQUATORIAL annulus
    # (|dz| <= 2), where propagation is purely tension-borne;
    # the axial/equatorial contrast is physics, reported separately.
    dz = np.abs(pos[:, 2] - pos[src, 2])
    ann = ((r >= lo) & (r <= hi) & (np.arange(n) != src)
           & (dz <= 2.0))
    rb = np.round(r[ann]).astype(int)
    med_r, med_e = [], []
    for rv in np.unique(rb):
        med_r.append(rv)
        med_e.append(np.median(env[ann][rb == rv]))
    med_r = np.array(med_r, float)
    med_e = np.array(med_e)
    ok = med_e > 0
    P = np.polyfit(np.log(med_r[ok]), np.log(med_e[ok]), 1)
    p_dyn = -float(P[0])
    fa = ann & (arr > 0)
    c = float(np.polyfit(arr[fa], r[fa], 1)[0]) if fa.sum() > 30 \
        else 0.0
    # AMENDMENT 4 (2026-08-26, daylight): DIFFERENTIAL classifier.
    # At low tau the pristine medium itself is anisotropic (leaky
    # equatorial slab mode), so an absolute p ~ 1 bar presumes an
    # isotropy the physics lacks. Each (z, tau) is judged against
    # the PRISTINE z = 6 row at the SAME tau (the calibration row
    # as reference): MEDIUM iff |p - p_ref| <= 0.3 AND
    # c >= 0.4 c_ref. z-blind; reduces to the absolute bar at
    # tau = 1.
    stt = load()
    ref = None
    for kk, vv in stt.items():
        if (isinstance(vv, dict) and vv.get('z') == 6.0
                and vv.get('tau') == tau and vv.get('L') == L):
            ref = vv
    if z >= 6 or ref is None:
        cls = ('MEDIUM' if (c > 0.05 and p_dyn < 6.0)
               else 'LOCALIZING') if z >= 6 else 'UNREFERENCED'
    else:
        cls = ('MEDIUM' if (abs(p_dyn - ref['p_dyn']) <= 0.3
                            and c >= 0.4 * ref['c'])
               else 'LOCALIZING')
    res = dict(z=z, tau=tau, L=L, p_dyn=p_dyn, c=c, cls=cls,
               ref=(None if ref is None else
                    [ref['p_dyn'], ref['c']]))
    st[key] = res
    save(st)
    return res


if __name__ == '__main__':
    import itertools
    print('== THIRD BRICK V4 calibration + V2 map ==')
    order = [(6.0, 1.0)] + [
        (z, t) for t, z in itertools.product(
            (1.0, 0.3, 0.02), (4.0, 3.5, 3.0, 5.0))
        if (z, t) != (6.0, 1.0)]
    for z, t in order:
        r = v1_classify(z=z, tau=t)
        print(f"  z={z} tau={t}: p_dyn = {r['p_dyn']:.3f}  "
              f"c = {r['c']:.3f}  [{r['cls']}]")

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

