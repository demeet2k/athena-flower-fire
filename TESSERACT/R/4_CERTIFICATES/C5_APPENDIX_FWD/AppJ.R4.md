<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.C4.md
-->

# AppJ — Fractal Lens / Certificates

- `AppJ.R4.a`: `ContractionCert` — Receipt proving the correction function satisfies the contraction condition `κ < 1`, the convergence bound `δ_n ≤ κ^n δ_0` was verified for the first `k` iterations, and the fixed point was reached within budget.
- `AppJ.R4.b`: `FixedPointCert` — Receipt proving the candidate fixed point satisfies `|f(x*) - x*| < ε`, the uniqueness condition holds in the declared neighborhood, and the residual was promoted from `NEAR-OK` to `OK`.
- `AppJ.R4.c`: `MultigridConsistencyCert` — Receipt proving the V-cycle corrections are consistent across all scale levels, the coarse-grid solution is correct, and the interpolated fine-grid correction achieves the target residual reduction.
- `AppJ.R4.d`: `SelfRepairCert` — Receipt proving the self-correcting residual's embedded repair function is a valid contraction, the termination bound is finite, and the repair function was derived correctly from the local Jacobian.
