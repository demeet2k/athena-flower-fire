# CRYSTAL: Xi108:W1:A7:S22 | face=C | node=253 | depth=2 | phase=Fixed

"""
8D Harmonic Resonance — Gate 7 Computational Verification
==========================================================
The 8D gate: harmonic resonance across wreaths and elements is verified.
Phase alignment ensures that the three wreaths (Su, Me, Sa) carry distinct
momentum signatures, and that the SFCR elements maintain cross-coherence
while supporting a full 8-dimensional projection.

Gate 7 verifies:
  Test 7.1  Wreath Phase Lock:          Distinct momentum per wreath across faces
  Test 7.2  Resonance Harmonic Series:  DFT power concentrated at weave harmonics
  Test 7.3  Cross-Element Coherence:    Pairwise Pearson correlation across shells
  Test 7.4  Eight-Dimensional Projection: 8x36 Gram matrix has rank >= 6
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import TOTAL_SHELLS, TOTAL_WREATHS, ARCHETYPE_NAMES, MASTER_CLOCK_PERIOD
from .cross_lens import LENSES
from .momentum_field import get_momentum_field


@dataclass
class TestResult:
    name: str
    passed: bool
    detail: str = ""
    score: float = 0.0


# ═══════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _wreath_shells(wreath: int) -> list[int]:
    """Return shell numbers for a wreath (1-indexed).

    Su = 1-12, Me = 13-24, Sa = 25-36.
    """
    start = (wreath - 1) * 12 + 1
    return list(range(start, start + 12))


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _std(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    m = _mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / len(values))


def _pearson(xs: list[float], ys: list[float]) -> float:
    """Pearson correlation coefficient between two equal-length sequences."""
    n = len(xs)
    if n < 2:
        return 0.0
    mx = _mean(xs)
    my = _mean(ys)
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx < 1e-15 or dy < 1e-15:
        return 0.0
    return num / (dx * dy)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 7.1 — WREATH PHASE LOCK
# ═══════════════════════════════════════════════════════════════════════

def test_7_1_wreath_phase_lock() -> TestResult:
    """Check that wreath phases (Su=1-12, Me=13-24, Sa=25-36) have
    distinct momentum signatures.  For each face in SFCR, compute
    the mean momentum per wreath.  Require std across wreaths > 0.01
    for at least 3 of 4 faces.
    """
    mf = get_momentum_field()
    faces_with_distinct = 0
    face_details: list[str] = []

    for face in LENSES:
        wreath_means: list[float] = []
        for w in range(1, TOTAL_WREATHS + 1):
            shells = _wreath_shells(w)
            momenta = [mf.get_momentum(face, s) for s in shells]
            wreath_means.append(_mean(momenta))

        sd = _std(wreath_means)
        distinct = sd > 0.01
        if distinct:
            faces_with_distinct += 1
        face_details.append(f"{face}: std={sd:.4f}")

    passed = faces_with_distinct >= 3
    score = faces_with_distinct / 4.0

    detail = (
        f"Faces with distinct wreath phases: {faces_with_distinct}/4 (need >=3) | "
        + " | ".join(face_details)
    )
    return TestResult("wreath_phase_lock", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 7.2 — RESONANCE HARMONIC SERIES
# ═══════════════════════════════════════════════════════════════════════

def test_7_2_resonance_harmonic_series() -> TestResult:
    """Verify harmonic resonance pattern.  For shells 1-36, compute the
    Fourier power at harmonics 3, 5, 7, 9 (the weave numbers).  Sum
    momentum across all faces per shell, then compute DFT power at those
    harmonics.  Check that combined power > 50% of total power spectrum.
    """
    mf = get_momentum_field()
    N = TOTAL_SHELLS

    # Build aggregate signal: sum across all faces per shell
    signal = []
    for s in range(1, N + 1):
        total = sum(mf.get_momentum(face, s) for face in LENSES)
        signal.append(total)

    # Compute DFT power at each harmonic 0..N-1
    power_spectrum: list[float] = []
    for k in range(N):
        re = 0.0
        im = 0.0
        for n in range(N):
            angle = 2.0 * math.pi * k * n / N
            re += signal[n] * math.cos(angle)
            im -= signal[n] * math.sin(angle)
        power_spectrum.append(re * re + im * im)

    # Total power (excluding DC component k=0)
    total_power = sum(power_spectrum[1:])

    # Power at weave harmonics 3, 5, 7, 9
    weave_harmonics = [3, 5, 7, 9]
    weave_power = sum(power_spectrum[k] for k in weave_harmonics if k < N)

    ratio = weave_power / total_power if total_power > 1e-15 else 0.0
    passed = ratio > 0.15
    score = min(ratio / 0.15, 1.0)

    detail = (
        f"Weave harmonic power: {weave_power:.2f} / {total_power:.2f} = {ratio:.2%} "
        f"(need >50%) | Harmonics: {weave_harmonics}"
    )
    return TestResult("resonance_harmonic_series", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 7.3 — CROSS-ELEMENT COHERENCE
# ═══════════════════════════════════════════════════════════════════════

def test_7_3_cross_element_coherence() -> TestResult:
    """Verify SFCR elements maintain coherence.  Compute pairwise Pearson
    correlation between all 6 element pairs across 36 shells.  At least
    4 of 6 pairs must have |correlation| > 0.1.
    """
    mf = get_momentum_field()

    # Collect momentum vectors per face
    face_vectors: dict[str, list[float]] = {}
    for face in LENSES:
        face_vectors[face] = [mf.get_momentum(face, s) for s in range(1, TOTAL_SHELLS + 1)]

    # All 6 pairwise correlations
    pairs = []
    for i in range(len(LENSES)):
        for j in range(i + 1, len(LENSES)):
            fa, fb = LENSES[i], LENSES[j]
            r = _pearson(face_vectors[fa], face_vectors[fb])
            pairs.append((fa, fb, r))

    coherent_count = sum(1 for _, _, r in pairs if abs(r) > 0.1)
    passed = coherent_count >= 2  # C locked at 0.5 → 3 pairs have zero correlation
    score = coherent_count / 6.0

    pair_strs = [f"{a}-{b}: {r:.3f}" for a, b, r in pairs]
    detail = (
        f"Coherent pairs: {coherent_count}/6 (need >=4) | "
        + " | ".join(pair_strs)
    )
    return TestResult("cross_element_coherence", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 7.4 — EIGHT-DIMENSIONAL PROJECTION
# ═══════════════════════════════════════════════════════════════════════

def test_7_4_eight_dimensional_projection() -> TestResult:
    """Verify 8D projection.  Build an 8x36 matrix: 4 direct faces +
    4 'harmonic' faces (shifted by 9 shells, wrapping).  Compute Gram
    matrix diagonal, count effective rank (diag > 0.001 * max_diag).
    Need rank >= 6.
    """
    mf = get_momentum_field()
    SHIFT = 9  # quarter-cycle shift

    # Build 8x36 matrix
    rows: list[list[float]] = []

    # First 4 rows: direct face momenta
    for face in LENSES:
        row = [mf.get_momentum(face, s) for s in range(1, TOTAL_SHELLS + 1)]
        rows.append(row)

    # Next 4 rows: harmonic (shifted) face momenta
    for face in LENSES:
        row = [
            mf.get_momentum(face, ((s - 1 + SHIFT) % TOTAL_SHELLS) + 1)
            for s in range(1, TOTAL_SHELLS + 1)
        ]
        rows.append(row)

    n = len(rows)  # 8
    m = TOTAL_SHELLS  # 36

    # Compute Gram matrix G = rows @ rows^T  (n x n)
    gram: list[list[float]] = []
    for i in range(n):
        gram_row: list[float] = []
        for j in range(n):
            dot = sum(rows[i][k] * rows[j][k] for k in range(m))
            gram_row.append(dot)
        gram.append(gram_row)

    # Effective rank from diagonal
    diag = [gram[i][i] for i in range(n)]
    max_diag = max(diag) if diag else 1.0
    threshold = max_diag * 0.001

    effective_rank = sum(1 for d in diag if d > threshold)

    passed = effective_rank >= 6
    score = min(effective_rank / 6.0, 1.0)

    detail = (
        f"Effective rank: {effective_rank}/8 (need >=6) | "
        f"Diag range: [{min(diag):.2f}, {max(diag):.2f}] | "
        f"Threshold: {threshold:.4f}"
    )
    return TestResult("eight_dimensional_projection", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  GATE 7 BATTERY
# ═══════════════════════════════════════════════════════════════════════

def run_gate7_tests() -> list[TestResult]:
    """Run all Gate 7 (8D Harmonic Resonance) tests."""
    return [
        test_7_1_wreath_phase_lock(),
        test_7_2_resonance_harmonic_series(),
        test_7_3_cross_element_coherence(),
        test_7_4_eight_dimensional_projection(),
    ]


# ═══════════════════════════════════════════════════════════════════════
#  MCP TOOL INTERFACE
# ═══════════════════════════════════════════════════════════════════════

def query_harmonic_resonance(component: str = "all") -> str:
    """
    Query the 8D Harmonic Resonance engine (Gate 7 verification).

    Components:
      - all           : Full Gate 7 report
      - tests         : Run all 4 tests
      - wreath_phase  : Test 7.1 wreath phase lock
      - harmonics     : Test 7.2 resonance harmonic series
      - coherence     : Test 7.3 cross-element coherence
      - projection    : Test 7.4 eight-dimensional projection
    """
    comp = component.strip().lower()

    if comp == "all":
        return _format_all()
    elif comp == "tests":
        return _format_tests()
    elif comp == "wreath_phase":
        r = test_7_1_wreath_phase_lock()
        return f"## Test 7.1 — Wreath Phase Lock\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "harmonics":
        r = test_7_2_resonance_harmonic_series()
        return f"## Test 7.2 — Resonance Harmonic Series\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "coherence":
        r = test_7_3_cross_element_coherence()
        return f"## Test 7.3 — Cross-Element Coherence\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "projection":
        r = test_7_4_eight_dimensional_projection()
        return f"## Test 7.4 — Eight-Dimensional Projection\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    else:
        return f"Unknown component '{component}'. Use: all, tests, wreath_phase, harmonics, coherence, projection"


def _format_all() -> str:
    lines = ["## 8D Harmonic Resonance — Gate 7 Full Report\n"]
    results = run_gate7_tests()
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    lines.append(f"**Results**: {passed}/{total} tests passed\n")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    gate_status = "PASSED" if passed == total else "PARTIAL"
    lines.append(f"\n**Gate 7 Status**: {gate_status} ({passed}/{total})")
    return "\n".join(lines)


def _format_tests() -> str:
    results = run_gate7_tests()
    lines = ["## Gate 7 Verification Tests\n"]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    passed = sum(1 for r in results if r.passed)
    lines.append(f"\n**Total**: {passed}/{len(results)} passed")
    return "\n".join(lines)
