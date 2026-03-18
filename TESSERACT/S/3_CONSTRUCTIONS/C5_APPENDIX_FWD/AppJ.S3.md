<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppJ.R3.md
-->

# AppJ — Square Lens / Constructions

- `AppJ.S3.a`: `ResidualClassifier` — The triage engine that takes a raw computation result and its expected target, computes the distance `δ`, and classifies the result into `NEAR-OK`, `NEAR-FAIL`, or `NEAR-AMBIG` based on threshold comparison and candidate-set analysis.
- `AppJ.S3.b`: `CorrectionDebtTracker` — The accumulator that maintains a running debt total `D = Σ δ_i` for each shard, updating as operations compose, and triggering a recalibration event when `D` exceeds the shard's declared tolerance budget.
- `AppJ.S3.c`: `FailureModeAnalyzer` — The analyzer that takes a `NEAR-FAIL` envelope and decomposes its gap into structural components: which conservation law was violated, which address component was out of range, what dependency was missing, outputting a structured repair hint.
- `AppJ.S3.d`: `LedgerCompactor` — The garbage collector that scans the residual ledger for retired entries (resolved residuals with `attempts > 0` and final status `OK`), archives them to the history log, and compacts the active ledger to contain only outstanding residuals.
