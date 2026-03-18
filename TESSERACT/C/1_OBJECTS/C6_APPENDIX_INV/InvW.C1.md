<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvW.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvW.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvW.R1.md
-->

# InvW — Cloud Lens / Objects

- `InvW.C1.a`: `ContainerCorruptionPrior` — The prior probability that a container is corrupted, estimated from historical data. The Cloud view: before opening any container, we have a base rate of corruption to expect. This prior governs how aggressively we verify.
- `InvW.C1.b`: `LayerIndependenceTest` — The statistical test for whether container layers are independent (no shared mutable state). If independent, unwinding can proceed in parallel. If dependent, sequential unwinding is required.
- `InvW.C1.c`: `ParallelUnwindProduct` — If layers are independent, P(successful unwind) = Π P(layer_i unwound). The factorized product gives the overall success probability, which must exceed the organism's reliability threshold.
- `InvW.C1.d`: `CostBenefitRatio` — The ratio of verification cost to corruption risk. When the ratio is high (expensive verification, low risk), sampling-based verification is preferred. When low (cheap verification, high risk), full verification is preferred.
