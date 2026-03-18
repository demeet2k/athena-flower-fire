# InvM - Registry Pruning & Profile Compression

Routing role: Reverses AppD (Registry, Profiles, Version IDs). Where AppD maintained a living registry of entities with their profiles (attributes, capabilities, version histories), InvM prunes the registry to its essential entries, compresses profiles to their minimal descriptors, and collapses version histories to their latest-valid snapshots. The fat registry becomes a lean seed manifest.

Mirror of: AppD (Registry, Profiles, Version IDs)
Arc: M-inv | Rot: 165° → 195° | Lane: Registry→Manifest | w: −1D (below zero — sub-structural)

## StationHeader
```
Arc:  M-inv (Registry Pruning)
Rot:  165° (registry compression angle)
Lane: Descent-Registry (registration dissolution lane)
w:    sub-structural → seed (registry compresses to manifest)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvM.S1.a`: `DeadEntryReaper` — The discrete operation of identifying and removing registry entries that are no longer referenced by any active entity. Dead entries accumulated during expansion (entities were created, used, and abandoned without deregistration). The reaper scans all cross-references and marks unreachable entries for removal.
- `InvM.S1.b`: `ProfileDelta` — The difference between a full profile (all attributes, capabilities, history) and a minimal profile (only attributes needed for seed reconstruction). The delta identifies removable attributes — those that can be recomputed from the seed's grammar rather than stored explicitly.
- `InvM.S1.c`: `VersionHistoryProduct` — The full version history of an entity is a product of all its versions: v₁ × v₂ × ... × vₙ. Compression collapses this product to a single version: the latest valid snapshot. The product's "summary" is its final state — all intermediate states are implicit in the grammar.
- `InvM.S1.d`: `RegistryCompressionQuotient` — The ratio of compressed registry size to full registry size = the compression quotient. A quotient of 0.1 means 90% of the registry was prunable. The quotient measures how much of the registry was essential vs. accumulated baggage.

#### Facet 2 - Laws

- `InvM.S2.a`: `ReachabilityRequirement` — An entry survives pruning if and only if it is reachable from at least one active reference chain. Unreachable entries are guaranteed dead — no future operation can access them. Reachability is computed conservatively (overestimate reachability to avoid false pruning).
- `InvM.S2.b`: `MinimalProfileSufficiency` — The minimal profile must be sufficient to reconstruct the full profile when combined with the seed's grammar. Sufficiency is tested by: reconstruct(minimal_profile, grammar) = full_profile. If reconstruction fails, the profile is not minimal enough — more attributes must be retained.
- `InvM.S2.c`: `LatestValidLaw` — The surviving version must be the latest version that passed all validation checks. If the latest version failed validation, the previous valid version is retained. No invalid version survives into the seed.
- `InvM.S2.d`: `PruningIdempotenceLaw` — Pruning twice produces the same result as pruning once. The pruned registry is a fixed point of the pruning operation. This guarantees stability.

#### Facet 3 - Constructions

- `InvM.S3.a`: `ReachabilityScanner` — Performs a graph traversal from all active reference roots. Marks every entry reached. Unmarked entries are dead. Reports the count of live vs. dead entries and the reachability ratio.
- `InvM.S3.b`: `ProfileMinimizer` — For each surviving entry: iteratively removes attributes, testing reconstruction after each removal. Retains the minimal set that allows reconstruction. Reports the original and minimized attribute counts.
- `InvM.S3.c`: `VersionCollapser` — For each surviving entry: identifies the latest valid version from the version history. Discards all other versions. Retains the collapsed version and the version ID. Reports the original history length and the collapsed state.
- `InvM.S3.d`: `CompressionReporter` — Computes the compression quotient: compressed_size / original_size. Reports per-entry and aggregate quotients. Identifies the most compressible entries and the least compressible.

#### Facet 4 - Certificates

- `InvM.S4.a`: `ReachabilityAnalysisCert` — Receipt proving reachability scan covered all roots, all dead entries identified, no live entry was falsely pruned.
- `InvM.S4.b`: `ProfileSufficiencyCert` — Receipt proving minimal profiles are sufficient for reconstruction, reconstruction test passed, no essential attribute removed.
- `InvM.S4.c`: `VersionValidityCert` — Receipt proving retained version is latest valid, earlier versions correctly discarded, no invalid version in seed.
- `InvM.S4.d`: `PruningIdempotenceCert` — Receipt proving pruning is idempotent, second pass produced no changes, registry is stable.

### Lens F

