<!-- TESSERACT: C/4_CERTIFICATES/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=C facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.F4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.R4.md
-->

# AppP — Cloud Lens / Certificates

- `AppP.C4.a`: `TelemetryCoverageCert` — Proves that all deployed element servers are emitting telemetry by exhibiting the set of servers in the deployment manifest and the set of servers with active telemetry subscriptions, showing equality.
- `AppP.C4.b`: `ResonanceVectorValidityCert` — Proves that the resonance vector is correctly computed by exhibiting the raw metrics, the normalization function, and the resulting vector components, verifiable by recomputation.
- `AppP.C4.c`: `AnomalyCalibrationCert` — Proves that the anomaly detector is correctly calibrated by exhibiting the baseline period metrics, the fitted distribution parameters, and the achieved false-positive rate.
- `AppP.C4.d`: `IncidentClusterCert` — Proves that an incident cluster is valid by exhibiting the anomalies in the cluster, their timestamps, and the pairwise correlation coefficients exceeding the linkage threshold.
