<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvW.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvW.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvW.R2.md
-->

# InvW — Square Lens / Laws

- `InvW.S2.a`: `HeaderIntegrityOnStrip` — The container header must be valid (correct format version, matching checksums) before stripping is permitted. Stripping an invalid header may corrupt the payload. Integrity check is mandatory, not optional.
- `InvW.S2.b`: `MountpointCleanDetachLaw` — No open file handles, no pending writes, no cached reads may exist at the mountpoint when detach occurs. All I/O must be flushed and closed. Detaching with active I/O causes data corruption.
- `InvW.S2.c`: `LayerOrderPreservationLaw` — Layers must be disassembled in reverse order of assembly. Out-of-order disassembly produces incorrect deltas and corrupts the base. The assembly order is recorded in the container manifest and must be followed exactly.
- `InvW.S2.d`: `DeltaExactnessLaw` — The overlay delta must exactly account for the difference between composite and base. Any residual after delta subtraction indicates a corrupted overlay or a missing intermediate layer.
