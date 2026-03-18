<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.R3.md
-->

# AppK — Flower Lens / Constructions

- `AppK.F3.a`: `AmplificationChainTracer` — The tracer that follows a conflict's causal chain through the dependency graph, recording each hop, measuring the amplification factor at each step, and triggering cutoff when chain length reaches `L_max`.
- `AppK.F3.b`: `CancellationDetector` — The detector that scans pairs of active conflicts for cancellation potential, computing the combined deviation `Δ_+ + Δ_-` and flagging pairs where the sum falls within tolerance `ε` of zero.
- `AppK.F3.c`: `QuarantineScheduler` — The scheduler that manages quarantine decay over time, computing `Q(t)` for each quarantined shard, adjusting access permissions as severity decreases, and triggering full release upon formal resolution.
- `AppK.F3.d`: `FirebreakConstructor` — The emergency construction that builds a quarantine perimeter at radius `R_max` from a conflict source, proactively isolating all shards on the perimeter to prevent wave front escape.
