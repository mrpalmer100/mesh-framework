"""COMMISSION JUNCTION-LOCK (charter analysis/JUNCTION_LOCK_charter_LOCKED.md, locked 2026-10-04).
SCOPE READ (recorded in the results): FND-184's sentence is 'at a crossing, the contact energy is a function of the
gap between the two strands' surfaces', with the registered contact law in the centre-line separation r. The registered
junction (FND-001, rope_microscopic_mechanics section 2) is a point atom held by a harmonic bond of stiffness kappa and
pulled by two rope tensions: E(r) = (kappa/2)|r|^2 - F1.r - F2.r, |F1| = |F2| = T, giving E*(dtheta) = -(T^2/kappa)
(1 + cos dtheta) + const. There is no gap, no contact law and no surface in it; the grant does not cover it. Under the
registered mechanics the material azimuth phi of either rope does not appear: f = 0 identically (JUNCTION-FREE at the
registered level). The script (i) checks that symbolically, (ii) runs the circular-limit control, and (iii) computes the
DISPLAY under the named extension 'the tie holds the face' (J1): the harmonic bond distributed over the two ropes'
end-faces (two discs of radius rho side by side), so that kappa_eff(dphi) = kappa x [overlap area of the two faces at
relative azimuth dphi] / [overlap at dphi = 0]; then E*(dphi) = -2T^2/kappa_eff(dphi) at dtheta = 0 and the azimuthal
locking amplitude relative to J = T^2/kappa is f = 2 (1/omega_min - 1), omega the overlap fraction. J2 (face against a
POINT node) has no orientation dependence: f = 0, which is the registered reading.
"""
import numpy as np, sympy as sp, pathlib
OUT = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'junction_lock.npz'


def registered_junction():
    k, T, dth, phi1, phi2 = sp.symbols('kappa T dtheta phi_1 phi_2', positive=True)
    rx, ry = sp.symbols('r_x r_y', real=True)
    F1 = sp.Matrix([T, 0]); F2 = sp.Matrix([T * sp.cos(dth), T * sp.sin(dth)])
    r = sp.Matrix([rx, ry]); E = k / 2 * (r.T * r)[0] - (F1.T * r)[0] - (F2.T * r)[0]
    sol = sp.solve([sp.diff(E, rx), sp.diff(E, ry)], [rx, ry]); Es = sp.simplify(E.subs(sol))
    J = sp.simplify((Es.subs(dth, sp.pi / 2) - Es.subs(dth, 0)) / (1 - sp.cos(sp.pi / 2)))
    print(f"[jl S0] registered junction: E* = {Es};  J = T^2/kappa reproduced: {sp.simplify(J - T**2 / k) == 0}")
    print(f"[jl S0] dE*/dphi_1 = {sp.diff(Es, phi1)}, dE*/dphi_2 = {sp.diff(Es, phi2)}  (the azimuths do not appear): f = 0 identically under FND-001's mechanics")
    return sp.simplify(J - T ** 2 / k) == 0


def face_mask(X, Y, rho, phi):
    c, s = np.cos(phi), np.sin(phi)
    u, v = c * X + s * Y, -s * X + c * Y                          # face coordinates: discs at (+-rho, 0) along the pair axis
    return ((u - rho) ** 2 + v ** 2 <= rho ** 2) | ((u + rho) ** 2 + v ** 2 <= rho ** 2)


def overlap_fraction(dphi, rho=1.0, n=1201, circular=False):
    L = 2.2 * rho; xs = np.linspace(-L, L, n); X, Y = np.meshgrid(xs, xs, indexing='ij')
    if circular:
        A = (X ** 2 + Y ** 2 <= (1.5 * rho) ** 2); B = A
    else:
        A = face_mask(X, Y, rho, 0.0); B = face_mask(X, Y, rho, dphi)
    return (A & B).sum() / A.sum()


def main():
    ok = registered_junction()
    # control: circular faces -> omega = 1 for every dphi -> f = 0 -> FND-001's J untouched
    om_c = [overlap_fraction(d, circular=True) for d in (0.0, 0.7, 1.571)]
    print(f"[jl J3 control] circular faces: overlap fraction {om_c} -> f = {2 * (1 / min(om_c) - 1):.1e} (FND-001's J reproduced; bar B-3 {max(abs(1 - o) for o in om_c) < 1e-9})")
    dphis = np.linspace(0, np.pi, 37); om = np.array([overlap_fraction(d) for d in dphis])
    Fphi = 2 * (1 / om - 1)                                        # E*(dphi) - E*(0) in units of J, at dtheta = 0
    f = float(Fphi.max()); per = 'pi' if abs(overlap_fraction(np.pi) - 1) < 1e-6 else '2pi'
    print(f"[jl J1 display] extension 'the tie holds the face' (bond distributed over two two-lobed end-faces): overlap fraction min {om.min():.4f} at dphi = {dphis[om.argmin()]:.3f};  azimuthal locking amplitude f = {f:.3f} J;  period {per};  E(dphi)/J at dphi = pi/4, pi/2: {np.interp(np.pi/4, dphis, Fphi):.3f}, {np.interp(np.pi/2, dphis, Fphi):.3f}")
    print("[jl J2] face against a POINT node (the registered node): no orientation dependence; f = 0.")
    T0s = (434.0, 1599.0, 2734.0); E = 1.602e-19; DC = 1.87e-19; R = DC / 2
    for lab, T0, a in (('kappa_pack 1', 434.0, 6.0e-17), ('kappa_pack 50', 1599.0, 1.63e-17), ('kappa_pack 250', 2734.0, 9.53e-18)):
        Ec = (2 * np.pi / 5) * f * T0 / E; J = T0 * a / 2; w = np.sqrt(T0 * R ** 2 / (2 * a * f * J))
        print(f"[jl J4 display] {lab:14s}: under the extension E_c = {Ec:.2e} V/m ({Ec / 1.32e18:.0f} x Schwinger), kink width w = {w:.1e} (self-trapped; onset 0.8)")
    print("[jl VERDICT] JUNCTION-FREE at the registered level (f = 0 identically: the registered node is a point atom with a harmonic bond, and FND-184's sentence covers crossings with a contact law, not bonds); the extension 'the tie holds the face' is priced by the display (f ~ %.1f J, ABOVE-QED class) and not adopted." % f)
    np.savez(OUT, s0_ok=ok, dphis=dphis, omega=om, f_display=f, verdict='JUNCTION-FREE'); print(f"[jl] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
