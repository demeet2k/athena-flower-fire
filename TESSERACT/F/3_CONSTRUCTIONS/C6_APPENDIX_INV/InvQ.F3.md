<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvQ.R3.md
-->

# InvQ — Flower Lens / Constructions

- `InvQ.F3.a`: `DeformationRetracter` — Constructs the deformation retraction: a family of maps h_t (t ∈ [0,1]) where h_0 = identity, h_1 = retraction to skeleton, and h_t is continuous. Verifies continuity at each time step.
- `InvQ.F3.b`: `PhaseDecayer` — Applies exponential decay to each coupling's phase. Monitors decay rate. Flags couplings with sub-exponential decay for information-absorption remediation.
- `InvQ.F3.c`: `LaplacianSpectralAnalyzer` — Computes the Laplacian eigenfunctions of the topology. Identifies the spectral gap. Classifies modes as essential (below gap) or redundant (above gap). Prunes redundant modes.
- `InvQ.F3.d`: `CurvatureRedistributor` — Tracks total curvature during contraction. Verifies Gauss-Bonnet conservation at each step. Reports curvature distribution on the skeleton.
