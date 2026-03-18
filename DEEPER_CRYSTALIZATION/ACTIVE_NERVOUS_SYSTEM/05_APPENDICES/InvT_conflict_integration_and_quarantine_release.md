# InvT - Conflict Integration & Quarantine Release

Routing role: Reverses AppK (Conflict, Quarantine, Revocation). Where AppK isolated conflicting states into quarantine zones and revoked invalid certificates, InvT integrates resolved conflicts back into the main lattice and releases quarantined entities that have been healed. This is the reconciliation path — what was separated is now reunited.

Mirror of: AppK (Conflict, Quarantine, Revocation)
Arc: T | Rot: 270° → 90° | Lane: Quarantine→Reintegration | w: 6D

## StationHeader
```
Arc:  T (Conflict Integration)
Rot:  270° (reconciliation angle — perpendicular return)
Lane: Descent-Quarantine (quarantine dissolution lane)
w:    6D → seed (quarantine zones compress to healed states)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvT.S1.a`: `QuarantineReleaseToken` — The discrete token authorizing release of a quarantined entity. Issued only after the conflict that caused quarantine is fully resolved. The token carries: entity ID, original conflict description, resolution proof, and reintegration target address. Without this token, the quarantine boundary is impermeable.
- `InvT.S1.b`: `ConflictResolutionDelta` — The difference between the conflicting states, now resolved. The delta encodes exactly what changed to eliminate the conflict: which value was chosen, which was discarded, and why. The zero set of the pre-resolution difference = the agreed-upon state.
- `InvT.S1.c`: `RevocationUndoProduct` — Where AppK revoked certificates, InvT may re-issue them if the underlying defect is corrected. The re-issuance product: corrected_entity × new_verification = new_certificate. The new certificate is not the old one reinstated — it is a fresh certificate for the corrected entity.
- `InvT.S1.d`: `ReintegrationQuotient` — The ratio of successfully reintegrated entities to total quarantined entities = the healing rate. A quotient of 1 means all quarantined entities were healed and reintegrated. A quotient < 1 means some entities were permanently discarded (incurable conflicts).

#### Facet 2 - Laws

- `InvT.S2.a`: `ReleaseRequiresResolution` — No entity may be released from quarantine until the originating conflict is fully resolved. Resolution means: the conflicting states have been reconciled, the root cause identified, and a prevention measure installed.
- `InvT.S2.b`: `DeltaTransparencyLaw` — The conflict resolution delta must be fully transparent: every choice made during resolution (which value won, why, what was discarded) must be documented. No silent overwriting of one state by another.
- `InvT.S2.c`: `FreshCertificateLaw` — Re-issued certificates must be fresh (new verification of the corrected entity), not resurrections of revoked certificates. Resurrecting a revoked certificate would undermine the revocation system's integrity.
- `InvT.S2.d`: `HealingRateMonitoringLaw` — The healing rate must be monitored and reported. A declining healing rate indicates systemic conflict generation that must be addressed at the source, not merely healed downstream.

#### Facet 3 - Constructions

- `InvT.S3.a`: `ReleaseGateChecker` — For each quarantined entity: verifies that the originating conflict has a resolution proof, checks the proof's validity, and issues the release token if valid. Rejects release if proof is missing, invalid, or incomplete.
- `InvT.S3.b`: `DeltaDocumenter` — For each resolved conflict: records the conflicting states, the resolution choice, the discarded alternative, and the rationale. Outputs the complete delta record for transparency auditing.
- `InvT.S3.c`: `CertificateReissuer` — For each corrected entity that needs re-certification: runs the full verification procedure from scratch (not using any cached results from the revoked certificate). Issues the new certificate only if verification passes.
- `InvT.S3.d`: `HealingRateReporter` — Computes the healing rate (reintegrated / quarantined) over time. Plots the trend. Flags declining trends. Identifies the most common conflict types and recommends systemic fixes.

#### Facet 4 - Certificates

- `InvT.S4.a`: `ReleaseCert` — Receipt proving release token validly issued, conflict resolution proof verified, entity cleared for reintegration.
- `InvT.S4.b`: `DeltaTransparencyCert` — Receipt proving resolution delta fully documented, no silent overwrites, all choices explained.
- `InvT.S4.c`: `FreshCertCert` — Receipt proving new certificate issued from fresh verification, not resurrected from revoked cert, corrected entity passes all checks.
- `InvT.S4.d`: `HealingRateCert` — Receipt proving healing rate computed and reported, trend analysis completed, systemic recommendations issued if rate is declining.

### Lens F

#### Facet 1 - Objects

