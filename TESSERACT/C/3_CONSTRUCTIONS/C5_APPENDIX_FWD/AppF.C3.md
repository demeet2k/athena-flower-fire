<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.R3.md
-->

# AppF — Cloud Lens / Constructions

- `AppF.C3.a`: `ConfidenceUpdater` — Updates transport confidence field after each successful or failed chart transport, using Bayesian accumulation.
- `AppF.C3.b`: `OptimalChartSelector` — Selects the lens chart that minimizes transported complexity for a given seed×element×level cell.
- `AppF.C3.c`: `RiskAssessor` — Evaluates corridor risk before transport attempt; triggers shadow resolution when risk exceeds threshold.
- `AppF.C3.d`: `DualRouteBalancer` — Monitors forward/backward route balance; flags asymmetric pairs for structural investigation.
