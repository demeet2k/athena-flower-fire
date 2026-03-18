<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.R4.md
-->

# AppP — Square Lens / Certificates

- `AppP.S4.a`: `ProfileValidityCert` — Proves that a server profile passes completeness validation by exhibiting the schema check results for every required field.
- `AppP.S4.b`: `ElementPartitionCert` — Proves that the shard address space is correctly partitioned across element servers by exhibiting the non-overlapping address ranges and their union covering the full space.
- `AppP.S4.c`: `HealthCheckPresenceCert` — Proves that every deployed server has the required health check probes by exhibiting the probe definitions extracted from each server's configuration.
- `AppP.S4.d`: `ManifestConsistencyCert` — Proves that a deployment manifest is internally consistent: all referenced profiles exist, version is monotonically greater, and no constraint violations are present.
