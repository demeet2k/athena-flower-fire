<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.C3.md
-->

# AppB — Fractal Lens / Constructions

- `AppB.R3.a`: `MetaLawVerifier` — The second-order verifier that checks whether the set of active conservation laws has cardinality exactly 6, independence rank exactly 6, and no redundant or missing members, using the crystal's own transport structure as test cases.
- `AppB.R3.b`: `KernelCompressor` — The compressor that takes the six conservation laws in expanded form and computes their joint kernel representation `ker(T)`, verifying that the kernel is a proper subgroup of the path group with the correct index.
- `AppB.R3.c`: `ConfluenceChecker` — The construction that tests the Church-Rosser property of the reduction system by generating all critical pairs of overlapping reduction rules and verifying that each pair converges to the same normal form.
- `AppB.R3.d`: `CircularWitnessChainBuilder` — The construction that builds the circular witness chain `L_1 → L_2 → ... → L_6 → L_1`, where each arrow represents "violation of `L_i` implies violation of `L_{i+1}`", closing the self-verification loop.
