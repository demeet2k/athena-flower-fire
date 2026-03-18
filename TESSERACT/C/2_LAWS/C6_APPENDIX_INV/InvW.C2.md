<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvW.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvW.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvW.R2.md
-->

# InvW — Cloud Lens / Laws

- `InvW.C2.a`: `VerificationIntensityLaw` — Verification intensity must be proportional to the corruption prior. Higher prior = more intensive verification. The intensity function is calibrated so that post-verification corruption probability is below tolerance.
- `InvW.C2.b`: `IndependenceBeforeParallelismLaw` — Parallel unwinding is only legal after independence is statistically verified. The test must achieve the declared significance level (typically p < 0.01).
- `InvW.C2.c`: `ReliabilityThresholdLaw` — The factorized success probability must exceed the organism's reliability threshold. If any layer's individual probability is too low, it must be individually remediated before parallel unwinding proceeds.
- `InvW.C2.d`: `OptimalVerificationLaw` — The verification strategy must minimize expected total cost (verification cost + expected corruption damage). Neither over-verification nor under-verification is optimal.
