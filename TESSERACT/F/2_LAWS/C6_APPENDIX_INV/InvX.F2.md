<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvX.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvX.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvX.R2.md
-->

# InvX — Flower Lens / Laws

- `InvX.F2.a`: `ContinuousReabsorptionLaw` — The intake stream must be continuous (no gaps, no repeated segments). Gaps indicate packet loss during transport; repeats indicate deduplication failure. Both must be resolved before absorption completes.
- `InvX.F2.b`: `PhaseReversalExactnessLaw` — The inverse encoding must exactly reverse the forward encoding. Approximate inversion (lossy decompression) is only permitted when explicitly declared and the loss budget is within tolerance.
- `InvX.F2.c`: `VolumeConservationLaw` — Total absorbed volume must equal total exported volume (before compression). Volume mismatches indicate data loss or data injection — both are integrity violations.
- `InvX.F2.d`: `DecompressionBoundLaw` — Decompression must complete in bounded time proportional to the compressed size. Decompression bombs (small compressed, huge decompressed) are detected by checking the ratio against declared bounds and rejected if exceeded.
