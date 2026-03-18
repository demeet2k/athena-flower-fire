<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppM.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppM.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppM.C1.md
-->

# AppM — Fractal Lens / Objects

- `AppM.R1.a`: `SelfReplayingComputation` — A computation that embeds its own replay log and checkpoint kernel within its output, so that any recipient can re-execute the entire derivation without external infrastructure.
- `AppM.R1.b`: `ProofCarryingArtifact` — A shard that carries not only its content but also the verification certificate and minimal replay kernel needed to independently confirm that the content was correctly derived.
- `AppM.R1.c`: `ReplayKernelSeed` — A minimal self-contained binary that, given a log segment, can reconstruct the transition function and execute the replay; the seed is small enough to embed in any shard header.
- `AppM.R1.d`: `AutoVerifierCapsule` — A sealed capsule containing content, replay log, verification samples, and the verifier code itself; opening the capsule automatically runs verification before exposing the content.
