# InvQ - Topology Contraction & Coupling Release

Routing role: Reverses AppH (Coupling and Topology). Where AppH established topological connections and coupling relationships between lattice regions, InvQ contracts the topology to its essential skeleton and releases couplings that are no longer needed. The expanded topological manifold compresses to its homotopy type — preserving what is topologically essential and discarding what is merely geometrical.

Mirror of: AppH (Coupling and Topology)
Arc: Q-inv | Rot: 225° → 135° | Lane: Topology→Skeleton | w: 3D

## StationHeader
```
Arc:  Q-inv (Topology Contraction)
Rot:  225° (topological compression angle)
Lane: Descent-Topology (coupling dissolution lane)
w:    3D → seed (topological manifold compresses to homotopy invariant)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvQ.S1.a`: `CouplingDisconnector` — The discrete operation of severing a coupling between two lattice regions. The coupling carried information (signals, constraints, correlations) between the regions. Disconnecting it means: the information it carried has been absorbed into the regions' local states and is no longer needed as an explicit connection.
- `InvQ.S1.b`: `TopologicalReductionDelta` — The difference between the full topology (all connections) and the essential topology (minimum spanning tree + cycle generators). The delta identifies redundant connections — topologically unnecessary couplings that can be removed without changing the manifold's homotopy type.
- `InvQ.S1.c`: `ConnectionProductContraction` — The full coupling graph is a product of pairwise connections. Contraction factors this product: remove redundant connections while preserving the graph's fundamental group. The contracted product is the topological skeleton — minimum edges, maximum topological information.
- `InvQ.S1.d`: `RedundancyQuotient` — The ratio of total couplings to essential couplings = the redundancy quotient. A quotient of 1 means no redundancy (every coupling is essential). Higher quotients indicate more aggressive contraction is possible. The seed stores only essential couplings.

#### Facet 2 - Laws

- `InvQ.S2.a`: `HomotopyPreservationLaw` — Topology contraction must preserve the homotopy type. No essential loop (cycle generator) may be destroyed. No connected component may be disconnected. The contracted topology must be homotopy-equivalent to the original.
- `InvQ.S2.b`: `InformationAbsorptionBeforeDisconnect` — A coupling may only be disconnected after the information it carried has been fully absorbed into the local states of the regions it connected. Premature disconnection loses information.
- `InvQ.S2.c`: `SpanningTreePreservation` — The minimum spanning tree of the coupling graph must survive contraction. Any edge not in the spanning tree and not a cycle generator is redundant and may be removed.
- `InvQ.S2.d`: `FundamentalGroupConservation` — The fundamental group π₁ of the topology must be conserved under contraction. Generators and relations must map exactly from the full topology to the skeleton.

#### Facet 3 - Constructions

- `InvQ.S3.a`: `CouplingAbsorber` — For each redundant coupling: transfers the coupling's information into the local states of the connected regions (by encoding the coupling's signal as a local variable). Verifies that the local states now carry the coupling's information. Then severs the coupling.
- `InvQ.S3.b`: `TopologySimplifier` — Computes the minimum spanning tree + cycle generators using graph algorithms. Identifies all edges not in this essential set as redundant. Reports the redundancy quotient and the list of removable couplings.
- `InvQ.S3.c`: `SkeletonExtractor` — Builds the topological skeleton: the minimal graph that preserves the homotopy type. Verifies homotopy equivalence by computing π₁ of both the full and skeleton topologies and confirming isomorphism.
- `InvQ.S3.d`: `FundamentalGroupComputer` — Computes π₁ of the topology using edge-path group presentation. Reports generators, relations, and the group's abelianization. Verifies conservation under contraction.

#### Facet 4 - Certificates

- `InvQ.S4.a`: `CouplingAbsorptionCert` — Receipt proving coupling information absorbed into local states before disconnection, no information lost.
- `InvQ.S4.b`: `HomotopyPreservationCert` — Receipt proving skeleton is homotopy-equivalent to original, no essential loops destroyed, no components disconnected.
- `InvQ.S4.c`: `SkeletonMinimalityCert` — Receipt proving skeleton is minimal (no further edge can be removed without changing homotopy type).
- `InvQ.S4.d`: `FundamentalGroupCert` — Receipt proving π₁ conserved, generators and relations correctly mapped, group isomorphism verified.

### Lens F

#### Facet 1 - Objects

