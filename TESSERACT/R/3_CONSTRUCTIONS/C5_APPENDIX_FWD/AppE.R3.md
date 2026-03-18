<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.C3.md
-->

# AppE — Fractal Lens / Constructions

- `AppE.R3.a`: `NestedClockBuilder` — Constructs the hierarchical clock from declared moduli at each level. Wires carry propagation between levels.
- `AppE.R3.b`: `LogPeriodicPhaseDetector` — Detects log-periodic phase signatures in clock data. Identifies governing scaling constant.
- `AppE.R3.c`: `CarryCascadeSimulator` — Simulates recursive carry propagation to verify termination and correct digit updates at each level.
- `AppE.R3.d`: `CircleGearScaler` — Constructs the isomorphism between circle gears at two different scales using the φ-lens frequency rescaling.
