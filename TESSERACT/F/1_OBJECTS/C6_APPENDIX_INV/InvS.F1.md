<!-- TESSERACT: F/1_OBJECTS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=F facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvS.S1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvS.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvS.R1.md
-->

# InvS — Flower Lens / Objects

- `InvS.F1.a`: `ResidualWaveDamping` — Residuals distributed across the lattice form a wave pattern (some cells positive, some negative). Absorption damps this wave to zero amplitude. The damping is smooth: no cell's residual changes sign abruptly.
- `InvS.F1.b`: `ApproximationRefinementCurve` — Each NEAR value's approximation improves along a refinement curve: the difference between approximate and exact decreases with each refinement step. The curve is monotonically decreasing and asymptotically approaches zero.
- `InvS.F1.c`: `ResidualFluxBalance` — Residuals flow between cells like a conserved fluid. The flux into any cell minus the flux out = the change in that cell's residual. At equilibrium (compression complete), all fluxes are zero.
- `InvS.F1.d`: `PrecisionConvergence` — The precision of each value converges to its full-precision limit as truncations are restored. The convergence follows a series: each restoration adds bits of precision, like partial sums approaching the full value.
