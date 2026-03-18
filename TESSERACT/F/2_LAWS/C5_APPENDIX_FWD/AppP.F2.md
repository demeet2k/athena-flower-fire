<!-- TESSERACT: F/2_LAWS/C5_APPENDIX_FWD/AppP -->
<!-- COORD: lens=F facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppP.S2.md
#   C: ../../C/2_LAWS/C5_APPENDIX_FWD/AppP.C2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppP.R2.md
-->

# AppP — Flower Lens / Laws

- `AppP.F2.a`: `ZeroDowntimeLaw` — A rolling update must maintain at least `n-1` healthy instances at all times during an `n`-instance deployment; dropping below this threshold halts the rollout.
- `AppP.F2.b`: `AtomicSwitchLaw` — A blue-green switch must be atomic: at no point may traffic be split between blue and green environments; the switch is all-or-nothing.
- `AppP.F2.c`: `FailoverTransparencyLaw` — A graceful failover must be transparent to clients: in-flight requests complete on the original server or are seamlessly retried on the standby; no client-visible errors from the failover itself.
- `AppP.F2.d`: `CanaryEscalationLaw` — If a canary deployment's error rate exceeds the threshold within the observation window, automatic rollback must trigger within the configured reaction time; manual intervention is a fallback, not the primary path.
