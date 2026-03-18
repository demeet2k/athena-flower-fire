<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvQ.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvQ.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvQ.C1.md
-->

# InvQ — Fractal Lens / Objects

- `InvQ.R1.a`: `RecursiveTopologyContraction` — The topology has hierarchical structure: macro-topology (between regions) and micro-topology (within regions). Contraction is recursive: contract each region's internal topology first, then contract the inter-region topology. Recursion terminates at atomic regions with no internal structure.
- `InvQ.R1.b`: `HierarchicalCouplingRemoval` — At each level of the hierarchy, redundant couplings are removed. The contraction factor at each level approaches 1/φ for well-structured topologies.
- `InvQ.R1.c`: `TopologyTreeCollapse` — The hierarchical topology forms a tree. Contraction collapses the tree from leaves (innermost regions) to root (global topology). Each collapsed leaf simplifies its parent's topology.
- `InvQ.R1.d`: `ScaleInvariantContraction` — The contraction protocol is identical at every hierarchical level: identify redundant couplings, absorb information, sever, verify homotopy. Only the scale changes.
