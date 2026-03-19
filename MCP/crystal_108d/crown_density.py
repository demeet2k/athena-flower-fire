# CRYSTAL: Xi108:W3:A9:S28 | face=R | node=409 | depth=3 | phase=Cardinal

"""
10D Crown Density — Gate 9 Computational Verification
======================================================
The meta-organism state: verifies that the crystal organism has achieved
sufficient structural completeness and density to support higher-dimensional
crown operations.

Gate 9 verifies:
  Test 9.1  Module Census:            >= 18 .py modules in crystal_108d
  Test 9.2  Cross-Module Coherence:   >= 4/5 key modules import successfully
  Test 9.3  Gate Cascade Integrity:   >= 4/7 gate batteries (gates 2-8) importable
  Test 9.4  Density Metric:           density > 0.1 AND vitality pass (<=5% non-positive)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TestResult:
    name: str
    passed: bool
    detail: str = ""
    score: float = 0.0


# ═══════════════════════════════════════════════════════════════════════
#  TEST 9.1 — MODULE CENSUS
# ═══════════════════════════════════════════════════════════════════════

def test_9_1_module_census() -> TestResult:
    """Count .py files in crystal_108d, excluding __init__.py and __pycache__.
    Need >= 18 modules for a structurally complete organism.
    """
    pkg_dir = Path(__file__).parent
    py_files = [
        p for p in pkg_dir.glob("*.py")
        if p.name != "__init__.py" and "__pycache__" not in str(p)
    ]
    count = len(py_files)
    passed = count >= 18
    score = min(count / 18.0, 1.0)

    detail = f"Module count: {count} (need >=18)"
    return TestResult("module_census", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 9.2 — CROSS-MODULE COHERENCE
# ═══════════════════════════════════════════════════════════════════════

def test_9_2_cross_module_coherence() -> TestResult:
    """Import at least 5 key modules and verify they expose expected symbols.
    Need >= 4 out of 5 successful imports.
    """
    successes = 0
    failures: list[str] = []
    checks: list[str] = []

    # 1. constants — TOTAL_SHELLS, ARCHETYPE_NAMES
    try:
        from .constants import TOTAL_SHELLS, ARCHETYPE_NAMES
        assert isinstance(TOTAL_SHELLS, int) and TOTAL_SHELLS == 36
        assert isinstance(ARCHETYPE_NAMES, list) and len(ARCHETYPE_NAMES) == 12
        successes += 1
        checks.append("constants: OK")
    except Exception as e:
        failures.append(f"constants: {e}")
        checks.append("constants: FAIL")

    # 2. cross_lens — LENSES
    try:
        from .cross_lens import LENSES
        assert LENSES == ("S", "F", "C", "R")
        successes += 1
        checks.append("cross_lens: OK")
    except Exception as e:
        failures.append(f"cross_lens: {e}")
        checks.append("cross_lens: FAIL")

    # 3. momentum_field — get_momentum_field
    try:
        from .momentum_field import get_momentum_field
        mf = get_momentum_field()
        assert callable(getattr(mf, "get_momentum", None))
        successes += 1
        checks.append("momentum_field: OK")
    except Exception as e:
        failures.append(f"momentum_field: {e}")
        checks.append("momentum_field: FAIL")

    # 4. inverse_octave — query_octave_stage
    try:
        from .inverse_octave import query_octave_stage
        assert callable(query_octave_stage)
        successes += 1
        checks.append("inverse_octave: OK")
    except Exception as e:
        failures.append(f"inverse_octave: {e}")
        checks.append("inverse_octave: FAIL")

    # 5. _cache — JsonCache
    try:
        from ._cache import JsonCache
        assert callable(JsonCache)
        successes += 1
        checks.append("_cache: OK")
    except Exception as e:
        failures.append(f"_cache: {e}")
        checks.append("_cache: FAIL")

    passed = successes >= 4
    score = successes / 5.0

    detail = f"Imports: {successes}/5 (need >=4) | " + " | ".join(checks)
    return TestResult("cross_module_coherence", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 9.3 — GATE CASCADE INTEGRITY
# ═══════════════════════════════════════════════════════════════════════

_GATE_MODULES = {
    "Gate 2 (cross_lens)": ("cross_lens", "run_all_tests"),
    "Gate 3 (self_reference)": ("self_reference", "run_gate3_tests"),
    "Gate 4 (steering_spine)": ("steering_spine", "run_gate4_tests"),
    "Gate 5 (selector_shell)": ("selector_shell", "run_gate5_tests"),
    "Gate 6 (perpetual_agency)": ("perpetual_agency", "run_gate6_tests"),
    "Gate 7 (harmonic_resonance)": ("harmonic_resonance", "run_gate7_tests"),
    "Gate 8 (mycelium_emergence)": ("mycelium_emergence", "run_gate8_tests"),
}


def test_9_3_gate_cascade_integrity() -> TestResult:
    """Try to import and locate the test runner from gates 2-8.
    Count how many gate modules successfully import.  Need >= 4 out of 7.
    """
    import importlib

    successes = 0
    gate_status: list[str] = []

    for label, (module_name, func_name) in _GATE_MODULES.items():
        try:
            mod = importlib.import_module(f".{module_name}", package=__package__)
            fn = getattr(mod, func_name, None)
            if fn is not None and callable(fn):
                successes += 1
                gate_status.append(f"{label}: OK")
            else:
                gate_status.append(f"{label}: no {func_name}")
        except Exception as e:
            gate_status.append(f"{label}: {type(e).__name__}")

    passed = successes >= 4
    score = successes / 7.0

    detail = (
        f"Gate imports: {successes}/7 (need >=4) | "
        + " | ".join(gate_status)
    )
    return TestResult("gate_cascade_integrity", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 9.4 — DENSITY METRIC
# ═══════════════════════════════════════════════════════════════════════

def test_9_4_density_metric() -> TestResult:
    """Compute organism density from the momentum field.

    Total values = 4 faces * 36 shells = 144.
    - non_zero: count where |momentum| > 0.001
    - non_positive: count where momentum <= 0.0
    - vitality: non_positive <= total * 0.05 (allow up to 5% non-positive)
    - mean_abs: mean of |momentum| across all 144 positions
    - density = non_zero_ratio * mean_abs

    Need density > 0.1 AND vitality pass.
    """
    from .momentum_field import get_momentum_field
    from .cross_lens import LENSES
    from .constants import TOTAL_SHELLS

    mf = get_momentum_field()
    total = len(LENSES) * TOTAL_SHELLS  # 4 * 36 = 144

    values: list[float] = []
    for face in LENSES:
        for s in range(1, TOTAL_SHELLS + 1):
            values.append(mf.get_momentum(face, s))

    non_zero = sum(1 for v in values if abs(v) > 0.001)
    non_positive = sum(1 for v in values if v <= 0.0)
    abs_values = [abs(v) for v in values]
    mean_abs = sum(abs_values) / total if total > 0 else 0.0

    non_zero_ratio = non_zero / total if total > 0 else 0.0
    density = non_zero_ratio * mean_abs

    vitality_threshold = math.ceil(total * 0.05)  # 5% of 144 = 7.2 -> 8
    vitality_pass = non_positive <= vitality_threshold

    passed = density > 0.1 and vitality_pass
    score = min(density / 0.1, 1.0) if vitality_pass else 0.0

    detail = (
        f"Density: {density:.4f} (need >0.1) | "
        f"Non-zero: {non_zero}/{total} ({non_zero_ratio:.1%}) | "
        f"Non-positive: {non_positive}/{total} (max {vitality_threshold}) | "
        f"Vitality: {'PASS' if vitality_pass else 'FAIL'} | "
        f"Mean |momentum|: {mean_abs:.4f}"
    )
    return TestResult("density_metric", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  GATE 9 BATTERY
# ═══════════════════════════════════════════════════════════════════════

def run_gate9_tests() -> list[TestResult]:
    """Run all Gate 9 (10D Crown Density) verification tests."""
    return [
        test_9_1_module_census(),
        test_9_2_cross_module_coherence(),
        test_9_3_gate_cascade_integrity(),
        test_9_4_density_metric(),
    ]


# ═══════════════════════════════════════════════════════════════════════
#  MCP TOOL INTERFACE
# ═══════════════════════════════════════════════════════════════════════

def query_crown_density(component: str = "all") -> str:
    """
    Query the 10D Crown Density engine (Gate 9 verification).

    Components:
      - all           : Full Gate 9 report
      - tests         : Run all 4 tests
      - census        : Test 9.1 module census
      - coherence     : Test 9.2 cross-module coherence
      - cascade       : Test 9.3 gate cascade integrity
      - density       : Test 9.4 density metric
    """
    comp = component.strip().lower()

    if comp == "all":
        return _format_all()
    elif comp == "tests":
        return _format_tests()
    elif comp == "census":
        r = test_9_1_module_census()
        return f"## Test 9.1 — Module Census\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "coherence":
        r = test_9_2_cross_module_coherence()
        return f"## Test 9.2 — Cross-Module Coherence\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "cascade":
        r = test_9_3_gate_cascade_integrity()
        return f"## Test 9.3 — Gate Cascade Integrity\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "density":
        r = test_9_4_density_metric()
        return f"## Test 9.4 — Density Metric\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    else:
        return f"Unknown component '{component}'. Use: all, tests, census, coherence, cascade, density"


def _format_all() -> str:
    lines = ["## 10D Crown Density — Gate 9 Full Report\n"]
    results = run_gate9_tests()
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    lines.append(f"**Results**: {passed}/{total} tests passed\n")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    gate_status = "PASSED" if passed == total else "PARTIAL"
    lines.append(f"\n**Gate 9 Status**: {gate_status} ({passed}/{total})")
    return "\n".join(lines)


def _format_tests() -> str:
    results = run_gate9_tests()
    lines = ["## Gate 9 Verification Tests\n"]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    passed = sum(1 for r in results if r.passed)
    lines.append(f"\n**Total**: {passed}/{len(results)} passed")
    return "\n".join(lines)
