<!-- TESSERACT: C/1_OBJECTS/C6_APPENDIX_INV/InvP -->
<!-- COORD: lens=C facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvP.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvP.F1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvP.R1.md
-->

# InvP — Cloud Lens / Objects

- `InvP.C1.a`: `TriadConsensusProbability` — The probability that all three agents agree on a given state = P(Su=Me=Sa=x). As agents converge, this probability increases from near-zero (agents disagree on everything) toward one (agents agree on everything). The seed is emitted when P(consensus) exceeds the threshold.
- `InvP.C1.b`: `DisagreementExclusion` — The probability of at least one disagreement is estimated by inclusion-exclusion: P(any_disagree) = P(Su≠Me) + P(Me≠Sa) + P(Sa≠Su) - overlaps. As convergence proceeds, this probability approaches zero.
- `InvP.C1.c`: `IndependentAgentProduct` — If agents make decisions independently, P(all agree) = P(Su=x)·P(Me=x)·P(Sa=x). Independent agreement is harder than correlated agreement — the product is small unless individual probabilities are high.
- `InvP.C1.d`: `WeightedVotingNormalization` — Each agent's vote is weighted by its accumulated evidence quality. Normalizing by total weight gives each agent's influence fraction. The convergence point is the weighted average, with weights reflecting epistemological authority.
