<!-- TESSERACT: S/4_CERTIFICATES/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=S facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvX.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvX.C4.md
#   R: ../../R/4_CERTIFICATES/C6_APPENDIX_INV/InvX.R4.md
-->

# InvX — Square Lens / Certificates

- `InvX.S4.a`: `ShardIntegrityCert` — Receipt proving all shards extracted and hash-verified, no corruption detected, all shards routed to correct addresses.
- `InvX.S4.b`: `FormatStripCert` — Receipt proving format stripping was lossless, all layers removed cleanly, shard content is bit-identical to pre-export state.
- `InvX.S4.c`: `ReferenceResolutionCert` — Receipt proving all cross-references resolved (or gaps explicitly documented), no dangling references in the absorbed state.
- `InvX.S4.d`: `VersionMergeCert` — Receipt proving version delta computed correctly, compatibility window respected, merge strategy applied without data loss.
