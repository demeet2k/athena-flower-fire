<!-- TESSERACT: F/2_LAWS/C6_APPENDIX_INV/InvM -->
<!-- COORD: lens=F facet=2(Laws) cell=C6_APPENDIX_INV -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C6_APPENDIX_INV/InvM.S2.md
#   C: ../../C/2_LAWS/C6_APPENDIX_INV/InvM.C2.md
#   R: ../../R/2_LAWS/C6_APPENDIX_INV/InvM.R2.md
-->

# InvM — Flower Lens / Laws

- `InvM.F2.a`: `EntropyReductionMonotoneLaw` — Registry entropy must decrease monotonically during pruning. Any increase indicates information being added (new entries created during pruning), which is prohibited.
- `InvM.F2.b`: `BandlimitFidelityLaw` — The bandlimited profile must faithfully represent the original's essential shape. The Nyquist criterion determines the minimum bandwidth: attributes that vary at scales smaller than the grammar's resolution are noise and may be removed.
- `InvM.F2.c`: `EnvelopeSufficiencyLaw` — The final value plus trajectory must be sufficient to predict the entity's next state (if the seed is planted and growth resumes). If not sufficient, additional envelope parameters must be retained.
- `InvM.F2.d`: `ConvergenceRateLaw` — Registry convergence must be at least geometric. Sub-geometric convergence indicates structural redundancy that pruning alone cannot address — the registry's schema needs redesign.
