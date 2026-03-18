<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppN.R3.md
-->

# AppN — Square Lens / Constructions

- `AppN.S3.a`: `ShardContainerBuilder` — Takes raw shard content, computes its crystal coordinate from the SFCR address, wraps it with metadata headers, and seals it with a content-address hash.
- `AppN.S3.b`: `BundleAssembler` — Collects a set of shard containers, sorts them by crystal coordinate, builds the offset table, and writes the seekable archive; validates completeness before sealing.
- `AppN.S3.c`: `ArchiveSnapshotter` — Traverses all 64 cells of a crystal tile, wraps each as a shard container, assembles them into a bundle, computes the Merkle root, and seals the crystal archive.
- `AppN.S3.d`: `SeedExtractor` — Given a crystal archive, identifies the four cardinal seed cells, extracts them with their generation rules, and packages them into a minimal seed packet.
