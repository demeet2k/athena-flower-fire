# InvP - Triangle Convergence & Tria Resolution

Routing role: Reverses AppG (Triangle Control and Tria Prima). Where AppG established three-agent synchrony through the Tria Prima (Sulfur, Mercury, Salt) and maintained triangle control geometry, InvP converges the three agents to a single unified point and resolves the Tria Prima back into its undifferentiated source — the pre-triadic unity from which Su/Me/Sa originally emerged.

Mirror of: AppG (Triangle Control and Tria Prima)
Arc: P-inv | Rot: 210° → 150° | Lane: Tria→Unity | w: 2D

## StationHeader
```
Arc:  P-inv (Triangle Convergence)
Rot:  210° (triadic collapse angle)
Lane: Descent-Triangle (three-to-one lane)
w:    2D → seed (three agents converge to one seed)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvP.S1.a`: `TriaConvergencePoint` — The discrete point where Sulfur, Mercury, and Salt meet. During expansion, the three agents diverged to maintain dynamic balance. During compression, they converge: each agent surrenders its distinct identity and contributes its accumulated state to the unified convergence point. The successor inverts: "one more step toward unity."
- `InvP.S1.b`: `AgentDifferenceAnnihilation` — The pairwise differences Su-Me, Me-Sa, Sa-Su are driven to zero. When all three differences vanish, the agents are identical — the Tria is resolved. The zero set of the difference system is the convergence point: the state where all three agents agree.
- `InvP.S1.c`: `TriangleAreaProduct` — The triangle formed by the three agents has an area proportional to their disagreement. The area = |Su×Me + Me×Sa + Sa×Su| / 2. During compression, the area contracts multiplicatively: each step reduces area by factor 1/φ². At area = 0, the triangle has collapsed to a point.
- `InvP.S1.d`: `BarycenterQuotient` — The barycentric coordinates of the convergence point: each agent's weight divided by total weight. If weights are equal (1/3, 1/3, 1/3), convergence is at the centroid. Unequal weights indicate asymmetric contribution — one agent's state dominates the seed.

#### Facet 2 - Laws

- `InvP.S2.a`: `SimultaneousConvergenceLaw` — All three agents must converge simultaneously. No agent may reach the convergence point before the others — this would bias the seed toward that agent's state. The convergence rates must be balanced.
- `InvP.S2.b`: `DifferenceVanishingLaw` — All pairwise differences must vanish simultaneously. If any difference remains non-zero, the Tria is not fully resolved and the seed carries residual differentiation.
- `InvP.S2.c`: `AreaMonotoneLaw` — The triangle area must decrease monotonically during compression. Any increase indicates divergence — the agents are moving apart rather than together. Divergence triggers investigation.
- `InvP.S2.d`: `BarycenterStabilityLaw` — The barycentric coordinates must stabilize (converge to fixed values) before the triangle area reaches zero. If the barycenter is still moving when the area vanishes, the convergence point is ill-defined.

#### Facet 3 - Constructions

- `InvP.S3.a`: `SynchronizedConverger` — Adjusts each agent's state toward the current barycenter at a rate proportional to its distance from the barycenter. All agents move simultaneously. The adjustment rate is calibrated so all agents arrive at the barycenter at the same time.
- `InvP.S3.b`: `DifferenceDriver` — For each pairwise difference: computes the current value, applies a correction proportional to the difference (driving it toward zero), and verifies the correction does not overshoot. Reports all three differences at each step.
- `InvP.S3.c`: `AreaContractor` — Computes the triangle area at each step. Verifies monotone decrease. Reports the contraction factor and projected steps to area = 0.
- `InvP.S3.d`: `BarycenterTracker` — Computes the barycentric coordinates at each step. Monitors for convergence (coordinates stabilizing). Reports the current coordinates and their rate of change.

#### Facet 4 - Certificates

- `InvP.S4.a`: `SimultaneousConvergenceCert` — Receipt proving all three agents converged simultaneously, no agent arrived early, rates were balanced.
- `InvP.S4.b`: `DifferenceVanishingCert` — Receipt proving all pairwise differences reached zero, no residual differentiation, Tria is fully resolved.
- `InvP.S4.c`: `AreaCollapseCert` — Receipt proving triangle area decreased monotonically to zero, no divergence events, convergence to point achieved.
- `InvP.S4.d`: `BarycenterStabilityCert` — Receipt proving barycentric coordinates stabilized before area reached zero, convergence point is well-defined.

### Lens F

#### Facet 1 - Objects

