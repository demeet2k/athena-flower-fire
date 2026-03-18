<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvM.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvM.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvM.R1.md
-->

# InvM — Cloud Lens / Objects

- `InvM.C1.a`: `DeadEntryProbability` — The probability that a given entry is dead (unreachable), estimated from reference patterns before the full reachability scan. High-probability dead entries are pruned first (fail-fast). Low-probability entries receive full reachability analysis.
- `InvM.C1.b`: `AttributeRedundancyEstimate` — The estimated redundancy of each profile attribute, computed from mutual information with other attributes. High mutual information means the attribute is predictable from others — it is redundant and can be removed.
- `InvM.C1.c`: `IndependentEntryPruning` — If entries are independent (no cross-references), pruning decisions can be made independently: P(all correctly pruned) = Π P(entry_i correctly pruned). Independence allows parallel pruning.
- `InvM.C1.d`: `PruningFalsePositiveRate` — The probability of falsely pruning a live entry (Type I error). Must be below the declared tolerance. Conservative reachability analysis keeps this rate low at the cost of retaining some dead entries.
