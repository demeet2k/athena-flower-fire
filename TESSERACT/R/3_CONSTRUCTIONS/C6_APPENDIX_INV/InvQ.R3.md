<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.C3.md
-->

# InvQ — Fractal Lens / Constructions

- `InvQ.R3.a`: `HierarchicalContractor` — Traverses the topology tree bottom-up. At each leaf: contracts internal topology. At each node: uses child contractions to simplify node topology, then contracts. Reports depth, total couplings removed, and homotopy verification at each level.
- `InvQ.R3.b`: `ContractionRatioTracker` — Measures coupling reduction ratio at each level. Verifies ≤ 1/φ. Flags sub-golden levels.
- `InvQ.R3.c`: `TreeCollapseEngine` — Manages the leaf-first collapse. Tracks which nodes are complete, which are pending. Ensures parent contraction waits for all children.
- `InvQ.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Reports deviations. Confirms fixed-point property.
