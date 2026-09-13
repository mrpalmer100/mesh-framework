"""PROBE-94 (2026-08-20) -- the decisive bounded experiment of the
NATIVE-96 session, run under the locked bars' control-(0*) lineage in
the SCOUT'S direction (64 -> 96), because the native march measured a
real dA2/ds collapse (~6.5e-4 at A2 = 0.0048 to ~6.8e-5 at 0.0063,
member-grade solves, still decaying) that prices the native approach
to the third shared pin at 500-1000 arc steps.

THE QUESTION: does the aligned branch exist at 96 x 36 at the third
shared RAMP_CONV pin (A2 = 0.009396), where the FND-142 64 x 24 member
converged? Procedure is the registered FND-143 deviation verbatim:
regenerate the 64 x 24 member with stage 2's OWN code, chart-convert
and FFT-interpolate to 96 x 36 (angle-safe psit handling), and
re-solve ARC-ANCHORED at ds = 0 against the interpolated tangent, with
A2 measured into the 5e-3 drift gate rather than pinned (the a2 pin is
near-singular natively in this region -- the measured 64-round stall).

OUTCOME (a): converges nearby (drift < 5e-3, closure < 1e-6) -- the
branch exists natively at 0.0094; the march crawl is traversable
geometry; session verdict RATES-REGISTERED with a CI-resumable walk.
OUTCOME (b): fails to converge or drifts beyond the gate -- the 64-grid
contamination boundary sits near A2 ~ 0.006, far deeper than the
gamma = 0.558 the scout could see; FND-143 is strengthened and the
asymptote scenario leads for the Sigma_wave question.

Checkpoint: /tmp/p94_ckpt.pkl (separate from the march checkpoint,
which stays valid for CI resumption regardless of this outcome).
"""
import sys
import time
import pickle
import pathlib
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations.traverse_steepened import TGrid, RMS_BAR
from benchmarks.foundations.traverse96_scout import TGrid96, interp_x, \
    lm_round, gn_exact
from benchmarks.foundations import truestate_stage2 as S2

CKPT = pathlib.Path('/tmp/p94_ckpt.pkl')
N96CKPT = pathlib.Path('/tmp/n96_ckpt.pkl')
A2_PIN = float(S2.RAMP_CONV[2])
DRIFT_BAR = 5e-3
CLOS_BAR = 1e-6


def load():
    return pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def solve96(T, st, key, x0, aux, deadline, rounds_max=60):
    """The NATIVE-96 ladder, restated locally so the probe writes its
    own checkpoint (importing the march module's ladder would write
    the march checkpoint). Numerics identical: f32-store LM high, f64
    LM mid, exact GN low; margin 100 s for the container chunk."""
    cur = st.get(key)
    x = cur['x'] if cur else x0
    rounds = cur['rounds'] if cur else 0
    while rounds < rounds_max:
        if deadline and time.time() > deadline - 100:
            st[key] = dict(x=x, rounds=rounds)
            save(st)
            return x, T.field_rms(x), False
        r_now = T.field_rms(x)
        if r_now < 3e-5:
            x, r, acc = gn_exact(T, x, 'arc', aux)
            rounds += 1
            print(f"      [round {rounds} (gnx): RMS {r:.1e}"
                  f"{'' if acc else '  (no step)'}]", flush=True)
            if not acc:
                break
        elif r_now < 5e-4:
            lam = st.get(key + '_lam', 1e-6)
            x, lam, r, acc = lm_round(T, x, 'arc', aux, lam, f64=True)
            st[key + '_lam'] = lam
            rounds += 1
            print(f"      [round {rounds} (f64): RMS {r:.1e}  "
                  f"lam {lam:.0e}]", flush=True)
        else:
            lam = st.get(key + '_lam', 1e-4)
            x, lam, r, acc = lm_round(T, x, 'arc', aux, lam)
            st[key + '_lam'] = lam
            rounds += 1
            print(f"      [round {rounds}: RMS {r:.1e}  lam {lam:.0e}"
                  f"{'' if acc else '  (no step accepted)'}]",
                  flush=True)
            if not acc and lam > 1e6:
                break
        if r < RMS_BAR:
            break
    st.pop(key, None)
    st.pop(key + '_lam', None)
    return x, T.field_rms(x), True


