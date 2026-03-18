<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.R3.md
-->

# AppJ — Flower Lens / Constructions

- `AppJ.F3.a`: `WavePropagator` — The engine that computes residual wave propagation from a `NEAR-FAIL` source, applying the attenuation law `δ_0/r²` to determine induced residuals at each neighbor, and updating the ledger with the new `NEAR-OK` entries.
- `AppJ.F3.b`: `FunnelTracker` — The monitor that tracks each `NEAR-OK` residual's convergence funnel, measuring the contraction rate `η` at each cycle, and escalating to `NEAR-FAIL` if `η` drops below the minimum threshold for `k` consecutive cycles.
- `AppJ.F3.c`: `ResonanceBreaker` — The intervention engine that detects residual resonance between `NEAR-AMBIG` pairs, injects disambiguating evidence (from AppL evidence plans), and forces decoupling by boosting the leading candidate's weight.
- `AppJ.F3.d`: `RepairFlowSolver` — The gradient descent engine that follows the `∇δ` flow field to determine the optimal repair ordering: which residuals to fix first to maximize total `δ` reduction per repair operation.
