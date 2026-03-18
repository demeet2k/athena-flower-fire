<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppJ.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppJ.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppJ.R2.md
-->

# AppJ — Flower Lens / Laws

- `AppJ.F2.a`: `WaveAttenuationLaw` — Residual waves attenuate with distance from the failure source: the induced `δ` at distance `r` is bounded by `δ_0 / r²` where `δ_0` is the original failure gap. Waves cannot amplify through propagation alone.
- `AppJ.F2.b`: `FunnelConvergenceLaw` — Every `NEAR-OK` convergence funnel must narrow at a rate of at least `δ(t+1) ≤ (1 - η) δ(t)` for contraction rate `η > 0`. Stalled funnels (zero convergence rate) trigger escalation to `NEAR-FAIL`.
- `AppJ.F2.c`: `ResonanceDecouplingLaw` — Residual resonance between two `NEAR-AMBIG` addresses must decouple within `T_max` cycles as evidence accumulates; perpetual oscillation is forbidden. Decoupling occurs when one candidate achieves confidence `> 1 - ε`.
- `AppJ.F2.d`: `FlowFieldIrrotationality` — The near-miss flow field `∇δ` is irrotational (curl-free) on each shell: there are no closed repair loops that cycle without reducing total residual. Every repair path leads monotonically toward lower total `δ`.
