<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.C3.md
-->

# AppL — Fractal Lens / Constructions

- `AppL.R3.a`: `SelfWitnessingHarness` — The harness that instruments a computation to produce its own correctness witness as a side effect, by logging each intermediate state, checking invariants at each step, and packaging the trace as a verifiable witness bundle.
- `AppL.R3.b`: `AdaptivePlanBuilder` — The builder that constructs the proof plan incrementally: executes `Step_1` to generate `Step_2`, executes `Step_2` to generate `Step_3`, and so on, adapting each step to the evidence gathered in the previous step, until the plan is complete or the budget is exhausted.
- `AppL.R3.c`: `EvidenceAmplificationEngine` — The engine that implements recursive evidence amplification: takes initial weak evidence, applies the amplification function `g` at each recursive level, tracks the strength trajectory, and terminates when the ceiling is reached or the target strength is achieved.
- `AppL.R3.d`: `FixedPointPromotionEngine` — The engine that drives the autonomous promotion loop to its fixed point: iterates the promote-and-strengthen cycle, monitors convergence via `|Result_{n+1} - Result_n|`, and declares stable promotion when the difference drops below `ε_stable`.
