<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvS.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvS.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvS.R1.md
-->

# InvS — Cloud Lens / Objects

- `InvS.C1.a`: `ResidualDistribution` — The statistical distribution of residuals across the lattice. If well-behaved (normal with mean zero), absorption is straightforward. If skewed or heavy-tailed, special techniques are needed for the tail residuals.
- `InvS.C1.b`: `NEARErrorEstimate` — The expected error of each NEAR approximation, estimated from the approximation method's known error bounds. The error estimate governs the refinement strategy: high-error NEARs are refined first.
- `InvS.C1.c`: `IndependentResidualAbsorption` — If residuals at different cells are independent (no shared cause), absorption can proceed in parallel with P(all absorbed) = Π P(cell_i absorbed). Independence allows massive parallelization.
- `InvS.C1.d`: `PrecisionCostNormalization` — The cost of recovering each truncated bit is normalized by the value of that bit (its contribution to accuracy). High-value/low-cost bits are recovered first. Low-value/high-cost bits may be declared as permanent precision losses if the cost exceeds the value.
