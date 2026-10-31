"""RING-WAVE-STABILITY-4: the locked statistics and form deciders (numpy only; no JAX, no checkpoint access).

Imported by driver.py (the stat_credential unit runs these on closed-form synthetic series) and by verdict.py (which
runs them on the sealed series). Every threshold comes from the CONFIG dict of driver.py, passed in as `cfg`.
Nothing here integrates anything. All statements are conditional on action (i) (the charter's premise P1).
"""
import math
import numpy as np

# the columns of every sealed per-run series (sampled every cfg['sample_stride'] steps)
COLS = (['m', 't', 'E', 'Jz', 'Pn', 'Q', 'R_mean', 'R_end_ratio', 'beta', 'seg_spread', 'L', 'Phidot_mean', 'z_mean']
        + [f'ar{n}' for n in range(1, 7)] + [f'az{n}' for n in range(1, 7)] + [f'aw{n}' for n in range(1, 7)])
CI = {c: i for i, c in enumerate(COLS)}

Q1_PROBES = ('W1', 'W2', 'R0')
SHAPE_BEARING = ('S3', 'S4', 'Z2', 'Z3')
SHAPE_ALL = ('S2', 'S3', 'S4', 'Z2', 'Z3')


def block_index(m, spp, nb):
    return np.minimum(nb, np.asarray(m) // spp + 1)


def block_max(m, A, spp, nb, fail_step=None):
    """Block maxima A_k (k = 1..nb) over finite samples; samples at or after fail_step are excluded; NaN where empty."""
    m = np.asarray(m); A = np.asarray(A, float)
    keep = np.isfinite(A)
    if fail_step is not None:
        keep = keep & (m < fail_step)
    out = np.full(nb, np.nan)
    b = block_index(m, spp, nb)
    for k in range(1, nb + 1):
        sel = keep & (b == k)
        if sel.any():
            out[k - 1] = A[sel].max()
    return out


def ols(x, y):
    """Least-squares slope and its standard error (needs >= 3 finite points), else (nan, nan)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    if len(x) < 3:
        return float('nan'), float('nan')
    xm = x.mean(); sxx = float(np.sum((x - xm) ** 2))
    slope = float(np.sum((x - xm) * (y - y.mean())) / sxx)
    res = y - (y.mean() + slope * (x - xm))
    se = math.sqrt(float(np.sum(res ** 2)) / (len(x) - 2) / sxx) if len(x) > 2 else float('nan')
    return slope, se


def v5_scan(a, cfg):
    """Replay of the driver's per-sample v5 check on a sealed series a (rows x COLS): returns (index, kind) of the first
    sample at which a v5 bar is breached, or (None, None). Same bars and the same order as driver.v5_breach: non-finite
    sample, E drift, Q drift, J drift, constraint violation (kinds 'nonfinite', 'E', 'Q', 'J', 'constraint')."""
    a = np.asarray(a, float).reshape(-1, len(COLS))
    n = len(a)
    if n == 0:
        return None, None
    fin = np.all(np.isfinite(a), axis=1)
    i0 = int(np.argmin(fin)) if not fin.all() else n
    nn = min(n, i0 + 1)
    E, J, Q, seg = a[:nn, CI['E']], a[:nn, CI['Jz']], a[:nn, CI['Q']], a[:nn, CI['seg_spread']]
    with np.errstate(invalid='ignore'):
        dE = (np.maximum.accumulate(E) - np.minimum.accumulate(E)) / abs(E[0])
        dQ = np.maximum.accumulate(Q) - np.minimum.accumulate(Q)
        dJ = np.maximum.accumulate(J) - np.minimum.accumulate(J)
        bE, bQ, bJ, bC = dE >= cfg['v5_E'], dQ >= cfg['v5_Q'], dJ > cfg['v5_J'], seg >= cfg['v5_con']
    for i in range(nn):
        if not fin[i]:
            return i, 'nonfinite'
        if bE[i]:
            return i, 'E'
        if bQ[i]:
            return i, 'Q'
        if bJ[i]:
            return i, 'J'
        if bC[i]:
            return i, 'constraint'
    return None, None


def breach_kind(reason):
    """Map the driver's breach reason text to the v5_scan kind (None if the failure was a Newton failure)."""
    if not reason or not str(reason).startswith('v5 breach: '):
        return None
    t = str(reason)[len('v5 breach: '):]
    for key, kind in (('non-finite', 'nonfinite'), ('E drift', 'E'), ('Q drift', 'Q'), ('J drift', 'J'), ('constraint', 'constraint')):
        if t.startswith(key):
            return kind
    return 'unknown'


def verify_failure(prefix, breach, fail_step, fail_reason, cfg):
    """The verdict's check of a failure record from the RETAINED raw series: `prefix` the sealed samples kept as valid,
    `breach` the separately sealed breaching sample ((1, ncols) array, or empty for a Newton failure). Returns (ok, text).
    v5 breach: the prefix must scan clean, the breach row's step index must equal fail_step, and the prefix plus the breach
    row must breach at exactly the breach row with the recorded kind. Newton failure: no breach row, prefix scans clean,
    and every kept sample precedes fail_step."""
    prefix = np.asarray(prefix, float).reshape(-1, len(COLS)); breach = np.asarray(breach, float).reshape(-1, len(COLS))
    i, kind = v5_scan(prefix, cfg)
    if i is not None:
        return False, f'prefix itself breaches v5 at sample {i} ({kind})'
    if len(prefix) and not np.all(prefix[:, CI['m']] < fail_step):
        return False, 'a kept sample is at or after fail_step'
    bk = breach_kind(fail_reason)
    if bk is None:
        if len(breach):
            return False, 'Newton failure with a retained breach row'
        return True, f'Newton/init failure at step {fail_step}: {len(prefix)} samples kept, all before it, prefix v5-clean'
    if len(breach) != 1:
        return False, 'v5 breach without exactly one retained breach row'
    if int(round(breach[0, CI['m']])) != int(fail_step):
        return False, f'breach row step {breach[0, CI["m"]]} differs from fail_step {fail_step}'
    full = np.vstack([prefix, breach])
    i, kind = v5_scan(full, cfg)
    if i != len(prefix) or kind != bk:
        return False, f'prefix plus breach row breaches at {i} ({kind}), recorded {len(prefix)} ({bk})'
    return True, f'v5 breach ({kind}) at the retained row, step {fail_step}: {len(prefix)} prefix samples v5-clean, breach row excluded from statistics'


def _nanmax(a):
    a = np.asarray(a, float)
    a = a[np.isfinite(a)]
    return float(a.max()) if len(a) else float('nan')


# ---------------------------------------------------------------------------------------------------------------
# Q1: the twist-speed channel
# ---------------------------------------------------------------------------------------------------------------
def q1_class(m, A, cm, cA, spp, base, cfg, fail_step=None, ctrl_ok=True):
    """Class of one Q1 probe run. m, A: sample step indices and the probed-mode amplitude; cm, cA: the control's.
    Returns dict(cls, valid, rho, sigma, prefix, n_full, first, why). cls in GROWS BOUNDED SLOW UNAVAILABLE
    BELOW-FLOOR NUMERICAL-FLOOR; valid is False for everything but GROWS, BOUNDED, SLOW."""
    nb = cfg['n_per']
    r = dict(cls='UNAVAILABLE', valid=False, rho=float('nan'), sigma=float('nan'), prefix=False, n_full=nb,
             first=float('nan'), why='', fast=False)
    if not ctrl_ok:
        r['why'] = 'control run not complete'; return r
    failed = fail_step is not None
    n_full = int(fail_step) // spp if failed else nb
    r['n_full'] = n_full
    if n_full < 2:
        r['why'] = 'fewer than 2 full blocks'; return r
    bm = block_max(m, A, spp, nb, fail_step); cbm = block_max(cm, cA, spp, nb)
    first = _nanmax(bm[0:2]); cfirst = _nanmax(cbm[0:2]); clate = _nanmax(cbm[20:nb])
    r['first'] = first
    if not (math.isfinite(first) and first > 0 and math.isfinite(cfirst) and math.isfinite(clate)):
        r['why'] = 'non-finite first-window statistic'; return r
    if not first > cfg['f1'] * cfirst:
        r['cls'] = 'BELOW-FLOOR'; r['why'] = f'f1: first-window max {first:.3e} not above {cfg["f1"]} x control {cfirst:.3e}'; return r
    if not clate < cfg['f2'] * first:
        r['cls'] = 'NUMERICAL-FLOOR'; r['why'] = f'f2: control late max {clate:.3e} not below {cfg["f2"]} x probe first {first:.3e}'; return r
    # growth window: blocks 3..k_sat (k_sat: first block among 1..20 above ksat_frac x base rate, else block 20)
    thr = cfg['ksat_frac'] * base
    k_sat = 20; crossed = False
    for k in range(1, min(n_full, 20) + 1):
        if math.isfinite(bm[k - 1]) and bm[k - 1] > thr:
            k_sat = k; crossed = True; break
    kend = min(k_sat, n_full) if failed else k_sat
    ks = list(range(3, kend + 1))
    sigma = float('nan')
    if len(ks) >= 3:
        y = bm[np.array(ks) - 1]
        if np.all(np.isfinite(y)) and np.all(y > 0):
            sigma, _ = ols(np.array(ks, float), np.log(y))
    r['sigma'] = sigma
    # FAST-GROWTH BRANCH (pre-stated; charter section 6 S1): when the threshold is crossed before block 5 (k_sat < fast_k) the
    # block fit has under 3 blocks, so sigma is fitted per sample on the running-maximum envelope of A over the (at most 2
    # periods) window ending at the first threshold crossing, and rho is taken against the probe's own initial amplitude
    # (max A over the first 0.05 period), not against the first-window maximum that a saturating run has already reached.
    # GROWS iff sigma_fast >= grows_sigma, rho_fast >= grows_rho and the perturbation has not returned below the threshold
    # (late max over blocks 21..40, or the last prefix block, is at or above the threshold). Otherwise the standard rules.
    if crossed and k_sat < cfg['fast_k']:
        fw = fast_growth(m, A, spp, thr, fail_step)
        if fw is not None:
            last = bm[n_full - 1] if failed else _nanmax(bm[20:nb])
            rho_f = (last / fw['aref']) if fw['aref'] > 0 else float('inf')
            if (math.isfinite(last) and last >= thr and fw['sigma'] >= cfg['grows_sigma'] and rho_f >= cfg['grows_rho']):
                r.update(cls='GROWS', valid=True, sigma=fw['sigma'], rho=rho_f, fast=True, prefix=failed)
                return r
    if not failed:
        rho = _nanmax(bm[20:nb]) / first
        r['rho'] = rho
        if rho <= cfg['bounded_rho']:
            r['cls'] = 'BOUNDED'; r['valid'] = True
        elif not math.isfinite(sigma):
            r['why'] = 'sigma unavailable (growth window under 3 blocks)'
        elif rho >= cfg['grows_rho'] and sigma >= cfg['grows_sigma']:
            r['cls'] = 'GROWS'; r['valid'] = True
        else:
            r['cls'] = 'SLOW'; r['valid'] = True
        return r
    # failed run: the valid prefix
    r['prefix'] = True
    rho = bm[n_full - 1] / first if math.isfinite(bm[n_full - 1]) else float('nan')
    r['rho'] = rho
    if n_full >= 4 and math.isfinite(rho) and rho >= cfg['grows_rho'] and math.isfinite(sigma) and sigma >= cfg['grows_sigma']:
        r['cls'] = 'GROWS'; r['valid'] = True
    else:
        r['cls'] = 'UNAVAILABLE'; r['why'] = 'failed run whose prefix does not bear GROWS (failure record)'
    return r


def fast_growth(m, A, spp, thr, fail_step=None):
    """Per-sample fit of the fast-growth branch. Samples at or after fail_step are excluded. Returns dict(sigma, t_cross,
    aref) or None. t is in periods (m / spp). The window is [t_cross - 2, t_cross] (t_cross: first sample with A > thr);
    the fit is the least-squares slope of ln(running max of A) on t over samples with positive running max (A(0) = 0 for
    the radial kick is excluded by that condition); aref = max A over samples with t <= 0.05 period."""
    m = np.asarray(m, float); A = np.asarray(A, float)
    keep = np.isfinite(A)
    if fail_step is not None:
        keep = keep & (m < fail_step)
    m, A = m[keep], A[keep]
    if len(m) < 3:
        return None
    tp = m / spp
    idx = np.where(A > thr)[0]
    if len(idx) == 0:
        return None
    tc = float(tp[int(idx[0])])
    env = np.maximum.accumulate(A)
    sel = (tp >= tc - 2.0) & (tp <= tc) & (env > 0)
    if int(sel.sum()) < 3:
        return None
    sigma, _ = ols(tp[sel], np.log(env[sel]))
    s0 = tp <= 0.05
    aref = float(A[s0].max()) if s0.any() else float('nan')
    if not (math.isfinite(sigma) and math.isfinite(aref)):
        return None
    return dict(sigma=sigma, t_cross=tc, aref=aref)


def half_blocked_q1(cls_p, cls_h):
    """h1: the h_p / 2 run must give the same class as the h_p run."""
    return not (cls_p == cls_h and cls_p in ('GROWS', 'BOUNDED', 'SLOW'))


# ---------------------------------------------------------------------------------------------------------------
# Q1b: the neutral manifold
# ---------------------------------------------------------------------------------------------------------------
def shape_class(f, D, spp, cfg, failed=False):
    """f: frame step indices; D: D_shape in units of the run's own eps R_d. HOLDS / DRIFTS / WOBBLES / UNAVAILABLE."""
    nb = cfg['n_per']
    r = dict(cls='UNAVAILABLE', valid=False, maxD=float('nan'), slope=float('nan'), se=float('nan'), why='')
    if failed:
        r['why'] = 'failed run'; return r
    D = np.asarray(D, float)
    if len(D) < 2 or not np.all(np.isfinite(D)):
        r['why'] = 'fewer than 2 frames or non-finite D_shape'; return r
    bm = block_max(f, D, spp, nb)
    slope, se = ols(np.arange(21, nb + 1, dtype=float), bm[20:nb])
    r.update(maxD=float(D.max()), slope=slope, se=se)
    if not math.isfinite(slope):
        r['why'] = 'second-half slope unavailable'; return r
    r['valid'] = True
    if r['maxD'] <= cfg['hold_D']:
        r['cls'] = 'HOLDS'
    elif slope > cfg['sigma3'] * se and slope > 0:
        r['cls'] = 'DRIFTS'
    else:
        r['cls'] = 'WOBBLES'
    return r


def g2_agree(sp, sh, cfg):
    """g2: the h_p / 2 shape run agrees with the h_p run on the class, and for DRIFTS on the slope (same sign, 30 percent)."""
    if not (sp['valid'] and sh['valid']) or sp['cls'] != sh['cls']:
        return False
    if sp['cls'] == 'DRIFTS':
        if sp['slope'] * sh['slope'] <= 0:
            return False
        return abs(sh['slope'] - sp['slope']) <= cfg['g2_slope_tol'] * abs(sp['slope'])
    return True


def ctrl_shape_stats(f, Drel, spp, cfg):
    """Control D_shape in units of R_d (not of eps): max and second-half block-maxima slope."""
    nb = cfg['n_per']
    bm = block_max(f, Drel, spp, nb)
    slope, _ = ols(np.arange(21, nb + 1, dtype=float), bm[20:nb])
    return dict(maxD_rel=float(np.max(Drel)), slope_rel=slope)


# ---------------------------------------------------------------------------------------------------------------
# end state marks (Q2)
# ---------------------------------------------------------------------------------------------------------------
def end_marks(m, Rratio, beta, E, spp, cfg, fail_step=None):
    """The two scored fold marks over the last 2 periods of the run (of the valid prefix if the run failed):
    R: mean R_end / R_mean > 1.3; B: mean twist phase speed beta < 0.5. E is reported, not scored (charter,
    WORKER'S CORRECTION 1). Marks are None when unavailable."""
    nb = cfg['n_per']
    m = np.asarray(m)
    if fail_step is not None:
        n_full = int(fail_step) // spp
        if n_full < 2:
            return dict(R=None, B=None, Rval=float('nan'), Bval=float('nan'), E_mean=float('nan'))
        lo, hi = (n_full - 2) * spp, min(n_full * spp, fail_step)
    else:
        lo, hi = (nb - 2) * spp, nb * spp
    sel = (m >= lo) & (m < hi)
    if not sel.any():
        return dict(R=None, B=None, Rval=float('nan'), Bval=float('nan'), E_mean=float('nan'))
    Rv = float(np.mean(np.asarray(Rratio)[sel])); Bv = float(np.mean(np.asarray(beta)[sel])); Ev = float(np.mean(np.asarray(E)[sel]))
    ok = math.isfinite(Rv) and math.isfinite(Bv)
    return dict(R=(Rv > cfg['rbar_ratio']) if ok else None, B=(Bv < cfg['beta_mark']) if ok else None,
                Rval=Rv, Bval=Bv, E_mean=Ev)


# ---------------------------------------------------------------------------------------------------------------
# the form deciders. Tables: key (probe, M, amp) with amp in 's' (scored) or 'c' (check).
# ---------------------------------------------------------------------------------------------------------------
def decide_q1(tbl, half_blocked, Ms=(48, 96)):
    """tbl[(probe, M, amp)] = q1_class dict (+ 'marks'); half_blocked[probe] = bool. Returns (token, why, witnesses)."""
    wit = []
    for p in Q1_PROBES:
        ok = all(tbl[(p, M, 's')]['cls'] == 'GROWS' and tbl[(p, M, 's')]['valid'] for M in Ms) and not half_blocked[p]
        if ok:
            wit.append(p)
    if wit:
        txt = '; '.join(f'{p} GROWS at M=' + ', '.join(f'{M} (sigma {tbl[(p, M, "s")]["sigma"]:.3g}/period, rho {tbl[(p, M, "s")]["rho"]:.3g}'
                        + (', valid prefix' if tbl[(p, M, 's')]['prefix'] else '') + ')' for M in Ms) for p in wit)
        return 'RING-UNSTABLE', 'under action (i): ' + txt, wit
    bad = []
    for p in Q1_PROBES:
        for M in Ms:
            for a in ('s', 'c'):
                if not tbl[(p, M, a)]['valid']:
                    bad.append(f'{p} M{M} {a}: {tbl[(p, M, a)]["cls"]}')
        if half_blocked[p]:
            bad.append(f'{p} half-blocked')
        if tbl[(p, Ms[0], 's')]['cls'] != tbl[(p, Ms[1], 's')]['cls']:
            bad.append(f'{p} D7 disagreement ({tbl[(p, Ms[0], "s")]["cls"]} vs {tbl[(p, Ms[1], "s")]["cls"]})')
    if bad:
        return 'Q1-NO-CALL', 'no valid RING-UNSTABLE witness; ' + '; '.join(bad), []
    allb = all(tbl[(p, M, a)]['cls'] == 'BOUNDED' for p in Q1_PROBES for M in Ms for a in ('s', 'c'))
    if allb:
        return 'RING-STABLE', 'under action (i): W1, W2, R0 BOUNDED at both resolutions and both amplitudes, none half-blocked', []
    anyg = any(tbl[(p, M, a)]['cls'] == 'GROWS' for p in Q1_PROBES for M in Ms for a in ('s', 'c'))
    anys = any(tbl[(p, M, 's')]['cls'] == 'SLOW' for p in Q1_PROBES for M in Ms)
    if (not anyg) and anys:
        return 'RING-SLOW', 'under action (i): no probe GROWS, at least one SLOW at the scored amplitude; rho and sigma on the face', []
    return 'Q1-NO-CALL', 'scored and check amplitudes disagree in class (not all BOUNDED, no SLOW scored probe, or a check-amplitude GROWS)', []


def decide_q1b(tbl, half_blocked, ctrl, g4, cfg, Ms=(48, 96)):
    """tbl[(probe, M, amp)] = shape_class dict for the form-bearing probes; ctrl[M] = ctrl_shape_stats; g4[M] bool;
    half_blocked[probe] = not g2. Returns (token, why, witnesses)."""
    eps_s = cfg['eps_scored']; eps_c = cfg['eps_check']
    for M in Ms:
        if not g4[M]:
            return 'Q1B-NO-CALL', f'g4: observable floor not below {cfg["g4_floor"]} at M={M}', []
        # g1: the control over the whole run, in units of eps_scored R_d
        if not ctrl[M]['maxD_rel'] / eps_s <= cfg['g1_D']:
            return 'Q1B-NO-CALL', f'g1: control D_shape {ctrl[M]["maxD_rel"] / eps_s:.3g} above {cfg["g1_D"]} at M={M}', []
        for p in SHAPE_BEARING:
            for a, e in (('s', eps_s), ('c', eps_c)):
                st = tbl[(p, M, a)]
                if st['valid'] and st['cls'] == 'DRIFTS':
                    cs = ctrl[M]['slope_rel'] / e
                    if not (math.isfinite(cs) and cs < cfg['g1_slope'] * st['slope']):
                        return 'Q1B-NO-CALL', f'g1: control drift slope {cs:.3g} not below {cfg["g1_slope"]} x probe slope {st["slope"]:.3g} ({p} M={M} {a})', []
    both_valid = {(p, M): tbl[(p, M, 's')]['valid'] and tbl[(p, M, 'c')]['valid'] for p in SHAPE_BEARING for M in Ms}
    # witnesses: the SCORED amplitude only (the amplitude with the scheduled half-step comparison g2), DRIFTS at BOTH M at that
    # same amplitude (a matched resolution check); the check amplitude is validity-bearing and reported, never a witness.
    wit = [p for p in SHAPE_BEARING if not half_blocked[p] and all(
        both_valid[(p, M)] and tbl[(p, M, 's')]['cls'] == 'DRIFTS' for M in Ms)]
    if wit:
        txt = '; '.join(f'{p}: ' + ', '.join(f'M={M} slope {tbl[(p, M, "s")]["slope"]:.3g}/block' for M in Ms) for p in wit)
        return ('NEUTRAL-DRIFTS', 'under action (i): at the scored amplitude the finite-amplitude shape distance grows over the second half '
                'of the run at both M (no amplitude-scaling test is part of this commission): ' + txt, wit)
    bad = []
    for p in SHAPE_BEARING:
        for M in Ms:
            if not both_valid[(p, M)]:
                bad.append(f'{p} M{M}: a run invalid ({tbl[(p, M, "s")]["cls"]}/{tbl[(p, M, "c")]["cls"]})')
            if any(tbl[(p, M, a)]['valid'] and tbl[(p, M, a)]['cls'] == 'DRIFTS' for a in ('s', 'c')):
                bad.append(f'{p} M{M}: DRIFTS at an amplitude/resolution that does not meet the witness predicate (scored amplitude at both M, not half-blocked)')
        if half_blocked[p]:
            bad.append(f'{p} half-blocked (g2)')
        if tbl[(p, Ms[0], 's')]['cls'] != tbl[(p, Ms[1], 's')]['cls']:
            bad.append(f'{p} D7/g3 disagreement ({tbl[(p, Ms[0], "s")]["cls"]} vs {tbl[(p, Ms[1], "s")]["cls"]})')
    if bad:
        return 'Q1B-NO-CALL', '; '.join(bad), []
    if all(tbl[(p, M, 's')]['cls'] == 'HOLDS' for p in SHAPE_BEARING for M in Ms):
        return 'NEUTRAL-HOLDS', 'under action (i): S3, S4, Z2, Z3 all HOLDS at both resolutions, gates g1 to g4 met', []
    if any(tbl[(p, M, 's')]['cls'] == 'WOBBLES' for p in SHAPE_BEARING for M in Ms):
        return 'NEUTRAL-WOBBLES', 'under action (i): no probe DRIFTS, at least one WOBBLES at both resolutions, gates met', []
    return 'Q1B-NO-CALL', 'classes not classifiable', []


def decide_q2(q1form, q1wit, q1tbl, q1btoken, q1bwit, shtbl, Ms=(48, 96)):
    """Qualifying runs: every valid, gated GROWS (Q1 witnesses) or DRIFTS (Q1b witnesses) run at the SCORED amplitude, at each M
    (the check-amplitude runs have no half-step comparison and are never qualifying).
    Each run stat carries 'marks' = end_marks(...). Returns (token, why, qualifying)."""
    trig = (q1form == 'RING-UNSTABLE') or (q1btoken == 'NEUTRAL-DRIFTS')
    if not trig:
        return 'END-NOT-TRIGGERED', 'neither RING-UNSTABLE nor NEUTRAL-DRIFTS was rendered (this does not assert that no witness existed when only one was)', []
    qual = []
    if q1form == 'RING-UNSTABLE':
        for p in q1wit:
            for M in Ms:
                for a in ('s',):
                    st = q1tbl[(p, M, a)]
                    if st['valid'] and st['cls'] == 'GROWS':
                        qual.append(((p, M, a), st))
    if q1btoken == 'NEUTRAL-DRIFTS':
        for p in q1bwit:
            for M in Ms:
                for a in ('s',):
                    st = shtbl[(p, M, a)]
                    if st['valid'] and st['cls'] == 'DRIFTS':
                        qual.append(((p, M, a), st))
    if not qual:
        return 'Q2-NO-CALL', 'triggered but no qualifying run found', []
    failed = [(k, s) for k, s in qual if (s['marks']['R'] is False or s['marks']['B'] is False)]
    unavail = [(k, s) for k, s in qual if (s['marks']['R'] is None or s['marks']['B'] is None)]
    desc = '; '.join(f'{k[0]} M{k[1]} {k[2]}: R_end/R_mean {s["marks"]["Rval"]:.3g}, beta {s["marks"]["Bval"]:.3g}, E {s["marks"]["E_mean"]:.4g}' for k, s in qual)
    if failed:
        return 'END-OTHER', 'at least one qualifying run has a known failed fold mark; ' + desc, [k for k, _ in qual]
    if unavail:
        return 'Q2-NO-CALL', 'no known failed mark, at least one mark unavailable; ' + desc, [k for k, _ in qual]
    return 'END-FOLD', 'every qualifying run meets both scored marks; ' + desc, [k for k, _ in qual]
