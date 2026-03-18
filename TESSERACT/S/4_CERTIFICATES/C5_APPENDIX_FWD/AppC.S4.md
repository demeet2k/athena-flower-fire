<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppC -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppC.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppC.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppC.R4.md
-->

# AppC — Square Lens / Certificates

- `AppC.S4.a`: `SuccessorReplayCert` — Proves: successor well-defined, domain closed under increment, one-step difference preserved, replay deterministic. Minimal cert for the additive seed.
- `AppC.S4.b`: `ZeroWitnessCert` — Proves: difference well-defined, zero set correctly computed, fixed-point or period witness valid, replay of root/equality detection correct.
- `AppC.S4.c`: `ProductBindingCert` — Proves: chart admissibility, product well-defined in chart, count/phase/probability/recursion invariant preserved, factorization/binding/route composition replayable.
- `AppC.S4.d`: `BézoutInverseCert` — Proves: `gcd(b,N) = 1`, `x = b⁻¹ mod N` via EEA, `ax ≡ a/b (mod N)`. The gate witness for lawful division. When gcd fails, the cert records "no inverse corridor exists."
