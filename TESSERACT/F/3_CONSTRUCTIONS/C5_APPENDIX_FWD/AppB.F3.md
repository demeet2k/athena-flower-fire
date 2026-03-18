<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.R3.md
-->

# AppB — Flower Lens / Constructions

- `AppB.F3.a`: `StrengthOscillatorEngine` — The engine that computes current law enforcement strength `λ_i(φ)` for each conservation law `i` as a function of superphase `φ`, outputting the 6-vector of enforcement strengths governing the current crystal rigidity.
- `AppB.F3.b`: `ResonanceDetector` — The detector that monitors pairs of conservation law oscillators for phase alignment, triggering a `ResonanceBridge` event when the phase difference drops below threshold `ε` and computing the exchange budget.
- `AppB.F3.c`: `RelaxationWaveSolver` — The wave equation solver that propagates a `LawRelaxationWave` outward from a Genesis source, computing the enforcement reduction at each shell as a function of distance from source and time since Genesis.
- `AppB.F3.d`: `DynamicNormalFormSorter` — The sorter that determines the current normal form ordering based on the active superphase, re-sorts any queued transport sequences to match, and flags sequences that were valid under the previous ordering but illegal under the current one.
