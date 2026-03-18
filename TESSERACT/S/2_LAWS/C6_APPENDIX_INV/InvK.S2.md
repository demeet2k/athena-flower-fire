<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvK.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvK.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvK.R2.md
-->

# InvK — Square Lens / Laws

- `InvK.S2.a`: `AxiomMinimalityLaw` — The axiom set must be minimal: no axiom can be derived from the others. An axiom that follows from the remaining axioms is redundant and must be classified as a theorem. Minimality ensures the seed carries no redundant legal weight.
- `InvK.S2.b`: `EquivalenceGenerationLaw` — Every equivalence in the organism must be derivable from the generating equivalences via the inference rules (reflexivity, symmetry, transitivity). Any underivable equivalence indicates a missing axiom.
- `InvK.S2.c`: `CommutationConsistencyLaw` — The collapsed commutation budget must be consistent with the axiom set's actual commutativity. If the axioms commute more (or less) than the budget allows, the budget is incorrectly collapsed.
- `InvK.S2.d`: `NormalFormUniquenessLaw` — Each equivalence class must have exactly one normal-form representative. Multiple representatives indicate an incomplete normalization procedure. Zero representatives indicate a missing class.
