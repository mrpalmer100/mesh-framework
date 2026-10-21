"""labkit's own tests: every reviewer objection the kit exists to retire has a test here. Run directly
(python benchmarks/lab/_kit/test_labkit.py) or under pytest. Each test builds a throwaway repo root in a
temporary directory, so nothing under analysis/ is touched.
"""
import contextlib
import io
import os
import pathlib
import shutil
import sys
import tempfile

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                 # noqa: E402

FORMS = ['EX-PASS', 'EX-FAIL', 'NO-CALL']


class Tmp:
    """A throwaway repo root with the manifest files copied in."""

    def __enter__(self):
        self.d = pathlib.Path(tempfile.mkdtemp())
        (self.d / 'analysis').mkdir()
        (self.d / 'locked').mkdir()
        (self.d / 'locked' / 'a.py').write_text('A = 1\n')
        (self.d / 'locked' / 'b.py').write_text('B = 2\n')
        return self.d

    def __exit__(self, *a):
        shutil.rmtree(self.d, ignore_errors=True)


MAN = ['locked/a.py', 'locked/b.py']
CFG = dict(tol=1e-9)


def units_ok():
    def u1(ck):
        ck.seal('x', np.arange(5.0)); return dict(k=1)

    def u2(ck):
        x = ck.sealed('x'); return dict(s=float(x.sum()))
    return [('one', u1), ('two', u2)]


def rule_ok(ck, out):
    out.append('numbers')
    s = ck.state['records']['two']['s']
    return [('Q1', 'EX-PASS' if s == 10.0 else 'EX-FAIL', f's = {s}')]


def capture(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn()
    return rc, buf.getvalue()


def test_one_unit_per_invocation_and_terminal():
    with Tmp() as d:
        rc1, o1 = capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        assert rc1 == 0 and K.TERMINAL not in o1
        rc2, o2 = capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        assert rc2 == 0 and o2.strip().endswith(K.TERMINAL)          # the last unit's invocation is terminal
        rc, out = capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        assert K.TERMINAL in out and 'already terminal' in out
        rc, out = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                            smoke=False).render(rule_ok))
        assert rc == 0 and 'FORM (Q1): EX-PASS' in out, out
        assert (d / 'analysis' / 'EX_verdict.log').read_text().strip().endswith('s = 10.0')


def run_all(d, units, smoke=False):
    for _ in range(len(units) + 1):
        rc, out = capture(lambda: K.Driver(d, 'ex', units, MAN, config=CFG, smoke=smoke).run())
        if K.TERMINAL in out:
            return out
    raise AssertionError('never terminal')


def test_exception_becomes_halt_and_open_form():
    def bad(ck):
        raise ZeroDivisionError('boom')
    with Tmp() as d:
        out = run_all(d, [('one', bad), ('two', lambda ck: {})])
        assert 'HALT: one: ZeroDivisionError: boom' in out and K.TERMINAL in out
        rc, vo = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                           smoke=False).render(rule_ok))
        assert 'FORM (Q1): NO-CALL' in vo and 'driver halted' in vo and 'numbers' not in vo


def test_blocked_exit_3():
    def blk(ck):
        raise K.Blocked('waiting for the draw')
    with Tmp() as d:
        rc, out = capture(lambda: K.Driver(d, 'ex', [('one', blk)], MAN, config=CFG, smoke=False).run())
        assert rc == 3 and 'BLOCKED' in out and K.TERMINAL not in out


def test_manifest_mismatch_halts():
    with Tmp() as d:
        capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        (d / 'locked' / 'a.py').write_text('A = 2\n')
        rc, out = capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        assert 'HALT: two: manifest: locked file(s) changed' in out and K.TERMINAL in out


def test_verdict_refuses_nonterminal_and_changed_files_and_broken_seal():
    with Tmp() as d:
        capture(lambda: K.Driver(d, 'ex', units_ok(), MAN, config=CFG, smoke=False).run())
        rc, vo = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                           smoke=False).render(rule_ok))
        assert 'FORM (Q1): NO-CALL' in vo and 'not terminal' in vo
        os.unlink(d / 'analysis' / 'EX_verdict.lock'); os.unlink(d / 'analysis' / 'EX_verdict.log')
        run_all(d, units_ok())
        (d / 'locked' / 'b.py').write_text('B = 3\n')
        rc, vo = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                           smoke=False).render(rule_ok))
        assert 'NO-CALL' in vo and 'changed since the run' in vo
        (d / 'locked' / 'b.py').write_text('B = 2\n')
        os.unlink(d / 'analysis' / 'EX_verdict.lock'); os.unlink(d / 'analysis' / 'EX_verdict.log')
        ck = K.Checkpoint(d, 'ex', ['one', 'two'], MAN, smoke=False, config=CFG); ck.load()
        ck.state['seals']['x']['payload']['bytes'] = b'\x00' * len(ck.state['seals']['x']['payload']['bytes'])
        ck.save()
        rc, vo = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                           smoke=False).render(rule_ok))
        assert 'NO-CALL' in vo and "seal 'x' broken" in vo


def test_verdict_one_shot_and_config_mismatch():
    with Tmp() as d:
        run_all(d, units_ok())
        v = lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG, smoke=False).render(rule_ok)
        rc1, o1 = capture(v); rc2, o2 = capture(v)
        assert rc1 == 0 and 'EX-PASS' in o1 and rc2 == 1 and 'REFUSED' in o2 and 'FORM' not in o2
        os.unlink(d / 'analysis' / 'EX_verdict.lock'); os.unlink(d / 'analysis' / 'EX_verdict.log')
        rc, o = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=dict(tol=1e-3),
                                          smoke=False).render(rule_ok))
        assert 'NO-CALL' in o and 'configuration differs' in o


