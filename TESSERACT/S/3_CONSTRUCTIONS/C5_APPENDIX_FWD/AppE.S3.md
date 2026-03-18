<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppE.R3.md
-->

# AppE — Square Lens / Constructions

- `AppE.S3.a`: `QuarterTurnIterator` — Applies `z ↦ iz` repeatedly, tracking cycle position in `{0,1,2,3}`. Detects completion when position returns to 0. Generates the fundamental 4-tick clock.
- `AppE.S3.b`: `MixedRadixCounter` — Multi-digit counter with configurable moduli per position. Implements carry propagation. The 21-station chapter orbit is one digit; arc position (5 arcs) is another; quarter-turn is another.
- `AppE.S3.c`: `PhaseLockDetector` — Monitors two clocks' phase difference. Reports lock/unlock status. Triggers re-synchronization when drift exceeds declared tolerance.
- `AppE.S3.d`: `PolygonRefinementEngine` — Computes `n·sin(π/n)` for increasing n. Tracks convergence to π. Each step adds one polygon side = one more station in the discrete circle gear.
