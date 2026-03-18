# AppO - Publication Import/Export Bundles

Routing role: Publication bundles, import/export law, signed releases, and dissemination packets.

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `AppO.S1.a`: `JSONCrystalBundle` — A JSON document that serializes a crystal tile's 64 cells with their addresses, names, descriptions, and cross-references intact; the canonical machine-readable export format.
- `AppO.S1.b`: `MarkdownExport` — A human-readable markdown rendering of a crystal tile preserving the lens/facet/atom hierarchy as nested headers, with backtick names and long-dash descriptions matching the source format.
- `AppO.S1.c`: `CoordinatePreservingSerializer` — A serialization layer that guarantees every shard retains its full crystal coordinate `(Appendix.Lens.Facet.Atom)` through export and re-import, preventing address drift across systems.
- `AppO.S1.d`: `SignedReleaseBall` — A tarball of exported crystal content signed with the organism's release key, containing a manifest of included shards, their hashes, and the signature block for authenticity verification.

#### Facet 2 - Laws

- `AppO.S2.a`: `ExportIdempotencyLaw` — Exporting a crystal tile and immediately re-importing the result must yield a tile identical to the original; `import(export(T)) = T` for all valid tiles.
- `AppO.S2.b`: `AddressStabilityLaw` — An exported shard's crystal coordinate must not change across export formats; `addr(json_export(s)) = addr(markdown_export(s)) = addr(s)` for all shards `s`.
- `AppO.S2.c`: `FormatFidelityLaw` — Each export format must preserve all semantically significant content; format-specific decorations (syntax highlighting, indentation) are permitted but content loss is not.
- `AppO.S2.d`: `SignatureBindingLaw` — A signed release ball's signature covers the manifest hash, which in turn covers all included shard hashes; modifying any shard invalidates the signature without needing to re-verify all shards.

#### Facet 3 - Constructions

- `AppO.S3.a`: `JSONExporter` — Traverses a crystal tile's 64 cells, serializes each into a JSON object with fields `{address, name, description, lens, facet, atom}`, and assembles them into an array wrapped in a tile envelope.
- `AppO.S3.b`: `MarkdownRenderer` — Converts a crystal tile into a markdown document by emitting `#` headers for lenses, `##` for facets, and `- backtick` list items for atoms, reproducing the canonical appendix format.
- `AppO.S3.c`: `DiffExporter` — Computes the delta between two versions of a crystal tile and exports only the changed cells as a patch bundle, with before/after pairs and crystal coordinates for targeted re-import.
- `AppO.S3.d`: `ReleaseSigner` — Computes the shard-level hashes, assembles the manifest, computes the manifest hash, signs it with the release key, and packages everything into the signed release ball.

#### Facet 4 - Certificates

- `AppO.S4.a`: `ExportRoundTripCert` — Proves export idempotency by exhibiting the original tile hash, the exported bundle, the re-imported tile hash, and showing equality.
- `AppO.S4.b`: `AddressPreservationCert` — Proves address stability by exhibiting each shard's coordinate in the source tile and in every export format, showing identity across all representations.
- `AppO.S4.c`: `ContentPreservationCert` — Proves format fidelity by exhibiting a semantic diff between the source tile and the re-imported export, showing zero meaningful differences.
- `AppO.S4.d`: `ReleaseSignatureCert` — Proves release authenticity by exhibiting the public key, the manifest hash, and the signature verification result; valid only if `verify(pubkey, manifest_hash, sig) = true`.

### Lens F

#### Facet 1 - Objects

- `AppO.F1.a`: `SyncProtocol` — A bidirectional synchronization protocol that compares local and remote crystal tile versions, identifies divergent cells, and transmits only the deltas needed to reconcile them.
- `AppO.F1.b`: `DeltaUpdateStream` — A continuous stream of cell-level changes emitted by a crystal tile as it evolves, formatted as `(address, old_hash, new_hash, new_content)` tuples for incremental consumption by subscribers.
- `AppO.F1.c`: `ConflictFreeImporter` — An import engine that applies incoming shard updates using CRDT merge semantics: concurrent edits to the same cell are resolved by last-writer-wins with logical timestamps.
- `AppO.F1.d`: `ExportQueue` — A persistent ordered queue of pending export operations that ensures every tile mutation is eventually exported, even if the export target is temporarily unreachable.

#### Facet 2 - Laws

