<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.R3.md
-->

# InvZ — Flower Lens / Constructions

- `InvZ.F3.a`: `FundamentalExtractor` — Computes the fundamental frequency by finding the GCD of all organism frequencies. Uses continued-fraction approximation for irrational ratios. Output: a single frequency value (or transcendental certificate) that encodes the organism's tonal identity.
- `InvZ.F3.b`: `PhaseRatioEncoder` — Converts all absolute phase angles to relative ratios referenced to the fundamental phase. Encodes as a compact vector of rational (or algebraic) numbers. Decoding restores all absolute phases given the fundamental.
- `InvZ.F3.c`: `EulerProductCondenser` — Folds the full Euler product `Π_p(1 - p^{-s})^{-1}` into its zeta-value at the organism's characteristic exponent s. The condensed value carries all prime-mode information implicitly.
- `InvZ.F3.d`: `SeriesLimitSealer` — For each harmonic series in the organism, computes and certifies the limit value. Stores limits as a compressed vector in the seed. Partial sums are discarded; only final values survive crown collapse.
