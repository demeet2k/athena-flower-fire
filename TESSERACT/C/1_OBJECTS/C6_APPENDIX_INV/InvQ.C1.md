<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvQ.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvQ.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvQ.R1.md
-->

# InvQ — Cloud Lens / Objects

- `InvQ.C1.a`: `CouplingStrengthDistribution` — The statistical distribution of coupling strengths across the topology. Strong couplings are essential (hard to remove); weak couplings are candidates for removal. The distribution's tail governs the contraction aggressiveness.
- `InvQ.C1.b`: `TopologicalRobustnessEstimate` — The probability that the topology remains connected after removing k random couplings. High robustness means many couplings are redundant. Low robustness means the topology is fragile and contraction must be careful.
- `InvQ.C1.c`: `IndependentComponentProduct` — If the topology decomposes into independent components (no coupling between them), contraction can proceed independently per component with P(all contracted) = Π P(component_i contracted).
- `InvQ.C1.d`: `ContractionCostNormalization` — The cost of removing each coupling (information loss risk) normalized by the benefit (complexity reduction). High benefit/low cost couplings are removed first.
