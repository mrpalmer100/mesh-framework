"""WHY-WINDING PROBE 144x42, under WHYWIND_probe42_bars_LOCKED.md.
Reuses whywind_stage3's phase-resumable machinery. Checkpoint
/tmp/p42_ckpt.pkl; rerun to resume; verdict renders when the
required 4/3 pair gates (control pair appended if present)."""
import pathlib
import pickle
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import benchmarks.foundations.whywind_stage3 as W3               # noqa: E402
from benchmarks.foundations.qsweep_stage1 import (                # noqa: E402
    QTGrid, metrics, RMS_BAR, CLOSURE_BAR)

CKPT = pathlib.Path('/tmp/p42_ckpt.pkl')
CK2C = pathlib.Path('analysis/qsweep_stage2c_ckpt.pkl')
CELLS = {'4/3': (3, 4), '5/3': (3, 5)}


def load():
    return pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


W3.save = save


def phipad(field, np_new):
    ns, npn = field.shape
    F = np.fft.fft(field, axis=1) / npn
    G = np.zeros((ns, np_new), complex)
    kp = np.fft.fftfreq(npn, 1 / npn).astype(int)
    for j, n in enumerate(kp):
        G[:, n % np_new] = F[:, j]
    return (np.fft.ifft(G, axis=1) * np_new).real


def seed(T_old, T_new, x):
    th, pt, Tf, om1, om2 = T_old.unpack(np.asarray(x))
    f = lambda a: phipad(a, T_new.NP)
    return T_new.pack(f(th), f(pt), f(Tf), om1, om2)


def band17(T, t):
    tp = t[T.N:2 * T.N].reshape(T.NS, T.NP)
    P = np.abs(np.fft.fft2(tp)) ** 2
    tot = P.sum()
    s = 0.0
    for sgn in (1, -1):
        for dm in (-1, 0, 1):
            for dn in (-1, 0, 1):
                s += P[(sgn * (19 + dm)) % T.NS, (sgn * (17 + dn)) % T.NP]
    return s / tot, P


def main():
    budget = 0
    if '--budget' in sys.argv:
        budget = int(sys.argv[sys.argv.index('--budget') + 1])
    deadline = time.time() + budget if budget else None
    st = load()
    st2c = pickle.loads(CK2C.read_bytes())
    for q in ('4/3', '5/3'):
        n1, n2 = CELLS[q]
        T_old = QTGrid(144, 36, n1, n2)
        Tn = QTGrid(144, 42, n1, n2)
        W3.bind_resumable_jac(Tn, f'p42_{q.replace("/", "")}')
        X = st2c['prof-%s' % q]['states']
        for which, idx in (('prev', 11), ('deep', 12)):
            key = f'p42|{q}|{which}'
            if st.get(key + '|done'):
                continue
            x_src = np.asarray(X[idx])
            x0 = st.get(key + '|x')
            if x0 is None:
                x0 = seed(T_old, Tn, x_src)
            _, c2 = T_old.modes(T_old.geom(x_src)[2])
            a2pin = float(np.abs(c2))
            print(f"== solving {key} (dof {Tn.n}, pin {a2pin:.7f})",
                  flush=True)
            while True:
                roll = time.time() + 420
                if deadline:
                    roll = min(roll, deadline)
                xs, rms, done = W3.resumable_lm(
                    Tn, st, key + '|solve', x0, a2pin, roll)
                st[key + '|x'] = xs
                x0 = xs
                save(st)
                if done or (deadline and time.time() > deadline - 210):
                    break
            if done:
                m = metrics(Tn, xs)
                gated = (m['rms'] < RMS_BAR and m['clos'] < CLOSURE_BAR)
                st[key + '|done'] = True
                st[key + '|gated'] = gated
                st[key + '|metrics'] = m
                print(f"   gated={gated} RMS {m['rms']:.2e} clos "
                      f"{m['clos']:.2e} A2 {m['A2']:.7f} om2 "
                      f"{m['om2']:.5f}", flush=True)
                save(st)
            if deadline and time.time() > deadline - 210:
                print('budget reached; rerun to resume.')
                return
        if q == '4/3':
            render(st, st2c, required_only=True)
    render(st, st2c, required_only=False)


def render(st, st2c, required_only):
    kp, kd = 'p42|4/3|prev', 'p42|4/3|deep'
    if not (st.get(kp + '|gated') and st.get(kd + '|gated')):
        return
    if st.get('verdict_printed') and required_only:
        return
    n1, n2 = CELLS['4/3']
    T_old = QTGrid(144, 36, n1, n2)
    Tn = QTGrid(144, 42, n1, n2)
    X = st2c['prof-4/3']['states']
    t_old = np.asarray(X[12]) - np.asarray(X[11])
    t_old /= np.linalg.norm(t_old)
    F17_36, _ = band17(T_old, t_old)
    t_new = st[kd + '|x'] - st[kp + '|x']
    t_new /= np.linalg.norm(t_new)
    F17_42, P = band17(Tn, t_new)
    nidx = np.fft.fftfreq(42, 1 / 42).astype(int)
    hi = P[:, (np.abs(nidx) >= 19)].sum() / P.sum()
    im = np.unravel_index(np.argmax(P), P.shape)
    m = im[0] if im[0] <= 72 else im[0] - 144
    n = im[1] if im[1] <= 21 else im[1] - 42
    dom_in = (abs(m), abs(n)) in {(a, b) for a in (18, 19, 20)
                                  for b in (16, 17, 18)}
    print('\n== VERDICT BLOCK (P42) ==')
    print(f'F17(144x36 retained) = {F17_36:.3f}   '
          f'F17(144x42) = {F17_42:.3f}')
    print(f'dominant 144x42 pt mode: (m={m:+d}, n={n:+d}) '
          f'in-band={dom_in}; HIBAND42 = {hi:.3f}')
    phys = F17_42 >= 0.5 * F17_36 and dom_in and hi < 0.10
    art = F17_42 < 0.05
    v = 'P42-PHYSICAL' if phys else ('P42-ARTIFACT' if art
                                     else 'P42-OPEN')
    print(f'\n**** VERDICT: {v} ****', flush=True)
    st['verdict_printed'] = True
    save(st)


if __name__ == '__main__':
    main()

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

