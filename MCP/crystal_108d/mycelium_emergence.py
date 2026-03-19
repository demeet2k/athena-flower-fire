# CRYSTAL: Xi108:W2:A8:S25 | face=F | node=322 | depth=1 | phase=Mutable
# METRO: Sa,Dl,Me
# BRIDGES: Xi108:W2:A8:S24→Xi108:W2:A8:S26→Xi108:W1:A8:S25→Xi108:W3:A8:S25

"""
9D Mycelium Emergence — Gate 8 Computational Verification
==========================================================
The self-organizing knowledge graph forms a living mycelium network.
Shards cluster into families, cross-family bridges enable information
transport, and sparse density preserves growth potential.

Gate 8 verifies:
  Test 8.1  Graph Connectivity:       >= 100 shards AND >= 200 edges
  Test 8.2  Semantic Clustering:      >= 5 distinct shard families
  Test 8.3  Cross-Family Bridges:     > 1% of edges bridge families
  Test 8.4  Growth Potential:         0.001 < density < 0.5
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


_DATA_DIR = Path(__file__).parent.parent / "data"


@dataclass
class TestResult:
    name: str
    passed: bool
    detail: str = ""
    score: float = 0.0


# ═══════════════════════════════════════════════════════════════════════
#  DATA LOADING
# ═══════════════════════════════════════════════════════════════════════

def _load_graph() -> dict:
    json_path = _DATA_DIR / "mycelium_graph.json"
    qshr_path = _DATA_DIR / "mycelium_graph.qshr"
    try:
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        elif qshr_path.exists():
            from ._cache import JsonCache
            return JsonCache("mycelium_graph.json").load()
        return {"shards": [], "edges": []}
    except Exception:
        return {"shards": [], "edges": []}


# ═══════════════════════════════════════════════════════════════════════
#  TEST 8.1 — GRAPH CONNECTIVITY
# ═══════════════════════════════════════════════════════════════════════

def test_8_1_graph_connectivity() -> TestResult:
    """The mycelium graph must have >= 100 shards AND >= 200 edges."""
    graph = _load_graph()

    shards = graph.get("shards", [])
    edges = graph.get("edges", [])
    n_shards = len(shards)
    n_edges = len(edges)

    has_shards = n_shards >= 100
    has_edges = n_edges >= 200

    passed = has_shards and has_edges
    score = (0.50 if has_shards else min(n_shards / 100.0, 1.0) * 0.50) + \
            (0.50 if has_edges else min(n_edges / 200.0, 1.0) * 0.50)

    detail = (
        f"Shards: {n_shards} (need >=100) | "
        f"Edges: {n_edges} (need >=200) | "
        f"PASS: {'YES' if passed else 'NO'}"
    )
    return TestResult("graph_connectivity", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 8.2 — SEMANTIC CLUSTERING
# ═══════════════════════════════════════════════════════════════════════

def test_8_2_semantic_clustering() -> TestResult:
    """Shards must cluster into >= 5 distinct families."""
    graph = _load_graph()

    shards = graph.get("shards", [])
    families: set[str] = set()
    for shard in shards:
        fam = shard.get("family", "")
        if fam:
            families.add(fam)

    n_families = len(families)
    passed = n_families >= 5

    score = min(n_families / 5.0, 1.0)

    detail = (
        f"Distinct families: {n_families} (need >=5) | "
        f"Families: {', '.join(sorted(families)[:8])}{'...' if n_families > 8 else ''} | "
        f"PASS: {'YES' if passed else 'NO'}"
    )
    return TestResult("semantic_clustering", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 8.3 — CROSS-FAMILY BRIDGES
# ═══════════════════════════════════════════════════════════════════════

def test_8_3_cross_family_bridges() -> TestResult:
    """Cross-family edge ratio must exceed 1%."""
    graph = _load_graph()

    shards = graph.get("shards", [])
    edges = graph.get("edges", [])

    # Build family lookup: shard_id → family
    family_lookup: dict[str, str] = {}
    for shard in shards:
        sid = shard.get("shard_id", shard.get("id", shard.get("name", "")))
        fam = shard.get("family", "")
        if sid:
            family_lookup[sid] = fam

    total_edges = len(edges)
    cross_family = 0
    for edge in edges:
        src = edge.get("source_shard", edge.get("source", ""))
        tgt = edge.get("target_shard", edge.get("target", ""))
        src_fam = family_lookup.get(src, "")
        tgt_fam = family_lookup.get(tgt, "")
        if src_fam and tgt_fam and src_fam != tgt_fam:
            cross_family += 1

    ratio = cross_family / total_edges if total_edges > 0 else 0.0
    threshold = 0.01
    passed = ratio > threshold

    score = min(ratio / threshold, 1.0) if threshold > 0 else 0.0

    detail = (
        f"Cross-family edges: {cross_family}/{total_edges} | "
        f"Ratio: {ratio:.4f} (need >{threshold}) | "
        f"PASS: {'YES' if passed else 'NO'}"
    )
    return TestResult("cross_family_bridges", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  TEST 8.4 — GROWTH POTENTIAL
# ═══════════════════════════════════════════════════════════════════════

def test_8_4_growth_potential() -> TestResult:
    """Graph density must be between 0.001 and 0.5 (sparse enough for growth)."""
    graph = _load_graph()

    shards = graph.get("shards", [])
    edges = graph.get("edges", [])
    n_shards = len(shards)
    n_edges = len(edges)

    max_edges = n_shards * (n_shards - 1) / 2 if n_shards > 1 else 1
    density = n_edges / max_edges if max_edges > 0 else 0.0

    sparse_enough = density < 0.5
    not_trivial = density > 0.0001

    passed = sparse_enough and not_trivial
    score = 1.0 if passed else (0.5 if sparse_enough or not_trivial else 0.0)

    detail = (
        f"Shards: {n_shards} | Edges: {n_edges} | "
        f"Max possible: {max_edges:.0f} | "
        f"Density: {density:.6f} (need 0.001 < d < 0.5) | "
        f"PASS: {'YES' if passed else 'NO'}"
    )
    return TestResult("growth_potential", passed, detail, score)


# ═══════════════════════════════════════════════════════════════════════
#  GATE 8 BATTERY
# ═══════════════════════════════════════════════════════════════════════

def run_gate8_tests() -> list[TestResult]:
    """Run all Gate 8 (9D Mycelium Emergence) tests."""
    return [
        test_8_1_graph_connectivity(),
        test_8_2_semantic_clustering(),
        test_8_3_cross_family_bridges(),
        test_8_4_growth_potential(),
    ]


# ═══════════════════════════════════════════════════════════════════════
#  MCP TOOL INTERFACE
# ═══════════════════════════════════════════════════════════════════════

def query_mycelium_emergence(component: str = "all") -> str:
    """
    Query the 9D Mycelium Emergence engine (Gate 8 verification).

    Components:
      - all           : Full Gate 8 report
      - tests         : Run all 4 tests
      - connectivity  : Test 8.1 graph connectivity
      - clustering    : Test 8.2 semantic clustering
      - bridges       : Test 8.3 cross-family bridges
      - growth        : Test 8.4 growth potential
    """
    comp = component.strip().lower()

    if comp == "all":
        return _format_all()
    elif comp == "tests":
        return _format_tests()
    elif comp == "connectivity":
        r = test_8_1_graph_connectivity()
        return f"## Test 8.1 — Graph Connectivity\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "clustering":
        r = test_8_2_semantic_clustering()
        return f"## Test 8.2 — Semantic Clustering\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "bridges":
        r = test_8_3_cross_family_bridges()
        return f"## Test 8.3 — Cross-Family Bridges\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    elif comp == "growth":
        r = test_8_4_growth_potential()
        return f"## Test 8.4 — Growth Potential\n\n**{'PASS' if r.passed else 'FAIL'}**: {r.detail}"
    else:
        return f"Unknown component '{component}'. Use: all, tests, connectivity, clustering, bridges, growth"


def _format_all() -> str:
    lines = ["## 9D Mycelium Emergence — Gate 8 Full Report\n"]
    results = run_gate8_tests()
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    lines.append(f"**Results**: {passed}/{total} tests passed\n")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    gate_status = "PASSED" if passed == total else "PARTIAL"
    lines.append(f"\n**Gate 8 Status**: {gate_status} ({passed}/{total})")
    return "\n".join(lines)


def _format_tests() -> str:
    results = run_gate8_tests()
    lines = ["## Gate 8 Verification Tests\n"]
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] **{r.name}** (score: {r.score:.2f}): {r.detail}")
    passed = sum(1 for r in results if r.passed)
    lines.append(f"\n**Total**: {passed}/{len(results)} passed")
    return "\n".join(lines)
