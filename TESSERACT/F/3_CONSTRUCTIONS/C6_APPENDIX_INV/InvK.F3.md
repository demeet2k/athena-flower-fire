<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvK.R3.md
-->

# InvK — Flower Lens / Constructions

- `InvK.F3.a`: `RootFrequencyExtractor` — Analyzes the organism's legal activity log. Extracts the invocation frequency of each law. Computes the GCD of all frequencies (the root). Reports the root and its harmonic multiples.
- `InvK.F3.b`: `HarmonicVerifier` — For each legal operation: checks if its frequency is a harmonic of the root. Reports non-harmonic operations as potential undeclared axioms or illegal activities.
- `InvK.F3.c`: `ResonanceAnalyzer` — Computes the commutation structure of the axiom set. Identifies resonant pairs (naturally commuting laws). Tests stability by perturbing axioms and checking for resonance changes.
- `InvK.F3.d`: `NormalizationRunner` — Applies normalization rules to each equivalence class representative. Iterates until fixed point is reached. Reports the number of iterations and any non-terminating cases.
