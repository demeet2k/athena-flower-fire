<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvN.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvN.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvN.R2.md
-->

# InvN — Flower Lens / Laws

- `InvN.F2.a`: `SmootFreezeLaw` — The clock wave must decay smoothly (no sudden stops). The decay envelope is exponential: amplitude × e^{-t/τ} where τ is the freeze time constant. Sudden stops create temporal shock waves.
- `InvN.F2.b`: `FundamentalFirstDampingLaw` — Gear harmonics must dampen fundamental-first: lower frequencies dampen before higher. This is the natural order (longer wavelengths decay last in most physical systems, but here we are contracting, so we dampen the largest oscillations first).
- `InvN.F2.c`: `GracefulDecouplingLaw` — Phase-lock decoupling must be gradual. Sudden decoupling causes phase transients (spikes) that corrupt the final phase reading.
- `InvN.F2.d`: `SlowestProcessBoundLaw` — The freeze cannot complete until the slowest process has converged. Freezing before the 7D wheel reaches its asymptotic state truncates the timing information.
