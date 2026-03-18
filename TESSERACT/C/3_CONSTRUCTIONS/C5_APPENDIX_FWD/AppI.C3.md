<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.R3.md
-->

# AppI — Cloud Lens / Constructions

- `AppI.C3.a`: `CorridorProbabilityUpdater` — Updates corridor open probability after each test using Bayesian accumulation.
- `AppI.C3.b`: `TruthConfidenceComputer` — Computes truth confidence distribution from evidence set. Reports distribution, not point estimate.
- `AppI.C3.c`: `EvidenceSufficiencyEvaluator` — Evaluates evidence sufficiency score against declared threshold for each truth-tag level.
- `AppI.C3.d`: `CorridorRiskRouter` — Routes operations based on corridor risk. High-risk operations deferred or rerouted. Threshold checked before execution.
