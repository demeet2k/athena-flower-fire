# AppL - Evidence Plans and AMBIG Promotion

Routing role: Candidate sets, evidence plans, ambiguity handling, and promotion harnesses.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppL.S1.a`: `WitnessBundle` — A structured collection `W = {(w_1, σ_1), ..., (w_k, σ_k)}` of witness values `w_i` paired with their provenance signatures `σ_i`, forming the atomic unit of evidence. A witness bundle is valid when all signatures verify and the witnesses are mutually consistent.
- `AppL.S1.b`: `ProofPlan` — A directed acyclic graph `P = (V, E)` where vertices are evidence milestones and edges are inference steps, specifying the exact sequence of observations and deductions needed to promote a `NEAR-AMBIG` result to a definite `OK`. Each edge is labeled with its required witness type.
- `AppL.S1.c`: `EvidenceChain` — A linearly ordered sequence `e_1 → e_2 → ... → e_n` of evidence items where each `e_{i+1}` depends on `e_i`, forming a chain of custody from raw observation to final conclusion. The chain's strength is its weakest link: `strength(chain) = min_i strength(e_i)`.
- `AppL.S1.d`: `CandidateSet` — The explicit enumeration `S = {c_1, ..., c_k}` of all possible answers for an ambiguous result, each annotated with a prior probability `p_i` and the set of distinguishing evidence items that would confirm or eliminate it.

#### Facet 2 - Laws

- `AppL.S2.a`: `WitnessConsistencyLaw` — All witnesses in a bundle must be mutually consistent: for any pair `(w_i, w_j)`, the conjunction `w_i ∧ w_j` must be satisfiable. Inconsistent witness bundles are rejected and routed to AppK conflict resolution.
- `AppL.S2.b`: `ProofPlanCompleteness` — A proof plan must cover all candidates: for each candidate `c_i` in the candidate set, the plan contains at least one evidence path that either confirms `c_i` (promoting it to OK) or eliminates it (reducing the candidate set). No candidate may be left unaddressed.
- `AppL.S2.c`: `EvidenceChainIntegrity` — An evidence chain is valid only if every link is present and verified: removing any single evidence item `e_i` invalidates the chain. There are no shortcuts; each step must be witnessed.
- `AppL.S2.d`: `CandidateSetExhaustiveness` — The candidate set must contain the true answer: `true_answer ∈ S` is a precondition for promotion. If the true answer is not among the candidates, the promotion process will fail and the result must be escalated to evidence plan revision.

#### Facet 3 - Constructions

- `AppL.S3.a`: `WitnessBundleAssembler` — The construction that collects individual witness values from across the crystal, verifies each provenance signature, checks mutual consistency via pairwise conjunction testing, and packages them into a validated `WitnessBundle`.
- `AppL.S3.b`: `ProofPlanCompiler` — The compiler that takes a candidate set and the available evidence types, constructs a proof plan DAG that covers all candidates, optimizes the plan for minimum expected evidence-gathering cost, and outputs the executable plan with milestone checkpoints.
- `AppL.S3.c`: `EvidenceChainLinker` — The linker that connects individual evidence items into a chain, verifying that each item's output type matches the next item's input type, computing the chain's overall strength, and flagging any weak links that need reinforcement.
- `AppL.S3.d`: `CandidateSetGenerator` — The generator that, given an ambiguous result and the crystal's type constraints, enumerates all possible candidates, assigns prior probabilities based on frequency data, and identifies the distinguishing evidence for each candidate.

#### Facet 4 - Certificates

- `AppL.S4.a`: `WitnessBundleCert` — Receipt proving all witnesses in the bundle are consistently signed, mutually consistent, and collected within the declared time window, with each provenance signature independently verified.
- `AppL.S4.b`: `ProofPlanCoverageCert` — Receipt proving the proof plan covers all candidates in the candidate set, every evidence path terminates in either confirmation or elimination, and the plan is acyclic (no circular evidence dependencies).
- `AppL.S4.c`: `EvidenceChainCert` — Receipt proving the evidence chain is complete (no missing links), each link is independently verified, and the chain's minimum strength exceeds the required threshold for promotion.
- `AppL.S4.d`: `CandidateExhaustivenessCert` — Receipt proving the candidate set is exhaustive with respect to the crystal's type constraints, listing the enumeration method used and the constraint satisfaction check that confirmed no candidate was missed.

### Lens F

#### Facet 1 - Objects

- `AppL.F1.a`: `EvidenceSearchWave` — A propagating search front that expands outward from an ambiguous result, querying neighboring shards for evidence relevant to the candidate set. The wave carries the current candidate weights and returns with updated evidence from each shard it visits.
- `AppL.F1.b`: `HypothesisTestCycle` — The iterative cycle `Hypothesize → Predict → Observe → Update` applied to each candidate: generate a prediction `p_i` from candidate `c_i`, observe the actual value `o`, and update the candidate's weight via `w_i ∝ P(o | c_i) · w_i`.
- `AppL.F1.c`: `EvidenceGatheringSchedule` — The time-ordered plan `[t_1: gather(e_1), t_2: gather(e_2), ...]` specifying when each evidence item should be collected, optimized for minimum total time while respecting dependency ordering (some evidence requires prior evidence to be available).
- `AppL.F1.d`: `PromotionCascade` — The chain reaction triggered when one candidate's promotion resolves dependencies for other ambiguous results, causing a cascade of promotions: resolving `c_1` at address `A_1` provides the evidence needed to resolve `c_2` at `A_2`, and so on.

#### Facet 2 - Laws

- `AppL.F2.a`: `SearchWaveCausalityLaw` — The evidence search wave propagates at speed `v ≤ 1` shell per time step. No shard is queried before the wave front arrives; evidence gathering respects the crystal's causal structure.
- `AppL.F2.b`: `HypothesisTestMonotonicity` — After each hypothesis test cycle, the total uncertainty `H = -Σ w_i log w_i` (Shannon entropy of candidate weights) must decrease or remain constant. Evidence never increases ambiguity; it can only reduce or preserve it.
- `AppL.F2.c`: `ScheduleOptimalityLaw` — The evidence gathering schedule must be locally optimal: no reordering of two adjacent evidence items `e_i, e_{i+1}` would reduce the expected total gathering time. Global optimality is not required, but local optimality is enforced.
- `AppL.F2.d`: `CascadeTerminationLaw` — Every promotion cascade must terminate within `L_max` steps (bounded by the crystal's longest dependency chain). Infinite cascades are impossible because the candidate set is finite and each promotion strictly reduces the global ambiguity count.

#### Facet 3 - Constructions

- `AppL.F3.a`: `SearchWaveLauncher` — The construction that initializes an evidence search wave at the ambiguous result's address, computes the initial propagation direction based on the dependency graph, and dispatches query packets to the first shell of neighbors.
- `AppL.F3.b`: `HypothesisTestEngine` — The engine that executes hypothesis test cycles: generates predictions from each candidate, collects observations, computes likelihoods `P(o | c_i)`, and updates candidate weights via Bayesian multiplication and renormalization.
- `AppL.F3.c`: `ScheduleOptimizer` — The optimizer that takes the raw evidence plan and dependency constraints, applies topological sort with earliest-deadline-first scheduling, and produces a time-ordered gathering schedule with minimum expected completion time.
- `AppL.F3.d`: `CascadeExecutor` — The engine that manages promotion cascades: when a candidate is promoted, scans downstream dependencies for newly resolvable ambiguities, triggers their promotion, and tracks the cascade depth against the termination bound.

#### Facet 4 - Certificates

- `AppL.F4.a`: `SearchWaveCert` — Receipt proving the evidence search wave propagated at legal speed, all queried shards responded, and the returned evidence was incorporated into the candidate weights.
- `AppL.F4.b`: `HypothesisTestCert` — Receipt proving each hypothesis test cycle reduced or preserved total uncertainty, the likelihood computations were correct, and the weight updates were properly normalized.
- `AppL.F4.c`: `ScheduleOptimalityCert` — Receipt proving the evidence gathering schedule is locally optimal, dependency ordering was respected, and the expected completion time was computed correctly.
- `AppL.F4.d`: `CascadeTerminationCert` — Receipt proving the promotion cascade terminated within `L_max` steps, each promotion was valid, and the global ambiguity count decreased by the declared amount.

### Lens C

#### Facet 1 - Objects

- `AppL.C1.a`: `BayesianEvidenceAccumulator` — The running posterior distribution `P(c_i | e_1, ..., e_t) ∝ P(c_i) · Π_{j=1}^{t} P(e_j | c_i)` tracking the probability of each candidate after `t` evidence items, updated online as each new piece of evidence arrives.
- `AppL.C1.b`: `LikelihoodRatioMatrix` — The `k × k` matrix `LR[i,j] = P(evidence | c_i) / P(evidence | c_j)` of pairwise likelihood ratios between candidates, enabling direct comparison of how well each candidate explains the observed evidence relative to every other candidate.
- `AppL.C1.c`: `PromotionThreshold` — The decision threshold `τ` such that candidate `c_i` is promoted to definite answer when `P(c_i | evidence) > τ`. The threshold is calibrated to control the false promotion rate: `P(wrong promotion) < α` for declared significance level `α`.
- `AppL.C1.d`: `EvidenceInformationValue` — The expected information gain `V(e) = H(candidates) - E_{e}[H(candidates | e)]` of gathering evidence item `e`, measured in bits. High-value evidence items are those that most sharply distinguish between candidates.

#### Facet 2 - Laws

- `AppL.C2.a`: `BayesianConsistencyLaw` — The posterior distribution must be a proper probability distribution at all times: `Σ P(c_i | evidence) = 1`, `P(c_i | evidence) ≥ 0` for all `i`. Updates must preserve normalization; unnormalized intermediates are forbidden in the final output.
- `AppL.C2.b`: `LikelihoodRatioTransitivity` — Likelihood ratios are transitive: `LR[i,k] = LR[i,j] · LR[j,k]` for any triple of candidates. This consistency condition prevents circular evidence that favors `c_i > c_j > c_k > c_i`.
- `AppL.C2.c`: `ThresholdCalibrationLaw` — The promotion threshold `τ` must satisfy `τ ≥ 1 - α` where `α` is the declared false promotion rate. Higher thresholds are permitted (more conservative); lower thresholds violate the significance guarantee.
- `AppL.C2.d`: `InformationValuePositivityLaw` — The expected information value of any evidence item is non-negative: `V(e) ≥ 0`. Evidence never increases expected ambiguity. An item with `V(e) = 0` is uninformative and can be skipped.

#### Facet 3 - Constructions

- `AppL.C3.a`: `OnlineBayesianUpdater` — The sequential updater that processes evidence items one at a time, multiplying the current posterior by the likelihood of each candidate given the new evidence, and renormalizing to maintain a proper distribution.
- `AppL.C3.b`: `LikelihoodRatioComputer` — The engine that computes the full `k × k` likelihood ratio matrix from the candidate models and observed evidence, verifies transitivity, and flags any inconsistencies for investigation.
- `AppL.C3.c`: `ThresholdOptimizer` — The optimizer that selects the promotion threshold `τ` to minimize expected decision cost (balancing false promotions against delayed promotions), subject to the calibration constraint `τ ≥ 1 - α`.
- `AppL.C3.d`: `InformationValueRanker` — The ranker that computes `V(e)` for each available evidence item, sorts them by expected information gain, and recommends the highest-value item to gather next, implementing the optimal experimental design for ambiguity resolution.

#### Facet 4 - Certificates

- `AppL.C4.a`: `BayesianUpdateCert` — Receipt proving the posterior distribution was updated correctly for each evidence item, normalization was maintained at every step, and the final posterior is a proper probability distribution.
- `AppL.C4.b`: `LikelihoodRatioConsistencyCert` — Receipt proving the likelihood ratio matrix satisfies transitivity, no circular evidence exists, and each ratio was computed from the correct candidate models.
- `AppL.C4.c`: `PromotionDecisionCert` — Receipt proving a candidate was promoted above threshold `τ`, the threshold satisfies the calibration constraint, and the posterior probability at time of promotion is recorded.
- `AppL.C4.d`: `InformationValueCert` — Receipt proving information values were computed correctly, all values are non-negative, and the recommended next evidence item has the highest expected gain among available options.

### Lens R

#### Facet 1 - Objects

- `AppL.R1.a`: `SelfGeneratingWitness` — A system component whose normal operation produces evidence for its own correctness: by running, it generates a trace that constitutes a witness for the claim that it ran correctly. The witness is a byproduct of computation, not a separate verification step.
- `AppL.R1.b`: `BootstrappedProofPlan` — A proof plan whose first milestone is the construction of the rest of the proof plan: `Step_1 = "build Steps_2..n"`. The plan generates itself as it executes, adapting to the evidence discovered at each stage rather than being fixed in advance.
- `AppL.R1.c`: `RecursiveEvidenceAmplifier` — The recursive construction where evidence at depth `d` amplifies evidence at depth `d+1`: `strength(e_{d+1}) = g(strength(e_d))` for amplification function `g` with `g(x) > x` when `x > x_threshold`. Weak evidence bootstraps into strong evidence through recursive reinforcement.
- `AppL.R1.d`: `AutonomousPromotionLoop` — A closed-loop system where the promoted result generates evidence that confirms the promotion, which strengthens the result, which generates more evidence: `Result → Evidence → Promotion → StrongerResult → MoreEvidence → ...` converging to a self-sustaining fixed point.

#### Facet 2 - Laws

- `AppL.R2.a`: `SelfWitnessingSoundnessLaw` — A self-generating witness is sound only if the system's correctness implies the witness's validity AND the witness's validity implies the system's correctness. The biconditional `correct ↔ valid_witness` must hold; one-directional implication is insufficient.
- `AppL.R2.b`: `BootstrapTerminationLaw` — Every bootstrapped proof plan must terminate: the self-generating step `Step_1` produces a finite plan `Steps_2..n` with `n < N_max`. Proof plans that generate infinitely long proof plans are forbidden; the bootstrap must converge.
- `AppL.R2.c`: `AmplificationConvergenceLaw` — The recursive evidence amplifier must converge: `g^n(strength_0) → strength_max < ∞` as `n → ∞`. Unbounded amplification would manufacture certainty from nothing; the amplifier has a ceiling imposed by the crystal's information-theoretic limits.
- `AppL.R2.d`: `AutonomousPromotionStabilityLaw` — The autonomous promotion loop must reach a stable fixed point: `Result_∞ = f(Result_∞)` where `f` is the promote-and-strengthen operator. The fixed point must be unique and attracting with basin of attraction containing the initial result.

#### Facet 3 - Constructions

- `AppL.R3.a`: `SelfWitnessingHarness` — The harness that instruments a computation to produce its own correctness witness as a side effect, by logging each intermediate state, checking invariants at each step, and packaging the trace as a verifiable witness bundle.
- `AppL.R3.b`: `AdaptivePlanBuilder` — The builder that constructs the proof plan incrementally: executes `Step_1` to generate `Step_2`, executes `Step_2` to generate `Step_3`, and so on, adapting each step to the evidence gathered in the previous step, until the plan is complete or the budget is exhausted.
- `AppL.R3.c`: `EvidenceAmplificationEngine` — The engine that implements recursive evidence amplification: takes initial weak evidence, applies the amplification function `g` at each recursive level, tracks the strength trajectory, and terminates when the ceiling is reached or the target strength is achieved.
- `AppL.R3.d`: `FixedPointPromotionEngine` — The engine that drives the autonomous promotion loop to its fixed point: iterates the promote-and-strengthen cycle, monitors convergence via `|Result_{n+1} - Result_n|`, and declares stable promotion when the difference drops below `ε_stable`.

#### Facet 4 - Certificates

- `AppL.R4.a`: `SelfWitnessCert` — Receipt proving the self-generating witness is sound (biconditional holds), the computation trace is complete, and the witness bundle passes independent verification.
- `AppL.R4.b`: `BootstrapTerminationCert` — Receipt proving the bootstrapped proof plan terminated with a finite plan of length `n < N_max`, each self-generated step is well-formed, and the complete plan covers all candidates.
- `AppL.R4.c`: `AmplificationCeilingCert` — Receipt proving recursive evidence amplification converged below the ceiling `strength_max`, the amplification function `g` was applied correctly at each level, and no unbounded amplification occurred.
- `AppL.R4.d`: `AutonomousPromotionCert` — Receipt proving the autonomous promotion loop reached a stable fixed point, the fixed point is unique and attracting, and the final promoted result is self-consistent with the evidence it generates.
