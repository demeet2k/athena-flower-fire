# InvO - Transport Stillness & Conjugacy Rest

Routing role: Reverses AppF (Transport, Rotation-as-Conjugacy, DUAL Legality). Where AppF established lens transport equations, conjugacy bridges between representations, and dual legality for rotational moves, InvO brings all transport to stillness, collapses conjugacy bridges into identity maps, and resolves dual legality into single determination. Motion ceases; all representations become one.

Mirror of: AppF (Transport, Rotation-as-Conjugacy, DUAL Legality)
Arc: O-inv | Rot: 195° → 165° | Lane: Transport→Stillness | w: 1D

## StationHeader
```
Arc:  O-inv (Transport Stillness)
Rot:  195° (motion cessation angle)
Lane: Descent-Transport (transport dissolution lane)
w:    1D → seed (all motion compresses to rest)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvO.S1.a`: `TransportFixedPoint` — The discrete fixed point where the transport map T equals the identity: T(x) = x. At this point, the transported value equals the native value — no lens transformation is needed. The successor function at the fixed point is the natural successor: n ↦ n+1 in every representation simultaneously.
- `InvO.S1.b`: `ConjugacyCollapse` — The difference between conjugate representations: T⁻¹∘f∘T vs. f. At the fixed point, this difference vanishes: T = id implies T⁻¹∘f∘T = f. The zero set of the conjugacy difference is the universal representation — the one in which all lens views agree.
- `InvO.S1.c`: `DualLegalityProduct` — In the forward direction, each move had dual legality (legal as both forward and backward). In compression, duality collapses: each move is classified as either forward-only or backward-only. The product of all move classifications = the directed motion graph. At stillness, all moves are null (neither forward nor backward).
- `InvO.S1.d`: `RotationQuotientIdentity` — The quotient of any rotated value by its unrotated original: f_T(x) / f(x). At the fixed point, this quotient is 1 (identity ratio). The quotient approaching 1 means rotation is becoming trivial — all angles collapse to zero.

#### Facet 2 - Laws

- `InvO.S2.a`: `FixedPointStabilityLaw` — The transport fixed point must be stable: small perturbations return to the fixed point. An unstable fixed point would allow transport to restart spontaneously, violating the stillness condition.
- `InvO.S2.b`: `ConjugacyUniquenessLaw` — The universal representation (where all conjugacies collapse) must be unique. If multiple representations survive collapse, the conjugacy bridges between them are essential (not collapsible) and must be preserved in the seed.
- `InvO.S2.c`: `DualityResolutionLaw` — Every dual move must be resolved to a single direction (or null). No duality survives in the seed. The resolution must be consistent: if move A→B is classified as forward, then B→A must be classified as backward.
- `InvO.S2.d`: `TrivialRotationLaw` — All rotation angles must collapse to zero modulo 2π. Any non-zero residual angle indicates incomplete transport collapse.

#### Facet 3 - Constructions

- `InvO.S3.a`: `FixedPointLocator` — Solves T(x) = x for the transport map T. For linear T, this is an eigenvalue problem (eigenvalue 1). For nonlinear T, uses iterative methods. Reports the fixed point and its stability (eigenvalue magnitudes < 1 for stability).
- `InvO.S3.b`: `ConjugacyReducer` — For each pair of conjugate representations: checks if the conjugacy bridge T is essential (representations are genuinely different) or redundant (T ≈ id). Collapses redundant bridges. Preserves essential ones.
- `InvO.S3.c`: `DualityResolver` — For each dual move: evaluates the forward and backward legality conditions in the current (converging) state. Classifies as forward, backward, or null. Verifies consistency of the classification.
- `InvO.S3.d`: `AngleCollapser` — For each rotation parameter: drives the angle toward zero modulo 2π. Uses continuous deceleration (not sudden snap). Reports residual angles at each step.

#### Facet 4 - Certificates

- `InvO.S4.a`: `FixedPointCert` — Receipt proving fixed point found, stability verified (all eigenvalues inside unit circle), transport at rest.
- `InvO.S4.b`: `ConjugacyCollapseCert` — Receipt proving all redundant conjugacies collapsed, essential ones preserved, universal representation identified (or multiplicity documented).
- `InvO.S4.c`: `DualityResolutionCert` — Receipt proving all dualities resolved, classification consistent, no residual duality.
- `InvO.S4.d`: `AngleCollapseCert` — Receipt proving all rotation angles collapsed to zero, no residual rotation, transport is trivial.

