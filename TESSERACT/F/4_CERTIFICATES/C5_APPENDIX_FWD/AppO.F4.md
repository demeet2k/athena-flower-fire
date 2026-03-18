<!-- TESSERACT: F/4_CERTIFICATES/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=F facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.S4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.R4.md
-->

# AppO — Flower Lens / Certificates

- `AppO.F4.a`: `SyncConvergenceCert` — Proves that two nodes have converged by exhibiting both nodes' tile root hashes after sync completion and showing equality.
- `AppO.F4.b`: `CausalOrderCert` — Proves that deltas were applied in causal order by exhibiting the dependency graph and the application sequence, showing all edges point forward.
- `AppO.F4.c`: `MergeCorrectnessCert` — Proves that a conflict-free merge produced the correct result by exhibiting the concurrent deltas, their vector timestamps, and the selected winner for each conflicting cell.
- `AppO.F4.d`: `ExportCompletionCert` — Proves that every enqueued export operation completed by exhibiting the queue drain log with delivery confirmations for each operation.
