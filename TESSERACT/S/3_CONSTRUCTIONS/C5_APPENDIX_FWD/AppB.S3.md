<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppB.R3.md
-->

# AppB — Square Lens / Constructions

- `AppB.S3.a`: `ConservationChecker` — The verifier that takes a proposed transport path and computes the six conservation sums `(Σ Δs, Σ Δz, Σ Δφ mod 2π, Δa, Σ Δf mod 6, Π σ)`, returning OK if all are zero/identity and VIOLATION with the offending law otherwise.
- `AppB.S3.b`: `NormalFormReducer` — The canonical reducer that takes any sequence of crystal operations and sorts them into normal form `[shell-moves | zoom-moves | phase-rotations | face-shifts | Mobius-flips]`, canceling inverse pairs and reducing modular components.
- `AppB.S3.c`: `EquivalenceClassBuilder` — The construction that partitions all transport paths between two fixed endpoints into equivalence classes under the six conservation laws, where two paths are equivalent iff they have identical conservation signatures.
- `AppB.S3.d`: `MinimalPathFinder` — The optimizer that, given a source and target Xi108 address, finds the shortest transport path in normal form, using the six conservation laws to prune impossible branches and the normal form uniqueness to avoid redundant search.
