<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvY.R3.md
-->

# InvY — Square Lens / Constructions

- `InvY.S3.a`: `CycleDrainer` — Iterates over all active execution slots. For each slot: waits for current cycle completion, captures final state snapshot, prevents re-entry, marks slot as drained. Reports total drained count and any slots that failed to complete within timeout.
- `InvY.S3.b`: `MetricFlusher` — For each registered metric: flushes buffered observations to persistent archive, verifies time-series completeness, generates gap annotations for any missing intervals, unregisters the hook from the monitoring surface.
- `InvY.S3.c`: `ArchiveSealer` — Materializes the full telemetry product (streams × windows), writes to immutable storage, computes archive hash, and seals with a tamper-evident signature. The sealed archive is the deployment's permanent record.
- `InvY.S3.d`: `ResourceReclaimer` — For each allocated resource: computes release ratio, frees cleanly if ratio = 1, traces residual consumption if ratio < 1, generates leak report. Final output: total resources freed, total residual, and leak remediation plan.
