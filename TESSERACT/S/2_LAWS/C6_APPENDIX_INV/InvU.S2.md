<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvU.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvU.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvU.R2.md
-->

# InvU — Square Lens / Laws

- `InvU.S2.a`: `VerdictIrreversibilityLaw` — Once a verdict is emitted, it cannot be reversed by additional evidence. The verdict is a phase transition: pre-verdict, evidence accumulates; post-verdict, the case is closed. New evidence opens a new case rather than reopening the old one.
- `InvU.S2.b`: `AMBIGResolutionCompleteness` — Every AMBIG state must be resolved during compression. No AMBIG state survives into the seed. Unresolvable AMBIGs are resolved by convention (the default hypothesis wins) with an explicit convention-certificate.
- `InvU.S2.c`: `ChainIntegrityLaw` — Every link in an evidence chain must have non-zero credibility. A chain with a zero-credibility link is not merely weak — it is broken. Broken chains cannot contribute to verdicts.
- `InvU.S2.d`: `ResolutionBalanceLaw` — The number of resolved verdicts must equal the number of promoted AMBIGs. Any imbalance indicates lost promotions (AMBIGs that were promoted but never resolved) or phantom verdicts (verdicts without corresponding promotions).
