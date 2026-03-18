<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.R3.md
-->

# InvU — Cloud Lens / Constructions

- `InvU.C3.a`: `MAPEstimator` — Computes the posterior for each hypothesis using Bayes' theorem. Selects the MAP hypothesis. Outputs the posterior distribution, the MAP verdict, and the confidence gap between first and second hypotheses.
- `InvU.C3.b`: `AMBIGProbabilityTracker` — Estimates P(AMBIG) at each evidence step using the overlap integral of hypothesis posteriors. Plots the AMBIG probability curve. Reports when P(AMBIG) crosses below the resolution threshold.
- `InvU.C3.c`: `IndependenceTester` — Tests pairwise independence of evidence items using mutual information. Reports dependent pairs. Adjusts likelihood computation for dependent evidence using copulas or conditional models.
- `InvU.C3.d`: `InformationGainRanker` — Computes the information gain of each piece of evidence. Ranks by gain-per-cost. Outputs the release priority order (lowest gain/cost first) for evidence compression.
