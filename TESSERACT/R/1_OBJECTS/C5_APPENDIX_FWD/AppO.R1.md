<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppO.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppO.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppO.C1.md
-->

# AppO — Fractal Lens / Objects

- `AppO.R1.a`: `SelfPublishingShard` — A shard that contains embedded publication logic: when invoked, it renders itself into all supported formats and emits the results without requiring an external publication engine.
- `AppO.R1.b`: `AutoBundleTile` — A crystal tile that monitors its own mutation history and automatically packages changed cells into a delta export bundle at configurable intervals, ready for distribution.
- `AppO.R1.c`: `PublicationManifestGenerator` — A module embedded in a crystal archive that, when triggered, scans all 64 cells, generates a publication manifest listing each cell's address, name, hash, and format availability.
- `AppO.R1.d`: `DistributionSeedCapsule` — A self-contained capsule that carries a crystal tile, its publication logic, and a list of distribution targets; opening the capsule triggers publication to all listed targets.
