<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppM.C4.md
-->

# AppM — Fractal Lens / Certificates

- `AppM.R4.a`: `SelfReplayRoundTripCert` — Proves that extracting the embedded replay kernel and log from a self-replaying artifact and executing the replay reproduces the artifact's content exactly.
- `AppM.R4.b`: `ProofIndependenceCert` — Proves that the embedded certificate can be verified using only the artifact's own data by exhibiting the verification execution trace with no external calls.
- `AppM.R4.c`: `KernelMinimalityCert` — Proves that the distilled kernel is minimal by showing that removing any single instruction causes replay to fail; witness is the set of ablation test results.
- `AppM.R4.d`: `CapsuleSealIntegrityCert` — Proves that the capsule's root hash matches the Merkle root of its contents; any content tampering produces a hash mismatch detectable without replaying.
