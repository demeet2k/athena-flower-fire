<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppH -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppH.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppH.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppH.R1.md
-->

# AppH — Square Lens / Objects

- `AppH.S1.a`: `CouplingBond` — The ×-seed's binding primitive applied to two system components: `A ⊗ B = AB`. A coupling bond makes two components behave as one composite. Source: ROSETTA[×] Bind compression.
- `AppH.S1.b`: `DecouplingOperator` — The −-seed's cancellation primitive applied to coupled components: `AB → A + B` (decoupling = factorization). Retrieves independent components from a composite.
- `AppH.S1.c`: `TopologicalClosure` — The π-seed's closure law applied to system topology: a system is topologically closed when every boundary is sealed (no open edges, no dangling references, no unresolved dependencies). `Σ(boundary segments) = 0`.
- `AppH.S1.d`: `DependencyGraph` — The directed acyclic graph of component dependencies. Each edge is a coupling bond. The graph's topology determines build order, failure propagation, and coupling strength.
