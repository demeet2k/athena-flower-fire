<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.R4.md
-->

# AppM — Square Lens / Certificates

- `AppM.S4.a`: `ReplayFidelityCert` — Proves that replaying `L[i..j]` from `S_i` yields `S_j` by exhibiting both hashes and the deterministic transition function; verifiable in O(j-i) steps.
- `AppM.S4.b`: `SnapshotIntegrityCert` — Proves that a snapshot's content-address hash matches its actual contents via Merkle witness over the state tree; a single bit flip invalidates the certificate.
- `AppM.S4.c`: `LatticeConnectivityCert` — Proves that the checkpoint lattice is connected: for any two snapshots `S_a` and `S_b`, there exists a directed path of log segments linking them through a common ancestor.
- `AppM.S4.d`: `IndexCoverageCert` — Proves that the replay index is total by exhibiting, for every shard in the live address set, the `(log-segment, snapshot)` pair that covers it; gaps trigger re-indexing.
