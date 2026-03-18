<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.R3.md
-->

# InvR — Cloud Lens / Constructions

- `InvR.C3.a`: `MLTruthCommitter` — For each corridor: estimates P(true) from evidence, commits to the ML value, records the confidence. Reports corridors with low confidence (near 0.5) as convention-evaluated.
- `InvR.C3.b`: `CorrelationComputer` — Computes pairwise corridor correlations. Identifies dependent clusters. Reports the correlation matrix and cluster assignments.
- `InvR.C3.c`: `IndependenceVerifier` — Tests corridor independence using mutual information or chi-squared tests. Authorizes independent evaluation for verified-independent corridors.
- `InvR.C3.d`: `InformationRanker` — Ranks truth values by information content. Reports the information distribution. Identifies the most information-dense truths for priority preservation.
