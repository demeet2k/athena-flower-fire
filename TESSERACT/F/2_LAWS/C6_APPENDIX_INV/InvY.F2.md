<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvY.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvY.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvY.R2.md
-->

# InvY — Flower Lens / Laws

- `InvY.F2.a`: `SmoothDescentLaw` — The load curve must be C¹-continuous during shutdown: no discontinuities, no infinite derivatives. This prevents system shock. The descent rate is bounded by the system's thermal capacity (maximum safe rate of change).
- `InvY.F2.b`: `ExponentialQuenchLaw` — Latency volatility must decay at least exponentially. Sub-exponential decay indicates a stuck process or resource contention that must be resolved before shutdown proceeds.
- `InvY.F2.c`: `MonotonicThroughputLaw` — Throughput must monotonically decrease during shutdown. Any increase indicates new work being admitted, which violates the drain protocol. The decrease need not be smooth, but it must be monotone.
- `InvY.F2.d`: `ErrorRateStabilityLaw` — The intrinsic error rate (errors/operations in steady state) must stabilize before the final error ratio is sealed. Transient shutdown errors must be distinguishable from intrinsic errors and excluded from the quality signature.
