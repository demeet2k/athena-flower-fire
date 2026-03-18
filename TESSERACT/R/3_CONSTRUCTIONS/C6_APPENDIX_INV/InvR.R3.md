<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.C3.md
-->

# InvR — Fractal Lens / Constructions

- `InvR.R3.a`: `RecursiveEvaluator` — Traverses the truth tree depth-first. At each leaf: evaluates the atomic proposition. At each node: substitutes child results and evaluates. Reports tree depth, total propositions, and evaluation path.
- `InvR.R3.b`: `DepthTracker` — Monitors nesting depth at each step. Verifies strict decrease. Reports depth sequence.
- `InvR.R3.c`: `CorridorTreeSealer` — Traverses the corridor hierarchy leaf-first. Seals each leaf, propagates result to parent, then seals parent when all children are sealed. Reports sealing order.
- `InvR.R3.d`: `ProtocolConsistencyChecker` — Verifies protocol identity at every level. Reports deviations.
