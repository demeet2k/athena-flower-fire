<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.R3.md
-->

# InvU — Flower Lens / Constructions

- `InvU.F3.a`: `WaveCollapser` — Tracks the evidence probability amplitude over time. At each new piece of evidence: updates the amplitude by interference. When the amplitude for one outcome exceeds the threshold, collapses the wave and emits the verdict.
- `InvU.F3.b`: `AmbiguityDamper` — Monitors the ambiguity level after each piece of evidence. Plots the damping curve. Flags any non-monotone step (ambiguity increase). Reports the current damping rate and projected evidence needed for threshold.
- `InvU.F3.c`: `ResonanceDetector` — Identifies independent evidence sources that agree. Computes the resonance factor. Applies bounded amplification to the combined credibility. Reports which source combinations are resonant.
- `InvU.F3.d`: `ConvergenceAnalyzer` — Computes the convergence ratio of the evidence sequence. Classifies as fast (ratio < 1/φ²), adequate (ratio ∈ [1/φ², 1/φ]), or slow (ratio > 1/φ). Recommends investigation strategy based on convergence quality.
