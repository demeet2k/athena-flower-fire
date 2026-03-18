<!-- TESSERACT: C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=C facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.F3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.R3.md
-->

# InvS — Cloud Lens / Constructions

- `InvS.C3.a`: `DistributionAnalyzer` — Fits the residual distribution using moment estimation. Tests for zero mean, normality, and heavy tails. Reports the distribution type and any required pre-processing (bias correction, tail handling).
- `InvS.C3.b`: `ErrorAuditor` — For each NEAR approximation: computes actual error, compares against declared bound, flags any bound violations. Reports the audit results and recommendations.
- `InvS.C3.c`: `CorrelationChecker` — Tests pairwise correlation of residuals at different cells. Reports the correlation matrix. Authorizes parallel absorption for uncorrelated cells and coordinates absorption for correlated clusters.
- `InvS.C3.d`: `CostBenefitAnalyzer` — For each truncated bit: estimates recovery cost and accuracy value. Computes the value/cost ratio. Ranks by ratio. Recommends recovery for high-ratio bits and permanent loss for low-ratio bits.
