<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.R4.md
-->

# AppO — Cloud Lens / Certificates

- `AppO.C4.a`: `MultiFormatConsistencyCert` — Proves that all published formats carry identical semantic content by exhibiting the canonical representation and a diff against each format's re-parsed content, showing zero semantic differences.
- `AppO.C4.b`: `CodeValidityCert` — Proves that generated code is syntactically valid by exhibiting the parser's success result for each generated source file in its target language.
- `AppO.C4.c`: `CatalogRegistrationCert` — Proves that a tile's catalog entry exists and is correctly populated by exhibiting the catalog query result and comparing it field-by-field against the tile's metadata.
- `AppO.C4.d`: `LinkIntegrityCert` — Proves that every cross-format link resolves correctly by exhibiting the resolution result for each shard address in each format, confirming no broken links.
