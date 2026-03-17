"""Smoke tests for the 4 guild hall tools."""

import sys
from pathlib import Path

# Ensure MCP/ is on the path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MCP"))


class TestQueryQuest:
    def test_all(self):
        from crystal_108d.guild_hall import query_quest
        result = query_quest("all")
        assert "Quest" in result or "Guild Hall" in result

    def test_active(self):
        from crystal_108d.guild_hall import query_quest
        result = query_quest("active")
        assert isinstance(result, str)

    def test_board(self):
        from crystal_108d.guild_hall import query_quest
        result = query_quest("board:quest")
        assert isinstance(result, str)

    def test_unknown(self):
        from crystal_108d.guild_hall import query_quest
        result = query_quest("quest:nonexistent_xyz_123")
        assert "not found" in result.lower() or "No quest" in result


class TestQuerySynthesis:
    def test_all(self):
        from crystal_108d.guild_hall import query_synthesis
        result = query_synthesis("all")
        assert isinstance(result, str)

    def test_liminal(self):
        from crystal_108d.guild_hall import query_synthesis
        result = query_synthesis("liminal")
        assert isinstance(result, str)

    def test_unknown(self):
        from crystal_108d.guild_hall import query_synthesis
        result = query_synthesis("nonexistent_section")
        assert "Unknown" in result or "Valid" in result


class TestQueryPromotionMembrane:
    def test_overview(self):
        from crystal_108d.guild_hall import query_promotion_membrane
        result = query_promotion_membrane("")
        assert "Promotion" in result or "Guild Hall" in result

    def test_ladder(self):
        from crystal_108d.guild_hall import query_promotion_membrane
        result = query_promotion_membrane("ladder")
        assert "Signal" in result or "Promotion" in result


class TestGuildHallStatus:
    def test_status(self):
        from crystal_108d.guild_hall import guild_hall_status
        result = guild_hall_status()
        assert "Guild Hall" in result
