"""ame2020_newset.py -- the NUC-NEW-1 evidence set: the nuclides measured between AME2012 and AME2020.

Design sealed first: analysis/NUC_NEW_1_design_SEALED.md (section 2). This tool is run ONCE, on the machine that
holds the AME2020 file (the author's or the adjudicator's; never the sandbox), and it writes

    analysis/holdout/NUC_NEW_1/labels.txt         'Z N' rows, sorted: the file the models may read
    analysis/holdout/NUC_NEW_1/sealed/test.txt    'Z N M' rows (mass excess, MeV; the AME2012.txt layout): read once
    analysis/holdout/NUC_NEW_1/MANIFEST.json      hashes, counts, the anchor check, who and when

    python tools/ame2020_newset.py --ame2020 /path/to/mass_1.mas20 --run-by "author"

and, afterwards, with --audit (design NUC_NEW_2 C-6), reads the same file and the hold-out it built and writes

    analysis/holdout/NUC_NEW_1/AUDIT.json           the real-file sanity record: the file's sha256, the counts, and
                                                    for the SHARED rows (AME2012 rows experimental in both tables)
                                                    how many agree within --tol MeV, how many do not, and the largest
                                                    absolute shift (AME2012 rows: not evidence). It reads no new row.

    python tools/ame2020_newset.py --ame2020 /path/to/mass_1.mas20 --run-by "author" --audit

The test set T is every (Z, N) whose AME2020 mass excess is EXPERIMENTAL (no '#' in the field), with A >= 12, that is
not a row of data/ame2012/AME2012.txt. It prints counts and hashes only; it never prints a mass of a new row. It
refuses to overwrite an existing hold-out and refuses the parse unless the five anchors (C-12, O-16, Ca-40, Fe-56,
Pb-208, all AME2012 rows) agree with AME2012.txt within 0.010 MeV (design C-4).

The AME2020 layout (file header 'format : a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,f10.5,1x,a2,f13.5,f11.5,
1x,i3,1x,f13.6,f12.6'): columns 5-9 N, 10-14 Z, 15-19 A, 29-42 mass excess in keV. A line is a data row when those
three integer fields parse and N + Z = A; header lines never do. A systematics value carries '#' in the field.
"""
import argparse, hashlib, json, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
AME2012 = ROOT / 'data' / 'ame2012' / 'AME2012.txt'
ANCHORS = [(6, 6), (8, 8), (20, 20), (26, 30), (82, 126)]          # C-12, O-16, Ca-40, Fe-56, Pb-208
ANCHOR_TOL_MEV = 0.010
MIN_A = 12
MIN_ROWS_PARSED = 2000                                              # fewer experimental rows than this is a misparse


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def parse_mas20(text):
    """Returns {(Z, N): (excess_MeV or None, flagged)} for every data row; None when the value is from systematics."""
    rows = {}
    for line in text.splitlines():
        if len(line) < 42:
            continue
        try:
            n, z, a = int(line[4:9]), int(line[9:14]), int(line[14:19])
        except ValueError:
            continue
        if n + z != a or n < 0 or z < 0:
            continue
        field = line[28:42]
        if '#' in line[28:43]:                  # a systematics value carries '#' in or at the end of the field
            rows[(z, n)] = (None, True)
            continue
        try:
            rows[(z, n)] = (float(field) / 1000.0, False)
        except ValueError:
            continue
    return rows


def read_ame2012(path=AME2012):
    out = {}
    for l in pathlib.Path(path).read_text().splitlines():
        t = l.split()
        if len(t) != 3:
            continue
        try:
            out[(int(t[0]), int(t[1]))] = float(t[2])
        except ValueError:
            continue
    return out


