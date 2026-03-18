<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.C3.md
-->

# AppI — Fractal Lens / Constructions

- `AppI.R3.a`: `RecursiveCorridorTester` — Tests corridor admissibility at each recursion depth. Reports per-depth status and consistency across depths.
- `AppI.R3.b`: `FractalTruthChecker` — Checks truth-tag consistency across recursion depths. Reports contradictions.
- `AppI.R3.c`: `RecursiveEvidenceAggregator` — Aggregates evidence from depth n into depth n+1 inputs. Requires depth-n certification before propagation.
- `AppI.R3.d`: `CorridorScaleBridgeBuilder` — Constructs the ScaleBridge between corridor admissibility at two scales using φ-scaling of thresholds.
