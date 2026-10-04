"""COMMISSION COMPOSITE-SELECT, Leg B verdict (QB) and Leg C price table (QC), computed ONCE from the
sealed checkpoint analysis/composite_legB_ckpt.pkl after 'LADDER COMPLETE'. Charter
analysis/COMPOSITE_SELECT_charter_LOCKED.md, D3/D4/D5 and the QB forms, verbatim:
  D(q)  = rate at the full-bar point nearest A2 = 0.0048 over rate at the full-bar point nearest 0.0063
          (Q-SWEEP stage 1's definition; nearest-point pairing; RMS < 1e-8 and closure < 1e-6 only).
  QB    = Spearman rho of D against q (value) and against N1 (order) over the cells with a D.
          RAT-SMOOTH |rho_q| >= 0.8 and |rho_N1| < 0.5; RAT-RESONANT |rho_N1| >= 0.8 and |rho_q| < 0.5;
          RAT-MIXED both in [0.5, 0.8) or both >= 0.8; RAT-OPEN fewer than six cells with a D.
  QC    = a TABLE: Sigma_wave (FND-135's closed form: truestate_stage2.Grid.price on the state exported
          by to_stage2) for (i) A2* if QA selected (Leg A: COMP-PIN-UNREACHABLE, so none), (ii) the deepest
          gated member at the cell nearest 1.492, (iii) the level-1 retreat 2.598; Prediction 32's upper
          edge as the dynamical share 1 - T0/Sigma_wave (FND-132: excess over booked / total; reproduces
          the exact lower edge 0.615 at 2.598); the kb-ceiling consequence is left to the desk (FND-141).
The four pre-existing cells enter the ladder as data: 3/2 from the registered stage-1 constants
(6.5e-4 / 6.8e-5), 4/3 and 5/3 from analysis/qsweep_stage1_ckpt.pkl by the same nearest-point rule, 5/4
from analysis/composite_legB_existing_D.json if the desk has entered it from FND-163/164's records
(the script says which cells it could not load; it never invents one).
Written 2026-10-04 ahead of LADDER COMPLETE and dry-run on synthetic checkpoints (tools/legb_verdict_dryrun.py)."""
import pickle, pathlib, sys, json, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from benchmarks.foundations import qsweep_stage1 as q1       # noqa
CKPT = ROOT / 'analysis' / 'composite_legB_ckpt.pkl'
Q1CK = ROOT / 'analysis' / 'qsweep_stage1_ckpt.pkl'
OVERRIDE = ROOT / 'analysis' / 'composite_legB_existing_D.json'
CELLS = [('7/5', 5, 7), ('8/5', 5, 8), ('10/7', 7, 10), ('11/7', 7, 11), ('13/9', 9, 13), ('14/9', 9, 14)]
EXISTING = [('3/2', 2, 3), ('4/3', 3, 4), ('5/3', 3, 5), ('5/4', 4, 5)]
LO, HI, QSTAR = 0.0048, 0.0063, 1.4920
RETREAT = 2.598


def full_bar(m): return m['rms'] < q1.RMS_BAR and m['clos'] < q1.CLOSURE_BAR


def D_from_meas(meas):
    pts = [(m['A2'], m['rate'], m) for m in meas if full_bar(m)]
    if not pts: return None
    lo = min(pts, key=lambda p: abs(p[0] - LO)); hi = min(pts, key=lambda p: abs(p[0] - HI))
    if hi[1] <= 0 or lo is hi: return None
    return dict(D=lo[1] / hi[1], A2_lo=lo[0], A2_hi=hi[0], rate_lo=lo[1], rate_hi=hi[1], om2_lo=lo[2]['om2'],
                A2_max=max(p[0] for p in pts), n_full=len(pts))


def spearman(x, y):
    from scipy.stats import spearmanr
    return float(spearmanr(x, y).statistic)


def existing_D():
    out = {'3/2': dict(D36=6.5e-4 / 6.8e-5, source='Q-SWEEP stage 1 registered constants (FND-147)')}
    if Q1CK.exists():
        st = pickle.loads(Q1CK.read_bytes())
        for tag, key in (('4/3', 'q4/3'), ('5/3', 'q5/3')):
            q = st.get(key, {}); lo = q1.nearest(q.get('rates_lo', []), LO); hi = q1.nearest(q.get('rates_hi', []), HI)
            if lo and hi and hi[1] > 0: out[tag] = dict(D36=lo[1] / hi[1], source=f'qsweep_stage1_ckpt {key} (FND-147)')
    if OVERRIDE.exists():
        for tag, rec in json.loads(OVERRIDE.read_text()).items(): out[tag] = dict(rec, source=rec.get('source', 'desk entry'))
    return out


