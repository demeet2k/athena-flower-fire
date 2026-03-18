<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppE -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppE.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppE.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppE.R1.md
-->

# AppE — Cloud Lens / Objects

- `AppE.C1.a`: `PhaseUncertaintyEnvelope` — The probability distribution over phase position when clock precision is finite. Wider envelope = less certain timing.
- `AppE.C1.b`: `ClockDriftDistribution` — The probability model for accumulated phase error over many cycles. Drift grows as `√n` for random errors (diffusive) or linearly for systematic errors.
- `AppE.C1.c`: `SynchronizationConfidence` — The probability that two clocks are phase-locked given noisy measurements. Bayesian update from successive phase-difference observations.
- `AppE.C1.d`: `ClosureProbability` — The probability that a polygon sequence has converged to π within declared tolerance at finite refinement depth.
