<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.R3.md
-->

# InvY — Cloud Lens / Constructions

- `InvY.C3.a`: `ShutdownSimulator` — Monte Carlo simulation of shutdown scenarios. Samples from the outcome distribution, estimates P(clean_shutdown), and reports confidence interval. If below threshold, identifies the bottleneck component.
- `InvY.C3.b`: `IncidentTriager` — Applies inclusion-exclusion to the incident log. Removes false alarms, duplicates, and already-resolved items. Outputs the genuine incident queue sorted by severity.
- `InvY.C3.c`: `IndependenceChecker` — Tests pairwise independence of execution slots by checking for shared memory, shared file handles, shared network connections. Reports dependency graph. For independent slots, computes factorized drain probability.
- `InvY.C3.d`: `RiskNormalizer` — Computes the normalized risk distribution over all residual items. Sorts by descending risk. Outputs the reclamation priority order and total residual risk mass.
