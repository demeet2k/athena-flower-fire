<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvW.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvW.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvW.C2.md
-->

# InvW — Fractal Lens / Laws

- `InvW.R2.a`: `DepthFirstUnwindingLaw` — Recursive unwinding must proceed depth-first: unwind the deepest nested container before its parent. This prevents accessing content through a partially-unwound wrapper.
- `InvW.R2.b`: `AcceleratingContractionLaw` — Each level must reduce nesting depth by exactly 1. No level may skip depths or create new nesting. The contraction is strict and monotone.
- `InvW.R2.c`: `FiniteNestingLaw` — Total nesting depth must be finite and bounded by the organism's declared recursion limit. Infinitely nested containers are rejected as malformed.
- `InvW.R2.d`: `ProtocolInvarianceLaw` — The unwinding protocol must be identical at every nesting level. Level-specific behavior indicates a format inconsistency that must be resolved.
