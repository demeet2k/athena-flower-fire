<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.R3.md
-->

# InvY — Flower Lens / Constructions

- `InvY.F3.a`: `LoadCurveIntegrator` — Integrates the load curve from shutdown start to completion. The integral = total work absorbed. Verifies C¹ continuity at each time step. Reports any discontinuities as violation events.
- `InvY.F3.b`: `LatencyDamper` — Applies exponential damping to the latency signal. Monitors decay rate and flags any cycle where damping ratio exceeds 1/e threshold. Output: damped latency profile and quench completion time estimate.
- `InvY.F3.c`: `ThroughputFader` — Multiplies the independent decline factors (request rate, processing depth, pipeline stages) to compute composite throughput at each time step. Verifies monotonic decrease. Reports any non-monotone anomalies.
- `InvY.F3.d`: `ErrorRateSeparator` — Separates transient shutdown errors from intrinsic operational errors using statistical filtering. Computes the intrinsic error rate as the stable limit of the filtered signal. Seals this rate as the deployment quality signature.
