<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvM.R3.md
-->

# InvM — Flower Lens / Constructions

- `InvM.F3.a`: `EntropyTracker` — Computes the registry's information entropy at each pruning step. Verifies monotone decrease. Reports the entropy curve and projected final entropy.
- `InvM.F3.b`: `BandlimitFilter` — Applies a low-pass filter to each profile's attribute waveform. Retains frequencies below the Nyquist cutoff. Verifies fidelity by comparing the filtered profile against the original at the grammar's resolution.
- `InvM.F3.c`: `EnvelopeExtractor` — Computes the version history envelope. Extracts the final value and slope. Tests sufficiency by predicting the next state and comparing against the actual next state (if available).
- `InvM.F3.d`: `ConvergenceMonitor` — Tracks registry information at each step. Computes convergence ratio. Reports the rate and identifies any sub-geometric steps for investigation.
