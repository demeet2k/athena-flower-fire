<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvU.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvU.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvU.C1.md
-->

# InvU — Fractal Lens / Objects

- `InvU.R1.a`: `RecursiveEvidenceTree` — Evidence accumulates in a tree structure: root question → sub-questions → sub-sub-questions → leaf observations. Compression works bottom-up: leaf observations compress to sub-verdicts, which compress to verdicts, which compress to the root answer.
- `InvU.R1.b`: `AMBIGContractionChain` — Each level of the evidence tree contracts the AMBIG space by factor 1/φ. At the root, AMBIG should be negligible. The contraction chain tracks how ambiguity shrinks level by level.
- `InvU.R1.c`: `VerdictTreePruning` — After bottom-up compression, the evidence tree is pruned: leaf observations are released (their information is captured in sub-verdicts), sub-questions are released (their information is captured in verdicts). Only the root verdict survives.
- `InvU.R1.d`: `ScaleInvariantJudgment` — The judgment protocol is identical at every level: accumulate evidence, cross threshold, emit verdict. Whether judging a leaf observation or the root question, the protocol is the same — only the evidence type changes.
