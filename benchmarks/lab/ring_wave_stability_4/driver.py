"""RING-WAVE-STABILITY-4 driver: the travelling-twist ring under perturbation, under action (i) (charter P1).

One unit per invocation through labkit.Driver. Units in order: credential, setup, stat_credential, static, the two
unperturbed controls, the 36 evidence runs, the half-step control and the 9 half-step runs, then one D_shape unit per
shape run (computed from the sealed node frames only). Every trajectory's observables are sealed as the run
completes; no statistic is computed during a run. LAB_SMOKE=1 runs a tiny version on a SYNTHETIC FIXTURE: the
beta = 0.5 family member of the same rope (not the evidence state) at M = 16 for 2 periods, one control and one S3 probe;
it reads nothing under data/, uses none of the evidence cells, and writes analysis/ring_wave_stability_4_smoke.pkl.
"""
import json
import math
import os
import pathlib
import sys
import time

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                         # noqa: E402
from benchmarks.lab.ring_wave_stability_4 import stats as ST                        # noqa: E402

SLUG = 'ring_wave_stability_4'
MANIFEST = ['benchmarks/lab/_kit/labkit.py',
            'benchmarks/lab/ring_wave_stability_4/driver.py',
            'benchmarks/lab/ring_wave_stability_4/verdict.py',
            'benchmarks/lab/ring_wave_stability_4/stats.py',
            'benchmarks/foundations/ring_wave_dynamics.py',
            'benchmarks/foundations/ring_wave_stability.py',
            'benchmarks/foundations/elec_rope_wave.py',
            'benchmarks/foundations/elec_rotator.py',
            'benchmarks/foundations/strand_calugareanu.py']

CONFIG = dict(
    kappa=0.5, Ms=(48, 96), cred_M=48, n_per=40, steps_per_period=500, sample_stride=10, frame_stride=200,
    eps_scored=3e-3, eps_check=1e-3,
    # Q1 statistics (D5)
    f1=10.0, f2=0.1, grows_rho=10.0, grows_sigma=0.05, bounded_rho=3.0, ksat_frac=0.1, fast_k=5,
    # Q1b statistics (D5)
    hold_D=0.1, sigma3=3.0, g1_D=0.02, g1_slope=0.1, g2_slope_tol=0.30, g4_floor=0.02,
    # Q2 marks (charter, WORKER'S CORRECTION 1: E reported, not scored)
    rbar_ratio=1.3, beta_mark=0.5, E_fold=8.144,
    # v5 (every evidence run, both amplitudes)
    v5_E=1e-4, v5_Q=1e-8, v5_con=1e-10, v5_J=2e-6,
    # WU family check
    wu_R=1e-2, wu_beta=2.5e-3,
    # D6 static cross-check
    static_M=48, static_S=1e-2,
    # credential bars (halt-grade)
    k1_rel=2e-3, k1_E=1e-6, k2_R=1e-3, k2_E0=1e-3, k2_E=1e-4,
    k3_E0=1e-3, k3_J0=1e-3, k3_E=1e-8, k3_J=1e-8, k3_Q=1e-8, k3_P=1e-8, k3_Rspread=1e-6, k3_Rmean=1e-4,
    k4_cons=1e-9, k4_order=1.8, k5_disp=0.1, k5_J=1e-7,
)
SMOKE = dict(M=16, beta=0.5, n_per=2, spp=100, stride=10, fstride=50, static_M=8)
SMOKE_RUNS = ('ctrl_M48', 'S3_M48_s')

PROBES = ('S2', 'S3', 'S4', 'Z2', 'Z3', 'R0', 'W1', 'W2', 'WU')
SHAPE_PROBES = ST.SHAPE_ALL


def run_specs():
    """The 48 trajectories, in order: name -> dict(M, probe, amp, half)."""
    out = {}
    out['ctrl_M48'] = dict(M=48, probe=None, eps=0.0, half=False)
    out['ctrl_M96'] = dict(M=96, probe=None, eps=0.0, half=False)
    for M in CONFIG['Ms']:
        for a, e in (('s', CONFIG['eps_scored']), ('c', CONFIG['eps_check'])):
            for p in PROBES:
                out[f'{p}_M{M}_{a}'] = dict(M=M, probe=p, eps=e, half=False)
    out['ctrl_M48_h'] = dict(M=48, probe=None, eps=0.0, half=True)
    for p in PROBES:
        out[f'{p}_M48_h'] = dict(M=48, probe=p, eps=CONFIG['eps_scored'], half=True)
    return out


