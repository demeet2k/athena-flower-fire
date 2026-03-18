<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppL.R3.md
-->

# AppL — Square Lens / Constructions

- `AppL.S3.a`: `WitnessBundleAssembler` — The construction that collects individual witness values from across the crystal, verifies each provenance signature, checks mutual consistency via pairwise conjunction testing, and packages them into a validated `WitnessBundle`.
- `AppL.S3.b`: `ProofPlanCompiler` — The compiler that takes a candidate set and the available evidence types, constructs a proof plan DAG that covers all candidates, optimizes the plan for minimum expected evidence-gathering cost, and outputs the executable plan with milestone checkpoints.
- `AppL.S3.c`: `EvidenceChainLinker` — The linker that connects individual evidence items into a chain, verifying that each item's output type matches the next item's input type, computing the chain's overall strength, and flagging any weak links that need reinforcement.
- `AppL.S3.d`: `CandidateSetGenerator` — The generator that, given an ambiguous result and the crystal's type constraints, enumerates all possible candidates, assigns prior probabilities based on frequency data, and identifies the distinguishing evidence for each candidate.
