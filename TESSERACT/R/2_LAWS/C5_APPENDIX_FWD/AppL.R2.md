<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppL.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppL.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppL.C2.md
-->

# AppL — Fractal Lens / Laws

- `AppL.R2.a`: `SelfWitnessingSoundnessLaw` — A self-generating witness is sound only if the system's correctness implies the witness's validity AND the witness's validity implies the system's correctness. The biconditional `correct ↔ valid_witness` must hold; one-directional implication is insufficient.
- `AppL.R2.b`: `BootstrapTerminationLaw` — Every bootstrapped proof plan must terminate: the self-generating step `Step_1` produces a finite plan `Steps_2..n` with `n < N_max`. Proof plans that generate infinitely long proof plans are forbidden; the bootstrap must converge.
- `AppL.R2.c`: `AmplificationConvergenceLaw` — The recursive evidence amplifier must converge: `g^n(strength_0) → strength_max < ∞` as `n → ∞`. Unbounded amplification would manufacture certainty from nothing; the amplifier has a ceiling imposed by the crystal's information-theoretic limits.
- `AppL.R2.d`: `AutonomousPromotionStabilityLaw` — The autonomous promotion loop must reach a stable fixed point: `Result_∞ = f(Result_∞)` where `f` is the promote-and-strengthen operator. The fixed point must be unique and attracting with basin of attraction containing the initial result.
