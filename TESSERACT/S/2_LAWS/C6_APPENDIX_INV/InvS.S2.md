<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvS.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvS.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvS.R2.md
-->

# InvS — Square Lens / Laws

- `InvS.S2.a`: `TotalResidualZeroLaw` — At compression completion, the total residual across all cells must be exactly zero. Any non-zero total indicates incomplete absorption — the compression is not finished.
- `InvS.S2.b`: `NEARCompletionMandateLaw` — Every NEAR value must be resolved to exact (or to a certified-irrational with declared approximation bounds). No NEAR approximation survives into the seed. The seed carries only exact values and explicit irrational certificates.
- `InvS.S2.c`: `RedistributionConservationLaw` — Redistribution must conserve the total residual exactly. The sum of shares distributed to neighbors must equal the original residual. No residual may be created or destroyed during redistribution — only moved.
- `InvS.S2.d`: `TruncationRecoveryLaw` — All truncated precision must be recovered. The truncation quotient must reach 1. If recovery is impossible (the truncated bits were irreversibly lost), a truncation-loss certificate must be issued declaring the permanent precision deficit.
