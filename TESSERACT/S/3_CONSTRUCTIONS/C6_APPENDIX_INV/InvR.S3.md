<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.R3.md
-->

# InvR — Square Lens / Constructions

- `InvR.S3.a`: `GateEvaluator` — For each corridor: evaluates the gate condition in the current state. Emits true (corridor becomes unconditional passage) or false (corridor is sealed). Records the evaluation result and the state it was evaluated in.
- `InvR.S3.b`: `TruthFlattener` — Traverses the truth lattice converting every conditional to an unconditional. For each `if A then B`: evaluates A, substitutes the result, and simplifies. Output: a flat Boolean lattice with no remaining conditionals.
- `InvR.S3.c`: `GateProductComputer` — Computes the AND of all gate conditions. Reports the product and identifies any false gates (sealed corridors). Provides the list of admissible corridors.
- `InvR.S3.d`: `CorridorPruner` — Removes all inadmissible corridors from the lattice. Records each pruned corridor in the manifest (ID, gate condition, evaluation result). The pruned lattice contains only unconditionally open passages.
