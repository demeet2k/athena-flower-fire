<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppO.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppO.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppO.C2.md
-->

# AppO — Fractal Lens / Laws

- `AppO.R2.a`: `SelfPublicationFidelityLaw` — A self-publishing shard's output must be identical to what an external publication engine would produce for the same content; self-publication is an optimization, not a semantic change.
- `AppO.R2.b`: `AutoBundleCompletenessLaw` — An auto-bundle must include every cell that changed since the last bundle; skipped mutations accumulate and must appear in the next bundle; no change may be permanently lost.
- `AppO.R2.c`: `ManifestAccuracyLaw` — A generated publication manifest must accurately reflect the current state of all 64 cells; stale manifests that describe a prior tile version must be marked as superseded.
- `AppO.R2.d`: `DistributionAtomicityLaw` — A distribution seed capsule must publish to all listed targets or roll back; partial distribution (some targets updated, others not) is a violation requiring retry.
