<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.R3.md
-->

# AppN — Flower Lens / Constructions

- `AppN.F3.a`: `VirtualMountEngine` — Maps a container's internal offset table to virtual path entries, registers them in the crystal namespace, and begins serving read requests; unmounting reverses the registration.
- `AppN.F3.b`: `PrefetchScheduler` — Monitors access patterns on a lazily-loaded mount and speculatively prefetches shards that are likely to be needed next, based on crystal-coordinate locality.
- `AppN.F3.c`: `StreamingPipeline` — Chains a container reader, a decompressor, and a shard parser into a zero-copy pipeline that converts raw archive bytes into typed shard objects without intermediate buffering.
- `AppN.F3.d`: `VersionedMountSwapper` — Coordinates hot swap by mounting the new container to a shadow mount point, verifying integrity, then atomically redirecting the primary mount point's resolution table.
