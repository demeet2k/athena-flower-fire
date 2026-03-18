<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvV.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvV.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvV.R2.md
-->

# InvV — Square Lens / Laws

- `InvV.S2.a`: `DigestFidelityLaw` — The digest must be a faithful summary: given the digest and the replay grammar, it must be possible to verify any specific step of the replay without storing the full log. This is a Merkle-like property — any step is verifiable from its path in the digest tree.
- `InvV.S2.b`: `CanonicalDeviationBound` — Deviations from canonical must be bounded and classified. Environmental deviations (timing, memory addresses) are tolerated. Logical deviations (different outputs for same inputs) are bugs. The bound separates tolerable from intolerable.
- `InvV.S2.c`: `CapsuleCompositionLaw` — Verifier capsules compose associatively: the order of composition does not affect the master attestation. This guarantees that capsules from different subsystems can be composed in any order. Non-associative capsules indicate a verification inconsistency.
- `InvV.S2.d`: `BoundedCompressionLaw` — The compression quotient must be bounded above by the replay's information-theoretic entropy. No compression scheme can beat the entropy bound. If the actual quotient exceeds the entropy bound, the digest is lossy (some information was silently dropped).
