<!-- TESSERACT: S/4_CERTIFICATES/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=S facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvW.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvW.C4.md
#   R: ../../R/4_CERTIFICATES/C6_APPENDIX_INV/InvW.R4.md
-->

# InvW — Square Lens / Certificates

- `InvW.S4.a`: `HeaderStripCert` — Receipt proving header was valid, checksums matched, stripping completed cleanly, raw payload is intact.
- `InvW.S4.b`: `CleanDetachCert` — Receipt proving all I/O flushed, all handles closed, no cached data lost, mountpoint is clean.
- `InvW.S4.c`: `LayerPeelCert` — Receipt proving layers peeled in correct reverse order, all deltas computed and archived, base hash matches after full peel.
- `InvW.S4.d`: `DeltaExactnessCert` — Receipt proving all overlay deltas exact, no residuals after subtraction, no missing layers detected.
