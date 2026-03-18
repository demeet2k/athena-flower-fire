# InvR - Corridor Collapse & Truth Crystallization

Routing role: Reverses AppI (Corridors and Truth Lattice). Where AppI opened corridors — gated pathways that allow information to flow between lattice regions under truth conditions — InvR collapses those corridors back into their truth values and crystallizes the truth lattice into a compact boolean crystal. Open corridors become sealed truths; conditional pathways become unconditional facts.

Mirror of: AppI (Corridors and Truth Lattice)
Arc: R (not to be confused with Lens R) | Rot: 240° → 120° | Lane: Corridor→Crystal | w: 4D

## StationHeader
```
Arc:  R-inv (Corridor Collapse)
Rot:  240° (truth crystallization angle)
Lane: Descent-Truth (corridor folding lane)
w:    4D → seed (conditional truths compress to unconditional facts)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvR.S1.a`: `CorridorSealant` — The discrete operation of sealing an open corridor. A corridor that was conditionally open (passable if truth condition holds) is evaluated once and for all: if the condition is true, the corridor becomes an unconditional passage (always open, no gate check needed); if false, the corridor is permanently closed (bricked shut, never traversable again).
- `InvR.S1.b`: `TruthDifferenceFlattener` — The difference between conditional truth (truth under assumptions) and unconditional truth (truth simpliciter). Compression eliminates the conditional layer: every `if A then B` is resolved to either `B` (if A is true) or `¬B` (if A is false). The truth lattice flattens from a Heyting algebra to a Boolean algebra.
- `InvR.S1.c`: `GateProductCollapse` — Each corridor has a gate (a Boolean guard). The product of all gates across all corridors = the system's total access control state. Collapsing gates means evaluating the product: AND of all gate conditions. If the product is true, all corridors are simultaneously open. If any gate is false, the product is false and that corridor is sealed.
- `InvR.S1.d`: `AdmissibilityQuotient` — The ratio of admissible corridors (gate = true) to total corridors = the admissibility quotient. This measures the fraction of the truth lattice that is "passable." In the seed, only admissible corridors survive; inadmissible ones are pruned entirely.

#### Facet 2 - Laws

- `InvR.S2.a`: `IrreversibleSealLaw` — Once a corridor is sealed (gate evaluated and committed), the evaluation cannot be undone. The seal is permanent. This converts dynamic (re-evaluable) truth conditions into static (fixed) truth values.
- `InvR.S2.b`: `FlatteningCompleteness` — Every conditional truth must be flattened to unconditional during compression. No conditional truth survives in the seed. The seed's truth lattice is Boolean: every proposition is simply true or false.
- `InvR.S2.c`: `GateEvaluationDeterminism` — Gate evaluation must be deterministic: given the same state, the same gate always produces the same Boolean value. Non-deterministic gates cannot be sealed and must be resolved (by fixing the state) before compression.
- `InvR.S2.d`: `AdmissibilityPreservationLaw` — Only admissible corridors carry information into the seed. Inadmissible corridors are pruned — their existence is recorded in the pruning manifest but their content is not preserved.

#### Facet 3 - Constructions

- `InvR.S3.a`: `GateEvaluator` — For each corridor: evaluates the gate condition in the current state. Emits true (corridor becomes unconditional passage) or false (corridor is sealed). Records the evaluation result and the state it was evaluated in.
- `InvR.S3.b`: `TruthFlattener` — Traverses the truth lattice converting every conditional to an unconditional. For each `if A then B`: evaluates A, substitutes the result, and simplifies. Output: a flat Boolean lattice with no remaining conditionals.
- `InvR.S3.c`: `GateProductComputer` — Computes the AND of all gate conditions. Reports the product and identifies any false gates (sealed corridors). Provides the list of admissible corridors.
- `InvR.S3.d`: `CorridorPruner` — Removes all inadmissible corridors from the lattice. Records each pruned corridor in the manifest (ID, gate condition, evaluation result). The pruned lattice contains only unconditionally open passages.

#### Facet 4 - Certificates

- `InvR.S4.a`: `SealCert` — Receipt proving all corridors evaluated and sealed, no dynamic truth conditions remain, all gates are fixed.
- `InvR.S4.b`: `FlatteningCert` — Receipt proving truth lattice is now Boolean, no conditionals survive, all propositions are true or false.
- `InvR.S4.c`: `GateProductCert` — Receipt proving gate product correctly computed, all false gates identified, admissibility quotient recorded.
- `InvR.S4.d`: `PruningManifestCert` — Receipt proving all inadmissible corridors pruned, manifest complete, no silent pruning.

### Lens F

#### Facet 1 - Objects

