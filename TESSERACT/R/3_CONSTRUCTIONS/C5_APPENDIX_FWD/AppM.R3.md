<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.C3.md
-->

# AppM — Fractal Lens / Constructions

- `AppM.R3.a`: `SelfReplayEmbedder` — Takes a computation trace and folds it into the output artifact by appending the replay log, checkpoint, and minimal kernel as structured metadata; the result is self-replaying.
- `AppM.R3.b`: `CertificateWeaver` — Interleaves verification certificates into the replay log at every checkpoint boundary, so that partial replays can verify incrementally without replaying the entire trace.
- `AppM.R3.c`: `KernelDistiller` — Extracts the minimal replay kernel from a full runtime by dead-code elimination and constant folding, producing the smallest self-contained replayer for a given computation class.
- `AppM.R3.d`: `CapsuleSealer` — Assembles content, log, certificates, and verifier code into a sealed capsule; computes the capsule's root hash; and embeds the hash in the capsule header for tamper detection.
