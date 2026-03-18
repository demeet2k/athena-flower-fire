<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvM.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvM.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvM.R1.md
-->

# InvM — Square Lens / Objects

- `InvM.S1.a`: `DeadEntryReaper` — The discrete operation of identifying and removing registry entries that are no longer referenced by any active entity. Dead entries accumulated during expansion (entities were created, used, and abandoned without deregistration). The reaper scans all cross-references and marks unreachable entries for removal.
- `InvM.S1.b`: `ProfileDelta` — The difference between a full profile (all attributes, capabilities, history) and a minimal profile (only attributes needed for seed reconstruction). The delta identifies removable attributes — those that can be recomputed from the seed's grammar rather than stored explicitly.
- `InvM.S1.c`: `VersionHistoryProduct` — The full version history of an entity is a product of all its versions: v₁ × v₂ × ... × vₙ. Compression collapses this product to a single version: the latest valid snapshot. The product's "summary" is its final state — all intermediate states are implicit in the grammar.
- `InvM.S1.d`: `RegistryCompressionQuotient` — The ratio of compressed registry size to full registry size = the compression quotient. A quotient of 0.1 means 90% of the registry was prunable. The quotient measures how much of the registry was essential vs. accumulated baggage.
