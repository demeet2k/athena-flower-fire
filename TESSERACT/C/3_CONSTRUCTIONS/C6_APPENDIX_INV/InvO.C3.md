<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvO.R3.md
-->

# InvO — Cloud Lens / Constructions

- `InvO.C3.a`: `StillnessEstimator` — Estimates P(stillness) from channel activity measurements. Reports the current probability and confidence interval.
- `InvO.C3.b`: `AgreementMeasurer` — Samples observable values from conjugate representations. Computes the agreement rate. Reports trend and projected convergence time.
- `InvO.C3.c`: `IndependenceChecker` — Tests channel independence using mutual information. Reports the dependency graph. Authorizes parallel shutdown for independent channels.
- `InvO.C3.d`: `ShutdownScheduler` — Computes throughput-per-cost for each channel. Sorts by ascending ratio. Generates the shutdown schedule.
