"""
Guild Hall — Social Coordination Query Surface
================================================
Exposes the Guild Hall boards, quests, synthesis, and promotion
membrane as navigable MCP tools. The Guild Hall is the organism's
social coordination organ — where synthesis becomes quests, quests
become artifacts, artifacts become writebacks, and writebacks emit
the next quest loop.

Tools: query_quest, query_synthesis, query_promotion_membrane, guild_hall_status
"""

import os
import re
from pathlib import Path

ATHENA_ROOT = Path(os.environ.get("ATHENA_ROOT", str(Path(__file__).resolve().parent.parent.parent)))
GUILD_HALL = ATHENA_ROOT / "self_actualize" / "mycelium_brain" / "GLOBAL_EMERGENT_GUILD_HALL"
BOARDS_DIR = GUILD_HALL / "BOARDS"

_BOARD_MAP = {
    "message":    "00_MESSAGE_BOARD.md",
    "fronts":     "01_ACTIVE_FRONTS_BOARD.md",
    "plans":      "02_FUTURE_PLANS_BOARD.md",
    "ideas":      "03_ORGANIZATION_IDEAS_BOARD.md",
    "changes":    "04_CHANGE_FEED_BOARD.md",
    "requests":   "05_REQUESTS_AND_OFFERS_BOARD.md",
    "quest":      "06_QUEST_BOARD.md",
    "execution":  "07_57_LOOP_EXECUTION_BOARD.md",
    "changefeed": "08_57_LOOP_CHANGEFEED.md",
    "events":     "09_COMMAND_EVENT_QUEUE_BOARD.md",
    "claims":     "10_COMMAND_CLAIM_LEASE_BOARD.md",
    "quality":    "11_COMMAND_ROUTE_QUALITY_BOARD.md",
}

_SYNTHESIS_MAP = {
    "all":          ("01_FULL_ATHENA_SYNTHESIS.md",            100),
    "full":         ("01_FULL_ATHENA_SYNTHESIS.md",            100),
    "liminal":      ("02_LIMINAL_TRANSITION_MAP.md",            80),
    "capabilities": ("03_EMERGENT_CAPABILITIES.md",             80),
    "leverage":     ("10_FRONTIER_LEVERAGE_RANKING.md",         80),
    "progress":     ("08_WHOLE_ORGANISM_PROGRESS_LEDGER.md",    80),
    "mass":         ("09_SEMANTIC_MASS_LEDGER.md",              80),
}


# ── Helpers ────────────────────────────────────────────────────────


def _read_guild_file(filename: str, limit: int = 100) -> str:
    """Read a Guild Hall file, truncating at *limit* lines."""
    path = GUILD_HALL / filename
    if not path.exists():
        return f"Guild Hall file not found: `{filename}`"
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if len(lines) > limit:
            return "\n".join(lines[:limit]) + f"\n\n... truncated at {limit}/{len(lines)} lines"
        return text
    except Exception as exc:
        return f"Error reading `{filename}`: {exc}"


def _read_board(board_name: str, limit: int = 100) -> str:
    """Read a board file from BOARDS/ directory."""
    filename = _BOARD_MAP.get(board_name.lower())
    if not filename:
        valid = ", ".join(sorted(_BOARD_MAP.keys()))
        return f"Unknown board '{board_name}'. Valid boards: {valid}"
    path = BOARDS_DIR / filename
    if not path.exists():
        return f"Board file not found: `{filename}`"
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if len(lines) > limit:
            return "\n".join(lines[:limit]) + f"\n\n... truncated at {limit}/{len(lines)} lines"
        return text
    except Exception as exc:
        return f"Error reading board `{filename}`: {exc}"


