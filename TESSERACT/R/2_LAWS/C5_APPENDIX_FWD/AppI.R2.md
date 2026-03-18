<!-- TESSERACT: R/2_LAWS/C5_APPENDIX_FWD/AppI -->
<!-- COORD: lens=R facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppI.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppI.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppI.C2.md
-->

# AppI — Fractal Lens / Laws

- `AppI.R2.a`: `RecursiveCorridorConsistencyLaw` — Corridor status at depth n must be consistent with corridor status at depth n−1. A corridor cannot be open at one depth and closed at the same depth's parent.
- `AppI.R2.b`: `FractalTruthConsistencyLaw` — Truth tags at depth n must not contradict truth tags at depth n−1. Promotion at one depth requires consistency check at adjacent depths.
- `AppI.R2.c`: `EvidenceAccumulationDepthLaw` — Evidence accumulated at depth n is valid as input at depth n+1 only if it carries a depth-n certification. Uncertified evidence cannot propagate upward.
- `AppI.R2.d`: `CorridorScalingLaw` — Admissibility thresholds scale by φ between levels: level n+1 threshold = φ × level n threshold. This ensures corridors tighten as governance deepens.
