<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.R4.md
-->

# AppL — Cloud Lens / Certificates

- `AppL.C4.a`: `BayesianUpdateCert` — Receipt proving the posterior distribution was updated correctly for each evidence item, normalization was maintained at every step, and the final posterior is a proper probability distribution.
- `AppL.C4.b`: `LikelihoodRatioConsistencyCert` — Receipt proving the likelihood ratio matrix satisfies transitivity, no circular evidence exists, and each ratio was computed from the correct candidate models.
- `AppL.C4.c`: `PromotionDecisionCert` — Receipt proving a candidate was promoted above threshold `τ`, the threshold satisfies the calibration constraint, and the posterior probability at time of promotion is recorded.
- `AppL.C4.d`: `InformationValueCert` — Receipt proving information values were computed correctly, all values are non-negative, and the recommended next evidence item has the highest expected gain among available options.
