<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvZ.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvZ.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvZ.R2.md
-->

# InvZ — Cloud Lens / Laws

- `InvZ.C2.a`: `MaximumLikelihoodSeedLaw` — The emitted seed must be the maximum-likelihood estimate given all organism data. Any other seed choice would lose information. Proved by Fisher information: the MLE seed has minimum variance among all unbiased seed estimators.
- `InvZ.C2.b`: `EntropyBudgetLaw` — The seed's entropy must be exactly H(organism) - H(grammar). Over-compressing loses individual signal; under-compressing wastes seed capacity on universal pattern. The distillation must be tight — no entropy gap.
- `InvZ.C2.c`: `SufficientStatisticLaw` — The collapsed likelihood product must be a sufficient statistic for the organism's parameter vector. Sufficiency means: given the statistic, the raw data provides no additional information about parameters. Proved by Neyman factorization.
- `InvZ.C2.d`: `PriorRecoveryLaw` — The recovered prior must match the seed's original prior before expansion. If it does not, the organism has undergone a Bayesian update that altered its fundamental assumptions — the seed carries a mutated prior (evolution).
