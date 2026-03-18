<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvS.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvS.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvS.R1.md
-->

# InvS — Square Lens / Objects

- `InvS.S1.a`: `ResidualAccumulator` — The discrete sum of all outstanding residuals across the lattice. Each residual is a signed quantity representing the gap between the exact value and the lattice-representable approximation. The total residual = Σ(exact - approximate) across all cells. During compression, this total must be driven to zero.
- `InvS.S1.b`: `NEARDifferenceEliminator` — The difference between a NEAR value and its exact target. For each NEAR approximation, computes `Δ = exact - near`. If Δ is within the cell's tolerance, the NEAR is promoted to exact by absorbing the residual. If Δ exceeds tolerance, the cell must be refined.
- `InvS.S1.c`: `ResidualRedistributionProduct` — Residuals that cannot be absorbed locally may be redistributed across neighboring cells. The product of redistribution: each cell receives a share proportional to its capacity. The total redistributed = the original residual. Conservation is exact.
- `InvS.S1.d`: `TruncationQuotient` — The quotient of truncated precision by full precision = the truncation ratio. During expansion, operations were truncated for efficiency. During compression, the truncated portion is recovered and reintegrated. The quotient approaches 1 as all truncations are restored.
