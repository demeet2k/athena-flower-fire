<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.R3.md
-->

# InvM — Square Lens / Constructions

- `InvM.S3.a`: `ReachabilityScanner` — Performs a graph traversal from all active reference roots. Marks every entry reached. Unmarked entries are dead. Reports the count of live vs. dead entries and the reachability ratio.
- `InvM.S3.b`: `ProfileMinimizer` — For each surviving entry: iteratively removes attributes, testing reconstruction after each removal. Retains the minimal set that allows reconstruction. Reports the original and minimized attribute counts.
- `InvM.S3.c`: `VersionCollapser` — For each surviving entry: identifies the latest valid version from the version history. Discards all other versions. Retains the collapsed version and the version ID. Reports the original history length and the collapsed state.
- `InvM.S3.d`: `CompressionReporter` — Computes the compression quotient: compressed_size / original_size. Reports per-entry and aggregate quotients. Identifies the most compressible entries and the least compressible.
