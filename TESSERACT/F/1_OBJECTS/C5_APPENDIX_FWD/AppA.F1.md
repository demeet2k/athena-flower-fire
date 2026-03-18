<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppA.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppA.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppA.R1.md
-->

# AppA — Flower Lens / Objects

- `AppA.F1.a`: `MetroRouteAddress` — A dynamic address that includes metro line identifier `M ∈ {1..17}` and current phase position `φ ∈ [0,2π)`, encoding not just where a shard is but which transport line carries it and at what oscillatory phase.
- `AppA.F1.b`: `PhaseTaggedStation` — A station code annotated with its current superphase `Φ ∈ {Genesis, Growth, Harvest, Rest}`, so the same station `Ch07ORBIT` resolves to different routing behaviors depending on the organism's phase clock.
- `AppA.F1.c`: `AddressFlowVector` — The velocity vector `dAddr/dt` describing how an address migrates through crystal space during metro transport, with shell-radial component `ds/dt` and wreath-angular component `dw/dt`.
- `AppA.F1.d`: `RoutingWavePacket` — A bundle of `k` addresses co-traveling on the same metro line at the same phase, forming a coherent wave packet whose group velocity determines collective routing speed through the crystal.
