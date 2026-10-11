# Lab decision: GRV-BLIND-2, beacon-draw

- When: 2026-10-11 11:52:01 -0400
- Decided by: the lab
- Choice: **drew from drand round 6543429 (seed 1083026663)**

## Why

The protocol needed a seed that nobody chose. The round was committed to the lab branch before it existed; its published randomness gave the seed; the draw ran unchanged in the job tree.

## Detail

```json
{
  "round": 6543429,
  "chain": "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce",
  "randomness": "c08dace7ee5f8c780b82fab93f43be0111d546a45b1895192d0d5ac14d857622",
  "seed": 1083026663,
  "command": "python tools/holdout_galaxies.py draw --name GRV_BLIND_2 --seed {seed} --n 30 --drawn-by \"{drawn_by}\"",
  "drawn_by": "drand beacon round 6543429 (chain 8990e7a9aaed2ffe)",
  "commit_fixing_round": "b0f8e1708d27165e086d49aa5d1492124e0633f1",
  "output_tail": "[holdout] GRV_BLIND_2: 30 galaxies held out of 155 eligible (175 files); seed 1083026663; drawn by drand beacon round 6543429 (chain 8990e7a9aaed2ffe)\n[holdout] paste into the locked charter:\n  train   sha256 26a7721fd44601e8af72e98a12cfe10d127c5bada6e4fb71b967e44b752c10b5  (analysis/holdout/GRV_BLIND_2/train.txt)\n  test    sha256 3fa3db3331fcf8d8390349b6828613b8e4f664caec4c240d0168c67b19ae807b  (the concatenated sealed truth; NOT to be read)\n  held out: D564-8, DDO064, DDO161, ESO079-G014, NGC0024, NGC2366, NGC3726, NGC4217, NGC5585, NGC6015, NGC6195, NGC6674, NGC7814, PGC51017, UGC00731, UGC02916, UGC02953, UGC03580, UGC04305, UGC05414, UGC06786, UGC06818, UGC06930, UGC07151, UGC07524, UGC07690, UGC09133, UGC10310, UGC11557, UGCA281\n"
}
```

This decision was made by the lab without the author. He reviews it at promotion and may reverse it.
