<!-- TESSERACT: F/1_OBJECTS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=F facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvM.S1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvM.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvM.R1.md
-->

# InvM — Flower Lens / Objects

- `InvM.F1.a`: `RegistryEntropyReduction` — The registry's information entropy decreases as dead entries are removed and profiles are minimized. The Flower view: the registry was a noisy signal; pruning increases the signal-to-noise ratio. The pruned registry is a cleaner, more harmonic signal.
- `InvM.F1.b`: `ProfileWaveformCompression` — Each profile is a waveform (a signal over attribute-space). Compression applies bandlimiting: high-frequency attribute variations (minor details) are removed, retaining only low-frequency content (essential characteristics). The compressed waveform faithfully represents the profile's essential shape.
- `InvM.F1.c`: `VersionHistoryEnvelope` — The version history is a time series. Its envelope (amplitude over time) shows the entity's evolution. Compression replaces the full time series with a single point on the envelope (the final value) plus the envelope's slope (the entity's current trajectory).
- `InvM.F1.d`: `RegistryConvergence` — As pruning and compression proceed, the registry's total information converges to its essential content. The convergence rate depends on the redundancy fraction. Highly redundant registries converge quickly; lean registries are already near their essential content.
