<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.R3.md
-->

# InvP — Cloud Lens / Constructions

- `InvP.C3.a`: `ConsensusTracker` — Computes P(consensus) at each step. Reports the consensus curve. Identifies the step where the threshold is crossed.
- `InvP.C3.b`: `DisagreementEstimator` — Applies inclusion-exclusion to estimate P(any_disagree). Reports the disagreement trend. Flags persistent disagreements.
- `InvP.C3.c`: `CorrelationMonitor` — Computes pairwise agent correlations at each step. Verifies monotonic increase. Reports the correlation matrix trend.
- `InvP.C3.d`: `WeightCalibrator` — Assesses each agent's evidence quality. Computes normalized weights. Verifies fairness. Reports the weighted convergence point.
