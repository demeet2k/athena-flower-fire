<!-- TESSERACT: C/2_LAWS/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=C facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvV.S2.md
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvV.F2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvV.R2.md
-->

# InvV — Cloud Lens / Laws

- `InvV.C2.a`: `SamplingConfidenceLaw` — The sample size k must be sufficient to achieve the declared confidence level. The relationship: k ≥ ln(1-confidence) / ln(1-p). Under-sampling is a certification violation.
- `InvV.C2.b`: `MinimalCoverageLaw` — The non-redundant capsule core must cover all declared verification properties. Releasing a capsule that breaks coverage is illegal. Coverage is checked before each release.
- `InvV.C2.c`: `IndependenceBeforeReleaseLaw` — Independent release is only legal after independence is verified. If properties are dependent, their capsules must be released together or not at all.
- `InvV.C2.d`: `OptimalReleaseOrderLaw` — Capsules must be released in order of ascending value/cost ratio. Releasing a high-value capsule before a low-value one wastes verification resources.
