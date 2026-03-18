<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppM.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppM.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppM.R1.md
-->

# AppM — Cloud Lens / Objects

- `AppM.C1.a`: `ReplaySamplingOracle` — A probabilistic verifier that checks replay correctness by sampling `m` random ticks, replaying short windows around each, and comparing against recorded hashes; catches corruption with probability `1 - (1-p)^m`.
- `AppM.C1.b`: `StatisticalDivergenceDetector` — Computes the KL-divergence between the distribution of state hashes in a replay and the distribution in the original execution; significant divergence signals non-determinism or corruption.
- `AppM.C1.c`: `ProbabilisticCheckpointSelector` — Selects which ticks to checkpoint using a probability distribution weighted by state entropy and transition complexity, optimizing the tradeoff between storage cost and replay granularity.
- `AppM.C1.d`: `ReplayConfidenceEstimator` — Computes a confidence interval `[1 - epsilon, 1]` for replay correctness based on the fraction of sampled ticks that pass verification, using Hoeffding bounds.
