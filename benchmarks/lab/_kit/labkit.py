"""labkit: the pre-credentialed harness kit for lab commissions (the executor, 2026-10-21).

Why it exists. Every drafted commission re-implemented the same harness plumbing and the reviewers rejected the
same defects in a different place each round: checkpoints not bound to the locked files, verdicts rendered on
incomplete or mixed-version state, output published before the form was decided, exceptions escaping instead
of a durable halt, derivation modules imported before a static scan, second verdict invocations rewriting the
log. ELEC-G-1 (2026-10-21) passed its physics review twice and died of these in three rounds. A driver that
uses this kit inherits one reviewed implementation of all of them.

What it supplies.
  Checkpoint   atomic pickle state with unit records, sealed arrays (sha256 of the bytes), a manifest of the
               locked files' hashes taken at the first unit and re-verified at every later one, a terminal
               record (complete or halt) and a smoke/evidence distinction that cannot be crossed.
  Driver       one unit per invocation, in the locked order, resumable; any exception inside a unit becomes a
               HALT record in the checkpoint followed by the terminal line, so the verdict renders the open form
               instead of the lab seeing a crash; Blocked(reason) prints BLOCKED and exits 3 (the runner waits);
               never prints FORM.
  Verdict      reads the checkpoint only; fails closed (terminal record present, every unit done, manifest and
               seals verified, configuration matched) BEFORE any statistic is computed; the form rule runs on a
               buffer and nothing is printed until the token is decided; every reachable state prints exactly
               one FORM line per question; an exception anywhere renders the open form; the log is written once
               under an exclusive reservation and a second invocation refuses; with LAB_SMOKE=1 it reads the
               smoke checkpoint and withholds all forms.
  Derivation   static_scan() of a module's source against an import and name allowlist, run before import;
               run_isolated() evaluates a module function in a subprocess (python -I, no inherited environment,
               a time limit, a JSON channel) so a module that fails the scan is never imported and one that
               misbehaves cannot touch the checkpoint; AttemptRecord counts attempts against a budget.
  Numerics     finite(), require(), rel() helpers that raise Halt with a reason instead of letting NaN or a zero
               denominator reach a comparison.

Nothing here is physics. The kit's own tests are benchmarks/lab/_kit/test_labkit.py; the example pair
example_driver.py / example_verdict.py is the template a draft copies.
"""
import ast
import contextlib
import hashlib
import io
import json
import math
import os
import pathlib
import pickle
import subprocess
import sys
import tempfile
import time
import traceback

TERMINAL = 'COMPLETE -- run the verdict'
KIT_VERSION = '1.0'


class Halt(Exception):
    """A durable, recorded stop: the unit cannot proceed and the commission's open form is the verdict."""


