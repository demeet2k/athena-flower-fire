# AppM - Replay Kernel and Verifier Capsules

Routing role: Replay capsules, deterministic verification, proof-carrying artifacts, and rerun contracts.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppM.S1.a`: `ReplayLog` — An append-only, content-addressed sequence of `(tick, action, state-hash)` triples that records every discrete transition of a computation, enabling bit-exact rerun from any checkpoint.
- `AppM.S1.b`: `DeterministicSnapshot` — A frozen image of full computation state at tick `t`, including register file, heap digest, and RNG seed, such that resuming from the snapshot reproduces the identical successor trace.
- `AppM.S1.c`: `CheckpointLattice` — A partially-ordered set of snapshots where `snap_i ≤ snap_j` iff `j` is reachable from `i` by replaying the intervening log segment; supports branching and merge for forked replays.
- `AppM.S1.d`: `ReplayIndex` — A B-tree over `(shard-id, tick-range)` pairs that maps any crystal address to the log segment and snapshot needed to reconstruct it, enabling O(log n) random-access replay.

#### Facet 2 - Laws

- `AppM.S2.a`: `BitExactReplayLaw` — Replaying log segment `L[i..j]` from snapshot `S_i` must produce snapshot `S_j` with identical state-hash; any divergence constitutes a verification failure and triggers quarantine.
- `AppM.S2.b`: `SnapshotImmutabilityLaw` — Once a snapshot is sealed with its content-address hash, no field may be mutated; any write produces a new snapshot with a new hash, preserving the checkpoint lattice's append-only invariant.
- `AppM.S2.c`: `CheckpointCompleteness` — For every pair of adjacent snapshots `(S_i, S_{i+1})` in the lattice, the connecting log segment `L[i..i+1]` must exist and be sufficient to reconstruct `S_{i+1}` from `S_i` without external input.
- `AppM.S2.d`: `ReplayIndexConsistency` — The replay index must be a total function over the shard address space: every live shard has exactly one canonical log segment and at least one ancestor snapshot from which it can be replayed.

#### Facet 3 - Constructions

- `AppM.S3.a`: `IncrementalCheckpointer` — A construction that emits a new snapshot every `k` ticks by diffing the current state against the previous snapshot, storing only the delta and a full hash, yielding O(delta) storage per checkpoint.
- `AppM.S3.b`: `LogCompactor` — Merges consecutive log segments `L[i..j]` and `L[j..k]` into a single `L[i..k]` while garbage-collecting intermediate snapshots that are no longer needed for any active replay cursor.
- `AppM.S3.c`: `ForkReplayEngine` — Given a checkpoint lattice with branch point `S_b`, constructs two independent replay streams that diverge from `S_b`, each maintaining its own log and snapshot chain for counterfactual exploration.
- `AppM.S3.d`: `ReplayIndexBuilder` — Scans all existing log segments and snapshots, constructs the B-tree index, and validates that every shard address resolves to a replayable path; emits orphan reports for unreachable segments.

#### Facet 4 - Certificates

- `AppM.S4.a`: `ReplayFidelityCert` — Proves that replaying `L[i..j]` from `S_i` yields `S_j` by exhibiting both hashes and the deterministic transition function; verifiable in O(j-i) steps.
- `AppM.S4.b`: `SnapshotIntegrityCert` — Proves that a snapshot's content-address hash matches its actual contents via Merkle witness over the state tree; a single bit flip invalidates the certificate.
- `AppM.S4.c`: `LatticeConnectivityCert` — Proves that the checkpoint lattice is connected: for any two snapshots `S_a` and `S_b`, there exists a directed path of log segments linking them through a common ancestor.
- `AppM.S4.d`: `IndexCoverageCert` — Proves that the replay index is total by exhibiting, for every shard in the live address set, the `(log-segment, snapshot)` pair that covers it; gaps trigger re-indexing.

### Lens F

#### Facet 1 - Objects

- `AppM.F1.a`: `TemporalReplayStream` — A time-ordered stream of state transitions that reconstructs the computation's evolution; supports forward play, pause, and seek-to-tick for temporal navigation.
- `AppM.F1.b`: `CausalReplayGraph` — A DAG where nodes are state transitions and edges are causal dependencies; replaying respects topological order so that every effect follows its cause even under concurrent execution.
- `AppM.F1.c`: `RewindCursor` — A bidirectional replay head that can move forward by applying log entries or backward by restoring prior snapshots, enabling temporal debugging and "what-if" exploration.
- `AppM.F1.d`: `ReplayClockSynchronizer` — A logical clock that aligns multiple replay streams to a common tick reference, ensuring that distributed replays reconstruct the same global ordering of events.

#### Facet 2 - Laws

- `AppM.F2.a`: `CausalOrderPreservation` — Replay must respect the causal partial order: if transition `A` causally precedes `B` in the original execution, `A` must precede `B` in every valid replay.
- `AppM.F2.b`: `TemporalReversibilityLaw` — For every forward replay step `S_i → S_{i+1}`, a reverse step exists via snapshot restoration; the system is temporally navigable in both directions at checkpoint granularity.
- `AppM.F2.c`: `ReplayConvergenceLaw` — Two replay streams starting from the same snapshot and applying the same log segment must converge to identical final states; divergence is proof of non-determinism contamination.
- `AppM.F2.d`: `ClockMonotonicityLaw` — The replay clock is strictly monotonic: `tick(S_{i+1}) > tick(S_i)` for every forward transition; no replay may produce a state with a tick value less than or equal to its predecessor.

#### Facet 3 - Constructions

- `AppM.F3.a`: `StreamingReplayPipeline` — Constructs a pipeline that reads log segments from storage, applies them to the current snapshot in tick order, and emits a live state stream for real-time observation of the replayed computation.
- `AppM.F3.b`: `CausalReplayScheduler` — Given a causal replay graph, produces a valid topological execution schedule that maximizes parallelism while preserving all causal dependencies.
- `AppM.F3.c`: `TemporalBisectionSearch` — Locates the first tick at which a property `P` becomes true by binary-searching over the checkpoint lattice, replaying only the log segments around candidate ticks; runs in O(log T) replays.
- `AppM.F3.d`: `MultiStreamAligner` — Merges `k` replay streams from different SFCR elements into a single interleaved global trace by aligning on the synchronized logical clock, producing a unified temporal view.

#### Facet 4 - Certificates

- `AppM.F4.a`: `CausalChainCert` — Proves that a replay trace respects causal order by exhibiting the topological sort and showing that every dependency edge points forward in the trace.
- `AppM.F4.b`: `RewindCorrectnessCert` — Proves that rewinding from `S_j` to `S_i` via snapshot restoration yields the identical state that was originally recorded at `S_i`; hash comparison is the witness.
- `AppM.F4.c`: `ConvergenceWitnessCert` — Proves two independent replays converge by exhibiting their terminal state hashes and showing equality; used to validate replay determinism across distributed nodes.
- `AppM.F4.d`: `ClockAlignmentCert` — Proves that `k` synchronized replay streams agree on the global tick ordering by exhibiting the merged timeline and verifying no causal inversion exists.

### Lens C

#### Facet 1 - Objects

- `AppM.C1.a`: `ReplaySamplingOracle` — A probabilistic verifier that checks replay correctness by sampling `m` random ticks, replaying short windows around each, and comparing against recorded hashes; catches corruption with probability `1 - (1-p)^m`.
- `AppM.C1.b`: `StatisticalDivergenceDetector` — Computes the KL-divergence between the distribution of state hashes in a replay and the distribution in the original execution; significant divergence signals non-determinism or corruption.
- `AppM.C1.c`: `ProbabilisticCheckpointSelector` — Selects which ticks to checkpoint using a probability distribution weighted by state entropy and transition complexity, optimizing the tradeoff between storage cost and replay granularity.
- `AppM.C1.d`: `ReplayConfidenceEstimator` — Computes a confidence interval `[1 - epsilon, 1]` for replay correctness based on the fraction of sampled ticks that pass verification, using Hoeffding bounds.

#### Facet 2 - Laws

- `AppM.C2.a`: `SamplingCoverageLaw` — If `m` ticks are sampled uniformly from a trace of length `T`, the probability of missing a corruption event of width `w` is at most `((T-w)/T)^m`; coverage is tunable by adjusting `m`.
- `AppM.C2.b`: `DivergenceBoundLaw` — If the statistical divergence between replay and original exceeds threshold `epsilon`, the replay is rejected; the threshold is calibrated so that false-positive rate is below `alpha`.
- `AppM.C2.c`: `CheckpointEntropyLaw` — Ticks with higher state entropy receive higher checkpoint probability; this ensures that complex, high-information states are preferentially preserved for replay verification.
- `AppM.C2.d`: `ConfidenceMonotonicityLaw` — As more sampled ticks pass verification, the confidence bound tightens monotonically; confidence can never decrease with additional passing samples.

#### Facet 3 - Constructions

- `AppM.C3.a`: `AdaptiveSamplingVerifier` — Begins with a coarse random sample of ticks, then refines by oversampling regions where state entropy is highest or where adjacent samples showed hash instability.
- `AppM.C3.b`: `DistributedReplayAudit` — Distributes replay verification across `k` independent nodes, each sampling different tick subsets; results are aggregated via majority vote to produce a consensus verification verdict.
- `AppM.C3.c`: `EntropyWeightedCheckpointer` — Measures state entropy at each tick in a sliding window and emits checkpoints when entropy exceeds a dynamic threshold, producing denser checkpoints in complex computation phases.
- `AppM.C3.d`: `SequentialConfidenceAccumulator` — Runs sampled verifications one at a time, updating a Bayesian posterior on replay correctness after each; halts early when confidence exceeds `1 - delta` or corruption is confirmed.

#### Facet 4 - Certificates

- `AppM.C4.a`: `SamplingVerificationCert` — Exhibits the `m` sampled tick indices, their replayed hashes, and the matching original hashes, plus the Hoeffding bound proving that `P(correct) >= 1 - epsilon`.
- `AppM.C4.b`: `DivergenceBelowThresholdCert` — Exhibits the computed KL-divergence value, the threshold `epsilon`, and the calibration parameters; certifies that replay divergence is within acceptable bounds.
- `AppM.C4.c`: `CheckpointOptimalityCert` — Proves that the selected checkpoint set minimizes expected replay cost under the given entropy distribution, by exhibiting the optimization objective and the achieved value.
- `AppM.C4.d`: `ConsensusVerificationCert` — Proves that `k` independent verifier nodes agreed on replay correctness by exhibiting each node's sample set, results, and the majority tally.

### Lens R

#### Facet 1 - Objects

- `AppM.R1.a`: `SelfReplayingComputation` — A computation that embeds its own replay log and checkpoint kernel within its output, so that any recipient can re-execute the entire derivation without external infrastructure.
- `AppM.R1.b`: `ProofCarryingArtifact` — A shard that carries not only its content but also the verification certificate and minimal replay kernel needed to independently confirm that the content was correctly derived.
- `AppM.R1.c`: `ReplayKernelSeed` — A minimal self-contained binary that, given a log segment, can reconstruct the transition function and execute the replay; the seed is small enough to embed in any shard header.
- `AppM.R1.d`: `AutoVerifierCapsule` — A sealed capsule containing content, replay log, verification samples, and the verifier code itself; opening the capsule automatically runs verification before exposing the content.

#### Facet 2 - Laws

- `AppM.R2.a`: `SelfContainmentLaw` — A self-replaying computation must carry everything needed for replay: transition function, log, initial snapshot, and RNG seed; no external dependency is permitted.
- `AppM.R2.b`: `ProofSufficiencyLaw` — A proof-carrying artifact's certificate must be independently verifiable using only the data embedded in the artifact itself; the verifier needs no network access or external state.
- `AppM.R2.c`: `KernelMinimalityLaw` — The replay kernel seed must be the smallest program that can execute the replay; any strictly smaller program that also replays correctly must be the same program up to isomorphism.
- `AppM.R2.d`: `CapsuleTamperEvidenceLaw` — Any modification to an auto-verifier capsule's content, log, or certificate causes the embedded verifier to reject; the capsule is tamper-evident by construction.

#### Facet 3 - Constructions

- `AppM.R3.a`: `SelfReplayEmbedder` — Takes a computation trace and folds it into the output artifact by appending the replay log, checkpoint, and minimal kernel as structured metadata; the result is self-replaying.
- `AppM.R3.b`: `CertificateWeaver` — Interleaves verification certificates into the replay log at every checkpoint boundary, so that partial replays can verify incrementally without replaying the entire trace.
- `AppM.R3.c`: `KernelDistiller` — Extracts the minimal replay kernel from a full runtime by dead-code elimination and constant folding, producing the smallest self-contained replayer for a given computation class.
- `AppM.R3.d`: `CapsuleSealer` — Assembles content, log, certificates, and verifier code into a sealed capsule; computes the capsule's root hash; and embeds the hash in the capsule header for tamper detection.

#### Facet 4 - Certificates

- `AppM.R4.a`: `SelfReplayRoundTripCert` — Proves that extracting the embedded replay kernel and log from a self-replaying artifact and executing the replay reproduces the artifact's content exactly.
- `AppM.R4.b`: `ProofIndependenceCert` — Proves that the embedded certificate can be verified using only the artifact's own data by exhibiting the verification execution trace with no external calls.
- `AppM.R4.c`: `KernelMinimalityCert` — Proves that the distilled kernel is minimal by showing that removing any single instruction causes replay to fail; witness is the set of ablation test results.
- `AppM.R4.d`: `CapsuleSealIntegrityCert` — Proves that the capsule's root hash matches the Merkle root of its contents; any content tampering produces a hash mismatch detectable without replaying.
