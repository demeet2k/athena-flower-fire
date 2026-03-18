<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.R3.md
-->

# AppP — Cloud Lens / Constructions

- `AppP.C3.a`: `DashboardBuilder` — Reads the deployment manifest, discovers all element servers, subscribes to their telemetry streams, and constructs a per-element panel with standard metric visualizations.
- `AppP.C3.b`: `ResonanceVectorComputer` — Polls each element server's health and load metrics, normalizes them to `[0, 1]`, assembles the 8D vector, and publishes it to the telemetry dashboard at configurable intervals.
- `AppP.C3.c`: `BaselineProfiler` — Collects metric values over a configurable baseline window, fits a Gaussian or non-parametric distribution to each metric, and stores the baseline parameters for the anomaly detector.
- `AppP.C3.d`: `IncidentCorrelator` — When the anomaly detector fires, queries all other element servers' metrics in the same time window, runs pairwise correlation tests, and groups co-occurring anomalies into incident clusters.
