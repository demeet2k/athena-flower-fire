<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvS.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvS.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvS.C1.md
-->

# InvS — Fractal Lens / Objects

- `InvS.R1.a`: `RecursiveResidualAbsorption` — Residuals exist at every level of the lattice hierarchy: global residuals, shell residuals, cell residuals, sub-cell residuals. Absorption is recursive: absorb sub-cell residuals into cells, cell residuals into shells, shell residuals into the global total.
- `InvS.R1.b`: `HierarchicalNEARCompletion` — NEAR values at deeper lattice levels must be completed before their ancestors. A shell-level NEAR depends on its cells' exact values. Bottom-up completion ensures consistency.
- `InvS.R1.c`: `ResidualTreeCollapse` — The residual hierarchy forms a tree. As bottom-level residuals are absorbed, their parent nodes' residuals change (because the children are now exact). The tree collapses level by level until only the root residual remains — which must be zero.
- `InvS.R1.d`: `ScaleInvariantAbsorption` — The absorption protocol is the same at every level: scan, compute residual, absorb or redistribute, verify zero. Only the scale changes. The protocol is a fixed point of the lattice hierarchy.
