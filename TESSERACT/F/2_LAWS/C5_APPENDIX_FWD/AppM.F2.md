<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppM.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppM.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppM.R2.md
-->

# AppM — Flower Lens / Laws

- `AppM.F2.a`: `CausalOrderPreservation` — Replay must respect the causal partial order: if transition `A` causally precedes `B` in the original execution, `A` must precede `B` in every valid replay.
- `AppM.F2.b`: `TemporalReversibilityLaw` — For every forward replay step `S_i → S_{i+1}`, a reverse step exists via snapshot restoration; the system is temporally navigable in both directions at checkpoint granularity.
- `AppM.F2.c`: `ReplayConvergenceLaw` — Two replay streams starting from the same snapshot and applying the same log segment must converge to identical final states; divergence is proof of non-determinism contamination.
- `AppM.F2.d`: `ClockMonotonicityLaw` — The replay clock is strictly monotonic: `tick(S_{i+1}) > tick(S_i)` for every forward transition; no replay may produce a state with a tick value less than or equal to its predecessor.
