<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.R3.md
-->

# AppI — Flower Lens / Constructions

- `AppI.F3.a`: `CorridorFlowRouter` — Routes operations through open corridors. Detects closed corridors and redirects flow to alternatives.
- `AppI.F3.b`: `TruthWavePropagator` — Propagates truth promotions through the system with bounded depth. Tracks which promotions triggered which downstream promotions.
- `AppI.F3.c`: `AdmissibilityGradientComputer` — Computes how close each operation is to its corridor boundary. Flags sensitive operations.
- `AppI.F3.d`: `ShadowCorridorRotator` — When a corridor closes, rotates the operation to a shadow/renormalized corridor where it can be executed lawfully. The ÷-seed's singularity resolution.
