# Capsule 297 — Sigma-15 to Sigma-60 Lens Escalation

**Source**: 2026-03-18_6x6_higher_lenses.md
**Family**: 6x6_higher_lenses
**Lens**: C (Cloud/Admissibility)

The 24-state chart-sector table ({A,B,C,D} x S_6) gives the visible atlas, while the 24-state lens-sector table ({Sq,Fl,Cl,Fr} x S_6) gives the constitutive renderer atlas. These must not be conflated. The full 96-slot cockpit is A^{cockpit}_{96} = {A,B,C,D} x {Sq,Fl,Cl,Fr} x S_6 with hidden payload law xi in Sigma_s where |Sigma_s| = 256.

Each of the 24 visible slots is explicitly defined with its chart face, board code, row/column realization, pairing skeleton, shell current, chirality, selector fiber, and hidden 256-state payload sector. The slot instantiation binds each to minimal Flower, Cloud, and Fractal packets. The Flower packet carries (pi_s, beat, chi_s, lambda, torsion_history). The Cloud packet carries (admissibility_min, truth_min=NEAR, beat_budget, evidence_min). The Fractal seed carries (P_X, t_X, pi_s, chi_s, beat, lambda, theta, sigma_board, cert_min).

The promotion rule from NEAR to OK requires that the board M_{X,s} is attached and passes HCRL with replay witness. This is the honest boundary: visible slot existence is settled, but fully certified instantiation is still being built.

## Key Objects
- 96-slot cockpit: 4 charts x 4 lenses x 6 sectors
- Per-slot Flower, Cloud, and Fractal packets
- Promotion rule: NEAR -> OK requires HCRL + replay witness

## Key Laws
- Chart atlas and lens atlas must not be conflated
- Each slot must carry all four lens projections simultaneously
- Truth starts at NEAR and promotes to OK only with explicit certification

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_6x6_higher_lenses.md`
