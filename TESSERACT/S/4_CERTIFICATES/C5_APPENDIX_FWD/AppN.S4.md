<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.R4.md
-->

# AppN — Square Lens / Certificates

- `AppN.S4.a`: `ContainerIntegrityCert` — Proves that a shard container's content-address hash matches its payload by exhibiting the hash computation; a single bit change in the payload invalidates the certificate.
- `AppN.S4.b`: `BundleCompletenessCert` — Proves that a capsule bundle's offset table is total and correct by exhibiting the list of all member shard addresses and their verified offsets.
- `AppN.S4.c`: `ArchiveMerkleCert` — Proves archive integrity by exhibiting the Merkle tree from leaf shard hashes to the root; any individual shard can be verified with an O(log n) Merkle path.
- `AppN.S4.d`: `SeedRegenerationCert` — Proves seed sufficiency by exhibiting the regenerated archive's root hash and showing it matches the original archive's root hash recorded in the seed packet.
