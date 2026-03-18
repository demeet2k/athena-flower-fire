<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppK.C3.md
-->

# AppK — Fractal Lens / Constructions

- `AppK.R3.a`: `SelfHealingEngine` — The engine that executes a self-healing contradiction's embedded repair function iteratively, tracking convergence via `δ_n = |C_n - C_{n-1}|`, and declaring resolution when `δ_n < ε_target` for the first time.
- `AppK.R3.b`: `FixedPointResolver` — The resolver that computes the conflict fixed point by iterating `C_{n+1} = Resolve(C_n)` from the initial conflict state, verifying uniqueness by checking that different initial perturbations converge to the same `C*`.
- `AppK.R3.c`: `RecursiveQuarantineManager` — The manager that handles nested quarantine shells, tracking the depth of each, escalating when depth exceeds `D_max`, and collapsing inner shells as their conflicts resolve from inside out.
- `AppK.R3.d`: `EigenmodeAnalyzer` — The spectral analyzer that computes the conflict interaction matrix `M`, extracts its eigenvalues and eigenvectors, identifies any amplifying modes `|λ| > 1`, and generates targeted quarantine plans for their support.
