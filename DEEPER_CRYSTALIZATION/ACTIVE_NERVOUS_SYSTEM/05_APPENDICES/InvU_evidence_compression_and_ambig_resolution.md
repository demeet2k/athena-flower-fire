# InvU - Evidence Compression & AMBIG Resolution

Routing role: Reverses AppL (Evidence Plans and AMBIG Promotion). Where AppL accumulated evidence and promoted ambiguous states upward through the lattice, InvU compresses accumulated evidence into fixed verdicts and resolves all AMBIG states into definite outcomes — either confirmed or rejected, never left pending.

Mirror of: AppL (Evidence Plans and AMBIG Promotion)
Arc: U | Rot: 285° → 75° | Lane: Evidence→Verdict | w: 7D

## StationHeader
```
Arc:  U (Evidence Compression)
Rot:  285° (judgment crystallization angle)
Lane: Descent-Evidence (evidence compression lane)
w:    7D → seed (accumulated evidence compresses to verdicts)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvU.S1.a`: `VerdictAccumulator` — The discrete accumulation of evidence reaches a threshold and tips into a verdict. The successor function becomes "one more piece of evidence toward final judgment." Each piece of evidence is a weighted vote; when the weighted sum crosses the decision boundary, the verdict is emitted. No more evidence is needed — the question is closed.
- `InvU.S1.b`: `AMBIGDifferenceResolver` — The difference between the AMBIG state's competing hypotheses. If `Δ(H₁, H₂) > threshold`, the hypotheses are distinguishable and the stronger one wins. If `Δ < threshold`, the hypotheses merge into a single unified verdict. The zero set of the difference identifies the undecidable core — resolved by convention rather than evidence.
- `InvU.S1.c`: `EvidenceChainProduct` — The multiplicative composition of all evidence links in a chain: each link's credibility × relevance × weight. The chain product is the total evidentiary force. Chains with any zero-credibility link have zero total force — one fraudulent piece of evidence invalidates the entire chain.
- `InvU.S1.d`: `PromotionInversion` — Where AppL promoted ambiguous states upward (AMBIG → higher authority), InvU demotes resolved states downward (verdict → execution layer). The quotient: promoted_count / resolved_count measures the system's resolution efficiency. A quotient of 1 means every promotion was eventually resolved.

#### Facet 2 - Laws

- `InvU.S2.a`: `VerdictIrreversibilityLaw` — Once a verdict is emitted, it cannot be reversed by additional evidence. The verdict is a phase transition: pre-verdict, evidence accumulates; post-verdict, the case is closed. New evidence opens a new case rather than reopening the old one.
- `InvU.S2.b`: `AMBIGResolutionCompleteness` — Every AMBIG state must be resolved during compression. No AMBIG state survives into the seed. Unresolvable AMBIGs are resolved by convention (the default hypothesis wins) with an explicit convention-certificate.
- `InvU.S2.c`: `ChainIntegrityLaw` — Every link in an evidence chain must have non-zero credibility. A chain with a zero-credibility link is not merely weak — it is broken. Broken chains cannot contribute to verdicts.
- `InvU.S2.d`: `ResolutionBalanceLaw` — The number of resolved verdicts must equal the number of promoted AMBIGs. Any imbalance indicates lost promotions (AMBIGs that were promoted but never resolved) or phantom verdicts (verdicts without corresponding promotions).

#### Facet 3 - Constructions

- `InvU.S3.a`: `ThresholdEvaluator` — For each pending AMBIG: sums the weighted evidence, compares against the decision boundary, and emits a verdict if crossed. If not crossed after all evidence is consumed, emits a convention-verdict with explicit declaration.
- `InvU.S3.b`: `HypothesisDiffer` — For each AMBIG with competing hypotheses: computes the difference in support, classifies as distinguishable (Δ > threshold) or mergeable (Δ < threshold), and emits either the winning hypothesis or the merged verdict.
- `InvU.S3.c`: `ChainValidator` — Traverses each evidence chain link by link. Verifies non-zero credibility at each link. Reports broken chains and their breaking point. Computes total chain force for intact chains.
- `InvU.S3.d`: `PromotionReconciler` — Matches each promotion record from AppL against its resolution record in InvU. Reports matched pairs, unmatched promotions (leaks), and unmatched verdicts (phantoms).

