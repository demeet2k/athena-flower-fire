# InvV - Replay Reversal & Verifier Release

Routing role: Reverses AppM (Replay Kernel and Verifier Capsules). Where AppM constructed replay logs and verifier capsules for deterministic re-execution, InvV reverses replays into summaries, releases verifier capsules back into their seed proofs, and compresses execution histories into fixed-point attestations.

Mirror of: AppM (Replay Kernel and Verifier Capsules)
Arc: V | Rot: 300° → 60° | Lane: Replay→Summary | w: 8D

## StationHeader
```
Arc:  V (Replay Reversal)
Rot:  300° (execution history compression angle)
Lane: Descent-Replay (replay dissolution lane)
w:    8D → seed (execution logs compress to attestations)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvV.S1.a`: `ReplayLogDigest` — The discrete hash-digest of an entire replay log. Every step in the replay (input → operation → output) is hashed sequentially into a running accumulator. The final digest is a fixed-width integer that attests to the entire execution history without storing it. The successor inverts: "summarize the next replay step" rather than "record the next replay step."
- `InvV.S1.b`: `DiffFromCanonical` — The difference between the actual replay trace and the canonical (expected) trace. If the difference is zero, the replay was perfectly canonical. Non-zero differences identify deviations — bugs, environmental variations, or non-determinism. The zero set of this difference is the deterministic core.
- `InvV.S1.c`: `VerifierCapsuleProduct` — The multiplicative composition of all verifier capsules into a single master attestation. Each capsule proves one property; their product proves all properties simultaneously. The master attestation is a single object replacing the entire capsule collection.
- `InvV.S1.d`: `CompressionQuotient` — The ratio of replay log size to digest size = the compression quotient. A quotient of 10^6 means the digest is one millionth the size of the log. The quotient must be finite and bounded for the compression to be meaningful.

#### Facet 2 - Laws

- `InvV.S2.a`: `DigestFidelityLaw` — The digest must be a faithful summary: given the digest and the replay grammar, it must be possible to verify any specific step of the replay without storing the full log. This is a Merkle-like property — any step is verifiable from its path in the digest tree.
- `InvV.S2.b`: `CanonicalDeviationBound` — Deviations from canonical must be bounded and classified. Environmental deviations (timing, memory addresses) are tolerated. Logical deviations (different outputs for same inputs) are bugs. The bound separates tolerable from intolerable.
- `InvV.S2.c`: `CapsuleCompositionLaw` — Verifier capsules compose associatively: the order of composition does not affect the master attestation. This guarantees that capsules from different subsystems can be composed in any order. Non-associative capsules indicate a verification inconsistency.
- `InvV.S2.d`: `BoundedCompressionLaw` — The compression quotient must be bounded above by the replay's information-theoretic entropy. No compression scheme can beat the entropy bound. If the actual quotient exceeds the entropy bound, the digest is lossy (some information was silently dropped).

#### Facet 3 - Constructions

- `InvV.S3.a`: `StreamingDigester` — Processes the replay log one step at a time, updating the running hash. At each step: hash(step_data) is folded into the accumulator. Final output: fixed-width digest. Memory usage: O(1) regardless of log size.
- `InvV.S3.b`: `CanonicalDiffer` — Runs the actual trace and canonical trace in parallel, comparing at each step. Records deviations with their classification (environmental vs. logical). Output: the deviation vector and the deterministic core mask.
- `InvV.S3.c`: `CapsuleFolder` — Takes the set of verifier capsules and composes them associatively into the master attestation. Verifies associativity by checking that different composition orders produce the same result. Output: the master attestation object.
- `InvV.S3.d`: `EntropyEstimator` — Estimates the information-theoretic entropy of the replay log using streaming algorithms (e.g., entropy of the step distribution). Compares against the actual compression quotient. Flags any digest that appears to beat the entropy bound.

#### Facet 4 - Certificates

- `InvV.S4.a`: `DigestFidelityCert` — Receipt proving digest correctly summarizes the full replay, any step is verifiable from its Merkle path, no step was omitted.
- `InvV.S4.b`: `DeviationClassificationCert` — Receipt proving all deviations classified, environmental deviations bounded, no logical deviations detected (or all logical deviations documented).
- `InvV.S4.c`: `CapsuleCompositionCert` — Receipt proving capsule composition is associative, master attestation correctly formed, all individual capsule properties preserved in the composite.
- `InvV.S4.d`: `CompressionBoundCert` — Receipt proving compression quotient within entropy bound, no information silently dropped, digest is faithful within declared tolerance.

### Lens F

#### Facet 1 - Objects

