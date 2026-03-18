<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvU.R3.md
-->

# InvU — Square Lens / Constructions

- `InvU.S3.a`: `ThresholdEvaluator` — For each pending AMBIG: sums the weighted evidence, compares against the decision boundary, and emits a verdict if crossed. If not crossed after all evidence is consumed, emits a convention-verdict with explicit declaration.
- `InvU.S3.b`: `HypothesisDiffer` — For each AMBIG with competing hypotheses: computes the difference in support, classifies as distinguishable (Δ > threshold) or mergeable (Δ < threshold), and emits either the winning hypothesis or the merged verdict.
- `InvU.S3.c`: `ChainValidator` — Traverses each evidence chain link by link. Verifies non-zero credibility at each link. Reports broken chains and their breaking point. Computes total chain force for intact chains.
- `InvU.S3.d`: `PromotionReconciler` — Matches each promotion record from AppL against its resolution record in InvU. Reports matched pairs, unmatched promotions (leaks), and unmatched verdicts (phantoms).