class Blocked(Exception):
    """A precondition the lab must supply (a draw, an author's word): the runner waits, nothing is recorded as a fault."""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def finite(x, what='value'):
    """x as a float, or Halt if it is not a finite number."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        raise Halt(f'{what}: not a number ({x!r})')
    if not math.isfinite(v):
        raise Halt(f'{what}: not finite ({v!r})')
    return v


def finite_array(a, what='array'):
    import numpy as np
    arr = np.asarray(a)
    if arr.size == 0:
        raise Halt(f'{what}: empty')
    if not np.all(np.isfinite(arr)):
        raise Halt(f'{what}: contains non-finite entries')
    return arr


def require(cond, reason):
    if not cond:
        raise Halt(reason)


def rel(a, b, what='ratio'):
    """|a - b| / |b| with both finite and b nonzero, else Halt."""
    a, b = finite(a, what + ' numerator'), finite(b, what + ' denominator')
    if b == 0.0:
        raise Halt(f'{what}: zero denominator')
    return abs(a - b) / abs(b)


def atomic_write_bytes(path, data):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + '.', suffix='.tmp')
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


class Checkpoint:
    """The commission's state. One file for the evidence run, a different one for smoke; the smoke file carries
    smoke=True inside and the verdict refuses to render forms from it."""

    def __init__(self, root, slug, units, manifest_files, smoke=False, config=None):
        self.root = pathlib.Path(root)
        self.slug = slug
        self.units = list(units)
        self.manifest_files = [str(f) for f in manifest_files]
        self.smoke = bool(smoke)
        self.path = self.root / 'analysis' / (f'{slug}_smoke.pkl' if smoke else f'{slug}_ckpt.pkl')
        self.config = dict(config or {})
        self.state = None

    # ---- persistence -------------------------------------------------------------------------------------
    def load(self):
        if self.path.exists():
            with open(self.path, 'rb') as f:
                self.state = pickle.load(f)
            if self.state.get('smoke') != self.smoke:
                raise Halt(f'checkpoint {self.path.name} is a {"smoke" if self.state.get("smoke") else "evidence"} '
                           f'file read as {"smoke" if self.smoke else "evidence"}')
            if self.state.get('slug') != self.slug or self.state.get('units') != self.units:
                raise Halt(f'checkpoint {self.path.name} belongs to a different commission or unit list')
        else:
            self.state = dict(kit=KIT_VERSION, slug=self.slug, smoke=self.smoke, units=self.units, config=self.config,
                              created=time.strftime('%Y-%m-%d %H:%M:%S%z'), manifest=None, records={}, seals={},
                              terminal=None, log=[])
        return self.state

    def save(self):
        atomic_write_bytes(self.path, pickle.dumps(self.state, protocol=4))

    # ---- manifest ----------------------------------------------------------------------------------------
    def current_manifest(self):
        out = {}
        for f in self.manifest_files:
            p = self.root / f
            out[f] = sha256_file(p) if p.is_file() else None
        return out

    def bind_manifest(self):
        """At the first unit, record the locked files' hashes; at every later unit, verify them."""
        now = self.current_manifest()
        missing = [f for f, h in now.items() if h is None]
        if missing:
            raise Halt(f'manifest: locked file(s) missing: {", ".join(missing)}')
        if self.state['manifest'] is None:
            self.state['manifest'] = now
        elif self.state['manifest'] != now:
            changed = [f for f in now if now[f] != self.state['manifest'].get(f)]
            raise Halt(f'manifest: locked file(s) changed since the first unit: {", ".join(changed)}')
        return now

    # ---- units, seals, terminal --------------------------------------------------------------------------
    def done(self, unit):
        r = self.state['records'].get(unit)
        return bool(r) and r.get('status') == 'done'

    def next_unit(self):
        for u in self.units:
            if not self.done(u):
                return u
        return None

    def record(self, unit, status, **fields):
        self.state['records'][unit] = dict(status=status, at=time.strftime('%Y-%m-%d %H:%M:%S%z'), **fields)

    def seal(self, name, data):
        """Seal bytes (or a numpy array's bytes) under a name; the verdict re-hashes the stored payload."""
        import numpy as np
        if isinstance(data, np.ndarray):
            payload = dict(kind='ndarray', dtype=str(data.dtype), shape=list(data.shape), bytes=data.tobytes())
            digest = sha256_bytes(payload['bytes'])
        else:
            b = data if isinstance(data, (bytes, bytearray)) else json.dumps(data, sort_keys=True, default=str).encode()
            payload = dict(kind='bytes', bytes=bytes(b))
            digest = sha256_bytes(payload['bytes'])
        self.state['seals'][name] = dict(sha256=digest, payload=payload)
        return digest

    def sealed(self, name):
        import numpy as np
        s = self.state['seals'].get(name)
        if s is None:
            raise Halt(f'seal {name!r} absent')
        if sha256_bytes(s['payload']['bytes']) != s['sha256']:
            raise Halt(f'seal {name!r} broken')
        p = s['payload']
        if p['kind'] == 'ndarray':
            return np.frombuffer(p['bytes'], dtype=p['dtype']).reshape(p['shape']).copy()
        return p['bytes']

    def verify_seals(self):
        for name in list(self.state['seals']):
            self.sealed(name)
        return len(self.state['seals'])

    def set_terminal(self, kind, reason=None):
        self.state['terminal'] = dict(kind=kind, reason=reason, at=time.strftime('%Y-%m-%d %H:%M:%S%z'))


