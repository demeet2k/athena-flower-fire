<!-- TESSERACT: S/4_CERTIFICATES/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=S facet=4(Certificates) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.F4.md
#   C: ../../C/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.C4.md
#   R: ../../R/4_CERTIFICATES/C5_APPENDIX_FWD/AppO.R4.md
-->

# AppO — Square Lens / Certificates

- `AppO.S4.a`: `ExportRoundTripCert` — Proves export idempotency by exhibiting the original tile hash, the exported bundle, the re-imported tile hash, and showing equality.
- `AppO.S4.b`: `AddressPreservationCert` — Proves address stability by exhibiting each shard's coordinate in the source tile and in every export format, showing identity across all representations.
- `AppO.S4.c`: `ContentPreservationCert` — Proves format fidelity by exhibiting a semantic diff between the source tile and the re-imported export, showing zero meaningful differences.
- `AppO.S4.d`: `ReleaseSignatureCert` — Proves release authenticity by exhibiting the public key, the manifest hash, and the signature verification result; valid only if `verify(pubkey, manifest_hash, sig) = true`.
