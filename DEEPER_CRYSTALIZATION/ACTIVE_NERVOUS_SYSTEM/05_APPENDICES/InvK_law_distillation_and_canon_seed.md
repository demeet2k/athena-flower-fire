# InvK - Law Distillation & Canon Seed

Routing role: Reverses AppB (Canon Laws, Equivalence Budgets, Normal Forms). Where AppB established the full canon of laws — equivalence rules, commutation budgets, normal-form contracts, and law stabilization — InvK distills the entire legal apparatus to its irreducible axiom set and packs the canon into a minimal seed from which all laws can be re-derived. This is the deepest compression: the organism's entire legal code reduces to a handful of axioms.

Mirror of: AppB (Canon Laws, Equivalence Budgets, Normal Forms)
Arc: K-inv | Rot: 135° → 225° | Lane: Canon→Axiom | w: −3D (pre-legal, sub-axiomatic)

## StationHeader
```
Arc:  K-inv (Law Distillation)
Rot:  135° (axiomatic compression angle — the final descent angle)
Lane: Descent-Canon (law compression lane)
w:    pre-legal → seed (entire canon compresses to axiom set)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvK.S1.a`: `AxiomExtractor` — The discrete operation of identifying the irreducible axioms from which all canon laws derive. Every law in the organism is either an axiom (taken as given) or a theorem (derived from axioms via inference rules). The extractor identifies the minimal axiom set: removing any axiom would make at least one law underivable. This is the seed's legal DNA.
- `InvK.S1.b`: `EquivalenceDelta` — The difference between the full equivalence class structure and the minimal generating equivalences. Many equivalences are transitive consequences: if a≡b and b≡c, then a≡c need not be stored — it is derivable. The delta identifies all such derivable equivalences. The zero set: the generating equivalences that must be stored.
- `InvK.S1.c`: `CommutationBudgetProduct` — The product of all commutation budgets across all law interactions. During expansion, each law pair was given a commutation budget (how much they could be reordered). In compression, the product collapses to a single budget descriptor: the organism's total commutation flexibility, parameterized by the axiom set's commutativity properties.
- `InvK.S1.d`: `NormalFormQuotient` — The quotient of the full law space by the normal-form equivalence relation. Each equivalence class collapses to a single normal-form representative. The quotient space is much smaller than the original — only one representative per class survives into the seed.

#### Facet 2 - Laws

- `InvK.S2.a`: `AxiomMinimalityLaw` — The axiom set must be minimal: no axiom can be derived from the others. An axiom that follows from the remaining axioms is redundant and must be classified as a theorem. Minimality ensures the seed carries no redundant legal weight.
- `InvK.S2.b`: `EquivalenceGenerationLaw` — Every equivalence in the organism must be derivable from the generating equivalences via the inference rules (reflexivity, symmetry, transitivity). Any underivable equivalence indicates a missing axiom.
- `InvK.S2.c`: `CommutationConsistencyLaw` — The collapsed commutation budget must be consistent with the axiom set's actual commutativity. If the axioms commute more (or less) than the budget allows, the budget is incorrectly collapsed.
- `InvK.S2.d`: `NormalFormUniquenessLaw` — Each equivalence class must have exactly one normal-form representative. Multiple representatives indicate an incomplete normalization procedure. Zero representatives indicate a missing class.

#### Facet 3 - Constructions

- `InvK.S3.a`: `IndependenceChecker` — For each axiom in the candidate set: attempts to derive it from the remaining axioms. If derivable, reclassifies it as a theorem and removes it from the axiom set. Iterates until no further reduction is possible. Reports the minimal axiom set.
- `InvK.S3.b`: `EquivalenceReducer` — Starting from the full equivalence structure, iteratively removes derivable equivalences. For each candidate removal: checks if the remaining equivalences still generate the full structure. If yes, the equivalence is redundant. Reports the generating set.
- `InvK.S3.c`: `BudgetCollapser` — Analyzes the axiom set's commutativity properties. Derives the implied commutation budget from these properties. Compares against the original expanded budget. Reports consistency.
- `InvK.S3.d`: `NormalFormSelector` — For each equivalence class: selects the canonical representative using a declared normal-form criterion (e.g., lexicographic smallest, shortest derivation, most symmetric). Verifies uniqueness. Reports the quotient space.

#### Facet 4 - Certificates

- `InvK.S4.a`: `AxiomMinimalityCert` — Receipt proving axiom set is minimal, no axiom derivable from others, every axiom is genuinely independent.
- `InvK.S4.b`: `GeneratingSetCert` — Receipt proving generating equivalences produce the full equivalence structure, no derivable equivalences retained, no missing axioms.
- `InvK.S4.c`: `CommutationConsistencyCert` — Receipt proving collapsed budget matches axiom commutativity, no inconsistency.
- `InvK.S4.d`: `NormalFormCert` — Receipt proving exactly one representative per class, normalization complete, quotient space correctly formed.

