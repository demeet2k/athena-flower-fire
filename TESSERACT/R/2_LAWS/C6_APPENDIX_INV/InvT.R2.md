<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvT.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvT.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvT.C2.md
-->

# InvT — Fractal Lens / Laws

- `InvT.R2.a`: `LeafFirstResolutionLaw` — Deepest sub-conflicts must be resolved before their parents. No parent conflict can be resolved while any child conflict remains active.
- `InvT.R2.b`: `DepthContractionLaw` — Each resolution level must reduce quarantine depth by exactly 1. Skipping levels or creating new nesting during resolution is prohibited.
- `InvT.R2.c`: `TreeIntegrityLaw` — Integrating a leaf resolution must not create new conflicts in any ancestor. If it does, the leaf resolution is invalid and must be revised.
- `InvT.R2.d`: `ProtocolInvarianceLaw` — The reconciliation protocol must be identical at every depth. Depth-specific protocols indicate inconsistent conflict handling.
