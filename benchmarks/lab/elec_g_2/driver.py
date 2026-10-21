"""ELEC-G-2 driver: a CONDITIONAL second-moment ratio diagnostic of the committed rotating terminus (the ratio of two
second moments, which equals a gyromagnetic ratio only under two named, unregistered current laws; see the charter).

Charter: analysis/ELEC_G_2_charter_LOCKED.md (drafted at analysis/lab/drafts/ELEC-G-2/charter.md).
Built on benchmarks/lab/_kit/labkit.py (Driver): one unit per invocation, atomic resumable checkpoint, manifest
binding, sealed raw outputs, any exception a recorded HALT followed by the terminal line.

Units, in order:
  credential   v3: the PRODUCTION MOMENT PATH (dense profile, spline, moment quadrature, g assembly) on three
               closed-form profiles, no solver and no data involved.
  solve_1..5   one BVP solve of the chain's EL-BVP solver per unit (the adjudicating run first), each solution's
               arrays (mesh r, f, f', the solver's cumulant) sealed with the solver's success flag and status.
  moments      v1, v2 from the seals; every moment and every g from the sealed arrays only, all five runs
               collected before any is published; the verdict recomputes all of it from the seals.

The solver file (explorations/w_dressing_phase1c.py) ends with an unconditional main() call, so importing it would
run the chain's five solves as a side effect. The driver therefore executes the file's source with that single
final call removed, in a private namespace; every function the solver defines (solve_el, rhs, bcs, lbfgs_guess,
elastic_density) runs unchanged, and the solver's own solve_bvp result is captured by a pass-through wrapper so the
arrays are sealed. The file's bytes are in the manifest.

Smoke (LAB_SMOKE=1): the same units on a SYNTHETIC FIXTURE that is not a charter cell: the same solver run at
k/T0 = 3 and x* = e^2 (not the registered k/T0 = 2, x* = e^(pi^2)), r_min and tol values not among the five evidence
cells, a coarser L-BFGS guess grid. It writes analysis/elec_g_2_smoke.pkl, reads nothing under data/ and never the
evidence checkpoint. v1 is skipped on the fixture (it has no chain number to reproduce).

BAR DERIVATIONS (v3, 1e-8). The three closed-form profiles are on a geometric grid of N = 2001 points on [a, R]
(a = 1e-3), ratio step delta = ln(R/a)/(N-1) <= 9.0/2000 = 4.5e-3. (i) f = r and (ii) f = r + 0.1 r^3 are cubic
polynomials, which the cubic Hermite spline reproduces exactly; their integrands (r^3 times degree <= 6) have degree
<= 9, which the 5-point Gauss-Legendre rule integrates exactly; the only error is rounding (~1e-13). (iii) f =
exp(-r^2/2): Hermite interpolation error <= h^4 |f''''| / 384 with h = delta r, so the relative error is at most
delta^4/384 * max(r^4 |f''''| / f) over the weighted region, 4.1e-10/384 * ~2.4e3 ~ 3e-9 at r = 3 where the weight
exp(-r^2) is 1e-4, and below 1e-11 integrated. The bar 1e-8 therefore sits about three orders above the expected
truncation and rounding, and is not tuned to any run.
"""
import os
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                 # noqa: E402

SLUG = 'elec_g_2'
SOLVER = 'explorations/w_dressing_phase1c.py'
MANIFEST = ['benchmarks/lab/_kit/labkit.py', SOLVER,
            'benchmarks/lab/elec_g_2/driver.py', 'benchmarks/lab/elec_g_2/verdict.py']
PI = float(np.pi)

