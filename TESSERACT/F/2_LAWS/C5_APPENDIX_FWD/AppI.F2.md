<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppI.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppI.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppI.R2.md
-->

# AppI — Flower Lens / Laws

- `AppI.F2.a`: `CorridorFlowContinuityLaw` — Corridor flow must be continuous: no operation may jump from one corridor to another without passing through a declared transition point.
- `AppI.F2.b`: `TruthWaveDampingLaw` — Truth waves must be damped: a single promotion cannot trigger unlimited cascade promotions. Propagation depth is bounded by evidence budget.
- `AppI.F2.c`: `AdmissibilityGradientLaw` — Operations with high admissibility gradient (near corridor edge) must be flagged as sensitive. Sensitive operations require additional certification.
- `AppI.F2.d`: `CorridorTransitionLaw` — Corridor phase transitions must be handled by rotation to shadow/renormalized corridor, not by direct execution at the singularity. The ÷-seed's anti-singularity doctrine.
