<!-- TESSERACT: C/1_OBJECTS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=C facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppF.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppF.F1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppF.R1.md
-->

# AppF — Cloud Lens / Objects

- `AppF.C1.a`: `TransportConfidenceField` — The probabilistic admissibility surface over all available lens charts, representing the system's confidence that each chart transport will preserve the seed's truth.
- `AppF.C1.b`: `ChartSelectionDistribution` — The probability distribution over available charts for a given operation, reflecting which chart is most likely to produce the simplest or most reliable transport.
- `AppF.C1.c`: `CorridorRiskSurface` — The probability that a given transport corridor will fail (inverse doesn't exist, denominator zero, chart singular). The ÷-seed's admissibility test expressed probabilistically.
- `AppF.C1.d`: `DualRouteBalanceField` — The ratio of forward-to-backward transport reliability, measuring how symmetric the dual legality is for a given seed-constant pair.
