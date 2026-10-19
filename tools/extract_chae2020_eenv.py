"""Extract the e_env column of Chae et al. 2020 (ApJ 904, 51; arXiv:2009.11525v2, erratum-corrected) Table 2 from the
authors' LaTeX source into data/sparc_efe/chae2020_eN.csv (header galaxy,eN_a0). Prints the row count, sha256 and
structural checks only; never a value. Usage: python extract_eenv.py ms_r2.tex out.csv"""
import csv, hashlib, re, sys
tex = open(sys.argv[1], encoding='utf-8').read()
rows, seen = [], set()
in_tab = False
for line in tex.splitlines():
    s = line.strip()
    if s.startswith(r'\caption{') and 'Fitted model parameters' in s:
        in_tab = True
        continue
    if in_tab and s.startswith(r'\end{tabular}'):
        in_tab = False
        continue
    if not in_tab or '&' not in s or s.startswith('galaxy') or s.startswith(r'\hline'):
        continue
    cells = [c.strip() for c in s.rstrip('\\').split('&')]
    if len(cells) != 9:
        sys.exit(f'row with {len(cells)} cells: {cells[0]!r}')
    name = re.sub(r'\$\^\{\\rm a\}\$', '', cells[0]).strip()   # footnote a (low S/N velocities) is the authors' fit flag, not an e_env flag
    m = re.match(r'\$\s*(-?[0-9.]+)\s*_\{', cells[3])
    if not m:
        sys.exit(f'unparsed e_env cell for {name!r}')
    if name in seen:
        sys.exit(f'duplicate galaxy {name!r}')
    seen.add(name)
    rows.append((name, m.group(1)))
if not (150 <= len(rows) <= 175):
    sys.exit(f'unexpected row count {len(rows)}')
vals = [float(v) for _, v in rows]
if min(vals) < 0 or max(vals) > 1:
    sys.exit('e_env out of the expected [0, 1] range')
with open(sys.argv[2], 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['galaxy', 'eN_a0'])
    w.writerows(rows)
h = hashlib.sha256(open(sys.argv[2], 'rb').read()).hexdigest()
# erratum check: the original paper's text gives NGC5055 e_env = 0.094 and NGC5033 0.102; the corrected table differs
d = dict(rows)
corrected = d.get('NGC5055') != '0.094' and d.get('NGC5033') != '0.102'
print(f'rows {len(rows)}; names unique; e_env in [0,1]; erratum-corrected values for NGC5033/5055: {corrected}')
print(f'sha256 {h}')
