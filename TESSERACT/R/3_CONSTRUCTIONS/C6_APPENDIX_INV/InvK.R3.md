<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.C3.md
-->

# InvK — Fractal Lens / Constructions

- `InvK.R3.a`: `TerminalAxiomFinder` — Traverses the derivation hierarchy downward. At each level: checks for laws with no further derivation. Identifies terminal axioms. Reports the depth at which terminals are found.
- `InvK.R3.b`: `ContractionTracker` — Measures law count reduction at each level. Computes contraction ratio. Flags sub-golden levels.
- `InvK.R3.c`: `DerivationPruner` — Prunes the derivation tree from leaves to root. At each leaf: verifies derivability from remaining structure, then releases. At each node: checks if still needed, releases if not. Reports pruning progress.
- `InvK.R3.d`: `ProtocolVerifier` — Compares distillation protocol at each level. Reports deviations.
