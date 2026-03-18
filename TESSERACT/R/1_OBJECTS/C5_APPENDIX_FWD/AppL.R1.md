<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppL.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppL.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppL.C1.md
-->

# AppL — Fractal Lens / Objects

- `AppL.R1.a`: `SelfGeneratingWitness` — A system component whose normal operation produces evidence for its own correctness: by running, it generates a trace that constitutes a witness for the claim that it ran correctly. The witness is a byproduct of computation, not a separate verification step.
- `AppL.R1.b`: `BootstrappedProofPlan` — A proof plan whose first milestone is the construction of the rest of the proof plan: `Step_1 = "build Steps_2..n"`. The plan generates itself as it executes, adapting to the evidence discovered at each stage rather than being fixed in advance.
- `AppL.R1.c`: `RecursiveEvidenceAmplifier` — The recursive construction where evidence at depth `d` amplifies evidence at depth `d+1`: `strength(e_{d+1}) = g(strength(e_d))` for amplification function `g` with `g(x) > x` when `x > x_threshold`. Weak evidence bootstraps into strong evidence through recursive reinforcement.
- `AppL.R1.d`: `AutonomousPromotionLoop` — A closed-loop system where the promoted result generates evidence that confirms the promotion, which strengthens the result, which generates more evidence: `Result → Evidence → Promotion → StrongerResult → MoreEvidence → ...` converging to a self-sustaining fixed point.
