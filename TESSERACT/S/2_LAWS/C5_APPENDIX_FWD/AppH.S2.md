<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppH -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppH.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppH.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppH.R2.md
-->

# AppH — Square Lens / Laws

- `AppH.S2.a`: `CouplingCompositionLaw` — Coupling bonds compose: if A is coupled to B and B is coupled to C, then A is transitively coupled to C. The ×-seed's associativity ensures composition order doesn't matter.
- `AppH.S2.b`: `DecouplingConservationLaw` — Decoupling must conserve all information: `Decouple(A⊗B) = (A, B, coupling_record)`. The coupling record preserves the bond's history so recoupling is possible.
- `AppH.S2.c`: `TopologicalClosureLaw` — A system cannot be certified as complete until topologically closed. Open boundaries = missing dependencies = potential failure modes. The π-seed's polygon closure applied to system architecture.
- `AppH.S2.d`: `AcyclicDependencyLaw` — The dependency graph must be acyclic. Cycles indicate circular dependencies that prevent clean build order. Cycle detection triggers restructuring or decoupling.
