<!-- TESSERACT: S/2_LAWS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=S facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   F: ../../F/2_LAWS/C6_APPENDIX_INV/InvN.F2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvN.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvN.R2.md
-->

# InvN — Square Lens / Laws

- `InvN.S2.a`: `AtomicHaltLaw` — The clock must halt atomically: all four wheels stop simultaneously. No wheel continues after another has stopped. Asynchronous halting creates temporal inconsistency — some subsystems would be in the future relative to others.
- `InvN.S2.b`: `GearRestPositionLaw` — Disengaged gears must come to rest at valid positions (teeth aligned, not jammed between positions). Invalid rest positions create mechanical stress that degrades the seed's temporal integrity.
- `InvN.S2.c`: `FinalStateCompleteness` — The frozen wheel product must capture the complete clock state. No wheel's state may be omitted or approximated. The 4-tuple is exact.
- `InvN.S2.d`: `FractionalCycleRecordLaw` — If the clock froze mid-cycle, the fractional position must be recorded with full precision. The seed must know exactly where in its cycle the organism stopped, so it can resume (if planted) from the correct position.