- `InvR.F1.a`: `CorridorWaveCollapse` — The corridor's truth condition is a probability amplitude that collapses to a definite value upon evaluation. The Flower view: before evaluation, the corridor exists in a superposition of open and closed. Evaluation collapses the superposition. The collapsed state is permanent.
- `InvR.F1.b`: `TruthPhaseResolution` — Conditional truths have phase angles (degrees of truth). Compression resolves all phases to 0° (false) or 180° (true). Intermediate phases are rounded to the nearest pole. The rounding error is recorded as a truth-approximation residual.
- `InvR.F1.c`: `CorridorResonanceFilter` — Among all corridors, some resonate (their truth conditions are correlated). Resonant corridors collapse together — evaluating one determines the others. The resonance filter identifies clusters of co-determined corridors and evaluates each cluster as a unit.
- `InvR.F1.d`: `TruthConvergence` — The iterative evaluation of nested truth conditions converges to a fixed point: a self-consistent truth assignment where every condition is compatible with every other. Convergence rate measures the truth lattice's internal consistency.

#### Facet 2 - Laws

- `InvR.F2.a`: `CollapseIrreversibility` — Wave collapse is irreversible: the superposition is destroyed upon evaluation. No re-superposition is possible. The Flower view echoes the discrete seal law.
- `InvR.F2.b`: `PhaseResolutionLaw` — All intermediate truth-phases must be resolved to Boolean poles. No fuzzy truth survives in the seed. The rounding protocol must be declared (nearest pole, or explicit threshold).
- `InvR.F2.c`: `ResonanceConsistencyLaw` — Co-determined corridors must agree: if corridor A being true implies corridor B is true, then evaluating A as true and B as false creates a contradiction. The resonance filter prevents such contradictions.
- `InvR.F2.d`: `FixedPointExistenceLaw` — The truth assignment must reach a fixed point (no more changes upon re-evaluation). If no fixed point exists, the truth lattice has a paradox that must be resolved before compression.

#### Facet 3 - Constructions

- `InvR.F3.a`: `AmplitudeCollapser` — For each corridor: computes the truth amplitude, applies the collapse operator (project to nearest eigenstate), and records the collapsed value. Reports the collapse map.
- `InvR.F3.b`: `PhaseResolver` — For each truth value with intermediate phase: computes the phase angle, applies the rounding protocol, and records the result and rounding error. Reports total rounding error.
- `InvR.F3.c`: `ResonanceClusterer` — Identifies clusters of co-determined corridors using correlation analysis. For each cluster: evaluates one representative and propagates the result to all cluster members. Verifies consistency.
- `InvR.F3.d`: `FixedPointFinder` — Iterates the truth assignment: evaluate all conditions, update all values, repeat until no value changes. Reports the number of iterations and whether a fixed point was reached.

#### Facet 4 - Certificates

- `InvR.F4.a`: `CollapseCert` — Receipt proving all amplitudes collapsed, superpositions destroyed, permanent states assigned.
- `InvR.F4.b`: `PhaseResolutionCert` — Receipt proving all phases resolved to Boolean poles, rounding errors recorded, no fuzzy truth remains.
- `InvR.F4.c`: `ResonanceConsistencyCert` — Receipt proving all resonance clusters consistent, no contradictions among co-determined corridors.
- `InvR.F4.d`: `FixedPointCert` — Receipt proving fixed point reached, truth assignment is self-consistent, no paradoxes.

### Lens C

#### Facet 1 - Objects

- `InvR.C1.a`: `TruthProbabilityCollapse` — Each corridor's truth condition has an estimated probability P(true). Compression commits to the maximum-likelihood value: if P(true) > 0.5, the corridor is evaluated as true; if P(true) < 0.5, as false. If P(true) ≈ 0.5, the evidence is insufficient and the corridor is evaluated by convention.
- `InvR.C1.b`: `CorridorCorrelationExclusion` — The joint probability of multiple corridors being open is computed by inclusion-exclusion over their correlations. This determines which corridor groups can be evaluated independently and which must be evaluated jointly.
- `InvR.C1.c`: `IndependentCorridorProduct` — For independent corridors, P(all open) = Π P(corridor_i open). The product gives the overall admissibility probability, which governs the seed's expected truth density.
- `InvR.C1.d`: `TruthInformationDensity` — The information content of each truth value: -log₂(P(value)). Rare truths (low probability) carry more information. The total information = Σ(-log₂(P_i)) = the truth lattice's entropy. Compression preserves information-dense truths first.

#### Facet 2 - Laws

