# InvW - Container Unwinding & Virtual Unmount

Routing role: Reverses AppN (Container Formats and Virtual Mount). Where AppN encapsulated organisms into container formats and mounted virtual filesystems for navigation, InvW unwinds containers back to raw crystal lattice and unmounts virtual layers, returning content to its native addressing.

Mirror of: AppN (Container Formats and Virtual Mount)
Arc: W | Rot: 315° → 45° | Lane: Container→Raw | w: 9D

## StationHeader
```
Arc:  W (Container Unwinding)
Rot:  315° (structural depackaging angle)
Lane: Descent-Container (container dissolution lane)
w:    9D → seed (virtual layers collapse to native addressing)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvW.S1.a`: `ContainerHeaderStrip` — The discrete removal of the container header from a packaged organism. The header contains format version, content manifest, integrity checksums, and mount instructions. Stripping reveals the raw payload. The successor inverts: "remove the outermost envelope layer."
- `InvW.S1.b`: `VirtualMountpointDetach` — The difference between the virtual filesystem's address space and the organism's native crystal addresses. Detaching the mountpoint removes the virtual-to-native translation layer, exposing raw crystal coordinates. The zero set: addresses that are identical in both spaces (natural mount points).
- `InvW.S1.c`: `LayerProductDisassembly` — Containers may have multiple layers (base + overlays). The product of all layers = the composite filesystem. Disassembly factors the product back into individual layers, each layer peeled independently. The factorization is unique when layers have no circular dependencies.
- `InvW.S1.d`: `OverlayQuotientReduction` — Each overlay layer is a quotient: overlay_content / base_content = delta. To unwind, the delta is subtracted from the composite, recovering the base. Multiple overlays unwind in reverse application order: last applied = first removed.

#### Facet 2 - Laws

- `InvW.S2.a`: `HeaderIntegrityOnStrip` — The container header must be valid (correct format version, matching checksums) before stripping is permitted. Stripping an invalid header may corrupt the payload. Integrity check is mandatory, not optional.
- `InvW.S2.b`: `MountpointCleanDetachLaw` — No open file handles, no pending writes, no cached reads may exist at the mountpoint when detach occurs. All I/O must be flushed and closed. Detaching with active I/O causes data corruption.
- `InvW.S2.c`: `LayerOrderPreservationLaw` — Layers must be disassembled in reverse order of assembly. Out-of-order disassembly produces incorrect deltas and corrupts the base. The assembly order is recorded in the container manifest and must be followed exactly.
- `InvW.S2.d`: `DeltaExactnessLaw` — The overlay delta must exactly account for the difference between composite and base. Any residual after delta subtraction indicates a corrupted overlay or a missing intermediate layer.

#### Facet 3 - Constructions

- `InvW.S3.a`: `HeaderValidator` — Reads the container header, verifies format version compatibility, recomputes payload checksums, and compares against declared values. If valid, authorizes stripping. If invalid, generates a corruption report.
- `InvW.S3.b`: `IOFlusher` — Scans for open file handles, pending writes, and cached reads at the mountpoint. Flushes all pending operations, closes all handles, invalidates all caches. Reports any operations that could not be cleanly completed.
- `InvW.S3.c`: `LayerPeeler` — Reads the assembly order from the manifest. Peels layers in reverse order: for each layer, computes its delta (layer_content - previous_state), archives the delta, and removes the layer from the composite. Verifies that the residual base matches the declared base hash.
- `InvW.S3.d`: `DeltaReconciler` — For each overlay: computes the delta, subtracts it from the composite, and checks for residual. Zero residual = clean peel. Non-zero residual triggers investigation into missing layers or corruption.

#### Facet 4 - Certificates

- `InvW.S4.a`: `HeaderStripCert` — Receipt proving header was valid, checksums matched, stripping completed cleanly, raw payload is intact.
- `InvW.S4.b`: `CleanDetachCert` — Receipt proving all I/O flushed, all handles closed, no cached data lost, mountpoint is clean.
- `InvW.S4.c`: `LayerPeelCert` — Receipt proving layers peeled in correct reverse order, all deltas computed and archived, base hash matches after full peel.
- `InvW.S4.d`: `DeltaExactnessCert` — Receipt proving all overlay deltas exact, no residuals after subtraction, no missing layers detected.

### Lens F

#### Facet 1 - Objects

