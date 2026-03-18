<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.R3.md
-->

# InvV — Cloud Lens / Constructions

- `InvV.C3.a`: `ReplaySampler` — Selects k random replay steps, re-executes each, compares output against the replay log. Reports pass/fail count and computed confidence level. If any fail, falls back to full replay verification.
- `InvV.C3.b`: `CoverageMinimizer` — Computes the minimal capsule set covering all properties using set-cover algorithms. Identifies redundant capsules. Reports the non-redundant core and the list of releasable redundancies.
- `InvV.C3.c`: `IndependenceVerifier` — Tests pairwise independence of verification properties by checking for logical dependencies (if property A implies property B, they are not independent). Reports the dependency graph.
- `InvV.C3.d`: `ReleaseScheduler` — Computes the value/cost ratio for each capsule. Sorts in ascending order. Generates the release schedule. Verifies coverage is maintained after each release. Output: the optimal release sequence.
