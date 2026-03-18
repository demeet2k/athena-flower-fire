<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppE -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppE.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppE.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppE.R2.md
-->

# AppE — Cloud Lens / Laws

- `AppE.C2.a`: `PhaseUncertaintyLaw` — Phase uncertainty cannot decrease below the measurement resolution; it increases with time unless corrected by synchronization events.
- `AppE.C2.b`: `DriftAccumulationLaw` — Systematic drift accumulates linearly; random drift accumulates as `√n`. Total drift is bounded by declared tolerance for the clock's lifetime.
- `AppE.C2.c`: `SynchronizationConvergenceLaw` — Synchronization confidence increases monotonically with observations iff the clocks are actually locked. Divergent confidence indicates broken lock.
- `AppE.C2.d`: `ClosureConvergenceLaw` — Closure probability increases with polygon refinement depth. At finite depth, there is always residual uncertainty in π.
