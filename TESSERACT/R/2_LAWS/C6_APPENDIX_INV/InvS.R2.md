<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvS.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvS.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvS.C2.md
-->

# InvS — Fractal Lens / Laws

- `InvS.R2.a`: `BottomUpAbsorptionLaw` — Sub-cell residuals must be absorbed before cell residuals. Cell residuals before shell residuals. Shell residuals before global. No level is absorbed until all its children are exact.
- `InvS.R2.b`: `HierarchicalConsistencyLaw` — Completing a lower-level NEAR must not create a new residual at a higher level. If it does, the completion is inconsistent and must be revised.
- `InvS.R2.c`: `MonotoneTreeCollapseLaw` — The residual tree must collapse monotonically: the number of non-zero residuals decreases at each step. Any increase indicates an absorption error.
- `InvS.R2.d`: `ProtocolFixedPointLaw` — The absorption protocol must be identical at every level. Level-specific protocols indicate inconsistency.
