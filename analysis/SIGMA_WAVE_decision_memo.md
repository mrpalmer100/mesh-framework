# SIGMA_WAVE DECISION MEMO (COMPOSITE-SELECT Leg D; the desk, 2026-10-19)

The question the charter puts on the desk (QC): with QA and QB in hand, what is Sigma_wave at its honest size,
and what happens to Prediction 32's upper edge and to the kb ceiling downstream. The decision is the author's.
This memo prices the two options with the sealed numbers and says what each commits the registry to. No grant is
made here.

## 1. Where the numbers stand

| | Sigma_wave (T0 per strand per axial length) | P32 share 1 - T0 / Sigma_wave | source |
|---|---|---|---|
| Level-1-exact (the retreat) | 2.598 | 0.6151, the exact lower edge | FND-132 (level 1 at c); FND-169's grant |
| Deepest gated member, cell 13/9, 432 x 36, A2 0.00520 (the hold) | 2.6069 | 0.6164 | Leg B, QC row (ii) |
| The same at 432 x 54, A2 0.00516 | 2.6067 | 0.6164 | Leg B, QC row (ii) |
| Reachable-family range, all nine cells | 2.598 to 2.609 | 0.6151 to 0.6167 | Leg A S-b (4/3, 5/3, 5/4) and Leg B |
| The ansatz bracket, superseded | [3.222, 4.313] | [0.690, 0.768] | FND-135 (the ansatz's, not the state's; retired by FND-169) |
| Prediction 32 as the paper printed it | | [0.615, 0.779] | the two-sided band, upper edge "closing with the composite build" |

What QA and QB settled:
- QA (FND-169, COMP-PIN-UNREACHABLE): no registered principle selects a level-2 amplitude the family reaches; the
  only principle that selects at all (level-2 Lorentz saturation) points an order of magnitude beyond A2_max. There
  is no A2* to price; row (i) is empty by verdict, not by omission.
- QB (Leg B, RAT-RESONANT): the collapse that bounds A2_max in the low-order cells is an artifact of the
  rationalized instrument. The high-order cells do not collapse through the window; their A2_max (0.0052) is the
  protocol's budget, not a fold. So the "deepest gated member" in row (ii) is deep because the march stopped, and
  its price is the price of wherever the march stopped.

## 2. The two options, priced

HOLD at the deepest reachable member. Sigma_wave = 2.6069 T0 (NP 36; 2.6067 at 54), P32 upper edge 0.6164, band
[0.615, 0.616]. Commits the registry to a number that is the budget's, not the state's: the march at 13/9 was flat
when it stopped (D 1.04x), so a longer march under the same protocol would reach a larger A2 and a larger price,
by Leg A's slope (dSigma/dA2 of +1.9 to +11.4) about +0.001 to +0.006 T0 per 0.001 in A2. The number would carry a
rider that it moves with the budget. The band's width would be 0.001, which is to say the upper edge would be a
decoration on the lower edge.

RETREAT to the level-1-exact value (granted 2026-09-05). Sigma_wave = 2.598 T0, P32 lower edge 0.6151 exact, with
the rider: the reachable two-frequency family prices at 2.598 to 2.609 T0 (nine cells, two densities), the level-2
contribution at reachable amplitudes is +0.3 percent, and the state's own selected amplitude is unreached
(FND-169). Commits the registry to a number that is forced (level 1 at c, FND-132) and to a rider that says how far
the reachable family departs from it. Prediction 32 becomes a one-sided statement: the share is at least 0.615,
with the upper edge unpriced until a state exists at a selected amplitude.

The difference between the options is 0.0089 T0 in Sigma_wave and 0.0013 in the share. Neither option moves the
kb ceiling: FND-141's chain (kb <= 0.09332 T0_f a_f^2) takes Sigma_wave through the level-1 sector that both
options share; the +0.3 percent of level 2 at reachable amplitudes is inside the chain's own display tolerance,
and the ceiling is left to the desk as the charter says.

## 3. What the memo recommends, and why

The retreat, as granted, with its rider's range updated from Leg A's three cells (2.598 to 2.609) to Leg B's nine
(the same range; the new cells add no larger member). The reasons are the charter's own:
1. The hold prices a budget. Leg B showed the high-order cells are flat where the march stops, so the deepest
   member is not a feature of the state and its price is not a property of anything.
2. The retreat prices an identity. Level 1 at c is forced and reproduces the exact lower edge 0.615; it is the
   number the registry can defend without a rider on its face.
3. The two are 0.3 percent apart. A decision between them is not a decision about a quantity; it is a decision
   about what kind of number the registry carries, and the house rule favours the forced one.

What the retreat does NOT settle, and the rider should say: the state's level-2 amplitude is unselected (QA) and
its collapse-bound A2_max was an artifact (QB), so Prediction 32's upper edge is open, not closed; the honest
sentence in the paper is "lower edge 0.615 exact; the upper edge waits on a selection principle for the level-2
amplitude, none of the three registered ones selecting a reachable value (FND-169), and on an anti-aliased
instrument for the quasi-periodic state (Leg B)".

## 4. Downstream, for the author to carry or not

- Paper sync: the predictions paper's Prediction 32 entry (two-sided band [0.615, 0.779]) to a lower edge with the
  rider; FND-169's grant already asked for this, and Leg B changes nothing in it.
- The CELL-SCOPE riders on FND-147/151/152/153/163 (Leg B's QB consequence (a)): one sentence each, on the
  author's word, by lab claim-edit or by hand.
- The next instrument: the anti-aliased continuum of the two-frequency state (QB consequence (c)). A charter for
  it would ask the question QB answered only for rational cells, on an instrument that has no cell: whether the
  aligned family grows, saturates, or collapses as a function of amplitude alone. It is the natural successor and
  the only route to a priced upper edge; it is not drafted here.
- The level-2 frequency: om2 = 6.28 (q - 1) + 0.13 on the six new cells (recorded, not formed, Leg B results
  section 7). If the slope is 2 pi to the precision a dedicated run can give, that is a derivation question for
  the lab's theorist (a derivation commission on what fixes om2); if it is not, it is a fit. Either way it is a
  charter, not a rider.
