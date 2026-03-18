<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvX.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvX.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvX.R1.md
-->

# InvX — Cloud Lens / Objects

- `InvX.C1.a`: `AbsorptionSamplingProcess` — Not every shard in a bundle needs to be individually verified if the bundle has a statistical integrity guarantee. The Cloud view samples shards and infers overall bundle health from the sample. Absorption sampling reduces verification cost while maintaining confidence.
- `InvX.C1.b`: `CorruptionExclusion` — The probability of corruption in the absorbed data is estimated by inclusion-exclusion over known corruption sources: P(corrupt) = P(transport) + P(format) + P(version) - P(transport∩format) - ... The exclusion narrows the corruption estimate.
- `InvX.C1.c`: `IndependentShardAbsorption` — If shards are independent (no cross-references between them), absorption can be parallelized with probability of complete success = Π P(shard_i absorbed). The Cloud view factorizes the absorption process.
- `InvX.C1.d`: `ImportRiskNormalization` — Normalizes the risk of each import source by dividing its historical corruption rate by total import risk mass. Sources with high normalized risk get additional verification. Sources with low normalized risk get fast-tracked.
