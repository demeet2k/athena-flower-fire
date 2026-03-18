<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvS.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvS.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvS.R2.md
-->

# InvS — Flower Lens / Laws

- `InvS.F2.a`: `SmoothDampingLaw` — Residual damping must be smooth: no cell's residual may change sign (positive → negative or vice versa) during absorption. Sign changes indicate overshooting, which creates new residuals.
- `InvS.F2.b`: `MonotoneRefinementLaw` — The NEAR-to-exact refinement curve must be monotonically decreasing. Any increase in the approximation error indicates a refinement bug.
- `InvS.F2.c`: `FluxConservationLaw` — The total flux into the lattice boundary must be zero (nothing enters or leaves the closed system). All residual flow is internal redistribution.
- `InvS.F2.d`: `PrecisionMonotoneLaw` — Precision must monotonically increase during truncation recovery. Losing precision during recovery is a regression.
