<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.C3.md
-->

# InvL — Fractal Lens / Constructions

- `InvL.R3.a`: `RecurrenceTracer` — Traces all recursive growth to the Fibonacci seed. Builds the derivation tree. Reports orphaned recurrences.
- `InvL.R3.b`: `ContractionVerifier` — Verifies all contractions use the golden ratio. Reports non-golden contractions with their justifications.
- `InvL.R3.c`: `EulerProductVerifier` — Verifies Euler product convergence at the declared s-value. Reports convergence rate and any divergence warnings.
- `InvL.R3.d`: `RGFixedPointVerifier` — Verifies the RG fixed point by applying F and checking fixed-point condition. Reports any false fixed points.