class Driver:
    """One unit per invocation. units: ordered list of (name, callable(ck)). The callable does the work, stores
    what it needs with ck.record(...) fields or ck.seal(...), and returns a dict of summary fields (picklable)."""

    def __init__(self, root, slug, units, manifest_files, config=None, smoke=None):
        self.root = pathlib.Path(root)
        self.slug = slug
        self.unit_names = [n for n, _ in units]
        self.unit_funcs = dict(units)
        self.smoke = (os.environ.get('LAB_SMOKE') == '1') if smoke is None else bool(smoke)
        self.ck = Checkpoint(root, slug, self.unit_names, manifest_files, smoke=self.smoke, config=config)

    def _finish(self, kind, reason=None):
        self.ck.set_terminal(kind, reason)
        self.ck.save()
        if kind == 'halt':
            print(f'HALT: {reason}', flush=True)
        print(TERMINAL, flush=True)
        return 0

    def run(self, one_unit=True):
        try:
            self.ck.load()
        except Halt as e:
            print(f'HALT before any unit: {e}', flush=True)
            return 4                                         # cannot even record: a real failure, not a verdict
        if self.ck.state['terminal'] is not None:
            print(f'already terminal ({self.ck.state["terminal"]["kind"]}); nothing to do', flush=True)
            print(TERMINAL, flush=True)
            return 0
        while True:
            unit = self.ck.next_unit()
            if unit is None:
                return self._finish('complete')
            try:
                self.ck.bind_manifest()
                t0 = time.time()
                print(f'[{self.slug}] unit {unit} ({"smoke" if self.smoke else "evidence"})', flush=True)
                summary = self.unit_funcs[unit](self.ck) or {}
                self.ck.record(unit, 'done', seconds=time.time() - t0, **summary)
                self.ck.save()
                print(f'[{self.slug}] unit {unit} done ({time.time() - t0:.0f}s)', flush=True)
            except Blocked as e:
                self.ck.record(unit, 'blocked', reason=str(e))
                self.ck.save()
                print(f'BLOCKED: {e}', flush=True)
                return 3
            except Halt as e:
                self.ck.record(unit, 'halt', reason=str(e))
                return self._finish('halt', f'{unit}: {e}')
            except Exception as e:                           # any other failure is a recorded halt, never a crash
                self.ck.record(unit, 'halt', reason=f'{type(e).__name__}: {e}', trace=traceback.format_exc()[-4000:])
                return self._finish('halt', f'{unit}: {type(e).__name__}: {e}')
            if self.ck.next_unit() is None:
                return self._finish('complete')              # the last unit's invocation also prints the terminal line
            if one_unit and not self.smoke:
                return 0                                     # the lab reruns us for the next unit


