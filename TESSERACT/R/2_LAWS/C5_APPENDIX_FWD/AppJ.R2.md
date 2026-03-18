<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppJ.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppJ.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppJ.C2.md
-->

# AppJ — Fractal Lens / Laws

- `AppJ.R2.a`: `ContractionMappingLaw` — The correction function `f` must be a contraction: `|f(x) - f(y)| ≤ κ|x - y|` with `κ < 1`. This guarantees convergence by Banach's fixed-point theorem and bounds the convergence rate by `δ_n ≤ κ^n δ_0`.
- `AppJ.R2.b`: `FixedPointUniquenessLaw` — The contraction mapping has a unique fixed point `x*` in the crystal's metric space. Multiple fixed points would create ambiguity about which exact answer to converge toward; uniqueness ensures deterministic refinement.
- `AppJ.R2.c`: `MultiscaleConsistencyLaw` — Corrections at coarse level `L_i` must be consistent with fine level `L_{i+1}`: the restriction of `L_{i+1}`'s correction to `L_i`'s scale must equal `L_i`'s correction. No scale introduces contradictory corrections.
- `AppJ.R2.d`: `SelfCorrectionTerminationLaw` — Every self-correcting residual must terminate: the embedded repair function satisfies the contraction law with `κ < 1`, guaranteeing `δ < ε_target` within `⌈log(δ_0/ε_target) / log(1/κ)⌉` iterations.