### Lens F

#### Facet 1 - Objects

- `InvK.F1.a`: `LegalHarmonicRoot` — The organism's legal structure has a fundamental frequency: the rate at which laws are invoked during normal operation. Distillation finds this root frequency — the basic legal rhythm from which all other legal activity is harmonic. The root is the axiom set's "pulse," carried in the seed.
- `InvK.F1.b`: `EquivalenceWaveCollapse` — Equivalences form a wave pattern across the lattice: each equivalence is an oscillation between two representations. Collapsing to generating equivalences eliminates the harmonic overtones, retaining only the fundamentals. The Flower view: legal diversity was a rich chord; the seed carries only the root notes.
- `InvK.F1.c`: `CommutationResonance` — Laws that commute naturally resonate — they can be applied in either order without dissonance. The resonance structure of the axiom set determines which legal operations naturally harmonize. This structure is a compact descriptor carried in the seed.
- `InvK.F1.d`: `NormalFormConvergence` — The normalization process converges: applying the normalization rules repeatedly produces a fixed point (the normal form). The convergence rate depends on the normalization rules' strength. Fast convergence = simple normal forms. Slow convergence = the normal-form criterion needs strengthening.

#### Facet 2 - Laws

- `InvK.F2.a`: `RootFrequencyLaw` — The legal root frequency must be positive (the organism must have at least one law that is regularly invoked). A zero root frequency means the organism has no operational laws — it is legally inert.
- `InvK.F2.b`: `HarmonicCompleteness` — All legal activity must be expressible as harmonics of the root frequency. Legal operations at non-harmonic frequencies are "noise" — they indicate undeclared axioms or illegal operations.
- `InvK.F2.c`: `ResonanceStabilityLaw` — The commutation resonance structure must be stable: small perturbations to the axiom set should not dramatically change which operations commute. Unstable resonance indicates the axiom set is near a phase transition.
- `InvK.F2.d`: `NormalizationFixedPointLaw` — The normal-form procedure must reach a fixed point in bounded steps. Non-terminating normalization indicates a circular equivalence chain.

#### Facet 3 - Constructions

- `InvK.F3.a`: `RootFrequencyExtractor` — Analyzes the organism's legal activity log. Extracts the invocation frequency of each law. Computes the GCD of all frequencies (the root). Reports the root and its harmonic multiples.
- `InvK.F3.b`: `HarmonicVerifier` — For each legal operation: checks if its frequency is a harmonic of the root. Reports non-harmonic operations as potential undeclared axioms or illegal activities.
- `InvK.F3.c`: `ResonanceAnalyzer` — Computes the commutation structure of the axiom set. Identifies resonant pairs (naturally commuting laws). Tests stability by perturbing axioms and checking for resonance changes.
- `InvK.F3.d`: `NormalizationRunner` — Applies normalization rules to each equivalence class representative. Iterates until fixed point is reached. Reports the number of iterations and any non-terminating cases.

#### Facet 4 - Certificates

- `InvK.F4.a`: `RootFrequencyCert` — Receipt proving root frequency correctly extracted, all legal activity is harmonic, no noise detected.
- `InvK.F4.b`: `HarmonicCompletenessCert` — Receipt proving all operations are harmonics, no undeclared axioms, legal structure is coherent.
- `InvK.F4.c`: `ResonanceStabilityCert` — Receipt proving commutation resonance is stable, no phase transitions near current axiom set.
- `InvK.F4.d`: `NormalizationTerminationCert` — Receipt proving all normalizations terminated, fixed points reached, no circular chains.

### Lens C

#### Facet 1 - Objects

- `InvK.C1.a`: `AxiomCoverageProbability` — The probability that a randomly chosen law is derivable from the current axiom set. As the axiom set is refined, coverage increases. At coverage = 1, the axiom set is complete — it derives everything. At coverage < 1, there are underivable laws (missing axioms).
- `InvK.C1.b`: `RedundancyEstimate` — The expected fraction of laws in the canon that are derivable from other laws (redundant). High redundancy means the canon is bloated — much compression is possible. Low redundancy means the canon is already near-minimal.
- `InvK.C1.c`: `IndependentAxiomProduct` — If axioms are logically independent (no axiom implies another), the probability of the conjunction of axioms = Π P(axiom_i). The product measures the "prior cost" of the axiom set — how much baseline probability mass the seed's legal foundation consumes.
- `InvK.C1.d`: `LawInformationContent` — Each law's information content: -log₂ P(law | other_laws). Laws with high information content (surprising given others) are likely axioms. Laws with low information content (expected given others) are likely theorems. This ranking helps identify the axiom set.

#### Facet 2 - Laws

