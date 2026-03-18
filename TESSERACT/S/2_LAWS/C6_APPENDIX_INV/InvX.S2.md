<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvX.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvX.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvX.R2.md
-->

# InvX — Square Lens / Laws

- `InvX.S2.a`: `ShardIntegrityOnAbsorption` — Every shard extracted from a bundle must match its declared hash. Corrupted shards are rejected, not silently accepted. The unpacking process is verified at every step.
- `InvX.S2.b`: `FormatLosslessnessLaw` — Format stripping must be lossless: the shard content after stripping must be bit-identical to the original shard before export. Any format layer that cannot be cleanly stripped indicates a format mismatch — absorption is paused.
- `InvX.S2.c`: `ReferenceConsistencyLaw` — After relinking, every cross-reference must resolve to a valid internal address. Dangling references (pointing to shards not in the organism) are flagged as absorption gaps requiring either deferred resolution or explicit null-binding.
- `InvX.S2.d`: `VersionCompatibilityLaw` — The version delta must be within the organism's declared compatibility window. Deltas exceeding the window require explicit migration, not automatic absorption.
