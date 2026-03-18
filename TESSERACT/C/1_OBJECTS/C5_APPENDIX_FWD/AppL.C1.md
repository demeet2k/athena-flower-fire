<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppL.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppL.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppL.R1.md
-->

# AppL — Cloud Lens / Objects

- `AppL.C1.a`: `BayesianEvidenceAccumulator` — The running posterior distribution `P(c_i | e_1, ..., e_t) ∝ P(c_i) · Π_{j=1}^{t} P(e_j | c_i)` tracking the probability of each candidate after `t` evidence items, updated online as each new piece of evidence arrives.
- `AppL.C1.b`: `LikelihoodRatioMatrix` — The `k × k` matrix `LR[i,j] = P(evidence | c_i) / P(evidence | c_j)` of pairwise likelihood ratios between candidates, enabling direct comparison of how well each candidate explains the observed evidence relative to every other candidate.
- `AppL.C1.c`: `PromotionThreshold` — The decision threshold `τ` such that candidate `c_i` is promoted to definite answer when `P(c_i | evidence) > τ`. The threshold is calibrated to control the false promotion rate: `P(wrong promotion) < α` for declared significance level `α`.
- `AppL.C1.d`: `EvidenceInformationValue` — The expected information gain `V(e) = H(candidates) - E_{e}[H(candidates | e)]` of gathering evidence item `e`, measured in bits. High-value evidence items are those that most sharply distinguish between candidates.
