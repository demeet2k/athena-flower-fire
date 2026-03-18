<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.R3.md
-->

# AppJ — Cloud Lens / Constructions

- `AppJ.C3.a`: `DistributionFitter` — The statistical engine that fits the residual distribution `P(δ)` to observed data using maximum likelihood estimation, selecting between exponential, Pareto, and log-normal models by AIC comparison.
- `AppJ.C3.b`: `ConvergenceRateTracker` — The online estimator that maintains a running MLE of the convergence rate `η̂` from observed `NEAR-OK → OK` transition times, with confidence intervals and trend detection for rate changes.
- `AppJ.C3.c`: `HealthDashboard` — The monitoring construction that computes the aggregate health score `H`, decomposes it by shell, archetype, and metro line, and generates alerts when any sub-population's health drops below threshold.
- `AppJ.C3.d`: `TransitionMatrixEstimator` — The estimator that builds the empirical transition matrix `M̂` from observed state transitions, tests for ergodicity by checking that the matrix's second-largest eigenvalue `|λ_2| < 1`, and computes the stationary distribution.