def build(ame2020_text, ame2012):
    """The set and the counts, as a dict; pure (no files). Raises ValueError on a refused parse."""
    rows = parse_mas20(ame2020_text)
    exp = {k: v for k, (v, flagged) in rows.items() if not flagged}
    if len(exp) < MIN_ROWS_PARSED:
        raise ValueError(f'parsed only {len(exp)} experimental rows; the layout was not recognised')
    anchors = []
    for z, n in ANCHORS:
        if (z, n) not in exp or (z, n) not in ame2012:
            raise ValueError(f'anchor Z={z} N={n} missing from one table')
        d = exp[(z, n)] - ame2012[(z, n)]
        anchors.append({'Z': z, 'N': n, 'delta_MeV': d, 'pass': abs(d) <= ANCHOR_TOL_MEV})
    if not all(a['pass'] for a in anchors):
        raise ValueError('anchor check failed: ' + '; '.join(f"Z={a['Z']} N={a['N']} delta {a['delta_MeV']:+.4f} MeV" for a in anchors))
    shared = [k for k in exp if k in ame2012]
    dropped = [k for k in ame2012 if k not in exp]
    new_all = [k for k in exp if k not in ame2012]
    new_light = sorted(k for k in new_all if k[0] + k[1] < MIN_A)
    test = sorted(k for k in new_all if k[0] + k[1] >= MIN_A)
    return dict(test=test, test_excess={k: exp[k] for k in test}, anchors=anchors,
                counts=dict(ame2020_rows=len(rows), ame2020_experimental=len(exp), ame2020_systematics=len(rows) - len(exp),
                            ame2012_rows=len(ame2012), shared=len(shared), ame2012_absent_from_ame2020=len(dropped),
                            new_a_below_12=len(new_light), n_test=len(test)))


