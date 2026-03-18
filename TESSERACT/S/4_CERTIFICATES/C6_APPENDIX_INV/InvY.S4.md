<!-- TESSERACT: S/4_CERTIFICATES/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=S facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvY.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvY.C4.md
#   R: ../../R/4_CERTIFICATES/C6_APPENDIX_INV/InvY.R4.md
-->

# InvY — Square Lens / Certificates

- `InvY.S4.a`: `DrainCompletionCert` — Receipt proving all execution slots drained, no mid-cycle terminations, all final states captured, re-entry prevention active on all slots.
- `InvY.S4.b`: `MetricArchiveCert` — Receipt proving all metrics have complete time series (or annotated gaps), all hooks unregistered, monitoring surface is empty.
- `InvY.S4.c`: `ArchiveSealCert` — Receipt proving telemetry archive is complete, hash is valid, signature is tamper-evident, archive is read-only.
- `InvY.S4.d`: `ResourceReleaseCert` — Receipt proving all resources freed (or residuals documented), release ratios computed, no silent leaks, debt against seed (if any) recorded.