SPECS = run_specs()
SHAPE_RUNS = [n for n, s in SPECS.items() if s['probe'] is None or s['probe'] in SHAPE_PROBES]


def _rwd():
    from benchmarks.foundations import ring_wave_dynamics as rwd
    return rwd


def _rws():
    from benchmarks.foundations import ring_wave_stability as rws
    return rws


# ---------------------------------------------------------------------------------------------------------------
# the state, the probes, one trajectory
# ---------------------------------------------------------------------------------------------------------------
def build_state(rwd, M, beta, R, probe, eps):
    q, v = rwd.ring(M, R, 1, -beta)
    th = 2 * math.pi * np.arange(M) / M
    c, s = np.cos(th), np.sin(th)
    if probe is None:
        return q, v
    if probe[0] == 'S':
        n = int(probe[1]); r = R * (1 + eps * np.cos(n * th))
        q[:3 * M] = rwd.equalize(np.stack([r * c, r * s, np.zeros(M)], 1)).ravel()
    elif probe[0] == 'Z':
        n = int(probe[1])
        q[:3 * M] = rwd.equalize(np.stack([R * c, R * s, eps * R * np.cos(n * th)], 1)).ravel()
    elif probe == 'R0':
        v[:3 * M] = eps * np.stack([c, s, np.zeros(M)], 1).ravel()
    elif probe[0] == 'W' and probe != 'WU':
        n = int(probe[1]); v[3 * M:] = v[3 * M:] + eps * np.cos(n * th) / R
    elif probe == 'WU':
        v[3 * M:] = v[3 * M:] + eps / R
    else:
        raise K.Halt(f'unknown probe {probe}')
    return q, v


def sample_row(integ, M, m):
    o = integ.observables()
    qm = np.asarray(0.5 * (integ.qprev + integ.q)); qd = np.asarray((integ.q - integ.qprev) / integ.h)
    X, _ = integ.split(qm); W = qd[3 * M:]
    Rr = np.linalg.norm(X - X.mean(0), axis=1)
    r = np.hypot(X[:, 0] - X[:, 0].mean(), X[:, 1] - X[:, 1].mean()); z = X[:, 2] - X[:, 2].mean()

    def am(f, n):
        return float(2.0 / M * abs(np.fft.fft(f)[n]))
    row = [float(m), o['t'], o['E'], o['J'][2], float(np.linalg.norm(o['P'])), o['Q'], o['R_mean'], float(Rr.max() / Rr.mean()),
           float(-W.mean() * o['R_mean']), o['seg_spread'], o['L'], float(W.mean()), float(X[:, 2].mean())]
    row += [am(r - r.mean(), n) for n in range(1, 7)] + [am(z, n) for n in range(1, 7)] + [am(W - W.mean(), n) for n in range(1, 7)]
    return row


def v5_breach(rows, cfg):
    a = np.asarray(rows); E, J, Q, seg = a[:, ST.CI['E']], a[:, ST.CI['Jz']], a[:, ST.CI['Q']], a[:, ST.CI['seg_spread']]
    if not np.all(np.isfinite(a[-1])):
        return 'non-finite sample'
    if (E.max() - E.min()) / abs(E[0]) >= cfg['v5_E']:
        return f'E drift {(E.max() - E.min()) / abs(E[0]):.2e}'
    if Q.max() - Q.min() >= cfg['v5_Q']:
        return f'Q drift {Q.max() - Q.min():.2e}'
    if J.max() - J.min() > cfg['v5_J']:
        return f'J drift {J.max() - J.min():.2e}'
    if seg[-1] >= cfg['v5_con']:
        return f'constraint violation {seg[-1]:.2e}'
    return None


