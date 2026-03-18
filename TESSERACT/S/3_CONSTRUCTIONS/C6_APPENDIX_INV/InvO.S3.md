<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.R3.md
-->

# InvO — Square Lens / Constructions

- `InvO.S3.a`: `FixedPointLocator` — Solves T(x) = x for the transport map T. For linear T, this is an eigenvalue problem (eigenvalue 1). For nonlinear T, uses iterative methods. Reports the fixed point and its stability (eigenvalue magnitudes < 1 for stability).
- `InvO.S3.b`: `ConjugacyReducer` — For each pair of conjugate representations: checks if the conjugacy bridge T is essential (representations are genuinely different) or redundant (T ≈ id). Collapses redundant bridges. Preserves essential ones.
- `InvO.S3.c`: `DualityResolver` — For each dual move: evaluates the forward and backward legality conditions in the current (converging) state. Classifies as forward, backward, or null. Verifies consistency of the classification.
- `InvO.S3.d`: `AngleCollapser` — For each rotation parameter: drives the angle toward zero modulo 2π. Uses continuous deceleration (not sudden snap). Reports residual angles at each step.
