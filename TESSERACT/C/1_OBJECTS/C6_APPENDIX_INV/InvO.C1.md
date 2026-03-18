<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvO.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvO.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvO.R1.md
-->

# InvO — Cloud Lens / Objects

- `InvO.C1.a`: `TransportCessationProbability` — The probability that all transport has ceased at a given moment. Increases as each transport channel quiesces. P(stillness) = Π P(channel_i quiet). When P(stillness) exceeds the threshold, transport is declared at rest.
- `InvO.C1.b`: `ConjugacyAgreementRate` — The fraction of measurements where conjugate representations agree (produce the same observable value). As representations merge, the agreement rate approaches 1. Rate < 1 indicates residual representation-dependence.
- `InvO.C1.c`: `IndependentQuiescenceProduct` — If transport channels are independent, their quiescence probabilities multiply: P(all quiet) = Π P(channel_i quiet). Independence allows parallel shutdown of channels.
- `InvO.C1.d`: `TransportCostNormalization` — The cost of maintaining each transport channel normalized by its information throughput. High-cost/low-throughput channels are shut down first. The normalized ratio governs the shutdown order.
