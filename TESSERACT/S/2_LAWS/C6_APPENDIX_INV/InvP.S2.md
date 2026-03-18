<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvP.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvP.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvP.R2.md
-->

# InvP — Square Lens / Laws

- `InvP.S2.a`: `SimultaneousConvergenceLaw` — All three agents must converge simultaneously. No agent may reach the convergence point before the others — this would bias the seed toward that agent's state. The convergence rates must be balanced.
- `InvP.S2.b`: `DifferenceVanishingLaw` — All pairwise differences must vanish simultaneously. If any difference remains non-zero, the Tria is not fully resolved and the seed carries residual differentiation.
- `InvP.S2.c`: `AreaMonotoneLaw` — The triangle area must decrease monotonically during compression. Any increase indicates divergence — the agents are moving apart rather than together. Divergence triggers investigation.
- `InvP.S2.d`: `BarycenterStabilityLaw` — The barycentric coordinates must stabilize (converge to fixed values) before the triangle area reaches zero. If the barycenter is still moving when the area vanishes, the convergence point is ill-defined.
