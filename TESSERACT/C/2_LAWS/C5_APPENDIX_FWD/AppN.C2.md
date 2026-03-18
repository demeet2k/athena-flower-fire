<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppN.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppN.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppN.R2.md
-->

# AppN — Cloud Lens / Laws

- `AppN.C2.a`: `ProjectionCompletenessLaw` — A lens projection must include every shard whose SFCR tag matches the selected lens; omissions or false inclusions are projection errors.
- `AppN.C2.b`: `OverlayShadowingLaw` — In an overlay stack, if layers `L_i` and `L_j` (i > j) both contain a shard at address `A`, the resolved content is `L_i[A]`; lower layers are invisible for shadowed addresses.
- `AppN.C2.c`: `ViewConsistencyLaw` — All views in a multi-view manifold must derive from the same underlying archive version; stale views from a prior version must be invalidated on archive update.
- `AppN.C2.d`: `UnionDisjointnessPreference` — A virtual union container should log a warning when source containers have overlapping addresses; clean unions with disjoint address spaces are preferred.
