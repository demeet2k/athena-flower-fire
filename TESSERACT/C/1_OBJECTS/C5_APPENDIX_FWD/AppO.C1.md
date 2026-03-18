<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppO.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppO.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppO.R1.md
-->

# AppO — Cloud Lens / Objects

- `AppO.C1.a`: `MultiFormatPublisher` — A publication engine that takes a single crystal tile and simultaneously emits it as JSON, markdown, HTML, and structured data, each format generated from the same canonical internal representation.
- `AppO.C1.b`: `CodeExporter` — Generates executable code (Python, TypeScript) from a crystal tile's constructions facet, embedding the crystal coordinates as comments and the descriptions as docstrings.
- `AppO.C1.c`: `DataCatalogEntry` — A structured metadata record that describes a published crystal tile in terms discoverable by data catalogs: title, description, schema version, coordinate range, and access URL.
- `AppO.C1.d`: `CrossFormatLinker` — A reference table that maps each shard's crystal address to its location in every published format (JSON path, markdown line number, HTML anchor, code symbol), enabling cross-format navigation.
