<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.R3.md
-->

# InvT — Flower Lens / Constructions

- `InvT.F3.a`: `PhaseAdjuster` — Adjusts the quarantined entity's phase to achieve constructive interference with the lattice. Uses feedback: measure current interference pattern, compute required phase shift, apply shift, remeasure. Iterates until constructive interference is achieved.
- `InvT.F3.b`: `BarrierLowerer` — Gradually reduces the quarantine barrier height. Monitors the entity at each height reduction. If the entity destabilizes (conflict reappears), restores the barrier and investigates. If stable, continues lowering.
- `InvT.F3.c`: `ResonanceTuner` — Adjusts the entity's natural frequency to match a lattice harmonic. Uses spectral analysis to identify the nearest harmonic and compute the required frequency shift. Applies the shift and verifies resonance.
- `InvT.F3.d`: `IterativeReconciler` — Applies successive adjustments with decreasing amplitude. At each iteration: adjusts, measures residual incompatibility, computes convergence ratio. Terminates when residual < tolerance.
