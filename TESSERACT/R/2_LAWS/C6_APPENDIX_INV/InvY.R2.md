<!-- TESSERACT: R/2_LAWS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=R facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvY.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvY.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvY.C2.md
-->

# InvY — Fractal Lens / Laws

- `InvY.R2.a`: `LeafFirstShutdownLaw` — Recursive shutdown must proceed leaf-first (bottom-up). No parent deployment shuts down before all its children have certified completion. This prevents orphaned processes.
- `InvY.R2.b`: `ContractionBoundLaw` — Each recursive step must reduce total deployment size by at least factor 1/φ. If a step fails to contract, it indicates a stuck sub-deployment that must be individually investigated.
- `InvY.R2.c`: `PruningIntegrityLaw` — Pruning a branch must release exactly the resources that branch consumed. Over-release indicates accounting error; under-release indicates leak. Both are flagged.
- `InvY.R2.d`: `ScaleInvarianceLaw` — The shutdown protocol must produce identical certificates at every scale. A process-level shutdown cert and a cluster-level shutdown cert must have the same structure, differing only in the scale parameter.
