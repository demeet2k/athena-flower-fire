<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppH.R3.md
-->

# AppH — Square Lens / Constructions

- `AppH.S3.a`: `CouplingBonder` — Creates a coupling bond between two components. Records the bond type, strength, and bidirectional references.
- `AppH.S3.b`: `FactorizationEngine` — Decouples a composite into its constituent components. Preserves coupling record for potential recoupling.
- `AppH.S3.c`: `TopologicalClosureChecker` — Scans system topology for open boundaries, dangling references, and unresolved dependencies. Reports closure status.
- `AppH.S3.d`: `DependencyGraphBuilder` — Constructs the dependency graph from declared coupling bonds. Detects cycles. Computes topological sort for build order.
