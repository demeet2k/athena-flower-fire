<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvY.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvY.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvY.R1.md
-->

# InvY — Cloud Lens / Objects

- `InvY.C1.a`: `ShutdownProbabilityModel` — The probabilistic model of shutdown outcomes: P(clean_shutdown), P(partial_drain), P(resource_leak), P(data_loss). The Cloud view treats shutdown as a stochastic process with these four outcome categories.
- `InvY.C1.b`: `IncidentExclusion` — The inclusion-exclusion count of shutdown incidents: total incidents minus false alarms minus already-resolved minus duplicates = genuine remaining incidents. Drives the priority queue for shutdown remediation.
- `InvY.C1.c`: `IndependentDrainProduct` — If execution slots drain independently (no shared state), the probability of complete drain = Π P(slot_i drained). The Cloud view factorizes the drain process into independent components and multiplies their success probabilities.
- `InvY.C1.d`: `ResidualRiskNormalization` — Normalizes residual risks by dividing each risk probability by total risk mass. The resulting distribution identifies which residuals are most likely to block shutdown. Resources are reclaimed in order of descending normalized risk.
