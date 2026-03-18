<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppJ.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppJ.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppJ.C1.md
-->

# AppJ — Fractal Lens / Objects

- `AppJ.R1.a`: `IterativeRefiner` — The recursive engine `R(x_0) = lim_{n→∞} f^n(x_0)` that takes a `NEAR-OK` result `x_0` and iteratively applies correction function `f` until `δ(x_n) < ε_target` or the iteration budget `N_max` is exhausted.
- `AppJ.R1.b`: `ResidualFixedPoint` — The fixed point `x* = f(x*)` of the correction function, representing the exact answer that the iterative refiner converges toward. When `δ(x*) = 0`, the residual is fully resolved; the `NEAR` tag is promoted to `OK`.
- `AppJ.R1.c`: `MultiScaleRefinementLadder` — A nested sequence of refinement levels `L_0 ⊂ L_1 ⊂ ... ⊂ L_k` where each level `L_i` resolves residuals at scale `2^{-i}`, and the correction at level `i` feeds the initial condition for level `i+1`, forming a multigrid V-cycle.
- `AppJ.R1.d`: `SelfCorrectingResidual` — A residual that contains its own correction procedure as metadata: the `NEAR-OK` envelope includes a function `repair: δ → δ'` such that repeated application `repair^n(δ) → 0`. The residual carries its own cure.
