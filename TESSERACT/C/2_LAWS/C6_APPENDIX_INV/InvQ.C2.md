<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvQ.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvQ.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvQ.R2.md
-->

# InvQ — Cloud Lens / Laws

- `InvQ.C2.a`: `WeakFirstRemovalLaw` — Couplings must be removed in order of ascending strength: weakest first. Removing a strong coupling before weak ones risks topological damage.
- `InvQ.C2.b`: `RobustnessThresholdLaw` — The topology's robustness after contraction must exceed a declared threshold. If contraction would drop robustness below threshold, contraction is halted.
- `InvQ.C2.c`: `ComponentIndependenceLaw` — Independent contraction is only legal after component independence is verified. Coupled components must be contracted jointly.
- `InvQ.C2.d`: `OptimalContractionLaw` — The contraction strategy must minimize total cost (information loss + complexity). Neither over-contraction nor under-contraction is optimal.
