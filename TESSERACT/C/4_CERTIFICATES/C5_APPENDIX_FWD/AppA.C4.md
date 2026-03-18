<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppA.R4.md
-->

# AppA — Cloud Lens / Certificates

- `AppA.C4.a`: `FuzzyResolutionCert` — Receipt proving fuzzy resolution converged to a unique address with posterior probability exceeding threshold `τ`, listing the top-k candidates and their probabilities.
- `AppA.C4.b`: `NeighborSearchCert` — Receipt proving all stations within Hamming radius `r` were enumerated, none were missed, and the sorted order is correct with respect to the declared distance metric.
- `AppA.C4.c`: `AmbiguityBoundCert` — Receipt proving the ambiguity cloud contains exactly `N` candidate addresses, the cloud volume matches the predicted reduction from parsed components, and all candidates exist in the registry.
- `AppA.C4.d`: `CalibrationCert` — Receipt proving the confidence estimator is calibrated within tolerance `ε` on the declared validation set, with calibration curve and Brier score recorded.
