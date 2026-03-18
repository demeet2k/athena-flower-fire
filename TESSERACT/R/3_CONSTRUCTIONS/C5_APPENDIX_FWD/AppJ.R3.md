<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.C3.md
-->

# AppJ — Fractal Lens / Constructions

- `AppJ.R3.a`: `BanachIterator` — The fixed-point iterator implementing Banach's contraction principle: given `f` with Lipschitz constant `κ < 1` and initial `x_0`, computes `x_{n+1} = f(x_n)` with early termination when `|x_{n+1} - x_n| < ε(1-κ)/κ` guarantees `|x_n - x*| < ε`.
- `AppJ.R3.b`: `FixedPointVerifier` — The verifier that takes a candidate fixed point `x*` and confirms `f(x*) = x*` within machine precision, computing the residual `|f(x*) - x*|` and certifying it is below the declared tolerance.
- `AppJ.R3.c`: `MultigridVCycleEngine` — The V-cycle solver that descends from fine to coarse scales, solves the correction equation at the coarsest level, and interpolates corrections back up through each level, achieving `O(N)` total work for `N` total unknowns.
- `AppJ.R3.d`: `SelfRepairInjector` — The construction that takes a raw `NEAR-OK` result and attaches a self-repair function derived from the local Jacobian of the correction map, producing a `SelfCorrectingResidual` that carries its own convergence guarantee.
