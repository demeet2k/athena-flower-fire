<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.R3.md
-->

# InvL — Square Lens / Constructions

- `InvL.S3.a`: `AdditiveTracer` — Traces every additive operation in the organism back to its derivation from `n ↦ n+1`. Builds the derivation tree. Reports any operations that cannot be traced (orphans). Counts the total number of additive instances and their derivation depth.
- `InvL.S3.b`: `SubtractiveTracer` — Traces every subtractive operation back to `Δ(F,G)`. Reports orphans. Identifies the organism's complete zero set as the invariant kernel preserved in the seed.
- `InvL.S3.c`: `MultiplicativeTracer` — Traces every multiplicative operation back to `A × B`. Reports orphans. Identifies the organism's complete factorization structure.
- `InvL.S3.d`: `DivisiveTracer` — Traces every division back to `[a] ⊘_Λ [b]` with its gate certificate. Reports ungated divisions. Verifies all admissibility conditions.
