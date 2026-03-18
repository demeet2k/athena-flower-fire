<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppA.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppA.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppA.R2.md
-->

# AppA — Cloud Lens / Laws

- `AppA.C2.a`: `FuzzyResolutionConvergenceLaw` — As evidence accumulates, the fuzzy address distribution `P_t(addr)` converges to a delta function `δ(addr*)` at the true address; convergence rate is bounded by `O(1/√t)` for `t` independent observations.
- `AppA.C2.b`: `ClosestStationMonotonicityLaw` — If station `A` is closer than station `B` to query `Q` in Hamming distance, then `P(A|Q) ≥ P(B|Q)` under uniform prior; distance rank and probability rank are monotonically aligned.
- `AppA.C2.c`: `AmbiguityReductionLaw` — Each additional parsed symbol component reduces ambiguity cloud volume by a factor of at least `1/|range_i|` where `|range_i|` is the cardinality of the `i`-th component's domain. Five fully parsed components yield a point.
- `AppA.C2.d`: `ConfidenceCalibrationLaw` — The symbol confidence vector must be calibrated: among all addresses parsed with confidence `p` for component `i`, the fraction correctly parsed must fall within `p ± ε` for declared tolerance `ε`.
