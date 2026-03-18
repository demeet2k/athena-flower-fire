<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.R3.md
-->

# InvP — Square Lens / Constructions

- `InvP.S3.a`: `SynchronizedConverger` — Adjusts each agent's state toward the current barycenter at a rate proportional to its distance from the barycenter. All agents move simultaneously. The adjustment rate is calibrated so all agents arrive at the barycenter at the same time.
- `InvP.S3.b`: `DifferenceDriver` — For each pairwise difference: computes the current value, applies a correction proportional to the difference (driving it toward zero), and verifies the correction does not overshoot. Reports all three differences at each step.
- `InvP.S3.c`: `AreaContractor` — Computes the triangle area at each step. Verifies monotone decrease. Reports the contraction factor and projected steps to area = 0.
- `InvP.S3.d`: `BarycenterTracker` — Computes the barycentric coordinates at each step. Monitors for convergence (coordinates stabilizing). Reports the current coordinates and their rate of change.