- `InvW.F1.a`: `ContainerDecompressionWave` — The container's compressed payload decompresses as a wave front expanding through the crystal lattice. The Flower view: container compression created a standing wave in data space; decompression releases the wave to propagate back to its natural state.
- `InvW.F1.b`: `VirtualAddressPhaseShift` — Virtual mounting applied a phase shift to the address space (translating crystal coordinates to virtual filesystem paths). Unmounting reverses the phase: virtual paths shift back to crystal coordinates. The inverse phase must be exact.
- `InvW.F1.c`: `LayerSuperposition` — Multiple container layers superpose like harmonic modes. The composite is the sum of all layer-waves. Unwinding decomposes the superposition into individual modes, each at its natural frequency. This is the inverse Fourier transform of the container.
- `InvW.F1.d`: `CompressionRelaxation` — The container's compressed state represents potential energy stored during packaging. Decompression is relaxation: potential energy converts to kinetic energy as data expands to its natural volume. The relaxation time constant governs decompression speed.

#### Facet 2 - Laws

- `InvW.F2.a`: `WavefrontIntegrityLaw` — The decompression wavefront must advance monotonically through the lattice. No position is decompressed twice, no position is skipped. The wavefront is a connected surface at all times.
- `InvW.F2.b`: `PhaseExactnessLaw` — The inverse phase shift must exactly cancel the forward phase shift. Any phase error accumulates across the address space and produces systematic addressing errors. Phase error tolerance: zero.
- `InvW.F2.c`: `ModeSeparationLaw` — Layer modes must be orthogonal for clean decomposition. Non-orthogonal layers require Gram-Schmidt orthogonalization before individual extraction is possible. The container format must guarantee mode orthogonality.
- `InvW.F2.d`: `RelaxationBoundLaw` — Decompression must complete within bounded time. The time constant is proportional to the compression ratio: higher compression = longer relaxation. Unbounded relaxation indicates a degenerate container (infinite compression ratio).

#### Facet 3 - Constructions

- `InvW.F3.a`: `WavefrontExpander` — Advances the decompression wavefront through the lattice one cell at a time. Verifies monotonic progress, connected surface, and no revisits. Reports wavefront position and completion percentage.
- `InvW.F3.b`: `InversePhaseApplier` — Computes the inverse phase function from the mount configuration and applies it to every virtual address. Verifies round-trip: apply(inverse(addr)) = original crystal address. Reports any phase errors.
- `InvW.F3.c`: `ModeDecomposer` — Applies inverse Fourier transform (or equivalent) to decompose the composite container into individual layer modes. Verifies orthogonality. Reports any non-orthogonal pairs requiring correction.
- `InvW.F3.d`: `RelaxationController` — Governs decompression speed according to the time constant. Prevents runaway expansion (buffer overflow) and stalled expansion (timeout). Reports actual relaxation profile vs. expected.

#### Facet 4 - Certificates

- `InvW.F4.a`: `WavefrontCert` — Receipt proving decompression wavefront advanced monotonically, no skips, no revisits, complete lattice coverage.
- `InvW.F4.b`: `PhaseReversalCert` — Receipt proving inverse phase exactly cancels forward phase, all addresses correctly resolved, zero phase error.
- `InvW.F4.c`: `ModeDecompositionCert` — Receipt proving all layers decomposed into orthogonal modes, no mode contamination, individual layers correctly extracted.
- `InvW.F4.d`: `RelaxationCert` — Receipt proving decompression completed within bounded time, no runaway or stall, relaxation profile matches expected.

### Lens C

#### Facet 1 - Objects

- `InvW.C1.a`: `ContainerCorruptionPrior` — The prior probability that a container is corrupted, estimated from historical data. The Cloud view: before opening any container, we have a base rate of corruption to expect. This prior governs how aggressively we verify.
- `InvW.C1.b`: `LayerIndependenceTest` — The statistical test for whether container layers are independent (no shared mutable state). If independent, unwinding can proceed in parallel. If dependent, sequential unwinding is required.
- `InvW.C1.c`: `ParallelUnwindProduct` — If layers are independent, P(successful unwind) = Π P(layer_i unwound). The factorized product gives the overall success probability, which must exceed the organism's reliability threshold.
- `InvW.C1.d`: `CostBenefitRatio` — The ratio of verification cost to corruption risk. When the ratio is high (expensive verification, low risk), sampling-based verification is preferred. When low (cheap verification, high risk), full verification is preferred.

#### Facet 2 - Laws

- `InvW.C2.a`: `VerificationIntensityLaw` — Verification intensity must be proportional to the corruption prior. Higher prior = more intensive verification. The intensity function is calibrated so that post-verification corruption probability is below tolerance.
- `InvW.C2.b`: `IndependenceBeforeParallelismLaw` — Parallel unwinding is only legal after independence is statistically verified. The test must achieve the declared significance level (typically p < 0.01).
- `InvW.C2.c`: `ReliabilityThresholdLaw` — The factorized success probability must exceed the organism's reliability threshold. If any layer's individual probability is too low, it must be individually remediated before parallel unwinding proceeds.
- `InvW.C2.d`: `OptimalVerificationLaw` — The verification strategy must minimize expected total cost (verification cost + expected corruption damage). Neither over-verification nor under-verification is optimal.

