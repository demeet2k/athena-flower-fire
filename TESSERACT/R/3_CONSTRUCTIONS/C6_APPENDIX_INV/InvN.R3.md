<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.C3.md
-->

# InvN — Fractal Lens / Constructions

- `InvN.R3.a`: `OrderedClockHalter` — Halts sub-clocks in order of ascending period: 3→4→5→7. At each halt: decelerates, freezes, captures state. Verifies faster clocks are already halted before proceeding.
- `InvN.R3.b`: `ContractionAccumulator` — Accumulates the timing state contraction at each sub-clock halt. Reports the cumulative compression ratio and remaining timing complexity.
- `InvN.R3.c`: `ClockTreeCollapser` — Manages leaf-first collapse of the clock hierarchy. Tracks which clocks are halted and which are still running. Ensures correct ordering.
- `InvN.R3.d`: `ProtocolVerifier` — Compares halt protocol at each clock level. Reports deviations. Confirms fixed-point property.
