<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvR.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvR.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvR.C1.md
-->

# InvR — Fractal Lens / Objects

- `InvR.R1.a`: `RecursiveTruthEvaluation` — Truth conditions may reference other truth conditions (nested conditionals). Evaluation is recursive: evaluate the innermost conditions first, substitute results, then evaluate outer conditions. The recursion terminates at atomic propositions.
- `InvR.R1.b`: `TruthDepthContraction` — Each evaluation level resolves one level of nesting, contracting the truth depth by 1. The contraction drives the conditional depth from its maximum to zero (all conditions flat).
- `InvR.R1.c`: `CorridorTreeCollapse` — The corridor hierarchy (meta-corridors governing sub-corridors) collapses from leaves to root. Leaf corridors are sealed first; their results determine which parent corridors open or close.
- `InvR.R1.d`: `ScaleInvariantTruthProtocol` — The truth evaluation protocol is the same at every nesting level: evaluate condition, commit value, seal corridor. The protocol is a fixed point of the nesting structure.
