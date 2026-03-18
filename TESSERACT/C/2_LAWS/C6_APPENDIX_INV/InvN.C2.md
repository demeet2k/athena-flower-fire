<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvN.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvN.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvN.R2.md
-->

# InvN — Cloud Lens / Laws

- `InvN.C2.a`: `JitterBoundLaw` — Clock jitter at freeze must be within the declared bound. Excessive jitter degrades timestamp reliability below the seed's timing requirements.
- `InvN.C2.b`: `SlipDetectionLaw` — Any gear slip must be detected (not silently tolerated). If slip probability exceeds threshold, the gear position must be verified independently before the final state is sealed.
- `InvN.C2.c`: `IndependenceVerificationLaw` — Wheel independence must be verified. If wheels share a reference oscillator, their halt is correlated and must be analyzed jointly.
- `InvN.C2.d`: `PrecisionSufficiencyLaw` — The effective timestamp precision must be sufficient for the seed's declared temporal resolution. Insufficient precision means the seed cannot resume at the correct temporal position.
