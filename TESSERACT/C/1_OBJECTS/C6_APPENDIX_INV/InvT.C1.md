<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvT.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvT.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvT.R1.md
-->

# InvT — Cloud Lens / Objects

- `InvT.C1.a`: `ReintegrationSuccessProbability` — The probability that a quarantined entity successfully reintegrates, estimated from historical data and the specific conflict type. High probability entities are fast-tracked; low probability entities receive additional attention.
- `InvT.C1.b`: `ConflictRecurrenceExclusion` — The probability that a resolved conflict recurs is estimated by inclusion-exclusion over known recurrence causes. P(recurrence) = P(cause₁) + P(cause₂) - P(cause₁∩cause₂) + ... This estimate governs the monitoring intensity after reintegration.
- `InvT.C1.c`: `IndependentHealingProduct` — If quarantined entities are independent (no shared conflict cause), their healing can proceed in parallel with P(all healed) = Π P(entity_i healed). Independence allows parallel processing.
- `InvT.C1.d`: `RiskNormalizedReintegration` — Reintegration risk is normalized by dividing each entity's recurrence probability by total reintegration risk mass. High normalized risk entities get extended monitoring; low normalized risk entities are released with standard monitoring.
