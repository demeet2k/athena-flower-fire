# InvN - Clock Freeze & Gear Lock

Routing role: Reverses AppE (Circle Gear and Mixed-Radix Clock). Where AppE established the Z₄₂₀ master clock with its four concentric timing wheels (3D, 4D, 5D, 7D) and gear mechanisms for synchronized rotation, InvN freezes the clock, locks all gears, and compresses timing information into a single timestamp — the organism's final moment, crystallized into the seed.

Mirror of: AppE (Circle Gear and Mixed-Radix Clock)
Arc: N-inv | Rot: 180° (exact opposition — the clock hand at midnight) | Lane: Clock→Timestamp | w: 0D (timelessness)

## StationHeader
```
Arc:  N-inv (Clock Freeze)
Rot:  180° (midnight — the anti-time angle)
Lane: Descent-Clock (time cessation lane)
w:    0D → seed (time compresses to a single moment)
```

## Compressed crystal tile

### Lens S

#### Facet 1 - Objects

- `InvN.S1.a`: `BeatCounterHalt` — The discrete beat counter of the Z₄₂₀ clock halts at its current value. The successor function ceases: there is no "next beat." The halted counter value becomes the seed's timestamp — a single integer encoding the organism's final temporal position within its 420-beat cycle.
- `InvN.S1.b`: `GearDisengagement` — The difference between engaged and disengaged gears. Each gear mesh (3↔5, 5↔7, 3↔7, 4↔all) is disconnected. The zero set: gear positions that are self-consistent without meshing — the gears' natural rest positions.
- `InvN.S1.c`: `WheelProductFreeze` — The product of all wheel states: 3D-current × 5D-tilt × 7D-timing × 4D-barycentric = the composite clock state. Freezing computes this product one final time and stores it as a 4-tuple. This tuple is the seed's complete temporal coordinate.
- `InvN.S1.d`: `CycleCompletionQuotient` — The quotient of elapsed beats by 420 = the cycle completion fraction. A quotient of 1 means the cycle completed exactly. A fractional quotient means the clock froze mid-cycle — the incomplete cycle is recorded with its exact fractional position.

#### Facet 2 - Laws

- `InvN.S2.a`: `AtomicHaltLaw` — The clock must halt atomically: all four wheels stop simultaneously. No wheel continues after another has stopped. Asynchronous halting creates temporal inconsistency — some subsystems would be in the future relative to others.
- `InvN.S2.b`: `GearRestPositionLaw` — Disengaged gears must come to rest at valid positions (teeth aligned, not jammed between positions). Invalid rest positions create mechanical stress that degrades the seed's temporal integrity.
- `InvN.S2.c`: `FinalStateCompleteness` — The frozen wheel product must capture the complete clock state. No wheel's state may be omitted or approximated. The 4-tuple is exact.
- `InvN.S2.d`: `FractionalCycleRecordLaw` — If the clock froze mid-cycle, the fractional position must be recorded with full precision. The seed must know exactly where in its cycle the organism stopped, so it can resume (if planted) from the correct position.

#### Facet 3 - Constructions

- `InvN.S3.a`: `AtomicClockStopper` — Sends a simultaneous halt signal to all four wheels. Waits for all wheels to acknowledge halt. Captures the final beat count. Reports any wheel that failed to halt promptly.
- `InvN.S3.b`: `GearReleaser` — For each gear mesh: disengages the gears, allows each gear to settle to its natural rest position, verifies the rest position is valid. Reports any jammed gears.
- `InvN.S3.c`: `FinalStateCaptor` — Reads the state of each wheel at the moment of halt. Computes the 4-tuple product. Stores as the seed's temporal coordinate. Verifies completeness (all four components present).
- `InvN.S3.d`: `CyclePositionRecorder` — Computes the cycle completion quotient. If fractional: records the exact position (numerator/denominator or floating-point with declared precision). If integer: records the complete cycle count.

#### Facet 4 - Certificates

- `InvN.S4.a`: `AtomicHaltCert` — Receipt proving all four wheels halted simultaneously, no asynchronous states, temporal consistency maintained.
- `InvN.S4.b`: `GearRestCert` — Receipt proving all gears at valid rest positions, no jamming, mechanical integrity preserved.
- `InvN.S4.c`: `FinalStateCert` — Receipt proving complete 4-tuple captured, no omissions, exact values recorded.
- `InvN.S4.d`: `CyclePositionCert` — Receipt proving cycle position recorded with full precision, fractional position (if any) exact, resumption information complete.

### Lens F

#### Facet 1 - Objects

