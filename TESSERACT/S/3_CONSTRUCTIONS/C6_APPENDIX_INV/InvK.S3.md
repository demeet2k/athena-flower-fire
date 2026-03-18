<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.R3.md
-->

# InvK — Square Lens / Constructions

- `InvK.S3.a`: `IndependenceChecker` — For each axiom in the candidate set: attempts to derive it from the remaining axioms. If derivable, reclassifies it as a theorem and removes it from the axiom set. Iterates until no further reduction is possible. Reports the minimal axiom set.
- `InvK.S3.b`: `EquivalenceReducer` — Starting from the full equivalence structure, iteratively removes derivable equivalences. For each candidate removal: checks if the remaining equivalences still generate the full structure. If yes, the equivalence is redundant. Reports the generating set.
- `InvK.S3.c`: `BudgetCollapser` — Analyzes the axiom set's commutativity properties. Derives the implied commutation budget from these properties. Compares against the original expanded budget. Reports consistency.
- `InvK.S3.d`: `NormalFormSelector` — For each equivalence class: selects the canonical representative using a declared normal-form criterion (e.g., lexicographic smallest, shortest derivation, most symmetric). Verifies uniqueness. Reports the quotient space.
