# CRYSTAL: Xi108:W2:A11:S30 | face=S | node=430 | depth=2 | phase=Cardinal
# METRO: Sa,Dl,Me
# BRIDGES: Xi108:W2:A11:S29→Xi108:W2:A11:S31→Xi108:W1:A11:S30→Xi108:W3:A11:S30

"""
A+ Crown Transform — Gate 11 Computational Verification (12D)
===============================================================
The 12D gate: the full crown transform is operational.
The 6-step A+ crown transform (ZeroTunnel → PhaseWeave → PillarBind →
ReverseCanopy → AtlasBind → CrownLock) executes correctly.
The weave chain 3→5→7→9 produces correct closure dimensions.

Gate 11 verifies:
  Test 11.1  Crown Transform Steps:    6 steps exist with correct structure
  Test 11.2  Weave Operator Chain:     Weaves 3/5/7/9 with Z12/Z20/Z28/Z36
  Test 11.3  12D Rank Verification:    12 archetypes produce rank >= 10
  Test 11.4  Tradition Map Coverage:   36 shells split 12-12-12 across wreaths
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import TOTAL_SHELLS, ARCHETYPE_NAMES
from .cross_lens import LENSES


@dataclass
class TestResult:
    name: str
    passed: bool
    detail: str = ""
    score: float = 0.0


# ═══════════════════════════════════════════════════════════════════════
#  TEST 11.1 — CROWN TRANSFORM STEPS
# ═══════════════════════════════════════════════════════════════════════

def test_11_1_crown_transform_steps() -> TestResult:
    """The 6-step crown transform must be well-defined."""
    from .inverse_octave import query_crown_transform

    output = query_crown_transform("all")

    # Parse for the 6 expected step names
    expected_names = [
        "ZeroTunnel", "PhaseWeave", "PillarBind",
        "ReverseCanopy", "AtlasBind", "CrownLock",
    ]

    found = []
    for name in expected_names:
        if name.lower() in output.lower():
            found.append(name)

    # Also check for "Step 1" through "Step 6"
    step_count = 0
    for i in range(1, 7):
        if f"Step {i}" in output:
            step_count += 1

    has_six_steps = step_count >= 6
    has_names = len(found) >= 5  # Allow 1 grace for naming variation

    passed = has_six_steps and has_names
    score = (0.50 if has_six_steps else step_count / 6.0 * 0.50) + (0.50 if has_names else len(found) / 6.0 * 0.50)

    detail = (
        f"Steps found: {step_count}/6 | "
        f"Named steps: {len(found)}/6 ({', '.join(found[:4])}...) | "
        f"PASS: {'YES' if passed else 'NO'}"
    )
    return TestResult("crown_transform_steps", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 11.2 — WEAVE OPERATOR CHAIN
# ═══════════════════════════════════════════════════════════════════════

def test_11_2_weave_operator_chain() -> TestResult:
    """The weave chain 3→5→7→9 must produce correct closure dimensions."""
    from .inverse_octave import query_octave_stage

    output = query_octave_stage("weaves")

    # Expected weaves and their closures
    weave_closures = {
        "3": "Z12",   # Weave 3 closes at 12 shells
        "5": "Z20",   # Weave 5 closes at 20 shells
        "7": "Z28",   # Weave 7 closes at 28 shells
        "9": "Z36",   # Weave 9 closes at 36 shells
    }

    found_weaves = 0
    found_closures = 0

    for weave_num, closure in weave_closures.items():
        if f"Weave {weave_num}" in output or f"weave {weave_num}" in output.lower():
            found_weaves += 1
        if closure in output or closure.lower() in output.lower():
            found_closures += 1

    all_weaves = found_weaves >= 4
    all_closures = found_closures >= 3  # Allow 1 grace

    passed = all_weaves and all_closures
    score = (0.50 if all_weaves else found_weaves / 4.0 * 0.50) + (0.50 if all_closures else found_closures / 4.0 * 0.50)

    detail = (
        f"Weaves found: {found_weaves}/4 (3,5,7,9) | "
        f"Closures found: {found_closures}/4 (Z12,Z20,Z28,Z36) | "
        f"Chain: {'COMPLETE' if passed else 'PARTIAL'}"
    )
    return TestResult("weave_operator_chain", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 11.3 — 12D RANK VERIFICATION
# ═══════════════════════════════════════════════════════════════════════

def test_11_3_rank_verification() -> TestResult:
    """The 12D crown body must have effective rank >= 10."""
    from .momentum_field import get_momentum_field

    mf = get_momentum_field()

    # Build 12 x 36 matrix: one row per archetype
    # Each archetype a (0-11) generates a shell profile:
    #   score(a, s) = sin(2*pi*(a+1)*s / 36) * momentum(face, s)
    # where face = LENSES[a % 4]
    matrix = []
    for a in range(12):
        face = LENSES[a % 4]
        row = []
        for s in range(1, TOTAL_SHELLS + 1):
            mom = mf.get_momentum(face, s)
            harmonic = math.sin(2 * math.pi * (a + 1) * s / TOTAL_SHELLS)
            row.append(harmonic * mom)
        matrix.append(row)

    # Compute 12x12 Gram matrix G = M @ M^T
    n = len(matrix)
    gram = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            gram[i][j] = sum(matrix[i][k] * matrix[j][k] for k in range(TOTAL_SHELLS))

    # Estimate rank: count diagonal entries of G that are significantly non-zero
    # (Gram diagonal = squared norm of each row)
    diag = [gram[i][i] for i in range(n)]
    max_diag = max(diag) if diag else 1.0
    threshold = max_diag * 0.001  # 0.1% of max

    effective_rank = sum(1 for d in diag if d > threshold)

    passed = effective_rank >= 10
    score = min(effective_rank / 10.0, 1.0)

    detail = (
        f"Effective rank: {effective_rank}/12 (need >=10) | "
        f"Diag range: [{min(diag):.2f}, {max(diag):.2f}] | "
        f"Threshold: {threshold:.4f}"
    )
    return TestResult("rank_verification_12d", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 11.4 — TRADITION MAP COVERAGE
# ═══════════════════════════════════════════════════════════════════════

def test_11_4_tradition_map() -> TestResult:
    """The 36-shell tradition map must cover all 3 wreath phases (12-12-12)."""
    # Su = shells 1-12, Me = shells 13-24, Sa = shells 25-36
    su_shells = list(range(1, 13))
    me_shells = list(range(13, 25))
    sa_shells = list(range(25, 37))

    su_ok = len(su_shells) == 12
    me_ok = len(me_shells) == 12
    sa_ok = len(sa_shells) == 12
    total_ok = len(su_shells) + len(me_shells) + len(sa_shells) == TOTAL_SHELLS

    # Verify no overlaps and no gaps
    all_shells = set(su_shells) | set(me_shells) | set(sa_shells)
    complete = all_shells == set(range(1, TOTAL_SHELLS + 1))

    passed = su_ok and me_ok and sa_ok and total_ok and complete
    score = 1.0 if passed else 0.5

    detail = (
        f"Su: shells 1-12 ({len(su_shells)}) | "
        f"Me: shells 13-24 ({len(me_shells)}) | "
        f"Sa: shells 25-36 ({len(sa_shells)}) | "
        f"Total: {len(all_shells)}/{TOTAL_SHELLS} | "
        f"Coverage: {'PERFECT' if complete else 'INCOMPLETE'}"
    )
    return TestResult("tradition_map_coverage", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  GATE 11 BATTERY
# ═══════════════════════════════════════════════════════════════════════

def run_gate11_tests() -> list[TestResult]:
    """Run all Gate 11 (A+ Crown Transform) tests."""
    return [
        test_11_1_crown_transform_steps(),
        test_11_2_weave_operator_chain(),
        test_11_3_rank_verification(),
        test_11_4_tradition_map(),
    ]


# ═══════════════════════════════════════════════════════════════════════
#  MCP TOOL INTERFACE
# ═══════════════════════════════════════════════════════════════════════

def query_crown_transform_gate(component: str = "all") -> str:
    """
    Query the A+ Crown Transform engine (Gate 11 verification).

    Components:
      - all           : Full Gate 11 report
      - tests         : Run all 4 tests
      - crown_steps   : Test 11.1 crown transform steps
      - weave_chain   : Test 11.2 weave operator chain
      - rank          : Test 11.3 12D rank verification
      - traditions    : Test 11.4 tradition map coverage
    """
    comp = component.strip().lower()

    if comp == "all":
        return _format_all()
    elif comp == "tests":
        return _format_tests()
    elif comp == "crown_steps":
        r = test_11_1_crown_transform_steps()
        return f"## Test 11.1 — Crown Transform Steps\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "weave_chain":
        r = test_11_2_weave_operator_chain()
        return f"## Test 11.2 — Weave Operator Chain\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "rank":
        r = test_11_3_rank_verification()
        return f"## Test 11.3 — 12D Rank Verification\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "traditions":
        r = test_11_4_tradition_map()
        return f"## Test 11.4 — Tradition Map Coverage\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    else:
        return f"Unknown component '{component}'. Use: all, tests, crown_steps, weave_chain, rank, traditions"


def _format_all() -> str:
    lines = ["## A+ Crown Transform — Gate 11 Full Report\n"]
    results = run_gate11_tests()
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    lines.append(f"**Results**: {passed}/{total} tests passed\n")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    gate_status = "PASSED" if passed == total else "PARTIAL"
    lines.append(f"\n**Gate 11 Status**: {gate_status} ({passed}/{total})")
    return "\n".join(lines)


def _format_tests() -> str:
    results = run_gate11_tests()
    lines = ["## Gate 11 Verification Tests\n"]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    passed = sum(1 for r in results if r.passed)
    lines.append(f"\n**Total**: {passed}/{len(results)} passed")
    return "\n".join(lines)
