<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppP.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppP.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppP.R2.md
-->

# AppP — Cloud Lens / Laws

- `AppP.C2.a`: `ObservabilityCompletenessLaw` — Every deployed element server must emit the full set of standard telemetry signals (request count, latency histogram, error count, shard operations); silent servers are operationally invisible and forbidden.
- `AppP.C2.b`: `ResonanceVectorNormalizationLaw` — Each component of the resonance vector must be normalized to `[0, 1]` where 0 is total failure and 1 is peak health; the normalization function must be monotonic and documented.
- `AppP.C2.c`: `AnomalyThresholdCalibrationLaw` — The anomaly detector's threshold must be calibrated so that the false-positive rate on the baseline period is below `alpha`; uncalibrated detectors must not trigger alerts.
- `AppP.C2.d`: `CorrelationCausalityLaw` — The correlation tracer must distinguish correlation from causation: correlated anomalies are reported as potentially linked, not as confirmed causal chains, unless a dependency edge exists.
