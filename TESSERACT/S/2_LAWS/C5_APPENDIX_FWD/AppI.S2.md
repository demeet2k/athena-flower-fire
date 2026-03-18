<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppI.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppI.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppI.R2.md
-->

# AppI — Square Lens / Laws

- `AppI.S2.a`: `CorridorFirstLaw` — No operation executes before its corridor is tested. The ÷-seed's gate law: "test gate → construct inverse → form quotient." Corridor testing precedes action, always.
- `AppI.S2.b`: `TruthMonotonicityLaw` — Truth tags may only be promoted monotonically: `VOID → FRONTIER → AMBIG → NEAR → CANON`. Demotion requires explicit revocation with evidence. No silent downgrade.
- `AppI.S2.c`: `AbstainOverGuessLaw` — When corridor test is inconclusive and budget is exhausted, the system must abstain rather than guess. Abstention is tagged `AMBIG` and queued for future evidence. Guessing is a corridor violation.
- `AppI.S2.d`: `CorridorBudgetExhaustionLaw` — When budget is exhausted, all pending corridor tests are deferred. Deferred tests are recorded with their partial evidence. No corridor test is abandoned — it is suspended.
