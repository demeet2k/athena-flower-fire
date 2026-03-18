<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.R3.md
-->

# InvN — Cloud Lens / Constructions

- `InvN.C3.a`: `JitterAnalyzer` — Measures jitter distribution over the final N beats before freeze. Fits to a distribution model. Reports mean, variance, skewness. Verifies within bound.
- `InvN.C3.b`: `SlipDetector` — Monitors gear tooth engagement during the final deceleration. Detects any missed engagements. Reports slip count and probability. Flags gears requiring independent verification.
- `InvN.C3.c`: `IndependenceTester` — Tests wheel independence by checking for shared oscillator, shared power supply, or correlated halt times. Reports the dependency structure.
- `InvN.C3.d`: `PrecisionCalculator` — Computes the effective precision from the jitter distribution and clock resolution. Reports the number of significant timing digits. Compares against the seed's requirements.
