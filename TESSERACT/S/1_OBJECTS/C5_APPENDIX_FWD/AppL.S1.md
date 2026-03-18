<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppL.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppL.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppL.R1.md
-->

# AppL — Square Lens / Objects

- `AppL.S1.a`: `WitnessBundle` — A structured collection `W = {(w_1, σ_1), ..., (w_k, σ_k)}` of witness values `w_i` paired with their provenance signatures `σ_i`, forming the atomic unit of evidence. A witness bundle is valid when all signatures verify and the witnesses are mutually consistent.
- `AppL.S1.b`: `ProofPlan` — A directed acyclic graph `P = (V, E)` where vertices are evidence milestones and edges are inference steps, specifying the exact sequence of observations and deductions needed to promote a `NEAR-AMBIG` result to a definite `OK`. Each edge is labeled with its required witness type.
- `AppL.S1.c`: `EvidenceChain` — A linearly ordered sequence `e_1 → e_2 → ... → e_n` of evidence items where each `e_{i+1}` depends on `e_i`, forming a chain of custody from raw observation to final conclusion. The chain's strength is its weakest link: `strength(chain) = min_i strength(e_i)`.
- `AppL.S1.d`: `CandidateSet` — The explicit enumeration `S = {c_1, ..., c_k}` of all possible answers for an ambiguous result, each annotated with a prior probability `p_i` and the set of distinguishing evidence items that would confirm or eliminate it.
