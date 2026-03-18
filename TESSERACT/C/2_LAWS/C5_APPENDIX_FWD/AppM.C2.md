<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppM.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppM.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppM.R2.md
-->

# AppM — Cloud Lens / Laws

- `AppM.C2.a`: `SamplingCoverageLaw` — If `m` ticks are sampled uniformly from a trace of length `T`, the probability of missing a corruption event of width `w` is at most `((T-w)/T)^m`; coverage is tunable by adjusting `m`.
- `AppM.C2.b`: `DivergenceBoundLaw` — If the statistical divergence between replay and original exceeds threshold `epsilon`, the replay is rejected; the threshold is calibrated so that false-positive rate is below `alpha`.
- `AppM.C2.c`: `CheckpointEntropyLaw` — Ticks with higher state entropy receive higher checkpoint probability; this ensures that complex, high-information states are preferentially preserved for replay verification.
- `AppM.C2.d`: `ConfidenceMonotonicityLaw` — As more sampled ticks pass verification, the confidence bound tightens monotonically; confidence can never decrease with additional passing samples.
