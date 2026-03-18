<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppL.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppL.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppL.R2.md
-->

# AppL — Cloud Lens / Laws

- `AppL.C2.a`: `BayesianConsistencyLaw` — The posterior distribution must be a proper probability distribution at all times: `Σ P(c_i | evidence) = 1`, `P(c_i | evidence) ≥ 0` for all `i`. Updates must preserve normalization; unnormalized intermediates are forbidden in the final output.
- `AppL.C2.b`: `LikelihoodRatioTransitivity` — Likelihood ratios are transitive: `LR[i,k] = LR[i,j] · LR[j,k]` for any triple of candidates. This consistency condition prevents circular evidence that favors `c_i > c_j > c_k > c_i`.
- `AppL.C2.c`: `ThresholdCalibrationLaw` — The promotion threshold `τ` must satisfy `τ ≥ 1 - α` where `α` is the declared false promotion rate. Higher thresholds are permitted (more conservative); lower thresholds violate the significance guarantee.
- `AppL.C2.d`: `InformationValuePositivityLaw` — The expected information value of any evidence item is non-negative: `V(e) ≥ 0`. Evidence never increases expected ambiguity. An item with `V(e) = 0` is uninformative and can be skipped.
