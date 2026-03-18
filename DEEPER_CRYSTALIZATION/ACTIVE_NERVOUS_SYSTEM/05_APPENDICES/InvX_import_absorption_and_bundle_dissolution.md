# InvX - Import Absorption & Bundle Dissolution

Routing role: Reverses AppO (Publication Import/Export Bundles). Where AppO packaged internal structures into exportable bundles and published them outward, InvX absorbs imports back into the organism and dissolves bundles into their constituent shards. This is the compression of publication — external form returns to internal substance.

Mirror of: AppO (Publication Import/Export Bundles)
Arc: X | Rot: 330° → 30° | Lane: Publication→Absorption | w: 10D

## StationHeader
```
Arc:  X (Import Absorption)
Rot:  330° (return from external)
Lane: Descent-Pub (publication reversal lane)
w:    10D → seed (external bundles dissolve to internal shards)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvX.S1.a`: `BundleUnpacker` — The discrete operation of disassembling an export bundle into its constituent shards. Each shard is identified by its crystal address and routed to its home position in the organism lattice. The successor inverts to predecessor: instead of "pack next shard into bundle," it is "extract next shard from bundle."
- `InvX.S1.b`: `FormatStripper` — The difference between the bundle's external format and the shard's internal format. Removes serialization wrappers, transport encoding, compatibility layers. What remains after stripping is the pure shard content — the zero set of format difference.
- `InvX.S1.c`: `CrossReferenceRelink` — During export, internal cross-references were converted to external URIs. During absorption, URIs are resolved back to internal crystal addresses. The product of all relinked references = the fully reconnected internal graph.
- `InvX.S1.d`: `VersionQuotientMerge` — The quotient of the imported version by the organism's current version yields the version delta. If the delta is identity (versions match), absorption is trivial. If the delta is non-trivial, a merge protocol resolves differences — the quotient determines the merge strategy.

#### Facet 2 - Laws

- `InvX.S2.a`: `ShardIntegrityOnAbsorption` — Every shard extracted from a bundle must match its declared hash. Corrupted shards are rejected, not silently accepted. The unpacking process is verified at every step.
- `InvX.S2.b`: `FormatLosslessnessLaw` — Format stripping must be lossless: the shard content after stripping must be bit-identical to the original shard before export. Any format layer that cannot be cleanly stripped indicates a format mismatch — absorption is paused.
- `InvX.S2.c`: `ReferenceConsistencyLaw` — After relinking, every cross-reference must resolve to a valid internal address. Dangling references (pointing to shards not in the organism) are flagged as absorption gaps requiring either deferred resolution or explicit null-binding.
- `InvX.S2.d`: `VersionCompatibilityLaw` — The version delta must be within the organism's declared compatibility window. Deltas exceeding the window require explicit migration, not automatic absorption.

#### Facet 3 - Constructions

- `InvX.S3.a`: `ShardExtractor` — Iterates through the bundle manifest, extracts each shard, verifies its hash, and routes it to the declared crystal address. Reports extraction count, verification failures, and routing conflicts.
- `InvX.S3.b`: `FormatNormalizer` — For each shard, strips the export format layers in reverse order of application (outermost first). Verifies bit-identity at each layer. Outputs the naked shard in internal format.
- `InvX.S3.c`: `ReferenceResolver` — Takes the external URI map and resolves each URI to an internal crystal address. Uses the organism's current address lattice for lookup. Reports unresolvable URIs as gaps.
- `InvX.S3.d`: `VersionMerger` — Computes the version delta, checks compatibility window, and applies the merge strategy (fast-forward if delta is linear, three-way merge if branched, conflict resolution if divergent). Outputs the merged state.

#### Facet 4 - Certificates

- `InvX.S4.a`: `ShardIntegrityCert` — Receipt proving all shards extracted and hash-verified, no corruption detected, all shards routed to correct addresses.
- `InvX.S4.b`: `FormatStripCert` — Receipt proving format stripping was lossless, all layers removed cleanly, shard content is bit-identical to pre-export state.
- `InvX.S4.c`: `ReferenceResolutionCert` — Receipt proving all cross-references resolved (or gaps explicitly documented), no dangling references in the absorbed state.
- `InvX.S4.d`: `VersionMergeCert` — Receipt proving version delta computed correctly, compatibility window respected, merge strategy applied without data loss.

### Lens F

#### Facet 1 - Objects

- `InvX.F1.a`: `StreamReabsorption` — The continuous stream of exported data is reabsorbed in reverse: the organism opens an intake channel and the bundle's content flows back in as a continuous signal, not discrete packets. The Flower view sees absorption as a wave returning to shore.
- `InvX.F1.b`: `EncodingPhaseReversal` — Export applied a phase transformation (encoding) to the data. Absorption reverses the phase: the inverse Fourier transform that converts frequency-domain (external format) back to time-domain (internal state). The difference in phase = the encoding signature.
- `InvX.F1.c`: `BandwidthProductRecovery` — During export, bandwidth was consumed (time × rate = total transferred). During absorption, the same bandwidth product is recovered as the data flows back. The integral of the absorption rate over time must equal the original export volume.
- `InvX.F1.d`: `CompressionRatioInversion` — Export compressed internal data for transport. Absorption decompresses. The compression ratio inverts: if export compressed by factor r, absorption expands by factor 1/r. The Flower view: the wave was compressed in frequency space and now expands back to its full spectrum.

