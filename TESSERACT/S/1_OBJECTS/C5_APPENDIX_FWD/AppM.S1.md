<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppM.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppM.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppM.R1.md
-->

# AppM — Square Lens / Objects

- `AppM.S1.a`: `ReplayLog` — An append-only, content-addressed sequence of `(tick, action, state-hash)` triples that records every discrete transition of a computation, enabling bit-exact rerun from any checkpoint.
- `AppM.S1.b`: `DeterministicSnapshot` — A frozen image of full computation state at tick `t`, including register file, heap digest, and RNG seed, such that resuming from the snapshot reproduces the identical successor trace.
- `AppM.S1.c`: `CheckpointLattice` — A partially-ordered set of snapshots where `snap_i ≤ snap_j` iff `j` is reachable from `i` by replaying the intervening log segment; supports branching and merge for forked replays.
- `AppM.S1.d`: `ReplayIndex` — A B-tree over `(shard-id, tick-range)` pairs that maps any crystal address to the log segment and snapshot needed to reconstruct it, enabling O(log n) random-access replay.
