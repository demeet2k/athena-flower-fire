<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.C3.md
-->

# AppH — Fractal Lens / Constructions

- `AppH.R3.a`: `RecursiveCouplingBuilder` — Constructs coupling graphs at multiple scales with consistency checks between levels.
- `AppH.R3.b`: `ScaleCouplingDecayComputer` — Computes coupling strength at each scale using 1/φ decay factor. Reports scale-dependent bond maps.
- `AppH.R3.c`: `TopologicalSelfSimilarityChecker` — Verifies coupling graph isomorphism across scales. Reports breaks.
- `AppH.R3.d`: `RecursiveCascadeBoundVerifier` — Verifies that recursive failure cascades are bounded. Reports worst-case cascade depth and breadth.
