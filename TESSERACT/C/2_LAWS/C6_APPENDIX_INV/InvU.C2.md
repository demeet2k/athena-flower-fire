<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvU.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvU.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvU.R2.md
-->

# InvU — Cloud Lens / Laws

- `InvU.C2.a`: `MAPOptimalityLaw` — The MAP verdict minimizes expected loss under the posterior. Any other verdict has higher expected loss. This is the Bayesian justification for the verdict.
- `InvU.C2.b`: `AMBIGVanishingLaw` — The AMBIG probability must vanish (approach zero) as evidence accumulates without bound. If AMBIG persists despite unbounded evidence, the hypotheses are genuinely indistinguishable and must be merged.
- `InvU.C2.c`: `IndependenceVerificationLaw` — The independence assumption must be verified before likelihood factorization. Dependent evidence that is treated as independent inflates confidence — a dangerous error.
- `InvU.C2.d`: `DiminishingReturnsLaw` — Information gain per piece of evidence must eventually diminish. Early evidence is most informative; late evidence is confirmatory. The compression protocol releases confirmatory evidence first (it adds least new information).
