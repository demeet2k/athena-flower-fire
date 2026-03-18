<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppF.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppF.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppF.R4.md
-->

# AppF — Square Lens / Certificates

- `AppF.S4.a`: `ChartAdmissibilityCert` — Proves: lens chart `T` is invertible, domain/range well-defined, transported arithmetic preserves the seed's algebraic identity.
- `AppF.S4.b`: `ConjugacyPreservationCert` — Proves: `f_T = T⁻¹ ∘ f ∘ T` correctly transports the seed operation, replay in native chart matches replay in transported chart.
- `AppF.S4.c`: `DualRouteCert` — Proves: forward and backward routes are both admissible, anti-constant family correctly generated, no corridor violation in either direction.
- `AppF.S4.d`: `CorridorIntegrityCert` — Proves: corridor test passed (or recorded failure), no division by zero attempted, shadow/renormalized resolution used when gate is closed.
