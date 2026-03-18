<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvS.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvS.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvS.R2.md
-->

# InvS — Cloud Lens / Laws

- `InvS.C2.a`: `ZeroMeanRequirement` — The residual distribution must have mean zero before compression begins. Non-zero mean indicates a systematic bias that must be corrected globally before cell-level absorption proceeds.
- `InvS.C2.b`: `ErrorBoundLaw` — Each NEAR approximation's error must be within the declared bound for its method. If actual error exceeds the bound, the approximation method is suspect and must be audited.
- `InvS.C2.c`: `IndependenceVerificationLaw` — Independence must be verified before parallel absorption. Correlated residuals require coordinated absorption.
- `InvS.C2.d`: `ValueCostThresholdLaw` — Bits whose recovery cost exceeds their accuracy value by a declared factor may be declared permanent losses. The factor must be explicitly declared and the precision deficit recorded.
