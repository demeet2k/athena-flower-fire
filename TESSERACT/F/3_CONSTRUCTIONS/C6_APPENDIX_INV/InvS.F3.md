<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvS.R3.md
-->

# InvS — Flower Lens / Constructions

- `InvS.F3.a`: `WaveDamper` — Applies a damping field to the residual wave. At each step: reduces the amplitude of the residual at each cell by a fixed fraction, redistributing the absorbed residual to the cell's exact value. Monitors for sign changes.
- `InvS.F3.b`: `RefinementIterator` — For each NEAR value: applies successive refinement steps (e.g., Newton's method for algebraic numbers, continued fraction convergents for irrationals). Tracks the refinement curve. Terminates when the target precision is reached.
- `InvS.F3.c`: `FluxBalancer` — Computes the residual flux between all adjacent cell pairs. Balances flows to drive all residuals toward zero while maintaining conservation. Reports the maximum remaining flux at each iteration.
- `InvS.F3.d`: `PrecisionExtender` — For each truncated value: extends precision by one unit (e.g., one additional decimal digit, one additional binary bit). Iterates until full precision is reached. Reports the precision at each step.
