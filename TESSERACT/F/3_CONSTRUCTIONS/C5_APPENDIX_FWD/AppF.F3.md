<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.R3.md
-->

# AppF — Flower Lens / Constructions

- `AppF.F3.a`: `PhiLadderGenerator` — Generates the complete preimage ladder from the φ-lens: `x_k = T⁻¹(θ + kπ/2) = φ^(2θ/π) · φ^k`. Produces entire constant families by transport from a simple chart-space lattice.
- `AppF.F3.b`: `ExponentialFlowGenerator` — Generates the exponential flow family: `x(t) = x₀ · e^t` via continuous transport in ln-chart. The semigroup of growth operators.
- `AppF.F3.c`: `FourierKernelGenerator` — Generates the Fourier basis `{e^{inθ}}` from repeated phase transport. Spectral decomposition as iterated quarter-turn composition.
- `AppF.F3.d`: `PolygonClosureGenerator` — Generates the polygon sequence `n·sin(π/n)` converging to π. Leibniz accumulation, orthogonality normalization, and curvature integral.
