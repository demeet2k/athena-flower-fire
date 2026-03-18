<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvQ.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvQ.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvQ.R1.md
-->

# InvQ — Square Lens / Objects

- `InvQ.S1.a`: `CouplingDisconnector` — The discrete operation of severing a coupling between two lattice regions. The coupling carried information (signals, constraints, correlations) between the regions. Disconnecting it means: the information it carried has been absorbed into the regions' local states and is no longer needed as an explicit connection.
- `InvQ.S1.b`: `TopologicalReductionDelta` — The difference between the full topology (all connections) and the essential topology (minimum spanning tree + cycle generators). The delta identifies redundant connections — topologically unnecessary couplings that can be removed without changing the manifold's homotopy type.
- `InvQ.S1.c`: `ConnectionProductContraction` — The full coupling graph is a product of pairwise connections. Contraction factors this product: remove redundant connections while preserving the graph's fundamental group. The contracted product is the topological skeleton — minimum edges, maximum topological information.
- `InvQ.S1.d`: `RedundancyQuotient` — The ratio of total couplings to essential couplings = the redundancy quotient. A quotient of 1 means no redundancy (every coupling is essential). Higher quotients indicate more aggressive contraction is possible. The seed stores only essential couplings.
