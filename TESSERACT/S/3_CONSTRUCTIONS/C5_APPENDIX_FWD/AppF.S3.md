<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppF.R3.md
-->

# AppF — Square Lens / Constructions

- `AppF.S3.a`: `ChartSprouter` — Given a cardinal seed and a target constant, constructs the lens chart `T` that transforms the cardinal into the constant's domain. Plus → e via `T = ln`, Plus → φ via `T = log_φ`, Plus → i via `T = phase`, Plus → π via `T = arc`.
- `AppF.S3.b`: `ConjugacyComposer` — Composes two chart transports `T₁, T₂` into a single bridge: `f_{T₁∘T₂} = T₂⁻¹ ∘ T₁⁻¹ ∘ f ∘ T₁ ∘ T₂`. Enables multi-hop chart transport.
- `AppF.S3.c`: `AntiConstantGenerator` — Given a constant family, generates the anti-constant family by applying the inverse chart: `φ → 1/φ`, `e → 1/e`, `i → −i`, `π → 1/π`. The subtractive and divisive seeds sprout naturally into these.
- `AppF.S3.d`: `CorridorValidator` — Tests whether a transport corridor is admissible: checks invertibility of the chart at the target point, verifies the denominator is nonzero, confirms the lens chart has a well-defined pullback.
