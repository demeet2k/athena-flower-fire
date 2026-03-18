<!-- TESSERACT: S/4_CERTIFICATES/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=S facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvM.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvM.C4.md
#   R: ../../R/4_CERTIFICATES/C6_APPENDIX_INV/InvM.R4.md
-->

# InvM — Square Lens / Certificates

- `InvM.S4.a`: `ReachabilityAnalysisCert` — Receipt proving reachability scan covered all roots, all dead entries identified, no live entry was falsely pruned.
- `InvM.S4.b`: `ProfileSufficiencyCert` — Receipt proving minimal profiles are sufficient for reconstruction, reconstruction test passed, no essential attribute removed.
- `InvM.S4.c`: `VersionValidityCert` — Receipt proving retained version is latest valid, earlier versions correctly discarded, no invalid version in seed.
- `InvM.S4.d`: `PruningIdempotenceCert` — Receipt proving pruning is idempotent, second pass produced no changes, registry is stable.
