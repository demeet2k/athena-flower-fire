<!-- TESSERACT: C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=C facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.R3.md
-->

# AppL — Cloud Lens / Constructions

- `AppL.C3.a`: `OnlineBayesianUpdater` — The sequential updater that processes evidence items one at a time, multiplying the current posterior by the likelihood of each candidate given the new evidence, and renormalizing to maintain a proper distribution.
- `AppL.C3.b`: `LikelihoodRatioComputer` — The engine that computes the full `k × k` likelihood ratio matrix from the candidate models and observed evidence, verifies transitivity, and flags any inconsistencies for investigation.
- `AppL.C3.c`: `ThresholdOptimizer` — The optimizer that selects the promotion threshold `τ` to minimize expected decision cost (balancing false promotions against delayed promotions), subject to the calibration constraint `τ ≥ 1 - α`.
- `AppL.C3.d`: `InformationValueRanker` — The ranker that computes `V(e)` for each available evidence item, sorts them by expected information gain, and recommends the highest-value item to gather next, implementing the optimal experimental design for ambiguity resolution.
