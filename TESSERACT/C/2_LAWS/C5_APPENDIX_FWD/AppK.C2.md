<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppK.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppK.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppK.R2.md
-->

# AppK — Cloud Lens / Laws

- `AppK.C2.a`: `ConflictProbabilityCalibration` — The conflict probability field must be calibrated: among all addresses assigned probability `p`, the observed fraction experiencing conflicts within `T` steps must lie within `p ± ε` for declared tolerance `ε`.
- `AppK.C2.b`: `EvidenceWeightNormalization` — Evidence weights must sum to 1 within each bundle: `Σ w_i = 1`. This prevents evidence inflation and ensures the Bayesian update is properly normalized.
- `AppK.C2.c`: `MajorityConvergenceLaw` — As the number of independent verifiers `k` grows, the probability that the majority vote reaches the correct resolution converges to 1, provided each verifier has individual accuracy `> 0.5` (Condorcet jury theorem).
- `AppK.C2.d`: `FalsePositiveBoundLaw` — The conflict detection system's false positive rate must not exceed `α_max`: at most `α_max` fraction of flagged conflicts may turn out to be non-conflicts upon investigation. Excessive false positives erode trust in the quarantine system.
