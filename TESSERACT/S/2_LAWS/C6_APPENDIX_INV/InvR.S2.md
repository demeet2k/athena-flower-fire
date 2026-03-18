<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvR.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvR.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvR.R2.md
-->

# InvR — Square Lens / Laws

- `InvR.S2.a`: `IrreversibleSealLaw` — Once a corridor is sealed (gate evaluated and committed), the evaluation cannot be undone. The seal is permanent. This converts dynamic (re-evaluable) truth conditions into static (fixed) truth values.
- `InvR.S2.b`: `FlatteningCompleteness` — Every conditional truth must be flattened to unconditional during compression. No conditional truth survives in the seed. The seed's truth lattice is Boolean: every proposition is simply true or false.
- `InvR.S2.c`: `GateEvaluationDeterminism` — Gate evaluation must be deterministic: given the same state, the same gate always produces the same Boolean value. Non-deterministic gates cannot be sealed and must be resolved (by fixing the state) before compression.
- `InvR.S2.d`: `AdmissibilityPreservationLaw` — Only admissible corridors carry information into the seed. Inadmissible corridors are pruned — their existence is recorded in the pruning manifest but their content is not preserved.