def audit(ame2020_text, ame2012, tol_mev):
    """The real-file sanity record (design NUC_NEW_2 C-6): pure; no new row is read or returned."""
    rows = parse_mas20(ame2020_text)
    exp = {k: v for k, (v, flagged) in rows.items() if not flagged}
    shared = [k for k in ame2012 if k in exp]
    deltas = [abs(exp[k] - ame2012[k]) for k in shared]
    within = sum(d <= tol_mev for d in deltas)
    return dict(tol_MeV=tol_mev, shared=len(shared), within=within, beyond=len(shared) - within,
                fraction_within=(within / len(shared)) if shared else 0.0,
                max_abs_shift_MeV=(max(deltas) if deltas else 0.0),
                counts=dict(ame2020_rows=len(rows), ame2020_experimental=len(exp), ame2020_systematics=len(rows) - len(exp),
                            ame2012_rows=len(ame2012), ame2012_absent_from_ame2020=len([k for k in ame2012 if k not in exp])))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ame2020', required=True, help='the AMDC file mass_1.mas20 (or mass20.txt)')
    ap.add_argument('--run-by', required=True, help='who ran it')
    ap.add_argument('--name', default='NUC_NEW_1')
    ap.add_argument('--out-root', default=str(ROOT), help='(smoke only) a different root for analysis/holdout/<name>')
    ap.add_argument('--audit', action='store_true', help='write AUDIT.json for an existing hold-out (design NUC_NEW_2 C-6)')
    ap.add_argument('--tol', type=float, default=0.100, help='audit tolerance on the shared rows, MeV (design C-6: 0.100)')
    a = ap.parse_args()
    out = pathlib.Path(a.out_root) / 'analysis' / 'holdout' / a.name
    src = pathlib.Path(a.ame2020)
    if a.audit:
        if not out.exists():
            sys.exit(f'[newset] REFUSED: {out} does not exist; the audit follows the build.')
        ap_ = out / 'AUDIT.json'
        if ap_.exists():
            sys.exit(f'[newset] REFUSED: {ap_} exists. The audit is written once.')
        man = json.loads((out / 'MANIFEST.json').read_text())
        h = sha256(src)
        if h != man['ame2020_sha256']:
            sys.exit(f'[newset] REFUSED: {src.name} sha256 {h[:16]}... is not the file the hold-out was built from. Nothing written.')
        r = audit(src.read_text(errors='replace'), read_ame2012(), a.tol)
        r.update(name=a.name, run_by=a.run_by, run_at_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                 ame2020_sha256=h, ame2012_sha256=sha256(AME2012), labels_sha256=sha256(out / 'labels.txt'),
                 test_sha256=sha256(out / 'sealed' / 'test.txt') if (out / 'sealed' / 'test.txt').exists() else None,
                 rule='Shared rows only (AME2012 rows experimental in both tables); no new row is read. Written once.')
        ap_.write_text(json.dumps(r, indent=1) + '\n')
        print(f"[newset] AUDIT {a.name}: shared rows {r['shared']}; within {a.tol:.3f} MeV: {r['within']} "
              f"({100 * r['fraction_within']:.2f} percent); beyond: {r['beyond']}; largest shift among shared rows "
              f"{r['max_abs_shift_MeV']:.4f} MeV; counts {r['counts']}; run by {a.run_by}")
        print(f"[newset] audit sha256 {sha256(ap_)}  (analysis/holdout/{a.name}/AUDIT.json)")
        return
    if out.exists():
        sys.exit(f'[newset] REFUSED: {out} exists. The set is built once; use a new --name.')
    src = pathlib.Path(a.ame2020)
    try:
        r = build(src.read_text(errors='replace'), read_ame2012())
    except ValueError as e:
        sys.exit(f'[newset] REFUSED: {e}. Nothing written.')
    (out / 'sealed').mkdir(parents=True)
    labels, test = out / 'labels.txt', out / 'sealed' / 'test.txt'
    labels.write_text('Z N\n' + ''.join(f'{z} {n}\n' for z, n in r['test']))
    test.write_text('Z N M\n' + ''.join(f'{z} {n} {r["test_excess"][(z, n)]!r}\n' for z, n in r['test']))
    man = {
        'name': a.name, 'design': 'analysis/NUC_NEW_1_design_SEALED.md (section 2)', 'run_by': a.run_by,
        'run_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'ame2020_file': src.name, 'ame2020_sha256': sha256(src), 'ame2012_sha256': sha256(AME2012),
        'min_a': MIN_A, 'anchor_tol_MeV': ANCHOR_TOL_MEV, 'anchors': r['anchors'], 'counts': r['counts'],
        'n_test': r['counts']['n_test'], 'test_zn': [[z, n] for z, n in r['test']],
        'labels_sha256': sha256(labels), 'test_sha256': sha256(test),
        'rule': 'The models and the sandbox read labels.txt only. sealed/test.txt is read once, by the commission verdict, '
                'after the predictions are sealed. No row is added or removed afterwards.',
    }
    (out / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
    c = r['counts']
    print(f"[newset] {a.name}: AME2020 {c['ame2020_rows']} rows, {c['ame2020_experimental']} experimental, "
          f"{c['ame2020_systematics']} from systematics; AME2012 {c['ame2012_rows']} rows; shared {c['shared']}; "
          f"AME2012 rows absent from AME2020 {c['ame2012_absent_from_ame2020']}; new with A < 12 {c['new_a_below_12']}; "
          f"TEST SET |T| = {c['n_test']} (new, experimental, A >= 12); run by {a.run_by}")
    print('[newset] anchors: ' + '; '.join(f"Z={x['Z']} N={x['N']} delta {x['delta_MeV']:+.4f} MeV" for x in r['anchors']) + '  (all within 0.010)')
    print('[newset] paste into the charter at lock:')
    print(f"  ame2020 sha256 {man['ame2020_sha256']}  ({src.name})")
    print(f"  labels  sha256 {man['labels_sha256']}  (analysis/holdout/{a.name}/labels.txt)")
    print(f"  test    sha256 {man['test_sha256']}  (analysis/holdout/{a.name}/sealed/test.txt; NOT to be read)")


if __name__ == '__main__':
    main()