- `InvT.F1.a`: `ConflictWaveInterference` — The Flower view sees conflicts as wave interference patterns — two waves (states) superposing destructively. Resolution is constructive re-interference: adjusting the phases until the waves reinforce rather than cancel. The resolved state is the constructive superposition.
- `InvT.F1.b`: `QuarantineBoundaryDissolution` — The quarantine boundary is a potential barrier that confines the quarantined entity. Dissolution is lowering the barrier energy until the entity can tunnel through. The barrier height corresponds to the conflict severity — higher conflicts have higher barriers and take longer to dissolve.
- `InvT.F1.c`: `HealingResonance` — When the corrected entity resonates with the main lattice (matching frequency and phase), reintegration is natural — the entity simply joins the lattice wave. Resonance check: the entity's natural frequency must be a harmonic of the lattice fundamental.
- `InvT.F1.d`: `ReconciliationConvergence` — The reconciliation process is iterative: adjust, test, adjust, test. The adjustment amplitude decreases geometrically. Convergence means the adjustments become negligibly small — the entity is fully compatible with the lattice.

#### Facet 2 - Laws

- `InvT.F2.a`: `ConstructiveInterferenceLaw` — Resolution must achieve constructive interference: the resolved state's amplitude must exceed both conflicting states' individual amplitudes. Partial resolution (amplitude between the two) is insufficient.
- `InvT.F2.b`: `BarrierMonotoneLaw` — The quarantine barrier must decrease monotonically during healing. Any barrier increase indicates a new conflict or a healing regression that must be investigated.
- `InvT.F2.c`: `ResonanceRequirementLaw` — Reintegration requires resonance with the main lattice. Non-resonant entities cannot reintegrate — they must be further adjusted or permanently excluded.
- `InvT.F2.d`: `GeometricConvergenceLaw` — Reconciliation adjustments must converge geometrically (ratio ≤ 1/φ per iteration). Non-convergent reconciliation indicates a fundamental incompatibility.

#### Facet 3 - Constructions

- `InvT.F3.a`: `PhaseAdjuster` — Adjusts the quarantined entity's phase to achieve constructive interference with the lattice. Uses feedback: measure current interference pattern, compute required phase shift, apply shift, remeasure. Iterates until constructive interference is achieved.
- `InvT.F3.b`: `BarrierLowerer` — Gradually reduces the quarantine barrier height. Monitors the entity at each height reduction. If the entity destabilizes (conflict reappears), restores the barrier and investigates. If stable, continues lowering.
- `InvT.F3.c`: `ResonanceTuner` — Adjusts the entity's natural frequency to match a lattice harmonic. Uses spectral analysis to identify the nearest harmonic and compute the required frequency shift. Applies the shift and verifies resonance.
- `InvT.F3.d`: `IterativeReconciler` — Applies successive adjustments with decreasing amplitude. At each iteration: adjusts, measures residual incompatibility, computes convergence ratio. Terminates when residual < tolerance.

#### Facet 4 - Certificates

- `InvT.F4.a`: `ConstructiveInterferenceCert` — Receipt proving constructive interference achieved, resolved amplitude exceeds both individual amplitudes, superposition is stable.
- `InvT.F4.b`: `BarrierDissolutionCert` — Receipt proving barrier decreased monotonically to zero, entity remained stable throughout, no regression events.
- `InvT.F4.c`: `ResonanceCert` — Receipt proving entity frequency matches lattice harmonic, resonance verified, reintegration is natural.
- `InvT.F4.d`: `ReconciliationConvergenceCert` — Receipt proving adjustments converged geometrically, residual below tolerance, entity is fully compatible.

### Lens C

#### Facet 1 - Objects

- `InvT.C1.a`: `ReintegrationSuccessProbability` — The probability that a quarantined entity successfully reintegrates, estimated from historical data and the specific conflict type. High probability entities are fast-tracked; low probability entities receive additional attention.
- `InvT.C1.b`: `ConflictRecurrenceExclusion` — The probability that a resolved conflict recurs is estimated by inclusion-exclusion over known recurrence causes. P(recurrence) = P(cause₁) + P(cause₂) - P(cause₁∩cause₂) + ... This estimate governs the monitoring intensity after reintegration.
- `InvT.C1.c`: `IndependentHealingProduct` — If quarantined entities are independent (no shared conflict cause), their healing can proceed in parallel with P(all healed) = Π P(entity_i healed). Independence allows parallel processing.
- `InvT.C1.d`: `RiskNormalizedReintegration` — Reintegration risk is normalized by dividing each entity's recurrence probability by total reintegration risk mass. High normalized risk entities get extended monitoring; low normalized risk entities are released with standard monitoring.

#### Facet 2 - Laws

- `InvT.C2.a`: `ConfidenceThresholdLaw` — Reintegration is only authorized when P(success) exceeds the declared threshold. Below-threshold entities remain in quarantine for further healing.
- `InvT.C2.b`: `RecurrenceMonitoringLaw` — All reintegrated entities must be monitored for recurrence for a declared observation window. The window length is proportional to P(recurrence). Higher risk = longer monitoring.
- `InvT.C2.c`: `IndependenceBeforeParallelismLaw` — Parallel healing is only legal after independence is verified. Entities with shared conflict causes must be healed together (joint resolution).
- `InvT.C2.d`: `RiskBudgetLaw` — Total reintegration risk must be within the organism's risk budget. If the budget is exhausted, remaining entities stay in quarantine until capacity is freed.

