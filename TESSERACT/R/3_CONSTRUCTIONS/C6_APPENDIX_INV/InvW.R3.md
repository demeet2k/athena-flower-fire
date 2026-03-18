<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.C3.md
-->

# InvW — Fractal Lens / Constructions

- `InvW.R3.a`: `DepthFirstUnwinder` — Traverses the container tree depth-first. At each leaf: unwraps the atomic content. At each internal node: validates, flushes, peels, reconciles, then exposes children. Reports total depth, total nodes, and any malformed levels.
- `InvW.R3.b`: `DepthTracker` — Monitors nesting depth at each step. Verifies strict monotone decrease. Reports the depth sequence and flags any anomalies.
- `InvW.R3.c`: `NestingBoundChecker` — Verifies total nesting depth is within the declared bound before beginning unwinding. Rejects containers exceeding the bound. Reports actual depth vs. limit.
- `InvW.R3.d`: `ProtocolVerifier` — Compares the operation sequence at each nesting level. Reports any deviations from the canonical protocol. Flags level-specific behavior for investigation.
