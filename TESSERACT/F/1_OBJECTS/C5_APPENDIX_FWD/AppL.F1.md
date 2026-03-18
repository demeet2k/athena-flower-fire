<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppL.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppL.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppL.R1.md
-->

# AppL — Flower Lens / Objects

- `AppL.F1.a`: `EvidenceSearchWave` — A propagating search front that expands outward from an ambiguous result, querying neighboring shards for evidence relevant to the candidate set. The wave carries the current candidate weights and returns with updated evidence from each shard it visits.
- `AppL.F1.b`: `HypothesisTestCycle` — The iterative cycle `Hypothesize → Predict → Observe → Update` applied to each candidate: generate a prediction `p_i` from candidate `c_i`, observe the actual value `o`, and update the candidate's weight via `w_i ∝ P(o | c_i) · w_i`.
- `AppL.F1.c`: `EvidenceGatheringSchedule` — The time-ordered plan `[t_1: gather(e_1), t_2: gather(e_2), ...]` specifying when each evidence item should be collected, optimized for minimum total time while respecting dependency ordering (some evidence requires prior evidence to be available).
- `AppL.F1.d`: `PromotionCascade` — The chain reaction triggered when one candidate's promotion resolves dependencies for other ambiguous results, causing a cascade of promotions: resolving `c_1` at address `A_1` provides the evidence needed to resolve `c_2` at `A_2`, and so on.
