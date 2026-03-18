<!-- TESSERACT: R/1_OBJECTS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=R facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C6_APPENDIX_INV/InvW.S1.md
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvW.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvW.C1.md
-->

# InvW — Fractal Lens / Objects

- `InvW.R1.a`: `RecursiveContainerUnwinding` — Containers may nest (a container within a container). Unwinding is recursive: unwind the outer container, discover inner containers, unwind those. The recursion terminates at atomic content (raw shards with no container wrapper).
- `InvW.R1.b`: `NestingDepthContraction` — Each unwinding level reduces nesting depth by 1. The contraction factor is 1/(current_depth), which increases as depth decreases — unwinding accelerates as it approaches the base. This is the inverse of the logarithmic slowdown during deep packaging.
- `InvW.R1.c`: `ContainerTreeTraversal` — The nesting structure forms a tree. Unwinding traverses the tree from leaves (deepest nested containers) to root (outermost container). At each node, the container wrapper is dissolved and its children are exposed. Multiplicative nesting inverts to sequential exposure.
- `InvW.R1.d`: `ScaleInvariantUnwinding` — The unwinding protocol is the same at every nesting level: validate header, flush I/O, peel layers, reconcile deltas. Only the content changes; the protocol is a fixed point of the nesting recursion.
