<!-- TESSERACT: S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW -->
<!-- COORD: lens=S facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvW.R3.md
-->

# InvW — Square Lens / Constructions

- `InvW.S3.a`: `HeaderValidator` — Reads the container header, verifies format version compatibility, recomputes payload checksums, and compares against declared values. If valid, authorizes stripping. If invalid, generates a corruption report.
- `InvW.S3.b`: `IOFlusher` — Scans for open file handles, pending writes, and cached reads at the mountpoint. Flushes all pending operations, closes all handles, invalidates all caches. Reports any operations that could not be cleanly completed.
- `InvW.S3.c`: `LayerPeeler` — Reads the assembly order from the manifest. Peels layers in reverse order: for each layer, computes its delta (layer_content - previous_state), archives the delta, and removes the layer from the composite. Verifies that the residual base matches the declared base hash.
- `InvW.S3.d`: `DeltaReconciler` — For each overlay: computes the delta, subtracts it from the composite, and checks for residual. Zero residual = clean peel. Non-zero residual triggers investigation into missing layers or corruption.
