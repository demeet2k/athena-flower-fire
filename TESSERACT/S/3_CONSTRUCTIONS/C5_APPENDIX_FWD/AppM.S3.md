<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.R3.md
-->

# AppM — Square Lens / Constructions

- `AppM.S3.a`: `IncrementalCheckpointer` — A construction that emits a new snapshot every `k` ticks by diffing the current state against the previous snapshot, storing only the delta and a full hash, yielding O(delta) storage per checkpoint.
- `AppM.S3.b`: `LogCompactor` — Merges consecutive log segments `L[i..j]` and `L[j..k]` into a single `L[i..k]` while garbage-collecting intermediate snapshots that are no longer needed for any active replay cursor.
- `AppM.S3.c`: `ForkReplayEngine` — Given a checkpoint lattice with branch point `S_b`, constructs two independent replay streams that diverge from `S_b`, each maintaining its own log and snapshot chain for counterfactual exploration.
- `AppM.S3.d`: `ReplayIndexBuilder` — Scans all existing log segments and snapshots, constructs the B-tree index, and validates that every shard address resolves to a replayable path; emits orphan reports for unreachable segments.
