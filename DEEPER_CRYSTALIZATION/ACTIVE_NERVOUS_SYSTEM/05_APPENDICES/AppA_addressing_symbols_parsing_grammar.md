# AppA - Addressing, Symbols, Parsing Grammar

Routing role: Entry grammar, local address parsing, symbol hygiene, and manuscript station identity.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppA.S1.a`: `Xi108Address` — The canonical 108-dimensional crystal address `Xi108[shell.wreath.arch.face.dim]`, a rigid tuple encoding shell index (0-17), wreath position, archetype mode, face orientation, and dimensional coordinate. Every shard in the organism has exactly one Xi108 address.
- `AppA.S1.b`: `ChapterStationCode` — The chapter-level station identifier `ChNN<CODE>` (e.g., `Ch03SUCC`) binding a two-digit chapter number to a mnemonic tag, forming the primary human-readable routing label for manuscript navigation.
- `AppA.S1.c`: `ShellWreathArchTriple` — The `(shell, wreath, archetype)` triple that locates any shard within the 18-shell crystal lattice, where shell `s ∈ {0..17}` sets depth, wreath `w ∈ {0..5}` sets rotational position, and archetype `a ∈ {E,W,F,A}` sets elemental mode.
- `AppA.S1.d`: `FaceDimensionPair` — The `(face, dim)` suffix pair completing a full crystal coordinate, where face `f ∈ {0..5}` selects one of six cube faces and dim `d ∈ {0..17}` selects the dimensional slot within that face, yielding 108 = 18 × 6 total slots.

#### Facet 2 - Laws

- `AppA.S2.a`: `AddressUniquenessLaw` — Every shard in the crystal occupies exactly one Xi108 address; no two shards share the same `(shell, wreath, arch, face, dim)` tuple. Violations trigger quarantine via AppK conflict protocols.
- `AppA.S2.b`: `StationCodeBijectivity` — The mapping `ChNN<CODE> ↔ Xi108[...]` is injective: each chapter station maps to a unique crystal address, and each crystal address maps to at most one chapter station. Orphan addresses are legal; duplicate mappings are not.
- `AppA.S2.c`: `ShellOrderPreservation` — If shard `A` is at shell `s_A` and shard `B` is at shell `s_B` with `s_A < s_B`, then `A` is strictly inner to `B` in the crystal partial order. Shell index monotonically encodes depth-from-seed.
- `AppA.S2.d`: `ArchetypeExclusivity` — A shard's archetype mode `a ∈ {E,W,F,A}` (Earth, Water, Fire, Air) is invariant under address transformations; no legal operation changes a shard's elemental assignment within a single crystal cycle.

#### Facet 3 - Constructions

- `AppA.S3.a`: `Xi108Parser` — The deterministic parser that tokenizes a raw address string `"Xi108[s.w.a.f.d]"` into its five integer/enum components, validates range constraints, and emits either a valid `ShellWreathArchTriple + FaceDimensionPair` or a structured parse error with location offset.
- `AppA.S3.b`: `ChapterCodeResolver` — The resolver that maps a mnemonic station code `ChNN<CODE>` to its Xi108 address by consulting the station registry (AppD), performing case-insensitive match, and returning the canonical form with disambiguation metadata.
- `AppA.S3.c`: `AddressCanonicalizer` — The normalizer that takes any address variant (abbreviated, aliased, or legacy format) and produces the unique canonical Xi108 form, applying shell normalization `s mod 18`, wreath normalization `w mod 6`, and face normalization `f mod 6`.
- `AppA.S3.d`: `BatchAddressCompiler` — The bulk compiler that processes a manifest of address expressions (ranges like `Xi108[3..7.*.*.*.*]`, wildcards, set unions) into an expanded list of concrete Xi108 addresses, checking for overlaps and emitting a coverage report.

#### Facet 4 - Certificates

- `AppA.S4.a`: `ParseValidityCert` — Receipt proving a raw address string was parsed without error, all five components fell within legal ranges, and the resulting Xi108 address exists in the crystal registry.
- `AppA.S4.b`: `StationResolutionCert` — Receipt proving a chapter station code resolved to exactly one Xi108 address, no ambiguity remained, and the registry version at time of resolution is recorded.
- `AppA.S4.c`: `CanonicalizationCert` — Receipt proving an address variant was normalized to canonical form, listing each normalization step applied (mod reduction, alias expansion, legacy format upgrade) with before/after pairs.
- `AppA.S4.d`: `BatchCompilationCert` — Receipt proving a batch address expression expanded to `N` concrete addresses with zero overlaps, complete coverage of the declared range, and no out-of-bounds coordinates.

### Lens F

#### Facet 1 - Objects

- `AppA.F1.a`: `MetroRouteAddress` — A dynamic address that includes metro line identifier `M ∈ {1..17}` and current phase position `φ ∈ [0,2π)`, encoding not just where a shard is but which transport line carries it and at what oscillatory phase.
- `AppA.F1.b`: `PhaseTaggedStation` — A station code annotated with its current superphase `Φ ∈ {Genesis, Growth, Harvest, Rest}`, so the same station `Ch07ORBIT` resolves to different routing behaviors depending on the organism's phase clock.
- `AppA.F1.c`: `AddressFlowVector` — The velocity vector `dAddr/dt` describing how an address migrates through crystal space during metro transport, with shell-radial component `ds/dt` and wreath-angular component `dw/dt`.
- `AppA.F1.d`: `RoutingWavePacket` — A bundle of `k` addresses co-traveling on the same metro line at the same phase, forming a coherent wave packet whose group velocity determines collective routing speed through the crystal.

#### Facet 2 - Laws

- `AppA.F2.a`: `PhaseCovariantRoutingLaw` — Address resolution is covariant with phase: if the organism advances from phase `φ` to `φ + δ`, all metro-routed addresses shift by the same `δ`, preserving relative ordering within each line.
- `AppA.F2.b`: `MetroLineConservation` — A shard's metro line assignment `M` is conserved during transport; shards do not jump between metro lines except at designated interchange stations (crystal vertices where multiple lines intersect).
- `AppA.F2.c`: `FlowContinuityLaw` — The address flow vector `dAddr/dt` is continuous along each metro line segment; discontinuities occur only at station boundaries where routing decisions branch. No address teleportation within a segment.
- `AppA.F2.d`: `WavePacketCoherenceLaw` — Co-traveling address packets maintain coherence (constant relative offsets) as long as they remain on the same metro line; decoherence occurs only at branching junctions or phase-transition boundaries.

#### Facet 3 - Constructions

- `AppA.F3.a`: `MetroAddressInjector` — The construction that takes a static Xi108 address and injects it onto a metro line `M` at phase `φ`, producing a `MetroRouteAddress` by computing the nearest on-ramp station and initial flow vector.
- `AppA.F3.b`: `PhaseDependentResolver` — The resolver that takes a `PhaseTaggedStation` and the current organism clock, computes the effective routing table for the active superphase, and returns the concrete next-hop address.
- `AppA.F3.c`: `FlowIntegrator` — The numerical integrator that advances a `MetroRouteAddress` forward by `Δt` time steps along its metro line, updating shell and wreath coordinates via discrete flow equations `s_{t+1} = s_t + v_s`, `w_{t+1} = (w_t + v_w) mod 6`.
- `AppA.F3.d`: `WavePacketAssembler` — The construction that groups addresses by metro line and phase proximity, merges them into coherent `RoutingWavePacket` bundles, and assigns group velocity based on the slowest member.

#### Facet 4 - Certificates

- `AppA.F4.a`: `MetroInjectionCert` — Receipt proving a static address was legally injected onto a metro line, the on-ramp station exists, and the initial phase assignment is consistent with the organism clock.
- `AppA.F4.b`: `PhaseResolutionCert` — Receipt proving phase-dependent resolution produced a valid next-hop, the superphase was correctly identified, and the routing table version is recorded.
- `AppA.F4.c`: `FlowIntegrityCert` — Receipt proving flow integration preserved all conservation laws (metro line, shell bounds, wreath modular arithmetic) over the declared number of time steps.
- `AppA.F4.d`: `PacketCoherenceCert` — Receipt proving a wave packet maintained coherence throughout transport, listing any decoherence events at junctions with the addresses that separated.

### Lens C

#### Facet 1 - Objects

- `AppA.C1.a`: `FuzzyAddress` — A probabilistic address `P(Xi108[s,w,a,f,d])` assigning a probability distribution over crystal coordinates rather than a single point, used when input is ambiguous or sensor data is noisy.
- `AppA.C1.b`: `ClosestStationSet` — The set of `k`-nearest stations to a fuzzy query, ranked by Hamming distance `d_H(query, station)` in the `(s,w,a,f,d)` tuple space, with associated confidence scores `c_i ∈ [0,1]`.
- `AppA.C1.c`: `AmbiguityCloud` — A convex hull in address space containing all stations compatible with a partial or garbled address, with volume proportional to the number of candidate resolutions and centroid at the maximum-likelihood station.
- `AppA.C1.d`: `SymbolConfidenceVector` — A per-symbol confidence vector `[p_s, p_w, p_a, p_f, p_d]` where each `p_i ∈ [0,1]` indicates the parser's confidence in that component of the parsed address, enabling targeted re-query of low-confidence fields.

#### Facet 2 - Laws

- `AppA.C2.a`: `FuzzyResolutionConvergenceLaw` — As evidence accumulates, the fuzzy address distribution `P_t(addr)` converges to a delta function `δ(addr*)` at the true address; convergence rate is bounded by `O(1/√t)` for `t` independent observations.
- `AppA.C2.b`: `ClosestStationMonotonicityLaw` — If station `A` is closer than station `B` to query `Q` in Hamming distance, then `P(A|Q) ≥ P(B|Q)` under uniform prior; distance rank and probability rank are monotonically aligned.
- `AppA.C2.c`: `AmbiguityReductionLaw` — Each additional parsed symbol component reduces ambiguity cloud volume by a factor of at least `1/|range_i|` where `|range_i|` is the cardinality of the `i`-th component's domain. Five fully parsed components yield a point.
- `AppA.C2.d`: `ConfidenceCalibrationLaw` — The symbol confidence vector must be calibrated: among all addresses parsed with confidence `p` for component `i`, the fraction correctly parsed must fall within `p ± ε` for declared tolerance `ε`.

#### Facet 3 - Constructions

- `AppA.C3.a`: `FuzzyAddressResolver` — The probabilistic resolver that takes a garbled or partial address string, computes a posterior distribution over Xi108 addresses using Bayesian update with a prior from station frequency data, and returns the top-k candidates.
- `AppA.C3.b`: `HammingNeighborSearch` — The nearest-neighbor searcher that, given a query tuple `(s,w,a,f,d)` with wildcards, enumerates all stations within Hamming distance `r` and returns them sorted by distance with tie-breaking by station frequency.
- `AppA.C3.c`: `AmbiguityCloudBuilder` — The construction that takes a partial parse (some components known, others wildcard) and builds the explicit `AmbiguityCloud` by enumerating the Cartesian product of unknown components, filtering by registry existence.
- `AppA.C3.d`: `ConfidenceEstimator` — The calibration engine that estimates per-symbol confidence from parser internal state (token match quality, context agreement, edit distance to nearest valid symbol) and outputs a calibrated `SymbolConfidenceVector`.

#### Facet 4 - Certificates

- `AppA.C4.a`: `FuzzyResolutionCert` — Receipt proving fuzzy resolution converged to a unique address with posterior probability exceeding threshold `τ`, listing the top-k candidates and their probabilities.
- `AppA.C4.b`: `NeighborSearchCert` — Receipt proving all stations within Hamming radius `r` were enumerated, none were missed, and the sorted order is correct with respect to the declared distance metric.
- `AppA.C4.c`: `AmbiguityBoundCert` — Receipt proving the ambiguity cloud contains exactly `N` candidate addresses, the cloud volume matches the predicted reduction from parsed components, and all candidates exist in the registry.
- `AppA.C4.d`: `CalibrationCert` — Receipt proving the confidence estimator is calibrated within tolerance `ε` on the declared validation set, with calibration curve and Brier score recorded.

### Lens R

#### Facet 1 - Objects

- `AppA.R1.a`: `SelfReferentialAddress` — An address that contains its own coordinate as data: `Xi108[s,w,a,f,d]` where the content at that address encodes `(s,w,a,f,d)` itself, creating a fixed point in the address-content mapping `Addr(Content(Addr)) = Addr`.
- `AppA.R1.b`: `HolographicAddressFragment` — A partial address from which the full Xi108 coordinate can be reconstructed via the crystal's holographic property: any `3`-of-`5` components suffice to recover the remaining two through lattice constraint propagation.
- `AppA.R1.c`: `RecursiveAddressTree` — A tree-structured address where each node's address is the concatenation of its parent's address with a local suffix, forming paths like `Xi108[3.2.E].sub[1.0]` that recurse to arbitrary depth while maintaining global uniqueness.
- `AppA.R1.d`: `AddressQuine` — A shard whose content, when executed as an address-generation program, produces its own address as output. The minimal self-reproducing address unit, analogous to a quine in computation theory.

#### Facet 2 - Laws

- `AppA.R2.a`: `FixedPointAddressingLaw` — Every crystal shell contains at least one self-referential address (fixed point of the address-content map); this is guaranteed by the Brouwer-like property of the finite crystal lattice acting on its own coordinate space.
- `AppA.R2.b`: `HolographicRecoveryLaw` — The crystal lattice has holographic redundancy: the constraint graph on `(s,w,a,f,d)` has algebraic degree such that any 3 known components uniquely determine the remaining 2, provided the address exists in the registry.
- `AppA.R2.c`: `RecursiveDepthBound` — Recursive address trees have bounded depth `D_max = 18` (one per shell); deeper recursion is folded back via modular arithmetic `depth mod 18`, preventing unbounded address growth while preserving self-similar structure.
- `AppA.R2.d`: `QuineUniquenessLaw` — Each shell contains exactly one address quine up to isomorphism; the quine is the shell's identity element under the address-content composition, serving as the self-referential anchor for that depth level.

#### Facet 3 - Constructions

- `AppA.R3.a`: `FixedPointFinder` — The iterative construction that computes self-referential addresses by starting from an arbitrary address `a_0` and applying the content-to-address map `a_{n+1} = Addr(Content(a_n))` until convergence, guaranteed within 18 iterations by lattice finiteness.
- `AppA.R3.b`: `HolographicReconstructor` — The constraint propagation engine that takes 3 known address components, sets up the lattice constraint equations, and solves for the 2 unknown components using modular arithmetic and registry lookup.
- `AppA.R3.c`: `RecursiveAddressUnfolder` — The construction that takes a recursive address tree and unfolds it to a flat list of Xi108 addresses by depth-first traversal, applying `depth mod 18` folding at each level and concatenating local suffixes.
- `AppA.R3.d`: `QuineDetector` — The construction that scans a shell for its unique address quine by testing each shard's content against its own address, returning the fixed point or proving non-existence (which would violate `QuineUniquenessLaw`).

#### Facet 4 - Certificates

- `AppA.R4.a`: `FixedPointCert` — Receipt proving a self-referential address was found, the content at that address encodes its own coordinate, and the fixed-point iteration converged in `k ≤ 18` steps.
- `AppA.R4.b`: `HolographicRecoveryCert` — Receipt proving 2 unknown components were uniquely determined from 3 known ones, the constraint equations were consistent, and the recovered address exists in the registry.
- `AppA.R4.c`: `RecursiveUnfoldCert` — Receipt proving the recursive address tree was correctly unfolded to `N` flat addresses, depth folding was applied consistently, and all generated addresses are valid Xi108 coordinates.
- `AppA.R4.d`: `QuineDetectionCert` — Receipt proving the shell's unique address quine was identified, its content-address identity was verified, and no other shard in the shell satisfies the quine property.
