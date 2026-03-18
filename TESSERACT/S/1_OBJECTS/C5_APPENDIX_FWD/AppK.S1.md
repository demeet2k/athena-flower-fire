<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppK -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppK.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppK.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppK.R1.md
-->

# AppK — Square Lens / Objects

- `AppK.S1.a`: `TypeCollisionPacket` — A conflict record emitted when two shards claim the same Xi108 address with incompatible types: `Conflict(addr, type_A, type_B, timestamp)`. The packet freezes both claimants until resolution, preserving the pre-collision state of each.
- `AppK.S1.b`: `ConservationViolationPacket` — A conflict record emitted when a transport path violates one of the six conservation laws (AppB): `Violation(law_id, Δ_observed, Δ_expected, path)`. The packet flags the specific law broken and the magnitude of the breach.
- `AppK.S1.c`: `AddressCollisionRecord` — A structural inconsistency where two distinct shards are assigned identical `(shell, wreath, arch, face, dim)` tuples, violating AppA's `AddressUniquenessLaw`. Records both shards' content hashes for forensic comparison.
- `AppK.S1.d`: `CyclicDependencyTrap` — A conflict detected when the dependency graph contains a cycle `A → B → C → A`, making topological sort impossible. Records the full cycle path, the depth at which it was detected, and the edge types (data, control, phase).
