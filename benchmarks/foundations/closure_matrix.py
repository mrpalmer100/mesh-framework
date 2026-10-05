"""COMMISSION CLOSURE-MATRIX (charter analysis/CLOSURE_MATRIX_charter_LOCKED.md, locked 2026-10-04).
M1 the matrix of typed, cited cells between the programme's primitives (rows) and its closure targets (columns),
   plus the registered primitive-to-primitive relations (the constants ledger and the night's chain);
M2 the graph; M3 the gap count by union-find over IDENTITY and EXPONENT edges only (B-2); M4 the leverage table,
   recorded and not ranked (B-3); the verdict form from the count (B-5). Every cell carries a claim id or is NONE (B-1).
Types: IDENTITY, EXPONENT, BOUND, BLOCKED, NONE. 'tension' marks an identity whose joint numerical closure with the
others is registered as failing (FND-MATTER-040); it still joins (B-2) and the tension is reported with the class.
"""
import json, pathlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'analysis' / 'closure_matrix.npz'; OUT_JSON = ROOT / 'analysis' / 'closure_matrix.json'

# rows: primitives / open quantities. 'source': how the registry currently fixes it (derived / measured / imported /
# calibrated / adopted / registered-by-lock / unsourced). Gap classes are formed over everything not 'derived'.
ROWS = {
    'hbar':            ('imported (GRV-014; FND-183)', 'unsourced'),
    'a (m_e)':         ('fixed at the M-point from m_e and Sigma (FND-MATTER-044); irreducible (FND-MATTER-005)', 'measured-pinned'),
    'T0':              ('degeneracy line with a (ROPE_PARAMETERS; FND-MATTER-044)', 'measured-pinned'),
    'Sigma':           ('measured, lattice band (FND-030)', 'measured'),
    'd_c':             ('calibration (HBAR-005)', 'calibrated'),
    'nucleon unit':    ('input (PM-005)', 'measured'),
    'eps (Ca-40)':     ('one calibration (NUC-005)', 'calibrated'),
    'k/T0 = 2':        ('adopted (FND-129)', 'adopted'),
    'Pi = 2':          ('registered by lock (PRED-003-LOCK)', 'registered'),
    'g = l_q/a':       ('the single mesoscopic unknown (FND-044); hbar imported fixes it through R1', 'unsourced'),
    'kappa_pack':      ('floor only (FND-030)', 'unsourced'),
    'Poisson ratio':   ('imported from isotropic elasticity', 'imported'),
    'contact convention': ('adopted, fourth grant (FND-184)', 'adopted'),
    'V_0':             ('on-site orientation potential; no vacuum source (JUNCTION-LOCK f = 0)', 'unsourced'),
    'd (internal dim)': ('registered as 1; SU(2)/SU(3) need 3 to 8 (FND-185)', 'unsourced'),
    'electron model':  ('unbuilt (ELEC-062)', 'unsourced'),
    'rho (alpha)':     ('numerically fixed by measured alpha, mechanism owed (ELEC-083)', 'measured'),
    'w (kink width)':  ('regime [0.8, 2.8], unpinned (FND-STRAND-002)', 'unsourced'),
    'f (junction fraction)': ('0 at the registered level; 3.5 under the unadopted extension (JUNCTION-LOCK)', 'unsourced'),
    'N ~ 1e21':        ('the one pure number the bridge needs (FND-183)', 'unsourced'),
}
# primitive-to-primitive relations: (row_i, row_j, type, id, note)
REL = [
    ('hbar', 'T0', 'IDENTITY', 'GRV-093 (R1)', 'hbar = T0 l_q^2/(4 pi alpha c)'),
    ('hbar', 'g = l_q/a', 'IDENTITY', 'GRV-093 (R1); HBAR-005', 'same relation; the mesoscopic patch ~75 spacings'),
    ('hbar', 'rho (alpha)', 'IDENTITY', 'GRV-093 (R1)', 'alpha enters R1'),
    ('hbar', 'a (m_e)', 'IDENTITY', 'GRV-095/075 (R2)', 'G = c^3 a^2/(16 pi zeta hbar); a_Sak = 8 l_P; TENSION with FND-MATTER-044 by ~17 orders (FND-MATTER-040)'),
    ('a (m_e)', 'T0', 'IDENTITY', 'FND-MATTER-044', 'a and T0 from m_e and Sigma at the M-point'),
    ('a (m_e)', 'Sigma', 'IDENTITY', 'FND-MATTER-044; FND-017', 'the derived invariance anchored on Sigma'),
    ('hbar', 'N ~ 1e21', 'IDENTITY', 'FND-183', 'hbar = N A*, A* = T0 a^2 g(Pi)/c'),
    ('rho (alpha)', 'g = l_q/a', 'IDENTITY', 'ELEC-083 (conditional); FND-044', '1/alpha = 2 pi^2 rho^2 under the shared-origin hypothesis; N = 2 g^2'),
    ('V_0', 'w (kink width)', 'IDENTITY', 'STRAND-MASS-SCALE', 'w^2 = T0 r^2/(2 a V_0)'),
    ('V_0', 'f (junction fraction)', 'IDENTITY', 'NODE-STANDOFF', 'V_0 = f J, J = T0 a/2'),
    ('V_0', 'contact convention', 'IDENTITY', 'FND-184; CROSSING-PRICE', 'V_0 = n_x V_sec with A_c symbolic'),
    ('Pi = 2', 'T0', 'IDENTITY', 'PRED-003-LOCK', 'kappa = 2T/(eta a), eta = 1'),
    ('k/T0 = 2', 'T0', 'IDENTITY', 'FND-129', 'adopted ratio'),
    ('electron model', 'hbar', 'BLOCKED', 'ELEC-062', 'the electron sits behind the quantum layer'),
    ('nucleon unit', 'T0', 'BLOCKED', 'FND-MATTER-039 (R5); FND-MATTER-066', 'm c^2 = T0 L a + lambda dE_zp with the proton L unregistered, lambda blocked'),
    ('eps (Ca-40)', 'V_0', 'BLOCKED', 'EM-RECON-017', 'the nuclear contact import "waiting for a go"; no identity'),
    ('kappa_pack', 'Sigma', 'BOUND', 'FND-030', 'a floor; would make Sigma Sigma_vac'),
    ('d_c', 'hbar', 'BLOCKED', 'HBAR-005', 'no combination of the medium constants gives hbar'),
    ('d (internal dim)', 'hbar', 'NONE', 'FND-185', 'no registered relation to any other primitive'),
    ('Poisson ratio', 'a (m_e)', 'NONE', '-', 'moves gamma by a factor of a few; no identity'),
]
# columns: closure targets, with the primitives each needs (AND) and the registered cell type per primitive
COLS = {
    'hbar derived':                 {'N ~ 1e21': ('IDENTITY', 'FND-183')},
    'a (m_e) derived':              {'hbar': ('IDENTITY', 'GRV-095 (R2)'), 'N ~ 1e21': ('IDENTITY', 'FND-183: Task 1 and Task 2 are one equation')},
    'G absolute value':             {'hbar': ('EXPONENT', 'GRV-075 (0,2), zeta = 1.208'), 'a (m_e)': ('EXPONENT', 'GRV-075')},
    'alpha (rho) derived':          {'g = l_q/a': ('IDENTITY', 'GRV-093 (R1); FND-044'), 'rho (alpha)': ('IDENTITY', 'ELEC-083 conditional')},
    'm_p/m_e and the spectrum':     {'nucleon unit': ('BLOCKED', 'FND-MATTER-066: spectrum-gated'), 'hbar': ('BLOCKED', 'FND-MATTER-008/039: the zero-point lever lambda')},
    'strand mass scale (eV)':       {'V_0': ('IDENTITY', 'STRAND-MASS-SCALE: omega_min^2 = V_0 c^2/(T0 a r^2)')},
    "FND-182's number":             {'V_0': ('IDENTITY', 'STRAND-MASS-SCALE: E_c = (4 pi/5) V_0/(e a)'), 'f (junction fraction)': ('IDENTITY', 'NODE-STANDOFF')},
    'gauge structure beyond U(1)':  {'d (internal dim)': ('BLOCKED', 'FND-185: dimension 1 where 3 to 8 are needed')},
    'quantum dynamics (guidance)':  {'hbar': ('BLOCKED', 'QGATE-011: the guidance flow is imported; HBAR-005')},
    'magnet strength':              {'electron model': ('BLOCKED', 'ELEC-062; NORTH_STAR row 3'), 'hbar': ('BLOCKED', 'ELEC-062')},
    'nuclear shell/pairing, light isotopes': {'hbar': ('BLOCKED', 'FND-BOUND-001'), 'a (m_e)': ('BLOCKED', 'FND-BOUND-001')},
    'dispersion forces (C6)':       {'hbar': ('BLOCKED', 'FND-BOUND-001; CHEM-MET-001')},
    'frame-dragging magnitude':     {'a (m_e)': ('BLOCKED', 'GRV-126: waits on a_f = a/n_sub; n_sub underived (FND-087), candidate row')},
}
JOIN = {'IDENTITY', 'EXPONENT'}


