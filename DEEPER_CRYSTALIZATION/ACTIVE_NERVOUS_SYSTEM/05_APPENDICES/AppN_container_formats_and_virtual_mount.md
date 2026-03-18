# AppN - Container Formats and Virtual Mount

Routing role: Containers, salvage routes, mounted corpora, and runtime packaging.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppN.S1.a`: `ShardContainer` — A content-addressed envelope that wraps a single shard with its crystal coordinate, SFCR lens tag, and integrity hash; the atomic unit of crystal storage.
- `AppN.S1.b`: `CapsuleBundle` — A collection of related shard containers grouped by metro line or chapter, stored as a single seekable archive with an internal offset table for O(1) access to any member.
- `AppN.S1.c`: `CrystalArchive` — A complete snapshot of an entire crystal tile (4 lenses x 4 facets x 4 atoms = 64 cells) packaged as a single immutable archive with a root Merkle hash for integrity verification.
- `AppN.S1.d`: `SeedPacket` — A minimal bootstrap container holding the four cardinal seeds (+, -, x, /) and their Rosetta generation rules, sufficient to regenerate the full crystal archive from scratch.

#### Facet 2 - Laws

- `AppN.S2.a`: `ContainerAddressabilityLaw` — Every container must expose a content-address derived from its payload hash; two containers with identical payloads must have identical addresses regardless of creation time or location.
- `AppN.S2.b`: `BundleCompletenessLaw` — A capsule bundle is valid only if its offset table accounts for every shard container it claims to hold; missing entries or dangling offsets render the bundle invalid.
- `AppN.S2.c`: `ArchiveImmutabilityLaw` — Once a crystal archive is sealed, no shard may be added, removed, or modified; any mutation requires creating a new archive version with a new root hash.
- `AppN.S2.d`: `SeedSufficiencyLaw` — A seed packet must be sufficient to regenerate its corresponding crystal archive; the generated archive's root hash must match the hash recorded in the seed packet's header.

#### Facet 3 - Constructions

- `AppN.S3.a`: `ShardContainerBuilder` — Takes raw shard content, computes its crystal coordinate from the SFCR address, wraps it with metadata headers, and seals it with a content-address hash.
- `AppN.S3.b`: `BundleAssembler` — Collects a set of shard containers, sorts them by crystal coordinate, builds the offset table, and writes the seekable archive; validates completeness before sealing.
- `AppN.S3.c`: `ArchiveSnapshotter` — Traverses all 64 cells of a crystal tile, wraps each as a shard container, assembles them into a bundle, computes the Merkle root, and seals the crystal archive.
- `AppN.S3.d`: `SeedExtractor` — Given a crystal archive, identifies the four cardinal seed cells, extracts them with their generation rules, and packages them into a minimal seed packet.

#### Facet 4 - Certificates

- `AppN.S4.a`: `ContainerIntegrityCert` — Proves that a shard container's content-address hash matches its payload by exhibiting the hash computation; a single bit change in the payload invalidates the certificate.
- `AppN.S4.b`: `BundleCompletenessCert` — Proves that a capsule bundle's offset table is total and correct by exhibiting the list of all member shard addresses and their verified offsets.
- `AppN.S4.c`: `ArchiveMerkleCert` — Proves archive integrity by exhibiting the Merkle tree from leaf shard hashes to the root; any individual shard can be verified with an O(log n) Merkle path.
- `AppN.S4.d`: `SeedRegenerationCert` — Proves seed sufficiency by exhibiting the regenerated archive's root hash and showing it matches the original archive's root hash recorded in the seed packet.

### Lens F

#### Facet 1 - Objects

- `AppN.F1.a`: `MountPoint` — A virtual filesystem node where a container's contents become addressable as if they were local files; mounting binds a container's shard addresses to path names in the crystal namespace.
- `AppN.F1.b`: `LazyLoader` — A deferred-access proxy that presents shard metadata immediately but fetches actual content only on first read, reducing mount latency for large capsule bundles.
- `AppN.F1.c`: `StreamingAccessor` — A sequential reader that traverses a container's shards in crystal-coordinate order, emitting content as a continuous stream without requiring the entire archive to be resident in memory.
- `AppN.F1.d`: `HotSwapSocket` — A mount point that supports live replacement of the underlying container without unmounting; active readers are transparently redirected to the new container version.

#### Facet 2 - Laws

- `AppN.F2.a`: `MountAtomicityLaw` — Mounting a container is atomic: either all shards become accessible or none do; partial mounts are illegal and must be rolled back.
- `AppN.F2.b`: `LazyConsistencyLaw` — A lazily-loaded shard, once fetched, must be identical to what an eager load would have produced; lazy loading is an optimization, never a semantic change.
- `AppN.F2.c`: `StreamOrderPreservation` — A streaming accessor must emit shards in strict crystal-coordinate order (S before F before C before R, facet 1 before 2 before 3 before 4, atom a before b before c before d).
- `AppN.F2.d`: `HotSwapContinuityLaw` — After a hot swap, any shard address that existed in both old and new containers must resolve to the new version's content; stale reads are forbidden.

#### Facet 3 - Constructions

- `AppN.F3.a`: `VirtualMountEngine` — Maps a container's internal offset table to virtual path entries, registers them in the crystal namespace, and begins serving read requests; unmounting reverses the registration.
- `AppN.F3.b`: `PrefetchScheduler` — Monitors access patterns on a lazily-loaded mount and speculatively prefetches shards that are likely to be needed next, based on crystal-coordinate locality.
- `AppN.F3.c`: `StreamingPipeline` — Chains a container reader, a decompressor, and a shard parser into a zero-copy pipeline that converts raw archive bytes into typed shard objects without intermediate buffering.
- `AppN.F3.d`: `VersionedMountSwapper` — Coordinates hot swap by mounting the new container to a shadow mount point, verifying integrity, then atomically redirecting the primary mount point's resolution table.

#### Facet 4 - Certificates

- `AppN.F4.a`: `MountCompleteCert` — Proves that all shards in a container are accessible via the mount point by enumerating every shard address and confirming resolution; issued only after successful atomic mount.
- `AppN.F4.b`: `LazyLoadFidelityCert` — Proves that a lazily-loaded shard matches its container's recorded hash by exhibiting the hash comparison after first fetch.
- `AppN.F4.c`: `StreamOrderCert` — Proves that a streaming accessor emitted shards in correct crystal-coordinate order by exhibiting the sequence of addresses and verifying monotonicity.
- `AppN.F4.d`: `HotSwapAtomicityCert` — Proves that a hot swap completed atomically by exhibiting the mount point's resolution table before and after swap, showing no intermediate state was observable.

### Lens C

#### Facet 1 - Objects

- `AppN.C1.a`: `LensProjection` — A virtual view that presents only the shards belonging to a single SFCR lens (S, F, C, or R) from a full crystal archive, without copying or restructuring the underlying data.
- `AppN.C1.b`: `OverlayStack` — A layered composition of multiple containers where higher layers shadow lower layers for the same crystal address; resolves reads by scanning layers top-down, enabling incremental patches.
- `AppN.C1.c`: `MultiViewManifold` — A structure that maintains `k` simultaneous lens projections over the same archive, each presenting a different facet-subset; queries can be routed to any active view.
- `AppN.C1.d`: `VirtualUnionContainer` — A container that presents the union of shards from multiple source containers as if they were a single archive, resolving address collisions by priority ranking.

#### Facet 2 - Laws

- `AppN.C2.a`: `ProjectionCompletenessLaw` — A lens projection must include every shard whose SFCR tag matches the selected lens; omissions or false inclusions are projection errors.
- `AppN.C2.b`: `OverlayShadowingLaw` — In an overlay stack, if layers `L_i` and `L_j` (i > j) both contain a shard at address `A`, the resolved content is `L_i[A]`; lower layers are invisible for shadowed addresses.
- `AppN.C2.c`: `ViewConsistencyLaw` — All views in a multi-view manifold must derive from the same underlying archive version; stale views from a prior version must be invalidated on archive update.
- `AppN.C2.d`: `UnionDisjointnessPreference` — A virtual union container should log a warning when source containers have overlapping addresses; clean unions with disjoint address spaces are preferred.

#### Facet 3 - Constructions

- `AppN.C3.a`: `LensFilter` — Scans a crystal archive's offset table, selects entries whose SFCR tag matches the desired lens, and constructs a lightweight projection index that maps filtered addresses to archive offsets.
- `AppN.C3.b`: `OverlayMerger` — Flattens an overlay stack into a single resolved container by iterating all addresses top-down and emitting the first hit for each; produces a materialized snapshot of the overlay state.
- `AppN.C3.c`: `ManifoldSpawner` — Given a crystal archive, spawns `k` concurrent lens projections, each with its own read cursor and filter index, sharing the underlying archive via memory-mapped access.
- `AppN.C3.d`: `UnionResolver` — Takes `n` source containers, builds a unified address index with priority rankings, and exposes a single virtual container interface; supports lazy resolution for deferred conflict handling.

#### Facet 4 - Certificates

- `AppN.C4.a`: `ProjectionCorrectnessCert` — Proves that a lens projection contains exactly the shards matching the selected lens by exhibiting the filter predicate and the matched/unmatched address partition.
- `AppN.C4.b`: `OverlayResolutionCert` — Proves that every address in an overlay stack resolves to the correct layer by exhibiting the layer scan order and the first-hit index for each address.
- `AppN.C4.c`: `ViewFreshnessCert` — Proves that all views in a multi-view manifold reference the same archive version by exhibiting the archive root hash that each view was derived from.
- `AppN.C4.d`: `UnionCoverageCert` — Proves that a virtual union container covers the union of all source address sets by exhibiting each source's address list and the merged index.

### Lens R

#### Facet 1 - Objects

- `AppN.R1.a`: `SelfDescribingContainer` — A container whose header includes a machine-readable schema definition, decompression algorithm identifier, and integrity-check procedure, so any reader can unpack it without external documentation.
- `AppN.R1.b`: `BootstrapArchive` — An archive that contains not only crystal shards but also the code needed to mount, query, and verify them; opening the archive installs a minimal runtime environment.
- `AppN.R1.c`: `SchemaEvolutionEnvelope` — A container wrapper that carries multiple schema versions and a migration function between them, ensuring that archives written under old schemas remain readable under new ones.
- `AppN.R1.d`: `AutoDecompressingPacket` — A container that detects the recipient's available decompression codecs, selects the optimal one, and presents its contents in the most efficient format the recipient supports.

#### Facet 2 - Laws

- `AppN.R2.a`: `SelfDocumentationLaw` — A self-describing container must carry sufficient metadata that a reader with no prior knowledge of the format can parse the header, identify the schema, and begin reading shards.
- `AppN.R2.b`: `BootstrapSufficiencyLaw` — A bootstrap archive's embedded runtime must be sufficient to mount the archive, resolve any shard address, and verify shard integrity without depending on any external software.
- `AppN.R2.c`: `SchemaMigrationLaw` — A schema evolution envelope must guarantee lossless round-trip migration: `migrate(v_old → v_new) ∘ migrate(v_new → v_old)` must yield the original content for all valid shards.
- `AppN.R2.d`: `CodecNegotiationLaw` — An auto-decompressing packet must never send data in a codec the recipient cannot decode; the negotiation protocol must confirm codec support before transmission begins.

#### Facet 3 - Constructions

- `AppN.R3.a`: `SchemaEmbedder` — Takes a container and its schema definition, serializes the schema into the container header using a universal meta-schema, and appends the decompression algorithm as a portable bytecode snippet.
- `AppN.R3.b`: `BootstrapPackager` — Bundles a crystal archive with a minimal mount runtime compiled to WebAssembly, producing a single file that can be opened in any environment with a WASM executor.
- `AppN.R3.c`: `MigrationChainBuilder` — Given schema versions `v_1, ..., v_n`, constructs the chain of migration functions `v_i → v_{i+1}` and their inverses, and embeds the chain in a schema evolution envelope.
- `AppN.R3.d`: `CodecProber` — Queries the recipient environment for available decompression codecs, ranks them by decompression speed and ratio, and rewraps the container's payload in the optimal codec before sending.

#### Facet 4 - Certificates

- `AppN.R4.a`: `SchemaParsabilityCert` — Proves that a self-describing container's schema is parsable by a generic reader by exhibiting the parse tree produced from the header using only the universal meta-schema.
- `AppN.R4.b`: `BootstrapSelfTestCert` — Proves that a bootstrap archive's embedded runtime can mount and verify the archive by exhibiting the runtime's execution trace on the archive itself, showing successful shard resolution.
- `AppN.R4.c`: `MigrationRoundTripCert` — Proves lossless schema migration by exhibiting a test shard, migrating it forward and back through the version chain, and showing bitwise identity with the original.
- `AppN.R4.d`: `CodecCompatibilityCert` — Proves that the selected codec is supported by the recipient by exhibiting the codec negotiation handshake log and the successful test decompression of a probe payload.
