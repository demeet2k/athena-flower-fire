<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppB.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppB.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppB.R1.md
-->

# AppB — Cloud Lens / Objects

- `AppB.C1.a`: `ErrorBudget` — A quantified tolerance `ε_i` for each conservation law `i`, specifying the maximum allowed deviation from exact conservation before a soft violation is declared. Budgets are drawn from a shared pool `E_total = Σ ε_i`.
- `AppB.C1.b`: `ToleranceThreshold` — The binary decision boundary `τ_i` for law `i`: deviations below `τ_i` are logged but accepted (NEAR-OK), deviations between `τ_i` and `ε_i` trigger warnings (NEAR-FAIL), and deviations above `ε_i` trigger hard violations.
- `AppB.C1.c`: `SoftViolationDistribution` — The statistical distribution `P(Δ_i)` of observed deviations for conservation law `i` across all recent transport paths, used to calibrate error budgets and detect systematic drift toward violation.
- `AppB.C1.d`: `BudgetAllocationMatrix` — The `6 × 6` matrix `B` allocating shared error budget across the six conservation laws, where `B[i,j]` specifies how much budget can be transferred from law `i` to law `j` when law `j` is under pressure.
