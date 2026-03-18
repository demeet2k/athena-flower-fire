<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvL.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvL.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvL.R1.md
-->

# InvL — Cloud Lens / Objects

- `InvL.C1.a`: `BayesianAccumulationSeal` — All Bayesian evidence accumulation (counting processes, empirical frequencies, occupancy growth) is sealed at its posterior distribution. The prior + all evidence = posterior. Only the posterior survives into the seed; the individual evidence items are discarded.
- `InvL.C1.b`: `InclusionExclusionResult` — All inclusion-exclusion computations are sealed at their final counts. The alternating-sum process is discarded; only the exact count remains. Coprime densities, overcounting corrections — all collapsed to their final numbers.
- `InvL.C1.c`: `IndependenceStructureSeal` — The organism's independence structure (which events/variables are independent) is sealed as a factorization graph. The graph encodes which probability distributions factorize and which do not. This is the seed's probabilistic skeleton.
- `InvL.C1.d`: `NormalizationConstantSeal` — All normalization operations (dividing by partition functions, normalizing densities) are sealed at their final normalized values. The normalization constants are discarded; only the normalized probabilities survive.
