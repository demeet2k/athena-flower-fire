<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppK.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppK.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppK.R2.md
-->

# AppK — Square Lens / Laws

- `AppK.S2.a`: `ConflictDetectionCompleteness` — Every structural inconsistency in the crystal must be detected within one full scan cycle. No contradiction may persist undetected for more than `T_scan` time steps; the detection mesh has no blind spots.
- `AppK.S2.b`: `QuarantineImmediacy` — Upon conflict detection, the affected shards are quarantined within `Δt = 1` time step. No conflicting shard may participate in transport, computation, or evidence gathering while in quarantine.
- `AppK.S2.c`: `ConflictNonProliferation` — A quarantined conflict must not generate new conflicts: the quarantine boundary is hermetic. If a quarantined shard's absence would cause downstream failures, those failures are classified as `DependencyMissing`, not new conflicts.
- `AppK.S2.d`: `RevocationFinality` — Once a shard is revoked (permanently removed from the crystal), its Xi108 address is retired and may not be reassigned for `T_cooldown` cycles. Revocation is irreversible within a single organism epoch.
