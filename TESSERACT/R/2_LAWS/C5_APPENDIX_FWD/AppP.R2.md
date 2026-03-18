<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppP.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppP.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppP.C2.md
-->

# AppP — Fractal Lens / Laws

- `AppP.R2.a`: `SelfConfigurationIdempotencyLaw` — A self-configuring server must produce identical configuration regardless of how many times it re-reads the manifest; configuration is a pure function of the manifest content.
- `AppP.R2.b`: `ScalingBoundednessLaw` — Auto-scaling must respect the minimum and maximum instance counts defined in the policy; no scaling action may produce an instance count outside these bounds.
- `AppP.R2.c`: `SelfHealingEscalationLaw` — Self-healing must attempt local remediation before escalating; direct escalation without attempted self-healing is a violation unless the degradation is classified as non-remediable.
- `AppP.R2.d`: `GenomeBootstrapDeterminismLaw` — Bootstrapping a deployment from the same genome on the same infrastructure must produce identical deployments; the genome is a deterministic specification, not a stochastic process.
