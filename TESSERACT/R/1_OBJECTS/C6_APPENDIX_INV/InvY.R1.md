<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvY.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvY.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvY.C1.md
-->

# InvY — Fractal Lens / Objects

- `InvY.R1.a`: `RecursiveShutdownSeed` — The shutdown process is itself self-similar: shutting down a deployment = shutting down each sub-deployment + shutting down their coordination layer. The recursion bottoms out at atomic processes that simply stop.
- `InvY.R1.b`: `ShutdownContractionMap` — Each recursive shutdown step contracts the deployment by factor 1/φ: a deployment of size N reduces to sub-deployments of total size N/φ. The remaining N(1-1/φ) = N/φ² is the coordination overhead, also shut down recursively.
- `InvY.R1.c`: `DeploymentTreePruning` — The deployment tree (root deployment → sub-deployments → atomic processes) is pruned from leaves to root. Multiplicative branching during deployment inverts to multiplicative pruning during shutdown. Each pruned branch releases its resources.
- `InvY.R1.d`: `ScaleInvariantShutdown` — The shutdown protocol is the same at every scale: drain, archive, release, certify. Whether shutting down a single process or an entire cluster, the steps are identical — only the scale parameter changes.
