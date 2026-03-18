<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppJ.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppJ.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppJ.R2.md
-->

# AppJ — Cloud Lens / Laws

- `AppJ.C2.a`: `ResidualDistributionStability` — The residual distribution `P(δ)` is stationary under normal organism operation: the rate of new residual creation equals the rate of residual resolution, maintaining a steady-state distribution with finite mean and variance.
- `AppJ.C2.b`: `ConvergenceRatePositivityLaw` — The estimated convergence rate `η̂` must be strictly positive: `η̂ > η_min > 0`. A zero or negative convergence rate indicates systematic failure and triggers organism-level alarm via AppK conflict protocols.
- `AppJ.C2.c`: `HealthScoreMonotonicity` — Under active repair, the health score `H(t)` is non-decreasing in expectation: `E[H(t+1)] ≥ E[H(t)]`. Repair operations must, on average, improve the crystal's residual health.
- `AppJ.C2.d`: `TransitionMatrixErgodicity` — The `NEAR-to-OK` transition matrix `M` is ergodic: from any residual state, there is a positive probability path to `OK` within finite steps. No residual state is absorbing except `OK` and `FAIL`.
