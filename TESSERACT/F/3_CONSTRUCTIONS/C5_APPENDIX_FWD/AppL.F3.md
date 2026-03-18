<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.R3.md
-->

# AppL — Flower Lens / Constructions

- `AppL.F3.a`: `SearchWaveLauncher` — The construction that initializes an evidence search wave at the ambiguous result's address, computes the initial propagation direction based on the dependency graph, and dispatches query packets to the first shell of neighbors.
- `AppL.F3.b`: `HypothesisTestEngine` — The engine that executes hypothesis test cycles: generates predictions from each candidate, collects observations, computes likelihoods `P(o | c_i)`, and updates candidate weights via Bayesian multiplication and renormalization.
- `AppL.F3.c`: `ScheduleOptimizer` — The optimizer that takes the raw evidence plan and dependency constraints, applies topological sort with earliest-deadline-first scheduling, and produces a time-ordered gathering schedule with minimum expected completion time.
- `AppL.F3.d`: `CascadeExecutor` — The engine that manages promotion cascades: when a candidate is promoted, scans downstream dependencies for newly resolvable ambiguities, triggers their promotion, and tracks the cascade depth against the termination bound.