def integrate(M, beta, R, probe, eps, half, nper, spp0, stride, fstride, name='', cfg=None):
    rwd = _rwd(); cfg = CONFIG if cfg is None else cfg
    breach_row = None
    spp = spp0 * (2 if half else 1); h = 2 * math.pi * R / spp
    q0, v0 = build_state(rwd, M, beta, R, probe, eps)
    X0 = q0[:3 * M].reshape(M, 3).copy()
    integ = rwd.StringIntegrator(M, cfg['kappa'], 1, h, q0)
    rows, frames, fn = [], [X0], [0]
    fail_step, fail_reason = None, None
    try:
        integ.init(q0, v0)
    except Exception as e:                                                           # an init failure is a failure record
        fail_step, fail_reason = 0, f'init: {type(e).__name__}: {e}'
    nsteps = nper * spp; n = 1; t0 = time.time()
    while fail_step is None:
        m = n - 1
        if m % stride == 0:
            rows.append(sample_row(integ, M, m))
            why = v5_breach(rows, cfg)
            if why:
                breach_row = rows.pop()                       # RETAINED and sealed apart from the valid prefix
                fail_step, fail_reason = m, f'v5 breach: {why}'; break
        if n % fstride == 0:
            frames.append(np.asarray(integ.split(np.asarray(integ.q))[0]).copy()); fn.append(n)
        if n >= nsteps:
            break
        try:
            integ.step()
        except Exception as e:
            fail_step, fail_reason = n, f'Newton: {type(e).__name__}: {str(e)[:120]}'; break
        n += 1
        if n % (20 * stride * 10) == 0:
            print(f'  {name} step {n}/{nsteps} ({time.time() - t0:.0f}s)', flush=True)
    ser = np.asarray(rows, float).reshape(len(rows), len(ST.COLS))
    breach = (np.asarray(breach_row, float).reshape(1, len(ST.COLS)) if breach_row is not None else np.zeros((0, len(ST.COLS))))
    return dict(ser=ser, breach=breach, X=np.asarray(frames), fn=np.asarray(fn, float), fail_step=fail_step, fail_reason=fail_reason,
                spp=spp, h=h, nsteps=nsteps)


def make_run_unit(name):
    spec = SPECS[name]

    def unit(ck):
        if ck.smoke:
            if name not in SMOKE_RUNS:
                return dict(skipped=True)
            M, beta, nper, spp0, stride, fstride = SMOKE['M'], SMOKE['beta'], SMOKE['n_per'], SMOKE['spp'], SMOKE['stride'], SMOKE['fstride']
            probe = None if spec['probe'] is None else spec['probe']
            R = _rwd().discrete_ring_radius(M, CONFIG['kappa'], 1, beta)
        else:
            M, beta, nper = spec['M'], 1.0, CONFIG['n_per']
            spp0, stride, fstride = CONFIG['steps_per_period'], CONFIG['sample_stride'], CONFIG['frame_stride']
            probe = spec['probe']
            R = K.finite(ck.state['records']['setup']['Rd'][str(M)], 'R_d')
        res = integrate(M, beta, R, probe, spec['eps'], spec['half'], nper, spp0, stride, fstride, name)
        ck.seal(f'ser/{name}', res['ser']); ck.seal(f'breach/{name}', res['breach'])
        ck.seal(f'X/{name}', res['X']); ck.seal(f'fn/{name}', res['fn'])
        done = res['fail_step'] is None
        print(f'  {name}: {"complete" if done else "FAILURE RECORD at step " + str(res["fail_step"]) + " (" + str(res["fail_reason"]) + ")"}; '
              f'{len(res["ser"])} samples, {len(res["fn"])} frames', flush=True)
        return dict(name=name, complete=done, fail_step=res['fail_step'], fail_reason=res['fail_reason'], n_samples=int(len(res['ser'])),
                    n_frames=int(len(res['fn'])), Rd=float(R), spp=int(res['spp']), h=float(res['h']), M=int(M))
    return unit


def make_dshape_unit(name):
    def unit(ck):
        if ck.smoke and name not in SMOKE_RUNS:
            return dict(skipped=True)
        rwd = _rwd()
        X = ck.sealed(f'X/{name}')
        K.require(len(X) >= 1, f'dshape {name}: no frames')
        D = np.zeros(len(X))
        for i in range(1, len(X)):
            D[i] = rwd.shape_distance(X[i], X[0])['D_max']
        K.finite_array(D, f'dshape {name}')
        ck.seal(f'D/{name}', D)
        return dict(name=name, n=int(len(D)))
    return unit


