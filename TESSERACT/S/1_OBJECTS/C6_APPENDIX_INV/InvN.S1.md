<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvN.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvN.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvN.R1.md
-->

# InvN — Square Lens / Objects

- `InvN.S1.a`: `BeatCounterHalt` — The discrete beat counter of the Z₄₂₀ clock halts at its current value. The successor function ceases: there is no "next beat." The halted counter value becomes the seed's timestamp — a single integer encoding the organism's final temporal position within its 420-beat cycle.
- `InvN.S1.b`: `GearDisengagement` — The difference between engaged and disengaged gears. Each gear mesh (3↔5, 5↔7, 3↔7, 4↔all) is disconnected. The zero set: gear positions that are self-consistent without meshing — the gears' natural rest positions.
- `InvN.S1.c`: `WheelProductFreeze` — The product of all wheel states: 3D-current × 5D-tilt × 7D-timing × 4D-barycentric = the composite clock state. Freezing computes this product one final time and stores it as a 4-tuple. This tuple is the seed's complete temporal coordinate.
- `InvN.S1.d`: `CycleCompletionQuotient` — The quotient of elapsed beats by 420 = the cycle completion fraction. A quotient of 1 means the cycle completed exactly. A fractional quotient means the clock froze mid-cycle — the incomplete cycle is recorded with its exact fractional position.
