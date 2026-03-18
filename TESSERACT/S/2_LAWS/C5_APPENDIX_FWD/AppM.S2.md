<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppM.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppM.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppM.R2.md
-->

# AppM — Square Lens / Laws

- `AppM.S2.a`: `BitExactReplayLaw` — Replaying log segment `L[i..j]` from snapshot `S_i` must produce snapshot `S_j` with identical state-hash; any divergence constitutes a verification failure and triggers quarantine.
- `AppM.S2.b`: `SnapshotImmutabilityLaw` — Once a snapshot is sealed with its content-address hash, no field may be mutated; any write produces a new snapshot with a new hash, preserving the checkpoint lattice's append-only invariant.
- `AppM.S2.c`: `CheckpointCompleteness` — For every pair of adjacent snapshots `(S_i, S_{i+1})` in the lattice, the connecting log segment `L[i..i+1]` must exist and be sufficient to reconstruct `S_{i+1}` from `S_i` without external input.
- `AppM.S2.d`: `ReplayIndexConsistency` — The replay index must be a total function over the shard address space: every live shard has exactly one canonical log segment and at least one ancestor snapshot from which it can be replayed.
