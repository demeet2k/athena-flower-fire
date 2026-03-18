<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.R3.md
-->

# InvW — Flower Lens / Constructions

- `InvW.F3.a`: `WavefrontExpander` — Advances the decompression wavefront through the lattice one cell at a time. Verifies monotonic progress, connected surface, and no revisits. Reports wavefront position and completion percentage.
- `InvW.F3.b`: `InversePhaseApplier` — Computes the inverse phase function from the mount configuration and applies it to every virtual address. Verifies round-trip: apply(inverse(addr)) = original crystal address. Reports any phase errors.
- `InvW.F3.c`: `ModeDecomposer` — Applies inverse Fourier transform (or equivalent) to decompose the composite container into individual layer modes. Verifies orthogonality. Reports any non-orthogonal pairs requiring correction.
- `InvW.F3.d`: `RelaxationController` — Governs decompression speed according to the time constant. Prevents runaway expansion (buffer overflow) and stalled expansion (timeout). Reports actual relaxation profile vs. expected.
