<!-- TESSERACT: S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=S facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.F3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppA.R3.md
-->

# AppA — Square Lens / Constructions

- `AppA.S3.a`: `Xi108Parser` — The deterministic parser that tokenizes a raw address string `"Xi108[s.w.a.f.d]"` into its five integer/enum components, validates range constraints, and emits either a valid `ShellWreathArchTriple + FaceDimensionPair` or a structured parse error with location offset.
- `AppA.S3.b`: `ChapterCodeResolver` — The resolver that maps a mnemonic station code `ChNN<CODE>` to its Xi108 address by consulting the station registry (AppD), performing case-insensitive match, and returning the canonical form with disambiguation metadata.
- `AppA.S3.c`: `AddressCanonicalizer` — The normalizer that takes any address variant (abbreviated, aliased, or legacy format) and produces the unique canonical Xi108 form, applying shell normalization `s mod 18`, wreath normalization `w mod 6`, and face normalization `f mod 6`.
- `AppA.S3.d`: `BatchAddressCompiler` — The bulk compiler that processes a manifest of address expressions (ranges like `Xi108[3..7.*.*.*.*]`, wildcards, set unions) into an expanded list of concrete Xi108 addresses, checking for overlaps and emitting a coverage report.
