<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvN.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvN.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvN.C2.md
-->

# InvN — Fractal Lens / Laws

- `InvN.R2.a`: `FastestFirstHaltLaw` — The fastest sub-clock halts before slower ones. Halting a slow clock while fast clocks still run creates timing aliasing.
- `InvN.R2.b`: `ContractionCumulationLaw` — The cumulative contraction must account for all sub-clocks. Missing a sub-clock leaves residual timing activity.
- `InvN.R2.c`: `LeafFirstCollapseLaw` — Clock tree collapses leaf-first. No parent clock halts while children still tick.
- `InvN.R2.d`: `ProtocolInvarianceLaw` — Halt protocol identical at every clock level.
