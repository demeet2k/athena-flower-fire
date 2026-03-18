<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppO -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppO.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppO.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppO.R2.md
-->

# AppO — Flower Lens / Laws

- `AppO.F2.a`: `SyncConvergenceLaw` — Two nodes running the sync protocol on the same tile must converge to identical state after exchanging all pending deltas; permanent divergence is a protocol violation.
- `AppO.F2.b`: `DeltaOrderingLaw` — Delta updates must be applied in causal order: if cell `A`'s new content references cell `B`, then `B`'s delta must be applied before `A`'s in any valid import sequence.
- `AppO.F2.c`: `MergeCommutativityLaw` — Conflict-free merge is commutative: `merge(delta_1, delta_2) = merge(delta_2, delta_1)` for all concurrent deltas, ensuring order-independent convergence.
- `AppO.F2.d`: `ExportDurabilityLaw` — Once an export operation is enqueued, it must eventually complete or be explicitly cancelled; silent drops are forbidden; the queue is durable across restarts.
