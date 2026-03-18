<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.R3.md
-->

# InvM — Cloud Lens / Constructions

- `InvM.C3.a`: `DeadProbabilityEstimator` — Estimates P(dead) for each entry using reference frequency analysis. Ranks by descending probability. Outputs the pruning priority order.
- `InvM.C3.b`: `RedundancyAnalyzer` — Computes mutual information between each attribute pair. Identifies redundant attributes (high MI with retained attributes). Reports the dependency structure.
- `InvM.C3.c`: `IndependenceChecker` — Tests entry independence using cross-reference analysis. Reports the dependency graph. Authorizes parallel pruning for independent clusters.
- `InvM.C3.d`: `FalsePositiveMonitor` — Tracks any instances where a pruned entry was later referenced (false positive). Reports the running false positive rate. Adjusts pruning aggressiveness if rate approaches tolerance.
