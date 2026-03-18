<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.C4.md
-->

# AppL — Fractal Lens / Certificates

- `AppL.R4.a`: `SelfWitnessCert` — Receipt proving the self-generating witness is sound (biconditional holds), the computation trace is complete, and the witness bundle passes independent verification.
- `AppL.R4.b`: `BootstrapTerminationCert` — Receipt proving the bootstrapped proof plan terminated with a finite plan of length `n < N_max`, each self-generated step is well-formed, and the complete plan covers all candidates.
- `AppL.R4.c`: `AmplificationCeilingCert` — Receipt proving recursive evidence amplification converged below the ceiling `strength_max`, the amplification function `g` was applied correctly at each level, and no unbounded amplification occurred.
- `AppL.R4.d`: `AutonomousPromotionCert` — Receipt proving the autonomous promotion loop reached a stable fixed point, the fixed point is unique and attracting, and the final promoted result is self-consistent with the evidence it generates.
