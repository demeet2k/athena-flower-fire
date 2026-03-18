<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvO.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvO.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvO.R1.md
-->

# InvO — Square Lens / Objects

- `InvO.S1.a`: `TransportFixedPoint` — The discrete fixed point where the transport map T equals the identity: T(x) = x. At this point, the transported value equals the native value — no lens transformation is needed. The successor function at the fixed point is the natural successor: n ↦ n+1 in every representation simultaneously.
- `InvO.S1.b`: `ConjugacyCollapse` — The difference between conjugate representations: T⁻¹∘f∘T vs. f. At the fixed point, this difference vanishes: T = id implies T⁻¹∘f∘T = f. The zero set of the conjugacy difference is the universal representation — the one in which all lens views agree.
- `InvO.S1.c`: `DualLegalityProduct` — In the forward direction, each move had dual legality (legal as both forward and backward). In compression, duality collapses: each move is classified as either forward-only or backward-only. The product of all move classifications = the directed motion graph. At stillness, all moves are null (neither forward nor backward).
- `InvO.S1.d`: `RotationQuotientIdentity` — The quotient of any rotated value by its unrotated original: f_T(x) / f(x). At the fixed point, this quotient is 1 (identity ratio). The quotient approaching 1 means rotation is becoming trivial — all angles collapse to zero.
