"""ELEC-G-2 verdict: reads the checkpoint only, through labkit.Verdict.

form_rule recomputes every moment and every g from the SEALED arrays with the driver's production functions, checks
the driver's record to 1e-12 relative, applies D2, and only then decides the form; nothing is published before the
decision. The measured electron moment is entered in ONE place, the last step of `decide`, after every number has
been computed; it appears in no other function and not in CONFIG.

Forms (Q1), exhaustive and exclusive, band 5e-4 in absolute g. ALL FOUR targets (2, 2.0023193, 1, 2 pi) are tested for
BOTH readings (A: R-geometry; B: profile-weighted); each reading's outcome (a target or none) is printed in every reason.
  both readings hit the same target -> that target's form (G-DIRAC, G-MEASURED, G-CLASSICAL, G-PI-DIRAC);
  neither reading hits any target -> G-OTHER;
  otherwise (different targets, or one hit against one miss) -> UNDERSPECIFIED;
  D2 (absolute range of each scored g across the five runs <= 1e-5) or any validation bar failed, or any harness
  fault -> NO-CALL (the kit's open form).
Q2 is a reported number, not a form: F = g / 2 per reading and its match against the Gate-1 candidates.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                   # noqa: E402
from benchmarks.lab.elec_g_2 import driver as D                                # noqa: E402
from benchmarks.lab.elec_g_2.driver import SLUG, MANIFEST, CONFIG, UNITS       # noqa: E402

NAME = 'ELEC-G-2'
FORMS = ['G-DIRAC', 'G-MEASURED', 'G-CLASSICAL', 'G-PI-DIRAC', 'G-OTHER', 'UNDERSPECIFIED', 'NO-CALL']


def _outcome(g, targets):
    """The single target whose band contains g, or None (bands cannot overlap: checked in decide)."""
    band = CONFIG['band_abs']
    hits = [tok for tok, val in targets if abs(g - val) <= band]
    return hits[0] if hits else None


def decide(gA, gB):
    """The last step: the only place the measured value enters. All four targets are tested for BOTH readings and each
    reading's outcome is printed in every reason."""
    G_MEASURED = 2.00231930                                                    # comparison value, loaded last
    c = CONFIG
    targets = [('G-DIRAC', c['g_dirac']), ('G-MEASURED', G_MEASURED), ('G-CLASSICAL', c['g_classical']),
               ('G-PI-DIRAC', c['g_pi_dirac'])]
    K.require(min(abs(a[1] - b[1]) for i, a in enumerate(targets) for b in targets[i + 1:]) > 2 * c['band_abs'],
              'target bands overlap')
    oA, oB = _outcome(gA, targets), _outcome(gB, targets)
    per = f'reading A: g_A = {gA:.6f} -> {oA or "no target"}; reading B: g_B = {gB:.6f} -> {oB or "no target"}'
    if oA is None and oB is None:
        return 'G-OTHER', f'{per}; neither reading within {c["band_abs"]:g} of any of the four targets'
    if oA == oB:
        return oA, f'both readings agree: {per}'
    return 'UNDERSPECIFIED', f'the two readings differ (a hit against a miss counts as differing): {per}'


