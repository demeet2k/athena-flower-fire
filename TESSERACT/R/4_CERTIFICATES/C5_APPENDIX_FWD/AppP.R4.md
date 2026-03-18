<!-- TESSERACT: R/4_CERTIFICATES/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=R facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.S4.md
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppP.C4.md
-->

# AppP — Fractal Lens / Certificates

- `AppP.R4.a`: `SelfConfigurationCert` — Proves that a self-configuring server's generated configuration matches what the manifest specifies by exhibiting both and showing field-by-field equality.
- `AppP.R4.b`: `ScalingComplianceCert` — Proves that all scaling actions respected the policy bounds by exhibiting the scaling event log with before/after instance counts and the policy's min/max values.
- `AppP.R4.c`: `SelfHealingAuditCert` — Proves that self-healing was attempted before escalation by exhibiting the remediation log with timestamps, actions taken, and outcomes, showing local remediation preceded any failover.
- `AppP.R4.d`: `GenomeFidelityCert` — Proves that the current deployment matches the genome by exhibiting a diff between the genome's declared state and the deployment's observed state, showing zero unintended divergences.
