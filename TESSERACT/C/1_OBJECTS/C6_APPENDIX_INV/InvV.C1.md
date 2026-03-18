<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvV.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvV.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvV.R1.md
-->

# InvV — Cloud Lens / Objects

- `InvV.C1.a`: `ReplaySamplingVerifier` — Instead of replaying every step, sample k steps randomly and verify those. If all k pass, the replay is statistically certified with confidence 1 - (1-p)^k where p is the per-step failure probability. This is the Cloud view: probabilistic replay verification.
- `InvV.C1.b`: `CapsuleRedundancyExclusion` — Multiple capsules may verify overlapping properties. Inclusion-exclusion identifies the non-redundant core: the minimal set of capsules that covers all properties. Redundant capsules are released — they add no new verification.
- `InvV.C1.c`: `IndependentVerificationProduct` — If verification properties are independent, the joint verification probability = Π P(property_i verified). Independent properties can be released independently without affecting the others.
- `InvV.C1.d`: `VerificationCostNormalization` — The cost of maintaining each verifier capsule is normalized by the value of what it verifies. High-value/low-cost capsules are retained longest. Low-value/high-cost capsules are released first. The normalized ratio governs the release order.
