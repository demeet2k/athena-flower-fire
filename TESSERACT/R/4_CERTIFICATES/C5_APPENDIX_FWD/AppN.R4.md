<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.C4.md
-->

# AppN — Fractal Lens / Certificates

- `AppN.R4.a`: `SchemaParsabilityCert` — Proves that a self-describing container's schema is parsable by a generic reader by exhibiting the parse tree produced from the header using only the universal meta-schema.
- `AppN.R4.b`: `BootstrapSelfTestCert` — Proves that a bootstrap archive's embedded runtime can mount and verify the archive by exhibiting the runtime's execution trace on the archive itself, showing successful shard resolution.
- `AppN.R4.c`: `MigrationRoundTripCert` — Proves lossless schema migration by exhibiting a test shard, migrating it forward and back through the version chain, and showing bitwise identity with the original.
- `AppN.R4.d`: `CodecCompatibilityCert` — Proves that the selected codec is supported by the recipient by exhibiting the codec negotiation handshake log and the successful test decompression of a probe payload.
