<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.R3.md
-->

# InvX — Cloud Lens / Constructions

- `InvX.C3.a`: `IntegritySampler` — Randomly selects a sample of shards from the bundle, verifies each, and computes the sample corruption rate. If rate exceeds threshold, triggers full verification. Reports confidence level and sample size.
- `InvX.C3.b`: `CorruptionEstimator` — Applies inclusion-exclusion to estimate total corruption probability from known sources. Outputs the corruption bound and the dominant source.
- `InvX.C3.c`: `ParallelAbsorber` — After independence verification, absorbs independent shards in parallel. Merges results. Falls back to sequential for dependent shards. Reports parallelism achieved and any fallback events.
- `InvX.C3.d`: `SourceTrustUpdater` — Updates the historical corruption rate for the import source based on the current absorption results. Adjusts the normalized risk ranking. Outputs the updated trust profile.