### Lens F

#### Facet 1 - Objects

- `InvO.F1.a`: `TransportWaveStillness` — The transport wave (information flowing between lens views) comes to rest. The wave amplitude decays to zero. No more information flows between representations — each view contains its own complete picture. Stillness is the Flower view of transport death.
- `InvO.F1.b`: `ConjugacyPhaseMerge` — Each conjugacy bridge has a phase offset (the angular difference between representations). Phase merge drives all offsets to zero. When all phases align, the representations are in phase — they see the same reality at the same time.
- `InvO.F1.c`: `RotationalEnergyDissipation` — Rotation carries kinetic energy (½Iω²). Compression dissipates this energy: the angular velocity ω decays to zero. The dissipated energy is absorbed into the seed as thermal content (internal energy rather than directed motion).
- `InvO.F1.d`: `TransportConvergence` — The transported value T⁻¹(T(x) + δ) converges to x + T⁻¹(δ) → x as δ → 0. Transport becomes negligible: the correction term vanishes. At convergence, transport is identity and all lens views coincide.

#### Facet 2 - Laws

- `InvO.F2.a`: `AmplitudeDecayLaw` — Transport wave amplitude must decay at least exponentially. Sub-exponential decay indicates a transport mode that resists stillness — its driving force has not been fully exhausted.
- `InvO.F2.b`: `PhaseMergeSmoothnessLaw` — Phase merging must be smooth (no phase jumps). Each phase offset evolves continuously toward zero.
- `InvO.F2.c`: `EnergyConservationLaw` — Total energy (kinetic + internal) is conserved. Energy dissipated from rotation appears as seed thermal content. No energy is created or destroyed.
- `InvO.F2.d`: `AsymptoticIdentityLaw` — The transport map must asymptotically approach the identity map. The convergence rate must be at least geometric (ratio ≤ 1/φ per step).

#### Facet 3 - Constructions

- `InvO.F3.a`: `WaveDamper` — Applies damping to the transport wave. Monitors amplitude decay. Flags any mode with sub-exponential decay. Reports the damped spectrum.
- `InvO.F3.b`: `PhaseMerger` — Continuously adjusts phase offsets toward zero. Uses smooth interpolation (no snapping). Reports phase alignment progress and residual offsets.
- `InvO.F3.c`: `EnergyAccountant` — Tracks kinetic energy (½Iω²) and internal energy (seed thermal content). Verifies conservation at each step. Reports energy flow from rotation to thermal.
- `InvO.F3.d`: `IdentityApproacher` — Computes ||T - id|| at each step. Verifies geometric decay toward zero. Reports convergence rate and projected step to identity.

#### Facet 4 - Certificates

- `InvO.F4.a`: `WaveStillnessCert` — Receipt proving transport wave amplitude at zero, all modes damped, no residual flow.
- `InvO.F4.b`: `PhaseMergeCert` — Receipt proving all phase offsets at zero, smooth evolution, no phase jumps.
- `InvO.F4.c`: `EnergyConservationCert` — Receipt proving total energy conserved, kinetic→thermal conversion complete, no energy lost or created.
- `InvO.F4.d`: `IdentityCert` — Receipt proving transport map converged to identity, convergence rate within bound, all lens views coincide.

### Lens C

#### Facet 1 - Objects

- `InvO.C1.a`: `TransportCessationProbability` — The probability that all transport has ceased at a given moment. Increases as each transport channel quiesces. P(stillness) = Π P(channel_i quiet). When P(stillness) exceeds the threshold, transport is declared at rest.
- `InvO.C1.b`: `ConjugacyAgreementRate` — The fraction of measurements where conjugate representations agree (produce the same observable value). As representations merge, the agreement rate approaches 1. Rate < 1 indicates residual representation-dependence.
- `InvO.C1.c`: `IndependentQuiescenceProduct` — If transport channels are independent, their quiescence probabilities multiply: P(all quiet) = Π P(channel_i quiet). Independence allows parallel shutdown of channels.
- `InvO.C1.d`: `TransportCostNormalization` — The cost of maintaining each transport channel normalized by its information throughput. High-cost/low-throughput channels are shut down first. The normalized ratio governs the shutdown order.

#### Facet 2 - Laws

