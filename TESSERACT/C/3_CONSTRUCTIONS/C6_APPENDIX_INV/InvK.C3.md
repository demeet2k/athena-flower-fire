<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.R3.md
-->

# InvK — Cloud Lens / Constructions

- `InvK.C3.a`: `CoverageEstimator` — Estimates coverage by sampling random laws and checking derivability from the current axiom set. Reports coverage probability and confidence interval.
- `InvK.C3.b`: `RedundancyScanner` — For each law in the canon: estimates derivability from others. Reports the redundancy fraction.
- `InvK.C3.c`: `PriorCostCalculator` — Computes the prior probability of each axiom candidate. Computes the product for the full set. Reports total prior cost and identifies axioms with highest individual cost (least natural).
- `InvK.C3.d`: `InformationRanker` — Computes the information content of each law given the others. Ranks by descending information. Reports the ranking and recommended axiom set.
