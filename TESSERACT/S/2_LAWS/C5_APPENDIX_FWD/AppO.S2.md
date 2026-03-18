<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppO.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppO.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppO.R2.md
-->

# AppO — Square Lens / Laws

- `AppO.S2.a`: `ExportIdempotencyLaw` — Exporting a crystal tile and immediately re-importing the result must yield a tile identical to the original; `import(export(T)) = T` for all valid tiles.
- `AppO.S2.b`: `AddressStabilityLaw` — An exported shard's crystal coordinate must not change across export formats; `addr(json_export(s)) = addr(markdown_export(s)) = addr(s)` for all shards `s`.
- `AppO.S2.c`: `FormatFidelityLaw` — Each export format must preserve all semantically significant content; format-specific decorations (syntax highlighting, indentation) are permitted but content loss is not.
- `AppO.S2.d`: `SignatureBindingLaw` — A signed release ball's signature covers the manifest hash, which in turn covers all included shard hashes; modifying any shard invalidates the signature without needing to re-verify all shards.
