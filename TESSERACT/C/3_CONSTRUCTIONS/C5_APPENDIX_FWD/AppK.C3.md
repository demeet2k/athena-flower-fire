<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.R3.md
-->

# AppK — Cloud Lens / Constructions

- `AppK.C3.a`: `ConflictRiskEstimator` — The engine that computes the conflict probability field by combining historical conflict rates, dependency graph centrality measures, and current residual levels (from AppJ) into a per-address risk score.
- `AppK.C3.b`: `EvidenceWeighter` — The engine that assigns reliability weights to evidence items based on source credibility, temporal recency, and consistency with other evidence, normalizing to sum to 1.
- `AppK.C3.c`: `BayesianUpdater` — The sequential Bayesian updater that processes evidence items one at a time, maintaining the posterior probability of each resolution outcome, and declaring resolution when the posterior exceeds the decision threshold `τ`.
- `AppK.C3.d`: `QuorumAssembler` — The construction that selects `k` independent verifiers (shards not in the conflict's dependency cone), distributes the conflict evidence to each, collects votes, and computes the majority decision with confidence intervals.
