<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.C3.md
-->

# InvM — Fractal Lens / Constructions

- `InvM.R3.a`: `HierarchicalPruner` — Traverses the registry tree bottom-up. At each leaf: prunes local registry. At each parent: re-scans reachability (some entries may now be dead), prunes newly dead entries. Reports level-by-level pruning progress.
- `InvM.R3.b`: `ContractionTracker` — Measures attribute reduction at each level. Verifies golden ratio contraction. Flags sub-golden levels.
- `InvM.R3.c`: `TreeCollapser` — Manages leaf-first collapse. Tracks which registries are pruned and which are pending.
- `InvM.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Reports deviations.
