<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.R4.md
-->

# AppM — Cloud Lens / Certificates

- `AppM.C4.a`: `SamplingVerificationCert` — Exhibits the `m` sampled tick indices, their replayed hashes, and the matching original hashes, plus the Hoeffding bound proving that `P(correct) >= 1 - epsilon`.
- `AppM.C4.b`: `DivergenceBelowThresholdCert` — Exhibits the computed KL-divergence value, the threshold `epsilon`, and the calibration parameters; certifies that replay divergence is within acceptable bounds.
- `AppM.C4.c`: `CheckpointOptimalityCert` — Proves that the selected checkpoint set minimizes expected replay cost under the given entropy distribution, by exhibiting the optimization objective and the achieved value.
- `AppM.C4.d`: `ConsensusVerificationCert` — Proves that `k` independent verifier nodes agreed on replay correctness by exhibiting each node's sample set, results, and the majority tally.
