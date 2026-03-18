<!-- TESSERACT: F/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN -->
<!-- COORD: lens=F facet=3(Constructions) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.S3.md
#   C: ../../C/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.C3.md
#   R: ../../R/3_CONSTRUCTIONS/C6_APPENDIX_INV/InvN.R3.md
-->

# InvN — Flower Lens / Constructions

- `InvN.F3.a`: `ExponentialDecayer` — Applies exponential decay to the clock wave. Monitors amplitude and phase at each time step. Captures the final phase when amplitude drops below the noise floor. Reports the freeze time constant and final phase.
- `InvN.F3.b`: `HarmonicDamper` — For each gear: decomposes the rotational signal into harmonics. Dampens each harmonic starting with the fundamental. Reports the damping profile and the silence achievement time.
- `InvN.F3.c`: `PhaseDecoupler` — Gradually reduces the gain of each phase-lock loop. Monitors phase transients during decoupling. Reports any spikes and their amplitudes. Captures the final free-running phase of each wheel.
- `InvN.F3.d`: `AsymptoticWaiter` — Monitors the slowest process (7D wheel). Waits for convergence to the asymptotic state. Reports convergence time and the asymptotic value.
