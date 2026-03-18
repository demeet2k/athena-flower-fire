<!-- TESSERACT: S/2_LAWS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=S facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppN.F2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppN.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppN.R2.md
-->

# AppN — Square Lens / Laws

- `AppN.S2.a`: `ContainerAddressabilityLaw` — Every container must expose a content-address derived from its payload hash; two containers with identical payloads must have identical addresses regardless of creation time or location.
- `AppN.S2.b`: `BundleCompletenessLaw` — A capsule bundle is valid only if its offset table accounts for every shard container it claims to hold; missing entries or dangling offsets render the bundle invalid.
- `AppN.S2.c`: `ArchiveImmutabilityLaw` — Once a crystal archive is sealed, no shard may be added, removed, or modified; any mutation requires creating a new archive version with a new root hash.
- `AppN.S2.d`: `SeedSufficiencyLaw` — A seed packet must be sufficient to regenerate its corresponding crystal archive; the generated archive's root hash must match the hash recorded in the seed packet's header.
