<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvV.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvV.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvV.R1.md
-->

# InvV — Square Lens / Objects

- `InvV.S1.a`: `ReplayLogDigest` — The discrete hash-digest of an entire replay log. Every step in the replay (input → operation → output) is hashed sequentially into a running accumulator. The final digest is a fixed-width integer that attests to the entire execution history without storing it. The successor inverts: "summarize the next replay step" rather than "record the next replay step."
- `InvV.S1.b`: `DiffFromCanonical` — The difference between the actual replay trace and the canonical (expected) trace. If the difference is zero, the replay was perfectly canonical. Non-zero differences identify deviations — bugs, environmental variations, or non-determinism. The zero set of this difference is the deterministic core.
- `InvV.S1.c`: `VerifierCapsuleProduct` — The multiplicative composition of all verifier capsules into a single master attestation. Each capsule proves one property; their product proves all properties simultaneously. The master attestation is a single object replacing the entire capsule collection.
- `InvV.S1.d`: `CompressionQuotient` — The ratio of replay log size to digest size = the compression quotient. A quotient of 10^6 means the digest is one millionth the size of the log. The quotient must be finite and bounded for the compression to be meaningful.
