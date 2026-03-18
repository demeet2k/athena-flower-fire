<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvR.R3.md
-->

# InvR — Flower Lens / Constructions

- `InvR.F3.a`: `AmplitudeCollapser` — For each corridor: computes the truth amplitude, applies the collapse operator (project to nearest eigenstate), and records the collapsed value. Reports the collapse map.
- `InvR.F3.b`: `PhaseResolver` — For each truth value with intermediate phase: computes the phase angle, applies the rounding protocol, and records the result and rounding error. Reports total rounding error.
- `InvR.F3.c`: `ResonanceClusterer` — Identifies clusters of co-determined corridors using correlation analysis. For each cluster: evaluates one representative and propagates the result to all cluster members. Verifies consistency.
- `InvR.F3.d`: `FixedPointFinder` — Iterates the truth assignment: evaluate all conditions, update all values, repeat until no value changes. Reports the number of iterations and whether a fixed point was reached.
