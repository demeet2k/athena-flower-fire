<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.R3.md
-->

# InvT — Cloud Lens / Constructions

- `InvT.C3.a`: `SuccessProbabilityEstimator` — Estimates P(success) from historical data + current conflict characteristics using Bayesian estimation. Outputs the posterior probability and confidence interval.
- `InvT.C3.b`: `RecurrenceEstimator` — Computes P(recurrence) via inclusion-exclusion over known causes. Determines the required monitoring window. Sets up the monitoring schedule.
- `InvT.C3.c`: `DependencyAnalyzer` — Checks for shared conflict causes among quarantined entities. Reports the dependency graph. Authorizes parallel healing for independent clusters and joint healing for dependent clusters.
- `InvT.C3.d`: `RiskBudgetManager` — Tracks the remaining risk budget. Authorizes reintegration in order of ascending normalized risk (safest first). Reports budget utilization and remaining capacity.