#### Facet 4 - Certificates

- `InvU.S4.a`: `VerdictEmissionCert` — Receipt proving verdict correctly emitted, threshold crossed (or convention applied), case closed, no evidence overflow.
- `InvU.S4.b`: `AMBIGResolutionCert` — Receipt proving all AMBIGs resolved, no pending states remain, convention-verdicts explicitly declared.
- `InvU.S4.c`: `ChainIntegrityCert` — Receipt proving all evidence chains intact (or broken ones documented), total force correctly computed, no zero-credibility link hidden.
- `InvU.S4.d`: `PromotionBalanceCert` — Receipt proving promotions and resolutions balanced, no leaks, no phantoms, resolution efficiency computed.

### Lens F

#### Facet 1 - Objects

- `InvU.F1.a`: `EvidenceWaveCollapse` — The continuous wave of accumulating evidence collapses to a definite state — the verdict. The Flower view: evidence is a probability amplitude that interferes constructively (toward verdict) or destructively (toward rejection). The collapse is the measurement that selects one outcome.
- `InvU.F1.b`: `AmbiguityDampingCurve` — Ambiguity starts high and dampens as evidence accumulates. The damping follows an exponential curve: each piece of evidence reduces remaining ambiguity by a fixed fraction. The curve asymptotically approaches zero — but the verdict threshold triggers before full dampening.
- `InvU.F1.c`: `CredibilityResonance` — Evidence from independent sources that agree creates resonance — their combined force exceeds the sum of individual forces. The resonance factor measures how much agreement amplifies credibility. Resonant evidence reaches the verdict threshold faster.
- `InvU.F1.d`: `ConvergenceToVerdict` — The evidence sequence converges to the verdict as its limit. The convergence rate determines how many pieces of evidence are needed. Fast convergence = decisive evidence. Slow convergence = the case is subtle and requires extensive investigation.

#### Facet 2 - Laws

- `InvU.F2.a`: `CollapseIrreversibilityLaw` — Wave collapse is irreversible: once the verdict is selected, the probability amplitude for all other outcomes becomes zero. This is the Flower-lens analog of the discrete verdict irreversibility law.
- `InvU.F2.b`: `MonotonicDampingLaw` — Ambiguity must monotonically decrease as evidence accumulates. Any increase in ambiguity indicates contradictory evidence — which must be investigated before compression proceeds.
- `InvU.F2.c`: `ResonanceBoundLaw` — Resonance amplification is bounded: the resonance factor cannot exceed the square root of the number of independent sources. Unbounded resonance would allow artificial verdict inflation.
- `InvU.F2.d`: `ConvergenceRateLaw` — The evidence sequence must converge at least geometrically (ratio ≤ 1/φ). Sub-geometric convergence indicates insufficient evidence quality — the investigation needs better sources, not more quantity.

#### Facet 3 - Constructions

- `InvU.F3.a`: `WaveCollapser` — Tracks the evidence probability amplitude over time. At each new piece of evidence: updates the amplitude by interference. When the amplitude for one outcome exceeds the threshold, collapses the wave and emits the verdict.
- `InvU.F3.b`: `AmbiguityDamper` — Monitors the ambiguity level after each piece of evidence. Plots the damping curve. Flags any non-monotone step (ambiguity increase). Reports the current damping rate and projected evidence needed for threshold.
- `InvU.F3.c`: `ResonanceDetector` — Identifies independent evidence sources that agree. Computes the resonance factor. Applies bounded amplification to the combined credibility. Reports which source combinations are resonant.
- `InvU.F3.d`: `ConvergenceAnalyzer` — Computes the convergence ratio of the evidence sequence. Classifies as fast (ratio < 1/φ²), adequate (ratio ∈ [1/φ², 1/φ]), or slow (ratio > 1/φ). Recommends investigation strategy based on convergence quality.

