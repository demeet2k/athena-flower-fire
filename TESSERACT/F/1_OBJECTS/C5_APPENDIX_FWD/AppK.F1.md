<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppK.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppK.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppK.R1.md
-->

# AppK — Flower Lens / Objects

- `AppK.F1.a`: `ConflictAmplificationChain` — A dynamic sequence where conflict `C_1` at address `A_1` triggers conflict `C_2` at dependent address `A_2`, which triggers `C_3` at `A_3`, forming a causal chain of escalating contradictions that must be halted before reaching critical mass.
- `AppK.F1.b`: `ConflictCancellationPair` — Two conflicts that mutually neutralize: `C_+` (a positive deviation) and `C_-` (a negative deviation) at nearby addresses whose combined effect is zero. Detected by checking if `Δ_+(C_+) + Δ_-(C_-) = 0` within tolerance.
- `AppK.F1.c`: `QuarantineDecayFunction` — The time-dependent function `Q(t) = Q_0 · e^{-t/τ}` governing how quarantine severity relaxes over time as the conflict is investigated. Starts at full isolation `Q_0 = 1` and decays toward supervised access as evidence of resolution accumulates.
- `AppK.F1.d`: `ConflictWaveFront` — The expanding boundary of a conflict's influence zone, propagating at speed `v ≤ 1` shell per time step through the dependency graph. Shards inside the wave front are pre-quarantined; those outside are safe.
