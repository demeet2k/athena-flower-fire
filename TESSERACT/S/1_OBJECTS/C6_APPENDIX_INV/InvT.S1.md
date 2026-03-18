<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvT -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvT.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvT.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvT.R1.md
-->

# InvT — Square Lens / Objects

- `InvT.S1.a`: `QuarantineReleaseToken` — The discrete token authorizing release of a quarantined entity. Issued only after the conflict that caused quarantine is fully resolved. The token carries: entity ID, original conflict description, resolution proof, and reintegration target address. Without this token, the quarantine boundary is impermeable.
- `InvT.S1.b`: `ConflictResolutionDelta` — The difference between the conflicting states, now resolved. The delta encodes exactly what changed to eliminate the conflict: which value was chosen, which was discarded, and why. The zero set of the pre-resolution difference = the agreed-upon state.
- `InvT.S1.c`: `RevocationUndoProduct` — Where AppK revoked certificates, InvT may re-issue them if the underlying defect is corrected. The re-issuance product: corrected_entity × new_verification = new_certificate. The new certificate is not the old one reinstated — it is a fresh certificate for the corrected entity.
- `InvT.S1.d`: `ReintegrationQuotient` — The ratio of successfully reintegrated entities to total quarantined entities = the healing rate. A quotient of 1 means all quarantined entities were healed and reintegrated. A quotient < 1 means some entities were permanently discarded (incurable conflicts).