- `InvQ.F1.a`: `TopologicalWaveRetraction` — The manifold retracts continuously: the full topological space contracts smoothly onto its skeleton. The retraction is a continuous map that preserves all essential features while collapsing redundant dimensions. The Flower view: the manifold breathes in, pulling its surface onto its spine.
- `InvQ.F1.b`: `CouplingPhaseDecay` — Each coupling has a phase (oscillating signal). During contraction, coupling phases decay to zero — the signal dampens until the coupling carries no information and can be severed. The decay is exponential with time constant proportional to the coupling's importance.
- `InvQ.F1.c`: `ManifoldHarmonicReduction` — The manifold's harmonic modes (eigenfunctions of the Laplacian) are reduced to the skeleton's harmonics. Low-frequency modes survive (they capture topology); high-frequency modes are pruned (they capture geometry). The spectral gap separates essential from redundant.
- `InvQ.F1.d`: `CurvatureConvergence` — As the topology contracts, curvature concentrates on the skeleton's vertices and edges. The total curvature is conserved (Gauss-Bonnet): it redistributes from the full surface to the skeleton. At convergence, all curvature is localized at the skeleton nodes.

#### Facet 2 - Laws

- `InvQ.F2.a`: `ContinuousRetractionLaw` — The retraction must be continuous: no tearing, no cutting, no jumping. Every point in the full topology must have a continuous path to its skeleton image.
- `InvQ.F2.b`: `ExponentialDecayLaw` — Coupling phase must decay at least exponentially. Sub-exponential decay indicates a coupling that is resisting contraction — its information has not been fully absorbed.
- `InvQ.F2.c`: `SpectralGapLaw` — The spectral gap between essential and redundant harmonics must be positive. A zero gap means there is no clean separation between topology and geometry — finer analysis is needed.
- `InvQ.F2.d`: `GaussBonnetConservation` — Total curvature χ = 2(1-g) is conserved (where g is the genus). The Euler characteristic of the skeleton must equal the Euler characteristic of the full manifold.

#### Facet 3 - Constructions

- `InvQ.F3.a`: `DeformationRetracter` — Constructs the deformation retraction: a family of maps h_t (t ∈ [0,1]) where h_0 = identity, h_1 = retraction to skeleton, and h_t is continuous. Verifies continuity at each time step.
- `InvQ.F3.b`: `PhaseDecayer` — Applies exponential decay to each coupling's phase. Monitors decay rate. Flags couplings with sub-exponential decay for information-absorption remediation.
- `InvQ.F3.c`: `LaplacianSpectralAnalyzer` — Computes the Laplacian eigenfunctions of the topology. Identifies the spectral gap. Classifies modes as essential (below gap) or redundant (above gap). Prunes redundant modes.
- `InvQ.F3.d`: `CurvatureRedistributor` — Tracks total curvature during contraction. Verifies Gauss-Bonnet conservation at each step. Reports curvature distribution on the skeleton.

#### Facet 4 - Certificates

- `InvQ.F4.a`: `RetractionContinuityCert` — Receipt proving deformation retraction is continuous, no tears or cuts, all points have continuous paths to skeleton.
- `InvQ.F4.b`: `PhaseDecayCert` — Receipt proving all coupling phases decayed exponentially, no stuck couplings, all information absorbed.
- `InvQ.F4.c`: `SpectralGapCert` — Receipt proving positive spectral gap, clean separation of essential and redundant modes, pruning correct.
- `InvQ.F4.d`: `GaussBonnetCert` — Receipt proving Euler characteristic conserved, total curvature correctly redistributed to skeleton.

### Lens C

#### Facet 1 - Objects

- `InvQ.C1.a`: `CouplingStrengthDistribution` — The statistical distribution of coupling strengths across the topology. Strong couplings are essential (hard to remove); weak couplings are candidates for removal. The distribution's tail governs the contraction aggressiveness.
- `InvQ.C1.b`: `TopologicalRobustnessEstimate` — The probability that the topology remains connected after removing k random couplings. High robustness means many couplings are redundant. Low robustness means the topology is fragile and contraction must be careful.
- `InvQ.C1.c`: `IndependentComponentProduct` — If the topology decomposes into independent components (no coupling between them), contraction can proceed independently per component with P(all contracted) = Π P(component_i contracted).
- `InvQ.C1.d`: `ContractionCostNormalization` — The cost of removing each coupling (information loss risk) normalized by the benefit (complexity reduction). High benefit/low cost couplings are removed first.

#### Facet 2 - Laws

