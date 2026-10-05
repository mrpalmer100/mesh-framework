"""input_ledger.py -- the machine side of the input ledger (adopted 2026-10-04 from external review).

Scans every benchmark for literal occurrences of the measured or imported constants the programme treats as
inputs, records which claims consume which constants, and flags the one failure mode a 778-claim registry cannot
police by hand: a claim whose benchmark contains the very constant its title says it derives or predicts.

    python tools/input_ledger.py            # writes analysis/input_ledger.json and docs/INPUT_LEDGER.md, prints flags
    python tools/input_ledger.py --strict   # exit 1 if any CIRCULAR flag is raised (for CI, once the flags are adjudicated)

What it is: a literal scanner. It finds numbers, not reasoning; a constant passed in through a data file or
computed from another constant is not seen. What it is not: a judge. A CIRCULAR flag means 'read this one';
the registry's own text decides, and an adjudicated flag is silenced by listing the claim id in
analysis/input_ledger_adjudicated.json with one line of reason. BLIND means the benchmark contains none of the
listed measured constants (it may still consume registered mesh parameters T0, a, Sigma, which are listed
separately as REGISTERED).
"""
import argparse, json, pathlib, re, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLAIMS = ROOT / 'claims.yaml'
OUT_JSON = ROOT / 'analysis' / 'input_ledger.json'
OUT_MD = ROOT / 'docs' / 'INPUT_LEDGER.md'
ADJ = ROOT / 'analysis' / 'input_ledger_adjudicated.json'

# constant -> (provenance class, list of literal regexes). Regexes match the common spellings of each value;
# a mantissa prefix match (e.g. 1.602 or 1.6022 or 1.602176634) with the right exponent counts.
MEASURED = {
    'e (elementary charge, C)':      ('MEASURED', [r'\b1\.602\d*[eE]-19\b']),
    'hbar (J s)':                    ('IMPORTED (GRV-014)', [r'\b1\.054\d*[eE]-34\b', r'\b6\.626\d*[eE]-34\b']),
    'G (m^3 kg^-1 s^-2)':            ('MEASURED', [r'\b6\.67\d*[eE]-11\b']),
    'm_e (kg)':                      ('MEASURED', [r'\b9\.109\d*[eE]-31\b']),
    'm_p (kg)':                      ('MEASURED', [r'\b1\.672\d*[eE]-27\b', r'\b1\.6726\d*[eE]-27\b']),
    'm_p/m_e':                       ('MEASURED', [r'\b1836\.1\d*\b', r'\b1836\b(?![\d.])']),
    'alpha / 1/alpha':               ('MEASURED', [r'\b137\.03\d*\b', r'\b7\.297\d*[eE]-3\b', r'\b0\.0072973\d*\b']),
    'eps0 (F/m)':                    ('MEASURED', [r'\b8\.854\d*[eE]-12\b']),
    'mu0':                           ('MEASURED', [r'\b1\.2566\d*[eE]-6\b', r'\b4\s*\*\s*(?:np\.|math\.|sp\.)?pi\s*\*\s*1[eE]-7\b']),
    'k_B (J/K)':                     ('MEASURED', [r'\b1\.380\d*[eE]-23\b']),
    'H0':                            ('MEASURED', [r'\b67\.[0-9]\b', r'\b70\.0\b', r'\b2\.2\d*[eE]-18\b']),
    'Schwinger field (V/m)':         ('MEASURED/DERIVED (QED)', [r'\b1\.32\d*[eE]18\b']),
    'Planck length (m)':             ('DERIVED FROM hbar, G, c', [r'\b1\.616\d*[eE]-35\b']),
}
REGISTERED = {
    'T0 (J/m)':       [r'\b434\.?\d*\b', r'\b1599\.?\d*\b', r'\b2734\.?\d*\b'],
    'a (m)':          [r'\b6\.0\d*[eE]-17\b', r'\b1\.63[eE]-17\b', r'\b9\.53[eE]-18\b'],
    'd_c (m)':        [r'\b1\.87[eE]-19\b'],
    'Sigma (J/m^3)':  [r'\b3\.6\d*[eE]35\b', r'\b3\.7\d*[eE]35\b'],
    'c (m/s)':        [r'\b2\.99\d*[eE]8\b', r'\b299792458\b'],
    'eps (Ca-40 bond depth)': [r'\bCa-?40\b'],
}
# title keywords that announce a derivation or prediction OF a constant (checked against the constant's own literal)
DERIVE_WORDS = r'(DERIV|PREDICT|COMPUT|FROM FIRST PRINCIPLES|ZERO (FREE )?PARAMETER|PARAMETER-FREE|NO FIT)'
TARGET_WORDS = {
    'alpha / 1/alpha': r'(\balpha\b|fine[- ]structure|1/alpha)',
    'G (m^3 kg^-1 s^-2)': r'(\bG\b(?! ?=)|newton\'?s? constant|gravitational constant|absolute (strength|scale) of gravity)',
    'hbar (J s)': r'(\bhbar\b|planck\'?s? constant)',
    'm_e (kg)': r'(electron mass|\bm_e\b)',
    'm_p/m_e': r'(1836|m_p/m_e|mass ratio)',
    'e (elementary charge, C)': r'(elementary charge|\bcharge e\b|unit charge)',
}


