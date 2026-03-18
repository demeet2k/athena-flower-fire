<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvY.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvY.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvY.R2.md
-->

# InvY — Square Lens / Laws

- `InvY.S2.a`: `GracefulDrainLaw` — No execution slot may be terminated before completing its current cycle. The drain is patient: it waits for natural completion, then prevents re-entry. This guarantees no partial state, no corrupted intermediate, no lost in-flight computation.
- `InvY.S2.b`: `MonitoringArchiveCompleteness` — Every metric that was ever registered must have a complete time series in the archive, from first observation to final detach. Gaps indicate monitoring failure and must be annotated with gap certificates.
- `InvY.S2.c`: `TelemetryImmutabilityLaw` — Once the telemetry archive is sealed, no entry may be modified. The archive is append-only during operation and becomes read-only at shutdown. Any post-seal mutation invalidates the deployment certificate.
- `InvY.S2.d`: `CleanReleaseRequirement` — All resources must achieve release ratio = 1 before shutdown is certified complete. Residual consumption (ratio < 1) blocks certification until resolved. Leaked resources are tracked as debt against the seed.
