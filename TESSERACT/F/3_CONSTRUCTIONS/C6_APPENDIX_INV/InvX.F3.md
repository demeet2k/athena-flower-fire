<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvX.R3.md
-->

# InvX — Flower Lens / Constructions

- `InvX.F3.a`: `StreamIntake` — Opens a continuous intake channel, receives the bundle stream, buffers for continuity verification, and routes to the shard reassembly pipeline. Reports throughput, latency, and any gap events.
- `InvX.F3.b`: `InverseEncoder` — Applies the inverse of the export encoding in exact reverse order. For each encoding layer: identifies the encoder, loads its inverse, applies, and verifies round-trip consistency.
- `InvX.F3.c`: `VolumeAccountant` — Tracks total bytes absorbed and compares against the declared export volume. Reports running total, expected remaining, and any discrepancies.
- `InvX.F3.d`: `SafeDecompressor` — Decompresses with ratio checking at every stage. If the decompression ratio exceeds the declared bound at any point, halts and reports a potential decompression bomb.
