<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvU.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvU.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvU.R1.md
-->

# InvU — Cloud Lens / Objects

- `InvU.C1.a`: `BayesianVerdictPosterior` — The posterior probability of each hypothesis after all evidence is accumulated. The hypothesis with highest posterior wins the verdict. The Cloud view: verdict is maximum a posteriori (MAP) estimation over the hypothesis space.
- `InvU.C1.b`: `AMBIGProbabilityExclusion` — The probability of AMBIG (neither hypothesis dominates) is estimated by inclusion-exclusion over the overlap region of hypothesis posteriors. As evidence accumulates, the overlap shrinks and AMBIG probability decreases.
- `InvU.C1.c`: `IndependentEvidenceProduct` — Independent pieces of evidence multiply likelihoods: L(H|e₁,e₂) = L(H|e₁)·L(H|e₂). The Cloud view factorizes the evidence into independent contributions, making the posterior computation tractable.
- `InvU.C1.d`: `InformationGainNormalization` — Each piece of evidence is valued by its information gain (KL divergence from prior to posterior). Evidence with high information gain per unit cost is prioritized during compression. Low-gain evidence is released first.