CONFIG = dict(
    k_over_T0=2.0,
    # (r_min, tol); the first is the adjudicating run (the chain's r_min 1e-3, tol 1e-10 cell)
    runs=[[1e-3, 1e-10], [1e-3, 1e-6], [1e-3, 1e-8], [1e-4, 1e-8], [3e-4, 1e-8]],
    D_E_chain=1.1051029, v1_tol_abs=1e-6,          # v1: D_E reproduced on the adjudicating run
    v2_norm_tol_rel=1e-8,                          # v2: Omega * (solver cumulant) = J_T, every run
    v2_quad_tol_rel=1e-6,                          # v2b: production quadrature of Int f^2 dA vs the cumulant, adjudicating run
    v3_tol_rel=1e-8, v3_n=2001, v3_a=1e-3, v3_R_poly=7.0, v3_R_gauss=8.0, v3_omega=0.3, v3_k=2.0,
    gl_order=5,
    d2_tol_abs=1e-5,                               # D2 floor: absolute range (max - min) of each scored g across the five
                                                   # runs; 50 times below the 5e-4 band half-width at every g
    band_abs=5e-4,                                 # D3: a form fires when |g - value| <= band
    g_dirac=2.0, g_classical=1.0, g_pi_dirac=2.0 * PI,
    q2_match_rel=5e-4,                             # Q2: a factor candidate matches when |F / c - 1| <= this
    q2_candidates=[['pi', PI], ['1/pi', 1.0 / PI], ['pi/2', PI / 2], ['2/pi', 2.0 / PI], ['2pi', 2 * PI],
                   ['pi/4', PI / 4], ['4/pi', 4.0 / PI]],
    # smoke fixture (synthetic, not a charter cell)
    smoke_k=3.0, smoke_lnx=2.0, smoke_guess_n=300, smoke_n_mesh=400,
    smoke_runs=[[1e-2, 1e-4], [1e-2, 1e-5], [5e-3, 1e-5], [5e-3, 1e-4], [2e-2, 1e-5]],
)
VARIANTS = ('full', 'elastic', 'chain')            # full = elastic + rotational (the reading); the others sensitivities


# ----------------------------------------------------------------------------------------------- the solver
def load_solver(fixture=False):
    """A private namespace holding the solver's functions (its final main() call removed). fixture=True overrides the
    module constants to the smoke fixture (k and x* differ from the registered ones) and coarsens the guess grid."""
    path = ROOT / SOLVER
    lines = path.read_text().rstrip().splitlines()
    K.require(lines[-1].strip() == 'main()', 'solver file does not end with the expected main() call')
    ns = {'__name__': 'w_dressing_phase1c_nomain'}
    exec(compile('\n'.join(lines[:-1]) + '\n', str(path), 'exec'), ns)
    for name in ('solve_el', 'rhs', 'bcs', 'lbfgs_guess', 'elastic_density', 'XSTAR', 'OMEGA', 'JT', 'NORM_TARGET'):
        K.require(name in ns, f'solver namespace lacks {name}')
    captured = []
    real = ns['solve_bvp']

    def capture(*a, **kw):
        sol = real(*a, **kw)
        captured.append(sol)
        return sol
    ns['solve_bvp'] = capture
    ns['_captured'] = captured
    if fixture:
        x = float(np.exp(CONFIG['smoke_lnx']))
        ns['XSTAR'] = x
        ns['JT'] = PI ** 2 * (x ** 2 - 1.0) / x
        ns['OMEGA'] = PI / x
        ns['NORM_TARGET'] = ns['JT'] / ns['OMEGA']
        orig = ns['lbfgs_guess']
        ns['lbfgs_guess'] = lambda k, n, r_min, lam_pen=1e4: orig(k, CONFIG['smoke_guess_n'], r_min, lam_pen)
    else:
        K.require(abs(ns['XSTAR'] - float(np.exp(PI ** 2))) < 1e-9 * ns['XSTAR'], 'solver x* is not e^(pi^2)')
        K.require(abs(ns['OMEGA'] - PI / ns['XSTAR']) < 1e-15, 'solver Omega is not pi / x*')
    return ns


# ------------------------------------------------------------------------- the production moment path
def eps_fn_physical(ns, k, omega, variant):
    """The energy density as a function of (x, f, f'): elastic (the solver's own elastic_density) plus rotational
    0.5 Omega^2 f^2 ('full', the reading); 'elastic' excludes the rotational density; 'chain' is the D_E numerator's
    density, elastic + rotational - f^2 / (2 x^2) (the LOG term subtracted)."""
    elastic = ns['elastic_density']

    def eps(x, f, fp):
        g2 = fp ** 2 + (f / x) ** 2
        el = elastic(g2, k)
        if variant == 'full':
            return el + 0.5 * omega ** 2 * f ** 2
        if variant == 'elastic':
            return el
        if variant == 'chain':
            return el + 0.5 * omega ** 2 * f ** 2 - f ** 2 / (2.0 * x ** 2)
        raise K.Halt(f'unknown variant {variant}')
    return eps


