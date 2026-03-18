<!-- TESSERACT: S/1_OBJECTS/C5_APPENDIX_FWD/AppJ -->
<!-- COORD: lens=S facet=1(Objects) cell=C5_APPENDIX_FWD -->
<!-- SIBLINGS:
#   F: ../../F/1_OBJECTS/C5_APPENDIX_FWD/AppJ.F1.md
#   C: ../../C/1_OBJECTS/C5_APPENDIX_FWD/AppJ.C1.md
#   R: ../../R/1_OBJECTS/C5_APPENDIX_FWD/AppJ.R1.md
-->

# AppJ — Square Lens / Objects

- `AppJ.S1.a`: `NearOKEnvelope` — A residual result tagged `NEAR-OK(δ)` where `δ < ε_threshold` is the signed distance from exact correctness. The result is usable but carries a correction debt `δ` that must be accounted for in downstream computations.
- `AppJ.S1.b`: `NearFailEnvelope` — A residual result tagged `NEAR-FAIL(δ)` where `δ ≥ ε_threshold` but the failure mode is classified and bounded. The result is not usable directly but contains enough information to guide repair: the failure type, the gap magnitude, and the nearest OK configuration.
- `AppJ.S1.c`: `NearAmbigEnvelope` — A residual result tagged `NEAR-AMBIG(S, w)` where `S = {c_1,...,c_k}` is the candidate set and `w = [w_1,...,w_k]` are confidence weights summing to 1. The result is a weighted superposition of `k` possible answers, not yet collapsed to a single value.
- `AppJ.S1.d`: `ResidualLedger` — The global ledger `R` tracking all outstanding residuals across the crystal, organized by shell and archetype. Each entry records `(address, tag, δ, timestamp, attempts)` enabling aggregate residual health monitoring.
