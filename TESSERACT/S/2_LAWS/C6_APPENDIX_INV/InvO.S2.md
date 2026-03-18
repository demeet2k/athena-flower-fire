<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvO -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvO.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvO.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvO.R2.md
-->

# InvO — Square Lens / Laws

- `InvO.S2.a`: `FixedPointStabilityLaw` — The transport fixed point must be stable: small perturbations return to the fixed point. An unstable fixed point would allow transport to restart spontaneously, violating the stillness condition.
- `InvO.S2.b`: `ConjugacyUniquenessLaw` — The universal representation (where all conjugacies collapse) must be unique. If multiple representations survive collapse, the conjugacy bridges between them are essential (not collapsible) and must be preserved in the seed.
- `InvO.S2.c`: `DualityResolutionLaw` — Every dual move must be resolved to a single direction (or null). No duality survives in the seed. The resolution must be consistent: if move A→B is classified as forward, then B→A must be classified as backward.
- `InvO.S2.d`: `TrivialRotationLaw` — All rotation angles must collapse to zero modulo 2π. Any non-zero residual angle indicates incomplete transport collapse.
