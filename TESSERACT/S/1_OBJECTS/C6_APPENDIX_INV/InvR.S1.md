<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvR.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvR.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvR.R1.md
-->

# InvR — Square Lens / Objects

- `InvR.S1.a`: `CorridorSealant` — The discrete operation of sealing an open corridor. A corridor that was conditionally open (passable if truth condition holds) is evaluated once and for all: if the condition is true, the corridor becomes an unconditional passage (always open, no gate check needed); if false, the corridor is permanently closed (bricked shut, never traversable again).
- `InvR.S1.b`: `TruthDifferenceFlattener` — The difference between conditional truth (truth under assumptions) and unconditional truth (truth simpliciter). Compression eliminates the conditional layer: every `if A then B` is resolved to either `B` (if A is true) or `¬B` (if A is false). The truth lattice flattens from a Heyting algebra to a Boolean algebra.
- `InvR.S1.c`: `GateProductCollapse` — Each corridor has a gate (a Boolean guard). The product of all gates across all corridors = the system's total access control state. Collapsing gates means evaluating the product: AND of all gate conditions. If the product is true, all corridors are simultaneously open. If any gate is false, the product is false and that corridor is sealed.
- `InvR.S1.d`: `AdmissibilityQuotient` — The ratio of admissible corridors (gate = true) to total corridors = the admissibility quotient. This measures the fraction of the truth lattice that is "passable." In the seed, only admissible corridors survive; inadmissible ones are pruned entirely.