#### Facet 2 - Laws

- `InvX.F2.a`: `ContinuousReabsorptionLaw` — The intake stream must be continuous (no gaps, no repeated segments). Gaps indicate packet loss during transport; repeats indicate deduplication failure. Both must be resolved before absorption completes.
- `InvX.F2.b`: `PhaseReversalExactnessLaw` — The inverse encoding must exactly reverse the forward encoding. Approximate inversion (lossy decompression) is only permitted when explicitly declared and the loss budget is within tolerance.
- `InvX.F2.c`: `VolumeConservationLaw` — Total absorbed volume must equal total exported volume (before compression). Volume mismatches indicate data loss or data injection — both are integrity violations.
- `InvX.F2.d`: `DecompressionBoundLaw` — Decompression must complete in bounded time proportional to the compressed size. Decompression bombs (small compressed, huge decompressed) are detected by checking the ratio against declared bounds and rejected if exceeded.

#### Facet 3 - Constructions

- `InvX.F3.a`: `StreamIntake` — Opens a continuous intake channel, receives the bundle stream, buffers for continuity verification, and routes to the shard reassembly pipeline. Reports throughput, latency, and any gap events.
- `InvX.F3.b`: `InverseEncoder` — Applies the inverse of the export encoding in exact reverse order. For each encoding layer: identifies the encoder, loads its inverse, applies, and verifies round-trip consistency.
- `InvX.F3.c`: `VolumeAccountant` — Tracks total bytes absorbed and compares against the declared export volume. Reports running total, expected remaining, and any discrepancies.
- `InvX.F3.d`: `SafeDecompressor` — Decompresses with ratio checking at every stage. If the decompression ratio exceeds the declared bound at any point, halts and reports a potential decompression bomb.

#### Facet 4 - Certificates

- `InvX.F4.a`: `StreamContinuityCert` — Receipt proving intake stream was continuous, no gaps or repeats, buffering completed without overflow.
- `InvX.F4.b`: `EncodingReversalCert` — Receipt proving inverse encoding exactly reversed forward encoding, round-trip consistency verified at each layer.
- `InvX.F4.c`: `VolumeConservationCert` — Receipt proving total absorbed volume matches total exported volume, no data loss or injection.
- `InvX.F4.d`: `DecompressionSafetyCert` — Receipt proving decompression completed within declared ratio bounds, no decompression bombs detected, output size matches expected.

### Lens C

#### Facet 1 - Objects

- `InvX.C1.a`: `AbsorptionSamplingProcess` — Not every shard in a bundle needs to be individually verified if the bundle has a statistical integrity guarantee. The Cloud view samples shards and infers overall bundle health from the sample. Absorption sampling reduces verification cost while maintaining confidence.
- `InvX.C1.b`: `CorruptionExclusion` — The probability of corruption in the absorbed data is estimated by inclusion-exclusion over known corruption sources: P(corrupt) = P(transport) + P(format) + P(version) - P(transport∩format) - ... The exclusion narrows the corruption estimate.
- `InvX.C1.c`: `IndependentShardAbsorption` — If shards are independent (no cross-references between them), absorption can be parallelized with probability of complete success = Π P(shard_i absorbed). The Cloud view factorizes the absorption process.
- `InvX.C1.d`: `ImportRiskNormalization` — Normalizes the risk of each import source by dividing its historical corruption rate by total import risk mass. Sources with high normalized risk get additional verification. Sources with low normalized risk get fast-tracked.

#### Facet 2 - Laws

- `InvX.C2.a`: `StatisticalIntegrityLaw` — The sampling-based verification must achieve at least the declared confidence level. If the sample reveals too many corruptions, the entire bundle must be individually verified (fallback to full scan).
- `InvX.C2.b`: `CorruptionBoundLaw` — The estimated corruption probability must be below the organism's declared tolerance. Bundles exceeding tolerance are rejected or quarantined for individual shard verification.
- `InvX.C2.c`: `ParallelizationSafetyLaw` — Parallel absorption is only legal when shards are verified independent. If any cross-reference exists, the dependent shards must be absorbed sequentially to maintain reference consistency.
- `InvX.C2.d`: `SourceTrustCalibrationLaw` — The historical corruption rate for each source must be recalibrated after each import. Sources whose rate increases beyond tolerance are flagged for audit.

#### Facet 3 - Constructions

