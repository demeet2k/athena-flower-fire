<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvT.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvT.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvT.C1.md
-->

# InvT — Fractal Lens / Objects

- `InvT.R1.a`: `RecursiveConflictResolution` — Conflicts may be nested: resolving a top-level conflict requires resolving sub-conflicts, which may have their own sub-conflicts. Resolution is recursive: resolve the deepest sub-conflicts first, then use those resolutions to resolve parent conflicts.
- `InvT.R1.b`: `QuarantineDepthContraction` — Each level of conflict resolution reduces quarantine depth by 1. The contraction maps the multi-level quarantine structure to a flat resolved state. Deep quarantine (many nested conflicts) requires proportionally more resolution steps.
- `InvT.R1.c`: `ConflictTreeIntegration` — The conflict tree (root conflict → sub-conflicts → leaf conflicts) is integrated from leaves to root. Each leaf resolution enables its parent resolution. The tree collapses to a single resolved state when the root is resolved.
- `InvT.R1.d`: `ScaleInvariantReconciliation` — The reconciliation protocol is the same at every conflict depth: identify conflicting states, compute resolution delta, apply correction, verify compatibility, issue release token. The protocol is a fixed point of the conflict nesting.
