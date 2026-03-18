<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.C3.md
-->

# InvT — Fractal Lens / Constructions

- `InvT.R3.a`: `RecursiveResolver` — Traverses the conflict tree depth-first. At each leaf: resolves the atomic conflict. At each node: aggregates child resolutions and resolves the node conflict. Reports total depth, total conflicts, and resolution path.
- `InvT.R3.b`: `DepthTracker` — Monitors quarantine depth at each resolution step. Verifies strict decrease. Reports the depth sequence and flags any anomalies.
- `InvT.R3.c`: `IntegrationVerifier` — After each leaf resolution, checks all ancestors for new conflicts. If any arise, rolls back the leaf resolution and reports the incompatibility.
- `InvT.R3.d`: `ProtocolConsistencyChecker` — Compares the reconciliation protocol at each depth. Reports any depth-specific deviations. Confirms fixed-point property.