# ---------------------------------------------------------------------------------------------------------------
# credential (halt-grade), setup, static
# ---------------------------------------------------------------------------------------------------------------
def unit_credential(ck):
    rwd = _rwd(); cfg = CONFIG; smoke = ck.smoke
    M = SMOKE['M'] if smoke else cfg['cred_M']
    rec, bars = dict(M=M, smoke=smoke), {}
    r1 = rwd.k1_twist_wave(M); rec['K1'] = r1
    bars['v1_K1'] = abs(r1['rel_to_discrete']) < cfg['k1_rel'] and r1['E_drift'] < cfg['k1_E']
    r2 = rwd.k2_pulsating(M); rec['K2'] = r2
    bars['v2_K2'] = (r2['worst_R_error'] < cfg['k2_R'] and abs(r2['E0'] - r2['E_exact']) / r2['E_exact'] < cfg['k2_E0']
                     and r2['E_drift'] < cfg['k2_E'])
    r5 = rwd.k5_shape_degeneracy(M); rec['K5'] = r5                                       # beta = 0.5 family member
    bars['v4b_K5'] = r5['worst_displacement'] < cfg['k5_disp'] * r5['eps'] * r5['R'] and r5['J_drift'] < cfg['k5_J']
    r6 = {str(m_): rwd.k6_shape_registration(m_) for m_ in ((M,) if smoke else cfg['Ms'])}; rec['K6'] = r6
    bars['v6_K6'] = all(all(o['bars'].values()) for o in r6.values())
    if not smoke:
        Rd = rwd.discrete_ring_radius(M, cfg['kappa'], 1, 1.0); hp = 2 * math.pi * Rd / cfg['steps_per_period']
        r3 = rwd.k3_ring_wave(M, cfg['kappa']); rec['K3'] = r3
        bars['v3_K3'] = (abs(r3['E0'] - r3['E_closed_form']) / r3['E_closed_form'] < cfg['k3_E0']
                         and abs(r3['J0'] - r3['J_closed_form']) / r3['J_closed_form'] < cfg['k3_J0']
                         and r3['E_drift'] < cfg['k3_E'] and r3['J_drift'] < cfg['k3_J'] and r3['Q_drift'] < cfg['k3_Q']
                         and r3['P_max'] < cfg['k3_P'] and r3['R_spread_max'] < cfg['k3_Rspread'] and r3['R_mean_drift'] < cfg['k3_Rmean'])
        r4 = rwd.k4_noether(); rec['K4'] = r4
        bars['v4_K4'] = (all(r['P_drift'] < cfg['k4_cons'] and r['J_drift'] < cfg['k4_cons'] and r['Q_drift'] < cfg['k4_cons']
                             for r in r4['rows'] if not r['pin']) and r4['E_order'] > cfg['k4_order'])
        r2p = rwd.k2_pulsating(M, 1.0, h=2 * math.pi * 1.0 / cfg['steps_per_period']); rec['K2p'] = r2p
        r3p = rwd.k3_ring_wave(M, cfg['kappa'], h=hp); rec['K3p'] = r3p
        bars['v2p_K2'] = (r2p['worst_R_error'] < cfg['k2_R'] and abs(r2p['E0'] - r2p['E_exact']) / r2p['E_exact'] < cfg['k2_E0']
                          and r2p['E_drift'] < cfg['k2_E'])
        bars['v2p_K3'] = (abs(r3p['E0'] - r3p['E_closed_form']) / r3p['E_closed_form'] < cfg['k3_E0']
                          and abs(r3p['J0'] - r3p['J_closed_form']) / r3p['J_closed_form'] < cfg['k3_J0']
                          and r3p['E_drift'] < cfg['k3_E'] and r3p['J_drift'] < cfg['k3_J'] and r3p['Q_drift'] < cfg['k3_Q']
                          and r3p['P_max'] < cfg['k3_P'] and r3p['R_spread_max'] < cfg['k3_Rspread'] and r3p['R_mean_drift'] < cfg['k3_Rmean'])
    rec['bars'] = {k: bool(v) for k, v in bars.items()}
    ck.seal('cred/record', json.dumps(rec, default=float, sort_keys=True).encode())
    print('  credential bars: ' + ' '.join(f'{k}={"PASS" if v else "FAIL"}' for k, v in rec['bars'].items()), flush=True)
    if not smoke:
        K.require(all(bars.values()), 'credential: halt-grade bar(s) failed: ' + ', '.join(k for k, v in bars.items() if not v))
    return dict(bars=rec['bars'], all_pass=bool(all(bars.values())))


def unit_setup(ck):
    rwd = _rwd()
    if ck.smoke:
        return dict(Rd={str(SMOKE['M']): float(rwd.discrete_ring_radius(SMOKE['M'], CONFIG['kappa'], 1, SMOKE['beta']))})
    Rd = {str(M): float(rwd.discrete_ring_radius(M, CONFIG['kappa'], 1, 1.0)) for M in CONFIG['Ms']}
    return dict(Rd=Rd, h_p={str(M): 2 * math.pi * Rd[str(M)] / CONFIG['steps_per_period'] for M in CONFIG['Ms']})


