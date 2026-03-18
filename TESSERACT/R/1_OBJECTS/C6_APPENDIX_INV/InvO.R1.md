<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvO.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvO.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvO.C1.md
-->

# InvO — Fractal Lens / Objects

- `InvO.R1.a`: `RecursiveTransportUnwinding` — Transport operates at multiple scales: global transport (between regions), local transport (within regions), and micro-transport (within cells). Unwinding is recursive: micro first, then local, then global. Each level's stillness simplifies the next level's transport.
- `InvO.R1.b`: `ConjugacyDepthContraction` — Each level of transport nesting adds a conjugacy layer: T₁∘T₂∘...∘Tₙ. Unwinding removes layers one at a time, from innermost to outermost. Each removal contracts the conjugacy depth by 1.
- `InvO.R1.c`: `TransportTreeStillness` — The transport hierarchy forms a tree. Stillness propagates from leaves (micro-transport) to root (global transport). Each leaf achieving stillness simplifies its parent's transport burden.
- `InvO.R1.d`: `ScaleInvariantStillness` — The stillness protocol is the same at every level: identify the transport map, find its fixed point, verify stability, declare stillness. Only the transport content changes.
