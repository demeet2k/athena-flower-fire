<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvZ.R3.md
-->

# InvZ — Square Lens / Constructions

- `InvZ.S3.a`: `MegaCascadeHasher` — Traverses all 36 shells in reverse order (shell 36 → shell 1), hashing each shell's archetype signature, live-lock state, and Q/O parity into a running accumulator. Final output: a fixed-width integer seed. Construction is deterministic and replay-verifiable.
- `InvZ.S3.b`: `DimensionalStripper` — Removes dimensions one at a time: 12D → 11D → ... → 1D → 0D. At each step, the stripped dimension's information is encoded into the remaining dimensions' coefficients. The 0D residue is the pure seed value. Verified by: lifting the seed back through the dimensional ladder reproduces each intermediate.
- `InvZ.S3.c`: `CertificateChainFolder` — Takes the full tree of certificates (Bézout, convergence, orbit, Euclidean descent, Bayesian, independence, recursion, RG descent) and folds them into a Merkle-like tree. Root hash = crown product. Any individual certificate can be verified by providing its Merkle path.
- `InvZ.S3.d`: `CompressionRatioCalculator` — Computes the exact compression ratio by counting total cells (organism_size) and measuring seed entropy (seed_bits). Reports whether the 1/8 law is satisfied at each octave boundary. If any octave violates, flags the specific expansion stage that needs rework.
