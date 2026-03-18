<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvM.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvM.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvM.R2.md
-->

# InvM — Square Lens / Laws

- `InvM.S2.a`: `ReachabilityRequirement` — An entry survives pruning if and only if it is reachable from at least one active reference chain. Unreachable entries are guaranteed dead — no future operation can access them. Reachability is computed conservatively (overestimate reachability to avoid false pruning).
- `InvM.S2.b`: `MinimalProfileSufficiency` — The minimal profile must be sufficient to reconstruct the full profile when combined with the seed's grammar. Sufficiency is tested by: reconstruct(minimal_profile, grammar) = full_profile. If reconstruction fails, the profile is not minimal enough — more attributes must be retained.
- `InvM.S2.c`: `LatestValidLaw` — The surviving version must be the latest version that passed all validation checks. If the latest version failed validation, the previous valid version is retained. No invalid version survives into the seed.
- `InvM.S2.d`: `PruningIdempotenceLaw` — Pruning twice produces the same result as pruning once. The pruned registry is a fixed point of the pruning operation. This guarantees stability.