def main(argv):
    deadline = None
    if '--budget' in argv:
        deadline = time.time() + float(argv[argv.index('--budget') + 1])
    st = load()
    if '--reset' in argv:
        st = {}

    G = S2.Grid(64, 24)
    # STAGE A: the 64 x 24 member at the third pin, by stage 2's own
    # instrument, seeded from the (0*) checkpointed member at pin 2.
    if 'x64' not in st:
        if 'x64_work' in st:
            x2w = st['x64_work']
        else:
            n96 = pickle.loads(N96CKPT.read_bytes())
            x2w = n96['x0_x64']
            r0 = G.rms(x2w, float(S2.RAMP_CONV[1]), -1)
            print(f"PROBE-94 -- stage A: seed = the (0*) 64-grid member "
                  f"at pin 2 (RMS there {r0:.1e}); converging at "
                  f"A2 = {A2_PIN:.6f}", flush=True)
        for it in range(24):
            if deadline and time.time() > deadline - 60:
                st['x64_work'] = x2w
                save(st)
                print("  [chunk end; rerun to resume]", flush=True)
                return 3
            x2w = S2.converge(G, x2w, A2_PIN, -1, tol=1e-9, chunks=1)
            r = G.rms(x2w, A2_PIN, -1)
            print(f"    [64-grid lsq pass {it + 1}: RMS {r:.1e}]",
                  flush=True)
            if r < 1e-9:
                break
        if r >= 1e-9:
            print(f"PROBE-94: stage A DID NOT CONVERGE (RMS {r:.1e}). "
                  f"The 64 x 24 regeneration itself fails from the "
                  f"pin-2 seed; recorded as its own finding.",
                  flush=True)
            st['verdict'] = 'A-unconverged'
            save(st)
            return 1
        _, _, _, gam64, _, om2_64 = G.unpack(x2w)
        st['x64'] = x2w
        st['gam64'], st['om2_64'] = float(gam64), float(om2_64)
        st.pop('x64_work', None)
        save(st)
        print(f"    64-grid member: RMS {r:.1e}  gamma = {gam64:.6f}  "
              f"Om2 = {om2_64:.5f}", flush=True)

    # STAGE B: chart-convert + interpolate both 64 members; tangent.
    T64, T96 = TGrid(64, 24), TGrid96(96, 36)
    if 'x96i' not in st:
        n96 = pickle.loads(N96CKPT.read_bytes())
        xa = interp_x(T64, T96, T64.from_stage2(n96['x0_x64']))
        xb = interp_x(T64, T96, T64.from_stage2(st['x64']))
        st['x96a'], st['x96i'] = xa, xb
        save(st)
        print(f"PROBE-94 -- stage B: interpolated to 96 x 36; "
              f"interpolation-image field RMS {T96.field_rms(xb):.1e}",
              flush=True)

    # STAGE C: arc-anchored re-solve at ds = 0 (registered deviation
    # form; A2 measured, not pinned).
    xb = st['x96i']
    t = xb - st['x96a']
    t = t / float(np.linalg.norm(t))
    if 'landed' in st:
        # stage C already adjudicated; do not re-run it (guard added
        # after one redundant chunk -- the completed solve pops its
        # resumable key, so re-entry restarted from the seed).
        xs = st['landed']
        r = T96.field_rms(xs)
        m = st['metrics']
    else:
        xs, r, done = solve96(T96, st, 'resolve', xb, (xb, t, 0.0),
                              deadline)
        if not done:
            return 3
        m = T96.report(xs, 'PROBE-94 landed @96x36')
    clos = float(m['clos']) if 'clos' in m \
        else float(T96.closure_max(xs))
    dg = abs(m['gam'] - st['gam64']) / abs(st['gam64'])
    do = abs(m['om2'] - st['om2_64']) / abs(st['om2_64'])
    da = abs(m['A2'] - A2_PIN) / A2_PIN
    conv = r < RMS_BAR
    inb = max(dg, do, da) < DRIFT_BAR and clos < CLOS_BAR
    print(f"PROBE-94 verdict inputs: converged = {conv} "
          f"(RMS {r:.1e})  drift gamma {dg:.2e}  Om2 {do:.2e}  "
          f"A2 {da:.2e}  closure {clos:.1e}", flush=True)
    if conv and inb:
        print("PROBE-94 VERDICT: OUTCOME (a) -- the branch EXISTS "
              "natively at the third shared pin. The march crawl is "
              "traversable geometry; RATES-REGISTERED with a "
              "CI-resumable walk.", flush=True)
        st['verdict'] = 'a'
    else:
        print("PROBE-94 VERDICT: OUTCOME (b) -- the 64-grid member "
              "does NOT re-solve within the gates natively. The "
              "contamination boundary sits near A2 ~ 0.006; FND-143 "
              "is strengthened and the asymptote scenario leads.",
              flush=True)
        st['verdict'] = 'b'
    st['landed'] = xs
    st['metrics'] = dict(m, clos=clos, dg=dg, do=do, da=da,
                         rms=float(r))
    save(st)

    # STAGE D (2026-08-20, added on the landed face, annotated): the
    # landed state converged (2.7e-10, closure 9.5e-9) but carries
    # wsNyq = 2.6e-3 -- five hundredfold the mild members. Under bars
    # delta 4 the tail trigger is armed: the 112 x 42 confirmation is
    # OWED before the landed numbers are citable. If it confirms, the
    # single-coordinate A2 displacement (+0.73%, out-of-gate; gamma
    # and Om2 in-gate) stands as the finding. If it fails, the
    # exhaustion is PROGRESSIVE across grids -- the strongest form of
    # the FND-143 lesson. Budget-boxed; partial trajectories are
    # recorded if the box empties.
    from benchmarks.foundations.native96_continuation import \
        gn_exact_f32j, gn_descent_capped, interp_to
    Tc = TGrid96(112, 42)
    if 'conf_seed' not in st:
        st['conf_seed'] = interp_to(T96, Tc, xs)
        print(f"PROBE-94 -- stage D: confirmation at 112 x 42; "
              f"interpolation-image field RMS "
              f"{Tc.field_rms(st['conf_seed']):.1e}", flush=True)
        save(st)
    xb2 = st['conf_seed']
    t2 = xb2 - interp_to(T96, Tc, st['x96a'])
    t2 = t2 / float(np.linalg.norm(t2))
    cur = st.get('confsolve')
    xc = cur['x'] if cur else xb2
    rounds = cur['rounds'] if cur else 0
    # cap 40 -> 80 (2026-08-21, annotated): at round 32 the floor
    # contracts steadily (~7%/pair) and the exact-GN bounces are
    # SHRINKING (1.2e-4 -> 4.9e-5) -- the pre-snap signature. A
    # cap is a budget, not a bar (registered scheduling argument).
    #
    # CAP 80 -> 240 AND THE NO-VERDICT GUARD (2026-08-21 session 3,
    # annotated in place). Two changes, both scheduling, neither
    # numerical:
    #   (a) The cap is raised again on the same registered argument.
    #       The round-38 close-out left the floor still contracting
    #       ~7-8% per pair without decay, which is a budget state and
    #       not a bar state; 240 prices the uncapped finish of the
    #       contraction at the measured per-pair rate with headroom.
    #   (b) THE GUARD IS THE IMPORTANT PART. As written, exhausting
    #       the cap fell THROUGH to the verdict block and would have
    #       registered conf_verdict = 'failed' on a still-descending
    #       solve -- a budget adjudicated as a bar, which the house
    #       rules forbid and which would have mis-registered the
    #       decisive displacement-vs-progressive-exhaustion call.
    #       Cap exhaustion now exits NO-VERDICT and resumable, the
    #       same exit a chunk-end budget takes. Only a genuine
    #       stall (no step accepted) or the RMS bar adjudicates.
    #
    # SCHEDULING FINDING (2026-08-21 session 3, measured, and it
    # REVERSES a registered instrument note): the earlier record
    # states that background processes die at the tool-call boundary,
    # which is why every previous stage-D chunk ran foreground with a
    # 200 s margin and ~1-3 rounds per call. Measured here: a run
    # launched under setsid with stdio redirected SURVIVES the
    # boundary and keeps running between calls. The uncapped finish
    # is therefore in-session work, not CI-only work. The per-round
    # save below is what makes that safe -- a detached run that is
    # reaped loses at most one round instead of the whole chunk.
    #
    # INCIDENT KEPT ON THE RECORD (2026-08-21 session 3): the first
    # detached run was REAPED at round 42, silently and with no
    # traceback -- the container's OOM signature, not a solver
    # failure. Cause: document work (pandoc, then soffice and the
    # diagram renderer for the plain-language guide rebuild) was run
    # in the SAME container while a stage-D round held ~2.7 GB of a
    # 4 GB budget. THE RULE THIS BUYS: a detached stage-D run is
    # MEMORY-EXCLUSIVE. While it is live, no soffice, no pandoc, no
    # second solve; monitoring commands only. The per-round save held
    # and the round-42 state plus its floor trajectory survived
    # intact, which is the whole reason that save exists.
    CONF_CAP = 240
    cap_exhausted = True
    while rounds < CONF_CAP:
        if deadline and time.time() > deadline - 200:
            st['confsolve'] = dict(x=xc, rounds=rounds)
            save(st)
            print("  [chunk end; rerun to resume]", flush=True)
            return 3
        rn = Tc.field_rms(xc)
        if rn < 5e-4:
            # ESCALATION SCHEDULE (2026-08-21, annotated; lineage:
            # the march's measured-crawl alternation): eight rounds
            # of pure exact-GN circulated (2.0e-4 -> 2.6e-4 field
            # while the weighted objective descended); the endgame
            # now ALTERNATES exact-GN with the capped min-norm
            # descent. Tools unchanged; schedule only.
            if rounds % 2 == 0:
                xc, rc2, acc = gn_exact_f32j(Tc, xc, 'arc',
                                             (xb2, t2, 0.0))
                tagc = 'gnx-f32j'
            else:
                xc, rc2, acc = gn_descent_capped(Tc, xc, 'arc',
                                                 (xb2, t2, 0.0))
                tagc = 'gnd-capped'
            rounds += 1
            print(f"      [conf round {rounds} ({tagc}): RMS "
                  f"{rc2:.1e}{'' if acc else '  (no step)'}]",
                  flush=True)
            if not acc and tagc == 'gnx-f32j':
                cap_exhausted = False
                break
        else:
            # MEMORY (2026-08-20, annotated after an OOM in stage D):
            # the f32 lm_round at 112 x 42 accumulates an f64 normal
            # matrix (1.59 GB) alongside its 0.80 GB Jacobian and the
            # container reaps it. The high-residual phase therefore
            # uses the capped-lsmr descent (Jacobian-only memory) --
            # the confirmations never met this because mild seeds
            # enter below 5e-4 and go straight to the endgame.
            xc, rc2, acc = gn_descent_capped(Tc, xc, 'arc',
                                             (xb2, t2, 0.0))
            rounds += 1
            print(f"      [conf round {rounds} (gnd-capped): RMS "
                  f"{rc2:.1e}{'' if acc else '  (no step)'}]",
                  flush=True)
            if not acc:
                cap_exhausted = False
                break
        # PER-ROUND SAVE (2026-08-21 session 3, annotated): the
        # checkpoint used to be written only at a budget exit, so a
        # detached or reaped run lost every round it had taken. The
        # floor trajectory is also kept here, because the trajectory
        # -- not the endpoint alone -- is what the contraction
        # argument is read off, and a run that is reaped mid-fight
        # must still leave its measured rates behind.
        st['confsolve'] = dict(x=xc, rounds=rounds)
        st.setdefault('conf_traj', []).append(
            (rounds, tagc if rn < 5e-4 else 'gnd-capped',
             float(rc2), bool(acc)))
        save(st)
        if rc2 < RMS_BAR:
            cap_exhausted = False
            break
    if cap_exhausted:
        # See the CONF_CAP annotation: a budget must not adjudicate.
        st['confsolve'] = dict(x=xc, rounds=rounds)
        save(st)
        print(f"  [cap {CONF_CAP} reached with the solve still "
              f"live: NO VERDICT, resumable from the checkpoint]",
              flush=True)
        return 3
    mc = Tc.report(xc, 'PROBE-94-CONF landed @112x42')
    closc = float(Tc.closure_max(xc))
    dgc = abs(mc['gam'] - m['gam']) / abs(m['gam'])
    doc = abs(mc['om2'] - m['om2']) / abs(m['om2'])
    dac = abs(mc['A2'] - m['A2']) / m['A2']
    convc = Tc.field_rms(xc) < RMS_BAR
    print(f"PROBE-94-CONF verdict inputs: converged = {convc} (RMS "
          f"{Tc.field_rms(xc):.1e})  drift vs 96 landed: gamma "
          f"{dgc:.2e}  Om2 {doc:.2e}  A2 {dac:.2e}  closure "
          f"{closc:.1e}", flush=True)
    if convc and max(dgc, doc, dac) < DRIFT_BAR and closc < CLOS_BAR:
        print("PROBE-94-CONF: the 96-grid landed state CONFIRMS at "
              "112 x 42. The A2-displacement finding is citable.",
              flush=True)
        st['conf_verdict'] = 'confirmed'
    else:
        print("PROBE-94-CONF: the 96-grid landed state DOES NOT "
              "confirm -- PROGRESSIVE resolution exhaustion across "
              "grids.", flush=True)
        st['conf_verdict'] = 'failed'
    st['conf_landed'] = xc
    st['conf_metrics'] = dict(mc, clos=closc, dg=dgc, do=doc, da=dac)
    save(st)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