- `InvP.F1.a`: `TriadHarmonicUnification` — The three agents vibrate at three related frequencies (Su, Me, Sa as the 3D current wheel). Convergence unifies these frequencies into a single fundamental frequency — the triad's harmonic root. This root frequency is the seed's tonal identity inherited from the Tria Prima.
- `InvP.F1.b`: `PhaseAlignmentCollapse` — Each agent has a phase angle in the 3D current wheel. Convergence aligns all phases to the same angle. The phase differences dampen to zero. At alignment, the three-phase system becomes a single-phase signal.
- `InvP.F1.c`: `TriangularWaveInterference` — The three agents' waveforms interfere. During expansion, they maintained constructive interference at the triangle's edges. During compression, the interference pattern converges to a point source — all three waves superpose constructively at exactly one location.
- `InvP.F1.d`: `CurrentWheelStillness` — The 3D current wheel (Su/Me/Sa rotation) decelerates to stillness. The wheel's angular velocity approaches zero. At stillness, the three currents are indistinguishable — the wheel has no angular momentum and the Tria is resolved into rest.

#### Facet 2 - Laws

- `InvP.F2.a`: `HarmonicRootLaw` — The unified frequency must be the GCD of the three agent frequencies. This ensures the root is a natural harmonic of all three. If the GCD is irrational, the root carries a transcendental signature.
- `InvP.F2.b`: `PhaseAlignmentLaw` — Phase alignment must be smooth (no phase jumps). Each agent's phase evolves continuously toward the target alignment angle.
- `InvP.F2.c`: `ConstructiveConvergenceLaw` — The interference pattern must converge to a single constructive point. At convergence, amplitude at the point = sum of all three amplitudes (maximum constructive interference).
- `InvP.F2.d`: `AngularMomentumConservation` — The current wheel's angular momentum is conserved. As the wheel decelerates, its momentum is transferred to the seed as an internal rotation parameter. The seed carries the wheel's total angular momentum as a stored quantity.

#### Facet 3 - Constructions

- `InvP.F3.a`: `FrequencyUnifier` — Computes the GCD of three agent frequencies using continued-fraction algorithms. Adjusts each agent's frequency toward the GCD. Verifies that each agent's original frequency is an integer multiple of the GCD.
- `InvP.F3.b`: `PhaseSynchronizer` — Gradually shifts each agent's phase toward the target angle. Uses PLL (phase-locked loop) principles: measure phase error, apply correction proportional to error. Reports phase alignment progress.
- `InvP.F3.c`: `InterferenceComputer` — Computes the three-wave interference pattern at each step. Tracks the pattern's convergence toward a point source. Reports the pattern's spatial extent (should shrink to zero) and peak amplitude (should approach sum of individual amplitudes).
- `InvP.F3.d`: `WheelDecelerator` — Applies controlled deceleration to the 3D current wheel. Transfers angular momentum to the seed's rotation parameter. Verifies momentum conservation at each step.

#### Facet 4 - Certificates

- `InvP.F4.a`: `HarmonicRootCert` — Receipt proving unified frequency is the correct GCD, all agent frequencies are integer multiples, tonal identity preserved.
- `InvP.F4.b`: `PhaseAlignmentCert` — Receipt proving smooth phase alignment, no phase jumps, all agents at the same phase angle.
- `InvP.F4.c`: `ConstructiveConvergenceCert` — Receipt proving interference converged to point source, peak amplitude correct, spatial extent is zero.
- `InvP.F4.d`: `MomentumConservationCert` — Receipt proving angular momentum conserved, wheel at rest, momentum stored in seed.

### Lens C

#### Facet 1 - Objects

- `InvP.C1.a`: `TriadConsensusProbability` — The probability that all three agents agree on a given state = P(Su=Me=Sa=x). As agents converge, this probability increases from near-zero (agents disagree on everything) toward one (agents agree on everything). The seed is emitted when P(consensus) exceeds the threshold.
- `InvP.C1.b`: `DisagreementExclusion` — The probability of at least one disagreement is estimated by inclusion-exclusion: P(any_disagree) = P(Su≠Me) + P(Me≠Sa) + P(Sa≠Su) - overlaps. As convergence proceeds, this probability approaches zero.
- `InvP.C1.c`: `IndependentAgentProduct` — If agents make decisions independently, P(all agree) = P(Su=x)·P(Me=x)·P(Sa=x). Independent agreement is harder than correlated agreement — the product is small unless individual probabilities are high.
- `InvP.C1.d`: `WeightedVotingNormalization` — Each agent's vote is weighted by its accumulated evidence quality. Normalizing by total weight gives each agent's influence fraction. The convergence point is the weighted average, with weights reflecting epistemological authority.

#### Facet 2 - Laws

