"""ROAD 1 check (executor, 2026-10-27): the exterior field of a winding does not know the core's size.
For a constraint source (EM-015), the braid phase outside the rope is a harmonic function with winding 1 about the
centreline: Phi(r, theta) = theta + const + sum_{m>=1} c_m (rho / r)^m sin(m theta + alpha_m). Its ISOTROPIC part is
exactly theta for any core shape or size (there is no m = 0 radial correction to a winding), and the anisotropic terms
carry the core's instantaneous orientation alpha_m = m Phi_0(s). Along a 2 pi kink the orientation Phi_0 sweeps a
full circle with the charge density dPhi/ds as weight, so every anisotropic term averages to zero:
int dPhi e^{i m Phi} = 0 for m >= 1. Numerically here: (1) the field of two half-windings at +-rho (the worst reading,
charge split onto the strands) averaged over the pair's orientation equals the point-winding field EXACTLY outside
rho (mean-value property); (2) the T-3 form factor J0(q rho) arises only from the region INSIDE rho, where the
split reading puts a potential the registered definition (phase about the common centreline, GRV-020 / ELEC-089)
does not have; with the singular line on the centreline the transverse form factor is 1 at every q."""
import math
import numpy as np
rho = 1.0
def phase_split(x, y, Phi0):            # half a winding on each strand at +-rho (e^{i Phi0} orientation)
    sx, sy = rho * math.cos(Phi0), rho * math.sin(Phi0)
    return 0.5 * (np.arctan2(y - sy, x - sx) + np.arctan2(y + sy, x + sx))
def point(x, y):
    return np.arctan2(y, x)
print('(1) exterior FIELD (grad Phi, single-valued) of the split reading, averaged over the pair orientation, against the point winding:')
Phis = np.linspace(0, 2 * math.pi, 720, endpoint=False)
def grad_split(x, y, Phi0):
    sx, sy = rho * math.cos(Phi0), rho * math.sin(Phi0)
    g = np.zeros(2)
    for cx, cy in ((sx, sy), (-sx, -sy)):
        dx, dy = x - cx, y - cy; r2 = dx * dx + dy * dy
        g += 0.5 * np.array([-dy, dx]) / r2
    return g
def grad_point(x, y):
    r2 = x * x + y * y; return np.array([-y, x]) / r2
for r in (1.05, 1.5, 3.0, 10.0):
    worst = 0.0
    for th in np.linspace(0.0, 2 * math.pi, 48, endpoint=False):
        x, y = r * math.cos(th), r * math.sin(th)
        avg = np.mean([grad_split(x, y, P) for P in Phis], axis=0); ref = grad_point(x, y)
        worst = max(worst, float(np.linalg.norm(avg - ref) / np.linalg.norm(ref)))
    print(f'    r = {r} rho: max relative |<E_split>_orientation - E_point| = {worst:.1e}')
print('    (exact outside rho by the mean-value property; inside r < rho the split reading differs, and the registered definition has no split)')
print('(2) the transverse form factor by source type (Born amplitude proportional to the Fourier transform of the potential):')
from scipy.special import j0
for qr in (0.2, 1.0, 4.1):
    print(f'    q rho = {qr}: coupling-source ring of charge (T-3\'s model) F = J0 = {j0(qr):+.3f};   constraint source on the centreline F = 1.000')
print('READ: T-3 scored the winding as a coupling source (charge at the strands); EM-015 says it is a constraint source and')
print('      GRV-020 / ELEC-089 put its singular line on the common centreline. Under the registered dictionary the EM form')
print('      factor of a 2 pi kink is F_par(q_par) alone; the transverse bound of FND-189 applies to the strands\' STRESS field')
print('      (the mass channel, gravitational-class), not to the charge.')
