<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.C3.md
-->

# InvZ — Fractal Lens / Constructions

- `InvZ.R3.a`: `FixedPointIterator` — Iterates F starting from the crown state: `crown → F(crown) → F²(crown) → ... → seed`. Each iteration compresses by factor 1/φ. Terminates when `|F^n(crown) - F^{n-1}(crown)| < ε`.
- `InvZ.R3.b`: `ContractionTracker` — Monitors the contraction sequence, verifying at each step that the contraction ratio stays ≤ 1/φ. Records the contraction trajectory as a descent path from crown to seed. Any step with ratio > 1/φ indicates incomplete expansion — flags for review.
- `InvZ.R3.c`: `EulerProductEvaluator` — Evaluates the Euler product at the organism's s-value, accumulating prime factors in order. Stores the running product and convergence rate. Final value = seed's multiplicative signature.
- `InvZ.R3.d`: `RGFlowIntegrator` — Integrates the RG flow equations from the crown (UV/microscopic) to the seed (IR/macroscopic). Tracks which operators are relevant (grow under flow), marginal (stay constant), or irrelevant (shrink). Seed retains only relevant operators.
