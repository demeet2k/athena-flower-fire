<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppP.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppP.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppP.R1.md
-->

# AppP — Flower Lens / Objects

- `AppP.F1.a`: `RollingUpdateController` — An orchestrator that replaces server instances one at a time, waiting for each new instance to pass health checks before proceeding to the next, ensuring zero-downtime deployment.
- `AppP.F1.b`: `BlueGreenSwitch` — A traffic router that maintains two complete deployment environments (blue and green); new versions deploy to the inactive environment, and a single atomic switch redirects all traffic.
- `AppP.F1.c`: `GracefulFailoverAgent` — A watchdog that monitors primary server health and, upon detecting sustained failure, redirects traffic to a standby replica while preserving in-flight request continuity.
- `AppP.F1.d`: `CanaryDeploymentProbe` — A deployment strategy that routes a small percentage of traffic to a new server version, monitors error rates and latency, and promotes or rolls back based on configurable thresholds.
