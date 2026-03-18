<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.R3.md
-->

# AppP — Flower Lens / Constructions

- `AppP.F3.a`: `RollingUpdateExecutor` — Iterates through server instances in deployment order, drains each instance's traffic, deploys the new version, runs health checks, and re-enables traffic before moving to the next.
- `AppP.F3.b`: `BlueGreenProvisioner` — Provisions the inactive environment with the new version, runs the full health check suite, and prepares the traffic router's switch configuration; does not activate until explicitly triggered.
- `AppP.F3.c`: `FailoverOrchestrator` — Monitors primary health via the health check runner, detects sustained failures using a sliding window, initiates standby promotion, and reroutes traffic through the load balancer.
- `AppP.F3.d`: `CanaryAnalyzer` — Collects error rate, latency percentiles, and shard-resolution success rate from the canary instance, compares them against baseline metrics from the stable fleet, and emits a promote/rollback decision.
