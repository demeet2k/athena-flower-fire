<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.C3.md
-->

# InvO — Fractal Lens / Constructions

- `InvO.R3.a`: `RecursiveUnwinder` — Traverses the transport tree bottom-up. At each leaf: finds fixed point, verifies stability, declares stillness. At each parent: simplifies transport using children's fixed points, then finds its own fixed point.
- `InvO.R3.b`: `DepthReducer` — Removes conjugacy layers one at a time from innermost outward. Reports depth at each step. Verifies monotone decrease.
- `InvO.R3.c`: `StillnessPropagator` — Propagates stillness declarations from leaves to root. At each parent: waits for all children to declare stillness, then begins its own stillness procedure.
- `InvO.R3.d`: `ProtocolVerifier` — Compares stillness protocol at each level. Reports deviations. Confirms fixed-point property.