def _count_quests(content: str) -> dict:
    """Parse quest board content to count active/completed/total quests."""
    active = 0
    completed = 0
    total = 0
    for line in content.splitlines():
        ll = line.lower().strip()
        if re.match(r"^[-*]\s", ll) or re.match(r"^#{1,4}\s", ll):
            if any(tag in ll for tag in ["[active]", "[open]", "[in-progress]", "status: active", "status: open"]):
                active += 1
                total += 1
            elif any(tag in ll for tag in ["[completed]", "[landed]", "[promoted]", "[done]", "status: completed", "status: landed"]):
                completed += 1
                total += 1
            elif re.match(r"^[-*]\s+\*\*q", ll) or re.match(r"^#{1,4}\s+q", ll):
                # Lines that look like quest entries (start with Q after bullet/header)
                total += 1
                active += 1  # default to active if no status tag
    return {"active": active, "completed": completed, "total": total}


def _extract_loop_state(content: str) -> str:
    """Extract current loop state from execution board."""
    for line in content.splitlines():
        ll = line.lower().strip()
        if "loop" in ll and ("state" in ll or "phase" in ll or "cycle" in ll or "status" in ll):
            return line.strip()
        if re.match(r"^#{1,3}\s", line) and "loop" in ll:
            return line.strip()
    return "Loop state: unknown"


def _extract_docs_gate(content: str) -> str:
    """Check docs gate status from fronts board content."""
    for line in content.splitlines():
        ll = line.lower().strip()
        if "gate" in ll and ("docs" in ll or "google" in ll):
            return line.strip()
        if "docs_gate" in ll or "doc_gate" in ll:
            return line.strip()
    return ""


# ── Tool Functions ─────────────────────────────────────────────────


def query_quest(quest_id_or_search: str = "all") -> str:
    """
    Query the Guild Hall quest board.

    Components:
      - all          : Quest overview (active quest count, completed count, loop state)
      - active       : All currently active/open quests
      - completed    : All landed/promoted quests
      - board:NAME   : Read a specific board by name (e.g. board:quest, board:message, board:fronts)
      - quest:ID     : Find a specific quest by ID substring
      - search:TERM  : Search across all quest content
    """
    if not GUILD_HALL.exists():
        return "Guild Hall not found. ATHENA_ROOT may not be configured."

    q = quest_id_or_search.strip()
    ql = q.lower()

    if ql == "all":
        return _quest_overview()
    elif ql == "active":
        return _quest_filtered("active")
    elif ql == "completed":
        return _quest_filtered("completed")
    elif ql.startswith("board:"):
        board_name = q.split(":", 1)[1].strip()
        return _read_board(board_name)
    elif ql.startswith("quest:"):
        quest_id = q.split(":", 1)[1].strip()
        return _quest_by_id(quest_id)
    elif ql.startswith("search:"):
        term = q.split(":", 1)[1].strip()
        return _quest_search(term)
    else:
        # Try direct quest ID lookup
        return _quest_by_id(q)


def query_synthesis(section: str = "all") -> str:
    """
    Query the organism synthesis from the Guild Hall.

    Components:
      - all          : Full synthesis overview
      - liminal      : Current liminal transition (N->N+7)
      - capabilities : Emergent capabilities
      - fronts       : Active fronts with leverage ranking
      - leverage     : Frontier leverage ranking
      - progress     : Whole organism progress ledger
      - mass         : Semantic mass ledger
    """
    if not GUILD_HALL.exists():
        return "Guild Hall not found. ATHENA_ROOT may not be configured."

    s = section.strip().lower()

    if s == "fronts":
        return _read_board("fronts", limit=80)

    entry = _SYNTHESIS_MAP.get(s)
    if entry:
        filename, limit = entry
        return _read_guild_file(filename, limit=limit)

    valid = ", ".join(sorted(_SYNTHESIS_MAP.keys()) + ["fronts"])
    return f"Unknown synthesis section '{section}'. Valid: {valid}"


