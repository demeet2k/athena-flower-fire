<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppL.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppL.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppL.R2.md
-->

# AppL — Square Lens / Laws

- `AppL.S2.a`: `WitnessConsistencyLaw` — All witnesses in a bundle must be mutually consistent: for any pair `(w_i, w_j)`, the conjunction `w_i ∧ w_j` must be satisfiable. Inconsistent witness bundles are rejected and routed to AppK conflict resolution.
- `AppL.S2.b`: `ProofPlanCompleteness` — A proof plan must cover all candidates: for each candidate `c_i` in the candidate set, the plan contains at least one evidence path that either confirms `c_i` (promoting it to OK) or eliminates it (reducing the candidate set). No candidate may be left unaddressed.
- `AppL.S2.c`: `EvidenceChainIntegrity` — An evidence chain is valid only if every link is present and verified: removing any single evidence item `e_i` invalidates the chain. There are no shortcuts; each step must be witnessed.
- `AppL.S2.d`: `CandidateSetExhaustiveness` — The candidate set must contain the true answer: `true_answer ∈ S` is a precondition for promotion. If the true answer is not among the candidates, the promotion process will fail and the result must be escalated to evidence plan revision.
