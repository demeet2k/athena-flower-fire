<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppK.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppK.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppK.R1.md
-->

# AppK — Cloud Lens / Objects

- `AppK.C1.a`: `ConflictProbabilityField` — The probability field `P_conflict(addr)` assigning to each crystal address the estimated probability that a conflict will occur there within the next `T` time steps, computed from historical conflict rates and dependency structure.
- `AppK.C1.b`: `WeightedEvidenceBundle` — A collection of `n` evidence items `{(e_i, w_i)}` bearing on a conflict's resolution, where each item has a weight `w_i` proportional to its reliability. The weighted sum `Σ w_i · sign(e_i)` determines the resolution direction.
- `AppK.C1.c`: `BayesianConflictResolver` — The probabilistic resolver that updates a prior belief `P(innocent | prior)` with each evidence item via Bayes' rule: `P(innocent | e) ∝ P(e | innocent) · P(innocent)`, converging toward a resolution as evidence accumulates.
- `AppK.C1.d`: `VotingQuorum` — A conflict resolution mechanism where `k` independent verifiers each cast a vote `v_i ∈ {keep, revoke, defer}` and the majority decision (requiring `> k/2` agreement) determines the shard's fate.
