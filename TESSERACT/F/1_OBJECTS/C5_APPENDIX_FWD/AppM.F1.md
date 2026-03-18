<!-- TESSERACT: F/1_OBJECTS/C5_APPENDIX_FWD/AppM -->
<!-- COORD: lens=F facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/1_OBJECTS/C5_APPENDIX_FWD/AppM.S1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppM.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppM.R1.md
-->

# AppM — Flower Lens / Objects

- `AppM.F1.a`: `TemporalReplayStream` — A time-ordered stream of state transitions that reconstructs the computation's evolution; supports forward play, pause, and seek-to-tick for temporal navigation.
- `AppM.F1.b`: `CausalReplayGraph` — A DAG where nodes are state transitions and edges are causal dependencies; replaying respects topological order so that every effect follows its cause even under concurrent execution.
- `AppM.F1.c`: `RewindCursor` — A bidirectional replay head that can move forward by applying log entries or backward by restoring prior snapshots, enabling temporal debugging and "what-if" exploration.
- `AppM.F1.d`: `ReplayClockSynchronizer` — A logical clock that aligns multiple replay streams to a common tick reference, ensuring that distributed replays reconstruct the same global ordering of events.
