<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.R3.md
-->

# AppO — Cloud Lens / Constructions

- `AppO.C3.a`: `SimultaneousPublisher` — Takes a crystal tile, runs all format-specific renderers in parallel, collects their outputs, and publishes them atomically so that all formats become available at the same instant.
- `AppO.C3.b`: `ConstructionCodeGenerator` — Extracts the Facet 3 (Constructions) cells from a crystal tile, generates a class or module for each construction with the crystal address as its identifier, and emits compilable source code.
- `AppO.C3.c`: `CatalogRegistrar` — Extracts metadata from a published tile, constructs a data catalog entry conforming to the catalog schema, and registers it with the discovery service.
- `AppO.C3.d`: `LinkTableBuilder` — After all formats are published, scans each format's output to locate every shard's rendered position, and assembles the cross-format link table mapping addresses to format-specific locations.
