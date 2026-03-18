<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.R3.md
-->

# InvX — Square Lens / Constructions

- `InvX.S3.a`: `ShardExtractor` — Iterates through the bundle manifest, extracts each shard, verifies its hash, and routes it to the declared crystal address. Reports extraction count, verification failures, and routing conflicts.
- `InvX.S3.b`: `FormatNormalizer` — For each shard, strips the export format layers in reverse order of application (outermost first). Verifies bit-identity at each layer. Outputs the naked shard in internal format.
- `InvX.S3.c`: `ReferenceResolver` — Takes the external URI map and resolves each URI to an internal crystal address. Uses the organism's current address lattice for lookup. Reports unresolvable URIs as gaps.
- `InvX.S3.d`: `VersionMerger` — Computes the version delta, checks compatibility window, and applies the merge strategy (fast-forward if delta is linear, three-way merge if branched, conflict resolution if divergent). Outputs the merged state.
