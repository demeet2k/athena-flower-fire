<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.C3.md
-->

# AppN — Fractal Lens / Constructions

- `AppN.R3.a`: `SchemaEmbedder` — Takes a container and its schema definition, serializes the schema into the container header using a universal meta-schema, and appends the decompression algorithm as a portable bytecode snippet.
- `AppN.R3.b`: `BootstrapPackager` — Bundles a crystal archive with a minimal mount runtime compiled to WebAssembly, producing a single file that can be opened in any environment with a WASM executor.
- `AppN.R3.c`: `MigrationChainBuilder` — Given schema versions `v_1, ..., v_n`, constructs the chain of migration functions `v_i → v_{i+1}` and their inverses, and embeds the chain in a schema evolution envelope.
- `AppN.R3.d`: `CodecProber` — Queries the recipient environment for available decompression codecs, ranks them by decompression speed and ratio, and rewraps the container's payload in the optimal codec before sending.
