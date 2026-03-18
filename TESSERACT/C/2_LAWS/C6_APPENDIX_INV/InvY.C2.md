<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvY -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvY.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvY.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvY.R2.md
-->

# InvY — Cloud Lens / Laws

- `InvY.C2.a`: `HighConfidenceShutdownLaw` — P(clean_shutdown) must exceed the deployment's declared reliability threshold (typically 1 - 10^{-6}). If the probability falls below threshold, shutdown is paused for remediation.
- `InvY.C2.b`: `IncidentResolutionLaw` — All genuine incidents must be resolved (or deferred with explicit debt certificates) before shutdown is certified. Unresolved incidents block certification.
- `InvY.C2.c`: `IndependenceVerificationLaw` — The independence assumption for drain factorization must be verified by testing for shared state. If slots share state, the joint drain probability cannot be factorized and must be computed directly.
- `InvY.C2.d`: `RiskBudgetExhaustionLaw` — The total residual risk after shutdown must be within the seed's risk budget. Excess risk is carried as debt. The debt must be finite and bounded.
