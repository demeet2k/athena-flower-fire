<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppI.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppI.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppI.R1.md
-->

# AppI — Cloud Lens / Objects

- `AppI.C1.a`: `CorridorOpenProbability` — The probability that a corridor will be found open when tested. Bayesian estimate from prior corridor tests and system state.
- `AppI.C1.b`: `TruthConfidenceField` — The probability distribution over truth tags for each claim. Not a single tag but a distribution: `P(CANON) = 0.7, P(NEAR) = 0.2, P(AMBIG) = 0.1`.
- `AppI.C1.c`: `EvidenceSufficiencyScore` — The probability that current evidence is sufficient for truth promotion. Below threshold = abstain. Above threshold = promote.
- `AppI.C1.d`: `CorridorRiskField` — The probability of corridor failure (closure, singularity, budget exhaustion) for each pending operation. High risk = preemptive routing to alternatives.
