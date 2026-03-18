<!-- TESSERACT: F/4_CERTIFICATES/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=F facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.S4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.R4.md
-->

# AppP — Flower Lens / Certificates

- `AppP.F4.a`: `RollingUpdateCompletionCert` — Proves that a rolling update completed successfully by exhibiting each instance's pre-update and post-update version, health check passage timestamp, and traffic restoration confirmation.
- `AppP.F4.b`: `BlueGreenSwitchCert` — Proves that a blue-green switch was atomic by exhibiting the traffic router's configuration snapshots immediately before and after the switch, showing a single-step transition.
- `AppP.F4.c`: `FailoverSuccessCert` — Proves that a failover preserved request continuity by exhibiting the client-visible error rate during the failover window and showing it did not exceed the baseline.
- `AppP.F4.d`: `CanaryPromotionCert` — Proves that a canary deployment met promotion criteria by exhibiting the canary's metrics, the baseline metrics, and the comparison showing all thresholds satisfied.
