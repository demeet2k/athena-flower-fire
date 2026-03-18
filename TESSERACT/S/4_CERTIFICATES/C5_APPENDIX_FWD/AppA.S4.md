<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.R4.md
-->

# AppA — Square Lens / Certificates

- `AppA.S4.a`: `ParseValidityCert` — Receipt proving a raw address string was parsed without error, all five components fell within legal ranges, and the resulting Xi108 address exists in the crystal registry.
- `AppA.S4.b`: `StationResolutionCert` — Receipt proving a chapter station code resolved to exactly one Xi108 address, no ambiguity remained, and the registry version at time of resolution is recorded.
- `AppA.S4.c`: `CanonicalizationCert` — Receipt proving an address variant was normalized to canonical form, listing each normalization step applied (mod reduction, alias expansion, legacy format upgrade) with before/after pairs.
- `AppA.S4.d`: `BatchCompilationCert` — Receipt proving a batch address expression expanded to `N` concrete addresses with zero overlaps, complete coverage of the declared range, and no out-of-bounds coordinates.