def dense_profile(r, f, fp):
    """The dense profile: the cubic Hermite spline through the sealed (r, f, f'), the form of solve_bvp's own
    interpolant."""
    from scipy.interpolate import CubicHermiteSpline
    r, f, fp = (K.finite_array(a, n) for a, n in ((r, 'r'), (f, 'f'), (fp, 'fp')))
    K.require(np.all(np.diff(r) > 0), 'mesh r is not strictly increasing')
    return CubicHermiteSpline(r, f, fp)


def quad_area(spl, r, integrand, order=None):
    """Int integrand(x, f, f') dA over [r[0], r[-1]], dA = 2 pi x dx, composite Gauss-Legendre per mesh interval on the
    dense profile."""
    order = CONFIG['gl_order'] if order is None else order
    nodes, wts = np.polynomial.legendre.leggauss(order)
    a, b = r[:-1, None], r[1:, None]
    half, mid = 0.5 * (b - a), 0.5 * (b + a)
    x = mid + half * nodes[None, :]
    f, fp = spl(x), spl(x, 1)
    vals = integrand(x, f, fp) * 2.0 * PI * x
    return K.finite(np.sum(half * wts[None, :] * vals), 'quadrature')


def g_assembly(Iq0, Iq2, Ie0, Ie2, omega):
    """g_mech = (mu / L)(2 m / q): mu = (Omega / 2) Iq2, L = Omega Ie2 (c = 1), m = Ie0, q = Iq0."""
    mu, L, m, q = 0.5 * omega * Iq2, omega * Ie2, Ie0, Iq0
    K.require(L != 0.0 and q != 0.0, 'zero angular momentum or charge in g assembly')
    return K.finite((mu / L) * (2.0 * m / q), 'g')


def moments(r, f, fp, eps_fn, omega, rstar):
    """Every moment and both g readings from (r, f, f') arrays. Reading A: charge at the edge, <r^2>_q = R*^2 (unit
    charge). Reading B: rho_q proportional to f^2."""
    spl = dense_profile(r, f, fp)
    Ie0 = quad_area(spl, r, eps_fn)
    Ie2 = quad_area(spl, r, lambda x, f_, fp_: eps_fn(x, f_, fp_) * x ** 2)
    If0 = quad_area(spl, r, lambda x, f_, fp_: f_ ** 2)
    If2 = quad_area(spl, r, lambda x, f_, fp_: f_ ** 2 * x ** 2)
    gA = g_assembly(1.0, rstar ** 2, Ie0, Ie2, omega)
    gB = g_assembly(If0, If2, Ie0, Ie2, omega)
    return dict(Ie0=Ie0, Ie2=Ie2, If0=If0, If2=If2, r2_eps=Ie2 / Ie0, r2_qB=If2 / If0, r2_qA=rstar ** 2,
                gA=gA, gB=gB)


# ------------------------------------------------------------------------------------ v3 closed forms
def _poly_moments(f_poly, eps_poly, a, b):
    from numpy.polynomial import Polynomial as P
    two_pi_r = P([0.0, 2.0 * PI])
    def I(poly, power):
        q = (poly * two_pi_r * P([0.0] * power + [1.0])).integ()
        return q(b) - q(a)
    return dict(Ie0=I(eps_poly, 0), Ie2=I(eps_poly, 2), If0=I(f_poly ** 2, 0), If2=I(f_poly ** 2, 2))


def _gauss_closed(a, b):
    G = [lambda u: np.exp(-u), lambda u: (u + 1) * np.exp(-u), lambda u: (u ** 2 + 2 * u + 2) * np.exp(-u)]
    In = [0.5 * (G[n](a ** 2) - G[n](b ** 2)) for n in range(3)]     # Int r^(2n+1) exp(-r^2) dr
    return dict(Ie0=2 * PI * (In[0] + 0.5 * In[1]), Ie2=2 * PI * (In[1] + 0.5 * In[2]),
                If0=2 * PI * In[0], If2=2 * PI * In[1])


