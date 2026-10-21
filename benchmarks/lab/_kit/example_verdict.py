"""KIT-EXAMPLE verdict: reads the checkpoint only, through labkit.Verdict.

form_rule computes the locked statistics from the sealed arrays and the unit records, appends the numbers it
wants published to `out`, and returns the decisions; the kit publishes nothing until the decision exists, so an
exception half-way renders the open form with nothing leaked. Forms: EX-PASS (slope within 1e-2 of 2),
EX-FAIL (outside), NO-CALL (the harness could not evaluate).
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                 # noqa: E402
from benchmarks.lab._kit.example_driver import SLUG, MANIFEST, CONFIG, UNITS   # noqa: E402

NAME = 'KIT-EXAMPLE'
FORMS = ['EX-PASS', 'EX-FAIL', 'NO-CALL']
SLOPE_TARGET, SLOPE_TOL = 2.0, 1e-2                          # locked thresholds


def form_rule(ck, out):
    rec = ck.state['records']
    out.append(f'control: Simpson {rec["control"]["simpson"]:.12f} (err {rec["control"]["err"]:.1e})')
    x, y = ck.sealed('x'), ck.sealed('y')                   # re-read from the seals, not from the fit record
    import numpy as np
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    slope = K.finite(coef[0], 'slope')
    K.require(abs(slope - rec['fit']['slope']) < 1e-12, 'verdict recomputation disagrees with the driver record')
    out.append(f'slope {slope:.6f} on {len(x)} sealed samples')
    tok = 'EX-PASS' if abs(slope - SLOPE_TARGET) <= SLOPE_TOL else 'EX-FAIL'
    return [('Q1', tok, f'|slope - {SLOPE_TARGET}| = {abs(slope - SLOPE_TARGET):.2e} against {SLOPE_TOL}')]


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, NAME, [u for u, _ in UNITS], MANIFEST, FORMS, open_form='NO-CALL', config=CONFIG)
    sys.exit(v.render(form_rule))
