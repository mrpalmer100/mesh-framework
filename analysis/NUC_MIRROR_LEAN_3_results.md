# NUC-MIRROR-LEAN-3: results (verdict rendered 2026-11-05; design analysis/NUC_MIRROR_LEAN_3_design_SEALED.md)

FORM (Q1): U-MISS-HIGH -- mean - h = +0.21358 > B1 = 0.085

n = 31 T = 1/2 mirror pairs at odd A >= 13, every pair with both rows in the pinned AME2012 table (sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13); predictions CDE_U(A) = a_c() A^(2/3) with a_c() = 0.7716295256894924 MeV sealed before the table was read (file analysis/NUC_MIRROR_LEAN_3_pred.txt, sha256 51c713ba12657100c0b4eb7fa84b92b411baa766c7b699b90ac7ae8e712a599a).

mean_delta = +0.246423; rms_delta = 0.256005; min +0.168872 at A = 69; max +0.439992 at A = 17; diagnostic Z(Z-1) mean +0.208843 (no form).

Floor: h_boot = 0.032841 (seed 20261104, 10000 resamples, 99.0th percentile); h_inst = 0.005954 (0.100 MeV sqrt 2 / CDE_U(13) / sqrt n); h = 0.032841; band B1 = 0.085; sign_resolved = True (decides nothing).

Rule applied in the locked order: (1) h > B1 U-NULL-FLOOR; (2) |mean| + h <= B1 U-AGREES; (3) mean - h > B1 U-MISS-HIGH; (4) mean + h < -B1 U-MISS-LOW; (5) otherwise U-OPEN-BAND.

| A | Z_p | CDE_meas (MeV) | CDE_U (MeV) | delta |
|---|---|---|---|---|
| 13 | 7 | 3.002819 | 4.266166 | +0.420720 |
| 15 | 8 | 3.536513 | 4.693207 | +0.327072 |
| 17 | 9 | 3.542811 | 5.101620 | +0.439992 |
| 19 | 10 | 4.021845 | 5.494286 | +0.366111 |
| 21 | 11 | 4.329486 | 5.873384 | +0.356601 |
| 23 | 12 | 4.838935 | 6.240615 | +0.289667 |
| 25 | 13 | 5.058953 | 6.597340 | +0.304092 |
| 27 | 14 | 5.594705 | 6.944666 | +0.241293 |
| 29 | 15 | 5.724974 | 7.283512 | +0.272235 |
| 31 | 16 | 6.180363 | 7.614650 | +0.232072 |
| 33 | 17 | 6.364864 | 7.938738 | +0.247275 |
| 35 | 18 | 6.748477 | 8.256339 | +0.223438 |
| 37 | 19 | 6.929796 | 8.567945 | +0.236392 |
| 39 | 20 | 7.306835 | 8.873983 | +0.214477 |
| 41 | 21 | 7.277823 | 9.174831 | +0.260656 |
| 43 | 22 | 7.649363 | 9.470825 | +0.238119 |
| 45 | 23 | 7.910919 | 9.762263 | +0.234024 |
| 47 | 24 | 8.227261 | 10.049414 | +0.221478 |
| 49 | 25 | 8.478302 | 10.332519 | +0.218702 |
| 51 | 26 | 8.823512 | 10.611798 | +0.202673 |
| 53 | 27 | 9.070454 | 10.887448 | +0.200320 |
| 55 | 28 | 9.476381 | 11.159651 | +0.177628 |
| 57 | 29 | 9.557313 | 11.428575 | +0.195794 |
| 59 | 30 | 9.925124 | 11.694370 | +0.178259 |
| 61 | 31 | 9.996496 | 11.957179 | +0.196137 |
| 63 | 32 | 10.408223 | 12.217130 | +0.173796 |
| 65 | 33 | 10.323512 | 12.474345 | +0.208343 |
| 67 | 34 | 10.789283 | 12.728934 | +0.179776 |
| 69 | 35 | 11.105582 | 12.981002 | +0.168872 |
| 71 | 36 | 10.957560 | 13.230647 | +0.207445 |
| 75 | 38 | 11.382347 | 13.723019 | +0.205641 |

Credentials: C-1, C-2, C-3 (F1 to F5 and T4), C-4, C-5, C-6 all passed (the driver halts otherwise).
Fixtures: {'F1': {'mean': 0.11111111111111116, 'h_boot': 0.0, 'h': 0.011720125593549844, 'form': 'U-MISS-HIGH'}, 'F2': {'mean': 0.0, 'h_boot': 0.0, 'h': 0.011720125593549844, 'form': 'U-AGREES'}, 'F3': {'mean': -0.16666666666666663, 'h_boot': 5.551115123125783e-17, 'h': 0.011720125593549844, 'form': 'U-MISS-LOW'}, 'F4': {'mean': 0.08000000000000007, 'h_boot': 0.02250000000000002, 'h': 0.02250000000000002, 'form': 'U-OPEN-BAND'}, 'F5': {'mean': 0.25, 'h_boot': 0.1875, 'h': 0.1875, 'form': 'U-NULL-FLOOR'}, 'T4': 'C-5 halt, 0 mass conversions'}

What this does not establish: the cause of any miss (self-energy, exchange, diffuseness, the odd nucleon, charge-symmetry breaking); NUC-C; the mass models' absolute accuracy; anything about A < 13, T = 1 or 3/2, or a trend in A. The rider wording is the design's section 7 for this form. Grade D2 unchanged; no North Star number moves.
