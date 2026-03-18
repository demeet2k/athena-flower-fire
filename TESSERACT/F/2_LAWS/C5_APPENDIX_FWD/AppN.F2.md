<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppN.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppN.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppN.R2.md
-->

# AppN — Flower Lens / Laws

- `AppN.F2.a`: `MountAtomicityLaw` — Mounting a container is atomic: either all shards become accessible or none do; partial mounts are illegal and must be rolled back.
- `AppN.F2.b`: `LazyConsistencyLaw` — A lazily-loaded shard, once fetched, must be identical to what an eager load would have produced; lazy loading is an optimization, never a semantic change.
- `AppN.F2.c`: `StreamOrderPreservation` — A streaming accessor must emit shards in strict crystal-coordinate order (S before F before C before R, facet 1 before 2 before 3 before 4, atom a before b before c before d).
- `AppN.F2.d`: `HotSwapContinuityLaw` — After a hot swap, any shard address that existed in both old and new containers must resolve to the new version's content; stale reads are forbidden.