#### Facet 3 - Constructions

- `InvW.C3.a`: `CorruptionPriorEstimator` — Estimates the corruption prior from historical container data. Uses Bayesian updating: prior × likelihood(current_evidence) = posterior. Outputs the posterior corruption probability.
- `InvW.C3.b`: `IndependenceTester` — Tests layer independence by checking for shared mutable state (shared files, shared memory regions, shared configuration). Reports the test statistic and p-value.
- `InvW.C3.c`: `SuccessProbabilityCalculator` — Computes Π P(layer_i unwound) from individual layer success probabilities. Identifies the weakest layer (lowest individual probability) and recommends remediation.
- `InvW.C3.d`: `VerificationOptimizer` — Computes the optimal verification strategy by minimizing expected total cost. Outputs the recommended intensity and method (full scan, sampling, or trust-based).

#### Facet 4 - Certificates

- `InvW.C4.a`: `CorruptionPriorCert` — Receipt proving prior correctly estimated, Bayesian update applied, posterior below tolerance.
- `InvW.C4.b`: `IndependenceTestCert` — Receipt proving independence test passed at declared significance level, parallel unwinding authorized.
- `InvW.C4.c`: `ReliabilityCert` — Receipt proving factorized success probability exceeds threshold, no weak layers unresolved.
- `InvW.C4.d`: `VerificationOptimalityCert` — Receipt proving verification strategy minimizes expected cost, neither over- nor under-verification applied.

### Lens R

#### Facet 1 - Objects

- `InvW.R1.a`: `RecursiveContainerUnwinding` — Containers may nest (a container within a container). Unwinding is recursive: unwind the outer container, discover inner containers, unwind those. The recursion terminates at atomic content (raw shards with no container wrapper).
- `InvW.R1.b`: `NestingDepthContraction` — Each unwinding level reduces nesting depth by 1. The contraction factor is 1/(current_depth), which increases as depth decreases — unwinding accelerates as it approaches the base. This is the inverse of the logarithmic slowdown during deep packaging.
- `InvW.R1.c`: `ContainerTreeTraversal` — The nesting structure forms a tree. Unwinding traverses the tree from leaves (deepest nested containers) to root (outermost container). At each node, the container wrapper is dissolved and its children are exposed. Multiplicative nesting inverts to sequential exposure.
- `InvW.R1.d`: `ScaleInvariantUnwinding` — The unwinding protocol is the same at every nesting level: validate header, flush I/O, peel layers, reconcile deltas. Only the content changes; the protocol is a fixed point of the nesting recursion.

#### Facet 2 - Laws

- `InvW.R2.a`: `DepthFirstUnwindingLaw` — Recursive unwinding must proceed depth-first: unwind the deepest nested container before its parent. This prevents accessing content through a partially-unwound wrapper.
- `InvW.R2.b`: `AcceleratingContractionLaw` — Each level must reduce nesting depth by exactly 1. No level may skip depths or create new nesting. The contraction is strict and monotone.
- `InvW.R2.c`: `FiniteNestingLaw` — Total nesting depth must be finite and bounded by the organism's declared recursion limit. Infinitely nested containers are rejected as malformed.
- `InvW.R2.d`: `ProtocolInvarianceLaw` — The unwinding protocol must be identical at every nesting level. Level-specific behavior indicates a format inconsistency that must be resolved.

#### Facet 3 - Constructions

- `InvW.R3.a`: `DepthFirstUnwinder` — Traverses the container tree depth-first. At each leaf: unwraps the atomic content. At each internal node: validates, flushes, peels, reconciles, then exposes children. Reports total depth, total nodes, and any malformed levels.
- `InvW.R3.b`: `DepthTracker` — Monitors nesting depth at each step. Verifies strict monotone decrease. Reports the depth sequence and flags any anomalies.
- `InvW.R3.c`: `NestingBoundChecker` — Verifies total nesting depth is within the declared bound before beginning unwinding. Rejects containers exceeding the bound. Reports actual depth vs. limit.
- `InvW.R3.d`: `ProtocolVerifier` — Compares the operation sequence at each nesting level. Reports any deviations from the canonical protocol. Flags level-specific behavior for investigation.

#### Facet 4 - Certificates

- `InvW.R4.a`: `DepthFirstCert` — Receipt proving depth-first unwinding completed, all leaves before parents, no partial unwrappings.
- `InvW.R4.b`: `MonotoneDepthCert` — Receipt proving nesting depth decreased monotonically, no skips or new nesting created.
- `InvW.R4.c`: `FiniteNestingCert` — Receipt proving total depth within bound, no infinite nesting, all levels accounted for.
- `InvW.R4.d`: `ProtocolInvarianceCert` — Receipt proving protocol identical at every level, no format inconsistencies, fixed-point property holds.
