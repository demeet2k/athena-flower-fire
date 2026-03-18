<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.R3.md
-->

# InvW — Cloud Lens / Constructions

- `InvW.C3.a`: `CorruptionPriorEstimator` — Estimates the corruption prior from historical container data. Uses Bayesian updating: prior × likelihood(current_evidence) = posterior. Outputs the posterior corruption probability.
- `InvW.C3.b`: `IndependenceTester` — Tests layer independence by checking for shared mutable state (shared files, shared memory regions, shared configuration). Reports the test statistic and p-value.
- `InvW.C3.c`: `SuccessProbabilityCalculator` — Computes Π P(layer_i unwound) from individual layer success probabilities. Identifies the weakest layer (lowest individual probability) and recommends remediation.
- `InvW.C3.d`: `VerificationOptimizer` — Computes the optimal verification strategy by minimizing expected total cost. Outputs the recommended intensity and method (full scan, sampling, or trust-based).
