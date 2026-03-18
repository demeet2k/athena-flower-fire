<!-- TESSERACT: F/4_CERTIFICATES/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=F facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.S4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.R4.md
-->

# AppM — Flower Lens / Certificates

- `AppM.F4.a`: `CausalChainCert` — Proves that a replay trace respects causal order by exhibiting the topological sort and showing that every dependency edge points forward in the trace.
- `AppM.F4.b`: `RewindCorrectnessCert` — Proves that rewinding from `S_j` to `S_i` via snapshot restoration yields the identical state that was originally recorded at `S_i`; hash comparison is the witness.
- `AppM.F4.c`: `ConvergenceWitnessCert` — Proves two independent replays converge by exhibiting their terminal state hashes and showing equality; used to validate replay determinism across distributed nodes.
- `AppM.F4.d`: `ClockAlignmentCert` — Proves that `k` synchronized replay streams agree on the global tick ordering by exhibiting the merged timeline and verifying no causal inversion exists.
