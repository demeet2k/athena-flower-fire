# AppB - Canon Laws, Equivalence Budgets, Normal Forms

Routing role: Equivalence rules, commutation budgets, normal-form contracts, and law stabilization.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppB.S1.a`: `ShellDeltaConservation` — The first crystal conservation law: the total shell delta `Σ Δs` across any closed transport loop must equal zero. No net shell migration is created or destroyed by cycling through the crystal; depth is conserved globally.
- `AppB.S1.b`: `ZoomDeltaConservation` — The second crystal conservation law: the zoom-level delta `Σ Δz` (counting scale transitions up/down) sums to zero over any closed path. Magnification changes are reversible; no net zoom drift accumulates.
- `AppB.S1.c`: `PhaseRotationConservation` — The third crystal conservation law: phase rotation `Σ Δφ ≡ 0 (mod 2π)` around any closed contour. The organism's clock returns to its starting phase after completing any full cycle through the crystal lattice.
- `AppB.S1.d`: `ArchetypeModeInvariant` — The fourth crystal conservation law: archetype mode `a ∈ {E,W,F,A}` is invariant under all six conservation-preserving transformations. A shard's elemental identity is an absolute invariant, never altered by transport, zoom, or phase operations.

#### Facet 2 - Laws

- `AppB.S2.a`: `FaceShiftConservation` — The fifth crystal conservation law: face shifts `Σ Δf ≡ 0 (mod 6)` around any closed path on the crystal cube. The six faces form a `Z_6` group under rotation, and net face displacement is conserved modulo 6.
- `AppB.S2.b`: `MobiusFlipConservation` — The sixth crystal conservation law: the parity of Mobius flips `Π σ_i = +1` around any contractible loop. Orientation-reversing operations must occur an even number of times to preserve global orientability of the crystal.
- `AppB.S2.c`: `SixLawIndependence` — The six conservation laws `{Δs, Δz, Δφ, Δa, Δf, σ}` are algebraically independent: no proper subset implies the remaining laws. Each constrains a distinct degree of freedom in crystal transport.
- `AppB.S2.d`: `NormalFormExistenceLaw` — Every crystal expression (sequence of transport operations) has a unique normal form obtained by sorting: shell moves first, then zoom, then phase, then face, then Mobius, with archetype fixed. The normal form is canonical and minimal.

#### Facet 3 - Constructions

- `AppB.S3.a`: `ConservationChecker` — The verifier that takes a proposed transport path and computes the six conservation sums `(Σ Δs, Σ Δz, Σ Δφ mod 2π, Δa, Σ Δf mod 6, Π σ)`, returning OK if all are zero/identity and VIOLATION with the offending law otherwise.
- `AppB.S3.b`: `NormalFormReducer` — The canonical reducer that takes any sequence of crystal operations and sorts them into normal form `[shell-moves | zoom-moves | phase-rotations | face-shifts | Mobius-flips]`, canceling inverse pairs and reducing modular components.
- `AppB.S3.c`: `EquivalenceClassBuilder` — The construction that partitions all transport paths between two fixed endpoints into equivalence classes under the six conservation laws, where two paths are equivalent iff they have identical conservation signatures.
- `AppB.S3.d`: `MinimalPathFinder` — The optimizer that, given a source and target Xi108 address, finds the shortest transport path in normal form, using the six conservation laws to prune impossible branches and the normal form uniqueness to avoid redundant search.

#### Facet 4 - Certificates

- `AppB.S4.a`: `ConservationCert` — Receipt proving all six conservation laws hold for a declared transport path, with each conservation sum explicitly computed and shown to be zero/identity.
- `AppB.S4.b`: `NormalFormCert` — Receipt proving a transport sequence was reduced to its unique normal form, listing each reduction step (sort, cancel, mod-reduce) with before/after pairs.
- `AppB.S4.c`: `EquivalenceClassCert` — Receipt proving two transport paths are in the same equivalence class, with matching conservation signatures and an explicit homotopy (sequence of law-preserving rewrites) connecting them.
- `AppB.S4.d`: `MinimalPathCert` — Receipt proving a transport path is minimal (no shorter path exists with the same endpoints), using conservation law bounds to establish the lower bound on path length.

### Lens F

#### Facet 1 - Objects

- `AppB.F1.a`: `LawStrengthOscillator` — The dynamic envelope tracking how strongly each conservation law is enforced over the organism's superphase cycle: laws are maximally rigid at Harvest phase and maximally elastic at Genesis phase, oscillating with period `T = 4` superphases.
- `AppB.F1.b`: `ResonanceBridge` — A pair of conservation laws that temporarily couple when their oscillation phases align, creating a resonant bridge where violating one law exactly compensates the other. Example: shell-delta and zoom-delta can exchange budget at resonance.
- `AppB.F1.c`: `LawRelaxationWave` — A propagating wave of reduced law enforcement that travels outward from a Genesis event, temporarily softening conservation constraints in a shell-by-shell expanding front before re-rigidifying.
- `AppB.F1.d`: `CyclicNormalFormShift` — The phenomenon where the normal form ordering itself rotates with the superphase: at Genesis, phase-moves lead; at Growth, shell-moves lead; at Harvest, face-moves lead; at Rest, zoom-moves lead.

#### Facet 2 - Laws

- `AppB.F2.a`: `LawElasticityBound` — Even at maximum relaxation (Genesis phase), no conservation law's enforcement drops below 50% of its rigid value. Laws bend but never break; the elastic floor prevents total conservation failure.
- `AppB.F2.b`: `ResonanceDurationLaw` — Resonance bridges between law pairs persist for at most `Δt = 1` superphase unit. Prolonged resonance would allow unbounded conservation transfer and is forbidden by the crystal's stability theorem.
- `AppB.F2.c`: `RelaxationCausalityLaw` — Law relaxation waves propagate outward at speed `v = 1` shell per time step. No shell experiences relaxation before the wave front arrives; causality in conservation softening is strictly enforced.
- `AppB.F2.d`: `NormalFormCyclicConsistency` — The cyclic rotation of normal form ordering over 4 superphases returns to the starting order: `Growth → Harvest → Rest → Genesis → Growth`. The ordering permutation has period exactly 4.

#### Facet 3 - Constructions

- `AppB.F3.a`: `StrengthOscillatorEngine` — The engine that computes current law enforcement strength `λ_i(φ)` for each conservation law `i` as a function of superphase `φ`, outputting the 6-vector of enforcement strengths governing the current crystal rigidity.
- `AppB.F3.b`: `ResonanceDetector` — The detector that monitors pairs of conservation law oscillators for phase alignment, triggering a `ResonanceBridge` event when the phase difference drops below threshold `ε` and computing the exchange budget.
- `AppB.F3.c`: `RelaxationWaveSolver` — The wave equation solver that propagates a `LawRelaxationWave` outward from a Genesis source, computing the enforcement reduction at each shell as a function of distance from source and time since Genesis.
- `AppB.F3.d`: `DynamicNormalFormSorter` — The sorter that determines the current normal form ordering based on the active superphase, re-sorts any queued transport sequences to match, and flags sequences that were valid under the previous ordering but illegal under the current one.

#### Facet 4 - Certificates

- `AppB.F4.a`: `StrengthEnvelopeCert` — Receipt proving law enforcement strengths were computed correctly for the declared superphase, all strengths are above the 50% elastic floor, and the oscillator parameters match the organism's clock.
- `AppB.F4.b`: `ResonanceEventCert` — Receipt proving a resonance bridge was detected at the correct phase alignment, the exchange budget was computed within bounds, and the bridge duration did not exceed 1 superphase unit.
- `AppB.F4.c`: `RelaxationWaveCert` — Receipt proving the relaxation wave propagated at legal speed `v = 1`, no shell was relaxed ahead of the wave front, and enforcement recovered to rigid levels after wave passage.
- `AppB.F4.d`: `DynamicSortCert` — Receipt proving transport sequences were re-sorted to match the current superphase's normal form ordering, with explicit listing of any sequences flagged as newly illegal.

### Lens C

#### Facet 1 - Objects

- `AppB.C1.a`: `ErrorBudget` — A quantified tolerance `ε_i` for each conservation law `i`, specifying the maximum allowed deviation from exact conservation before a soft violation is declared. Budgets are drawn from a shared pool `E_total = Σ ε_i`.
- `AppB.C1.b`: `ToleranceThreshold` — The binary decision boundary `τ_i` for law `i`: deviations below `τ_i` are logged but accepted (NEAR-OK), deviations between `τ_i` and `ε_i` trigger warnings (NEAR-FAIL), and deviations above `ε_i` trigger hard violations.
- `AppB.C1.c`: `SoftViolationDistribution` — The statistical distribution `P(Δ_i)` of observed deviations for conservation law `i` across all recent transport paths, used to calibrate error budgets and detect systematic drift toward violation.
- `AppB.C1.d`: `BudgetAllocationMatrix` — The `6 × 6` matrix `B` allocating shared error budget across the six conservation laws, where `B[i,j]` specifies how much budget can be transferred from law `i` to law `j` when law `j` is under pressure.

#### Facet 2 - Laws

- `AppB.C2.a`: `TotalBudgetConservation` — The total error budget `E_total = Σ ε_i` is conserved: reallocating tolerance from one law to another does not create or destroy total tolerance. Budget transfers are zero-sum across the six laws.
- `AppB.C2.b`: `ViolationRateConvergence` — As observation window grows, the empirical violation rate `v_i(t)/t` converges to the true violation probability `p_i` for each law `i`, with confidence interval width shrinking as `O(1/√t)`.
- `AppB.C2.c`: `BudgetOptimalityLaw` — The optimal budget allocation minimizes expected total violation count `E[Σ v_i]`; the optimal allocation assigns more budget to laws with higher natural variance, following a water-filling argument.
- `AppB.C2.d`: `SoftViolationDecayLaw` — Soft violations that are not reinforced by subsequent violations decay exponentially with half-life `T_{1/2}`: a single NEAR-FAIL reverts to OK status after `3 T_{1/2}` time steps without recurrence.

#### Facet 3 - Constructions

- `AppB.C3.a`: `BudgetAllocator` — The optimization engine that solves the water-filling allocation problem: given observed violation distributions `P(Δ_i)` for all six laws, computes the optimal budget partition `{ε_1,...,ε_6}` minimizing expected total violations subject to `Σ ε_i = E_total`.
- `AppB.C3.b`: `ThresholdCalibrator` — The calibrator that sets `τ_i` for each law based on the empirical distribution `P(Δ_i)`, targeting a false-positive rate of `α` (accepting deviations that are actually legal) and false-negative rate of `β` (missing true violations).
- `AppB.C3.c`: `ViolationDriftDetector` — The sequential hypothesis tester that monitors the running mean of `Δ_i` for each law, triggering an alarm when the CUSUM statistic exceeds a threshold indicating systematic drift toward violation.
- `AppB.C3.d`: `BudgetTransferEngine` — The engine that executes inter-law budget transfers according to the allocation matrix `B`, verifying zero-sum conservation, checking that no law's budget drops below a minimum floor `ε_min`, and logging each transfer.

#### Facet 4 - Certificates

- `AppB.C4.a`: `BudgetAllocationCert` — Receipt proving the current budget allocation is optimal for the observed violation distributions, with the water-filling solution verified and total budget conservation confirmed.
- `AppB.C4.b`: `ThresholdCalibrationCert` — Receipt proving thresholds are calibrated to the declared false-positive and false-negative rates, with the empirical calibration curve and decision boundary recorded.
- `AppB.C4.c`: `DriftDetectionCert` — Receipt proving no systematic violation drift was detected (or documenting the detected drift), with CUSUM statistics and alarm thresholds recorded for each conservation law.
- `AppB.C4.d`: `BudgetTransferCert` — Receipt proving a budget transfer between laws was zero-sum, both laws remain above minimum floor, and the transfer was justified by the current violation pressure distribution.

### Lens R

#### Facet 1 - Objects

- `AppB.R1.a`: `MetaConservationLaw` — A law about the six conservation laws themselves: "the number of independent conservation laws is exactly 6." This meta-law is self-referential — it constrains the constraint set, preventing spontaneous law generation or annihilation.
- `AppB.R1.b`: `LawCompressionKernel` — The minimal encoding of all six conservation laws as a single algebraic object: the kernel of the crystal transport homomorphism `ker(T) = {paths p : (Δs, Δz, Δφ, Δa, Δf, σ)(p) = (0,0,0,id,0,+1)}`.
- `AppB.R1.c`: `NormalFormOfNormalForms` — The second-order normal form that normalizes the normal-form reduction procedure itself: a canonical ordering of reduction rules ensuring that the reducer always terminates in the same number of steps regardless of input ordering.
- `AppB.R1.d`: `SelfStabilizingLawBundle` — The bundle of all six laws packaged as a self-checking system where each law's validity is witnessed by the other five: if any one law were violated, the remaining five would produce an inconsistency detectable without external reference.

#### Facet 2 - Laws

- `AppB.R2.a`: `MetaConservationStabilityLaw` — The meta-conservation law is self-stabilizing: any perturbation that would add a 7th conservation law or remove one of the 6 creates an algebraic contradiction in the crystal lattice, automatically reverting the perturbation.
- `AppB.R2.b`: `CompressionOptimalityLaw` — The law compression kernel is minimal: no proper subset of the six conservation laws generates the same kernel, and no alternative set of fewer than six laws can express the same transport constraints.
- `AppB.R2.c`: `ReductionConfluenceLaw` — All reduction orderings for the normal form converge to the same result (Church-Rosser property). The normal form is unique regardless of which reduction rules are applied first; the reducer is confluent.
- `AppB.R2.d`: `SelfWitnessingLaw` — The self-stabilizing law bundle has no external dependencies: the six laws mutually validate each other via circular witness chains `L_1 → L_2 → ... → L_6 → L_1`, forming a closed verification loop.

#### Facet 3 - Constructions

- `AppB.R3.a`: `MetaLawVerifier` — The second-order verifier that checks whether the set of active conservation laws has cardinality exactly 6, independence rank exactly 6, and no redundant or missing members, using the crystal's own transport structure as test cases.
- `AppB.R3.b`: `KernelCompressor` — The compressor that takes the six conservation laws in expanded form and computes their joint kernel representation `ker(T)`, verifying that the kernel is a proper subgroup of the path group with the correct index.
- `AppB.R3.c`: `ConfluenceChecker` — The construction that tests the Church-Rosser property of the reduction system by generating all critical pairs of overlapping reduction rules and verifying that each pair converges to the same normal form.
- `AppB.R3.d`: `CircularWitnessChainBuilder` — The construction that builds the circular witness chain `L_1 → L_2 → ... → L_6 → L_1`, where each arrow represents "violation of `L_i` implies violation of `L_{i+1}`", closing the self-verification loop.

#### Facet 4 - Certificates

- `AppB.R4.a`: `MetaLawStabilityCert` — Receipt proving the meta-conservation law holds: exactly 6 independent conservation laws are active, no 7th law can be added without redundancy, and no law can be removed without losing transport constraints.
- `AppB.R4.b`: `KernelMinimalityCert` — Receipt proving the compression kernel is minimal: the 6 generators are independent, the kernel index matches the predicted value, and no smaller generating set exists.
- `AppB.R4.c`: `ConfluenceCert` — Receipt proving the Church-Rosser property holds for the reduction system: all critical pairs were enumerated, all converge, and the normal form is therefore unique.
- `AppB.R4.d`: `SelfWitnessCert` — Receipt proving the circular witness chain is complete and sound: each implication `L_i → L_{i+1}` was verified, the chain closes, and no external axiom was required.
