<!-- TESSERACT: S/4_CERTIFICATES/C6_APPENDIX_INV/InvV -->
<!-- COORD: lens=S facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvV.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvV.C4.md
#   R: ../../R/4_CERTIFICATES/C6_APPENDIX_INV/InvV.R4.md
-->

# InvV — Square Lens / Certificates

- `InvV.S4.a`: `DigestFidelityCert` — Receipt proving digest correctly summarizes the full replay, any step is verifiable from its Merkle path, no step was omitted.
- `InvV.S4.b`: `DeviationClassificationCert` — Receipt proving all deviations classified, environmental deviations bounded, no logical deviations detected (or all logical deviations documented).
- `InvV.S4.c`: `CapsuleCompositionCert` — Receipt proving capsule composition is associative, master attestation correctly formed, all individual capsule properties preserved in the composite.
- `InvV.S4.d`: `CompressionBoundCert` — Receipt proving compression quotient within entropy bound, no information silently dropped, digest is faithful within declared tolerance.
