<!-- TESSERACT: R/1_OBJECTS/C5_APPENDIX_FWD/AppN -->
<!-- COORD: lens=R facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppN.S1.md
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppN.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppN.C1.md
-->

# AppN — Fractal Lens / Objects

- `AppN.R1.a`: `SelfDescribingContainer` — A container whose header includes a machine-readable schema definition, decompression algorithm identifier, and integrity-check procedure, so any reader can unpack it without external documentation.
- `AppN.R1.b`: `BootstrapArchive` — An archive that contains not only crystal shards but also the code needed to mount, query, and verify them; opening the archive installs a minimal runtime environment.
- `AppN.R1.c`: `SchemaEvolutionEnvelope` — A container wrapper that carries multiple schema versions and a migration function between them, ensuring that archives written under old schemas remain readable under new ones.
- `AppN.R1.d`: `AutoDecompressingPacket` — A container that detects the recipient's available decompression codecs, selects the optimal one, and presents its contents in the most efficient format the recipient supports.