def v3_cases(ns):
    """The credential cases: name, (r, f, fp), eps_fn, closed-form moments, R*."""
    from numpy.polynomial import Polynomial as P
    c = CONFIG
    a, N, om, k = c['v3_a'], c['v3_n'], c['v3_omega'], c['v3_k']
    cases = []
    # (i) f = r with the PHYSICAL energy density: g2 = 2 everywhere, eps = e0 + 0.5 Omega^2 r^2 exactly
    R = c['v3_R_poly']
    r = np.geomspace(a, R, N)
    e0 = (np.sqrt(3.0) - 1.0) + 0.5 * k * (np.sqrt(3.0) - 1.0) ** 2
    cases.append(('f=r (physical eps)', (r, r.copy(), np.ones_like(r)), eps_fn_physical(ns, k, om, 'full'),
                  _poly_moments(P([0.0, 1.0]), P([e0, 0.0, 0.5 * om ** 2]), a, R), R))
    # (ii) two-term polynomial profile, test density f^2 + 0.5 f'^2 (exercises the derivative path)
    fpoly = P([0.0, 1.0, 0.0, 0.1])
    f2 = fpoly(r)
    fp2 = fpoly.deriv()(r)
    cases.append(('f=r+0.1r^3 (test eps)', (r, f2, fp2), lambda x, f_, fp_: f_ ** 2 + 0.5 * fp_ ** 2,
                  _poly_moments(fpoly, fpoly ** 2 + 0.5 * fpoly.deriv() ** 2, a, R), R))
    # (iii) Gaussian
    R = c['v3_R_gauss']
    rg = np.geomspace(a, R, N)
    fg = np.exp(-rg ** 2 / 2)
    cases.append(('f=exp(-r^2/2) (test eps)', (rg, fg, -rg * fg), lambda x, f_, fp_: f_ ** 2 + 0.5 * fp_ ** 2,
                  _gauss_closed(a, R), R))
    return cases


def v3_run(ns):
    """Pass every case through THE SAME moments() that scores g; compare to the closed forms. Returns the table."""
    om, tol = CONFIG['v3_omega'], CONFIG['v3_tol_rel']
    table = []
    for name, (r, f, fp), eps_fn, closed, R in v3_cases(ns):
        got = moments(r, f, fp, eps_fn, om, R)
        want = dict(r2_eps=closed['Ie2'] / closed['Ie0'], r2_qB=closed['If2'] / closed['If0'], r2_qA=R ** 2)
        want['gA'] = want['r2_qA'] / want['r2_eps']
        want['gB'] = want['r2_qB'] / want['r2_eps']
        row = dict(case=name)
        for key in ('r2_eps', 'r2_qB', 'gA', 'gB'):
            row[key] = K.rel(got[key], want[key], f'v3 {name} {key}')
        # the assembly itself: g from (mu, L, m, q) equals <r^2>_q / <r^2>_eps
        row['assembly'] = K.rel(g_assembly(closed['If0'], closed['If2'], closed['Ie0'], closed['Ie2'], om), want['gB'],
                                f'v3 {name} assembly')
        row['worst'] = max(row[k_] for k_ in ('r2_eps', 'r2_qB', 'gA', 'gB', 'assembly'))
        table.append(row)
        K.require(row['worst'] <= tol, f'v3 {name}: worst relative error {row["worst"]:.2e} above {tol}')
    return table


# -------------------------------------------------------------------------------------------------- units
def unit_credential(ck):
    table = v3_run(load_solver(fixture=False))
    ck.seal('v3_table', [dict(r) for r in table])
    return dict(v3=[dict(r) for r in table], v3_worst=max(r['worst'] for r in table))


def make_solve(i):
    def unit(ck):
        if ck.smoke:
            ns = load_solver(fixture=True)
            k = CONFIG['smoke_k']
            r_min, tol = CONFIG['smoke_runs'][i]
            out = ns['solve_el'](k, r_min, tol, n_mesh=CONFIG['smoke_n_mesh'])
        else:
            ns = load_solver(fixture=False)
            k = CONFIG['k_over_T0']
            r_min, tol = CONFIG['runs'][i]
            out = ns['solve_el'](k, r_min, tol)
        sol = ns['_captured'][-1] if ns['_captured'] else None
        K.require(sol is not None and sol.success and out is not None,
                  f'solve {i + 1} (r_min {r_min}, tol {tol}): solver reported failure '
                  f'({getattr(sol, "message", "no solution")})')
        K.finite_array(sol.x, 'mesh'); K.finite_array(sol.y, 'solution')
        ck.seal(f'r_{i}', np.asarray(sol.x, dtype=float))
        ck.seal(f'f_{i}', np.asarray(sol.y[0], dtype=float))
        ck.seal(f'fp_{i}', np.asarray(sol.y[1], dtype=float))
        ck.seal(f'y2_{i}', np.asarray(sol.y[2], dtype=float))
        print(f'  run {i + 1}: r_min {r_min:g} tol {tol:g} nodes {len(sol.x)} D_E(solver) {out["D"]:.7f}', flush=True)
        return dict(r_min=r_min, tol=tol, nodes=int(len(sol.x)), success=bool(sol.success), solver_status=int(sol.status),
                    solver_message=str(sol.message), D_solver=float(out['D']), lam=float(out['lam']),
                    E_el_solver=float(out['E_el']), LOG_solver=float(out['LOG']))
    return unit


