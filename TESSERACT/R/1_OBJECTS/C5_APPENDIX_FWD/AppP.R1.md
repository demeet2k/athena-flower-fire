<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppP.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppP.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppP.C1.md
-->

# AppP — Fractal Lens / Objects

- `AppP.R1.a`: `SelfConfiguringServer` — A server that reads its own SFCR element assignment from the deployment manifest, auto-generates its server profile, configures its resource limits, and begins serving without manual setup.
- `AppP.R1.b`: `AutoScalingPolicy` — A policy object embedded in the deployment manifest that specifies scaling rules: metric thresholds for scale-up/scale-down, cooldown periods, and minimum/maximum instance counts per element.
- `AppP.R1.c`: `SelfHealingWatchdog` — A local agent on each server that detects degraded states (memory leaks, stuck threads, shard corruption), attempts automated remediation, and escalates to failover only if self-healing fails.
- `AppP.R1.d`: `DeploymentGenome` — A compact, self-describing specification from which an entire deployment can be bootstrapped: it encodes all server profiles, scaling policies, health checks, and monitoring configurations in a single artifact.
