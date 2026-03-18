<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvV.R3.md
-->

# InvV — Square Lens / Constructions

- `InvV.S3.a`: `StreamingDigester` — Processes the replay log one step at a time, updating the running hash. At each step: hash(step_data) is folded into the accumulator. Final output: fixed-width digest. Memory usage: O(1) regardless of log size.
- `InvV.S3.b`: `CanonicalDiffer` — Runs the actual trace and canonical trace in parallel, comparing at each step. Records deviations with their classification (environmental vs. logical). Output: the deviation vector and the deterministic core mask.
- `InvV.S3.c`: `CapsuleFolder` — Takes the set of verifier capsules and composes them associatively into the master attestation. Verifies associativity by checking that different composition orders produce the same result. Output: the master attestation object.
- `InvV.S3.d`: `EntropyEstimator` — Estimates the information-theoretic entropy of the replay log using streaming algorithms (e.g., entropy of the step distribution). Compares against the actual compression quotient. Flags any digest that appears to beat the entropy bound.
