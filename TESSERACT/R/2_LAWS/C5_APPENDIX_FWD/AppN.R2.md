<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppN.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppN.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppN.C2.md
-->

# AppN — Fractal Lens / Laws

- `AppN.R2.a`: `SelfDocumentationLaw` — A self-describing container must carry sufficient metadata that a reader with no prior knowledge of the format can parse the header, identify the schema, and begin reading shards.
- `AppN.R2.b`: `BootstrapSufficiencyLaw` — A bootstrap archive's embedded runtime must be sufficient to mount the archive, resolve any shard address, and verify shard integrity without depending on any external software.
- `AppN.R2.c`: `SchemaMigrationLaw` — A schema evolution envelope must guarantee lossless round-trip migration: `migrate(v_old → v_new) ∘ migrate(v_new → v_old)` must yield the original content for all valid shards.
- `AppN.R2.d`: `CodecNegotiationLaw` — An auto-decompressing packet must never send data in a codec the recipient cannot decode; the negotiation protocol must confirm codec support before transmission begins.
