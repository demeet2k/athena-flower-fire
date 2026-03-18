<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.C3.md
-->

# InvX — Fractal Lens / Constructions

- `InvX.R3.a`: `RecursiveUnpacker` — Traverses the bundle tree bottom-up. At each leaf: extracts shard, verifies, absorbs. At each node: dissolves sub-bundle wrapper after all children absorbed. Reports total depth, total shards, and any malformed levels.
- `InvX.R3.b`: `NestingAnalyzer` — Computes the contraction factor at each recursive level. Reports the sequence of factors and flags any non-contracting levels. Estimates total absorption time from the contraction profile.
- `InvX.R3.c`: `ConvergenceChecker` — Sums total shards across all nesting levels. Verifies the sum is finite and within the declared bound. Reports any level that contributes disproportionately.
- `InvX.R3.d`: `ProtocolConsistencyChecker` — Verifies that the absorption protocol is identical at every level by comparing the operation sequence. Reports any level-specific deviations.
