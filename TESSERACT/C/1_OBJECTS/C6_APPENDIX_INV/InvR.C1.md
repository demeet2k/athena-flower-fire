<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvR.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvR.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvR.R1.md
-->

# InvR — Cloud Lens / Objects

- `InvR.C1.a`: `TruthProbabilityCollapse` — Each corridor's truth condition has an estimated probability P(true). Compression commits to the maximum-likelihood value: if P(true) > 0.5, the corridor is evaluated as true; if P(true) < 0.5, as false. If P(true) ≈ 0.5, the evidence is insufficient and the corridor is evaluated by convention.
- `InvR.C1.b`: `CorridorCorrelationExclusion` — The joint probability of multiple corridors being open is computed by inclusion-exclusion over their correlations. This determines which corridor groups can be evaluated independently and which must be evaluated jointly.
- `InvR.C1.c`: `IndependentCorridorProduct` — For independent corridors, P(all open) = Π P(corridor_i open). The product gives the overall admissibility probability, which governs the seed's expected truth density.
- `InvR.C1.d`: `TruthInformationDensity` — The information content of each truth value: -log₂(P(value)). Rare truths (low probability) carry more information. The total information = Σ(-log₂(P_i)) = the truth lattice's entropy. Compression preserves information-dense truths first.
