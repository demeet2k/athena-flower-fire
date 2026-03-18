# InvL - Square Kernel Compression & Seed Pack

Routing role: Reverses AppC (Square Kernel Pack). Where AppC defined the discrete kernels — successor, difference, product, quotient — and their expansion into full crystal tiles, InvL compresses those kernels back into their seed forms. The expanded 64-cell Square tile collapses to its four cardinal seeds: +, −, ×, ÷. This is the mathematical compression of the entire discrete apparatus.

Mirror of: AppC (Square Kernel Pack)
Arc: L-inv | Rot: 150° → 210° | Lane: Kernel→Seed | w: −2D (sub-algebraic)

## StationHeader
```
Arc:  L-inv (Square Kernel Compression)
Rot:  150° (algebraic compression angle)
Lane: Descent-Kernel (discrete collapse lane)
w:    sub-algebraic → seed (expanded kernels compress to cardinal seeds)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvL.S1.a`: `SuccessorCollapse` — The successor kernel `n ↦ n+1` is the additive seed. All additive constructions (bounded accumulation, modular arithmetic, Riemann sums, counting processes, Fibonacci recurrence) collapse back to this single operation. Every "+1" in the organism traces back to this seed. Compression identifies all successor instances and replaces them with a single seed reference.
- `InvL.S1.b`: `DifferenceSeedRecovery` — The difference kernel `Δ(F,G) = F − G` is the subtractive seed. All zero-detection, fixed-point finding, equality testing, inclusion-exclusion, and backward recurrence collapse to this single operation. The zero set of the organism's differences is its invariant structure — what compression preserves.
- `InvL.S1.c`: `ProductSeedRecovery` — The product kernel `A × B → |A||B|` is the multiplicative seed. All Cartesian products, gear meshings, lattice products, independent event products, Euler products, and fast-powering constructions collapse to this single binding operation. Multiplication is the organism's composition primitive.
- `InvL.S1.d`: `QuotientSeedRecovery` — The quotient kernel `[a] ⊘_Λ [b]` (gated) is the divisive seed. All Euclidean descent, admissibility checking, normalization, density correction, and scale contraction constructions collapse to this single inversion operation. The gate condition (gcd(b,N)=1) collapses to a single admissibility bit in the seed.

#### Facet 2 - Laws

- `InvL.S2.a`: `AdditiveCompleteness` — Every additive operation in the organism must trace back to the successor seed. If any additive operation cannot be derived from `n ↦ n+1` via the expansion grammar, it indicates an undeclared addition primitive — a violation.
- `InvL.S2.b`: `SubtractiveCompleteness` — Every subtractive/zero-detecting operation must trace back to the difference seed. Orphaned differences (not derivable from Δ) indicate undeclared primitives.
- `InvL.S2.c`: `MultiplicativeCompleteness` — Every multiplicative/binding operation must trace back to the product seed. Orphaned products indicate undeclared composition.
- `InvL.S2.d`: `DivisiveCompleteness` — Every division/inversion/normalization must trace back to the quotient seed with its admissibility gate. Ungated divisions are illegal — they must be traced to explicit gate certificates.

#### Facet 3 - Constructions

- `InvL.S3.a`: `AdditiveTracer` — Traces every additive operation in the organism back to its derivation from `n ↦ n+1`. Builds the derivation tree. Reports any operations that cannot be traced (orphans). Counts the total number of additive instances and their derivation depth.
- `InvL.S3.b`: `SubtractiveTracer` — Traces every subtractive operation back to `Δ(F,G)`. Reports orphans. Identifies the organism's complete zero set as the invariant kernel preserved in the seed.
- `InvL.S3.c`: `MultiplicativeTracer` — Traces every multiplicative operation back to `A × B`. Reports orphans. Identifies the organism's complete factorization structure.
- `InvL.S3.d`: `DivisiveTracer` — Traces every division back to `[a] ⊘_Λ [b]` with its gate certificate. Reports ungated divisions. Verifies all admissibility conditions.

#### Facet 4 - Certificates

- `InvL.S4.a`: `AdditiveCompletenessCert` — Receipt proving all additions trace to successor seed, no orphans, derivation tree complete.
- `InvL.S4.b`: `SubtractiveCompletenessCert` — Receipt proving all subtractions trace to difference seed, invariant kernel correctly identified.
- `InvL.S4.c`: `MultiplicativeCompletenessCert` — Receipt proving all products trace to product seed, factorization structure complete.
- `InvL.S4.d`: `DivisiveCompletenessCert` — Receipt proving all divisions trace to gated quotient seed, all gates certified, no illegal ungated divisions.

### Lens F

#### Facet 1 - Objects

