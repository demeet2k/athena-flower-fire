<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppL.R4.md
-->

# AppL — Square Lens / Certificates

- `AppL.S4.a`: `WitnessBundleCert` — Receipt proving all witnesses in the bundle are consistently signed, mutually consistent, and collected within the declared time window, with each provenance signature independently verified.
- `AppL.S4.b`: `ProofPlanCoverageCert` — Receipt proving the proof plan covers all candidates in the candidate set, every evidence path terminates in either confirmation or elimination, and the plan is acyclic (no circular evidence dependencies).
- `AppL.S4.c`: `EvidenceChainCert` — Receipt proving the evidence chain is complete (no missing links), each link is independently verified, and the chain's minimum strength exceeds the required threshold for promotion.
- `AppL.S4.d`: `CandidateExhaustivenessCert` — Receipt proving the candidate set is exhaustive with respect to the crystal's type constraints, listing the enumeration method used and the constraint satisfaction check that confirmed no candidate was missed.