def main():
    rows = list(ROWS)
    # M1 print the matrix
    print(f"[cm M1] {len(rows)} rows x {len(COLS)} columns; cells typed and cited; NONE written as NONE")
    for col, cells in COLS.items():
        print(f"[cm M1]   {col:38s} " + '; '.join(f"{r}: {t} ({i})" for r, (t, i) in cells.items()))
    # M3 union-find over JOIN edges among non-derived primitives
    parent = {r: r for r in rows}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[rb] = ra
    tension = []
    for a, b, t, i, note in REL:
        if t in JOIN:
            union(a, b)
            if 'TENSION' in note: tension.append((a, b, i, note))
    classes = {}
    for r in rows: classes.setdefault(find(r), []).append(r)
    # a class is a GAP if some column is blocked on, or needs, one of its members and no member is 'derived'
    blocked_on = {r: [] for r in rows}
    for col, cells in COLS.items():
        for r in cells: blocked_on[r].append(col)
    gap_classes = []
    print(f"[cm M3] union-find over IDENTITY/EXPONENT edges: {len(classes)} classes among {len(rows)} primitives")
    for k, mem in classes.items():
        cols = sorted({c for r in mem for c in blocked_on[r]})
        kind = 'GAP (columns depend on it)' if cols else 'input with no column on it'
        if cols: gap_classes.append((mem, cols))
        print(f"[cm M3]   class {{{', '.join(mem)}}}: {kind}" + (f"; columns: {', '.join(cols)}" if cols else ''))
    for a, b, i, note in tension:
        print(f"[cm M3]   TENSION inside the class joining {a} and {b} ({i}): {note}")
    # M4 leverage: columns that close if a class is supplied, IDENTITY/EXPONENT cells only, AND respected
    print("[cm M4] leverage (recorded, not ranked; B-3): columns whose every needed primitive is in the supplied class via IDENTITY/EXPONENT cells")
    lev = {}
    for mem, _ in gap_classes:
        closes = [col for col, cells in COLS.items()
                  if all(r in mem and t in JOIN for r, (t, i) in cells.items())]
        partial = [col for col, cells in COLS.items()
                   if any(r in mem for r in cells) and col not in closes]
        lev[', '.join(mem)] = (closes, partial)
        print(f"[cm M4]   supply {{{', '.join(mem)}}}: CLOSES {closes if closes else 'nothing by identity'}; TOUCHES (blocked-by or AND with another class) {partial}")
    n_gaps = len(gap_classes)
    verdict = 'ONE-FENCE' if n_gaps == 1 else f'N-GAPS (N = {n_gaps})'
    print(f"[cm VERDICT] {verdict}: {len(classes)} classes in all, {n_gaps} of them load-bearing (a column depends on them); the prior said three.")
    json.dump({'rows': ROWS, 'relations': REL, 'columns': COLS, 'classes': list(classes.values()),
               'gap_classes': [{'members': m, 'columns': c} for m, c in gap_classes], 'tension': tension,
               'leverage': lev, 'verdict': verdict}, open(OUT_JSON, 'w'), indent=1)
    np.savez(OUT, verdict=verdict, n_classes=len(classes), n_gaps=n_gaps)
    print(f"[cm] sealed -> {OUT.name}, {OUT_JSON.name}")


if __name__ == '__main__':
    main()
