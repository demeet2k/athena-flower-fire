<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.R4.md
-->

# AppJ — Cloud Lens / Certificates

- `AppJ.C4.a`: `DistributionFitCert` — Receipt proving the residual distribution was fit to observed data, the selected model is the best by AIC, and the fitted parameters are within confidence bounds.
- `AppJ.C4.b`: `ConvergenceRateCert` — Receipt proving the convergence rate estimate `η̂` is positive, the confidence interval excludes zero, and the estimation used at least `N_min` observed transitions.
- `AppJ.C4.c`: `HealthScoreCert` — Receipt proving the aggregate health score was computed correctly, the decomposition by sub-population is consistent with the aggregate, and all sub-populations are above minimum threshold.
- `AppJ.C4.d`: `ErgodicityVerificationCert` — Receipt proving the transition matrix is ergodic, `|λ_2| < 1`, the stationary distribution assigns positive probability to `OK`, and no absorbing non-terminal state exists.
