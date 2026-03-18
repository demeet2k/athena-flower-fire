<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppP.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppP.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppP.R2.md
-->

# AppP — Square Lens / Laws

- `AppP.S2.a`: `ProfileCompletenessLaw` — Every server profile must specify all required fields (element, resources, bindings, tools); incomplete profiles must be rejected at validation time before deployment begins.
- `AppP.S2.b`: `ElementExclusivityLaw` — Each shard address range must be owned by exactly one element server; overlapping ownership is a configuration error that must be detected and resolved before deployment.
- `AppP.S2.c`: `HealthCheckMandatoryLaw` — Every deployed server must have at least one liveness probe and one readiness probe; servers without health checks may not receive traffic.
- `AppP.S2.d`: `ManifestVersionMonotonicityLaw` — Each new deployment manifest must have a version strictly greater than its predecessor; version rollback requires an explicit rollback operation, not a version decrement.
