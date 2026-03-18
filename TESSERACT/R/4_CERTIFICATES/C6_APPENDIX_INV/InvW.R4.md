<!-- TESSERACT: R/4_CERTIFICATES/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=R facet=4(Certificates) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/4_CERTIFICATES/C6_APPENDIX_INV/InvW.S4.md
#   F: ../../F/4_CERTIFICATES/C6_APPENDIX_INV/InvW.F4.md
#   C: ../../C/4_CERTIFICATES/C6_APPENDIX_INV/InvW.C4.md
-->

# InvW — Fractal Lens / Certificates

- `InvW.R4.a`: `DepthFirstCert` — Receipt proving depth-first unwinding completed, all leaves before parents, no partial unwrappings.
- `InvW.R4.b`: `MonotoneDepthCert` — Receipt proving nesting depth decreased monotonically, no skips or new nesting created.
- `InvW.R4.c`: `FiniteNestingCert` — Receipt proving total depth within bound, no infinite nesting, all levels accounted for.
- `InvW.R4.d`: `ProtocolInvarianceCert` — Receipt proving protocol identical at every level, no format inconsistencies, fixed-point property holds.
