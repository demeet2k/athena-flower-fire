<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvX.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvX.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvX.C2.md
-->

# InvX — Fractal Lens / Laws

- `InvX.R2.a`: `LeafFirstAbsorptionLaw` — Recursive absorption must proceed leaf-first. No parent bundle is dissolved until all its child shards/sub-bundles are fully absorbed. This prevents orphaned references.
- `InvX.R2.b`: `ContractionBoundLaw` — Each recursive level must reduce remaining complexity. If a level fails to contract (e.g., a sub-bundle is larger than its parent's allocation), the bundle structure is malformed and absorption halts.
- `InvX.R2.c`: `ConvergentAbsorptionLaw` — The total number of shards absorbed must converge (sum of shards at all levels is finite). Infinite nesting is not permitted; maximum depth is bounded by the organism's declared recursion limit.
- `InvX.R2.d`: `ProtocolFixedPointLaw` — The absorption protocol must be structurally identical at every level. Any level-specific deviation indicates a format inconsistency between nesting levels.
