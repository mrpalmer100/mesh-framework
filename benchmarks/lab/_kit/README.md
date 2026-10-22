# labkit: the harness kit for lab commissions

One reviewed implementation of the plumbing every commission driver and verdict script needs, so a draft does
not reimplement it and the reviewers do not reject it in a new place each round. Written 2026-10-21 after
ELEC-G-1 passed its physics review twice and was withdrawn on harness defects in three rounds.

| Reviewer objection (checklist item) | What the kit does |
|---|---|
| verdict reads a partial or mixed-version checkpoint (F) | `Verdict._validate` refuses: no terminal record, a halted run, a unit not done, locked files changed since the run (manifest re-hashed), a broken seal, a configuration that differs |
| evidence published before the form is decided (F) | `form_rule` writes to a buffer; nothing prints until every token is decided; an exception renders the open form with the buffer discarded |
| a second verdict invocation recomputes or overwrites (F) | exclusive `O_EXCL` reservation, atomic log write, the second invocation prints REFUSED and exits 1 |
| exceptions escape instead of a durable halt (J) | any exception in a unit becomes a `halt` record plus the terminal line; the verdict renders the open form with the reason |
| driver state not bound to the locked files (F, H) | manifest hashes bound at the first unit and verified at every later one; a change halts the run |
| smoke touches the evidence checkpoint (J) | separate files, `smoke=True` inside the state; an evidence verdict refuses a smoke file and a smoke verdict withholds all forms |
| NaN, zero denominators, empty arrays reach a comparison (C, E) | `finite`, `finite_array`, `rel`, `require` raise `Halt` with the reason |
| derivation module imported before a static scan (I) | `static_scan` (import and name allowlist) before any import; `run_isolated` evaluates in `python -I` with an empty environment, a scratch cwd, a time limit and a JSON channel |
| unbounded derivation attempts (G) | `AttemptRecord` against a declared maximum |

Use: copy `example_driver.py` and `example_verdict.py`; put the locked numbers in one `CONFIG` dict shared by
both; list every locked file in `MANIFEST`; write each unit as a function of the checkpoint that seals raw
outputs before any statistic is computed from them; write `form_rule(ck, out)` to recompute the locked
statistics from the seals and return the decisions. The kit's tests are `test_labkit.py` (run it directly).

The kit is an instrument: list `benchmarks/lab/_kit/labkit.py` under `instrument:` in the charter's lab block so
its bytes are hashed at lock.