def main(path=CKPT, do_price=True, include_existing=True):
    """include_existing=False exists for the dry run only; the charter's ladder includes the four existing cells."""
    st = pickle.loads(pathlib.Path(path).read_bytes())
    print("[legB verdict] cells of the ladder:")
    table = {}
    for tag, N1, N2 in CELLS:
        c = st.get(f'cell|{tag}')
        if c is None: print(f"[legB verdict]   {tag}: not opened"); continue
        d36 = D_from_meas(c['prof36']['meas']); d54 = D_from_meas(c['prof54']['meas'])
        table[tag] = dict(N1=N1, q=N2 / N1, phase=c['phase'], halt=c['halt'], D36=d36, D54=d54, cell=c)
        f = lambda d: f"D {d['D']:.2f}x (rate {d['rate_lo']:.3e} @ {d['A2_lo']:.5f} -> {d['rate_hi']:.3e} @ {d['A2_hi']:.5f}; A2_max {d['A2_max']:.5f}; om2 {d['om2_lo']:+.5f}; {d['n_full']} full-bar pts)" if d else "no D (fewer than two full-bar points bracketing the targets)"
        print(f"[legB verdict]   {tag} (q {N2 / N1:.4f}, N1 {N1}) phase {c['phase']} halt {c['halt']}: 36: {f(d36)}; 54: {f(d54)}")
    unfinished = [t for t, r in table.items() if r['phase'] != 'done' and not r['halt']]
    if unfinished: print(f"[legB verdict] cells still running: {unfinished}; checkpoint is not terminal (verdict refused)"); return 'INCOMPLETE'
    ex = existing_D() if include_existing else {}
    for tag, N1, N2 in EXISTING:
        if tag in ex: print(f"[legB verdict]   existing {tag} (q {N2 / N1:.4f}, N1 {N1}): D36 {ex[tag].get('D36', float('nan')):.2f}x" + (f", D54 {ex[tag]['D54']:.2f}x" if 'D54' in ex[tag] else "") + f"  [{ex[tag]['source']}]")
        else: print(f"[legB verdict]   existing {tag}: NOT LOADABLE from disk; enter from the registered records into {OVERRIDE.name} or it stays out of the ladder")
    verdicts = {}
    for grid in ('36', '54'):
        rows = []
        for tag, N1, N2 in CELLS:
            r = table.get(tag); d = r and r[f'D{grid}']
            if d: rows.append((tag, N2 / N1, N1, d['D']))
        for tag, N1, N2 in EXISTING:
            if tag in ex and f'D{grid}' in ex[tag]: rows.append((tag, N2 / N1, N1, ex[tag][f'D{grid}']))
        print(f"[legB verdict] ladder at NP = {grid}: {len(rows)} cells with a D: " + ', '.join(f"{t} {D:.2f}x" for t, _, _, D in rows))
        if len(rows) < 6: verdicts[grid] = ('RAT-OPEN', None, None); print(f"[legB verdict]   NP {grid}: RAT-OPEN (fewer than six cells)"); continue
        rq = spearman([r[1] for r in rows], [r[3] for r in rows]); rn = spearman([r[2] for r in rows], [r[3] for r in rows])
        if abs(rq) >= 0.8 and abs(rn) < 0.5: v = 'RAT-SMOOTH'
        elif abs(rn) >= 0.8 and abs(rq) < 0.5: v = 'RAT-RESONANT'
        elif (0.5 <= abs(rq) < 0.8 and 0.5 <= abs(rn) < 0.8) or (abs(rq) >= 0.8 and abs(rn) >= 0.8): v = 'RAT-MIXED'
        else: v = 'NO CALL (outside the three forms: one correlation weak, the other intermediate)'
        verdicts[grid] = (v, rq, rn); print(f"[legB verdict]   NP {grid}: rho(D, q) {rq:+.3f}  rho(D, N1) {rn:+.3f}  -> {v}")
    # QC table
    print("[legB verdict] QC price table (Sigma_wave in units of T0; share = 1 - 1/Sigma_wave; kb ceiling to the desk, FND-141):")
    print(f"[legB verdict]   (i)   A2* selected by QA: none (Leg A: COMP-PIN-UNREACHABLE, FND-169)")
    near = min(((tag, N1, N2) for tag, N1, N2 in CELLS if tag in table), key=lambda c: abs(c[2] / c[1] - QSTAR), default=None)
    if near and do_price:
        tag, N1, N2 = near; c = table[tag]['cell']
        for grid, NP in (('36', 36), ('54', 54)):
            P = c[f'prof{grid}']; pts = [(m['A2'], i) for i, m in enumerate(P['meas']) if full_bar(m)]
            if not pts: print(f"[legB verdict]   (ii)  cell {tag} at NP {NP}: no full-bar member"); continue
            A2m, i = max(pts); x = np.asarray(P['states'][i + 2], float); T = q1.QTGrid(48 * N1, NP, N1, N2)
            S, ke = T.G2.price(T.to_stage2(x))
            print(f"[legB verdict]   (ii)  deepest gated member, cell {tag} (q {N2 / N1:.4f}) at {48 * N1}x{NP}, A2 {A2m:.5f}: Sigma_wave {S:.4f} T0 (ke {ke:.4f}); P32 upper edge {1 - 1 / S:.4f}; grid scope NP {NP}")
    print(f"[legB verdict]   (iii) level-1 retreat: Sigma_wave {RETREAT:.3f} T0; P32 edge {1 - 1 / RETREAT:.4f} (the exact lower edge)")
    v36 = verdicts.get('36', ('RAT-OPEN',))[0]; v54 = verdicts.get('54', ('RAT-OPEN',))[0]
    print(f"[legB verdict] QB VERDICT: NP 36 {v36}; NP 54 {v54}")
    return v36, v54


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else CKPT)
