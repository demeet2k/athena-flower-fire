# Capsule 294 — Board Operators and Mirror Skeleton

**Source**: 2026-03-18_6x6_higher_lenses.md
**Family**: 6x6_higher_lenses
**Lens**: S (Square/Structure)

The visible 6x6 board is not the shell itself but a reversal-skeleton realization of the shell. The admissible board side is the anti-free mirror-skeleton family, with the visible chart slice promoted through: A = F_{P3}^{row}, B = F_{P1}^{row}, C = F_{P1}^{col}, D = F_{P3}^{col}, where P_1 = (12)(35)(46) and P_3 = (13)(24)(56). The board algebra is the admissible cube S_board isomorphic to (Z_2)^3 x Z_2^T.

The admissible mirror-board layer supports three anti-block flips and transpose duality. On the visible chart slice: Tau swaps A_s with B_s and D_s with C_s (total board-flip), while T swaps A_s with D_s and B_s with C_s (row/column duality). The 24-slot atlas factors as A_{24}^{chart} isomorphic to Z_2^{Tau} x Z_2^T (chart rectangle) x Z_6^H (shell torsion cycle).

For each fixed shell sector s, the chart rectangle is A_s <-> B_s (via Tau) and A_s <-> D_s (via T), creating a 2x2 navigation grid. For each fixed chart X, the shell cycle traces X through all six torsion steps.

## Key Objects
- Chart slice: A (P3-row), B (P1-row), C (P1-col), D (P3-col)
- Board operators: Tau (total flip), T (row/col duality)
- 24-slot atlas: Z_2 x Z_2 x Z_6

## Key Laws
- The board is a reversal-skeleton realization of the shell, not the shell itself
- Tau and T commute with shell operators
- The atlas factors cleanly into chart rectangle x shell torsion cycle

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_6x6_higher_lenses.md`
