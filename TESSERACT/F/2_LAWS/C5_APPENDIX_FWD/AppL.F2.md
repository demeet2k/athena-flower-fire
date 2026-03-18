<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppL.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppL.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppL.R2.md
-->

# AppL — Flower Lens / Laws

- `AppL.F2.a`: `SearchWaveCausalityLaw` — The evidence search wave propagates at speed `v ≤ 1` shell per time step. No shard is queried before the wave front arrives; evidence gathering respects the crystal's causal structure.
- `AppL.F2.b`: `HypothesisTestMonotonicity` — After each hypothesis test cycle, the total uncertainty `H = -Σ w_i log w_i` (Shannon entropy of candidate weights) must decrease or remain constant. Evidence never increases ambiguity; it can only reduce or preserve it.
- `AppL.F2.c`: `ScheduleOptimalityLaw` — The evidence gathering schedule must be locally optimal: no reordering of two adjacent evidence items `e_i, e_{i+1}` would reduce the expected total gathering time. Global optimality is not required, but local optimality is enforced.
- `AppL.F2.d`: `CascadeTerminationLaw` — Every promotion cascade must terminate within `L_max` steps (bounded by the crystal's longest dependency chain). Infinite cascades are impossible because the candidate set is finite and each promotion strictly reduces the global ambiguity count.