def unit_static(ck):
    """D6: the constrained spectrum of the Leg C static functional at the ring-wave polygon, without the Coulomb term
    (kappa_C = 0: the dynamics carry none and alpha enters nowhere). A cross-check, recorded, never a halt."""
    rwd, rws = _rwd(), _rws()
    M = SMOKE['static_M'] if ck.smoke else CONFIG['static_M']
    beta = SMOKE['beta'] if ck.smoke else 1.0
    R = rwd.discrete_ring_radius(M, CONFIG['kappa'], 1, beta)
    X, _ = rwd.ring(M, R, 1, -beta)
    Xn = X[:3 * M].reshape(M, 3)
    spec, p = rws.rope_spectrum(Xn, 2 * math.pi * CONFIG['kappa'] * beta, beta, CONFIG['kappa'], 0.0)
    ev = np.asarray(spec['eig'])
    out = dict(M=int(M), S=float(spec['S']), E=float(p['E']), nneg=int(spec['nneg']), nnull=int(spec['nnull']), npos=int(spec['npos']),
               dim=int(spec['dim']), eig_low=[float(v) for v in ev[:6]], S_below_bar=bool(spec['S'] < CONFIG['static_S']))
    print(f'  static D6 M={M}: S={out["S"]:.3e} nneg={out["nneg"]} nnull={out["nnull"]} dim={out["dim"]}', flush=True)
    return out


