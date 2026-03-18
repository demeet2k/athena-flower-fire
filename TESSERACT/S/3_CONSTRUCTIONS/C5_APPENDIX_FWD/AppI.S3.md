<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppI.R3.md
-->

# AppI — Square Lens / Constructions

- `AppI.S3.a`: `CorridorTester` — Tests whether a corridor is open for a given operation. Returns: `OPEN` (proceed), `CLOSED` (abort), or `AMBIG` (insufficient evidence). Source: ÷-seed's gate condition.
- `AppI.S3.b`: `TruthPromoter` — Promotes a truth tag from one level to the next when sufficient evidence is provided. Enforces monotonicity. Records promotion receipt.
- `AppI.S3.c`: `AbstentionRecorder` — Records an abstention decision with partial evidence, reason for abstention, and re-entry conditions. The claim stays tagged `AMBIG` until new evidence arrives.
- `AppI.S3.d`: `CorridorBudgetManager` — Tracks corridor budget consumption. Triggers abstention when budget exhausted. Allocates budget to highest-priority corridor tests first.
