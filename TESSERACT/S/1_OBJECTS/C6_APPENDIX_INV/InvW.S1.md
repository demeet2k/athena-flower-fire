<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvW.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvW.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvW.R1.md
-->

# InvW — Square Lens / Objects

- `InvW.S1.a`: `ContainerHeaderStrip` — The discrete removal of the container header from a packaged organism. The header contains format version, content manifest, integrity checksums, and mount instructions. Stripping reveals the raw payload. The successor inverts: "remove the outermost envelope layer."
- `InvW.S1.b`: `VirtualMountpointDetach` — The difference between the virtual filesystem's address space and the organism's native crystal addresses. Detaching the mountpoint removes the virtual-to-native translation layer, exposing raw crystal coordinates. The zero set: addresses that are identical in both spaces (natural mount points).
- `InvW.S1.c`: `LayerProductDisassembly` — Containers may have multiple layers (base + overlays). The product of all layers = the composite filesystem. Disassembly factors the product back into individual layers, each layer peeled independently. The factorization is unique when layers have no circular dependencies.
- `InvW.S1.d`: `OverlayQuotientReduction` — Each overlay layer is a quotient: overlay_content / base_content = delta. To unwind, the delta is subtracted from the composite, recovering the base. Multiple overlays unwind in reverse application order: last applied = first removed.
