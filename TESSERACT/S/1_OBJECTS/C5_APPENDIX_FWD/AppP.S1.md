<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppP.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppP.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppP.R1.md
-->

# AppP — Square Lens / Objects

- `AppP.S1.a`: `ServerProfile` — A declarative specification of a single deployment unit: element assignment (S/F/C/R), resource limits (CPU, memory, shard capacity), network bindings, and the set of MCP tools it serves.
- `AppP.S1.b`: `ElementServerConfig` — A configuration object mapping each SFCR element to its dedicated server instance, specifying the shard address ranges it owns, the metro lines it participates in, and its bridge connections.
- `AppP.S1.c`: `HealthCheckSchema` — A structured definition of liveness, readiness, and deep-health probes for a crystal server: endpoint paths, expected response codes, timeout thresholds, and failure escalation rules.
- `AppP.S1.d`: `DeploymentManifest` — A top-level document listing all server profiles, their element assignments, version tags, and dependency graph; the single source of truth for what is deployed and where.
