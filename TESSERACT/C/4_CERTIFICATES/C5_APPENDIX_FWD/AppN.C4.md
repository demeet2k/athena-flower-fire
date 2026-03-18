<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppN.R4.md
-->

# AppN — Cloud Lens / Certificates

- `AppN.C4.a`: `ProjectionCorrectnessCert` — Proves that a lens projection contains exactly the shards matching the selected lens by exhibiting the filter predicate and the matched/unmatched address partition.
- `AppN.C4.b`: `OverlayResolutionCert` — Proves that every address in an overlay stack resolves to the correct layer by exhibiting the layer scan order and the first-hit index for each address.
- `AppN.C4.c`: `ViewFreshnessCert` — Proves that all views in a multi-view manifold reference the same archive version by exhibiting the archive root hash that each view was derived from.
- `AppN.C4.d`: `UnionCoverageCert` — Proves that a virtual union container covers the union of all source address sets by exhibiting each source's address list and the merged index.
