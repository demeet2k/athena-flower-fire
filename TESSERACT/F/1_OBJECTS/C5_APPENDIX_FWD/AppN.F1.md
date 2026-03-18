<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppN.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppN.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppN.R1.md
-->

# AppN — Flower Lens / Objects

- `AppN.F1.a`: `MountPoint` — A virtual filesystem node where a container's contents become addressable as if they were local files; mounting binds a container's shard addresses to path names in the crystal namespace.
- `AppN.F1.b`: `LazyLoader` — A deferred-access proxy that presents shard metadata immediately but fetches actual content only on first read, reducing mount latency for large capsule bundles.
- `AppN.F1.c`: `StreamingAccessor` — A sequential reader that traverses a container's shards in crystal-coordinate order, emitting content as a continuous stream without requiring the entire archive to be resident in memory.
- `AppN.F1.d`: `HotSwapSocket` — A mount point that supports live replacement of the underlying container without unmounting; active readers are transparently redirected to the new container version.
