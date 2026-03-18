<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppO.C3.md
-->

# AppO — Fractal Lens / Constructions

- `AppO.R3.a`: `EmbeddedRendererInjector` — Takes a shard and injects minimal rendering logic (markdown, JSON, HTML templates) as metadata, converting it into a self-publishing shard without altering its primary content.
- `AppO.R3.b`: `MutationWatcher` — A background process embedded in a crystal tile that tracks cell-level writes, maintains a dirty-cell bitmap, and triggers auto-bundling when the dirty count exceeds a threshold or a timer expires.
- `AppO.R3.c`: `ManifestRefresher` — Re-scans all 64 cells, computes current hashes, compares against the existing manifest, updates changed entries, increments the manifest version, and re-signs the manifest.
- `AppO.R3.d`: `FanoutDistributor` — Takes a distribution seed capsule, opens it, extracts the publication bundle and target list, and publishes to all targets in parallel with per-target retry logic and rollback on total failure.