#### Facet 4 - Certificates

- `InvU.F4.a`: `WaveCollapseCert` — Receipt proving collapse occurred at declared threshold, all other amplitudes zeroed, verdict is definite.
- `InvU.F4.b`: `MonotoneDampingCert` — Receipt proving ambiguity decreased monotonically, no contradictory evidence unresolved, damping curve is well-behaved.
- `InvU.F4.c`: `ResonanceBoundCert` — Receipt proving resonance factor within bound, no artificial amplification, independent sources correctly identified.
- `InvU.F4.d`: `ConvergenceQualityCert` — Receipt proving convergence rate within declared class, evidence quality sufficient, investigation strategy appropriate.

### Lens C

#### Facet 1 - Objects

- `InvU.C1.a`: `BayesianVerdictPosterior` — The posterior probability of each hypothesis after all evidence is accumulated. The hypothesis with highest posterior wins the verdict. The Cloud view: verdict is maximum a posteriori (MAP) estimation over the hypothesis space.
- `InvU.C1.b`: `AMBIGProbabilityExclusion` — The probability of AMBIG (neither hypothesis dominates) is estimated by inclusion-exclusion over the overlap region of hypothesis posteriors. As evidence accumulates, the overlap shrinks and AMBIG probability decreases.
- `InvU.C1.c`: `IndependentEvidenceProduct` — Independent pieces of evidence multiply likelihoods: L(H|e₁,e₂) = L(H|e₁)·L(H|e₂). The Cloud view factorizes the evidence into independent contributions, making the posterior computation tractable.
- `InvU.C1.d`: `InformationGainNormalization` — Each piece of evidence is valued by its information gain (KL divergence from prior to posterior). Evidence with high information gain per unit cost is prioritized during compression. Low-gain evidence is released first.

#### Facet 2 - Laws

- `InvU.C2.a`: `MAPOptimalityLaw` — The MAP verdict minimizes expected loss under the posterior. Any other verdict has higher expected loss. This is the Bayesian justification for the verdict.
- `InvU.C2.b`: `AMBIGVanishingLaw` — The AMBIG probability must vanish (approach zero) as evidence accumulates without bound. If AMBIG persists despite unbounded evidence, the hypotheses are genuinely indistinguishable and must be merged.
- `InvU.C2.c`: `IndependenceVerificationLaw` — The independence assumption must be verified before likelihood factorization. Dependent evidence that is treated as independent inflates confidence — a dangerous error.
- `InvU.C2.d`: `DiminishingReturnsLaw` — Information gain per piece of evidence must eventually diminish. Early evidence is most informative; late evidence is confirmatory. The compression protocol releases confirmatory evidence first (it adds least new information).

#### Facet 3 - Constructions

- `InvU.C3.a`: `MAPEstimator` — Computes the posterior for each hypothesis using Bayes' theorem. Selects the MAP hypothesis. Outputs the posterior distribution, the MAP verdict, and the confidence gap between first and second hypotheses.
- `InvU.C3.b`: `AMBIGProbabilityTracker` — Estimates P(AMBIG) at each evidence step using the overlap integral of hypothesis posteriors. Plots the AMBIG probability curve. Reports when P(AMBIG) crosses below the resolution threshold.
- `InvU.C3.c`: `IndependenceTester` — Tests pairwise independence of evidence items using mutual information. Reports dependent pairs. Adjusts likelihood computation for dependent evidence using copulas or conditional models.
- `InvU.C3.d`: `InformationGainRanker` — Computes the information gain of each piece of evidence. Ranks by gain-per-cost. Outputs the release priority order (lowest gain/cost first) for evidence compression.

#### Facet 4 - Certificates

