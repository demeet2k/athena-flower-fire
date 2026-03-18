<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvX.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvX.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvX.R2.md
-->

# InvX — Cloud Lens / Laws

- `InvX.C2.a`: `StatisticalIntegrityLaw` — The sampling-based verification must achieve at least the declared confidence level. If the sample reveals too many corruptions, the entire bundle must be individually verified (fallback to full scan).
- `InvX.C2.b`: `CorruptionBoundLaw` — The estimated corruption probability must be below the organism's declared tolerance. Bundles exceeding tolerance are rejected or quarantined for individual shard verification.
- `InvX.C2.c`: `ParallelizationSafetyLaw` — Parallel absorption is only legal when shards are verified independent. If any cross-reference exists, the dependent shards must be absorbed sequentially to maintain reference consistency.
- `InvX.C2.d`: `SourceTrustCalibrationLaw` — The historical corruption rate for each source must be recalibrated after each import. Sources whose rate increases beyond tolerance are flagged for audit.
