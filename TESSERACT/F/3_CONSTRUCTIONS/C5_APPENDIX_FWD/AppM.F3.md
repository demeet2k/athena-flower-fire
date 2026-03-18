<!-- TESSERACT: F/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=F facet=3(Constructions) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C5_APPENDIX_FWD/AppM.R3.md
-->

# AppM — Flower Lens / Constructions

- `AppM.F3.a`: `StreamingReplayPipeline` — Constructs a pipeline that reads log segments from storage, applies them to the current snapshot in tick order, and emits a live state stream for real-time observation of the replayed computation.
- `AppM.F3.b`: `CausalReplayScheduler` — Given a causal replay graph, produces a valid topological execution schedule that maximizes parallelism while preserving all causal dependencies.
- `AppM.F3.c`: `TemporalBisectionSearch` — Locates the first tick at which a property `P` becomes true by binary-searching over the checkpoint lattice, replaying only the log segments around candidate ticks; runs in O(log T) replays.
- `AppM.F3.d`: `MultiStreamAligner` — Merges `k` replay streams from different SFCR elements into a single interleaved global trace by aligning on the synchronized logical clock, producing a unified temporal view.