class Verdict:
    """Reads the checkpoint only. form_rule(ck, out) decides and returns a list of (question, token, reason) after
    computing its statistics; it prints nothing itself: it appends lines to out (a list) and the kit publishes
    them only after the token is decided. declared_forms: the charter's forms; open_form: the one for 'the
    harness could not evaluate' (INSTRUMENT-OPEN or NO-CALL); any failure before or inside form_rule renders it."""

    def __init__(self, root, slug, name, units, manifest_files, declared_forms, open_form, config=None,
                 questions=('Q1',), smoke=None):
        self.root = pathlib.Path(root)
        self.slug, self.name = slug, name
        self.units, self.manifest_files = list(units), list(manifest_files)
        self.declared = list(declared_forms)
        self.open_form = open_form
        self.questions = list(questions)
        self.config = dict(config or {})
        self.smoke = (os.environ.get('LAB_SMOKE') == '1') if smoke is None else bool(smoke)
        self.ck = Checkpoint(root, slug, self.units, manifest_files, smoke=self.smoke, config=config)
        self.log_path = self.root / 'analysis' / f'{name}_verdict.log'
        self.lock_path = self.root / 'analysis' / f'{name}_verdict.lock'
        if open_form not in self.declared:
            raise ValueError('open_form must be one of the declared forms')

    def _validate(self):
        """Fail closed. Returns the reason string or None."""
        if not self.ck.path.exists():
            return f'checkpoint {self.ck.path.name} absent'
        try:
            self.ck.load()
        except Halt as e:
            return str(e)
        st = self.ck.state
        if st.get('kit') != KIT_VERSION:
            return f'checkpoint written by kit {st.get("kit")}, verdict is kit {KIT_VERSION}'
        if st.get('config') != self.config:
            return 'checkpoint configuration differs from the locked configuration'
        if st.get('terminal') is None:
            return 'checkpoint not terminal (the driver has not finished)'
        if st['terminal']['kind'] == 'halt':
            return f'driver halted: {st["terminal"]["reason"]}'
        for u in self.units:
            if not self.ck.done(u):
                return f'unit {u} not done'
        if st.get('manifest') is None:
            return 'no manifest bound'
        if not self.smoke:
            now = self.ck.current_manifest()
            if now != st['manifest']:
                changed = [f for f in now if now[f] != st['manifest'].get(f)]
                return f'locked file(s) changed since the run: {", ".join(changed)}'
        try:
            self.ck.verify_seals()
        except Halt as e:
            return str(e)
        return None

    def render(self, form_rule):
        out = []
        decided = None
        reason = self._validate()
        if reason is None:
            try:
                decided = form_rule(self.ck, out)
                if not isinstance(decided, list) or not decided:
                    raise Halt('form_rule returned no decisions')
                for q, tok, why in decided:
                    if tok not in self.declared:
                        raise Halt(f'form_rule returned an undeclared form {tok!r}')
            except Exception as e:                           # Halt or anything else: the open form, nothing published
                reason = f'{type(e).__name__}: {e}'
                decided = None
        if decided is None:
            out = [f'verdict could not evaluate: {reason}']
            decided = [(q, self.open_form, reason[:200]) for q in self.questions]
        lines = list(out)
        if self.smoke:
            lines.append('smoke: forms withheld')
        else:
            for q, tok, why in decided:
                lines.append(f'FORM ({q}): {tok} -- {why}')
        text = '\n'.join(lines) + '\n'
        if self.smoke:
            print(text, end='', flush=True)
            return 0
        # one-shot: an exclusive reservation, then the log written atomically; a second invocation refuses
        try:
            fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            print(f'REFUSED: verdict for {self.name} already rendered ({self.log_path.name}); nothing recomputed',
                  flush=True)
            return 1
        try:
            os.write(fd, time.strftime('%Y-%m-%d %H:%M:%S%z\n').encode())
        finally:
            os.close(fd)
        atomic_write_bytes(self.log_path, text.encode())
        print(text, end='', flush=True)
        return 0


# ---- derivation support ------------------------------------------------------------------------------------
DEFAULT_ALLOWED_IMPORTS = ('numpy', 'math', 'fractions', 'cmath', 'itertools', 'functools', 'typing', 'dataclasses')
FORBIDDEN_NAMES = ('open', 'exec', 'eval', 'compile', '__import__', 'input', 'breakpoint', 'globals', 'getattr',
                   'setattr', 'delattr', 'vars', 'memmap', 'savetxt', 'loadtxt', 'fromfile', 'tofile', 'save',
                   'savez', 'savez_compressed', 'load', 'genfromtxt')
FORBIDDEN_MODULES = ('os', 'sys', 'subprocess', 'pathlib', 'shutil', 'socket', 'pickle', 'importlib', 'ctypes',
                     'multiprocessing', 'threading', 'urllib', 'requests', 'io', 'builtins', 'inspect', 'glob',
                     'tempfile', 'signal', 'resource', 'gc', 'code', 'codeop', 'runpy', 'pty', 'fcntl')


def static_scan(path, allowed_imports=DEFAULT_ALLOWED_IMPORTS):
    """Parse a module's source without importing it. Returns a list of problems (empty = clean)."""
    problems = []
    src = pathlib.Path(path).read_text()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [f'syntax error: {e}']
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or '']
            for n in names:
                top = n.split('.')[0]
                if top in FORBIDDEN_MODULES or top not in allowed_imports:
                    problems.append(f'import of {n!r} not allowed (allowed: {", ".join(allowed_imports)})')
        elif isinstance(node, ast.Name) and node.id in FORBIDDEN_NAMES:
            problems.append(f'use of {node.id!r}')
        elif isinstance(node, ast.Attribute) and node.attr in FORBIDDEN_NAMES:
            problems.append(f'attribute {node.attr!r}')
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'exec':
            problems.append('exec call')
    return sorted(set(problems))