- `AppO.F2.a`: `SyncConvergenceLaw` — Two nodes running the sync protocol on the same tile must converge to identical state after exchanging all pending deltas; permanent divergence is a protocol violation.
- `AppO.F2.b`: `DeltaOrderingLaw` — Delta updates must be applied in causal order: if cell `A`'s new content references cell `B`, then `B`'s delta must be applied before `A`'s in any valid import sequence.
- `AppO.F2.c`: `MergeCommutativityLaw` — Conflict-free merge is commutative: `merge(delta_1, delta_2) = merge(delta_2, delta_1)` for all concurrent deltas, ensuring order-independent convergence.
- `AppO.F2.d`: `ExportDurabilityLaw` — Once an export operation is enqueued, it must eventually complete or be explicitly cancelled; silent drops are forbidden; the queue is durable across restarts.

#### Facet 3 - Constructions

- `AppO.F3.a`: `TreeDiffSynchronizer` — Computes a Merkle tree over both local and remote tiles, identifies the minimal subtree of differing cells by comparing intermediate hashes, and transmits only the divergent leaves.
- `AppO.F3.b`: `DeltaCompressor` — Groups consecutive delta updates to the same cell into a single compound delta that jumps directly from the initial to the final state, reducing transmission volume for burst edits.
- `AppO.F3.c`: `CRDTMergeEngine` — Maintains a vector clock per cell, tags each delta with its vector timestamp, and resolves concurrent writes by selecting the delta with the highest timestamp component for the originating node.
- `AppO.F3.d`: `RetryableExportWorker` — Dequeues export operations, attempts delivery with exponential backoff, and returns failed operations to the queue with incremented retry counters; dead-letters after configurable max retries.

#### Facet 4 - Certificates

- `AppO.F4.a`: `SyncConvergenceCert` — Proves that two nodes have converged by exhibiting both nodes' tile root hashes after sync completion and showing equality.
- `AppO.F4.b`: `CausalOrderCert` — Proves that deltas were applied in causal order by exhibiting the dependency graph and the application sequence, showing all edges point forward.
- `AppO.F4.c`: `MergeCorrectnessCert` — Proves that a conflict-free merge produced the correct result by exhibiting the concurrent deltas, their vector timestamps, and the selected winner for each conflicting cell.
- `AppO.F4.d`: `ExportCompletionCert` — Proves that every enqueued export operation completed by exhibiting the queue drain log with delivery confirmations for each operation.

### Lens C

#### Facet 1 - Objects

- `AppO.C1.a`: `MultiFormatPublisher` — A publication engine that takes a single crystal tile and simultaneously emits it as JSON, markdown, HTML, and structured data, each format generated from the same canonical internal representation.
- `AppO.C1.b`: `CodeExporter` — Generates executable code (Python, TypeScript) from a crystal tile's constructions facet, embedding the crystal coordinates as comments and the descriptions as docstrings.
- `AppO.C1.c`: `DataCatalogEntry` — A structured metadata record that describes a published crystal tile in terms discoverable by data catalogs: title, description, schema version, coordinate range, and access URL.
- `AppO.C1.d`: `CrossFormatLinker` — A reference table that maps each shard's crystal address to its location in every published format (JSON path, markdown line number, HTML anchor, code symbol), enabling cross-format navigation.

#### Facet 2 - Laws

- `AppO.C2.a`: `ContentInvarianceLaw` — All published formats must carry the same semantic content; differences are limited to format-specific presentation; `semantics(json) = semantics(markdown) = semantics(html) = semantics(code)`.
- `AppO.C2.b`: `CodeExecutabilityLaw` — Code generated by the code exporter must be syntactically valid and executable in its target language without modification; generated code that fails to parse is a publication error.
- `AppO.C2.c`: `CatalogDiscoverabilityLaw` — Every published tile must have a corresponding data catalog entry; unpublished catalog entries and uncatalogued publications are both violations.
- `AppO.C2.d`: `CrossFormatLinkConsistencyLaw` — The cross-format linker must map every shard address to a valid location in every published format; broken links indicate a synchronization failure between formats.

#### Facet 3 - Constructions

- `AppO.C3.a`: `SimultaneousPublisher` — Takes a crystal tile, runs all format-specific renderers in parallel, collects their outputs, and publishes them atomically so that all formats become available at the same instant.
- `AppO.C3.b`: `ConstructionCodeGenerator` — Extracts the Facet 3 (Constructions) cells from a crystal tile, generates a class or module for each construction with the crystal address as its identifier, and emits compilable source code.
- `AppO.C3.c`: `CatalogRegistrar` — Extracts metadata from a published tile, constructs a data catalog entry conforming to the catalog schema, and registers it with the discovery service.
- `AppO.C3.d`: `LinkTableBuilder` — After all formats are published, scans each format's output to locate every shard's rendered position, and assembles the cross-format link table mapping addresses to format-specific locations.

