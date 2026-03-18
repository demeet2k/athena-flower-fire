<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvX.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvX.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvX.C1.md
-->

# InvX — Fractal Lens / Objects

- `InvX.R1.a`: `RecursiveBundleDisassembly` — A bundle may contain sub-bundles (nested exports). Disassembly is recursive: unpack the outer bundle, find inner bundles, unpack those, and so on until atomic shards are reached. The recursion depth = the nesting depth of the export.
- `InvX.R1.b`: `NestingContractionFactor` — Each recursive unpacking level reduces the remaining bundle complexity by a contraction factor. The factor approaches 1/φ for well-structured bundles (golden-ratio nesting). Poorly structured bundles have irregular contraction.
- `InvX.R1.c`: `BranchReabsorptionTree` — The export tree (root bundle → sub-bundles → shards) is traversed leaf-first during absorption. Each leaf shard is absorbed, then its parent sub-bundle is dissolved, then the grandparent, up to the root. Multiplicative branching during export inverts to convergent absorption.
- `InvX.R1.d`: `ScaleIndependentAbsorption` — The absorption protocol is identical at every nesting level: unpack, verify, strip format, resolve references, merge version. Only the scale parameter changes. The protocol is a fixed point of the nesting transformation.
