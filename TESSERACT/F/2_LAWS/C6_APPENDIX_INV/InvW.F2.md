<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvW.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvW.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvW.R2.md
-->

# InvW — Flower Lens / Laws

- `InvW.F2.a`: `WavefrontIntegrityLaw` — The decompression wavefront must advance monotonically through the lattice. No position is decompressed twice, no position is skipped. The wavefront is a connected surface at all times.
- `InvW.F2.b`: `PhaseExactnessLaw` — The inverse phase shift must exactly cancel the forward phase shift. Any phase error accumulates across the address space and produces systematic addressing errors. Phase error tolerance: zero.
- `InvW.F2.c`: `ModeSeparationLaw` — Layer modes must be orthogonal for clean decomposition. Non-orthogonal layers require Gram-Schmidt orthogonalization before individual extraction is possible. The container format must guarantee mode orthogonality.
- `InvW.F2.d`: `RelaxationBoundLaw` — Decompression must complete within bounded time. The time constant is proportional to the compression ratio: higher compression = longer relaxation. Unbounded relaxation indicates a degenerate container (infinite compression ratio).
