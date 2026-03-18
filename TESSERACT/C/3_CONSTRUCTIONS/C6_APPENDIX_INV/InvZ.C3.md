<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.R3.md
-->

# InvZ — Cloud Lens / Constructions

- `InvZ.C3.a`: `MLESeedEstimator` — Runs maximum-likelihood estimation over the full organism state space. Uses EM algorithm for latent variables (hidden shells, compressed archetypes). Outputs the single most likely seed configuration.
- `InvZ.C3.b`: `EntropyDistiller` — Computes H(organism) via traversal, H(grammar) from the Rosetta engine's known structure, and derives H(seed) = H(organism) - H(grammar). Packs exactly H(seed) bits into the seed payload.
- `InvZ.C3.c`: `SufficientStatisticComputer` — Applies Neyman factorization to the organism's likelihood function. Extracts the minimal sufficient statistic. Verifies sufficiency by checking that the conditional distribution of data given statistic is parameter-free.
- `InvZ.C3.d`: `PriorExtractor` — Divides the posterior at the crown by the accumulated likelihood to extract the prior. Compares extracted prior with the declared initial prior. Reports any mutation (Bayesian drift).