- `InvV.F1.a`: `ExecutionWaveformSummary` — The continuous waveform of execution (state evolving over time) is summarized by its envelope: amplitude (peak state deviation), frequency (oscillation rate), and phase (timing offset). The envelope replaces the full waveform — compression through spectral summary.
- `InvV.F1.b`: `VerificationDampingCurve` — As more verification capsules are composed, the uncertainty about correctness dampens exponentially. Each capsule reduces remaining doubt by a factor. The damping curve shows how confidence grows as capsules accumulate — and in reversal, how quickly it can be released.
- `InvV.F1.c`: `ReplayHarmonicDecomposition` — The replay trace decomposed into harmonic components: fundamental (the main computation), first overtone (error correction), second overtone (environmental adaptation), higher overtones (noise). Compression discards noise overtones and retains signal harmonics.
- `InvV.F1.d`: `ConvergenceToAttestation` — The replay's output sequence converges to a fixed-point attestation. The convergence rate measures how quickly the replay stabilizes. Fast convergence = the replay quickly reaches its conclusion. Slow convergence = the replay has long transient behavior that compresses poorly.

#### Facet 2 - Laws

- `InvV.F2.a`: `SpectralSufficiencyLaw` — The envelope (amplitude, frequency, phase) must be sufficient to reconstruct the waveform within declared tolerance. If not sufficient, additional spectral components must be retained until sufficiency is achieved.
- `InvV.F2.b`: `MonotonicConfidenceLaw` — Confidence must monotonically increase as capsules are composed. Any capsule that decreases confidence indicates a verification inconsistency and must be quarantined.
- `InvV.F2.c`: `SignalPreservationLaw` — Harmonic compression must preserve all signal components (fundamental + overtones up to the declared cutoff). Only noise above the cutoff may be discarded. The cutoff must be declared explicitly.
- `InvV.F2.d`: `ConvergenceRateBoundLaw` — The convergence rate must be at least geometric (ratio ≤ 1/φ per step). Sub-geometric convergence indicates a replay that is too long or too complex for efficient compression.

#### Facet 3 - Constructions

- `InvV.F3.a`: `EnvelopeExtractor` — Computes the execution waveform envelope by tracking amplitude, frequency, and phase over time. Uses Hilbert transform for instantaneous amplitude and frequency. Output: the three-component envelope summary.
- `InvV.F3.b`: `ConfidenceTracker` — Tracks confidence level as each capsule is composed. Plots the damping curve. Flags any non-monotone step. Reports final confidence level and the number of capsules needed to reach the target.
- `InvV.F3.c`: `HarmonicFilter` — Decomposes the replay trace via FFT (or wavelet transform). Identifies fundamental and overtone components. Applies the declared cutoff. Output: the signal-only trace (noise removed) and the noise floor estimate.
- `InvV.F3.d`: `ConvergenceDetector` — Monitors the output sequence for convergence. Computes the convergence ratio at each step. Declares convergence when the ratio stabilizes below 1/φ. Output: the fixed-point attestation and the convergence step count.

#### Facet 4 - Certificates

- `InvV.F4.a`: `EnvelopeSufficiencyCert` — Receipt proving envelope is spectrally sufficient, waveform reconstructable within tolerance, no essential component omitted.
- `InvV.F4.b`: `MonotoneConfidenceCert` — Receipt proving confidence was monotonically increasing, no inconsistent capsules, target confidence reached.
- `InvV.F4.c`: `SignalNoiseSeparationCert` — Receipt proving cutoff correctly applied, all signal preserved, noise correctly identified and discarded.
- `InvV.F4.d`: `ConvergenceCert` — Receipt proving output sequence converged, fixed-point attestation correctly computed, convergence rate within bound.

### Lens C

#### Facet 1 - Objects

- `InvV.C1.a`: `ReplaySamplingVerifier` — Instead of replaying every step, sample k steps randomly and verify those. If all k pass, the replay is statistically certified with confidence 1 - (1-p)^k where p is the per-step failure probability. This is the Cloud view: probabilistic replay verification.
- `InvV.C1.b`: `CapsuleRedundancyExclusion` — Multiple capsules may verify overlapping properties. Inclusion-exclusion identifies the non-redundant core: the minimal set of capsules that covers all properties. Redundant capsules are released — they add no new verification.
- `InvV.C1.c`: `IndependentVerificationProduct` — If verification properties are independent, the joint verification probability = Π P(property_i verified). Independent properties can be released independently without affecting the others.
- `InvV.C1.d`: `VerificationCostNormalization` — The cost of maintaining each verifier capsule is normalized by the value of what it verifies. High-value/low-cost capsules are retained longest. Low-value/high-cost capsules are released first. The normalized ratio governs the release order.

#### Facet 2 - Laws

- `InvV.C2.a`: `SamplingConfidenceLaw` — The sample size k must be sufficient to achieve the declared confidence level. The relationship: k ≥ ln(1-confidence) / ln(1-p). Under-sampling is a certification violation.
- `InvV.C2.b`: `MinimalCoverageLaw` — The non-redundant capsule core must cover all declared verification properties. Releasing a capsule that breaks coverage is illegal. Coverage is checked before each release.
- `InvV.C2.c`: `IndependenceBeforeReleaseLaw` — Independent release is only legal after independence is verified. If properties are dependent, their capsules must be released together or not at all.
- `InvV.C2.d`: `OptimalReleaseOrderLaw` — Capsules must be released in order of ascending value/cost ratio. Releasing a high-value capsule before a low-value one wastes verification resources.

