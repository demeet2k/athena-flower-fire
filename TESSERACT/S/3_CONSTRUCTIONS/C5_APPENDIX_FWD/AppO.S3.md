<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.R3.md
-->

# AppO — Square Lens / Constructions

- `AppO.S3.a`: `JSONExporter` — Traverses a crystal tile's 64 cells, serializes each into a JSON object with fields `{address, name, description, lens, facet, atom}`, and assembles them into an array wrapped in a tile envelope.
- `AppO.S3.b`: `MarkdownRenderer` — Converts a crystal tile into a markdown document by emitting `#` headers for lenses, `##` for facets, and `- backtick` list items for atoms, reproducing the canonical appendix format.
- `AppO.S3.c`: `DiffExporter` — Computes the delta between two versions of a crystal tile and exports only the changed cells as a patch bundle, with before/after pairs and crystal coordinates for targeted re-import.
- `AppO.S3.d`: `ReleaseSigner` — Computes the shard-level hashes, assembles the manifest, computes the manifest hash, signs it with the release key, and packages everything into the signed release ball.
