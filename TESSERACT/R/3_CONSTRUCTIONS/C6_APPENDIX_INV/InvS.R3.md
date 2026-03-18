<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.C3.md
-->

# InvS — Fractal Lens / Constructions

- `InvS.R3.a`: `HierarchicalScanner` — Scans the residual tree bottom-up. At each leaf level: computes residuals, absorbs them, and propagates the effect to parents. Reports level-by-level absorption progress.
- `InvS.R3.b`: `ConsistencyChecker` — After each lower-level completion, checks all ancestors for new residuals. Reports any inconsistencies and recommends revisions.
- `InvS.R3.c`: `TreeCollapseMonitor` — Tracks the count of non-zero residuals at each step. Verifies monotone decrease. Reports any increases as absorption errors.
- `InvS.R3.d`: `ProtocolVerifier` — Compares the absorption protocol at each level. Reports any level-specific deviations. Confirms fixed-point property.
