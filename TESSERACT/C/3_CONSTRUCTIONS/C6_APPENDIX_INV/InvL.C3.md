<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.R3.md
-->

# InvL — Cloud Lens / Constructions

- `InvL.C3.a`: `PosteriorSealer` — Computes the final posterior for each Bayesian process. Stores the posterior parameters (sufficient statistics). Discards individual evidence items. Verifies posterior is proper (integrates to 1).
- `InvL.C3.b`: `ExactCounter` — Verifies each inclusion-exclusion result is exact. Reports any approximate counts requiring refinement. Stores exact counts in the seed.
- `InvL.C3.c`: `IndependenceGraphBuilder` — Constructs the factorization graph from tested independence relationships. Verifies no false independence or false dependence. Stores the graph in the seed.
- `InvL.C3.d`: `NormalizationVerifier` — Checks that all normalized distributions sum/integrate to 1. Reports any deviations. Corrects any rounding errors.
