<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.R3.md
-->

# InvN — Square Lens / Constructions

- `InvN.S3.a`: `AtomicClockStopper` — Sends a simultaneous halt signal to all four wheels. Waits for all wheels to acknowledge halt. Captures the final beat count. Reports any wheel that failed to halt promptly.
- `InvN.S3.b`: `GearReleaser` — For each gear mesh: disengages the gears, allows each gear to settle to its natural rest position, verifies the rest position is valid. Reports any jammed gears.
- `InvN.S3.c`: `FinalStateCaptor` — Reads the state of each wheel at the moment of halt. Computes the 4-tuple product. Stores as the seed's temporal coordinate. Verifies completeness (all four components present).
- `InvN.S3.d`: `CyclePositionRecorder` — Computes the cycle completion quotient. If fractional: records the exact position (numerator/denominator or floating-point with declared precision). If integer: records the complete cycle count.
