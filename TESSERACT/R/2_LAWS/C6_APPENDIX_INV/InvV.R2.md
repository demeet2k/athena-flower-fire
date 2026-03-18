<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvV.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvV.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvV.C2.md
-->

# InvV — Fractal Lens / Laws

- `InvV.R2.a`: `BottomUpSummaryLaw` — Sub-replays must be summarized before their parents. A parent summary that references un-summarized children is invalid. Bottom-up order is mandatory.
- `InvV.R2.b`: `GeometricContractionLaw` — Each nesting level must reduce verification burden by at least factor 1/φ. If a sub-replay is as complex as its parent, the nesting structure is degenerate and must be refactored.
- `InvV.R2.c`: `LeafFirstPruningLaw` — Capsule tree pruning must proceed leaf-first. No parent capsule is released until all its children have been absorbed. This ensures the root attestation correctly reflects all leaf verifications.
- `InvV.R2.d`: `ProtocolFixedPointLaw` — The verification protocol must be identical at every recursion level. Level-specific protocols indicate structural inconsistency.
