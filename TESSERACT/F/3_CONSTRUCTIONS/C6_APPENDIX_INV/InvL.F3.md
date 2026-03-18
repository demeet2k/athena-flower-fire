<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvL.R3.md
-->

# InvL — Flower Lens / Constructions

- `InvL.F3.a`: `LimitCapturer` — For each convergence process: verifies the limit has been reached (within declared tolerance), captures the limit value, and discards the partial-sum history. Reports any processes still converging.
- `InvL.F3.b`: `TerminalStateExtractor` — For each recurrence: verifies the wave has reached its terminal state, extracts the final amplitude, and discards the oscillation history.
- `InvL.F3.c`: `PeriodCalculator` — For each multiplicative orbit: computes the exact period using group theory (order of the element in the group). Captures the current phase. Discards the full orbit trajectory.
- `InvL.F3.d`: `GCDSealer` — For each Euclidean descent: verifies the GCD is exact (not approximate). Stores the GCD as the descent's essential value. Discards the quotient-remainder chain.
