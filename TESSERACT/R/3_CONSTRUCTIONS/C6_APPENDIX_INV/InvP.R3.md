<!-- TESSERACT: R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=R facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvP.C3.md
-->

# InvP — Fractal Lens / Constructions

- `InvP.R3.a`: `RecursiveTriadResolver` — Traverses the triad tree bottom-up. At each leaf triad: converges the three agents, emits the unified point. At each parent: receives child unifications and resolves its own triad using the simplified structure.
- `InvP.R3.b`: `ContractionCounter` — Counts agents at each level before and after resolution. Verifies 3→1 contraction. Reports the contraction profile.
- `InvP.R3.c`: `TreeCollapseTracker` — Tracks total remaining triads. Verifies monotone decrease. Reports progress toward full collapse (single point).
- `InvP.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Confirms identity. Reports deviations.
