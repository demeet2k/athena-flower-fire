<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.R3.md
-->

# InvS — Square Lens / Constructions

- `InvS.S3.a`: `GlobalResidualScanner` — Scans the entire lattice, computing the residual at each cell. Aggregates into the total residual. Reports cells with largest residuals (hotspots) for priority absorption.
- `InvS.S3.b`: `NEARResolver` — For each NEAR value: computes the exact target using higher-precision arithmetic, compares against the NEAR approximation, and either promotes to exact (if within tolerance) or flags for refinement (if outside tolerance).
- `InvS.S3.c`: `CapacityBasedRedistributor` — For each unabsorbable local residual: surveys neighboring cells' capacities, computes shares proportional to capacity, distributes shares, and verifies conservation (total distributed = original).
- `InvS.S3.d`: `TruncationRestorer` — For each truncated operation: retrieves the full-precision result (recomputing if necessary), computes the truncated portion, and reintegrates it. Reports the truncation quotient before and after restoration.
