<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.R3.md
-->

# InvQ — Square Lens / Constructions

- `InvQ.S3.a`: `CouplingAbsorber` — For each redundant coupling: transfers the coupling's information into the local states of the connected regions (by encoding the coupling's signal as a local variable). Verifies that the local states now carry the coupling's information. Then severs the coupling.
- `InvQ.S3.b`: `TopologySimplifier` — Computes the minimum spanning tree + cycle generators using graph algorithms. Identifies all edges not in this essential set as redundant. Reports the redundancy quotient and the list of removable couplings.
- `InvQ.S3.c`: `SkeletonExtractor` — Builds the topological skeleton: the minimal graph that preserves the homotopy type. Verifies homotopy equivalence by computing π₁ of both the full and skeleton topologies and confirming isomorphism.
- `InvQ.S3.d`: `FundamentalGroupComputer` — Computes π₁ of the topology using edge-path group presentation. Reports generators, relations, and the group's abelianization. Verifies conservation under contraction.
