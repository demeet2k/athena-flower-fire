<!-- TESSERACT: S/1_OBJECTS/C6_APPENDIX_INV/InvX -->
<!-- COORD: lens=S facet=1(Objects) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C6_APPENDIX_INV/InvX.F1.md
#   C: ../../C/1_OBJECTS/C6_APPENDIX_INV/InvX.C1.md
#   R: ../../R/1_OBJECTS/C6_APPENDIX_INV/InvX.R1.md
-->

# InvX — Square Lens / Objects

- `InvX.S1.a`: `BundleUnpacker` — The discrete operation of disassembling an export bundle into its constituent shards. Each shard is identified by its crystal address and routed to its home position in the organism lattice. The successor inverts to predecessor: instead of "pack next shard into bundle," it is "extract next shard from bundle."
- `InvX.S1.b`: `FormatStripper` — The difference between the bundle's external format and the shard's internal format. Removes serialization wrappers, transport encoding, compatibility layers. What remains after stripping is the pure shard content — the zero set of format difference.
- `InvX.S1.c`: `CrossReferenceRelink` — During export, internal cross-references were converted to external URIs. During absorption, URIs are resolved back to internal crystal addresses. The product of all relinked references = the fully reconnected internal graph.
- `InvX.S1.d`: `VersionQuotientMerge` — The quotient of the imported version by the organism's current version yields the version delta. If the delta is identity (versions match), absorption is trivial. If the delta is non-trivial, a merge protocol resolves differences — the quotient determines the merge strategy.