#### Facet 4 - Certificates

- `AppO.C4.a`: `MultiFormatConsistencyCert` — Proves that all published formats carry identical semantic content by exhibiting the canonical representation and a diff against each format's re-parsed content, showing zero semantic differences.
- `AppO.C4.b`: `CodeValidityCert` — Proves that generated code is syntactically valid by exhibiting the parser's success result for each generated source file in its target language.
- `AppO.C4.c`: `CatalogRegistrationCert` — Proves that a tile's catalog entry exists and is correctly populated by exhibiting the catalog query result and comparing it field-by-field against the tile's metadata.
- `AppO.C4.d`: `LinkIntegrityCert` — Proves that every cross-format link resolves correctly by exhibiting the resolution result for each shard address in each format, confirming no broken links.

### Lens R

#### Facet 1 - Objects

- `AppO.R1.a`: `SelfPublishingShard` — A shard that contains embedded publication logic: when invoked, it renders itself into all supported formats and emits the results without requiring an external publication engine.
- `AppO.R1.b`: `AutoBundleTile` — A crystal tile that monitors its own mutation history and automatically packages changed cells into a delta export bundle at configurable intervals, ready for distribution.
- `AppO.R1.c`: `PublicationManifestGenerator` — A module embedded in a crystal archive that, when triggered, scans all 64 cells, generates a publication manifest listing each cell's address, name, hash, and format availability.
- `AppO.R1.d`: `DistributionSeedCapsule` — A self-contained capsule that carries a crystal tile, its publication logic, and a list of distribution targets; opening the capsule triggers publication to all listed targets.

#### Facet 2 - Laws

- `AppO.R2.a`: `SelfPublicationFidelityLaw` — A self-publishing shard's output must be identical to what an external publication engine would produce for the same content; self-publication is an optimization, not a semantic change.
- `AppO.R2.b`: `AutoBundleCompletenessLaw` — An auto-bundle must include every cell that changed since the last bundle; skipped mutations accumulate and must appear in the next bundle; no change may be permanently lost.
- `AppO.R2.c`: `ManifestAccuracyLaw` — A generated publication manifest must accurately reflect the current state of all 64 cells; stale manifests that describe a prior tile version must be marked as superseded.
- `AppO.R2.d`: `DistributionAtomicityLaw` — A distribution seed capsule must publish to all listed targets or roll back; partial distribution (some targets updated, others not) is a violation requiring retry.

#### Facet 3 - Constructions

- `AppO.R3.a`: `EmbeddedRendererInjector` — Takes a shard and injects minimal rendering logic (markdown, JSON, HTML templates) as metadata, converting it into a self-publishing shard without altering its primary content.
- `AppO.R3.b`: `MutationWatcher` — A background process embedded in a crystal tile that tracks cell-level writes, maintains a dirty-cell bitmap, and triggers auto-bundling when the dirty count exceeds a threshold or a timer expires.
- `AppO.R3.c`: `ManifestRefresher` — Re-scans all 64 cells, computes current hashes, compares against the existing manifest, updates changed entries, increments the manifest version, and re-signs the manifest.
- `AppO.R3.d`: `FanoutDistributor` — Takes a distribution seed capsule, opens it, extracts the publication bundle and target list, and publishes to all targets in parallel with per-target retry logic and rollback on total failure.

#### Facet 4 - Certificates

- `AppO.R4.a`: `SelfPublicationMatchCert` — Proves that a self-publishing shard's output matches external publication by exhibiting both outputs and showing bitwise equality.
- `AppO.R4.b`: `AutoBundleCoverageCert` — Proves that an auto-bundle covers all mutations since the last bundle by exhibiting the mutation log, the dirty-cell bitmap at bundle time, and the bundle's included cell list.
- `AppO.R4.c`: `ManifestFreshnessCert` — Proves that a publication manifest is current by exhibiting each cell's live hash and the manifest's recorded hash, showing equality for all 64 cells.
- `AppO.R4.d`: `FullDistributionCert` — Proves that a distribution seed capsule published to all targets by exhibiting each target's delivery acknowledgment and the capsule's target list, showing complete coverage.
