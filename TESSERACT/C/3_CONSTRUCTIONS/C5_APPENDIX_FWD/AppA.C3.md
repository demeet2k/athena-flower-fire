<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.R3.md
-->

# AppA — Cloud Lens / Constructions

- `AppA.C3.a`: `FuzzyAddressResolver` — The probabilistic resolver that takes a garbled or partial address string, computes a posterior distribution over Xi108 addresses using Bayesian update with a prior from station frequency data, and returns the top-k candidates.
- `AppA.C3.b`: `HammingNeighborSearch` — The nearest-neighbor searcher that, given a query tuple `(s,w,a,f,d)` with wildcards, enumerates all stations within Hamming distance `r` and returns them sorted by distance with tie-breaking by station frequency.
- `AppA.C3.c`: `AmbiguityCloudBuilder` — The construction that takes a partial parse (some components known, others wildcard) and builds the explicit `AmbiguityCloud` by enumerating the Cartesian product of unknown components, filtering by registry existence.
- `AppA.C3.d`: `ConfidenceEstimator` — The calibration engine that estimates per-symbol confidence from parser internal state (token match quality, context agreement, edit distance to nearest valid symbol) and outputs a calibrated `SymbolConfidenceVector`.
