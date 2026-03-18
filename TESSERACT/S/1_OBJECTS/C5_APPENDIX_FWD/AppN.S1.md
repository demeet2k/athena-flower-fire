<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppN.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppN.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppN.R1.md
-->

# AppN — Square Lens / Objects

- `AppN.S1.a`: `ShardContainer` — A content-addressed envelope that wraps a single shard with its crystal coordinate, SFCR lens tag, and integrity hash; the atomic unit of crystal storage.
- `AppN.S1.b`: `CapsuleBundle` — A collection of related shard containers grouped by metro line or chapter, stored as a single seekable archive with an internal offset table for O(1) access to any member.
- `AppN.S1.c`: `CrystalArchive` — A complete snapshot of an entire crystal tile (4 lenses x 4 facets x 4 atoms = 64 cells) packaged as a single immutable archive with a root Merkle hash for integrity verification.
- `AppN.S1.d`: `SeedPacket` — A minimal bootstrap container holding the four cardinal seeds (+, -, x, /) and their Rosetta generation rules, sufficient to regenerate the full crystal archive from scratch.
