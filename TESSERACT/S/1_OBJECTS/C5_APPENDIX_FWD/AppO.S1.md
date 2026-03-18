<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppO.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppO.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppO.R1.md
-->

# AppO — Square Lens / Objects

- `AppO.S1.a`: `JSONCrystalBundle` — A JSON document that serializes a crystal tile's 64 cells with their addresses, names, descriptions, and cross-references intact; the canonical machine-readable export format.
- `AppO.S1.b`: `MarkdownExport` — A human-readable markdown rendering of a crystal tile preserving the lens/facet/atom hierarchy as nested headers, with backtick names and long-dash descriptions matching the source format.
- `AppO.S1.c`: `CoordinatePreservingSerializer` — A serialization layer that guarantees every shard retains its full crystal coordinate `(Appendix.Lens.Facet.Atom)` through export and re-import, preventing address drift across systems.
- `AppO.S1.d`: `SignedReleaseBall` — A tarball of exported crystal content signed with the organism's release key, containing a manifest of included shards, their hashes, and the signature block for authenticity verification.
