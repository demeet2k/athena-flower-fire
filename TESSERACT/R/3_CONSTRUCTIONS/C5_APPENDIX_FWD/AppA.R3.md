<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.C3.md
-->

# AppA — Fractal Lens / Constructions

- `AppA.R3.a`: `FixedPointFinder` — The iterative construction that computes self-referential addresses by starting from an arbitrary address `a_0` and applying the content-to-address map `a_{n+1} = Addr(Content(a_n))` until convergence, guaranteed within 18 iterations by lattice finiteness.
- `AppA.R3.b`: `HolographicReconstructor` — The constraint propagation engine that takes 3 known address components, sets up the lattice constraint equations, and solves for the 2 unknown components using modular arithmetic and registry lookup.
- `AppA.R3.c`: `RecursiveAddressUnfolder` — The construction that takes a recursive address tree and unfolds it to a flat list of Xi108 addresses by depth-first traversal, applying `depth mod 18` folding at each level and concatenating local suffixes.
- `AppA.R3.d`: `QuineDetector` — The construction that scans a shell for its unique address quine by testing each shard's content against its own address, returning the fixed point or proving non-existence (which would violate `QuineUniquenessLaw`).
