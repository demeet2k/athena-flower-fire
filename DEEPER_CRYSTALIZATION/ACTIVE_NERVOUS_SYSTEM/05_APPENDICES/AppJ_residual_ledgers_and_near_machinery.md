# AppJ - Residual Ledgers and NEAR Machinery

Routing role: Residual envelopes, bounded approximation, NEAR upgrades, and partial-closure bookkeeping.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppJ.S1.a`: `NearOKEnvelope` — A residual result tagged `NEAR-OK(δ)` where `δ < ε_threshold` is the signed distance from exact correctness. The result is usable but carries a correction debt `δ` that must be accounted for in downstream computations.
- `AppJ.S1.b`: `NearFailEnvelope` — A residual result tagged `NEAR-FAIL(δ)` where `δ ≥ ε_threshold` but the failure mode is classified and bounded. The result is not usable directly but contains enough information to guide repair: the failure type, the gap magnitude, and the nearest OK configuration.
- `AppJ.S1.c`: `NearAmbigEnvelope` — A residual result tagged `NEAR-AMBIG(S, w)` where `S = {c_1,...,c_k}` is the candidate set and `w = [w_1,...,w_k]` are confidence weights summing to 1. The result is a weighted superposition of `k` possible answers, not yet collapsed to a single value.
- `AppJ.S1.d`: `ResidualLedger` — The global ledger `R` tracking all outstanding residuals across the crystal, organized by shell and archetype. Each entry records `(address, tag, δ, timestamp, attempts)` enabling aggregate residual health monitoring.

#### Facet 2 - Laws

- `AppJ.S2.a`: `ResidualClassificationExhaustiveness` — Every non-exact result must be classified into exactly one of `{NEAR-OK, NEAR-FAIL, NEAR-AMBIG}`. No residual may exist in an unclassified state; the three tags partition the space of near-miss outcomes.
- `AppJ.S2.b`: `CorrectionDebtMonotonicity` — For `NEAR-OK` residuals, the correction debt `δ` must not increase under downstream operations: `δ(f(x)) ≤ δ(x) + ε_f` where `ε_f` is the declared error bound of operation `f`. Debt accumulates additively, never multiplicatively.
- `AppJ.S2.c`: `NearFailBoundedness` — Every `NEAR-FAIL` residual has a finite gap magnitude `δ < ∞` and a classified failure mode from the enumerated set `{TypeMismatch, RangeExceeded, CycleDetected, DependencyMissing}`. Unclassified failures are illegal.
- `AppJ.S2.d`: `LedgerCompleteness` — The residual ledger contains every outstanding residual in the crystal. No residual may exist off-ledger; creation and retirement of residuals are atomic operations that always update the ledger.

#### Facet 3 - Constructions

- `AppJ.S3.a`: `ResidualClassifier` — The triage engine that takes a raw computation result and its expected target, computes the distance `δ`, and classifies the result into `NEAR-OK`, `NEAR-FAIL`, or `NEAR-AMBIG` based on threshold comparison and candidate-set analysis.
- `AppJ.S3.b`: `CorrectionDebtTracker` — The accumulator that maintains a running debt total `D = Σ δ_i` for each shard, updating as operations compose, and triggering a recalibration event when `D` exceeds the shard's declared tolerance budget.
- `AppJ.S3.c`: `FailureModeAnalyzer` — The analyzer that takes a `NEAR-FAIL` envelope and decomposes its gap into structural components: which conservation law was violated, which address component was out of range, what dependency was missing, outputting a structured repair hint.
- `AppJ.S3.d`: `LedgerCompactor` — The garbage collector that scans the residual ledger for retired entries (resolved residuals with `attempts > 0` and final status `OK`), archives them to the history log, and compacts the active ledger to contain only outstanding residuals.

#### Facet 4 - Certificates

- `AppJ.S4.a`: `ClassificationCert` — Receipt proving a result was classified into exactly one residual category, the distance `δ` was correctly computed, and the threshold comparison used the current calibrated values.
- `AppJ.S4.b`: `DebtBoundCert` — Receipt proving the cumulative correction debt for a shard remains within its tolerance budget, listing each contributing operation and its individual `ε_f` bound.
- `AppJ.S4.c`: `FailureAnalysisCert` — Receipt proving a `NEAR-FAIL` was analyzed into a classified failure mode, the gap magnitude is finite and correctly measured, and the repair hint is consistent with the failure type.
- `AppJ.S4.d`: `LedgerIntegrityCert` — Receipt proving the residual ledger is complete (no off-ledger residuals), consistent (no duplicate entries), and compacted (no retired entries remain in the active section).

### Lens F

#### Facet 1 - Objects

- `AppJ.F1.a`: `ResidualWave` — A propagating disturbance in the residual ledger where a `NEAR-FAIL` at address `A` induces `NEAR-OK` residuals at neighboring addresses `{A ± Δ}`, creating a wave front of degraded-but-usable results spreading outward from the failure source.
- `AppJ.F1.b`: `ConvergenceFunnel` — The dynamic trajectory of a `NEAR-OK` residual's correction debt `δ(t)` over successive refinement cycles, forming a funnel shape: wide at entry (large `δ`), narrowing toward zero as iterative correction converges.
- `AppJ.F1.c`: `ResidualResonance` — The phenomenon where two `NEAR-AMBIG` residuals at nearby addresses have candidate sets that overlap, causing their confidence weights to oscillate in anti-phase as evidence for one candidate strengthens the other's alternative.
- `AppJ.F1.d`: `NearMissFlowField` — The vector field over the crystal assigning to each address the direction `∇δ` of steepest residual improvement, guiding repair operations toward the regions of highest residual concentration.

#### Facet 2 - Laws

- `AppJ.F2.a`: `WaveAttenuationLaw` — Residual waves attenuate with distance from the failure source: the induced `δ` at distance `r` is bounded by `δ_0 / r²` where `δ_0` is the original failure gap. Waves cannot amplify through propagation alone.
- `AppJ.F2.b`: `FunnelConvergenceLaw` — Every `NEAR-OK` convergence funnel must narrow at a rate of at least `δ(t+1) ≤ (1 - η) δ(t)` for contraction rate `η > 0`. Stalled funnels (zero convergence rate) trigger escalation to `NEAR-FAIL`.
- `AppJ.F2.c`: `ResonanceDecouplingLaw` — Residual resonance between two `NEAR-AMBIG` addresses must decouple within `T_max` cycles as evidence accumulates; perpetual oscillation is forbidden. Decoupling occurs when one candidate achieves confidence `> 1 - ε`.
- `AppJ.F2.d`: `FlowFieldIrrotationality` — The near-miss flow field `∇δ` is irrotational (curl-free) on each shell: there are no closed repair loops that cycle without reducing total residual. Every repair path leads monotonically toward lower total `δ`.

#### Facet 3 - Constructions

- `AppJ.F3.a`: `WavePropagator` — The engine that computes residual wave propagation from a `NEAR-FAIL` source, applying the attenuation law `δ_0/r²` to determine induced residuals at each neighbor, and updating the ledger with the new `NEAR-OK` entries.
- `AppJ.F3.b`: `FunnelTracker` — The monitor that tracks each `NEAR-OK` residual's convergence funnel, measuring the contraction rate `η` at each cycle, and escalating to `NEAR-FAIL` if `η` drops below the minimum threshold for `k` consecutive cycles.
- `AppJ.F3.c`: `ResonanceBreaker` — The intervention engine that detects residual resonance between `NEAR-AMBIG` pairs, injects disambiguating evidence (from AppL evidence plans), and forces decoupling by boosting the leading candidate's weight.
- `AppJ.F3.d`: `RepairFlowSolver` — The gradient descent engine that follows the `∇δ` flow field to determine the optimal repair ordering: which residuals to fix first to maximize total `δ` reduction per repair operation.

#### Facet 4 - Certificates

- `AppJ.F4.a`: `WaveAttenuationCert` — Receipt proving residual wave propagation followed the attenuation law, no amplification occurred, and all induced residuals were correctly logged in the ledger.
- `AppJ.F4.b`: `FunnelConvergenceCert` — Receipt proving a `NEAR-OK` funnel converged to exact within `T` cycles at the declared contraction rate, or documenting the escalation to `NEAR-FAIL` with stall evidence.
- `AppJ.F4.c`: `ResonanceBreakCert` — Receipt proving resonance between two `NEAR-AMBIG` addresses was broken within `T_max` cycles, the winning candidate achieved confidence `> 1 - ε`, and the injected evidence was legitimate.
- `AppJ.F4.d`: `RepairFlowCert` — Receipt proving the repair ordering followed the irrotational flow field, total `δ` decreased monotonically, and no repair cycle was entered.

### Lens C

#### Facet 1 - Objects

- `AppJ.C1.a`: `ResidualDistribution` — The probability distribution `P(δ)` of residual magnitudes across the crystal, typically following a truncated exponential `P(δ) ∝ e^{-λδ}` for `δ ∈ [0, δ_max]`, characterizing the organism's overall approximation quality.
- `AppJ.C1.b`: `ConvergenceRateEstimator` — The statistical estimator `η̂` for the true convergence rate `η` from `NEAR-OK` to `OK`, computed from observed transition times using maximum likelihood on the geometric distribution `P(T=t) = η(1-η)^{t-1}`.
- `AppJ.C1.c`: `ResidualHealthScore` — The aggregate health metric `H = 1 - E[δ]/δ_max` summarizing the crystal's residual state as a single number in `[0,1]`, where `H = 1` means all results are exact and `H = 0` means all results are at maximum allowed deviation.
- `AppJ.C1.d`: `NearToOKTransitionMatrix` — The Markov transition matrix `M[i,j]` giving the probability of transitioning from residual state `i ∈ {NEAR-OK, NEAR-FAIL, NEAR-AMBIG}` to state `j ∈ {OK, NEAR-OK, NEAR-FAIL, NEAR-AMBIG, FAIL}` in one refinement cycle.

#### Facet 2 - Laws

- `AppJ.C2.a`: `ResidualDistributionStability` — The residual distribution `P(δ)` is stationary under normal organism operation: the rate of new residual creation equals the rate of residual resolution, maintaining a steady-state distribution with finite mean and variance.
- `AppJ.C2.b`: `ConvergenceRatePositivityLaw` — The estimated convergence rate `η̂` must be strictly positive: `η̂ > η_min > 0`. A zero or negative convergence rate indicates systematic failure and triggers organism-level alarm via AppK conflict protocols.
- `AppJ.C2.c`: `HealthScoreMonotonicity` — Under active repair, the health score `H(t)` is non-decreasing in expectation: `E[H(t+1)] ≥ E[H(t)]`. Repair operations must, on average, improve the crystal's residual health.
- `AppJ.C2.d`: `TransitionMatrixErgodicity` — The `NEAR-to-OK` transition matrix `M` is ergodic: from any residual state, there is a positive probability path to `OK` within finite steps. No residual state is absorbing except `OK` and `FAIL`.

#### Facet 3 - Constructions

- `AppJ.C3.a`: `DistributionFitter` — The statistical engine that fits the residual distribution `P(δ)` to observed data using maximum likelihood estimation, selecting between exponential, Pareto, and log-normal models by AIC comparison.
- `AppJ.C3.b`: `ConvergenceRateTracker` — The online estimator that maintains a running MLE of the convergence rate `η̂` from observed `NEAR-OK → OK` transition times, with confidence intervals and trend detection for rate changes.
- `AppJ.C3.c`: `HealthDashboard` — The monitoring construction that computes the aggregate health score `H`, decomposes it by shell, archetype, and metro line, and generates alerts when any sub-population's health drops below threshold.
- `AppJ.C3.d`: `TransitionMatrixEstimator` — The estimator that builds the empirical transition matrix `M̂` from observed state transitions, tests for ergodicity by checking that the matrix's second-largest eigenvalue `|λ_2| < 1`, and computes the stationary distribution.

#### Facet 4 - Certificates

- `AppJ.C4.a`: `DistributionFitCert` — Receipt proving the residual distribution was fit to observed data, the selected model is the best by AIC, and the fitted parameters are within confidence bounds.
- `AppJ.C4.b`: `ConvergenceRateCert` — Receipt proving the convergence rate estimate `η̂` is positive, the confidence interval excludes zero, and the estimation used at least `N_min` observed transitions.
- `AppJ.C4.c`: `HealthScoreCert` — Receipt proving the aggregate health score was computed correctly, the decomposition by sub-population is consistent with the aggregate, and all sub-populations are above minimum threshold.
- `AppJ.C4.d`: `ErgodicityVerificationCert` — Receipt proving the transition matrix is ergodic, `|λ_2| < 1`, the stationary distribution assigns positive probability to `OK`, and no absorbing non-terminal state exists.

### Lens R

#### Facet 1 - Objects

- `AppJ.R1.a`: `IterativeRefiner` — The recursive engine `R(x_0) = lim_{n→∞} f^n(x_0)` that takes a `NEAR-OK` result `x_0` and iteratively applies correction function `f` until `δ(x_n) < ε_target` or the iteration budget `N_max` is exhausted.
- `AppJ.R1.b`: `ResidualFixedPoint` — The fixed point `x* = f(x*)` of the correction function, representing the exact answer that the iterative refiner converges toward. When `δ(x*) = 0`, the residual is fully resolved; the `NEAR` tag is promoted to `OK`.
- `AppJ.R1.c`: `MultiScaleRefinementLadder` — A nested sequence of refinement levels `L_0 ⊂ L_1 ⊂ ... ⊂ L_k` where each level `L_i` resolves residuals at scale `2^{-i}`, and the correction at level `i` feeds the initial condition for level `i+1`, forming a multigrid V-cycle.
- `AppJ.R1.d`: `SelfCorrectingResidual` — A residual that contains its own correction procedure as metadata: the `NEAR-OK` envelope includes a function `repair: δ → δ'` such that repeated application `repair^n(δ) → 0`. The residual carries its own cure.

