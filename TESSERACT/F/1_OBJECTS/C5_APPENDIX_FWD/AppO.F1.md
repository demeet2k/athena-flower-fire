<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppO.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppO.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppO.R1.md
-->

# AppO — Flower Lens / Objects

- `AppO.F1.a`: `SyncProtocol` — A bidirectional synchronization protocol that compares local and remote crystal tile versions, identifies divergent cells, and transmits only the deltas needed to reconcile them.
- `AppO.F1.b`: `DeltaUpdateStream` — A continuous stream of cell-level changes emitted by a crystal tile as it evolves, formatted as `(address, old_hash, new_hash, new_content)` tuples for incremental consumption by subscribers.
- `AppO.F1.c`: `ConflictFreeImporter` — An import engine that applies incoming shard updates using CRDT merge semantics: concurrent edits to the same cell are resolved by last-writer-wins with logical timestamps.
- `AppO.F1.d`: `ExportQueue` — A persistent ordered queue of pending export operations that ensures every tile mutation is eventually exported, even if the export target is temporarily unreachable.
