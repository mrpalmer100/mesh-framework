"""GRANT-CANDIDATE-CONTACT-SECTION, cheap test T-1 (sandbox, 2026-10-04; a display for the price sheet, no claim).
The registered contact form is V(r) = A_c / (1 + (r/sigma)^4) in the CENTRE-LINE separation r
(commission_h_rerun_torsion.py, EM-RECON-023), so the registered engine cannot see a cross-section at all;
T-1 therefore runs on the geometry the price sheet's P1 names: a two-strand rope's section is two discs of
radius rho side by side, whose half-extent in the direction phi from the pair axis is the support function
h(phi) = rho (1 + |cos phi|). A section-aware contact replaces r by the surface gap, r - [h1(phi1) + h2(phi2) - 2 h_bar],
with h_bar = rho (1 + 2/pi) the circular reference, so that circular sections reproduce the registered form exactly.
Read: the period of V in each azimuth (n), the sign of the preferred orientation (phi_0), and the amplitude of the
orientation-dependent part relative to the line part, as a function of rho/sigma (the one unregistered ratio).
"""
import numpy as np
Ac = 1.0


def h(phi, rho): return rho * (1.0 + np.abs(np.cos(phi)))


def V(r, phi1, phi2, rho, sigma):
    hbar = rho * (1.0 + 2.0 / np.pi)
    gap = r - (h(phi1, rho) + h(phi2, rho) - 2 * hbar)
    return Ac / (1.0 + (np.clip(gap, 1e-9, None) / sigma) ** 4)


def main():
    sigma = 1.0; phis = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    print("[cs T1] section: two discs side by side (rho each); support function h(phi) = rho (1 + |cos phi|); contact V = A_c/(1 + (gap/sigma)^4)")
    print(f"[cs T1] {'r/sigma':>8s} {'rho/sigma':>9s} {'V_line':>8s} {'V_sec/V_line':>12s} {'period/pi':>9s} {'preferred':>10s} {'2nd harm/1st':>12s}")
    rows = []
    for r_over in (0.8, 1.0, 1.2, 1.5):
        for rho_over in (0.05, 0.1, 0.2, 0.3, 0.5):
            r = r_over * sigma; rho = rho_over * sigma
            v = V(r, phis, 0.0, rho, sigma)                      # phi2 fixed at 0 (crossed partner lying flat), sweep phi1
            F = np.fft.rfft(v - v.mean()) / len(v) * 2
            k = int(np.argmax(np.abs(F[1:])) + 1)                 # dominant harmonic in phi1
            period_over_pi = 2.0 / k
            Vline = V(r, np.pi / 2 + 1e-9, np.pi / 2 + 1e-9, rho, sigma)  # both sections at the circular reference? no: use the mean over orientations
            Vline = v.mean()
            amp = (v.max() - v.min()) / 2
            pref = 'flat (minor radius faces)' if v[np.argmin(v)] == v.min() and abs(np.cos(phis[np.argmin(v)])) < 0.1 else 'crossed'
            h2 = abs(F[2 * k]) / abs(F[k]) if 2 * k < len(F) else 0.0
            rows.append((r_over, rho_over, Vline, amp / Vline, period_over_pi, pref, h2))
            print(f"[cs T1] {r_over:8.2f} {rho_over:9.2f} {Vline:8.4f} {amp / Vline:12.3f} {period_over_pi:9.2f} {pref:>10s} {h2:12.3f}")
    # the full two-azimuth surface at one representative point: Fourier content in (phi1, phi2)
    r, rho = 1.0, 0.2
    P1, P2 = np.meshgrid(phis, phis, indexing='ij'); S = V(r, P1, P2, rho, sigma)
    F2 = np.abs(np.fft.rfft2(S - S.mean())) / S.size * 4
    i, j = np.unravel_index(np.argmax(F2[1:, 1:]), F2[1:, 1:].shape); i += 1; j += 1
    print(f"[cs T1] two-azimuth surface at r/sigma 1.0, rho/sigma 0.2: dominant mixed harmonic (k1, k2) = ({i}, {j}); separable n = 2 in each azimuth: {i == 2 and j == 2}")
    np.savez('analysis/contact_section_t1.npz', rows=np.array(rows, dtype=object))
    print("[cs T1] sealed -> analysis/contact_section_t1.npz")


if __name__ == '__main__':
    main()
