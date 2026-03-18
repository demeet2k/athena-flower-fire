<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.R3.md
-->

# AppK — Square Lens / Constructions

- `AppK.S3.a`: `StructuralConsistencyScanner` — The full-crystal scanner that checks every shard against the type system, address uniqueness, conservation laws, and dependency acyclicity, emitting conflict packets for each detected inconsistency.
- `AppK.S3.b`: `QuarantineEnforcer` — The isolation engine that, upon receiving a conflict packet, immediately removes the affected shards from all routing tables, metro lines, and computation queues, replacing them with `QUARANTINED` sentinel values.
- `AppK.S3.c`: `ConflictClassifier` — The triage system that classifies conflicts by severity: `CRITICAL` (conservation violation, address collision), `MAJOR` (type mismatch, cycle detection), `MINOR` (soft threshold breach), determining the resolution priority and protocol.
- `AppK.S3.d`: `RevocationExecutor` — The engine that permanently removes a shard from the crystal: deletes its content, retires its Xi108 address, updates all routing tables and dependency graphs, and emits a `RevocationReceipt` for the permanent record.
