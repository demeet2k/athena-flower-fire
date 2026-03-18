<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.C4.md
-->

# AppO — Fractal Lens / Certificates

- `AppO.R4.a`: `SelfPublicationMatchCert` — Proves that a self-publishing shard's output matches external publication by exhibiting both outputs and showing bitwise equality.
- `AppO.R4.b`: `AutoBundleCoverageCert` — Proves that an auto-bundle covers all mutations since the last bundle by exhibiting the mutation log, the dirty-cell bitmap at bundle time, and the bundle's included cell list.
- `AppO.R4.c`: `ManifestFreshnessCert` — Proves that a publication manifest is current by exhibiting each cell's live hash and the manifest's recorded hash, showing equality for all 64 cells.
- `AppO.R4.d`: `FullDistributionCert` — Proves that a distribution seed capsule published to all targets by exhibiting each target's delivery acknowledgment and the capsule's target list, showing complete coverage.