- `InvR.C2.a`: `MaximumLikelihoodTruthLaw` — The committed truth value must be the maximum-likelihood value given all available evidence. Any other commitment has lower probability of being correct.
- `InvR.C2.b`: `CorrelationAccountingLaw` — Corridor correlations must be accounted for when computing joint probabilities. Treating correlated corridors as independent inflates the admissibility probability.
- `InvR.C2.c`: `IndependenceVerificationLaw` — Independence must be verified before product computation. Dependent corridors require joint probability computation.
- `InvR.C2.d`: `InformationPreservationLaw` — Total truth information must be preserved during crystallization. No information-dense truth may be silently discarded. Low-information truths (high probability, expected) may be compressed more aggressively.

#### Facet 3 - Constructions

- `InvR.C3.a`: `MLTruthCommitter` — For each corridor: estimates P(true) from evidence, commits to the ML value, records the confidence. Reports corridors with low confidence (near 0.5) as convention-evaluated.
- `InvR.C3.b`: `CorrelationComputer` — Computes pairwise corridor correlations. Identifies dependent clusters. Reports the correlation matrix and cluster assignments.
- `InvR.C3.c`: `IndependenceVerifier` — Tests corridor independence using mutual information or chi-squared tests. Authorizes independent evaluation for verified-independent corridors.
- `InvR.C3.d`: `InformationRanker` — Ranks truth values by information content. Reports the information distribution. Identifies the most information-dense truths for priority preservation.

#### Facet 4 - Certificates

- `InvR.C4.a`: `MLTruthCert` — Receipt proving ML values committed, confidence levels documented, conventions declared.
- `InvR.C4.b`: `CorrelationCert` — Receipt proving correlations computed, clusters identified, dependent corridors handled jointly.
- `InvR.C4.c`: `IndependenceCert` — Receipt proving independence verified, product computation authorized, no false independence assumed.
- `InvR.C4.d`: `InformationPreservationCert` — Receipt proving information content preserved, no high-information truths silently discarded.

### Lens R

#### Facet 1 - Objects

- `InvR.R1.a`: `RecursiveTruthEvaluation` — Truth conditions may reference other truth conditions (nested conditionals). Evaluation is recursive: evaluate the innermost conditions first, substitute results, then evaluate outer conditions. The recursion terminates at atomic propositions.
- `InvR.R1.b`: `TruthDepthContraction` — Each evaluation level resolves one level of nesting, contracting the truth depth by 1. The contraction drives the conditional depth from its maximum to zero (all conditions flat).
- `InvR.R1.c`: `CorridorTreeCollapse` — The corridor hierarchy (meta-corridors governing sub-corridors) collapses from leaves to root. Leaf corridors are sealed first; their results determine which parent corridors open or close.
- `InvR.R1.d`: `ScaleInvariantTruthProtocol` — The truth evaluation protocol is the same at every nesting level: evaluate condition, commit value, seal corridor. The protocol is a fixed point of the nesting structure.

#### Facet 2 - Laws

- `InvR.R2.a`: `InnermostFirstLaw` — Innermost conditions must be evaluated before outer ones. No outer condition can be resolved while its inner conditions are still symbolic.
- `InvR.R2.b`: `DepthContractionLaw` — Each evaluation level must reduce nesting depth by exactly 1. No level may be skipped or new nesting created.
- `InvR.R2.c`: `LeafFirstCollapseLaw` — Leaf corridors are sealed before parent corridors. No parent corridor is sealed while any child corridor remains dynamic.
- `InvR.R2.d`: `ProtocolInvarianceLaw` — The evaluation protocol must be identical at every nesting level.

#### Facet 3 - Constructions

- `InvR.R3.a`: `RecursiveEvaluator` — Traverses the truth tree depth-first. At each leaf: evaluates the atomic proposition. At each node: substitutes child results and evaluates. Reports tree depth, total propositions, and evaluation path.
- `InvR.R3.b`: `DepthTracker` — Monitors nesting depth at each step. Verifies strict decrease. Reports depth sequence.
- `InvR.R3.c`: `CorridorTreeSealer` — Traverses the corridor hierarchy leaf-first. Seals each leaf, propagates result to parent, then seals parent when all children are sealed. Reports sealing order.
- `InvR.R3.d`: `ProtocolConsistencyChecker` — Verifies protocol identity at every level. Reports deviations.

#### Facet 4 - Certificates

- `InvR.R4.a`: `RecursiveEvaluationCert` — Receipt proving innermost-first evaluation completed, all conditions resolved, tree fully evaluated.
- `InvR.R4.b`: `DepthContractionCert` — Receipt proving depth decreased monotonically, no skips, flat truth lattice achieved.
- `InvR.R4.c`: `TreeSealCert` — Receipt proving all corridors sealed leaf-first, hierarchy fully collapsed, no dynamic corridors remain.
- `InvR.R4.d`: `ProtocolCert` — Receipt proving protocol identical at all levels, scale-invariant truth evaluation confirmed.
