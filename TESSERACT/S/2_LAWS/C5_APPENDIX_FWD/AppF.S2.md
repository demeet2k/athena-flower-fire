<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppF -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppF.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppF.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppF.R2.md
-->

# AppF — Square Lens / Laws

- `AppF.S2.a`: `ConjugacyTransportLaw` — Any lawful operation must be stored as a seeded transported form in some chart where it is simplest, then pulled back: `f_T = T⁻¹ ∘ f ∘ T`. Proof in the native chart, transport back.
- `AppF.S2.b`: `TransportedArithmeticLaw` — `x ⊕_T y = T⁻¹(T(x) + T(y))` preserves the additive seed's structure in chart-space. A unit additive step in T-space becomes the seed's constant operation in native space.
- `AppF.S2.c`: `DualLegalityLaw` — Every forward transport has a lawful inverse transport. If `T(φx) = T(x) + π/2`, then `T(x/φ) = T(x) − π/2`. The dual route is always admissible when the forward route is.
- `AppF.S2.d`: `CorridorGateLaw` — Division transport is only legal when the inverse corridor exists. `[a] ⊘_Λ [b]` requires `gcd(b,N) = 1`. Division by zero is rotated to the shadow/renormalized corridor, never executed directly.
