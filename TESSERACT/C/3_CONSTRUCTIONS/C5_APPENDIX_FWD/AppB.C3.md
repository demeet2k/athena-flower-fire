<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.R3.md
-->

# AppB — Cloud Lens / Constructions

- `AppB.C3.a`: `BudgetAllocator` — The optimization engine that solves the water-filling allocation problem: given observed violation distributions `P(Δ_i)` for all six laws, computes the optimal budget partition `{ε_1,...,ε_6}` minimizing expected total violations subject to `Σ ε_i = E_total`.
- `AppB.C3.b`: `ThresholdCalibrator` — The calibrator that sets `τ_i` for each law based on the empirical distribution `P(Δ_i)`, targeting a false-positive rate of `α` (accepting deviations that are actually legal) and false-negative rate of `β` (missing true violations).
- `AppB.C3.c`: `ViolationDriftDetector` — The sequential hypothesis tester that monitors the running mean of `Δ_i` for each law, triggering an alarm when the CUSUM statistic exceeds a threshold indicating systematic drift toward violation.
- `AppB.C3.d`: `BudgetTransferEngine` — The engine that executes inter-law budget transfers according to the allocation matrix `B`, verifying zero-sum conservation, checking that no law's budget drops below a minimum floor `ε_min`, and logging each transfer.
