<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvN.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvN.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvN.C1.md
-->

# InvN — Fractal Lens / Objects

- `InvN.R1.a`: `RecursiveClockHalt` — The Z₄₂₀ clock is itself composed of sub-clocks (3-beat, 4-beat, 5-beat, 7-beat cycles). Halting is recursive: halt the fastest sub-clock first (3-beat), then the next (4-beat), then 5-beat, then 7-beat. Each sub-clock's halt simplifies the composite clock's state.
- `InvN.R1.b`: `PeriodContractionChain` — Each sub-clock halt contracts the total timing state. The contraction factor is the sub-clock's period / total period: 3/420, 4/420, 5/420, 7/420. The cumulative contraction compresses the timing state to a single timestamp.
- `InvN.R1.c`: `ClockTreeCollapse` — The clock hierarchy (master clock → sub-clocks → sub-sub-clocks if any) collapses from leaves (fastest clocks) to root (master Z₄₂₀). Each collapsed sub-clock reduces the master clock's complexity.
- `InvN.R1.d`: `ScaleInvariantHalt` — The halt protocol is identical at every clock level: decelerate, freeze, capture final state, verify rest. Only the period changes.