def scan(text, table):
    hits = {}
    for name, spec in table.items():
        pats = spec[1] if isinstance(spec, tuple) else spec
        n = sum(len(re.findall(p, text)) for p in pats)
        if n:
            hits[name] = n
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()
    claims = yaml.safe_load(CLAIMS.read_text())['claims']
    adjudicated = json.loads(ADJ.read_text()) if ADJ.exists() else {}
    ledger, flags, blind, consumers = {}, [], [], {k: set() for k in list(MEASURED) + list(REGISTERED)}
    for c in claims:
        b = c.get('benchmark')
        if not b:
            continue
        p = ROOT / b
        if not p.exists():
            continue
        txt = p.read_text(errors='replace')
        # strip comments and docstrings crudely so that a constant quoted in a comment does not count as consumed
        code = re.sub(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', '', txt)
        code = '\n'.join(l.split('#', 1)[0] for l in code.splitlines())
        m = scan(code, MEASURED); r = scan(code, REGISTERED)
        ledger[c['id']] = {'benchmark': b, 'status': c['status'], 'measured': m, 'registered': r}
        for k in m: consumers[k].add(c['id'])
        for k in r: consumers[k].add(c['id'])
        if not m:
            blind.append(c['id'])
        title = c['title']
        if re.search(DERIVE_WORDS, title, re.I):
            for const, kw in TARGET_WORDS.items():
                near = re.search(DERIVE_WORDS + r'[^.;:]{0,60}?' + kw, title, re.I) or re.search(kw + r'[^.;:]{0,60}?' + DERIVE_WORDS, title, re.I)
                if const in m and near:
                    flags.append({'id': c['id'], 'constant': const, 'hits': m[const], 'benchmark': b,
                                  'adjudicated': adjudicated.get(c['id']), 'title': title[:160]})
    live = [f for f in flags if not f['adjudicated']]
    OUT_JSON.parent.mkdir(exist_ok=True)
    OUT_JSON.write_text(json.dumps({'claims': ledger, 'flags': flags, 'blind': blind,
                                    'consumers': {k: sorted(v) for k, v in consumers.items()}}, indent=1) + '\n')
    # the markdown summary
    n = len(ledger)
    L = ['# The input ledger, machine side (generated by tools/input_ledger.py; do not edit)', '',
         f'Benchmarks scanned: {n} (every claim with a benchmark field). BLIND (no measured constant literal in the code): {len(blind)}. '
         f'CIRCULAR flags: {len(flags)} ({len(live)} unadjudicated). A flag means "read this one"; the registry decides.', '',
         '## Consumers per constant', '', '| constant | provenance | benchmarks consuming it | examples |', '|---|---|---|---|']
    for k, spec in MEASURED.items():
        ids = sorted(consumers[k]); L.append(f"| {k} | {spec[0]} | {len(ids)} | {', '.join(ids[:6])}{' ...' if len(ids) > 6 else ''} |")
    for k in REGISTERED:
        ids = sorted(consumers[k]); L.append(f"| {k} | REGISTERED (ROPE_PARAMETERS) | {len(ids)} | {', '.join(ids[:6])}{' ...' if len(ids) > 6 else ''} |")
    L += ['', '## CIRCULAR flags (title announces a derivation or prediction of a constant whose literal the benchmark contains)', '']
    if not flags:
        L.append('None.')
    for f in flags:
        L.append(f"- **{f['id']}** consumes {f['constant']} ({f['hits']} literal{'s' if f['hits'] > 1 else ''}) in {f['benchmark']}: "
                 + (f"adjudicated: {f['adjudicated']}" if f['adjudicated'] else 'UNADJUDICATED') + f"  \n  {f['title']}")
    L += ['', '## What the scanner cannot see', '',
          'Constants passed through data files, computed from other constants, or spelled in a form not in the table. '
          'A BLIND benchmark is blind to these literals, not certified parameter-free; a D1 grade still needs the reading. '
          'Adjudications live in analysis/input_ledger_adjudicated.json (claim id: one line of reason).']
    OUT_MD.write_text('\n'.join(L) + '\n')
    print(f'[ledger] {n} benchmarks scanned; {len(blind)} BLIND; {len(flags)} CIRCULAR flags ({len(live)} unadjudicated) -> {OUT_MD.relative_to(ROOT)}, {OUT_JSON.relative_to(ROOT)}')
    for f in flags:
        print(f"[ledger] {'FLAG' if not f['adjudicated'] else 'adj '} {f['id']:18s} {f['constant']:26s} x{f['hits']}  {f['benchmark']}")
    if a.strict and live:
        sys.exit(1)


if __name__ == '__main__':
    main()
