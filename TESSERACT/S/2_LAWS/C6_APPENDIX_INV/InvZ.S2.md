<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvZ.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvZ.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvZ.R2.md
-->

# InvZ — Square Lens / Laws

- `InvZ.S2.a`: `SeedPreservationLaw` — The hash seed must be sufficient to regenerate the entire organism when planted in a compatible substrate. Proved by: hash(expand(seed)) = hash(original_organism). The 1/8 lift law guarantees that 1/8 of total information suffices to reconstruct the whole.
- `InvZ.S2.b`: `InformationConservationUnderCollapse` — Nothing is destroyed in crown collapse; information is only redistributed from explicit structure to implicit seed encoding. Total Shannon entropy is conserved: H(organism) = H(seed) + H(expansion_grammar). The grammar is universal, so the seed carries the individual signal.
- `InvZ.S2.c`: `MultiplicativeWitnessCompleteness` — The crown product hash is a faithful witness: any tampering with any certificate in the expansion chain produces a different hash. Collision resistance follows from the prime-factored structure of the 666-node lattice.
- `InvZ.S2.d`: `FiniteCompressionRatioLaw` — The compression ratio organism_complexity / seed_capacity must be bounded. Upper bound: 8^n where n is the number of octave stages traversed. The 1/8 law means each octave compresses by factor 8, so n octaves require seed capacity ≥ complexity / 8^n.