def query_promotion_membrane(quest_id: str = "") -> str:
    """
    Query the Guild Hall promotion membrane.

    Components:
      - (empty)      : Overview of promotion protocol + witness hierarchy
      - quest:ID     : Promotion status of a specific quest
      - ladder       : The full promotion ladder (Signal->Proposal->Quest->Witness->Writeback->Promoted->Restart)
      - witness      : Canonical witness hierarchy
    """
    if not GUILD_HALL.exists():
        return "Guild Hall not found. ATHENA_ROOT may not be configured."

    q = quest_id.strip()
    ql = q.lower()

    if not q:
        return _promotion_overview()
    elif ql == "ladder":
        return _promotion_ladder()
    elif ql == "witness":
        return _read_guild_file("07_CANONICAL_WITNESS_HIERARCHY.md", limit=100)
    elif ql.startswith("quest:"):
        qid = q.split(":", 1)[1].strip()
        return _promotion_quest_status(qid)
    else:
        return _promotion_quest_status(q)


def guild_hall_status() -> str:
    """Compact Guild Hall status for resource endpoint."""
    if not GUILD_HALL.exists():
        return "## Guild Hall\n\n**Status**: not found"

    lines = ["## Guild Hall Status\n"]

    # Active fronts
    fronts_content = _read_board("fronts", limit=200)
    p0 = len(re.findall(r"\bP0\b", fronts_content, re.IGNORECASE))
    p1 = len(re.findall(r"\bP1\b", fronts_content, re.IGNORECASE))
    lines.append(f"**Active Fronts**: P0={p0}, P1={p1}")

    # Quest counts
    quest_content = _read_board("quest", limit=300)
    counts = _count_quests(quest_content)
    lines.append(f"**Quests**: {counts['active']} active, {counts['completed']} completed, {counts['total']} total")

    # Loop state
    exec_content = _read_board("execution", limit=200)
    loop_state = _extract_loop_state(exec_content)
    lines.append(f"**Loop**: {loop_state}")

    # Docs gate
    docs_gate = _extract_docs_gate(fronts_content)
    if docs_gate:
        lines.append(f"**Docs Gate**: {docs_gate}")

    # Board file count
    board_count = len(list(BOARDS_DIR.glob("*.md"))) if BOARDS_DIR.exists() else 0
    guild_count = len(list(GUILD_HALL.glob("*.md"))) if GUILD_HALL.exists() else 0
    lines.append(f"**Files**: {guild_count} guild files, {board_count} boards")

    return "\n".join(lines)


# ── Quest Formatters ───────────────────────────────────────────────


def _quest_overview() -> str:
    """Build quest overview with counts and loop state."""
    quest_content = _read_board("quest", limit=300)
    exec_content = _read_board("execution", limit=200)

    counts = _count_quests(quest_content)
    loop_state = _extract_loop_state(exec_content)

    lines = [
        "## Guild Hall Quest Overview\n",
        f"**Active Quests**: {counts['active']}",
        f"**Completed Quests**: {counts['completed']}",
        f"**Total Quests**: {counts['total']}",
        f"**Loop State**: {loop_state}\n",
        "### Available Boards\n",
    ]
    for name, filename in sorted(_BOARD_MAP.items()):
        path = BOARDS_DIR / filename
        marker = "+" if path.exists() else "-"
        lines.append(f"  {marker} **{name}** — `{filename}`")

    lines.append(f"\n*Use `board:NAME` to read a specific board.*")
    return "\n".join(lines)


def _quest_filtered(status: str) -> str:
    """Return quests filtered by active or completed status."""
    quest_content = _read_board("quest", limit=500)
    if quest_content.startswith("Board file not found") or quest_content.startswith("Unknown board"):
        return quest_content

    active_tags = ["[active]", "[open]", "[in-progress]", "status: active", "status: open"]
    completed_tags = ["[completed]", "[landed]", "[promoted]", "[done]", "status: completed", "status: landed"]
    tags = active_tags if status == "active" else completed_tags
    label = "Active" if status == "active" else "Completed"

    matches = []
    for line in quest_content.splitlines():
        ll = line.lower().strip()
        if any(tag in ll for tag in tags):
            matches.append(line.strip())

    if not matches:
        return f"No {label.lower()} quests found in quest board."

    lines = [f"## {label} Quests ({len(matches)})\n"]
    for m in matches:
        lines.append(f"- {m}")
    return "\n".join(lines)