def run_arrays(ck, i):
    return tuple(ck.sealed(f'{n}_{i}') for n in ('r', 'f', 'fp', 'y2'))


def run_numbers(ck, i, ns):
    """Everything computed for run i from its seals only (shared by the driver's moments unit and the verdict)."""
    k = CONFIG['smoke_k'] if ck.smoke else CONFIG['k_over_T0']
    omega, xstar, JT = ns['OMEGA'], ns['XSTAR'], ns['JT']
    r, f, fp, y2 = run_arrays(ck, i)
    K.require(abs(r[-1] - xstar) <= 1e-12 * xstar, f'run {i + 1}: outer mesh point {r[-1]} is not x* = {xstar}')
    # v1 inputs: D_E recomputed with the solver's own formulas on the sealed arrays
    g2 = fp ** 2 + (f / r) ** 2
    E_el = float(np.trapezoid(ns['elastic_density'](g2, k) * 2.0 * PI * r, r))
    LOG = float(np.trapezoid((f ** 2 / (2.0 * r ** 2)) * 2.0 * PI * r, r))
    E_rot = 0.5 * omega * JT
    D = (E_el - LOG + E_rot) / E_rot
    # v2: the solver's cumulant satisfies the normalisation J = J_T
    J_cum = omega * float(y2[-1])
    out = dict(D_E=K.finite(D, 'D_E'), v2_norm=K.rel(J_cum, JT, 'v2 normalisation'))
    spl = dense_profile(r, f, fp)
    out['v2_quad'] = K.rel(omega * quad_area(spl, r, lambda x, f_, fp_: f_ ** 2), JT, 'v2b quadrature vs J_T')
    for v in VARIANTS:
        m = moments(r, f, fp, eps_fn_physical(ns, k, omega, v), omega, xstar)
        out[v] = m
    return out


def unit_moments(ck):
    ns = load_solver(fixture=ck.smoke)
    n_runs = len(CONFIG['smoke_runs'] if ck.smoke else CONFIG['runs'])
    nums = [run_numbers(ck, i, ns) for i in range(n_runs)]           # all runs collected before any is published
    c = CONFIG
    for i, n in enumerate(nums):
        K.require(n['v2_norm'] <= c['v2_norm_tol_rel'],
                  f'v2: run {i + 1} normalisation off by {n["v2_norm"]:.2e} (bar {c["v2_norm_tol_rel"]})')
    if not ck.smoke:
        d = abs(nums[0]['D_E'] - c['D_E_chain'])
        K.require(d <= c['v1_tol_abs'], f'v1: D_E on the adjudicating run {nums[0]["D_E"]:.8f} differs from the chain '
                  f'{c["D_E_chain"]} by {d:.2e} (bar {c["v1_tol_abs"]})')
        K.require(nums[0]['v2_quad'] <= c['v2_quad_tol_rel'],
                  f'v2b: production quadrature of Int f^2 dA off the solver cumulant by {nums[0]["v2_quad"]:.2e} '
                  f'(bar {c["v2_quad_tol_rel"]})')
    for i, n in enumerate(nums):
        print(f'  run {i + 1}: v2 {n["v2_norm"]:.1e} v2b {n["v2_quad"]:.1e} (numbers withheld until the verdict)', flush=True)
    return dict(runs=nums)


UNITS = ([('credential', unit_credential)] + [(f'solve_{i + 1}', make_solve(i)) for i in range(5)]
         + [('moments', unit_moments)])

if __name__ == '__main__':
    if os.environ.get('LAB_SMOKE') == '1':                          # the smoke file only, never the evidence file
        sp = ROOT / 'analysis' / f'{SLUG}_smoke.pkl'
        if sp.exists():
            sp.unlink()
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
