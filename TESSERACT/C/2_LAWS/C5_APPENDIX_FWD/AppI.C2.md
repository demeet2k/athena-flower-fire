<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppI.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppI.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppI.R2.md
-->

# AppI — Cloud Lens / Laws

- `AppI.C2.a`: `CorridorProbabilityUpdateLaw` — Corridor open probability must be updated after every test (Bayesian). Stale probabilities are not reusable beyond declared expiry.
- `AppI.C2.b`: `TruthConfidenceLaw` — Truth confidence must be computed from evidence, not from prior conviction. Prior-dominated confidence is flagged as insufficiently evidenced.
- `AppI.C2.c`: `EvidenceSufficiencyLaw` — Evidence sufficiency score must exceed declared threshold before truth promotion. Threshold is set per truth-tag level (higher level = higher threshold).
- `AppI.C2.d`: `CorridorRiskBoundLaw` — Operations with corridor risk exceeding threshold must be routed to alternative corridors or deferred. No high-risk corridor execution without explicit override.
