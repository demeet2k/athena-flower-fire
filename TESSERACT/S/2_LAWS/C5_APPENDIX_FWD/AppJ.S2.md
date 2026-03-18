<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppJ.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppJ.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppJ.R2.md
-->

# AppJ — Square Lens / Laws

- `AppJ.S2.a`: `ResidualClassificationExhaustiveness` — Every non-exact result must be classified into exactly one of `{NEAR-OK, NEAR-FAIL, NEAR-AMBIG}`. No residual may exist in an unclassified state; the three tags partition the space of near-miss outcomes.
- `AppJ.S2.b`: `CorrectionDebtMonotonicity` — For `NEAR-OK` residuals, the correction debt `δ` must not increase under downstream operations: `δ(f(x)) ≤ δ(x) + ε_f` where `ε_f` is the declared error bound of operation `f`. Debt accumulates additively, never multiplicatively.
- `AppJ.S2.c`: `NearFailBoundedness` — Every `NEAR-FAIL` residual has a finite gap magnitude `δ < ∞` and a classified failure mode from the enumerated set `{TypeMismatch, RangeExceeded, CycleDetected, DependencyMissing}`. Unclassified failures are illegal.
- `AppJ.S2.d`: `LedgerCompleteness` — The residual ledger contains every outstanding residual in the crystal. No residual may exist off-ledger; creation and retirement of residuals are atomic operations that always update the ledger.