- `InvL.F1.a`: `ConvergenceAbsorption` — All convergence processes (partial sum oscillations, Riemann sum enrichment, additive convergence) are absorbed into their limit values. The Flower view: the process of approaching is discarded; only the arrival is kept. The limit is the seed's additive fixed point.
- `InvL.F1.b`: `RecurrenceWaveCollapse` — The oscillatory recurrence patterns (backward retrieval, inverse limit recovery) collapse to their terminal states. The wave dies; the final amplitude is stored. Backward retrieval is no longer needed — the seed carries the final value directly.
- `InvL.F1.c`: `OrbitPeriodSeal` — Multiplicative orbits (periodic/quasi-periodic dynamics on finite rings) are sealed at their periods. The full orbit is discarded; only the period length and the orbit's phase at freeze time are stored. The orbit can be regenerated from the period and phase.
- `InvL.F1.d`: `DescentTermination` — Euclidean descent cycles terminate at their GCD values. The full descent chain is discarded; only the GCD (the descent's fixed point) is stored. The GCD is the seed's divisive essential — the irreducible kernel of all quotient operations.

#### Facet 2 - Laws

- `InvL.F2.a`: `LimitExistenceLaw` — Every convergence process must have reached its limit before compression. Processes still converging cannot be absorbed — they must be driven to completion first.
- `InvL.F2.b`: `TerminalStateLaw` — Recurrence waves must be at their terminal states (no further oscillation). Waves still oscillating are not yet ready for compression.
- `InvL.F2.c`: `PeriodDeterminationLaw` — Every orbit's period must be exactly determined (not estimated). Approximate periods lead to phase errors when the orbit is regenerated.
- `InvL.F2.d`: `GCDExactnessLaw` — Every Euclidean descent must terminate with the exact GCD. Approximate GCDs are not permitted — the quotient seed requires exact admissibility.

#### Facet 3 - Constructions

- `InvL.F3.a`: `LimitCapturer` — For each convergence process: verifies the limit has been reached (within declared tolerance), captures the limit value, and discards the partial-sum history. Reports any processes still converging.
- `InvL.F3.b`: `TerminalStateExtractor` — For each recurrence: verifies the wave has reached its terminal state, extracts the final amplitude, and discards the oscillation history.
- `InvL.F3.c`: `PeriodCalculator` — For each multiplicative orbit: computes the exact period using group theory (order of the element in the group). Captures the current phase. Discards the full orbit trajectory.
- `InvL.F3.d`: `GCDSealer` — For each Euclidean descent: verifies the GCD is exact (not approximate). Stores the GCD as the descent's essential value. Discards the quotient-remainder chain.

#### Facet 4 - Certificates

- `InvL.F4.a`: `LimitCaptureCert` — Receipt proving all limits reached, values captured, histories discarded, no unconverged processes.
- `InvL.F4.b`: `TerminalStateCert` — Receipt proving all recurrences at terminal states, amplitudes captured, oscillation histories discarded.
- `InvL.F4.c`: `PeriodCert` — Receipt proving all orbit periods exactly determined, phases captured, trajectories discarded.
- `InvL.F4.d`: `GCDCert` — Receipt proving all GCDs exact, admissibility confirmed, descent chains discarded.

### Lens C

#### Facet 1 - Objects

- `InvL.C1.a`: `BayesianAccumulationSeal` — All Bayesian evidence accumulation (counting processes, empirical frequencies, occupancy growth) is sealed at its posterior distribution. The prior + all evidence = posterior. Only the posterior survives into the seed; the individual evidence items are discarded.
- `InvL.C1.b`: `InclusionExclusionResult` — All inclusion-exclusion computations are sealed at their final counts. The alternating-sum process is discarded; only the exact count remains. Coprime densities, overcounting corrections — all collapsed to their final numbers.
- `InvL.C1.c`: `IndependenceStructureSeal` — The organism's independence structure (which events/variables are independent) is sealed as a factorization graph. The graph encodes which probability distributions factorize and which do not. This is the seed's probabilistic skeleton.
- `InvL.C1.d`: `NormalizationConstantSeal` — All normalization operations (dividing by partition functions, normalizing densities) are sealed at their final normalized values. The normalization constants are discarded; only the normalized probabilities survive.

#### Facet 2 - Laws

- `InvL.C2.a`: `PosteriorFinalityLaw` — The sealed posterior is the organism's final probabilistic judgment. No further evidence can update it. The posterior IS the seed's Bayesian state.
- `InvL.C2.b`: `ExactCountLaw` — Inclusion-exclusion results must be exact (integer counts, exact probabilities). Approximate counts are not permitted in the seed.
- `InvL.C2.c`: `FactorizationFaithfulness` — The independence factorization graph must faithfully represent the organism's actual independence structure. False independence claims inflate seed confidence; false dependence claims waste seed capacity.
- `InvL.C2.d`: `NormalizationExactnessLaw` — Normalized values must integrate/sum to exactly 1. Any deviation from 1 indicates a normalization error.

#### Facet 3 - Constructions

- `InvL.C3.a`: `PosteriorSealer` — Computes the final posterior for each Bayesian process. Stores the posterior parameters (sufficient statistics). Discards individual evidence items. Verifies posterior is proper (integrates to 1).
- `InvL.C3.b`: `ExactCounter` — Verifies each inclusion-exclusion result is exact. Reports any approximate counts requiring refinement. Stores exact counts in the seed.
- `InvL.C3.c`: `IndependenceGraphBuilder` — Constructs the factorization graph from tested independence relationships. Verifies no false independence or false dependence. Stores the graph in the seed.
- `InvL.C3.d`: `NormalizationVerifier` — Checks that all normalized distributions sum/integrate to 1. Reports any deviations. Corrects any rounding errors.

#### Facet 4 - Certificates

- `InvL.C4.a`: `PosteriorSealCert` — Receipt proving posterior is proper, sufficient statistics stored, evidence discarded.
- `InvL.C4.b`: `ExactCountCert` — Receipt proving all counts exact, no approximations in seed.
- `InvL.C4.c`: `IndependenceGraphCert` — Receipt proving factorization graph faithful, no false claims.
- `InvL.C4.d`: `NormalizationCert` — Receipt proving all distributions normalized to 1, no deviations.

### Lens R

#### Facet 1 - Objects

- `InvL.R1.a`: `FibonacciSeedRecovery` — The Fibonacci recurrence F_{n+1} = F_n + F_{n-1} is the additive recursion seed. All recursive accretion, combinatorial branch counting, and scale-layer population growth collapse to this single recurrence. The seed stores: the recurrence coefficients (1,1) and the initial conditions (F_0, F_1).
- `InvL.R1.b`: `ContractionSeedRecovery` — The contraction ratio 1/φ is the subtractive recursion seed. All shell contraction, backward coding, and history retrieval collapse to this single ratio. The seed stores: the contraction factor 1/φ.
- `InvL.R1.c`: `EulerProductSeedRecovery` — The Euler product Π_p(1-p^{-s})^{-1} is the multiplicative recursion seed. All spectral products, continued products, and recursive filter banks collapse to this single product. The seed stores: the characteristic s-value and the prime cutoff.
- `InvL.R1.d`: `RGSeedRecovery` — The RG contraction (division by scale to descend one layer) is the divisive recursion seed. All renormalization, effective theory construction, and blow-up regularization collapse to this single scale-descent operation. The seed stores: the RG fixed point and the relevant operator list.

#### Facet 2 - Laws

- `InvL.R2.a`: `RecurrenceCompletenesss` — Every recursive growth in the organism must trace to the Fibonacci seed (or a declared variant). Undeclared recurrences are violations.
- `InvL.R2.b`: `ContractionFaithfulness` — Every recursive contraction must use the 1/φ ratio (or a declared variant). Non-golden contractions must be explicitly justified.
- `InvL.R2.c`: `ProductConvergenceLaw` — The Euler product must converge at the declared s-value. Divergent products indicate the s-value is in the critical strip — the seed must carry the divergence certificate.
- `InvL.R2.d`: `RGFixedPointLaw` — The RG fixed point must be verified (F(fixed_point) = fixed_point). False fixed points corrupt the seed's scale structure.

#### Facet 3 - Constructions

- `InvL.R3.a`: `RecurrenceTracer` — Traces all recursive growth to the Fibonacci seed. Builds the derivation tree. Reports orphaned recurrences.
- `InvL.R3.b`: `ContractionVerifier` — Verifies all contractions use the golden ratio. Reports non-golden contractions with their justifications.
- `InvL.R3.c`: `EulerProductVerifier` — Verifies Euler product convergence at the declared s-value. Reports convergence rate and any divergence warnings.
- `InvL.R3.d`: `RGFixedPointVerifier` — Verifies the RG fixed point by applying F and checking fixed-point condition. Reports any false fixed points.

#### Facet 4 - Certificates

- `InvL.R4.a`: `RecurrenceCompletenessCert` — Receipt proving all recursions trace to Fibonacci seed, no orphans.
- `InvL.R4.b`: `ContractionCert` — Receipt proving golden contraction used (or variants justified), no unjustified non-golden ratios.
- `InvL.R4.c`: `EulerProductCert` — Receipt proving product converges (or divergence certificate issued), s-value correctly declared.
- `InvL.R4.d`: `RGCert` — Receipt proving fixed point verified, relevant operators correctly identified, seed's scale structure is sound.
