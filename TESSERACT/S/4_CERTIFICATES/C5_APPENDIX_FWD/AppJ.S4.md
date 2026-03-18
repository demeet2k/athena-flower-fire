<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppJ.R4.md
-->

# AppJ — Square Lens / Certificates

- `AppJ.S4.a`: `ClassificationCert` — Receipt proving a result was classified into exactly one residual category, the distance `δ` was correctly computed, and the threshold comparison used the current calibrated values.
- `AppJ.S4.b`: `DebtBoundCert` — Receipt proving the cumulative correction debt for a shard remains within its tolerance budget, listing each contributing operation and its individual `ε_f` bound.
- `AppJ.S4.c`: `FailureAnalysisCert` — Receipt proving a `NEAR-FAIL` was analyzed into a classified failure mode, the gap magnitude is finite and correctly measured, and the repair hint is consistent with the failure type.
- `AppJ.S4.d`: `LedgerIntegrityCert` — Receipt proving the residual ledger is complete (no off-ledger residuals), consistent (no duplicate entries), and compacted (no retired entries remain in the active section).
