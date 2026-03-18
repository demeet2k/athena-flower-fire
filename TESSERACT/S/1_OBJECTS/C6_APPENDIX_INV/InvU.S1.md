<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvU -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvU.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvU.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvU.R1.md
-->

# InvU — Square Lens / Objects

- `InvU.S1.a`: `VerdictAccumulator` — The discrete accumulation of evidence reaches a threshold and tips into a verdict. The successor function becomes "one more piece of evidence toward final judgment." Each piece of evidence is a weighted vote; when the weighted sum crosses the decision boundary, the verdict is emitted. No more evidence is needed — the question is closed.
- `InvU.S1.b`: `AMBIGDifferenceResolver` — The difference between the AMBIG state's competing hypotheses. If `Δ(H₁, H₂) > threshold`, the hypotheses are distinguishable and the stronger one wins. If `Δ < threshold`, the hypotheses merge into a single unified verdict. The zero set of the difference identifies the undecidable core — resolved by convention rather than evidence.
- `InvU.S1.c`: `EvidenceChainProduct` — The multiplicative composition of all evidence links in a chain: each link's credibility × relevance × weight. The chain product is the total evidentiary force. Chains with any zero-credibility link have zero total force — one fraudulent piece of evidence invalidates the entire chain.
- `InvU.S1.d`: `PromotionInversion` — Where AppL promoted ambiguous states upward (AMBIG → higher authority), InvU demotes resolved states downward (verdict → execution layer). The quotient: promoted_count / resolved_count measures the system's resolution efficiency. A quotient of 1 means every promotion was eventually resolved.
