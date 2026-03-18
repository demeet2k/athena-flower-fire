# InvS - Residual Absorption & NEAR Completion

Routing role: Reverses AppJ (Residual Ledgers and NEAR Machinery). Where AppJ tracked residuals — quantities that did not fit cleanly into the lattice structure — and maintained NEAR machinery for approximate operations, InvS absorbs all residuals into the crystal lattice and completes all NEAR approximations to their exact values. Nothing approximate survives into the seed.

Mirror of: AppJ (Residual Ledgers and NEAR Machinery)
Arc: S | Rot: 255° → 105° | Lane: Residual→Absorbed | w: 5D

## StationHeader
```
Arc:  S (Residual Absorption)
Rot:  255° (residual resolution angle)
Lane: Descent-Residual (residual collapse lane)
w:    5D → seed (residuals compress to exact values)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvS.S1.a`: `ResidualAccumulator` — The discrete sum of all outstanding residuals across the lattice. Each residual is a signed quantity representing the gap between the exact value and the lattice-representable approximation. The total residual = Σ(exact - approximate) across all cells. During compression, this total must be driven to zero.
- `InvS.S1.b`: `NEARDifferenceEliminator` — The difference between a NEAR value and its exact target. For each NEAR approximation, computes `Δ = exact - near`. If Δ is within the cell's tolerance, the NEAR is promoted to exact by absorbing the residual. If Δ exceeds tolerance, the cell must be refined.
- `InvS.S1.c`: `ResidualRedistributionProduct` — Residuals that cannot be absorbed locally may be redistributed across neighboring cells. The product of redistribution: each cell receives a share proportional to its capacity. The total redistributed = the original residual. Conservation is exact.
- `InvS.S1.d`: `TruncationQuotient` — The quotient of truncated precision by full precision = the truncation ratio. During expansion, operations were truncated for efficiency. During compression, the truncated portion is recovered and reintegrated. The quotient approaches 1 as all truncations are restored.

#### Facet 2 - Laws

- `InvS.S2.a`: `TotalResidualZeroLaw` — At compression completion, the total residual across all cells must be exactly zero. Any non-zero total indicates incomplete absorption — the compression is not finished.
- `InvS.S2.b`: `NEARCompletionMandateLaw` — Every NEAR value must be resolved to exact (or to a certified-irrational with declared approximation bounds). No NEAR approximation survives into the seed. The seed carries only exact values and explicit irrational certificates.
- `InvS.S2.c`: `RedistributionConservationLaw` — Redistribution must conserve the total residual exactly. The sum of shares distributed to neighbors must equal the original residual. No residual may be created or destroyed during redistribution — only moved.
- `InvS.S2.d`: `TruncationRecoveryLaw` — All truncated precision must be recovered. The truncation quotient must reach 1. If recovery is impossible (the truncated bits were irreversibly lost), a truncation-loss certificate must be issued declaring the permanent precision deficit.

#### Facet 3 - Constructions

- `InvS.S3.a`: `GlobalResidualScanner` — Scans the entire lattice, computing the residual at each cell. Aggregates into the total residual. Reports cells with largest residuals (hotspots) for priority absorption.
- `InvS.S3.b`: `NEARResolver` — For each NEAR value: computes the exact target using higher-precision arithmetic, compares against the NEAR approximation, and either promotes to exact (if within tolerance) or flags for refinement (if outside tolerance).
- `InvS.S3.c`: `CapacityBasedRedistributor` — For each unabsorbable local residual: surveys neighboring cells' capacities, computes shares proportional to capacity, distributes shares, and verifies conservation (total distributed = original).
- `InvS.S3.d`: `TruncationRestorer` — For each truncated operation: retrieves the full-precision result (recomputing if necessary), computes the truncated portion, and reintegrates it. Reports the truncation quotient before and after restoration.

#### Facet 4 - Certificates

- `InvS.S4.a`: `ZeroResidualCert` — Receipt proving total residual is exactly zero, all cells absorbed, no hotspots remaining.
- `InvS.S4.b`: `NEARCompletionCert` — Receipt proving all NEAR values resolved to exact (or certified-irrational), no approximations in the seed.
- `InvS.S4.c`: `RedistributionConservationCert` — Receipt proving redistribution conserved total residual, all shares accounted for, no creation or destruction.
- `InvS.S4.d`: `TruncationRecoveryCert` — Receipt proving truncation quotient = 1 (or permanent losses declared), all recoverable precision restored.

### Lens F

#### Facet 1 - Objects

