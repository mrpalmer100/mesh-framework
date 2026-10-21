"""KIT-EXAMPLE driver: the template a draft copies. One unit per invocation through labkit.Driver.

The commission here is a toy: credential a quadrature on a closed-form integral (the control leg, run first),
then measure the slope of a synthetic line (the evidence), sealing the raw samples before any fit. Nothing
physical. The verdict is example_verdict.py. LAB_SMOKE=1 runs every unit in one process on a smaller fixture and
writes analysis/kit_example_smoke.pkl, never the evidence checkpoint.
"""
import os
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                 # noqa: E402

SLUG = 'kit_example'
MANIFEST = ['benchmarks/lab/_kit/labkit.py', 'benchmarks/lab/_kit/example_driver.py',
            'benchmarks/lab/_kit/example_verdict.py']
CONFIG = dict(n_samples=200, control_tol=1e-10, seed=20261021)     # locked numbers live in one place


def unit_control(ck):
    """The control leg: Simpson on x^2 over [0, 1] must give 1/3 to the locked tolerance."""
    x = np.linspace(0, 1, 2001)
    y = x ** 2
    h = x[1] - x[0]
    s = h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())
    err = abs(s - 1 / 3)
    K.require(err <= CONFIG['control_tol'], f'control: Simpson error {err:.2e} above {CONFIG["control_tol"]}')
    return dict(simpson=float(s), err=float(err))


def unit_samples(ck):
    """The evidence samples, sealed BEFORE any statistic is computed (a later unit fits them)."""
    n = 20 if ck.smoke else CONFIG['n_samples']
    rng = np.random.default_rng(CONFIG['seed'])
    x = np.linspace(0, 1, n)
    y = 2.0 * x + 0.5 + rng.normal(0, 1e-3, n)
    K.finite_array(y, 'samples')
    ck.seal('x', x); ck.seal('y', y)
    return dict(n=int(n))


def unit_fit(ck):
    """The fit, from the sealed arrays only."""
    x, y = ck.sealed('x'), ck.sealed('y')
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    slope, icpt = (K.finite(c, 'fit coefficient') for c in coef)
    return dict(slope=slope, intercept=icpt)


UNITS = [('control', unit_control), ('samples', unit_samples), ('fit', unit_fit)]

if __name__ == '__main__':
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
