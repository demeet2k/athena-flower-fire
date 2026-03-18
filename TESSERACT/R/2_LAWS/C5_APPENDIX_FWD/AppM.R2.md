<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppM.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppM.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppM.C2.md
-->

# AppM — Fractal Lens / Laws

- `AppM.R2.a`: `SelfContainmentLaw` — A self-replaying computation must carry everything needed for replay: transition function, log, initial snapshot, and RNG seed; no external dependency is permitted.
- `AppM.R2.b`: `ProofSufficiencyLaw` — A proof-carrying artifact's certificate must be independently verifiable using only the data embedded in the artifact itself; the verifier needs no network access or external state.
- `AppM.R2.c`: `KernelMinimalityLaw` — The replay kernel seed must be the smallest program that can execute the replay; any strictly smaller program that also replays correctly must be the same program up to isomorphism.
- `AppM.R2.d`: `CapsuleTamperEvidenceLaw` — Any modification to an auto-verifier capsule's content, log, or certificate causes the embedded verifier to reject; the capsule is tamper-evident by construction.