- `InvS.F1.a`: `ResidualWaveDamping` — Residuals distributed across the lattice form a wave pattern (some cells positive, some negative). Absorption damps this wave to zero amplitude. The damping is smooth: no cell's residual changes sign abruptly.
- `InvS.F1.b`: `ApproximationRefinementCurve` — Each NEAR value's approximation improves along a refinement curve: the difference between approximate and exact decreases with each refinement step. The curve is monotonically decreasing and asymptotically approaches zero.
- `InvS.F1.c`: `ResidualFluxBalance` — Residuals flow between cells like a conserved fluid. The flux into any cell minus the flux out = the change in that cell's residual. At equilibrium (compression complete), all fluxes are zero.
- `InvS.F1.d`: `PrecisionConvergence` — The precision of each value converges to its full-precision limit as truncations are restored. The convergence follows a series: each restoration adds bits of precision, like partial sums approaching the full value.

#### Facet 2 - Laws

- `InvS.F2.a`: `SmoothDampingLaw` — Residual damping must be smooth: no cell's residual may change sign (positive → negative or vice versa) during absorption. Sign changes indicate overshooting, which creates new residuals.
- `InvS.F2.b`: `MonotoneRefinementLaw` — The NEAR-to-exact refinement curve must be monotonically decreasing. Any increase in the approximation error indicates a refinement bug.
- `InvS.F2.c`: `FluxConservationLaw` — The total flux into the lattice boundary must be zero (nothing enters or leaves the closed system). All residual flow is internal redistribution.
- `InvS.F2.d`: `PrecisionMonotoneLaw` — Precision must monotonically increase during truncation recovery. Losing precision during recovery is a regression.

#### Facet 3 - Constructions