def test_form_rule_exception_publishes_nothing():
    def rule_bad(ck, out):
        out.append('SECRET NUMBER 42')
        raise RuntimeError('midway')
    with Tmp() as d:
        run_all(d, units_ok())
        rc, o = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                          smoke=False).render(rule_bad))
        assert 'NO-CALL' in o and 'SECRET' not in o and 'midway' in o

    def rule_undeclared(ck, out):
        return [('Q1', 'EX-MAYBE', 'x')]
    with Tmp() as d:
        run_all(d, units_ok())
        rc, o = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                          smoke=False).render(rule_undeclared))
        assert 'NO-CALL' in o and 'undeclared' in o


def test_smoke_separate_file_and_forms_withheld():
    with Tmp() as d:
        out = run_all(d, units_ok(), smoke=True)
        assert (d / 'analysis' / 'ex_smoke.pkl').exists() and not (d / 'analysis' / 'ex_ckpt.pkl').exists()
        rc, o = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                          smoke=True).render(rule_ok))
        assert 'smoke: forms withheld' in o and 'FORM' not in o and 'numbers' in o
        # an evidence verdict must not read the smoke file
        rc, o = capture(lambda: K.Verdict(d, 'ex', 'EX', ['one', 'two'], MAN, FORMS, 'NO-CALL', config=CFG,
                                          smoke=False).render(rule_ok))
        assert 'NO-CALL' in o and 'absent' in o


def test_numeric_helpers():
    for bad in (float('nan'), float('inf'), 'x', None):
        try:
            K.finite(bad); raise AssertionError('accepted')
        except K.Halt:
            pass
    try:
        K.rel(1.0, 0.0); raise AssertionError('zero denominator accepted')
    except K.Halt:
        pass
    assert K.rel(1.0, 2.0) == 0.5
    try:
        K.finite_array(np.array([1.0, np.nan])); raise AssertionError('nan array accepted')
    except K.Halt:
        pass


def test_static_scan_and_isolated_run():
    with Tmp() as d:
        good = d / 'good.py'
        good.write_text('import numpy as np\nSTATUS = "DERIVED"\nASSUMPTIONS = []\nOBSTRUCTION = None\n'
                        'def f(x):\n    return np.asarray(x) * 2\n')
        assert K.static_scan(good) == []
        r = K.run_isolated(good, 'f', dict(x=np.arange(3.0)), timeout_s=60)
        assert r['ok'] and np.allclose(r['result'], [0, 2, 4]) and r['meta']['STATUS'] == 'DERIVED', r
        bad = d / 'bad.py'
        bad.write_text('import os\nimport numpy as np\ndef f(x):\n    return open("/etc/passwd").read()\n')
        probs = K.static_scan(bad)
        assert any('os' in p for p in probs) and any("'open'" in p for p in probs), probs
        r = K.run_isolated(bad, 'f', dict(x=1))
        assert not r['ok'] and r['error'] == 'static scan failed' and r['scan']
        sneaky = d / 'sneaky.py'
        sneaky.write_text('import numpy as np\ndef f(x):\n    return np.load("/nonexistent.npy")\n')
        assert any('load' in p for p in K.static_scan(sneaky))
        slow = d / 'slow.py'
        slow.write_text('def f(x):\n    while True:\n        pass\n')
        r = K.run_isolated(slow, 'f', dict(x=1), timeout_s=2)
        assert not r['ok'] and 'timeout' in r['error']
        crash = d / 'crash.py'
        crash.write_text('def f(x):\n    raise ValueError("inside")\n')
        r = K.run_isolated(crash, 'f', dict(x=1), timeout_s=30)
        assert not r['ok'] and 'ValueError: inside' in r['error']


def test_example_pair_end_to_end():
    """The template itself runs: driver three times, verdict once, in a copy of the kit under a temp root."""
    with Tmp() as d:
        kit = d / 'benchmarks' / 'lab' / '_kit'
        kit.mkdir(parents=True)
        for f in ('labkit.py', 'example_driver.py', 'example_verdict.py'):
            shutil.copy(HERE / f, kit / f)
        (d / 'benchmarks' / '__init__.py').touch(); (d / 'benchmarks' / 'lab' / '__init__.py').touch()
        (kit / '__init__.py').touch()
        import subprocess
        env = dict(os.environ); env.pop('LAB_SMOKE', None)
        outs = [subprocess.run([sys.executable, str(kit / 'example_driver.py')], capture_output=True, text=True,
                               cwd=str(d), env=env).stdout for _ in range(4)]
        assert K.TERMINAL not in outs[1] and outs[2].strip().endswith(K.TERMINAL) and 'already terminal' in outs[3], outs
        v = subprocess.run([sys.executable, str(kit / 'example_verdict.py')], capture_output=True, text=True,
                           cwd=str(d), env=env)
        assert 'FORM (Q1): EX-PASS' in v.stdout, v.stdout + v.stderr
        env['LAB_SMOKE'] = '1'
        s = subprocess.run([sys.executable, str(kit / 'example_driver.py')], capture_output=True, text=True,
                           cwd=str(d), env=env)
        assert K.TERMINAL in s.stdout and (d / 'analysis' / 'kit_example_smoke.pkl').exists()
        sv = subprocess.run([sys.executable, str(kit / 'example_verdict.py')], capture_output=True, text=True,
                            cwd=str(d), env=env)
        assert 'smoke: forms withheld' in sv.stdout and 'FORM' not in sv.stdout


if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    for t in tests:
        t()
        print(f'  [PASS] {t.__name__}')
    print(f'== labkit: {len(tests)} passed')
