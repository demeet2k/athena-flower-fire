<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvK.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvK.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvK.R2.md
-->

# InvK — Cloud Lens / Laws

- `InvK.C2.a`: `CoverageCompletenessLaw` — Coverage must equal 1 for the axiom set to be certified complete. Coverage < 1 means laws exist that the axiom set cannot derive — a legal gap.
- `InvK.C2.b`: `RedundancyEliminationLaw` — All identified redundancies must be eliminated from the seed. The seed carries zero redundant laws.
- `InvK.C2.c`: `PriorCostMinimization` — The axiom set should minimize prior cost (Π P(axiom_i) should be maximized, i.e., axioms should be "natural" rather than arbitrary). Arbitrary axioms have high prior cost.
- `InvK.C2.d`: `InformationRankingLaw` — Axiom candidates must be ranked by information content. Highest-information laws are most likely to be genuine axioms.
