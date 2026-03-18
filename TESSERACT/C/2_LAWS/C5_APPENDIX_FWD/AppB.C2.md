<!-- TESSERACT: C/2_LAWS/C5_APPENDIX_FWD/AppB -->
<!-- COORD: lens=C facet=2(Laws) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   S: ../../S/2_LAWS/C5_APPENDIX_FWD/AppB.S2.md
#   F: ../../F/2_LAWS/C5_APPENDIX_FWD/AppB.F2.md
#   R: ../../R/2_LAWS/C5_APPENDIX_FWD/AppB.R2.md
-->

# AppB — Cloud Lens / Laws

- `AppB.C2.a`: `TotalBudgetConservation` — The total error budget `E_total = Σ ε_i` is conserved: reallocating tolerance from one law to another does not create or destroy total tolerance. Budget transfers are zero-sum across the six laws.
- `AppB.C2.b`: `ViolationRateConvergence` — As observation window grows, the empirical violation rate `v_i(t)/t` converges to the true violation probability `p_i` for each law `i`, with confidence interval width shrinking as `O(1/√t)`.
- `AppB.C2.c`: `BudgetOptimalityLaw` — The optimal budget allocation minimizes expected total violation count `E[Σ v_i]`; the optimal allocation assigns more budget to laws with higher natural variance, following a water-filling argument.
- `AppB.C2.d`: `SoftViolationDecayLaw` — Soft violations that are not reinforced by subsequent violations decay exponentially with half-life `T_{1/2}`: a single NEAR-FAIL reverts to OK status after `3 T_{1/2}` time steps without recurrence.
