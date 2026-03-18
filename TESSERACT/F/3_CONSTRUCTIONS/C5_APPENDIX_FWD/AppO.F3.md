<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.R3.md
-->

# AppO — Flower Lens / Constructions

- `AppO.F3.a`: `TreeDiffSynchronizer` — Computes a Merkle tree over both local and remote tiles, identifies the minimal subtree of differing cells by comparing intermediate hashes, and transmits only the divergent leaves.
- `AppO.F3.b`: `DeltaCompressor` — Groups consecutive delta updates to the same cell into a single compound delta that jumps directly from the initial to the final state, reducing transmission volume for burst edits.
- `AppO.F3.c`: `CRDTMergeEngine` — Maintains a vector clock per cell, tags each delta with its vector timestamp, and resolves concurrent writes by selecting the delta with the highest timestamp component for the originating node.
- `AppO.F3.d`: `RetryableExportWorker` — Dequeues export operations, attempts delivery with exponential backoff, and returns failed operations to the queue with incremented retry counters; dead-letters after configurable max retries.
