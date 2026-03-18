<!-- TESSERACT: F/1_OBJECTS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=F facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvV.S1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvV.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvV.R1.md
-->

# InvV — Flower Lens / Objects

- `InvV.F1.a`: `ExecutionWaveformSummary` — The continuous waveform of execution (state evolving over time) is summarized by its envelope: amplitude (peak state deviation), frequency (oscillation rate), and phase (timing offset). The envelope replaces the full waveform — compression through spectral summary.
- `InvV.F1.b`: `VerificationDampingCurve` — As more verification capsules are composed, the uncertainty about correctness dampens exponentially. Each capsule reduces remaining doubt by a factor. The damping curve shows how confidence grows as capsules accumulate — and in reversal, how quickly it can be released.
- `InvV.F1.c`: `ReplayHarmonicDecomposition` — The replay trace decomposed into harmonic components: fundamental (the main computation), first overtone (error correction), second overtone (environmental adaptation), higher overtones (noise). Compression discards noise overtones and retains signal harmonics.
- `InvV.F1.d`: `ConvergenceToAttestation` — The replay's output sequence converges to a fixed-point attestation. The convergence rate measures how quickly the replay stabilizes. Fast convergence = the replay quickly reaches its conclusion. Slow convergence = the replay has long transient behavior that compresses poorly.
