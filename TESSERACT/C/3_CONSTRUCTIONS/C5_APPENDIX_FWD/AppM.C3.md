<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.R3.md
-->

# AppM — Cloud Lens / Constructions

- `AppM.C3.a`: `AdaptiveSamplingVerifier` — Begins with a coarse random sample of ticks, then refines by oversampling regions where state entropy is highest or where adjacent samples showed hash instability.
- `AppM.C3.b`: `DistributedReplayAudit` — Distributes replay verification across `k` independent nodes, each sampling different tick subsets; results are aggregated via majority vote to produce a consensus verification verdict.
- `AppM.C3.c`: `EntropyWeightedCheckpointer` — Measures state entropy at each tick in a sliding window and emits checkpoints when entropy exceeds a dynamic threshold, producing denser checkpoints in complex computation phases.
- `AppM.C3.d`: `SequentialConfidenceAccumulator` — Runs sampled verifications one at a time, updating a Bayesian posterior on replay correctness after each; halts early when confidence exceeds `1 - delta` or corruption is confirmed.
