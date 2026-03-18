<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.R3.md
-->

# InvV — Flower Lens / Constructions

- `InvV.F3.a`: `EnvelopeExtractor` — Computes the execution waveform envelope by tracking amplitude, frequency, and phase over time. Uses Hilbert transform for instantaneous amplitude and frequency. Output: the three-component envelope summary.
- `InvV.F3.b`: `ConfidenceTracker` — Tracks confidence level as each capsule is composed. Plots the damping curve. Flags any non-monotone step. Reports final confidence level and the number of capsules needed to reach the target.
- `InvV.F3.c`: `HarmonicFilter` — Decomposes the replay trace via FFT (or wavelet transform). Identifies fundamental and overtone components. Applies the declared cutoff. Output: the signal-only trace (noise removed) and the noise floor estimate.
- `InvV.F3.d`: `ConvergenceDetector` — Monitors the output sequence for convergence. Computes the convergence ratio at each step. Declares convergence when the ratio stabilizes below 1/φ. Output: the fixed-point attestation and the convergence step count.
