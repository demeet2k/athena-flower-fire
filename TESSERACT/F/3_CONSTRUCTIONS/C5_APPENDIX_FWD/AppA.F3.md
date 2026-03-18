<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.R3.md
-->

# AppA — Flower Lens / Constructions

- `AppA.F3.a`: `MetroAddressInjector` — The construction that takes a static Xi108 address and injects it onto a metro line `M` at phase `φ`, producing a `MetroRouteAddress` by computing the nearest on-ramp station and initial flow vector.
- `AppA.F3.b`: `PhaseDependentResolver` — The resolver that takes a `PhaseTaggedStation` and the current organism clock, computes the effective routing table for the active superphase, and returns the concrete next-hop address.
- `AppA.F3.c`: `FlowIntegrator` — The numerical integrator that advances a `MetroRouteAddress` forward by `Δt` time steps along its metro line, updating shell and wreath coordinates via discrete flow equations `s_{t+1} = s_t + v_s`, `w_{t+1} = (w_t + v_w) mod 6`.
- `AppA.F3.d`: `WavePacketAssembler` — The construction that groups addresses by metro line and phase proximity, merges them into coherent `RoutingWavePacket` bundles, and assigns group velocity based on the slowest member.
