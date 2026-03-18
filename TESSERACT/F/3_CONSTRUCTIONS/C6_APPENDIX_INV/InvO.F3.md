<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.R3.md
-->

# InvO — Flower Lens / Constructions

- `InvO.F3.a`: `WaveDamper` — Applies damping to the transport wave. Monitors amplitude decay. Flags any mode with sub-exponential decay. Reports the damped spectrum.
- `InvO.F3.b`: `PhaseMerger` — Continuously adjusts phase offsets toward zero. Uses smooth interpolation (no snapping). Reports phase alignment progress and residual offsets.
- `InvO.F3.c`: `EnergyAccountant` — Tracks kinetic energy (½Iω²) and internal energy (seed thermal content). Verifies conservation at each step. Reports energy flow from rotation to thermal.
- `InvO.F3.d`: `IdentityApproacher` — Computes ||T - id|| at each step. Verifies geometric decay toward zero. Reports convergence rate and projected step to identity.
