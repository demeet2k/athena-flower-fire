<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvR.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvR.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvR.C2.md
-->

# InvR — Fractal Lens / Laws

- `InvR.R2.a`: `InnermostFirstLaw` — Innermost conditions must be evaluated before outer ones. No outer condition can be resolved while its inner conditions are still symbolic.
- `InvR.R2.b`: `DepthContractionLaw` — Each evaluation level must reduce nesting depth by exactly 1. No level may be skipped or new nesting created.
- `InvR.R2.c`: `LeafFirstCollapseLaw` — Leaf corridors are sealed before parent corridors. No parent corridor is sealed while any child corridor remains dynamic.
- `InvR.R2.d`: `ProtocolInvarianceLaw` — The evaluation protocol must be identical at every nesting level.
