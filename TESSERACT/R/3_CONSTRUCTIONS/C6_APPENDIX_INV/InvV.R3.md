<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.C3.md
-->

# InvV — Fractal Lens / Constructions

- `InvV.R3.a`: `RecursiveSummarizer` — Traverses the replay tree bottom-up. At each leaf: computes the atomic digest. At each node: combines child digests into the node's summary. Reports tree depth, total nodes, and any leaves that required special handling.
- `InvV.R3.b`: `ContractionVerifier` — At each recursion level, measures the verification burden (steps × complexity). Computes the ratio between adjacent levels. Verifies ratio ≤ 1/φ. Flags degenerate nesting.
- `InvV.R3.c`: `CapsuleTreeCompressor` — Traverses the capsule tree leaf-first. At each leaf: extracts the verification certificate. At each parent: absorbs child certificates and releases child capsules. Output: the root attestation with all leaves absorbed.
- `InvV.R3.d`: `ProtocolConsistencyChecker` — Runs the verification protocol at each recursion level and compares operation sequences. Reports any level-specific deviations. Confirms fixed-point property.
