<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppP.C3.md
-->

# AppP — Fractal Lens / Constructions

- `AppP.R3.a`: `BootstrapSequencer` — Takes a deployment genome, parses it, generates server profiles for each element, provisions infrastructure, deploys servers in dependency order, and runs post-deployment health checks.
- `AppP.R3.b`: `AutoScaler` — Monitors the resonance vector and per-element load metrics, evaluates scaling rules from the auto-scaling policy, and issues scale-up or scale-down commands with cooldown enforcement.
- `AppP.R3.c`: `RemediationEngine` — Maintains a library of remediation procedures (restart, cache flush, shard reindex, thread pool reset) and selects the appropriate one based on the detected degradation pattern.
- `AppP.R3.d`: `GenomeEvolver` — Compares the current deployment state against the genome, identifies drift (manual changes, unplanned scaling), and either reconciles the deployment to match the genome or updates the genome to reflect intentional changes.
