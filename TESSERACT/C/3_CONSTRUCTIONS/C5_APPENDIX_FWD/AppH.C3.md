<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.R3.md
-->

# AppH — Cloud Lens / Constructions

- `AppH.C3.a`: `CouplingProbabilityEstimator` — Estimates bond formation probability from component compatibility, resources, and corridor status.
- `AppH.C3.b`: `FailurePropagationSimulator` — Simulates failure propagation through the dependency graph. Reports affected components and cascade depth.
- `AppH.C3.c`: `TopologicalHoleDetector` — Scans coupling graph for expected-but-absent bonds. Reports holes with severity and recommended fill actions.
- `AppH.C3.d`: `CouplingEntropyTracker` — Tracks coupling entropy over time. Reports trend and flags entropy increases.
