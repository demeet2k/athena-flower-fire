<!-- TESSERACT: F/1_OBJECTS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=F facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvY.S1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvY.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvY.R1.md
-->

# InvY — Flower Lens / Objects

- `InvY.F1.a`: `LoadCurveDescent` — The continuous load curve of the deployment descends smoothly from peak to zero. No step functions, no sudden drops — the Flower view demands harmonic descent. The load curve integral over the shutdown window represents total work-in-flight absorbed.
- `InvY.F1.b`: `LatencyWaveQuench` — The oscillating latency pattern of the live system dampens to zero as requests drain. Each quench cycle reduces amplitude by a factor proportional to 1/e — exponential decay of operational volatility.
- `InvY.F1.c`: `ThroughputProductFade` — The multiplicative throughput (requests/sec × processing depth × pipeline stages) fades multiplicatively: each factor independently declines toward zero, and their product declines faster than any individual.
- `InvY.F1.d`: `ErrorRatioConvergence` — The ratio of errors to total operations converges to the deployment's intrinsic error rate as transient shutdown errors are absorbed. The limiting ratio is the deployment's quality signature — carried into the seed.
