<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvV.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvV.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvV.R2.md
-->

# InvV — Flower Lens / Laws

- `InvV.F2.a`: `SpectralSufficiencyLaw` — The envelope (amplitude, frequency, phase) must be sufficient to reconstruct the waveform within declared tolerance. If not sufficient, additional spectral components must be retained until sufficiency is achieved.
- `InvV.F2.b`: `MonotonicConfidenceLaw` — Confidence must monotonically increase as capsules are composed. Any capsule that decreases confidence indicates a verification inconsistency and must be quarantined.
- `InvV.F2.c`: `SignalPreservationLaw` — Harmonic compression must preserve all signal components (fundamental + overtones up to the declared cutoff). Only noise above the cutoff may be discarded. The cutoff must be declared explicitly.
- `InvV.F2.d`: `ConvergenceRateBoundLaw` — The convergence rate must be at least geometric (ratio ≤ 1/φ per step). Sub-geometric convergence indicates a replay that is too long or too complex for efficient compression.