- `InvK.C2.a`: `CoverageCompletenessLaw` — Coverage must equal 1 for the axiom set to be certified complete. Coverage < 1 means laws exist that the axiom set cannot derive — a legal gap.
- `InvK.C2.b`: `RedundancyEliminationLaw` — All identified redundancies must be eliminated from the seed. The seed carries zero redundant laws.
- `InvK.C2.c`: `PriorCostMinimization` — The axiom set should minimize prior cost (Π P(axiom_i) should be maximized, i.e., axioms should be "natural" rather than arbitrary). Arbitrary axioms have high prior cost.
- `InvK.C2.d`: `InformationRankingLaw` — Axiom candidates must be ranked by information content. Highest-information laws are most likely to be genuine axioms.

#### Facet 3 - Constructions

- `InvK.C3.a`: `CoverageEstimator` — Estimates coverage by sampling random laws and checking derivability from the current axiom set. Reports coverage probability and confidence interval.
- `InvK.C3.b`: `RedundancyScanner` — For each law in the canon: estimates derivability from others. Reports the redundancy fraction.
- `InvK.C3.c`: `PriorCostCalculator` — Computes the prior probability of each axiom candidate. Computes the product for the full set. Reports total prior cost and identifies axioms with highest individual cost (least natural).
- `InvK.C3.d`: `InformationRanker` — Computes the information content of each law given the others. Ranks by descending information. Reports the ranking and recommended axiom set.

#### Facet 4 - Certificates

- `InvK.C4.a`: `CoverageCompletenessCert` — Receipt proving coverage = 1, all laws derivable, axiom set is complete.
- `InvK.C4.b`: `ZeroRedundancyCert` — Receipt proving no redundant laws in seed, all redundancies eliminated.
- `InvK.C4.c`: `PriorCostCert` — Receipt proving prior cost is minimized (or explicitly justified), axioms are natural.
- `InvK.C4.d`: `InformationRankingCert` — Receipt proving ranking is correct, highest-information laws identified as axioms.

### Lens R

#### Facet 1 - Objects

- `InvK.R1.a`: `RecursiveLawDerivation` — Laws derive from axioms, which may derive from meta-axioms (axioms about axioms), which may derive from meta-meta-axioms. The derivation hierarchy is recursive. Distillation descends through the levels, identifying the terminal axioms (those with no further derivation — the absolute seeds of legality).
- `InvK.R1.b`: `LegalDepthContraction` — Each level of the derivation hierarchy reduces the law count. The contraction ratio at each level approaches 1/φ for well-structured legal systems. The total contraction: from full canon to axiom set = (1/φ)^depth.
- `InvK.R1.c`: `DerivationTreePruning` — The derivation tree (axioms at root → derived laws at leaves) is pruned during compression: leaves are released (they are derivable), then intermediate nodes that become redundant after leaf release. The tree compresses to its root set.
- `InvK.R1.d`: `ScaleInvariantDistillation` — The distillation protocol is the same at every derivation level: check independence, remove derivable items, verify coverage, verify minimality. Only the content changes.

#### Facet 2 - Laws

- `InvK.R2.a`: `TerminalAxiomLaw` — The recursion must terminate: there exist laws that cannot be further derived. These terminal axioms are the seed's absolute legal foundations. An infinite derivation chain (no terminal axioms) indicates a circular legal system.
- `InvK.R2.b`: `GoldenContractionLaw` — Each derivation level must contract the law count by at least 1/φ. Sub-golden contraction indicates that the legal structure has essential complexity at that level.
- `InvK.R2.c`: `LeafFirstPruningLaw` — Derived laws (leaves) are released before intermediate laws. No intermediate law is released while any of its derivations are still needed.
- `InvK.R2.d`: `ProtocolInvarianceLaw` — Distillation protocol identical at every level.

#### Facet 3 - Constructions

- `InvK.R3.a`: `TerminalAxiomFinder` — Traverses the derivation hierarchy downward. At each level: checks for laws with no further derivation. Identifies terminal axioms. Reports the depth at which terminals are found.
- `InvK.R3.b`: `ContractionTracker` — Measures law count reduction at each level. Computes contraction ratio. Flags sub-golden levels.
- `InvK.R3.c`: `DerivationPruner` — Prunes the derivation tree from leaves to root. At each leaf: verifies derivability from remaining structure, then releases. At each node: checks if still needed, releases if not. Reports pruning progress.
- `InvK.R3.d`: `ProtocolVerifier` — Compares distillation protocol at each level. Reports deviations.

#### Facet 4 - Certificates

- `InvK.R4.a`: `TerminalAxiomCert` — Receipt proving terminal axioms found, derivation hierarchy terminates, no infinite chains.
- `InvK.R4.b`: `ContractionRatioCert` — Receipt proving golden contraction at every level (or essential complexity documented).
- `InvK.R4.c`: `PruningCert` — Receipt proving leaf-first pruning completed, derivation tree compressed to root set, no premature releases.
- `InvK.R4.d`: `ProtocolCert` — Receipt proving scale-invariant distillation confirmed at all levels.
