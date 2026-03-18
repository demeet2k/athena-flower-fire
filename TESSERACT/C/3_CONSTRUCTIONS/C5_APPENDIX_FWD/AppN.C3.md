<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.R3.md
-->

# AppN — Cloud Lens / Constructions

- `AppN.C3.a`: `LensFilter` — Scans a crystal archive's offset table, selects entries whose SFCR tag matches the desired lens, and constructs a lightweight projection index that maps filtered addresses to archive offsets.
- `AppN.C3.b`: `OverlayMerger` — Flattens an overlay stack into a single resolved container by iterating all addresses top-down and emitting the first hit for each; produces a materialized snapshot of the overlay state.
- `AppN.C3.c`: `ManifoldSpawner` — Given a crystal archive, spawns `k` concurrent lens projections, each with its own read cursor and filter index, sharing the underlying archive via memory-mapped access.
- `AppN.C3.d`: `UnionResolver` — Takes `n` source containers, builds a unified address index with priority rankings, and exposes a single virtual container interface; supports lazy resolution for deferred conflict handling.
