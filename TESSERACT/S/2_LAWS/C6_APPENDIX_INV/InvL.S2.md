<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvL.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvL.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvL.R2.md
-->

# InvL — Square Lens / Laws

- `InvL.S2.a`: `AdditiveCompleteness` — Every additive operation in the organism must trace back to the successor seed. If any additive operation cannot be derived from `n ↦ n+1` via the expansion grammar, it indicates an undeclared addition primitive — a violation.
- `InvL.S2.b`: `SubtractiveCompleteness` — Every subtractive/zero-detecting operation must trace back to the difference seed. Orphaned differences (not derivable from Δ) indicate undeclared primitives.
- `InvL.S2.c`: `MultiplicativeCompleteness` — Every multiplicative/binding operation must trace back to the product seed. Orphaned products indicate undeclared composition.
- `InvL.S2.d`: `DivisiveCompleteness` — Every division/inversion/normalization must trace back to the quotient seed with its admissibility gate. Ungated divisions are illegal — they must be traced to explicit gate certificates.