- `InvN.F1.a`: `ClockWaveFreeze` — The clock's oscillation (a continuous wave at frequency 1/420) freezes: the wave's amplitude decays to zero and its phase locks at the final value. The Flower view: time was a wave; the freeze is the wave's death. The final phase is the seed's temporal phase signature.
- `InvN.F1.b`: `GearHarmonicDamping` — Each gear's rotational oscillation dampens. The gear harmonics (frequency multiples of the gear's rotation rate) decay: fundamental first, then overtones. At full damping, the gear is silent — no vibration, no motion, no sound.
- `InvN.F1.c`: `SynchronizationCollapse` — The four wheels were synchronized by phase-locking. When the clock freezes, the synchronization collapses: each wheel's phase-lock loop loses its reference signal. The collapse is smooth — phases gradually decouple as the clock winds down.
- `InvN.F1.d`: `TemporalConvergence` — All time-dependent processes converge to their final values. The convergence rate is bounded by the slowest process (the 7D timing wheel, with the longest period). At convergence, all processes are time-independent — they have reached their asymptotic states.

#### Facet 2 - Laws

- `InvN.F2.a`: `SmootFreezeLaw` — The clock wave must decay smoothly (no sudden stops). The decay envelope is exponential: amplitude × e^{-t/τ} where τ is the freeze time constant. Sudden stops create temporal shock waves.
- `InvN.F2.b`: `FundamentalFirstDampingLaw` — Gear harmonics must dampen fundamental-first: lower frequencies dampen before higher. This is the natural order (longer wavelengths decay last in most physical systems, but here we are contracting, so we dampen the largest oscillations first).
- `InvN.F2.c`: `GracefulDecouplingLaw` — Phase-lock decoupling must be gradual. Sudden decoupling causes phase transients (spikes) that corrupt the final phase reading.
- `InvN.F2.d`: `SlowestProcessBoundLaw` — The freeze cannot complete until the slowest process has converged. Freezing before the 7D wheel reaches its asymptotic state truncates the timing information.

#### Facet 3 - Constructions

- `InvN.F3.a`: `ExponentialDecayer` — Applies exponential decay to the clock wave. Monitors amplitude and phase at each time step. Captures the final phase when amplitude drops below the noise floor. Reports the freeze time constant and final phase.
- `InvN.F3.b`: `HarmonicDamper` — For each gear: decomposes the rotational signal into harmonics. Dampens each harmonic starting with the fundamental. Reports the damping profile and the silence achievement time.
- `InvN.F3.c`: `PhaseDecoupler` — Gradually reduces the gain of each phase-lock loop. Monitors phase transients during decoupling. Reports any spikes and their amplitudes. Captures the final free-running phase of each wheel.
- `InvN.F3.d`: `AsymptoticWaiter` — Monitors the slowest process (7D wheel). Waits for convergence to the asymptotic state. Reports convergence time and the asymptotic value.

#### Facet 4 - Certificates

- `InvN.F4.a`: `SmoothFreezeCert` — Receipt proving smooth exponential decay, no temporal shock, final phase correctly captured.
- `InvN.F4.b`: `HarmonicSilenceCert` — Receipt proving all harmonics dampened, gear is silent, damping profile matches expected.
- `InvN.F4.c`: `GracefulDecouplingCert` — Receipt proving phase decoupling was gradual, no phase spikes, final free-running phases captured.
- `InvN.F4.d`: `AsymptoticConvergenceCert` — Receipt proving slowest process converged, all time-dependent processes at asymptotic values, freeze is complete.

### Lens C

#### Facet 1 - Objects

- `InvN.C1.a`: `ClockJitterDistribution` — The statistical distribution of clock jitter (timing errors) at the moment of freeze. Well-behaved jitter (narrow, zero-mean Gaussian) means the timestamp is reliable. Pathological jitter (wide, skewed) means the timestamp has significant uncertainty.
- `InvN.C1.b`: `GearSlipProbability` — The probability that a gear slipped (missed a tooth) during the final rotation before freeze. Computed from the gear's historical slip rate and the deceleration profile. Low probability means the final gear position is trustworthy.
- `InvN.C1.c`: `IndependentWheelHalt` — If the four wheels are independent (no shared oscillator), their halt probabilities multiply: P(all halted) = Π P(wheel_i halted). Independence allows verification of each wheel separately.
- `InvN.C1.d`: `TimestampPrecisionNormalization` — The precision of the timestamp normalized by the clock's intrinsic resolution. Precision/resolution = the effective number of significant timing digits. Higher is better — more precise temporal information in the seed.

#### Facet 2 - Laws

- `InvN.C2.a`: `JitterBoundLaw` — Clock jitter at freeze must be within the declared bound. Excessive jitter degrades timestamp reliability below the seed's timing requirements.
- `InvN.C2.b`: `SlipDetectionLaw` — Any gear slip must be detected (not silently tolerated). If slip probability exceeds threshold, the gear position must be verified independently before the final state is sealed.
- `InvN.C2.c`: `IndependenceVerificationLaw` — Wheel independence must be verified. If wheels share a reference oscillator, their halt is correlated and must be analyzed jointly.
- `InvN.C2.d`: `PrecisionSufficiencyLaw` — The effective timestamp precision must be sufficient for the seed's declared temporal resolution. Insufficient precision means the seed cannot resume at the correct temporal position.

