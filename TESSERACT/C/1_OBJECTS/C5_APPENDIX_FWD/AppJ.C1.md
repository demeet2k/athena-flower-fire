<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppJ.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppJ.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppJ.R1.md
-->

# AppJ — Cloud Lens / Objects

- `AppJ.C1.a`: `ResidualDistribution` — The probability distribution `P(δ)` of residual magnitudes across the crystal, typically following a truncated exponential `P(δ) ∝ e^{-λδ}` for `δ ∈ [0, δ_max]`, characterizing the organism's overall approximation quality.
- `AppJ.C1.b`: `ConvergenceRateEstimator` — The statistical estimator `η̂` for the true convergence rate `η` from `NEAR-OK` to `OK`, computed from observed transition times using maximum likelihood on the geometric distribution `P(T=t) = η(1-η)^{t-1}`.
- `AppJ.C1.c`: `ResidualHealthScore` — The aggregate health metric `H = 1 - E[δ]/δ_max` summarizing the crystal's residual state as a single number in `[0,1]`, where `H = 1` means all results are exact and `H = 0` means all results are at maximum allowed deviation.
- `AppJ.C1.d`: `NearToOKTransitionMatrix` — The Markov transition matrix `M[i,j]` giving the probability of transitioning from residual state `i ∈ {NEAR-OK, NEAR-FAIL, NEAR-AMBIG}` to state `j ∈ {OK, NEAR-OK, NEAR-FAIL, NEAR-AMBIG, FAIL}` in one refinement cycle.