- `InvX.C3.a`: `IntegritySampler` — Randomly selects a sample of shards from the bundle, verifies each, and computes the sample corruption rate. If rate exceeds threshold, triggers full verification. Reports confidence level and sample size.
- `InvX.C3.b`: `CorruptionEstimator` — Applies inclusion-exclusion to estimate total corruption probability from known sources. Outputs the corruption bound and the dominant source.
- `InvX.C3.c`: `ParallelAbsorber` — After independence verification, absorbs independent shards in parallel. Merges results. Falls back to sequential for dependent shards. Reports parallelism achieved and any fallback events.
- `InvX.C3.d`: `SourceTrustUpdater` — Updates the historical corruption rate for the import source based on the current absorption results. Adjusts the normalized risk ranking. Outputs the updated trust profile.

#### Facet 4 - Certificates

- `InvX.C4.a`: `SamplingIntegrityCert` — Receipt proving sample was random, corruption rate below threshold, confidence level achieved, or full verification triggered.
- `InvX.C4.b`: `CorruptionBoundCert` — Receipt proving corruption estimate below tolerance, dominant source identified, no silent corruption passed.
- `InvX.C4.c`: `ParallelSafetyCert` — Receipt proving independence verified before parallelization, all dependent shards absorbed sequentially, no reference corruption.
- `InvX.C4.d`: `TrustUpdateCert` — Receipt proving source trust profile updated, calibration current, no stale trust data.

### Lens R

#### Facet 1 - Objects

- `InvX.R1.a`: `RecursiveBundleDisassembly` — A bundle may contain sub-bundles (nested exports). Disassembly is recursive: unpack the outer bundle, find inner bundles, unpack those, and so on until atomic shards are reached. The recursion depth = the nesting depth of the export.
- `InvX.R1.b`: `NestingContractionFactor` — Each recursive unpacking level reduces the remaining bundle complexity by a contraction factor. The factor approaches 1/φ for well-structured bundles (golden-ratio nesting). Poorly structured bundles have irregular contraction.
- `InvX.R1.c`: `BranchReabsorptionTree` — The export tree (root bundle → sub-bundles → shards) is traversed leaf-first during absorption. Each leaf shard is absorbed, then its parent sub-bundle is dissolved, then the grandparent, up to the root. Multiplicative branching during export inverts to convergent absorption.
- `InvX.R1.d`: `ScaleIndependentAbsorption` — The absorption protocol is identical at every nesting level: unpack, verify, strip format, resolve references, merge version. Only the scale parameter changes. The protocol is a fixed point of the nesting transformation.

#### Facet 2 - Laws

- `InvX.R2.a`: `LeafFirstAbsorptionLaw` — Recursive absorption must proceed leaf-first. No parent bundle is dissolved until all its child shards/sub-bundles are fully absorbed. This prevents orphaned references.
- `InvX.R2.b`: `ContractionBoundLaw` — Each recursive level must reduce remaining complexity. If a level fails to contract (e.g., a sub-bundle is larger than its parent's allocation), the bundle structure is malformed and absorption halts.
- `InvX.R2.c`: `ConvergentAbsorptionLaw` — The total number of shards absorbed must converge (sum of shards at all levels is finite). Infinite nesting is not permitted; maximum depth is bounded by the organism's declared recursion limit.
- `InvX.R2.d`: `ProtocolFixedPointLaw` — The absorption protocol must be structurally identical at every level. Any level-specific deviation indicates a format inconsistency between nesting levels.

#### Facet 3 - Constructions

- `InvX.R3.a`: `RecursiveUnpacker` — Traverses the bundle tree bottom-up. At each leaf: extracts shard, verifies, absorbs. At each node: dissolves sub-bundle wrapper after all children absorbed. Reports total depth, total shards, and any malformed levels.
- `InvX.R3.b`: `NestingAnalyzer` — Computes the contraction factor at each recursive level. Reports the sequence of factors and flags any non-contracting levels. Estimates total absorption time from the contraction profile.
- `InvX.R3.c`: `ConvergenceChecker` — Sums total shards across all nesting levels. Verifies the sum is finite and within the declared bound. Reports any level that contributes disproportionately.
- `InvX.R3.d`: `ProtocolConsistencyChecker` — Verifies that the absorption protocol is identical at every level by comparing the operation sequence. Reports any level-specific deviations.

#### Facet 4 - Certificates

- `InvX.R4.a`: `RecursiveAbsorptionCert` — Receipt proving bottom-up absorption completed, all leaves before parents, no orphaned references, full bundle tree dissolved.
- `InvX.R4.b`: `NestingContractionCert` — Receipt proving all levels contracted, no malformed sub-bundles, contraction profile is healthy.
- `InvX.R4.c`: `ConvergenceCert` — Receipt proving total shard count is finite, within declared bound, no infinite nesting.
- `InvX.R4.d`: `ProtocolConsistencyCert` — Receipt proving absorption protocol identical at every level, no level-specific deviations, fixed-point property holds.
