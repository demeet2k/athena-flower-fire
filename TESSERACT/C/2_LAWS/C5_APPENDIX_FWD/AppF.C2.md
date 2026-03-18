<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppF.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppF.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppF.R2.md
-->

# AppF — Cloud Lens / Laws

- `AppF.C2.a`: `TransportConfidenceLaw` — Transport confidence must increase monotonically as charts are verified; a failed transport attempt reduces confidence in the specific corridor without affecting other corridors.
- `AppF.C2.b`: `ChartSelectionLaw` — The optimal chart for a given operation is the one that minimizes transported complexity; chart selection must consider all four lens options before committing.
- `AppF.C2.c`: `CorridorRiskBoundLaw` — Corridor risk must be bounded below a declared threshold before transport is attempted; exceeding threshold triggers shadow/renormalized resolution.
- `AppF.C2.d`: `DualRouteSymmetryLaw` — If forward transport has confidence p, backward transport must have confidence ≥ p·(1/φ); asymmetric dual routes indicate structural defect.