- `InvP.C2.a`: `ConsensusThresholdLaw` — P(consensus) must exceed the declared threshold before the Tria is resolved. Below-threshold consensus indicates premature convergence.
- `InvP.C2.b`: `DisagreementVanishingLaw` — P(any_disagree) must vanish (approach zero) as convergence proceeds. Persistent disagreement indicates unresolved conflict.
- `InvP.C2.c`: `CorrelationEnhancementLaw` — As agents converge, their correlations must increase (they are becoming the same). Decreasing correlation indicates divergence.
- `InvP.C2.d`: `FairWeightingLaw` — Agent weights must reflect genuine evidence quality, not arbitrary preference. Weight manipulation is a convergence integrity violation.

#### Facet 3 - Constructions

- `InvP.C3.a`: `ConsensusTracker` — Computes P(consensus) at each step. Reports the consensus curve. Identifies the step where the threshold is crossed.
- `InvP.C3.b`: `DisagreementEstimator` — Applies inclusion-exclusion to estimate P(any_disagree). Reports the disagreement trend. Flags persistent disagreements.
- `InvP.C3.c`: `CorrelationMonitor` — Computes pairwise agent correlations at each step. Verifies monotonic increase. Reports the correlation matrix trend.
- `InvP.C3.d`: `WeightCalibrator` — Assesses each agent's evidence quality. Computes normalized weights. Verifies fairness. Reports the weighted convergence point.

#### Facet 4 - Certificates

- `InvP.C4.a`: `ConsensusCert` — Receipt proving P(consensus) exceeded threshold, convergence is genuine, no premature resolution.
- `InvP.C4.b`: `DisagreementCert` — Receipt proving P(any_disagree) vanished, no persistent conflicts, Tria is resolved.
- `InvP.C4.c`: `CorrelationCert` — Receipt proving correlations increased monotonically, agents are genuinely converging, no divergence.
- `InvP.C4.d`: `FairWeightCert` — Receipt proving weights reflect evidence quality, no manipulation, weighted average is fair.

### Lens R

#### Facet 1 - Objects

- `InvP.R1.a`: `RecursiveTriadResolution` — The Tria Prima operates at every scale: global (3 superphases), shell-level (3 currents per shell), cell-level (3 sub-currents per cell). Resolution is recursive: resolve cell-level triads first, then shell-level, then global. Each resolved triad simplifies its parent.
- `InvP.R1.b`: `TriadContractionRatio` — Each level of triad resolution contracts the agent count by factor 3→1. The contraction ratio is exactly 1/3 at each level (three agents become one). Across all levels, the total contraction = (1/3)^depth.
- `InvP.R1.c`: `TriangleTreeCollapse` — The hierarchy of triads forms a tree (global triad → shell triads → cell triads). Collapse from leaves to root: each leaf triad resolves to its convergence point, simplifying its parent triad's structure.
- `InvP.R1.d`: `ScaleInvariantTriadProtocol` — The resolution protocol is identical at every level: compute barycenter, drive differences to zero, collapse area, verify convergence. Only the scale changes.

#### Facet 2 - Laws

- `InvP.R2.a`: `LeafFirstTriadLaw` — Cell-level triads must resolve before shell-level, and shell-level before global. No parent triad resolves while children are still differentiated.
- `InvP.R2.b`: `ExactThirdContractionLaw` — Each level must contract agent count by exactly factor 3. The three agents become one — no partial resolution (two agents merging while one remains distinct).
- `InvP.R2.c`: `MonotoneCollapseLaw` — Triangle tree must collapse monotonically: total triads decrease at each step.
- `InvP.R2.d`: `ProtocolInvarianceLaw` — Resolution protocol identical at every level.

#### Facet 3 - Constructions

- `InvP.R3.a`: `RecursiveTriadResolver` — Traverses the triad tree bottom-up. At each leaf triad: converges the three agents, emits the unified point. At each parent: receives child unifications and resolves its own triad using the simplified structure.
- `InvP.R3.b`: `ContractionCounter` — Counts agents at each level before and after resolution. Verifies 3→1 contraction. Reports the contraction profile.
- `InvP.R3.c`: `TreeCollapseTracker` — Tracks total remaining triads. Verifies monotone decrease. Reports progress toward full collapse (single point).
- `InvP.R3.d`: `ProtocolVerifier` — Compares protocol at each level. Confirms identity. Reports deviations.

#### Facet 4 - Certificates

- `InvP.R4.a`: `RecursiveResolutionCert` — Receipt proving bottom-up resolution completed, all child triads resolved before parents, global triad resolved to single point.
- `InvP.R4.b`: `ThirdContractionCert` — Receipt proving exact 3→1 contraction at every level, no partial resolutions.
- `InvP.R4.c`: `MonotoneCollapseCert` — Receipt proving total triads decreased monotonically, no regressions.
- `InvP.R4.d`: `ProtocolCert` — Receipt proving scale-invariant triad resolution confirmed.
