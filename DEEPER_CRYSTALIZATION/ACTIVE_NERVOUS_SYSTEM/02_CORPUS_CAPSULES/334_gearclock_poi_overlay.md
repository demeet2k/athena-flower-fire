# Capsule 334 — Gearclock Poi Overlay

**Source**: 2026-03-18_4d_calculus.md
**Family**: 4d_calculus
**Lens**: F (Flower/Dynamics)

The raw shell is mapped as a circular gearclock with quartet rank r(SR)=0, r(SL)=1, r(AL)=2, r(AR)=3, and shell notch index n(mu,q) = 4(mu-1) + r(q) giving n in {0,...,59}. This is the outer 60-notch clock. Refined by scale band kappa, the micro-notch index is n_kappa(mu,q,p) = kappa * n(mu,q) + p, and the liminal angle is theta(mu,q,kappa,p) = 2pi/(60*kappa) * n_kappa. This gives exact circular position for every microstate.

The 2-circle poi overlay law is the fully generative layer. A circle is represented as C = (kappa, Delta, q_0, sigma, psi) with refinement ring, global phase offset, initial quartet orientation, weave class, and parity/resonance lock. Given two circles C_i and C_j, they are lifted to a shared refinement L = lcm(kappa_i, kappa_j). Points are transported into a shared clock of length 60L. A direct nexus candidate exists when t_i = t_j + delta_t (mod 60L) for some legal offset delta_t prescribed by the weave class.

Every 2-circle poi pattern becomes a codified object P_2 = (C_i, C_j, delta_t, sigma, psi, mode), and every such P_2 generates a nexus set N(P_2). This is the first exact codification of "overlap every systematic 2-circle poi pattern and find every possible nexus point."

## Key Objects
- 60-notch gearclock with micro-notch refinement by scale bands
- 2-circle poi overlay: codified as P_2 = (C_i, C_j, delta_t, sigma, psi, mode)
- Shared refinement clock L = lcm(kappa_i, kappa_j) x 60

## Key Laws
- The shell is exactly a circular clockwork with explicit angular coordinates
- Nexus candidates exist where two circles align modulo legal offset
- Every 2-circle poi pattern is a codified object generating a nexus set

## Source
- `29_ACCEPTED_INPUTS/2026-03-18_4d_calculus.md`