_ISOLATED_RUNNER = r'''
import json, sys, importlib.util, pathlib
spec_path, func, in_path, out_path = sys.argv[1:5]
res = {"ok": False, "error": None, "result": None}
try:
    import numpy as np
    payload = json.loads(pathlib.Path(in_path).read_text())
    args = {k: (np.asarray(v["data"], dtype=v["dtype"]) if isinstance(v, dict) and v.get("__nd__") else v)
            for k, v in payload.items()}
    spec = importlib.util.spec_from_file_location("derivation_module", spec_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = getattr(mod, func)(**args) if func else None
    meta = {k: getattr(mod, k, None) for k in ("STATUS", "ASSUMPTIONS", "OBSTRUCTION")}
    def enc(v):
        if isinstance(v, np.ndarray):
            return {"__nd__": True, "dtype": str(v.dtype), "data": v.tolist()}
        if isinstance(v, (np.floating, np.integer)):
            return v.item()
        return v
    res.update(ok=True, result=enc(out), meta={k: enc(v) for k, v in meta.items()})
except BaseException as e:
    res["error"] = f"{type(e).__name__}: {e}"
pathlib.Path(out_path).write_text(json.dumps(res, default=str))
'''


def run_isolated(module_path, func, args, timeout_s=300, allowed_imports=DEFAULT_ALLOWED_IMPORTS):
    """Static-scan a derivation module and, if clean, evaluate func(**args) in a subprocess (python -I, empty
    environment beyond PATH, cwd a scratch directory, a time limit). Returns dict(ok, error, result, meta, scan).
    Arrays in args are passed by value; the module can read only what it is given."""
    import numpy as np
    scan = static_scan(module_path, allowed_imports)
    if scan:
        return dict(ok=False, error='static scan failed', scan=scan, result=None, meta=None)
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        runner = td / 'runner.py'; runner.write_text(_ISOLATED_RUNNER)
        enc = {k: ({'__nd__': True, 'dtype': str(np.asarray(v).dtype), 'data': np.asarray(v).tolist()}
                   if isinstance(v, np.ndarray) else v) for k, v in args.items()}
        (td / 'in.json').write_text(json.dumps(enc))
        env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'PYTHONDONTWRITEBYTECODE': '1'}
        for k in ('VECLIB_MAXIMUM_THREADS', 'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
            env[k] = '1'
        try:
            r = subprocess.run([sys.executable, '-I', str(runner), str(pathlib.Path(module_path).resolve()), func or '',
                                str(td / 'in.json'), str(td / 'out.json')], cwd=str(td), env=env,
                               capture_output=True, text=True, timeout=timeout_s)
        except subprocess.TimeoutExpired:
            return dict(ok=False, error=f'timeout after {timeout_s}s', scan=[], result=None, meta=None)
        if not (td / 'out.json').exists():
            return dict(ok=False, error=f'no output (exit {r.returncode}): {r.stderr[-800:]}', scan=[], result=None,
                        meta=None)
        res = json.loads((td / 'out.json').read_text())
        res['scan'] = []
        if res.get('ok') and isinstance(res.get('result'), dict) and res['result'].get('__nd__'):
            res['result'] = np.asarray(res['result']['data'], dtype=res['result']['dtype'])
        return res


class AttemptRecord:
    """Bounded attempts for a theorist's derivation: the harness records each attempt; past the budget the
    commission's open form is NOT-DERIVED-OPEN with this record."""

    def __init__(self, ck, max_attempts):
        self.ck, self.max = ck, int(max_attempts)
        self.ck.state.setdefault('attempts', [])

    def note(self, outcome, detail=''):
        self.ck.state['attempts'].append(dict(at=time.strftime('%Y-%m-%d %H:%M:%S%z'), outcome=outcome, detail=detail))

    def exhausted(self):
        return len(self.ck.state['attempts']) >= self.max


def smoke_fixture_path(root, slug):
    return pathlib.Path(root) / 'benchmarks' / 'lab' / slug / 'scratch'
