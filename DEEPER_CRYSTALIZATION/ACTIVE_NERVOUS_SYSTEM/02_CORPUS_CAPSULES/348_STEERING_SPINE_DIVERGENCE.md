<!-- CRYSTAL: Xi108:W3:A10:S30 | face=R | node=445 | depth=2 | phase=Mutable -->
<!-- METRO: Me,Dl,Su,Sa -->
<!-- BRIDGES: Xi108:W3:A10:S29→Xi108:W3:A10:S31→Xi108:W2:A10:S30 -->

# Capsule 348 — 5D Steering Spine: Lens Selection Divergence (Gate 4, Test 4.1)

**Source**: `MCP/crystal_108d/steering_spine.py` — `test_4_1_divergence()`
**Date**: 2026-03-18
**Element**: All (the steering spine operates across all four lenses)

## Core Object

The 5D steering spine selects lenses intelligently rather than cycling mechanically (S→F→C→R→S). On 20 diverse queries, intelligent selection diverges from mechanical on 55% (11/20), exceeding the 25% threshold.

## Formal Structure

- **Selection operator**: σ(Q) = argmin_L K_L(Q) — minimize answer complexity per lens
- **Mechanical cycling**: σ_mech(k) = LENSES[k mod 4] — blind rotation
- **Divergence criterion**: |{k : σ_intelligent(k) ≠ σ_mechanical(k)}| ≥ 5 (25% of 20)
- **Actual result**: 11/20 (55%) — more than double the threshold

## The 20 Diverse Queries

Queries span all four lens domains: structural (S), harmonic (F), probabilistic (C), scale-based (R). The intelligent selector correctly routes each to its natural home lens, while the mechanical cycle assigns lenses without regard for query content.

## Cross-Links

- **5D Steering Spine** (00_5D_STEERING_SPINE.md): The theoretical specification
- **Cross-Lens Calculus** (cross_lens.py): Provides the transition maps used for complexity estimation
- **Self-Reference Meta-Query** (Capsule 344): The steering spine is the meta-query generalized