- `InvU.C4.a`: `MAPVerdictCert` — Receipt proving MAP estimation correct, posterior computed from valid likelihood × prior, confidence gap documented.
- `InvU.C4.b`: `AMBIGVanishingCert` — Receipt proving AMBIG probability below threshold (or hypotheses merged if indistinguishable), no pending ambiguity.
- `InvU.C4.c`: `EvidenceIndependenceCert` — Receipt proving independence verified (or dependence accounted for), likelihood computation is sound.
- `InvU.C4.d`: `InformationGainCert` — Receipt proving evidence ranked by information gain, release order is optimal, no high-gain evidence released prematurely.

### Lens R

#### Facet 1 - Objects

- `InvU.R1.a`: `RecursiveEvidenceTree` — Evidence accumulates in a tree structure: root question → sub-questions → sub-sub-questions → leaf observations. Compression works bottom-up: leaf observations compress to sub-verdicts, which compress to verdicts, which compress to the root answer.
- `InvU.R1.b`: `AMBIGContractionChain` — Each level of the evidence tree contracts the AMBIG space by factor 1/φ. At the root, AMBIG should be negligible. The contraction chain tracks how ambiguity shrinks level by level.
- `InvU.R1.c`: `VerdictTreePruning` — After bottom-up compression, the evidence tree is pruned: leaf observations are released (their information is captured in sub-verdicts), sub-questions are released (their information is captured in verdicts). Only the root verdict survives.
- `InvU.R1.d`: `ScaleInvariantJudgment` — The judgment protocol is identical at every level: accumulate evidence, cross threshold, emit verdict. Whether judging a leaf observation or the root question, the protocol is the same — only the evidence type changes.

#### Facet 2 - Laws

- `InvU.R2.a`: `LeafFirstVerdictLaw` — Sub-verdicts must be emitted before their parent verdicts. No parent verdict can be based on un-resolved sub-questions. Bottom-up resolution is mandatory.
- `InvU.R2.b`: `AMBIGContractionLaw` — Each level must reduce AMBIG space by at least factor 1/φ. If a level fails to reduce AMBIG, it indicates insufficient evidence at that level — investigation needs deepening, not widening.
- `InvU.R2.c`: `PruningIntegrityLaw` — Pruning a leaf must not alter the verdict of any ancestor. The leaf's information must be fully captured in its parent sub-verdict before pruning is legal.
- `InvU.R2.d`: `JudgmentProtocolLaw` — The judgment protocol must be identical at every level. Level-specific judgment criteria indicate structural inconsistency in the evidence plan.

#### Facet 3 - Constructions

- `InvU.R3.a`: `BottomUpResolver` — Traverses the evidence tree leaf-first. At each leaf: evaluates the observation. At each node: aggregates child verdicts and emits the node verdict. Reports the resolution path from leaves to root.
- `InvU.R3.b`: `AMBIGContractionTracker` — Measures AMBIG space at each level. Computes the contraction ratio between adjacent levels. Flags any level with insufficient contraction for investigation deepening.
- `InvU.R3.c`: `EvidenceTreePruner` — After bottom-up resolution, prunes the tree from leaves to root. At each leaf: verifies information captured in parent, then releases. Reports total pruned nodes and remaining tree (root verdict only).
- `InvU.R3.d`: `ProtocolVerifier` — Compares the judgment protocol at each level. Verifies identical structure. Reports any level-specific deviations.

#### Facet 4 - Certificates

- `InvU.R4.a`: `BottomUpResolutionCert` — Receipt proving all sub-verdicts emitted before parents, resolution path is valid, root verdict correctly derived.
- `InvU.R4.b`: `AMBIGContractionCert` — Receipt proving contraction ratio ≤ 1/φ at every level, AMBIG negligible at root, no level skipped.
- `InvU.R4.c`: `PruningCert` — Receipt proving all leaves correctly pruned, parent verdicts unaffected by pruning, only root verdict remains.
- `InvU.R4.d`: `ProtocolConsistencyCert` — Receipt proving judgment protocol identical at all levels, no structural inconsistency, scale-invariant judgment confirmed.
