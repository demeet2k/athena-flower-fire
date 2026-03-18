<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvT.R3.md
-->

# InvT — Square Lens / Constructions

- `InvT.S3.a`: `ReleaseGateChecker` — For each quarantined entity: verifies that the originating conflict has a resolution proof, checks the proof's validity, and issues the release token if valid. Rejects release if proof is missing, invalid, or incomplete.
- `InvT.S3.b`: `DeltaDocumenter` — For each resolved conflict: records the conflicting states, the resolution choice, the discarded alternative, and the rationale. Outputs the complete delta record for transparency auditing.
- `InvT.S3.c`: `CertificateReissuer` — For each corrected entity that needs re-certification: runs the full verification procedure from scratch (not using any cached results from the revoked certificate). Issues the new certificate only if verification passes.
- `InvT.S3.d`: `HealingRateReporter` — Computes the healing rate (reintegrated / quarantined) over time. Plots the trend. Flags declining trends. Identifies the most common conflict types and recommends systemic fixes.