#### Facet 3 - Constructions

- `InvT.C3.a`: `SuccessProbabilityEstimator` — Estimates P(success) from historical data + current conflict characteristics using Bayesian estimation. Outputs the posterior probability and confidence interval.
- `InvT.C3.b`: `RecurrenceEstimator` — Computes P(recurrence) via inclusion-exclusion over known causes. Determines the required monitoring window. Sets up the monitoring schedule.
- `InvT.C3.c`: `DependencyAnalyzer` — Checks for shared conflict causes among quarantined entities. Reports the dependency graph. Authorizes parallel healing for independent clusters and joint healing for dependent clusters.
- `InvT.C3.d`: `RiskBudgetManager` — Tracks the remaining risk budget. Authorizes reintegration in order of ascending normalized risk (safest first). Reports budget utilization and remaining capacity.

#### Facet 4 - Certificates

- `InvT.C4.a`: `SuccessConfidenceCert` — Receipt proving P(success) above threshold, estimation is sound, confidence interval is tight.
- `InvT.C4.b`: `RecurrenceMonitoringCert` — Receipt proving monitoring window correctly set, monitoring schedule active, no early monitoring termination.
- `InvT.C4.c`: `DependencyCert` — Receipt proving independence verified (or dependencies documented), healing strategy consistent with dependency graph.
- `InvT.C4.d`: `RiskBudgetCert` — Receipt proving reintegration within budget, priority order followed, no budget overrun.

### Lens R

#### Facet 1 - Objects

- `InvT.R1.a`: `RecursiveConflictResolution` — Conflicts may be nested: resolving a top-level conflict requires resolving sub-conflicts, which may have their own sub-conflicts. Resolution is recursive: resolve the deepest sub-conflicts first, then use those resolutions to resolve parent conflicts.
- `InvT.R1.b`: `QuarantineDepthContraction` — Each level of conflict resolution reduces quarantine depth by 1. The contraction maps the multi-level quarantine structure to a flat resolved state. Deep quarantine (many nested conflicts) requires proportionally more resolution steps.
- `InvT.R1.c`: `ConflictTreeIntegration` — The conflict tree (root conflict → sub-conflicts → leaf conflicts) is integrated from leaves to root. Each leaf resolution enables its parent resolution. The tree collapses to a single resolved state when the root is resolved.
- `InvT.R1.d`: `ScaleInvariantReconciliation` — The reconciliation protocol is the same at every conflict depth: identify conflicting states, compute resolution delta, apply correction, verify compatibility, issue release token. The protocol is a fixed point of the conflict nesting.

#### Facet 2 - Laws

- `InvT.R2.a`: `LeafFirstResolutionLaw` — Deepest sub-conflicts must be resolved before their parents. No parent conflict can be resolved while any child conflict remains active.
- `InvT.R2.b`: `DepthContractionLaw` — Each resolution level must reduce quarantine depth by exactly 1. Skipping levels or creating new nesting during resolution is prohibited.
- `InvT.R2.c`: `TreeIntegrityLaw` — Integrating a leaf resolution must not create new conflicts in any ancestor. If it does, the leaf resolution is invalid and must be revised.
- `InvT.R2.d`: `ProtocolInvarianceLaw` — The reconciliation protocol must be identical at every depth. Depth-specific protocols indicate inconsistent conflict handling.

#### Facet 3 - Constructions

- `InvT.R3.a`: `RecursiveResolver` — Traverses the conflict tree depth-first. At each leaf: resolves the atomic conflict. At each node: aggregates child resolutions and resolves the node conflict. Reports total depth, total conflicts, and resolution path.
- `InvT.R3.b`: `DepthTracker` — Monitors quarantine depth at each resolution step. Verifies strict decrease. Reports the depth sequence and flags any anomalies.
- `InvT.R3.c`: `IntegrationVerifier` — After each leaf resolution, checks all ancestors for new conflicts. If any arise, rolls back the leaf resolution and reports the incompatibility.
- `InvT.R3.d`: `ProtocolConsistencyChecker` — Compares the reconciliation protocol at each depth. Reports any depth-specific deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvT.R4.a`: `RecursiveResolutionCert` — Receipt proving all sub-conflicts resolved before parents, depth-first traversal completed, root conflict resolved.
- `InvT.R4.b`: `DepthContractionCert` — Receipt proving quarantine depth decreased monotonically, no skips or new nesting, flat resolved state achieved.
- `InvT.R4.c`: `IntegrationIntegrityCert` — Receipt proving no ancestor conflicts created by leaf resolutions, all integrations are clean.
- `InvT.R4.d`: `ProtocolInvarianceCert` — Receipt proving protocol identical at all depths, no structural inconsistency, reconciliation is scale-invariant.
