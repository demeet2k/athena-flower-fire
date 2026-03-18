<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.R3.md
-->

# InvP — Flower Lens / Constructions

- `InvP.F3.a`: `FrequencyUnifier` — Computes the GCD of three agent frequencies using continued-fraction algorithms. Adjusts each agent's frequency toward the GCD. Verifies that each agent's original frequency is an integer multiple of the GCD.
- `InvP.F3.b`: `PhaseSynchronizer` — Gradually shifts each agent's phase toward the target angle. Uses PLL (phase-locked loop) principles: measure phase error, apply correction proportional to error. Reports phase alignment progress.
- `InvP.F3.c`: `InterferenceComputer` — Computes the three-wave interference pattern at each step. Tracks the pattern's convergence toward a point source. Reports the pattern's spatial extent (should shrink to zero) and peak amplitude (should approach sum of individual amplitudes).
- `InvP.F3.d`: `WheelDecelerator` — Applies controlled deceleration to the 3D current wheel. Transfers angular momentum to the seed's rotation parameter. Verifies momentum conservation at each step.
