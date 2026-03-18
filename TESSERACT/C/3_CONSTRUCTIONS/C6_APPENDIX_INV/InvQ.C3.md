<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.R3.md
-->

# InvQ — Cloud Lens / Constructions

- `InvQ.C3.a`: `StrengthRanker` — Measures the strength of each coupling. Ranks by ascending strength. Outputs the removal priority order.
- `InvQ.C3.b`: `RobustnessTester` — Simulates the removal of k couplings and tests connectivity. Reports the robustness curve (robustness vs. k). Identifies the critical removal count where robustness drops below threshold.
- `InvQ.C3.c`: `ComponentDetector` — Identifies independent components using connected-component analysis on the coupling graph. Reports component boundaries and inter-component couplings.
- `InvQ.C3.d`: `ContractionOptimizer` — Computes the optimal contraction strategy using cost-benefit analysis. Outputs the recommended removal set and expected complexity reduction.