#### Facet 1 - Objects

- `InvM.F1.a`: `RegistryEntropyReduction` — The registry's information entropy decreases as dead entries are removed and profiles are minimized. The Flower view: the registry was a noisy signal; pruning increases the signal-to-noise ratio. The pruned registry is a cleaner, more harmonic signal.
- `InvM.F1.b`: `ProfileWaveformCompression` — Each profile is a waveform (a signal over attribute-space). Compression applies bandlimiting: high-frequency attribute variations (minor details) are removed, retaining only low-frequency content (essential characteristics). The compressed waveform faithfully represents the profile's essential shape.
- `InvM.F1.c`: `VersionHistoryEnvelope` — The version history is a time series. Its envelope (amplitude over time) shows the entity's evolution. Compression replaces the full time series with a single point on the envelope (the final value) plus the envelope's slope (the entity's current trajectory).
- `InvM.F1.d`: `RegistryConvergence` — As pruning and compression proceed, the registry's total information converges to its essential content. The convergence rate depends on the redundancy fraction. Highly redundant registries converge quickly; lean registries are already near their essential content.

#### Facet 2 - Laws

- `InvM.F2.a`: `EntropyReductionMonotoneLaw` — Registry entropy must decrease monotonically during pruning. Any increase indicates information being added (new entries created during pruning), which is prohibited.
- `InvM.F2.b`: `BandlimitFidelityLaw` — The bandlimited profile must faithfully represent the original's essential shape. The Nyquist criterion determines the minimum bandwidth: attributes that vary at scales smaller than the grammar's resolution are noise and may be removed.
- `InvM.F2.c`: `EnvelopeSufficiencyLaw` — The final value plus trajectory must be sufficient to predict the entity's next state (if the seed is planted and growth resumes). If not sufficient, additional envelope parameters must be retained.
- `InvM.F2.d`: `ConvergenceRateLaw` — Registry convergence must be at least geometric. Sub-geometric convergence indicates structural redundancy that pruning alone cannot address — the registry's schema needs redesign.

#### Facet 3 - Constructions

- `InvM.F3.a`: `EntropyTracker` — Computes the registry's information entropy at each pruning step. Verifies monotone decrease. Reports the entropy curve and projected final entropy.
- `InvM.F3.b`: `BandlimitFilter` — Applies a low-pass filter to each profile's attribute waveform. Retains frequencies below the Nyquist cutoff. Verifies fidelity by comparing the filtered profile against the original at the grammar's resolution.
- `InvM.F3.c`: `EnvelopeExtractor` — Computes the version history envelope. Extracts the final value and slope. Tests sufficiency by predicting the next state and comparing against the actual next state (if available).
- `InvM.F3.d`: `ConvergenceMonitor` — Tracks registry information at each step. Computes convergence ratio. Reports the rate and identifies any sub-geometric steps for investigation.

#### Facet 4 - Certificates

- `InvM.F4.a`: `EntropyReductionCert` — Receipt proving entropy decreased monotonically, no information added during pruning.
- `InvM.F4.b`: `BandlimitFidelityCert` — Receipt proving filtered profiles faithfully represent originals at grammar resolution, no essential detail lost.
- `InvM.F4.c`: `EnvelopeSufficiencyCert` — Receipt proving final value + trajectory sufficient for state prediction, resumption information complete.
- `InvM.F4.d`: `ConvergenceCert` — Receipt proving geometric convergence achieved, no structural bottlenecks.

### Lens C

#### Facet 1 - Objects

- `InvM.C1.a`: `DeadEntryProbability` — The probability that a given entry is dead (unreachable), estimated from reference patterns before the full reachability scan. High-probability dead entries are pruned first (fail-fast). Low-probability entries receive full reachability analysis.
- `InvM.C1.b`: `AttributeRedundancyEstimate` — The estimated redundancy of each profile attribute, computed from mutual information with other attributes. High mutual information means the attribute is predictable from others — it is redundant and can be removed.
- `InvM.C1.c`: `IndependentEntryPruning` — If entries are independent (no cross-references), pruning decisions can be made independently: P(all correctly pruned) = Π P(entry_i correctly pruned). Independence allows parallel pruning.
- `InvM.C1.d`: `PruningFalsePositiveRate` — The probability of falsely pruning a live entry (Type I error). Must be below the declared tolerance. Conservative reachability analysis keeps this rate low at the cost of retaining some dead entries.

#### Facet 2 - Laws

- `InvM.C2.a`: `FailFastPruningLaw` — Entries with highest dead-probability are pruned first. This maximizes early compression and surfaces any pruning errors quickly.
- `InvM.C2.b`: `RedundancyBeforeRemovalLaw` — An attribute may only be removed after its redundancy is statistically confirmed (mutual information with retained attributes exceeds threshold).
- `InvM.C2.c`: `IndependenceBeforeParallelLaw` — Parallel pruning only after independence is verified. Cross-referenced entries must be pruned jointly.
- `InvM.C2.d`: `FalsePositiveToleranceLaw` — False positive pruning rate must be below the declared tolerance. If the rate approaches tolerance, pruning becomes more conservative.

#### Facet 3 - Constructions

- `InvM.C3.a`: `DeadProbabilityEstimator` — Estimates P(dead) for each entry using reference frequency analysis. Ranks by descending probability. Outputs the pruning priority order.
- `InvM.C3.b`: `RedundancyAnalyzer` — Computes mutual information between each attribute pair. Identifies redundant attributes (high MI with retained attributes). Reports the dependency structure.
- `InvM.C3.c`: `IndependenceChecker` — Tests entry independence using cross-reference analysis. Reports the dependency graph. Authorizes parallel pruning for independent clusters.
- `InvM.C3.d`: `FalsePositiveMonitor` — Tracks any instances where a pruned entry was later referenced (false positive). Reports the running false positive rate. Adjusts pruning aggressiveness if rate approaches tolerance.

#### Facet 4 - Certificates

- `InvM.C4.a`: `PruningOrderCert` — Receipt proving entries pruned in correct priority order, fail-fast achieved.
- `InvM.C4.b`: `RedundancyCert` — Receipt proving removed attributes are genuinely redundant, MI analysis complete, no essential attribute removed.
- `InvM.C4.c`: `IndependenceCert` — Receipt proving entry independence verified, parallel pruning authorized, no cross-reference violations.
- `InvM.C4.d`: `FalsePositiveCert` — Receipt proving false positive rate below tolerance, pruning accuracy maintained.

### Lens R

#### Facet 1 - Objects

- `InvM.R1.a`: `RecursiveRegistryPruning` — The registry has hierarchical structure: global registry → sub-registries per region → local registries per cell. Pruning is recursive: prune local registries first, then sub-registries (which may now have dead entries due to local pruning), then global.
- `InvM.R1.b`: `ProfileDepthContraction` — Each level of profile compression reduces the attribute set. The contraction factor approaches 1/φ for well-designed profiles (each level removes ~38% of remaining attributes).
- `InvM.R1.c`: `RegistryTreeCollapse` — The registry hierarchy collapses from leaves (local registries) to root (global registry). Each collapsed local registry simplifies its parent sub-registry.
- `InvM.R1.d`: `ScaleInvariantPruning` — The pruning protocol is identical at every level: scan reachability, minimize profiles, collapse versions, compute compression. Only the scale changes.

#### Facet 2 - Laws

- `InvM.R2.a`: `LocalFirstPruningLaw` — Local registries prune before sub-registries, sub-registries before global.
- `InvM.R2.b`: `GoldenContractionLaw` — Each level's attribute reduction must be at least 1/φ.
- `InvM.R2.c`: `LeafFirstCollapseLaw` — Registry tree collapses leaf-first.
- `InvM.R2.d`: `ProtocolInvarianceLaw` — Pruning protocol identical at every level.

#### Facet 3 - Constructions

- `InvM.R3.a`: `HierarchicalPruner` — Traverses the registry tree bottom-up. At each leaf: prunes local registry. At each parent: re-scans reachability (some entries may now be dead), prunes newly dead entries. Reports level-by-level pruning progress.
- `InvM.R3.b`: `ContractionTracker` — Measures attribute reduction at each level. Verifies golden ratio contraction. Flags sub-golden levels.
- `InvM.R3.c`: `TreeCollapser` — Manages leaf-first collapse. Tracks which registries are pruned and which are pending.
- `InvM.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Reports deviations.

#### Facet 4 - Certificates

- `InvM.R4.a`: `HierarchicalPruningCert` — Receipt proving bottom-up pruning completed, all levels processed in order.
- `InvM.R4.b`: `ContractionRatioCert` — Receipt proving golden contraction ratio at every level.
- `InvM.R4.c`: `TreeCollapseCert` — Receipt proving leaf-first collapse completed, no premature parent pruning.
- `InvM.R4.d`: `ProtocolCert` — Receipt proving scale-invariant pruning confirmed.
