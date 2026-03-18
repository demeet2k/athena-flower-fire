<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvK -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvK.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvK.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvK.R1.md
-->

# InvK — Cloud Lens / Objects

- `InvK.C1.a`: `AxiomCoverageProbability` — The probability that a randomly chosen law is derivable from the current axiom set. As the axiom set is refined, coverage increases. At coverage = 1, the axiom set is complete — it derives everything. At coverage < 1, there are underivable laws (missing axioms).
- `InvK.C1.b`: `RedundancyEstimate` — The expected fraction of laws in the canon that are derivable from other laws (redundant). High redundancy means the canon is bloated — much compression is possible. Low redundancy means the canon is already near-minimal.
- `InvK.C1.c`: `IndependentAxiomProduct` — If axioms are logically independent (no axiom implies another), the probability of the conjunction of axioms = Π P(axiom_i). The product measures the "prior cost" of the axiom set — how much baseline probability mass the seed's legal foundation consumes.
- `InvK.C1.d`: `LawInformationContent` — Each law's information content: -log₂ P(law | other_laws). Laws with high information content (surprising given others) are likely axioms. Laws with low information content (expected given others) are likely theorems. This ranking helps identify the axiom set.
