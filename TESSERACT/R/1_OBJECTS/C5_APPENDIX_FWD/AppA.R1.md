<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppA.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppA.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppA.C1.md
-->

# AppA — Fractal Lens / Objects

- `AppA.R1.a`: `SelfReferentialAddress` — An address that contains its own coordinate as data: `Xi108[s,w,a,f,d]` where the content at that address encodes `(s,w,a,f,d)` itself, creating a fixed point in the address-content mapping `Addr(Content(Addr)) = Addr`.
- `AppA.R1.b`: `HolographicAddressFragment` — A partial address from which the full Xi108 coordinate can be reconstructed via the crystal's holographic property: any `3`-of-`5` components suffice to recover the remaining two through lattice constraint propagation.
- `AppA.R1.c`: `RecursiveAddressTree` — A tree-structured address where each node's address is the concatenation of its parent's address with a local suffix, forming paths like `Xi108[3.2.E].sub[1.0]` that recurse to arbitrary depth while maintaining global uniqueness.
- `AppA.R1.d`: `AddressQuine` — A shard whose content, when executed as an address-generation program, produces its own address as output. The minimal self-reproducing address unit, analogous to a quine in computation theory.