- `InvQ.C2.a`: `WeakFirstRemovalLaw` — Couplings must be removed in order of ascending strength: weakest first. Removing a strong coupling before weak ones risks topological damage.
- `InvQ.C2.b`: `RobustnessThresholdLaw` — The topology's robustness after contraction must exceed a declared threshold. If contraction would drop robustness below threshold, contraction is halted.
- `InvQ.C2.c`: `ComponentIndependenceLaw` — Independent contraction is only legal after component independence is verified. Coupled components must be contracted jointly.
- `InvQ.C2.d`: `OptimalContractionLaw` — The contraction strategy must minimize total cost (information loss + complexity). Neither over-contraction nor under-contraction is optimal.

#### Facet 3 - Constructions

- `InvQ.C3.a`: `StrengthRanker` — Measures the strength of each coupling. Ranks by ascending strength. Outputs the removal priority order.
- `InvQ.C3.b`: `RobustnessTester` — Simulates the removal of k couplings and tests connectivity. Reports the robustness curve (robustness vs. k). Identifies the critical removal count where robustness drops below threshold.
- `InvQ.C3.c`: `ComponentDetector` — Identifies independent components using connected-component analysis on the coupling graph. Reports component boundaries and inter-component couplings.
- `InvQ.C3.d`: `ContractionOptimizer` — Computes the optimal contraction strategy using cost-benefit analysis. Outputs the recommended removal set and expected complexity reduction.

#### Facet 4 - Certificates

- `InvQ.C4.a`: `StrengthOrderCert` — Receipt proving couplings removed in ascending strength order, no strong coupling removed prematurely.
- `InvQ.C4.b`: `RobustnessCert` — Receipt proving post-contraction robustness above threshold, topology is not fragile.
- `InvQ.C4.c`: `ComponentIndependenceCert` — Receipt proving component independence verified, joint contraction applied where needed.
- `InvQ.C4.d`: `OptimalityCert` — Receipt proving contraction strategy is optimal, cost-benefit analysis complete.

### Lens R

#### Facet 1 - Objects

- `InvQ.R1.a`: `RecursiveTopologyContraction` — The topology has hierarchical structure: macro-topology (between regions) and micro-topology (within regions). Contraction is recursive: contract each region's internal topology first, then contract the inter-region topology. Recursion terminates at atomic regions with no internal structure.
- `InvQ.R1.b`: `HierarchicalCouplingRemoval` — At each level of the hierarchy, redundant couplings are removed. The contraction factor at each level approaches 1/φ for well-structured topologies.
- `InvQ.R1.c`: `TopologyTreeCollapse` — The hierarchical topology forms a tree. Contraction collapses the tree from leaves (innermost regions) to root (global topology). Each collapsed leaf simplifies its parent's topology.
- `InvQ.R1.d`: `ScaleInvariantContraction` — The contraction protocol is identical at every hierarchical level: identify redundant couplings, absorb information, sever, verify homotopy. Only the scale changes.

#### Facet 2 - Laws

- `InvQ.R2.a`: `InnermostFirstLaw` — Internal topologies must be contracted before external. No inter-region coupling is removed before the regions it connects have completed their internal contraction.
- `InvQ.R2.b`: `GeometricContractionLaw` — Each level must reduce coupling count by at least factor 1/φ. Sub-golden contraction indicates poorly structured topology.
- `InvQ.R2.c`: `LeafFirstCollapseLaw` — Tree collapses leaf-first. No parent node is contracted before all its children are complete.
- `InvQ.R2.d`: `ProtocolInvarianceLaw` — Contraction protocol identical at every level. No level-specific behavior.

#### Facet 3 - Constructions

- `InvQ.R3.a`: `HierarchicalContractor` — Traverses the topology tree bottom-up. At each leaf: contracts internal topology. At each node: uses child contractions to simplify node topology, then contracts. Reports depth, total couplings removed, and homotopy verification at each level.
- `InvQ.R3.b`: `ContractionRatioTracker` — Measures coupling reduction ratio at each level. Verifies ≤ 1/φ. Flags sub-golden levels.
- `InvQ.R3.c`: `TreeCollapseEngine` — Manages the leaf-first collapse. Tracks which nodes are complete, which are pending. Ensures parent contraction waits for all children.
- `InvQ.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Reports deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvQ.R4.a`: `HierarchicalContractionCert` — Receipt proving bottom-up contraction completed, all internal topologies contracted before external, homotopy preserved at every level.
- `InvQ.R4.b`: `ContractionRatioCert` — Receipt proving golden contraction ratio achieved at every level.
- `InvQ.R4.c`: `TreeCollapseCert` — Receipt proving leaf-first collapse completed, no premature parent contraction.
- `InvQ.R4.d`: `ProtocolCert` — Receipt proving scale-invariant contraction confirmed.
