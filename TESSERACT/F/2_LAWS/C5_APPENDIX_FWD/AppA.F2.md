<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppA.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppA.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppA.R2.md
-->

# AppA — Flower Lens / Laws

- `AppA.F2.a`: `PhaseCovariantRoutingLaw` — Address resolution is covariant with phase: if the organism advances from phase `φ` to `φ + δ`, all metro-routed addresses shift by the same `δ`, preserving relative ordering within each line.
- `AppA.F2.b`: `MetroLineConservation` — A shard's metro line assignment `M` is conserved during transport; shards do not jump between metro lines except at designated interchange stations (crystal vertices where multiple lines intersect).
- `AppA.F2.c`: `FlowContinuityLaw` — The address flow vector `dAddr/dt` is continuous along each metro line segment; discontinuities occur only at station boundaries where routing decisions branch. No address teleportation within a segment.
- `AppA.F2.d`: `WavePacketCoherenceLaw` — Co-traveling address packets maintain coherence (constant relative offsets) as long as they remain on the same metro line; decoherence occurs only at branching junctions or phase-transition boundaries.
