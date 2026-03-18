<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvM.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvM.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvM.R2.md
-->

# InvM — Cloud Lens / Laws

- `InvM.C2.a`: `FailFastPruningLaw` — Entries with highest dead-probability are pruned first. This maximizes early compression and surfaces any pruning errors quickly.
- `InvM.C2.b`: `RedundancyBeforeRemovalLaw` — An attribute may only be removed after its redundancy is statistically confirmed (mutual information with retained attributes exceeds threshold).
- `InvM.C2.c`: `IndependenceBeforeParallelLaw` — Parallel pruning only after independence is verified. Cross-referenced entries must be pruned jointly.
- `InvM.C2.d`: `FalsePositiveToleranceLaw` — False positive pruning rate must be below the declared tolerance. If the rate approaches tolerance, pruning becomes more conservative.