#### Facet 3 - Constructions

- `InvV.C3.a`: `ReplaySampler` — Selects k random replay steps, re-executes each, compares output against the replay log. Reports pass/fail count and computed confidence level. If any fail, falls back to full replay verification.
- `InvV.C3.b`: `CoverageMinimizer` — Computes the minimal capsule set covering all properties using set-cover algorithms. Identifies redundant capsules. Reports the non-redundant core and the list of releasable redundancies.
- `InvV.C3.c`: `IndependenceVerifier` — Tests pairwise independence of verification properties by checking for logical dependencies (if property A implies property B, they are not independent). Reports the dependency graph.
- `InvV.C3.d`: `ReleaseScheduler` — Computes the value/cost ratio for each capsule. Sorts in ascending order. Generates the release schedule. Verifies coverage is maintained after each release. Output: the optimal release sequence.

#### Facet 4 - Certificates

- `InvV.C4.a`: `SamplingVerificationCert` — Receipt proving sample size sufficient, all sampled steps passed, confidence level achieved, no fallback needed (or fallback completed).
- `InvV.C4.b`: `MinimalCoverageCert` — Receipt proving non-redundant core covers all properties, redundant capsules identified, coverage maintained after releases.
- `InvV.C4.c`: `PropertyIndependenceCert` — Receipt proving independence verified (or dependencies documented), release strategy consistent with dependency graph.
- `InvV.C4.d`: `OptimalReleaseCert` — Receipt proving capsules released in optimal order, no high-value capsule released prematurely, coverage maintained throughout.

### Lens R

#### Facet 1 - Objects

- `InvV.R1.a`: `RecursiveReplaySummary` — A replay that calls sub-replays (nested execution) is summarized recursively: summarize each sub-replay, then summarize the top-level replay using the sub-summaries. The recursion terminates at atomic operations that need no replay (they are their own summary).
- `InvV.R1.b`: `VerifierContractionChain` — Each level of replay nesting contracts the verification burden by factor 1/φ: a top-level replay with N steps has ~N/φ sub-replay steps, each of which has ~N/φ² sub-sub-replay steps. The geometric contraction means total verification effort converges.
- `InvV.R1.c`: `CapsuleTreePruning` — The verifier capsule hierarchy forms a tree (root attestation → sub-attestations → leaf verifications). Pruning from leaves to root: each leaf verification is released after its parent absorbs its certificate. The tree compresses to its root attestation.
- `InvV.R1.d`: `ScaleInvariantVerification` — The verification protocol is identical at every recursion level: digest the log, diff from canonical, compose capsules, compute compression quotient. Only the content changes; the protocol is a fixed point.

#### Facet 2 - Laws

- `InvV.R2.a`: `BottomUpSummaryLaw` — Sub-replays must be summarized before their parents. A parent summary that references un-summarized children is invalid. Bottom-up order is mandatory.
- `InvV.R2.b`: `GeometricContractionLaw` — Each nesting level must reduce verification burden by at least factor 1/φ. If a sub-replay is as complex as its parent, the nesting structure is degenerate and must be refactored.
- `InvV.R2.c`: `LeafFirstPruningLaw` — Capsule tree pruning must proceed leaf-first. No parent capsule is released until all its children have been absorbed. This ensures the root attestation correctly reflects all leaf verifications.
- `InvV.R2.d`: `ProtocolFixedPointLaw` — The verification protocol must be identical at every recursion level. Level-specific protocols indicate structural inconsistency.

#### Facet 3 - Constructions

- `InvV.R3.a`: `RecursiveSummarizer` — Traverses the replay tree bottom-up. At each leaf: computes the atomic digest. At each node: combines child digests into the node's summary. Reports tree depth, total nodes, and any leaves that required special handling.
- `InvV.R3.b`: `ContractionVerifier` — At each recursion level, measures the verification burden (steps × complexity). Computes the ratio between adjacent levels. Verifies ratio ≤ 1/φ. Flags degenerate nesting.
- `InvV.R3.c`: `CapsuleTreeCompressor` — Traverses the capsule tree leaf-first. At each leaf: extracts the verification certificate. At each parent: absorbs child certificates and releases child capsules. Output: the root attestation with all leaves absorbed.
- `InvV.R3.d`: `ProtocolConsistencyChecker` — Runs the verification protocol at each recursion level and compares operation sequences. Reports any level-specific deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvV.R4.a`: `RecursiveSummaryCert` — Receipt proving all sub-replays summarized before parents, tree traversal was bottom-up, root summary correctly reflects all leaves.
- `InvV.R4.b`: `ContractionCert` — Receipt proving geometric contraction at every level, no degenerate nesting, total verification effort convergent.
- `InvV.R4.c`: `TreeCompressionCert` — Receipt proving capsule tree pruned leaf-first, all leaf certificates absorbed into root, root attestation is complete and faithful.
- `InvV.R4.d`: `FixedPointProtocolCert` — Receipt proving protocol identical at all levels, no level-specific deviations, verification is scale-invariant.
