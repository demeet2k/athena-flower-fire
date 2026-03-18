<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.C3.md
-->

# InvY — Fractal Lens / Constructions

- `InvY.R3.a`: `RecursiveShutdownEngine` — Traverses the deployment tree bottom-up. At each node: shuts down children (recursively), drains the node, archives its telemetry, releases resources, generates cert. Outputs the fully-pruned tree with all certs attached.
- `InvY.R3.b`: `ContractionMonitor` — At each recursive step, measures the contraction ratio (size_after / size_before). Logs the ratio sequence. Verifies each ratio ≤ 1/φ. Flags any non-contracting step for manual intervention.
- `InvY.R3.c`: `ResourceLedgerReconciler` — For each pruned branch, reconciles allocated resources vs. released resources. Reports exact match, over-release, or under-release for each branch. Aggregates across the full tree.
- `InvY.R3.d`: `CertNormalizer` — Takes certs from all scales and verifies structural identity. Normalizes scale parameters so that certs from different levels can be compared. Outputs the universal shutdown cert template.