- `InvS.F3.a`: `WaveDamper` — Applies a damping field to the residual wave. At each step: reduces the amplitude of the residual at each cell by a fixed fraction, redistributing the absorbed residual to the cell's exact value. Monitors for sign changes.
- `InvS.F3.b`: `RefinementIterator` — For each NEAR value: applies successive refinement steps (e.g., Newton's method for algebraic numbers, continued fraction convergents for irrationals). Tracks the refinement curve. Terminates when the target precision is reached.
- `InvS.F3.c`: `FluxBalancer` — Computes the residual flux between all adjacent cell pairs. Balances flows to drive all residuals toward zero while maintaining conservation. Reports the maximum remaining flux at each iteration.
- `InvS.F3.d`: `PrecisionExtender` — For each truncated value: extends precision by one unit (e.g., one additional decimal digit, one additional binary bit). Iterates until full precision is reached. Reports the precision at each step.

#### Facet 4 - Certificates

- `InvS.F4.a`: `SmoothDampingCert` — Receipt proving damping was smooth, no sign changes, residual amplitude monotonically decreased.
- `InvS.F4.b`: `MonotoneRefinementCert` — Receipt proving refinement curve was monotonically decreasing, target precision reached, no regression.
- `InvS.F4.c`: `FluxConservationCert` — Receipt proving all fluxes balanced, boundary flux is zero, total residual conserved during redistribution.
- `InvS.F4.d`: `PrecisionExtensionCert` — Receipt proving precision monotonically increased, full precision reached, no bits lost during recovery.

### Lens C

#### Facet 1 - Objects

- `InvS.C1.a`: `ResidualDistribution` — The statistical distribution of residuals across the lattice. If well-behaved (normal with mean zero), absorption is straightforward. If skewed or heavy-tailed, special techniques are needed for the tail residuals.
- `InvS.C1.b`: `NEARErrorEstimate` — The expected error of each NEAR approximation, estimated from the approximation method's known error bounds. The error estimate governs the refinement strategy: high-error NEARs are refined first.
- `InvS.C1.c`: `IndependentResidualAbsorption` — If residuals at different cells are independent (no shared cause), absorption can proceed in parallel with P(all absorbed) = Π P(cell_i absorbed). Independence allows massive parallelization.
- `InvS.C1.d`: `PrecisionCostNormalization` — The cost of recovering each truncated bit is normalized by the value of that bit (its contribution to accuracy). High-value/low-cost bits are recovered first. Low-value/high-cost bits may be declared as permanent precision losses if the cost exceeds the value.

#### Facet 2 - Laws

- `InvS.C2.a`: `ZeroMeanRequirement` — The residual distribution must have mean zero before compression begins. Non-zero mean indicates a systematic bias that must be corrected globally before cell-level absorption proceeds.
- `InvS.C2.b`: `ErrorBoundLaw` — Each NEAR approximation's error must be within the declared bound for its method. If actual error exceeds the bound, the approximation method is suspect and must be audited.
- `InvS.C2.c`: `IndependenceVerificationLaw` — Independence must be verified before parallel absorption. Correlated residuals require coordinated absorption.
- `InvS.C2.d`: `ValueCostThresholdLaw` — Bits whose recovery cost exceeds their accuracy value by a declared factor may be declared permanent losses. The factor must be explicitly declared and the precision deficit recorded.

#### Facet 3 - Constructions

- `InvS.C3.a`: `DistributionAnalyzer` — Fits the residual distribution using moment estimation. Tests for zero mean, normality, and heavy tails. Reports the distribution type and any required pre-processing (bias correction, tail handling).
- `InvS.C3.b`: `ErrorAuditor` — For each NEAR approximation: computes actual error, compares against declared bound, flags any bound violations. Reports the audit results and recommendations.
- `InvS.C3.c`: `CorrelationChecker` — Tests pairwise correlation of residuals at different cells. Reports the correlation matrix. Authorizes parallel absorption for uncorrelated cells and coordinates absorption for correlated clusters.
- `InvS.C3.d`: `CostBenefitAnalyzer` — For each truncated bit: estimates recovery cost and accuracy value. Computes the value/cost ratio. Ranks by ratio. Recommends recovery for high-ratio bits and permanent loss for low-ratio bits.

#### Facet 4 - Certificates

- `InvS.C4.a`: `ZeroMeanCert` — Receipt proving residual distribution has zero mean (or bias corrected), distribution analysis complete.
- `InvS.C4.b`: `ErrorBoundCert` — Receipt proving all NEAR errors within declared bounds, no violations unresolved.
- `InvS.C4.c`: `CorrelationCert` — Receipt proving independence verified (or correlations accounted for), absorption strategy consistent with correlation structure.
- `InvS.C4.d`: `CostBenefitCert` — Receipt proving value/cost analysis complete, recovery decisions justified, permanent losses explicitly declared.

### Lens R

#### Facet 1 - Objects

- `InvS.R1.a`: `RecursiveResidualAbsorption` — Residuals exist at every level of the lattice hierarchy: global residuals, shell residuals, cell residuals, sub-cell residuals. Absorption is recursive: absorb sub-cell residuals into cells, cell residuals into shells, shell residuals into the global total.
- `InvS.R1.b`: `HierarchicalNEARCompletion` — NEAR values at deeper lattice levels must be completed before their ancestors. A shell-level NEAR depends on its cells' exact values. Bottom-up completion ensures consistency.
- `InvS.R1.c`: `ResidualTreeCollapse` — The residual hierarchy forms a tree. As bottom-level residuals are absorbed, their parent nodes' residuals change (because the children are now exact). The tree collapses level by level until only the root residual remains — which must be zero.
- `InvS.R1.d`: `ScaleInvariantAbsorption` — The absorption protocol is the same at every level: scan, compute residual, absorb or redistribute, verify zero. Only the scale changes. The protocol is a fixed point of the lattice hierarchy.

#### Facet 2 - Laws

- `InvS.R2.a`: `BottomUpAbsorptionLaw` — Sub-cell residuals must be absorbed before cell residuals. Cell residuals before shell residuals. Shell residuals before global. No level is absorbed until all its children are exact.
- `InvS.R2.b`: `HierarchicalConsistencyLaw` — Completing a lower-level NEAR must not create a new residual at a higher level. If it does, the completion is inconsistent and must be revised.
- `InvS.R2.c`: `MonotoneTreeCollapseLaw` — The residual tree must collapse monotonically: the number of non-zero residuals decreases at each step. Any increase indicates an absorption error.
- `InvS.R2.d`: `ProtocolFixedPointLaw` — The absorption protocol must be identical at every level. Level-specific protocols indicate inconsistency.

#### Facet 3 - Constructions

- `InvS.R3.a`: `HierarchicalScanner` — Scans the residual tree bottom-up. At each leaf level: computes residuals, absorbs them, and propagates the effect to parents. Reports level-by-level absorption progress.
- `InvS.R3.b`: `ConsistencyChecker` — After each lower-level completion, checks all ancestors for new residuals. Reports any inconsistencies and recommends revisions.
- `InvS.R3.c`: `TreeCollapseMonitor` — Tracks the count of non-zero residuals at each step. Verifies monotone decrease. Reports any increases as absorption errors.
- `InvS.R3.d`: `ProtocolVerifier` — Compares the absorption protocol at each level. Reports any level-specific deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvS.R4.a`: `HierarchicalAbsorptionCert` — Receipt proving bottom-up absorption completed, all levels processed in order, no premature absorption.
- `InvS.R4.b`: `ConsistencyCert` — Receipt proving no lower-level completions created higher-level residuals, consistency maintained throughout.
- `InvS.R4.c`: `MonotoneCollapseCert` — Receipt proving non-zero residual count decreased monotonically, no absorption errors.
- `InvS.R4.d`: `ProtocolCert` — Receipt proving protocol identical at all levels, scale-invariant absorption confirmed.