- `InvO.C2.a`: `StillnessThresholdLaw` — P(stillness) must exceed the declared threshold before transport cessation is certified.
- `InvO.C2.b`: `AgreementConvergenceLaw` — The conjugacy agreement rate must converge to 1. Stagnation below 1 indicates an essential representation difference that cannot be collapsed.
- `InvO.C2.c`: `IndependenceBeforeParallelShutdownLaw` — Parallel channel shutdown only after independence is verified.
- `InvO.C2.d`: `OptimalShutdownOrderLaw` — Channels shut down in order of ascending throughput-per-cost.

#### Facet 3 - Constructions

- `InvO.C3.a`: `StillnessEstimator` — Estimates P(stillness) from channel activity measurements. Reports the current probability and confidence interval.
- `InvO.C3.b`: `AgreementMeasurer` — Samples observable values from conjugate representations. Computes the agreement rate. Reports trend and projected convergence time.
- `InvO.C3.c`: `IndependenceChecker` — Tests channel independence using mutual information. Reports the dependency graph. Authorizes parallel shutdown for independent channels.
- `InvO.C3.d`: `ShutdownScheduler` — Computes throughput-per-cost for each channel. Sorts by ascending ratio. Generates the shutdown schedule.

#### Facet 4 - Certificates

- `InvO.C4.a`: `StillnessCert` — Receipt proving P(stillness) above threshold, all channels quiescent.
- `InvO.C4.b`: `AgreementCert` — Receipt proving agreement rate converged to 1 (or essential differences documented).
- `InvO.C4.c`: `IndependenceCert` — Receipt proving channel independence verified, parallel shutdown authorized.
- `InvO.C4.d`: `ShutdownOrderCert` — Receipt proving optimal shutdown order followed, no high-throughput channel shut down prematurely.

### Lens R

#### Facet 1 - Objects

- `InvO.R1.a`: `RecursiveTransportUnwinding` — Transport operates at multiple scales: global transport (between regions), local transport (within regions), and micro-transport (within cells). Unwinding is recursive: micro first, then local, then global. Each level's stillness simplifies the next level's transport.
- `InvO.R1.b`: `ConjugacyDepthContraction` — Each level of transport nesting adds a conjugacy layer: T₁∘T₂∘...∘Tₙ. Unwinding removes layers one at a time, from innermost to outermost. Each removal contracts the conjugacy depth by 1.
- `InvO.R1.c`: `TransportTreeStillness` — The transport hierarchy forms a tree. Stillness propagates from leaves (micro-transport) to root (global transport). Each leaf achieving stillness simplifies its parent's transport burden.
- `InvO.R1.d`: `ScaleInvariantStillness` — The stillness protocol is the same at every level: identify the transport map, find its fixed point, verify stability, declare stillness. Only the transport content changes.

#### Facet 2 - Laws

- `InvO.R2.a`: `InnermostFirstStillnessLaw` — Micro-transport stills before local, local before global.
- `InvO.R2.b`: `MonotoneDepthReductionLaw` — Conjugacy depth must decrease by exactly 1 at each level.
- `InvO.R2.c`: `LeafFirstPropagationLaw` — Stillness propagates leaf-first through the tree.
- `InvO.R2.d`: `ProtocolInvarianceLaw` — Stillness protocol identical at every level.

#### Facet 3 - Constructions

- `InvO.R3.a`: `RecursiveUnwinder` — Traverses the transport tree bottom-up. At each leaf: finds fixed point, verifies stability, declares stillness. At each parent: simplifies transport using children's fixed points, then finds its own fixed point.
- `InvO.R3.b`: `DepthReducer` — Removes conjugacy layers one at a time from innermost outward. Reports depth at each step. Verifies monotone decrease.
- `InvO.R3.c`: `StillnessPropagator` — Propagates stillness declarations from leaves to root. At each parent: waits for all children to declare stillness, then begins its own stillness procedure.
- `InvO.R3.d`: `ProtocolVerifier` — Compares stillness protocol at each level. Reports deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvO.R4.a`: `RecursiveStillnessCert` — Receipt proving bottom-up unwinding completed, all levels at fixed points, global transport at rest.
- `InvO.R4.b`: `DepthReductionCert` — Receipt proving conjugacy depth decreased monotonically to zero, all layers removed.
- `InvO.R4.c`: `PropagationCert` — Receipt proving leaf-first stillness propagation completed, root reached, all children still before parents.
- `InvO.R4.d`: `ProtocolCert` — Receipt proving scale-invariant stillness protocol confirmed at all levels.
