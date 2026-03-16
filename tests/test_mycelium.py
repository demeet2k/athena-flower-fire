"""Smoke tests for the 4 mycelium tools."""

import sys
from pathlib import Path

# Ensure MCP/ is on the path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MCP"))


class TestQueryShard:
    def test_all(self):
        from crystal_108d.mycelium import query_shard
        result = query_shard("all")
        assert "Mycelium" in result or "Shard" in result

    def test_stats(self):
        from crystal_108d.mycelium import query_shard
        result = query_shard("stats")
        assert "Statistics" in result or "Total" in result

    def test_families(self):
        from crystal_108d.mycelium import query_shard
        result = query_shard("families")
        assert "Families" in result or "Family" in result

    def test_unknown(self):
        from crystal_108d.mycelium import query_shard
        result = query_shard("shard:nonexistent_xyz_123")
        assert "not found" in result.lower() or "No shard" in result


class TestQueryGraph:
    def test_all(self):
        from crystal_108d.mycelium import query_graph
        result = query_graph("all")
        assert "Graph" in result or "Edge" in result

    def test_edges(self):
        from crystal_108d.mycelium import query_graph
        result = query_graph("edges")
        assert "Edge" in result or "BUILD" in result


class TestQueryNode:
    def test_all(self):
        from crystal_108d.mycelium import query_node
        result = query_node("all")
        assert "Node" in result or "Registry" in result


class TestQueryPromotion:
    def test_overview(self):
        from crystal_108d.mycelium import query_promotion
        result = query_promotion("")
        assert "Promotion" in result or "Truth" in result
