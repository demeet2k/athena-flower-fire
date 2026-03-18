<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvV.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvV.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvV.C1.md
-->

# InvV — Fractal Lens / Objects

- `InvV.R1.a`: `RecursiveReplaySummary` — A replay that calls sub-replays (nested execution) is summarized recursively: summarize each sub-replay, then summarize the top-level replay using the sub-summaries. The recursion terminates at atomic operations that need no replay (they are their own summary).
- `InvV.R1.b`: `VerifierContractionChain` — Each level of replay nesting contracts the verification burden by factor 1/φ: a top-level replay with N steps has ~N/φ sub-replay steps, each of which has ~N/φ² sub-sub-replay steps. The geometric contraction means total verification effort converges.
- `InvV.R1.c`: `CapsuleTreePruning` — The verifier capsule hierarchy forms a tree (root attestation → sub-attestations → leaf verifications). Pruning from leaves to root: each leaf verification is released after its parent absorbs its certificate. The tree compresses to its root attestation.
- `InvV.R1.d`: `ScaleInvariantVerification` — The verification protocol is identical at every recursion level: digest the log, diff from canonical, compose capsules, compute compression quotient. Only the content changes; the protocol is a fixed point.