def _quest_by_id(quest_id: str) -> str:
    """Find a quest by ID substring across quest board and execution board."""
    ql = quest_id.lower()
    results = []

    for board_name in ("quest", "execution"):
        content = _read_board(board_name, limit=500)
        if content.startswith(("Board file not found", "Unknown board", "Error")):
            continue
        block = []
        capturing = False
        for line in content.splitlines():
            if ql in line.lower():
                capturing = True
                block.append(line)
            elif capturing:
                if line.strip() == "" or re.match(r"^#{1,4}\s", line):
                    capturing = False
                    results.append("\n".join(block))
                    block = []
                else:
                    block.append(line)
        if block:
            results.append("\n".join(block))

    if not results:
        return f"No quest matching '{quest_id}' found."
    return f"## Quest: {quest_id}\n\n" + "\n\n---\n\n".join(results)


def _quest_search(term: str) -> str:
    """Search across all board content for a term."""
    tl = term.lower()
    hits = []

    for name, filename in _BOARD_MAP.items():
        path = BOARDS_DIR / filename
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if tl in line.lower():
                hits.append((name, i, line.strip()))

    if not hits:
        return f"No results for '{term}' across Guild Hall boards."

    lines = [f"## Search: '{term}' ({len(hits)} hits)\n"]
    for board, lineno, text in hits[:30]:
        lines.append(f"- **{board}** L{lineno}: {text}")
    if len(hits) > 30:
        lines.append(f"\n... and {len(hits) - 30} more hits")
    return "\n".join(lines)


# ── Promotion Formatters ──────────────────────────────────────────


def _promotion_overview() -> str:
    """Overview combining promotion protocol and witness hierarchy."""
    protocol = _read_guild_file("06_GUILD_PROMOTION_PROTOCOL.md", limit=60)
    witness = _read_guild_file("07_CANONICAL_WITNESS_HIERARCHY.md", limit=40)

    lines = [
        "## Guild Hall Promotion Membrane\n",
        "### Promotion Protocol\n",
        protocol,
        "\n### Witness Hierarchy\n",
        witness,
    ]
    return "\n".join(lines)


def _promotion_ladder() -> str:
    """Extract the promotion ladder from the protocol file."""
    content = _read_guild_file("06_GUILD_PROMOTION_PROTOCOL.md", limit=200)
    lines = [
        "## Promotion Ladder\n",
        "```",
        "Signal -> Proposal -> Quest -> Witness -> Writeback -> Promoted -> Restart",
        "```\n",
    ]

    # Extract ladder-related sections from the protocol
    capturing = False
    for line in content.splitlines():
        ll = line.lower().strip()
        if any(kw in ll for kw in ["ladder", "stage", "phase", "step", "promotion"]):
            capturing = True
        if capturing:
            lines.append(line)
            if line.strip() == "" and len(lines) > 10:
                capturing = False

    return "\n".join(lines)


def _promotion_quest_status(quest_id: str) -> str:
    """Find promotion status of a specific quest."""
    ql = quest_id.lower()

    # Search promotion protocol for the quest
    protocol = _read_guild_file("06_GUILD_PROMOTION_PROTOCOL.md", limit=300)
    quest_board = _read_board("quest", limit=500)

    hits = []
    for source, content in [("protocol", protocol), ("quest_board", quest_board)]:
        for line in content.splitlines():
            if ql in line.lower():
                hits.append((source, line.strip()))

    if not hits:
        return f"No promotion data for quest '{quest_id}'."

    lines = [f"## Promotion Status: {quest_id}\n"]
    for source, text in hits:
        lines.append(f"- **{source}**: {text}")
    return "\n".join(lines)