def form_rule(ck, out):
    rec = ck.state['records']
    c = CONFIG
    ns = D.load_solver(fixture=ck.smoke)
    n_runs = len(c['smoke_runs'] if ck.smoke else c['runs'])
    out.append(f'credential v3 (production moment path on closed forms): worst relative error '
               f'{rec["credential"]["v3_worst"]:.2e} against {c["v3_tol_rel"]:g}')
    for row in rec['credential']['v3']:
        out.append(f'  v3 {row["case"]}: <r2>_eps {row["r2_eps"]:.1e} <r2>_q {row["r2_qB"]:.1e} g_A {row["gA"]:.1e} '
                   f'g_B {row["gB"]:.1e} assembly {row["assembly"]:.1e}')
    K.require(rec['credential']['v3_worst'] <= c['v3_tol_rel'], 'v3 not met')
    for row in D.v3_run(ns):                                                   # re-run the credential here too
        K.require(row['worst'] <= c['v3_tol_rel'], 'v3 re-run not met')
    # recompute everything from the seals
    nums = [D.run_numbers(ck, i, ns) for i in range(n_runs)]
    drv = rec['moments']['runs']
    for i, (n, d) in enumerate(zip(nums, drv)):
        K.require(K.rel(n['D_E'], d['D_E'], 'D_E recompute') <= 1e-12, f'run {i + 1}: D_E differs from the driver record')
        for v in D.VARIANTS:
            for key in ('gA', 'gB', 'r2_eps', 'r2_qB'):
                K.require(K.rel(n[v][key], d[v][key], f'{v} {key}') <= 1e-12,
                          f'run {i + 1} {v} {key}: verdict recomputation disagrees with the driver record')
    n0 = nums[0]
    if not ck.smoke:
        K.require(abs(n0['D_E'] - c['D_E_chain']) <= c['v1_tol_abs'], 'v1 not met')
        K.require(n0['v2_quad'] <= c['v2_quad_tol_rel'], 'v2b not met')
    for i, n in enumerate(nums):
        K.require(n['v2_norm'] <= c['v2_norm_tol_rel'], f'v2 not met on run {i + 1}')
        r_min, tol = (c['smoke_runs'] if ck.smoke else c['runs'])[i]
        out.append(f'run {i + 1} (r_min {r_min:g}, tol {tol:g}, nodes {rec[f"solve_{i + 1}"]["nodes"]}): '
                   f'D_E {n["D_E"]:.7f} v2 {n["v2_norm"]:.1e} v2b {n["v2_quad"]:.1e}')
        for v in D.VARIANTS:
            m = n[v]
            out.append(f'   {v:8s} <r2>_eps {m["r2_eps"]:.9e} <r2>_qB {m["r2_qB"]:.9e} R*^2 {m["r2_qA"]:.9e} '
                       f'g_A {m["gA"]:.9f} g_B {m["gB"]:.9f}')
    # D2 floor: ABSOLUTE range (max - min) of each scored g across the runs (full energy density), at most d2_tol_abs
    d2 = {r_: max(n['full'][r_] for n in nums) - min(n['full'][r_] for n in nums) for r_ in ('gA', 'gB')}
    out.append(f'D2: absolute range of g across the {n_runs} runs: g_A {d2["gA"]:.2e}, g_B {d2["gB"]:.2e} '
               f'against {c["d2_tol_abs"]:g} (band {c["band_abs"]:g}, ratio {c["band_abs"] / c["d2_tol_abs"]:.0f})')
    if not ck.smoke:                      # the coarse smoke fixture is not held to the evidence floor (it is not a cell)
        K.require(max(d2.values()) <= c['d2_tol_abs'],
                  f'D2 not met: g_A range {d2["gA"]:.2e}, g_B range {d2["gB"]:.2e} against {c["d2_tol_abs"]:g}')
    gA, gB = n0['full']['gA'], n0['full']['gB']
    # Q2: the factor, reported as a number, no factor applied
    for label, g in (('A', gA), ('B', gB)):
        F = g / 2.0
        hits = [nm for nm, val in c['q2_candidates'] if abs(F / val - 1.0) <= c['q2_match_rel']]
        out.append(f'Q2 (reading {label}): g/2 = {F:.9f}; Gate-1 candidates matched within {c["q2_match_rel"]:g}: '
                   f'{", ".join(hits) if hits else "none"}')
    sens = {v: (n0[v]['gA'], n0[v]['gB']) for v in ('elastic', 'chain')}
    out.append('sensitivities (reported, not readings, no role in the form): ' +
               '; '.join(f'{v}: g_A {a:.6f} g_B {b:.6f}' for v, (a, b) in sens.items()))
    if ck.smoke:
        out.append('smoke: numeric plumbing checked on the synthetic fixture (k/T0 = 3, x* = e^2); the form is not decided')
        return [('Q1', 'NO-CALL', 'smoke')]
    tok, why = decide(gA, gB)
    return [('Q1', tok, why)]


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, NAME, [u for u, _ in UNITS], MANIFEST, FORMS, open_form='NO-CALL', config=CONFIG)
    sys.exit(v.render(form_rule))
