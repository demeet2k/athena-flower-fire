<!-- TESSERACT: R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=R facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.S3.md
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.C3.md
-->

# AppF — Fractal Lens / Constructions

- `AppF.R3.a`: `NestedChartExpander` — Recursively applies chart transport to generate depth-indexed lens families; computes `T^n(x)` for declared depth n.
- `AppF.R3.b`: `ScaleLatticeBuilder` — Builds the self-similar transport lattice `{φ^k · x_0}` from the φ-lens chart; generates entire constant families.
- `AppF.R3.c`: `LogPeriodicDetector` — Detects log-periodic oscillations in data and identifies the governing scaling constant by period analysis.
- `AppF.R3.d`: `RGFlowIterator` — Iterates the RG transport chain toward fixed point; detects convergence, universality class, and contraction ratio.