# ---------------------------------------------------------------------------------------------------------------
# stat_credential: the D5 statistics and the deciders on closed-form synthetic trajectories, classes pre-stated
# ---------------------------------------------------------------------------------------------------------------
def unit_stat_credential(ck):
    cfg = CONFIG; spp = 500; nb = 40; base = 1.414
    m = np.arange(0, nb * spp, 10); tp = m / spp
    ctrl = np.full(len(m), 1e-12)
    a0 = 4e-3
    res = []

    def expect(name, got, want):
        res.append(dict(name=name, got=str(got), want=str(want), ok=bool(got == want)))

    def cq(A, cA=None, **kw):
        return ST.q1_class(m, A, m, ctrl if cA is None else cA, spp, base, cfg, **kw)
    expect('exp sigma 0.1', cq(a0 * np.exp(0.1 * tp))['cls'], 'GROWS')
    expect('tanh-saturated sigma 0.3', cq(1.4 * np.tanh(a0 * np.exp(0.3 * tp) / 1.4))['cls'], 'GROWS')
    expect('bounded oscillation', cq(a0 * (1 + 0.1 * np.sin(2 * np.pi * tp / 7.3)))['cls'], 'BOUNDED')
    expect('slow sigma 0.04', cq(a0 * np.exp(0.04 * tp))['cls'], 'SLOW')
    quiet = a0 * (1 + 0.1 * np.sin(2 * np.pi * tp / 7.3))
    expect('late-noise control (f2)', cq(quiet, cA=1e-12 + np.where(tp > 20, 2e-3, 0.0))['cls'], 'NUMERICAL-FLOOR')
    expect('below floor (f1)', cq(np.full(len(m), 5e-12))['cls'], 'BELOW-FLOOR')
    expect('h1 step-dependent growth blocks', ST.half_blocked_q1('GROWS', 'BOUNDED'), True)
    expect('h1 agreement does not block', ST.half_blocked_q1('GROWS', 'GROWS'), False)
    g12 = cq(a0 * np.exp(0.4 * tp), fail_step=12 * spp + 137)
    expect('growing run failing at period 12 (prefix witness)', (g12['cls'], g12['valid'], g12['prefix']), ('GROWS', True, True))
    g3 = cq(a0 * np.exp(0.4 * tp), fail_step=3 * spp + 137)
    expect('growing run failing at period 3 (failure record)', (g3['cls'], g3['valid']), ('UNAVAILABLE', False))
    # fast growth (fixtures derived from arithmetic: the W-probe threshold is 0.1 x base = 0.1414, a0 = 4e-3, so an exponential
    # at sigma crosses at t = ln(0.1414 / 4e-3) / sigma = 3.565 / sigma periods: 1.78 at sigma 2, 2.38 at 1.5, 5.09 at 0.7)
    e2 = cq(a0 * np.exp(2.0 * tp))
    expect('exp sigma 2 per period (fast branch)', (e2['cls'], e2['valid'], e2['fast'], bool(abs(e2['sigma'] - 2.0) < 1e-6)), ('GROWS', True, True, True))
    t2 = cq(1.4 * np.tanh(a0 * np.exp(2.0 * tp) / 1.4))
    expect('tanh-saturated sigma 2 per period (fast branch)', (t2['cls'], t2['valid'], t2['fast'], bool(1.8 < t2['sigma'] < 2.05)), ('GROWS', True, True, True))
    expect('exp sigma 0.7 (crossing at 5.09 periods, block fit with 4 blocks)', cq(a0 * np.exp(0.7 * tp))['cls'], 'GROWS')
    f4 = cq(a0 * np.exp(1.5 * tp), fail_step=4 * spp + 137)
    expect('growing run (sigma 1.5) failing at period 4: prefix GROWS', (f4['cls'], f4['valid'], f4['prefix'], bool(abs(f4['sigma'] - 1.5) < 1e-6)), ('GROWS', True, True, True))
    f3b = cq(a0 * np.exp(1.5 * tp), fail_step=3 * spp + 137)
    expect('growing run (sigma 1.5) failing at period 3 after crossing at 2.38: prefix GROWS', (f3b['cls'], f3b['valid']), ('GROWS', True))
    f2b = cq(a0 * np.exp(1.5 * tp), fail_step=2 * spp + 137)
    expect('growing run (sigma 1.5) failing at period 2, before the crossing: failure record', (f2b['cls'], f2b['valid']), ('UNAVAILABLE', False))
    pulse = a0 + 0.2 * np.exp(-((tp - 1.0) / 0.4) ** 2)
    expect('transient excursion above the threshold that returns', cq(pulse)['cls'], 'BOUNDED')
    kick = 0.8 * np.tanh(3e-3 * np.sinh(2.0 * tp) / 0.8)                       # a radial-kick-like A(0) = 0, base R_d = 0.707
    kk = ST.q1_class(m, kick, m, ctrl, spp, 0.707, cfg)
    expect('R0-like exponential from A(0) = 0, sigma 2, saturating', (kk['cls'], kk['valid'], kk['fast']), ('GROWS', True, True))
    # v5 breach retained and verified from the raw series (synthetic closed form; a breach by E drift at sample 61)
    ncol = len(ST.COLS); nser = 100
    sy = np.zeros((nser, ncol)); sy[:, ST.CI['m']] = np.arange(nser) * 10.0; sy[:, ST.CI['E']] = 8.8
    sy[:, ST.CI['E']] += np.where(np.arange(nser) >= 61, 8.8 * 2e-4, 0.0)
    ibr, kbr = ST.v5_scan(sy, cfg)
    inc = None
    for i_ in range(nser):
        w_ = v5_breach(sy[:i_ + 1], cfg)
        if w_:
            inc = (i_, ST.breach_kind('v5 breach: ' + w_)); break
    expect('v5_scan agrees with the driver\'s incremental v5_breach', (ibr, kbr, inc), (61, 'E', (61, 'E')))
    pre, br = sy[:61], sy[61:62]
    okv, _ = ST.verify_failure(pre, br, 610, 'v5 breach: E drift 2.00e-04', cfg)
    expect('breach verified from the retained rows', okv, True)
    expect('breach row with the wrong step is rejected', ST.verify_failure(pre, br, 620, 'v5 breach: E drift 2.00e-04', cfg)[0], False)
    expect('breach row removed (popped) is rejected', ST.verify_failure(pre, sy[:0], 610, 'v5 breach: E drift 2.00e-04', cfg)[0], False)
    expect('prefix containing the breach is rejected', ST.verify_failure(sy[:70], sy[70:71], 700, 'v5 breach: E drift 2.00e-04', cfg)[0], False)
    expect('breach of the wrong recorded kind is rejected', ST.verify_failure(pre, br, 610, 'v5 breach: J drift 2.00e-04', cfg)[0], False)
    expect('Newton failure with clean prefix verified', ST.verify_failure(sy[:50], sy[:0], 520, 'Newton: RuntimeError: x', cfg)[0], True)
    # end marks: the prefix is used, not the post-breach tail
    fs = 12 * spp + 137
    Rr = np.where(m < fs, 1.5, 1.0); be = np.where(m < fs, 0.3, 1.0); Ee = np.full(len(m), 8.8)
    mk = ST.end_marks(m, Rr, be, Ee, spp, cfg, fail_step=fs)
    expect('end marks from the prefix, not the tail', (mk['R'], mk['B']), (True, True))
    mk2 = ST.end_marks(m, Rr, be, Ee, spp, cfg)
    expect('end marks of the full series (tail)', (mk2['R'], mk2['B']), (False, False))
    # shape statistics
    fm = np.arange(0, nb * spp + 1, 200); per = fm / spp
    expect('shape holds', ST.shape_class(fm, 0.01 * np.abs(np.sin(per)), spp, cfg)['cls'], 'HOLDS')
    s_dr = ST.shape_class(fm, 0.05 + 0.02 * per, spp, cfg)
    expect('shape drifts', s_dr['cls'], 'DRIFTS')
    s_wo = ST.shape_class(fm, 0.85 * np.abs(np.sin(2 * np.pi * per / 7.3)), spp, cfg)
    expect('shape wobbles (equal maxima, no monotone growth)', s_wo['cls'], 'WOBBLES')
    expect('g2 equal maxima, incompatible drift blocks', ST.g2_agree(s_dr, s_wo, cfg), False)
    expect('g2 agreement', ST.g2_agree(s_dr, ST.shape_class(fm, 0.05 + 0.021 * per, spp, cfg), cfg), True)
    cs = ST.ctrl_shape_stats(fm, 1e-6 + np.where(per > 20, 5.5e-5 * (per - 20) / 20, 0.0), spp, cfg)
    shd = ST.shape_class(fm, 0.05 + 0.002 * per, spp, cfg)
    expect('shape probe drifts slowly', shd['cls'], 'DRIFTS')

    # deciders on hand-built tables
    def q(cls, valid=True, prefix=False, marks=None, sigma=0.3, rho=50.0):
        return dict(cls=cls, valid=valid, prefix=prefix, sigma=sigma, rho=rho, n_full=40,
                    marks=marks or dict(R=True, B=True, Rval=1.5, Bval=0.3, E_mean=8.88))
    met = dict(R=True, B=True, Rval=1.5, Bval=0.3, E_mean=8.88)
    failm = dict(R=False, B=True, Rval=1.0, Bval=0.3, E_mean=8.88)
    miss = dict(R=None, B=True, Rval=float('nan'), Bval=0.3, E_mean=8.88)
    Ms = (48, 96)

    def q1table(over=None, default='BOUNDED'):
        t = {(p, M, a): q(default, sigma=float('nan'), rho=1.0) for p in ST.Q1_PROBES for M in Ms for a in ('s', 'c')}
        t.update(over or {})
        return t
    nohalf = {p: False for p in ST.Q1_PROBES}
    bad = q('UNAVAILABLE', valid=False)
    t = q1table({('W1', M, 's'): q('GROWS') for M in Ms} | {('W1', M, 'c'): bad for M in Ms})
    f, _, w = ST.decide_q1(t, nohalf)
    expect('Q1 failed check beside valid scored GROWS: witness kept', f, 'RING-UNSTABLE')
    t = q1table({('W1', 48, 'c'): bad})
    expect('Q1 failed check blocks a non-witness form', ST.decide_q1(t, nohalf)[0], 'Q1-NO-CALL')
    expect('Q1 all bounded', ST.decide_q1(q1table(), nohalf)[0], 'RING-STABLE')
    expect('Q1 slow', ST.decide_q1(q1table({('W2', M, 's'): q('SLOW', sigma=0.02, rho=5.0) for M in Ms}), nohalf)[0], 'RING-SLOW')
    expect('Q1 half-blocked blocks RING-STABLE', ST.decide_q1(q1table(), dict(nohalf, R0=True))[0], 'Q1-NO-CALL')
    expect('Q1 D7 disagreement', ST.decide_q1(q1table({('W1', 96, 's'): q('SLOW', sigma=0.02, rho=5.0)}), nohalf)[0], 'Q1-NO-CALL')
    # Q2: witness beside a half-blocked GROWS probe with different marks
    t = q1table({('W1', M, 's'): q('GROWS', marks=met) for M in Ms} | {('W2', M, 's'): q('GROWS', marks=failm) for M in Ms})
    f1_, _, w1 = ST.decide_q1(t, dict(nohalf, W2=True))
    q2 = ST.decide_q2(f1_, w1, t, 'Q1B-NO-CALL', [], {})
    expect('Q2 half-blocked probe is not qualifying', (f1_, w1, q2[0]), ('RING-UNSTABLE', ['W1'], 'END-FOLD'))
    t = q1table({('W1', 48, 's'): q('GROWS', marks=met), ('W1', 96, 's'): q('GROWS', marks=miss)})
    f1_, _, w1 = ST.decide_q1(t, nohalf)
    expect('Q2 mixed availability', ST.decide_q2(f1_, w1, t, 'Q1B-NO-CALL', [], {})[0], 'Q2-NO-CALL')
    t = q1table({('W1', 48, 's'): q('GROWS', marks=met), ('W1', 96, 's'): q('GROWS', marks=failm)})
    f1_, _, w1 = ST.decide_q1(t, nohalf)
    expect('Q2 known failed mark', ST.decide_q2(f1_, w1, t, 'Q1B-NO-CALL', [], {})[0], 'END-OTHER')
    expect('Q2 not triggered', ST.decide_q2('RING-STABLE', [], t, 'NEUTRAL-HOLDS', [], {})[0], 'END-NOT-TRIGGERED')

    def sq(cls, valid=True, slope=0.02, marks=None):
        return dict(cls=cls, valid=valid, maxD=0.3, slope=slope, se=0.001, marks=marks or met)

    def shtable(over=None, default='HOLDS'):
        t = {(p, M, a): sq(default, slope=0.0) for p in ST.SHAPE_BEARING for M in Ms for a in ('s', 'c')}
        t.update(over or {})
        return t
    ctrl_ok = {M: dict(maxD_rel=1e-9, slope_rel=1e-12) for M in Ms}
    g4ok = {M: True for M in Ms}
    nohalf2 = {p: False for p in ST.SHAPE_BEARING}
    expect('Q1b all hold', ST.decide_q1b(shtable(), nohalf2, ctrl_ok, g4ok, cfg)[0], 'NEUTRAL-HOLDS')
    expect('Q1b failed check blocks HOLDS', ST.decide_q1b(shtable({('S3', 48, 'c'): sq('UNAVAILABLE', valid=False)}), nohalf2, ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    expect('Q1b failed check blocks DRIFTS',
           ST.decide_q1b(shtable({('S3', M, 's'): sq('DRIFTS') for M in Ms} | {('S3', 48, 'c'): sq('UNAVAILABLE', valid=False)}),
                         nohalf2, ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    t = shtable({('S3', M, 's'): sq('DRIFTS') for M in Ms} | {('S3', 48, 'c'): sq('DRIFTS')})
    fq, _, wq = ST.decide_q1b(t, nohalf2, ctrl_ok, g4ok, cfg)
    q2 = ST.decide_q2('RING-STABLE', [], q1table(), fq, wq, t)
    expect('Q1b witness DRIFTS at the scored amplitude at both M; Q2 qualifying set is the two scored runs only',
           (fq, wq, q2[0], sorted(q2[2])), ('NEUTRAL-DRIFTS', ['S3'], 'END-FOLD', [('S3', 48, 's'), ('S3', 96, 's')]))
    t = shtable({('S3', 48, 'c'): sq('DRIFTS'), ('S3', 96, 's'): sq('DRIFTS')})
    expect('Q1b DRIFTS at check at one M and scored at the other is no witness', ST.decide_q1b(t, nohalf2, ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    t = shtable({('S3', 96, 's'): sq('DRIFTS')})
    expect('Q1b DRIFTS at the scored amplitude at one M only is no witness', ST.decide_q1b(t, nohalf2, ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    t = shtable({('S3', M, 'c'): sq('DRIFTS') for M in Ms})
    expect('Q1b DRIFTS at the check amplitude at both M, scored HOLDS: no witness', ST.decide_q1b(t, nohalf2, ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    drift_t = shtable({('S3', M, 's'): sq('DRIFTS', slope=0.002) for M in Ms})
    ctrl_drift = {M: cs for M in Ms}
    expect('g1 quiet-then-drifting control blocks', ST.decide_q1b(drift_t, nohalf2, ctrl_drift, g4ok, cfg)[0], 'Q1B-NO-CALL')
    expect('g2 half-blocked witness cannot witness', ST.decide_q1b(shtable({('S3', M, 's'): sq('DRIFTS') for M in Ms}), dict(nohalf2, S3=True), ctrl_ok, g4ok, cfg)[0], 'Q1B-NO-CALL')
    expect('g4 floor fails', ST.decide_q1b(shtable(), nohalf2, ctrl_ok, {48: True, 96: False}, cfg)[0], 'Q1B-NO-CALL')
    wob = shtable({('S4', M, 's'): sq('WOBBLES', slope=0.0) for M in Ms})
    expect('Q1b wobbles', ST.decide_q1b(wob, nohalf2, ctrl_ok, g4ok, cfg)[0], 'NEUTRAL-WOBBLES')
    ck.seal('statcred/results', json.dumps(res, sort_keys=True).encode())
    badl = [r for r in res if not r['ok']]
    for r in res:
        print(f'  stat_credential {"PASS" if r["ok"] else "FAIL"}: {r["name"]} -> {r["got"]} (pre-stated {r["want"]})', flush=True)
    K.require(not badl, 'stat_credential: fixture(s) failed: ' + '; '.join(r['name'] for r in badl))
    return dict(n=len(res), all_pass=True)


# ---------------------------------------------------------------------------------------------------------------
UNITS = ([('credential', unit_credential), ('setup', unit_setup), ('stat_credential', unit_stat_credential), ('static', unit_static)]
         + [(n, make_run_unit(n)) for n in SPECS]
         + [(f'dshape_{n}', make_dshape_unit(n)) for n in SHAPE_RUNS])

if __name__ == '__main__':
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
