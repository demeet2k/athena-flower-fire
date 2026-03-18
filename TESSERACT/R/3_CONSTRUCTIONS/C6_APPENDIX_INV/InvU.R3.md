<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.C3.md
-->

# InvU — Fractal Lens / Constructions

- `InvU.R3.a`: `BottomUpResolver` — Traverses the evidence tree leaf-first. At each leaf: evaluates the observation. At each node: aggregates child verdicts and emits the node verdict. Reports the resolution path from leaves to root.
- `InvU.R3.b`: `AMBIGContractionTracker` — Measures AMBIG space at each level. Computes the contraction ratio between adjacent levels. Flags any level with insufficient contraction for investigation deepening.
- `InvU.R3.c`: `EvidenceTreePruner` — After bottom-up resolution, prunes the tree from leaves to root. At each leaf: verifies information captured in parent, then releases. Reports total pruned nodes and remaining tree (root verdict only).
- `InvU.R3.d`: `ProtocolVerifier` — Compares the judgment protocol at each level. Verifies identical structure. Reports any level-specific deviations.
