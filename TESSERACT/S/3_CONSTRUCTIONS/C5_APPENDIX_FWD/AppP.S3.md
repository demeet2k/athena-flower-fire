<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.R3.md
-->

# AppP — Square Lens / Constructions

- `AppP.S3.a`: `ProfileGenerator` — Takes an SFCR element specification and resource budget, generates a server profile with appropriate defaults, and validates it against the profile completeness schema.
- `AppP.S3.b`: `ConfigDistributor` — Reads the deployment manifest, extracts each element server's configuration, and pushes it to the target server's configuration endpoint with version verification.
- `AppP.S3.c`: `HealthCheckRunner` — Executes all probes defined in a server's health check schema at configurable intervals, records results in a time-series store, and triggers alerts when failure thresholds are breached.
- `AppP.S3.d`: `ManifestValidator` — Parses a deployment manifest, checks all profiles for completeness, verifies no shard address overlaps exist, confirms health check presence, and emits a validation report.
