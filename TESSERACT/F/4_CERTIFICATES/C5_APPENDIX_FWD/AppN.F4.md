<!-- TESSERACT: F/4_CERTIFICATES/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=F facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.S4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.R4.md
-->

# AppN — Flower Lens / Certificates

- `AppN.F4.a`: `MountCompleteCert` — Proves that all shards in a container are accessible via the mount point by enumerating every shard address and confirming resolution; issued only after successful atomic mount.
- `AppN.F4.b`: `LazyLoadFidelityCert` — Proves that a lazily-loaded shard matches its container's recorded hash by exhibiting the hash comparison after first fetch.
- `AppN.F4.c`: `StreamOrderCert` — Proves that a streaming accessor emitted shards in correct crystal-coordinate order by exhibiting the sequence of addresses and verifying monotonicity.
- `AppN.F4.d`: `HotSwapAtomicityCert` — Proves that a hot swap completed atomically by exhibiting the mount point's resolution table before and after swap, showing no intermediate state was observable.
