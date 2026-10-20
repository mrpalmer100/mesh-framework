"""COMPOSITE-SELECT Leg B: the verifier's check of the shipped record (2026-10-20). Runs the LOCKED verdict script
(benchmarks/foundations/composite_legB_verdict.py, untouched) on the repository extract of the sealed checkpoint
(analysis/composite_legB_ckpt_verdict_extract.pkl, tools/legb_ckpt_extract.py) and compares its output line for
line with the log of record (analysis/COMPOSITE_SELECT_legB_verdict.log, computed once on the Mac mini). Writes
nothing. Exit 0 if identical, 1 otherwise."""
import contextlib
import hashlib
import io
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations import composite_legB_verdict as V      # noqa: E402

EXTRACT = ROOT / 'analysis' / 'composite_legB_ckpt_verdict_extract.pkl'
LOG = ROOT / 'analysis' / 'COMPOSITE_SELECT_legB_verdict.log'
SHA_EXTRACT = '3d4a5a06a9a9eefa2c5fefcfe1e322598a27973665001ee19824520df9a6040d'
SHA_LOG = '85c263ed452ed9d23f04bc62c998be2346f95531ce02e0741dbc7ebf38f51015'


def main():
    ok = True
    for p, sha in ((EXTRACT, SHA_EXTRACT), (LOG, SHA_LOG)):
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        print(f'[legB verify] {p.name} sha256 {h} {"ok" if h == sha else "MISMATCH (expected " + sha + ")"}')
        ok &= h == sha
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        V.main(EXTRACT)
    got = [l.rstrip() for l in buf.getvalue().splitlines()]
    exp = [l.rstrip() for l in LOG.read_text().splitlines()]
    same = got == exp
    print(f'[legB verify] verdict script on the extract: {len(got)} lines, {"identical to" if same else "DIFFERS from"} the log of record')
    if not same:
        for a, b in zip(got, exp):
            if a != b:
                print(f'  got: {a}\n  exp: {b}'); break
    print(f'[legB verify] QB VERDICT line: {[l for l in got if "QB VERDICT" in l]}')
    return 0 if (ok and same) else 1


if __name__ == '__main__':
    sys.exit(main())
