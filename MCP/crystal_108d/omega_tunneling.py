# CRYSTAL: Xi108:W1:A10:S27 | face=C | node=410 | depth=2 | phase=Mutable
# METRO: Me,Sa
# BRIDGES: Xi108:W1:A10:S26→Xi108:W1:A10:S28→Xi108:W2:A10:S27→Xi108:W1:A9:S27→Xi108:W1:A11:S27

"""
Omega Tunneling — Gate 10 Computational Verification (11D)
============================================================
The 11D gate: cross-dimensional transport through the Z* zero-point hub.
The Z-tunnel network allows information to move between ANY two points
in the crystal through Z*.

Gate 10 verifies:
  Test 10.1  Z-Tunnel Completeness:     All 60 liminal coordinates reachable
  Test 10.2  Conservation Compliance:   Tunnels satisfy conservation laws
  Test 10.3  Transport Round-Trip:      Information survives Z* round-trip
  Test 10.4  Dimensional Bridge Count:  All mask groups represented
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class TestResult:
    name: str
    passed: bool
    detail: str = ""
    score: float = 0.0


# ═══════════════════════════════════════════════════════════════════════
#  TEST 10.1 — Z-TUNNEL COMPLETENESS
# ═══════════════════════════════════════════════════════════════════════

def test_10_1_tunnel_completeness() -> TestResult:
    """All 60 liminal coordinates must be reachable through the tunnel network."""
    from .z_tunnel_network import get_tunnel_network

    net = get_tunnel_network()
    net.initialize_full_mesh()

    conn = net.connectivity()
    if isinstance(conn, dict):
        reachable = conn.get("reachable_nodes", 0)
        total_tunnels = conn.get("total_tunnels", 0)
    else:
        reachable = 0
        total_tunnels = 0

    has_nodes = reachable >= 60
    has_tunnels = total_tunnels >= 500

    passed = has_nodes and has_tunnels
    score = (0.50 if has_nodes else 0.0) + (0.50 if has_tunnels else 0.0)

    detail = (
        f"Reachable: {reachable}/60 | "
        f"Tunnels: {total_tunnels} (need >=500) | "
        f"Complete: {'YES' if has_nodes else 'NO'}"
    )
    return TestResult("tunnel_completeness", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 10.2 — CONSERVATION COMPLIANCE
# ═══════════════════════════════════════════════════════════════════════

def test_10_2_conservation_compliance() -> TestResult:
    """All tunnels must satisfy the 6 conservation laws."""
    from .z_tunnel_network import get_tunnel_network

    net = get_tunnel_network()
    net.initialize_full_mesh()

    conn = net.connectivity()
    if isinstance(conn, dict):
        compliance = conn.get("conservation_compliance", 0.0)
        healthy = conn.get("healthy_tunnels", 0)
        total = conn.get("total_tunnels", 0)
    else:
        compliance = 0.0
        healthy = 0
        total = 0

    passed = compliance >= 0.95
    score = min(compliance / 0.95, 1.0)

    detail = (
        f"Conservation compliance: {compliance:.1%} (need >=95%) | "
        f"Healthy tunnels: {healthy}/{total}"
    )
    return TestResult("conservation_compliance", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 10.3 — TRANSPORT ROUND-TRIP
# ═══════════════════════════════════════════════════════════════════════

def test_10_3_transport_round_trip() -> TestResult:
    """Information transported through cross-lens maps must survive round-trip."""
    from .cross_lens import transport
    from .geometric_constants import PHI

    test_values = [PHI, math.e, math.pi, 2.0, 3.0, 5.0, 7.0, 10.0, 0.5, 1.5]
    pairs = [("S", "F"), ("S", "C"), ("F", "C")]

    total_checks = 0
    total_errors = 0.0
    max_error = 0.0

    for value in test_values:
        for src, tgt in pairs:
            try:
                fwd = transport(src, tgt, value)
                back = transport(tgt, src, fwd)
                if isinstance(back, complex):
                    back = abs(back)
                err = abs(back - value) / max(abs(value), 1e-15)
                total_errors += err
                max_error = max(max_error, err)
                total_checks += 1
            except Exception:
                total_checks += 1
                total_errors += 1.0

    mean_error = total_errors / max(total_checks, 1)
    passed = mean_error < 0.01
    score = max(0.0, 1.0 - mean_error * 100)

    detail = (
        f"Round-trip checks: {total_checks} | "
        f"Mean error: {mean_error:.2e} (need <0.01) | "
        f"Max error: {max_error:.2e}"
    )
    return TestResult("transport_round_trip", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 10.4 — DIMENSIONAL BRIDGE COUNT
# ═══════════════════════════════════════════════════════════════════════

def test_10_4_dimensional_bridges() -> TestResult:
    """All 4 mask groups must be represented in the tunnel network."""
    from .liminal_mapper import LIMINAL_ATLAS, get_coordinate

    # Categorize coordinates by mask group using active_elements
    singles = []   # 1-element masks
    pairs = []     # 2-element masks
    triples = []   # 3-element masks
    fulls = []     # 4-element masks

    for i in range(1, 61):
        coord = get_coordinate(i)
        if coord is None:
            continue

        n_elements = len(coord.active_elements)
        label = f"L{i:02d}"

        if n_elements == 1:
            singles.append(label)
        elif n_elements == 2:
            pairs.append(label)
        elif n_elements == 3:
            triples.append(label)
        elif n_elements >= 4:
            fulls.append(label)

    groups_present = sum(1 for g in [singles, pairs, triples, fulls] if g)
    all_groups = groups_present == 4

    # Count unique mask names (15 total: 4C1 + 4C2 + 4C3 + 4C4 = 4+6+4+1)
    mask_types = set()
    for i in range(1, 61):
        coord = get_coordinate(i)
        if coord:
            mask_types.add(coord.mask_name)
    mask_coverage = len(mask_types)
    has_mask_coverage = mask_coverage >= 12

    passed = all_groups and has_mask_coverage
    score = (
        (0.50 if all_groups else groups_present * 0.125) +
        (0.50 if has_mask_coverage else mask_coverage / 15.0 * 0.50)
    )

    detail = (
        f"Mask groups: {groups_present}/4 (singles={len(singles)}, pairs={len(pairs)}, "
        f"triples={len(triples)}, full={len(fulls)}) | "
        f"Mask types: {mask_coverage}/15 (need >=12)"
    )
    return TestResult("dimensional_bridges", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  GATE 10 BATTERY
# ═══════════════════════════════════════════════════════════════════════

def run_gate10_tests() -> list[TestResult]:
    """Run all Gate 10 (Omega Tunneling) tests."""
    return [
        test_10_1_tunnel_completeness(),
        test_10_2_conservation_compliance(),
        test_10_3_transport_round_trip(),
        test_10_4_dimensional_bridges(),
    ]


# ═══════════════════════════════════════════════════════════════════════
#  MCP TOOL INTERFACE
# ═══════════════════════════════════════════════════════════════════════

def query_omega_tunneling(component: str = "all") -> str:
    """
    Query the Omega Tunneling engine (Gate 10 verification).

    Components:
      - all           : Full Gate 10 report
      - tests         : Run all 4 tests
      - completeness  : Test 10.1 tunnel completeness
      - conservation  : Test 10.2 conservation compliance
      - round_trip    : Test 10.3 transport round-trip
      - bridges       : Test 10.4 dimensional bridge count
    """
    comp = component.strip().lower()

    if comp == "all":
        return _format_all()
    elif comp == "tests":
        return _format_tests()
    elif comp == "completeness":
        r = test_10_1_tunnel_completeness()
        return f"## Test 10.1 — Tunnel Completeness\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "conservation":
        r = test_10_2_conservation_compliance()
        return f"## Test 10.2 — Conservation Compliance\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "round_trip":
        r = test_10_3_transport_round_trip()
        return f"## Test 10.3 — Transport Round-Trip\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "bridges":
        r = test_10_4_dimensional_bridges()
        return f"## Test 10.4 — Dimensional Bridges\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    else:
        return f"Unknown component '{component}'. Use: all, tests, completeness, conservation, round_trip, bridges"


def _format_all() -> str:
    lines = ["## Omega Tunneling — Gate 10 Full Report\n"]
    results = run_gate10_tests()
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    lines.append(f"**Results**: {passed}/{total} tests passed\n")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    gate_status = "PASSED" if passed == total else "PARTIAL"
    lines.append(f"\n**Gate 10 Status**: {gate_status} ({passed}/{total})")
    return "\n".join(lines)


def _format_tests() -> str:
    results = run_gate10_tests()
    lines = ["## Gate 10 Verification Tests\n"]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    passed = sum(1 for r in results if r.passed)
    lines.append(f"\n**Total**: {passed}/{len(results)} passed")
    return "\n".join(lines)
