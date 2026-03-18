<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvN.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvN.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvN.R1.md
-->

# InvN — Cloud Lens / Objects

- `InvN.C1.a`: `ClockJitterDistribution` — The statistical distribution of clock jitter (timing errors) at the moment of freeze. Well-behaved jitter (narrow, zero-mean Gaussian) means the timestamp is reliable. Pathological jitter (wide, skewed) means the timestamp has significant uncertainty.
- `InvN.C1.b`: `GearSlipProbability` — The probability that a gear slipped (missed a tooth) during the final rotation before freeze. Computed from the gear's historical slip rate and the deceleration profile. Low probability means the final gear position is trustworthy.
- `InvN.C1.c`: `IndependentWheelHalt` — If the four wheels are independent (no shared oscillator), their halt probabilities multiply: P(all halted) = Π P(wheel_i halted). Independence allows verification of each wheel separately.
- `InvN.C1.d`: `TimestampPrecisionNormalization` — The precision of the timestamp normalized by the clock's intrinsic resolution. Precision/resolution = the effective number of significant timing digits. Higher is better — more precise temporal information in the seed.
