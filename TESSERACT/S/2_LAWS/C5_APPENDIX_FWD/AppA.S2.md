<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppA.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppA.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppA.R2.md
-->

# AppA — Square Lens / Laws

- `AppA.S2.a`: `AddressUniquenessLaw` — Every shard in the crystal occupies exactly one Xi108 address; no two shards share the same `(shell, wreath, arch, face, dim)` tuple. Violations trigger quarantine via AppK conflict protocols.
- `AppA.S2.b`: `StationCodeBijectivity` — The mapping `ChNN<CODE> ↔ Xi108[...]` is injective: each chapter station maps to a unique crystal address, and each crystal address maps to at most one chapter station. Orphan addresses are legal; duplicate mappings are not.
- `AppA.S2.c`: `ShellOrderPreservation` — If shard `A` is at shell `s_A` and shard `B` is at shell `s_B` with `s_A < s_B`, then `A` is strictly inner to `B` in the crystal partial order. Shell index monotonically encodes depth-from-seed.
- `AppA.S2.d`: `ArchetypeExclusivity` — A shard's archetype mode `a ∈ {E,W,F,A}` (Earth, Water, Fire, Air) is invariant under address transformations; no legal operation changes a shard's elemental assignment within a single crystal cycle.
