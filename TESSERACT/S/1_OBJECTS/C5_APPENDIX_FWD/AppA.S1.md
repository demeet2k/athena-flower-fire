<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppA -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppA.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppA.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppA.R1.md
-->

# AppA — Square Lens / Objects

- `AppA.S1.a`: `Xi108Address` — The canonical 108-dimensional crystal address `Xi108[shell.wreath.arch.face.dim]`, a rigid tuple encoding shell index (0-17), wreath position, archetype mode, face orientation, and dimensional coordinate. Every shard in the organism has exactly one Xi108 address.
- `AppA.S1.b`: `ChapterStationCode` — The chapter-level station identifier `ChNN<CODE>` (e.g., `Ch03SUCC`) binding a two-digit chapter number to a mnemonic tag, forming the primary human-readable routing label for manuscript navigation.
- `AppA.S1.c`: `ShellWreathArchTriple` — The `(shell, wreath, archetype)` triple that locates any shard within the 18-shell crystal lattice, where shell `s ∈ {0..17}` sets depth, wreath `w ∈ {0..5}` sets rotational position, and archetype `a ∈ {E,W,F,A}` sets elemental mode.
- `AppA.S1.d`: `FaceDimensionPair` — The `(face, dim)` suffix pair completing a full crystal coordinate, where face `f ∈ {0..5}` selects one of six cube faces and dim `d ∈ {0..17}` selects the dimensional slot within that face, yielding 108 = 18 × 6 total slots.
