<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvM.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvM.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvM.C1.md
-->

# InvM — Fractal Lens / Objects

- `InvM.R1.a`: `RecursiveRegistryPruning` — The registry has hierarchical structure: global registry → sub-registries per region → local registries per cell. Pruning is recursive: prune local registries first, then sub-registries (which may now have dead entries due to local pruning), then global.
- `InvM.R1.b`: `ProfileDepthContraction` — Each level of profile compression reduces the attribute set. The contraction factor approaches 1/φ for well-designed profiles (each level removes ~38% of remaining attributes).
- `InvM.R1.c`: `RegistryTreeCollapse` — The registry hierarchy collapses from leaves (local registries) to root (global registry). Each collapsed local registry simplifies its parent sub-registry.
- `InvM.R1.d`: `ScaleInvariantPruning` — The pruning protocol is identical at every level: scan reachability, minimize profiles, collapse versions, compute compression. Only the scale changes.
