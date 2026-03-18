<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppN.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppN.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppN.R1.md
-->

# AppN — Cloud Lens / Objects

- `AppN.C1.a`: `LensProjection` — A virtual view that presents only the shards belonging to a single SFCR lens (S, F, C, or R) from a full crystal archive, without copying or restructuring the underlying data.
- `AppN.C1.b`: `OverlayStack` — A layered composition of multiple containers where higher layers shadow lower layers for the same crystal address; resolves reads by scanning layers top-down, enabling incremental patches.
- `AppN.C1.c`: `MultiViewManifold` — A structure that maintains `k` simultaneous lens projections over the same archive, each presenting a different facet-subset; queries can be routed to any active view.
- `AppN.C1.d`: `VirtualUnionContainer` — A container that presents the union of shards from multiple source containers as if they were a single archive, resolving address collisions by priority ranking.
