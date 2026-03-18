<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppA.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppA.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppA.R1.md
-->

# AppA — Cloud Lens / Objects

- `AppA.C1.a`: `FuzzyAddress` — A probabilistic address `P(Xi108[s,w,a,f,d])` assigning a probability distribution over crystal coordinates rather than a single point, used when input is ambiguous or sensor data is noisy.
- `AppA.C1.b`: `ClosestStationSet` — The set of `k`-nearest stations to a fuzzy query, ranked by Hamming distance `d_H(query, station)` in the `(s,w,a,f,d)` tuple space, with associated confidence scores `c_i ∈ [0,1]`.
- `AppA.C1.c`: `AmbiguityCloud` — A convex hull in address space containing all stations compatible with a partial or garbled address, with volume proportional to the number of candidate resolutions and centroid at the maximum-likelihood station.
- `AppA.C1.d`: `SymbolConfidenceVector` — A per-symbol confidence vector `[p_s, p_w, p_a, p_f, p_d]` where each `p_i ∈ [0,1]` indicates the parser's confidence in that component of the parsed address, enabling targeted re-query of low-confidence fields.