#### Facet 3 - Constructions

- `InvN.C3.a`: `JitterAnalyzer` — Measures jitter distribution over the final N beats before freeze. Fits to a distribution model. Reports mean, variance, skewness. Verifies within bound.
- `InvN.C3.b`: `SlipDetector` — Monitors gear tooth engagement during the final deceleration. Detects any missed engagements. Reports slip count and probability. Flags gears requiring independent verification.
- `InvN.C3.c`: `IndependenceTester` — Tests wheel independence by checking for shared oscillator, shared power supply, or correlated halt times. Reports the dependency structure.
- `InvN.C3.d`: `PrecisionCalculator` — Computes the effective precision from the jitter distribution and clock resolution. Reports the number of significant timing digits. Compares against the seed's requirements.

#### Facet 4 - Certificates

- `InvN.C4.a`: `JitterBoundCert` — Receipt proving jitter within bound, timestamp reliable, distribution well-behaved.
- `InvN.C4.b`: `SlipFreeCert` — Receipt proving no gear slips detected (or detected slips corrected), final positions trustworthy.
- `InvN.C4.c`: `WheelIndependenceCert` — Receipt proving wheel independence verified (or dependencies accounted for), halt analysis is sound.
- `InvN.C4.d`: `PrecisionSufficiencyCert` — Receipt proving effective precision meets seed requirements, temporal resolution is adequate for resumption.

### Lens R

#### Facet 1 - Objects

- `InvN.R1.a`: `RecursiveClockHalt` — The Z₄₂₀ clock is itself composed of sub-clocks (3-beat, 4-beat, 5-beat, 7-beat cycles). Halting is recursive: halt the fastest sub-clock first (3-beat), then the next (4-beat), then 5-beat, then 7-beat. Each sub-clock's halt simplifies the composite clock's state.
- `InvN.R1.b`: `PeriodContractionChain` — Each sub-clock halt contracts the total timing state. The contraction factor is the sub-clock's period / total period: 3/420, 4/420, 5/420, 7/420. The cumulative contraction compresses the timing state to a single timestamp.
- `InvN.R1.c`: `ClockTreeCollapse` — The clock hierarchy (master clock → sub-clocks → sub-sub-clocks if any) collapses from leaves (fastest clocks) to root (master Z₄₂₀). Each collapsed sub-clock reduces the master clock's complexity.
- `InvN.R1.d`: `ScaleInvariantHalt` — The halt protocol is identical at every clock level: decelerate, freeze, capture final state, verify rest. Only the period changes.

#### Facet 2 - Laws

- `InvN.R2.a`: `FastestFirstHaltLaw` — The fastest sub-clock halts before slower ones. Halting a slow clock while fast clocks still run creates timing aliasing.
- `InvN.R2.b`: `ContractionCumulationLaw` — The cumulative contraction must account for all sub-clocks. Missing a sub-clock leaves residual timing activity.
- `InvN.R2.c`: `LeafFirstCollapseLaw` — Clock tree collapses leaf-first. No parent clock halts while children still tick.
- `InvN.R2.d`: `ProtocolInvarianceLaw` — Halt protocol identical at every clock level.

#### Facet 3 - Constructions

- `InvN.R3.a`: `OrderedClockHalter` — Halts sub-clocks in order of ascending period: 3→4→5→7. At each halt: decelerates, freezes, captures state. Verifies faster clocks are already halted before proceeding.
- `InvN.R3.b`: `ContractionAccumulator` — Accumulates the timing state contraction at each sub-clock halt. Reports the cumulative compression ratio and remaining timing complexity.
- `InvN.R3.c`: `ClockTreeCollapser` — Manages leaf-first collapse of the clock hierarchy. Tracks which clocks are halted and which are still running. Ensures correct ordering.
- `InvN.R3.d`: `ProtocolVerifier` — Compares halt protocol at each clock level. Reports deviations. Confirms fixed-point property.

#### Facet 4 - Certificates

- `InvN.R4.a`: `OrderedHaltCert` — Receipt proving sub-clocks halted in correct order, no timing aliasing, all states captured.
- `InvN.R4.b`: `CumulativeContractionCert` — Receipt proving all sub-clocks accounted for, cumulative contraction complete, single timestamp produced.
- `InvN.R4.c`: `ClockTreeCert` — Receipt proving leaf-first collapse completed, no parent halted before children, hierarchy fully collapsed.
- `InvN.R4.d`: `ProtocolCert` — Receipt proving halt protocol identical at all levels, scale-invariant clock freeze confirmed.