#### Facet 2 - Laws

- `AppJ.R2.a`: `ContractionMappingLaw` — The correction function `f` must be a contraction: `|f(x) - f(y)| ≤ κ|x - y|` with `κ < 1`. This guarantees convergence by Banach's fixed-point theorem and bounds the convergence rate by `δ_n ≤ κ^n δ_0`.
- `AppJ.R2.b`: `FixedPointUniquenessLaw` — The contraction mapping has a unique fixed point `x*` in the crystal's metric space. Multiple fixed points would create ambiguity about which exact answer to converge toward; uniqueness ensures deterministic refinement.
- `AppJ.R2.c`: `MultiscaleConsistencyLaw` — Corrections at coarse level `L_i` must be consistent with fine level `L_{i+1}`: the restriction of `L_{i+1}`'s correction to `L_i`'s scale must equal `L_i`'s correction. No scale introduces contradictory corrections.
- `AppJ.R2.d`: `SelfCorrectionTerminationLaw` — Every self-correcting residual must terminate: the embedded repair function satisfies the contraction law with `κ < 1`, guaranteeing `δ < ε_target` within `⌈log(δ_0/ε_target) / log(1/κ)⌉` iterations.

#### Facet 3 - Constructions

- `AppJ.R3.a`: `BanachIterator` — The fixed-point iterator implementing Banach's contraction principle: given `f` with Lipschitz constant `κ < 1` and initial `x_0`, computes `x_{n+1} = f(x_n)` with early termination when `|x_{n+1} - x_n| < ε(1-κ)/κ` guarantees `|x_n - x*| < ε`.
- `AppJ.R3.b`: `FixedPointVerifier` — The verifier that takes a candidate fixed point `x*` and confirms `f(x*) = x*` within machine precision, computing the residual `|f(x*) - x*|` and certifying it is below the declared tolerance.
- `AppJ.R3.c`: `MultigridVCycleEngine` — The V-cycle solver that descends from fine to coarse scales, solves the correction equation at the coarsest level, and interpolates corrections back up through each level, achieving `O(N)` total work for `N` total unknowns.
- `AppJ.R3.d`: `SelfRepairInjector` — The construction that takes a raw `NEAR-OK` result and attaches a self-repair function derived from the local Jacobian of the correction map, producing a `SelfCorrectingResidual` that carries its own convergence guarantee.

#### Facet 4 - Certificates

- `AppJ.R4.a`: `ContractionCert` — Receipt proving the correction function satisfies the contraction condition `κ < 1`, the convergence bound `δ_n ≤ κ^n δ_0` was verified for the first `k` iterations, and the fixed point was reached within budget.
- `AppJ.R4.b`: `FixedPointCert` — Receipt proving the candidate fixed point satisfies `|f(x*) - x*| < ε`, the uniqueness condition holds in the declared neighborhood, and the residual was promoted from `NEAR-OK` to `OK`.
- `AppJ.R4.c`: `MultigridConsistencyCert` — Receipt proving the V-cycle corrections are consistent across all scale levels, the coarse-grid solution is correct, and the interpolated fine-grid correction achieves the target residual reduction.
- `AppJ.R4.d`: `SelfRepairCert` — Receipt proving the self-correcting residual's embedded repair function is a valid contraction, the termination bound is finite, and the repair function was derived correctly from the local Jacobian.
