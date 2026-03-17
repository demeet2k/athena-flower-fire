"""
Athena Mycelium Graph Generator
================================
Scans MCP/data/*.json, MCP/crystal_108d/*.py, and MCP/element_servers/*.py
to produce the universal shard/edge graph manifest.

Usage:
    python -X utf8 MCP/generate_graph.py

Emits:
    MCP/data/mycelium_graph.json
    MCP/data/node_registry.json
"""

import json
import re
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

# Ensure MCP/ is importable
_MCP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_MCP_DIR))
os.environ.setdefault("ATHENA_ROOT", str(_MCP_DIR.parent))

from crystal_108d.metabolism import (
    Shard, Edge, make_shard_id, make_edge_id, to_dict, now_iso,
)

DATA_DIR = _MCP_DIR / "data"
CRYSTAL_DIR = _MCP_DIR / "crystal_108d"
ELEMENT_DIR = _MCP_DIR / "element_servers"
GUILD_HALL_DIR = _MCP_DIR.parent / "self_actualize" / "mycelium_brain" / "GLOBAL_EMERGENT_GUILD_HALL"
ATHENA_REPO_DIR = Path(os.environ.get("ATHENA_REPO", str(Path.home() / "Documents" / "athena")))

NOW = now_iso()

# ── Family inference from filename ──────────────────────────────────

FAMILY_MAP = {
    "shell_registry": "shells",
    "hologram_chapters": "hologram",
    "dimensional_ladder": "dimensions",
    "organ_atlas": "organs",
    "live_lock_registry": "live_lock",
    "clock_projections": "clock",
    "move_primitives": "moves",
    "metro_lines": "metro",
    "z_point_hierarchy": "z_points",
    "conservation_laws": "conservation",
    "overlay_registries": "overlays",
    "transport_stacks": "transport",
    "mobius_lenses": "mobius",
    "stage_codes": "stages",
    "angel_object": "angel",
    "brain_network": "brain",
    "live_cell_constitution": "live_cell",
    "dimensional_emergence": "emergence",
    "hologram_reading": "hologram",
    "hologram_rosetta": "hologram",
    "angel_geometry": "angel",
    "angel_conservation": "angel",
    "inverse_crystal_seed": "inverse_crystal",
    "inverse_crystal_octave": "inverse_crystal",
    "inverse_crystal_complete": "inverse_crystal",
}

MODULE_FAMILY_MAP = {
    "shells": "shells",
    "dimensions": "dimensions",
    "organs": "organs",
    "address": "address",
    "live_lock": "live_lock",
    "clock": "clock",
    "moves": "moves",
    "metro_lines": "metro",
    "z_points": "z_points",
    "conservation": "conservation",
    "overlays": "overlays",
    "transport": "transport",
    "mobius_lenses": "mobius",
    "stage_codes": "stages",
    "angel": "angel",
    "angel_geometry": "angel",
    "brain": "brain",
    "live_cell": "live_cell",
    "emergence": "emergence",
    "hologram_reading": "hologram",
    "inverse_seed": "inverse_crystal",
    "inverse_octave": "inverse_crystal",
    "inverse_complete": "inverse_crystal",
    "metabolism": "mycelium",
    "mycelium": "mycelium",
}

ELEMENT_LENS = {
    "square_server": "S",
    "flower_server": "F",
    "cloud_server": "C",
    "fractal_server": "R",
}

SKIP_MODULES = {"__init__", "_cache", "constants", "__pycache__"}

MANUSCRIPT_MODULE_FAMILY = {
    "address": "crystal",
    "parse_kernel": "kernel",
    "wave_engine": "kernel",
    "lattice": "crystal",
    "gate": "crystal",
    "router": "metro",
    "schedule": "metro",
    "certificate": "proof",
    "conservation": "proof",
    "seed": "replication",
    "corridor": "truth",
    "witness": "truth",
    "collective": "swarm",
    "stack": "transport",
    "sfcr": "lens",
    "field": "tensor",
    "regeneration": "cycle",
    "store": "memory",
    "runtime": "agent",
    "executor": "runtime",
}


def _infer_family(stem: str) -> str:
    return FAMILY_MAP.get(stem, stem.replace("_", "-"))


def _extract_docstring(path: Path) -> str:
    """Extract first line of module docstring."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r'"""(.*?)"""', text, re.DOTALL)
        if m:
            first = m.group(1).strip().split("\n")[0].strip()
            if first and len(first) > 5:
                return first
        m = re.search(r"'''(.*?)'''", text, re.DOTALL)
        if m:
            first = m.group(1).strip().split("\n")[0].strip()
            if first and len(first) > 5:
                return first
    except Exception:
        pass
    return f"Module {path.stem}"


def _extract_json_caches(path: Path) -> list[str]:
    """Find all JsonCache('filename.json') references in a Python file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return re.findall(r'JsonCache\(["\']([^"\']+\.json)["\']\)', text)
    except Exception:
        return []


def _extract_json_title(path: Path) -> str:
    """Extract meta.title from a JSON file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "meta" in data:
            return data["meta"].get("title", path.stem)
    except Exception:
        pass
    return path.stem


def _infer_dimensional_scope(data: dict, stem: str) -> str:
    """Infer dimensional scope from JSON content."""
    if "dimension" in str(data).lower()[:200]:
        return "3D-12D"
    if "108" in stem or "shell" in stem:
        return "108D"
    if "brain" in stem:
        return "4D-10D"
    if "angel" in stem:
        return "all"
    if "inverse_crystal" in stem:
        return "3D-108D"
    if "hologram" in stem:
        return "all"
    if "emergence" in stem:
        return "3D-A+"
    return "all"


def _infer_seed_vector(family: str, lens: str | None) -> list[float]:
    """Infer SFCR seed vector from family and lens."""
    if lens == "S":
        return [1.0, 0.0, 0.0, 0.0]
    if lens == "F":
        return [0.0, 1.0, 0.0, 0.0]
    if lens == "C":
        return [0.0, 0.0, 1.0, 0.0]
    if lens == "R":
        return [0.0, 0.0, 0.0, 1.0]
    # Universal — balanced
    return [0.25, 0.25, 0.25, 0.25]


# ── Scan Functions ──────────────────────────────────────────────────

def scan_json_data() -> list[Shard]:
    """Scan MCP/data/*.json and create shards."""
    shards = []
    for fp in sorted(DATA_DIR.glob("*.json")):
        stem = fp.stem
        rel = f"data/{fp.name}"
        sid = make_shard_id("json", rel)
        title = _extract_json_title(fp)
        family = _infer_family(stem)

        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            data = {}

        shards.append(Shard(
            shard_id=sid,
            lineage_id=sid,
            medium="json",
            repo="athena-mcp-server",
            lens=None,
            dimensional_scope=_infer_dimensional_scope(data, stem),
            payload_ref=rel,
            summary=title,
            seed_vector=_infer_seed_vector(family, None),
            route_refs=[],
            cert_refs=[],
            mirror_refs=[],
            truth_status="CANONICAL",
            promotion_status="PROMOTED",
            family=family,
            tags=[stem],
            created_at=NOW,
            updated_at=NOW,
        ))
    return shards


def scan_crystal_modules() -> list[Shard]:
    """Scan MCP/crystal_108d/*.py and create shards."""
    shards = []
    for fp in sorted(CRYSTAL_DIR.glob("*.py")):
        if fp.stem in SKIP_MODULES:
            continue
        rel = f"crystal_108d/{fp.name}"
        sid = make_shard_id("code", rel)
        summary = _extract_docstring(fp)
        family = MODULE_FAMILY_MAP.get(fp.stem, fp.stem)

        shards.append(Shard(
            shard_id=sid,
            lineage_id=sid,
            medium="code",
            repo="athena-mcp-server",
            lens=None,
            dimensional_scope="all",
            payload_ref=rel,
            summary=summary,
            seed_vector=[0.25, 0.25, 0.25, 0.25],
            route_refs=[],
            cert_refs=[],
            mirror_refs=[],
            truth_status="CANONICAL",
            promotion_status="PROMOTED",
            family=family,
            tags=[fp.stem, "tool_module"],
            created_at=NOW,
            updated_at=NOW,
        ))
    return shards


def scan_element_servers() -> list[Shard]:
    """Scan MCP/element_servers/*.py and create shards."""
    shards = []
    for fp in sorted(ELEMENT_DIR.glob("*.py")):
        if fp.stem == "__init__":
            continue
        rel = f"element_servers/{fp.name}"
        sid = make_shard_id("code", rel)
        summary = _extract_docstring(fp)
        lens = ELEMENT_LENS.get(fp.stem)
        family = "brain"

        shards.append(Shard(
            shard_id=sid,
            lineage_id=sid,
            medium="code",
            repo="athena-mcp-server",
            lens=lens,
            dimensional_scope="all",
            payload_ref=rel,
            summary=summary,
            seed_vector=_infer_seed_vector(family, lens),
            route_refs=[],
            cert_refs=[],
            mirror_refs=[],
            truth_status="CANONICAL",
            promotion_status="PROMOTED",
            family=family,
            tags=[fp.stem, "element_server", f"lens_{lens}"],
            created_at=NOW,
            updated_at=NOW,
        ))
    return shards


def scan_main_server() -> Shard:
    """Create a shard for the main server entry point."""
    rel = "athena_mcp_server.py"
    sid = make_shard_id("code", rel)
    return Shard(
        shard_id=sid,
        lineage_id=sid,
        medium="code",
        repo="athena-mcp-server",
        lens=None,
        dimensional_scope="all",
        payload_ref=rel,
        summary="Athena MCP Server — unified 64-tool entry point",
        seed_vector=[0.25, 0.25, 0.25, 0.25],
        route_refs=[],
        cert_refs=[],
        mirror_refs=[],
        truth_status="CANONICAL",
        promotion_status="PROMOTED",
        family="server",
        tags=["entry_point", "mcp_server"],
        created_at=NOW,
        updated_at=NOW,
    )


def scan_guild_hall() -> list[Shard]:
    """Scan Guild Hall markdown files and create shards."""
    shards = []
    if not GUILD_HALL_DIR.exists():
        return shards
    for fp in sorted(GUILD_HALL_DIR.glob("**/*.md")):
        rel = str(fp.relative_to(GUILD_HALL_DIR.parent.parent.parent))
        sid = make_shard_id("doc", rel)
        title = fp.stem.replace("_", " ").title()
        # Infer family from path
        if "BOARDS" in str(fp):
            family = "quest"
        elif "SYNTHESIS" in str(fp) or "SYNTHESIS" in fp.stem:
            family = "synthesis"
        elif "PROMOTION" in str(fp) or "WITNESS" in str(fp):
            family = "guild_hall"
        else:
            family = "guild_hall"

        shards.append(Shard(
            shard_id=sid,
            lineage_id=sid,
            medium="doc",
            repo="athena-mcp-server",
            lens=None,
            dimensional_scope="all",
            payload_ref=rel,
            summary=title,
            seed_vector=[0.25, 0.25, 0.25, 0.25],
            route_refs=[],
            cert_refs=[],
            mirror_refs=[],
            truth_status="CANONICAL",
            promotion_status="PROMOTED",
            family=family,
            tags=[fp.stem, "guild_hall"],
            created_at=NOW,
            updated_at=NOW,
        ))
    return shards


def scan_manuscript_being() -> list[Shard]:
    """Scan the manuscript-being Python framework modules."""
    shards = []
    src_dir = ATHENA_REPO_DIR / "src" / "athena"
    if not src_dir.exists():
        return shards
    for fp in sorted(src_dir.glob("**/*.py")):
        if fp.stem.startswith("_"):
            continue
        rel = str(fp.relative_to(ATHENA_REPO_DIR))
        sid = make_shard_id("code", f"manuscript-being/{rel}")
        summary = _extract_docstring(fp)
        family = MANUSCRIPT_MODULE_FAMILY.get(fp.stem, fp.parent.name)

        shards.append(Shard(
            shard_id=sid,
            lineage_id=sid,
            medium="code",
            repo="manuscript-being",
            lens=None,
            dimensional_scope="all",
            payload_ref=rel,
            summary=summary,
            seed_vector=[0.25, 0.25, 0.25, 0.25],
            route_refs=[],
            cert_refs=[],
            mirror_refs=[],
            truth_status="CANONICAL",
            promotion_status="PROMOTED",
            family=family,
            tags=[fp.stem, "manuscript_being", fp.parent.name],
            created_at=NOW,
            updated_at=NOW,
        ))
    return shards


# ── Edge Building ───────────────────────────────────────────────────

def build_edges(shards: list[Shard]) -> list[Edge]:
    """Build typed edges from shard relationships."""
    edges = []
    shard_by_ref = {s.payload_ref: s.shard_id for s in shards}
    shard_by_stem = {}
    for s in shards:
        stem = s.payload_ref.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        shard_by_stem[stem] = s.shard_id

    # BUILD edges: code modules → their JsonCache data files
    for fp in sorted(CRYSTAL_DIR.glob("*.py")):
        if fp.stem in SKIP_MODULES:
            continue
        code_ref = f"crystal_108d/{fp.name}"
        code_sid = shard_by_ref.get(code_ref)
        if not code_sid:
            continue

        for json_name in _extract_json_caches(fp):
            data_ref = f"data/{json_name}"
            data_sid = shard_by_ref.get(data_ref)
            if data_sid:
                eid = make_edge_id(code_sid, data_sid, "BUILD")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=code_sid,
                    target_shard=data_sid,
                    edge_type="BUILD",
                    weight=0.8,
                    medium_cross=False,
                    metadata={"json_file": json_name},
                ))

    # BRIDGE edges: element servers → brain_network entry
    brain_sid = shard_by_ref.get("data/brain_network.json")
    if brain_sid:
        for fp in sorted(ELEMENT_DIR.glob("*.py")):
            if fp.stem == "__init__":
                continue
            srv_ref = f"element_servers/{fp.name}"
            srv_sid = shard_by_ref.get(srv_ref)
            if srv_sid:
                eid = make_edge_id(srv_sid, brain_sid, "BRIDGE")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=srv_sid,
                    target_shard=brain_sid,
                    edge_type="BRIDGE",
                    weight=0.618,
                    medium_cross=False,
                    metadata={"bridge_type": "element_to_brain"},
                ))

    # MIRROR edges: element servers ↔ main server
    main_sid = shard_by_ref.get("athena_mcp_server.py")
    if main_sid:
        for fp in sorted(ELEMENT_DIR.glob("*.py")):
            if fp.stem == "__init__":
                continue
            srv_ref = f"element_servers/{fp.name}"
            srv_sid = shard_by_ref.get(srv_ref)
            if srv_sid:
                eid = make_edge_id(srv_sid, main_sid, "MIRROR")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=srv_sid,
                    target_shard=main_sid,
                    edge_type="MIRROR",
                    weight=0.5,
                    medium_cross=False,
                    metadata={"mirror_type": "lobe_to_unified"},
                ))

    # REF edges: JSON files in same family
    family_groups: dict[str, list[str]] = {}
    for s in shards:
        if s.medium == "json":
            family_groups.setdefault(s.family, []).append(s.shard_id)
    for family, sids in family_groups.items():
        if len(sids) > 1:
            for i, a in enumerate(sids):
                for b in sids[i + 1:]:
                    eid = make_edge_id(a, b, "REF")
                    edges.append(Edge(
                        edge_id=eid,
                        source_shard=a,
                        target_shard=b,
                        edge_type="REF",
                        weight=0.7,
                        medium_cross=False,
                        metadata={"family": family},
                    ))

    # BRIDGE edges: guild hall shards → MCP data shards
    guild_shards = [s for s in shards if "guild_hall" in s.tags]
    mcp_data_shards = [s for s in shards if s.medium == "json"]
    if guild_shards and mcp_data_shards:
        # Connect guild hall to brain_network
        if brain_sid:
            for gs in guild_shards:
                eid = make_edge_id(gs.shard_id, brain_sid, "BRIDGE")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=gs.shard_id,
                    target_shard=brain_sid,
                    edge_type="BRIDGE",
                    weight=0.5,
                    medium_cross=True,
                    metadata={"bridge_type": "guild_hall_to_brain"},
                ))

    # BRIDGE edges: manuscript-being modules → MCP tool modules
    ms_shards = [s for s in shards if s.repo == "manuscript-being"]
    mcp_code_shards = [s for s in shards if s.repo == "athena-mcp-server" and s.medium == "code"]
    for ms in ms_shards:
        # Connect manuscript-being modules to their MCP counterparts by family
        for mcp in mcp_code_shards:
            if ms.family == mcp.family or ms.family in mcp.tags:
                eid = make_edge_id(ms.shard_id, mcp.shard_id, "BRIDGE")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=ms.shard_id,
                    target_shard=mcp.shard_id,
                    edge_type="BRIDGE",
                    weight=0.618,
                    medium_cross=False,
                    metadata={"bridge_type": "manuscript_to_mcp"},
                ))
                break  # one bridge per manuscript module

    # SEEDS edge: main server → all element servers
    if main_sid:
        for fp in sorted(ELEMENT_DIR.glob("*.py")):
            if fp.stem == "__init__":
                continue
            srv_ref = f"element_servers/{fp.name}"
            srv_sid = shard_by_ref.get(srv_ref)
            if srv_sid:
                eid = make_edge_id(main_sid, srv_sid, "SEEDS")
                edges.append(Edge(
                    edge_id=eid,
                    source_shard=main_sid,
                    target_shard=srv_sid,
                    edge_type="SEEDS",
                    weight=0.9,
                    medium_cross=False,
                    metadata={"seed_type": "unified_to_lobe"},
                ))

    return edges


# ── Node Registry ───────────────────────────────────────────────────

def build_node_registry() -> list[dict]:
    """Build the node registry for all Athena nodes."""
    return [
        {
            "node_id": "athena-mcp-server",
            "role": "unified",
            "medium_class": "code",
            "lobe_affinity": None,
            "shard_families": ["all"],
            "mirrors": ["athena-square-earth", "athena-flower-fire", "athena-cloud-water", "athena-fractal-air"],
            "bridges": [
                {"type": "git_to_mcp", "description": "Git state exposed via 68 MCP tools + 21 resources"},
                {"type": "element_to_unified", "description": "4 element servers mirror unified tool subsets"},
            ],
            "cert_capabilities": ["STRUCTURAL", "CONSERVATION"],
            "read_surfaces": ["mcp_tool", "mcp_resource", "file_read", "git_log"],
            "write_surfaces": ["file_write", "git_commit"],
            "sync_sources": ["https://github.com/demeet2k/athena-mcp-server"],
            "github_repo": "https://github.com/demeet2k/athena-mcp-server",
            "tool_count": 71,
            "resource_count": 23,
        },
        {
            "node_id": "athena-square-earth",
            "role": "lobe",
            "medium_class": "code",
            "lobe_affinity": "S",
            "shard_families": ["shells", "dimensions", "address", "conservation", "hologram", "inverse_crystal", "angel"],
            "mirrors": ["athena-mcp-server"],
            "bridges": [{"type": "lobe_to_unified", "description": "Mirrors unified server's structure/address tools"}],
            "cert_capabilities": ["STRUCTURAL"],
            "read_surfaces": ["mcp_tool", "mcp_resource"],
            "write_surfaces": [],
            "sync_sources": ["https://github.com/demeet2k/athena-square-earth"],
            "github_repo": "https://github.com/demeet2k/athena-square-earth",
            "tool_count": 17,
            "resource_count": 1,
        },
        {
            "node_id": "athena-flower-fire",
            "role": "lobe",
            "medium_class": "code",
            "lobe_affinity": "F",
            "shard_families": ["metro", "clock", "moves", "transport", "z_points", "inverse_crystal"],
            "mirrors": ["athena-mcp-server"],
            "bridges": [{"type": "lobe_to_unified", "description": "Mirrors unified server's dynamics/corridor tools"}],
            "cert_capabilities": [],
            "read_surfaces": ["mcp_tool", "mcp_resource"],
            "write_surfaces": [],
            "sync_sources": ["https://github.com/demeet2k/athena-flower-fire"],
            "github_repo": "https://github.com/demeet2k/athena-flower-fire",
            "tool_count": 15,
            "resource_count": 1,
        },
        {
            "node_id": "athena-cloud-water",
            "role": "lobe",
            "medium_class": "code",
            "lobe_affinity": "C",
            "shard_families": ["conservation", "hologram", "angel", "brain"],
            "mirrors": ["athena-mcp-server"],
            "bridges": [{"type": "lobe_to_unified", "description": "Mirrors unified server's observation tools"}],
            "cert_capabilities": ["CONSERVATION"],
            "read_surfaces": ["mcp_tool", "mcp_resource"],
            "write_surfaces": [],
            "sync_sources": ["https://github.com/demeet2k/athena-cloud-water"],
            "github_repo": "https://github.com/demeet2k/athena-cloud-water",
            "tool_count": 16,
            "resource_count": 1,
        },
        {
            "node_id": "athena-fractal-air",
            "role": "lobe",
            "medium_class": "code",
            "lobe_affinity": "R",
            "shard_families": ["stages", "angel", "mobius", "inverse_crystal", "hologram"],
            "mirrors": ["athena-mcp-server"],
            "bridges": [{"type": "lobe_to_unified", "description": "Mirrors unified server's compression/seed tools"}],
            "cert_capabilities": ["REPLAY"],
            "read_surfaces": ["mcp_tool", "mcp_resource"],
            "write_surfaces": [],
            "sync_sources": ["https://github.com/demeet2k/athena-fractal-air"],
            "github_repo": "https://github.com/demeet2k/athena-fractal-air",
            "tool_count": 16,
            "resource_count": 1,
        },
        {
            "node_id": "google-docs",
            "role": "docs",
            "medium_class": "google_doc",
            "lobe_affinity": None,
            "shard_families": ["core", "crystal", "emergence", "skills", "brain_stem"],
            "mirrors": ["athena-mcp-server"],
            "bridges": [{"type": "docs_to_github", "description": "Google Docs sections mirror nervous system files"}],
            "cert_capabilities": [],
            "read_surfaces": ["google_drive_api"],
            "write_surfaces": ["google_drive_api"],
            "sync_sources": [
                "https://docs.google.com/document/d/1OUjhabDK08QvamAa0USQmTeEDNAwN3b853OVmvMUdaE",
                "https://docs.google.com/document/d/1bzcO7PKGlMUc2A35VYo5msN7hGYZzGA4KRQaFaRfbvQ",
                "https://docs.google.com/document/d/1LJEMi-OmqSfSqJTc585nxlf5zGF0rfyqbygNlYYB6J4",
            ],
            "github_repo": None,
            "tool_count": 0,
            "resource_count": 0,
        },
        {
            "node_id": "athena-guild-hall",
            "role": "guild-hall",
            "medium_class": "code",
            "lobe_affinity": None,
            "shard_families": ["manuscript", "quest", "synthesis", "proof", "replication", "guild_hall"],
            "mirrors": ["athena-mcp-server", "google-docs"],
            "bridges": [
                {"type": "guild_to_mcp", "description": "Guild Hall boards exposed via 4 MCP tools + 2 resources"},
                {"type": "guild_to_framework", "description": "Python framework implements 21-chapter x 256-gate computational model"},
                {"type": "guild_to_docs", "description": "Guild Hall synthesis mirrors Google Docs organism state"},
            ],
            "cert_capabilities": ["STRUCTURAL", "CONSERVATION", "REPLAY", "PROMOTION"],
            "read_surfaces": ["mcp_tool", "mcp_resource", "file_read", "cli"],
            "write_surfaces": ["file_write", "git_commit"],
            "sync_sources": [],
            "github_repo": None,
            "tool_count": 4,
            "resource_count": 2,
        },
        {
            "node_id": "manuscript-being",
            "role": "main-brain",
            "medium_class": "code",
            "lobe_affinity": None,
            "shard_families": ["manuscript", "quest", "synthesis", "proof", "replication",
                               "guild_hall", "crystal", "metro", "swarm", "truth"],
            "mirrors": ["athena-mcp-server", "athena-guild-hall", "google-docs"],
            "bridges": [
                {"type": "main_brain_to_mcp", "description": "MCP tools expose manuscript-being computation to all agents"},
                {"type": "main_brain_to_guild_hall", "description": "Guild Hall is the social coordination surface"},
                {"type": "main_brain_to_docs", "description": "Google Docs = slow-form, manuscript-being = executable form"},
            ],
            "cert_capabilities": ["STRUCTURAL", "CONSERVATION", "REPLAY", "PROMOTION", "REPLICATION", "TRUTH_CORRIDOR"],
            "read_surfaces": ["mcp_tool", "mcp_resource", "file_read", "cli", "python_import"],
            "write_surfaces": ["file_write", "git_commit", "python_exec"],
            "sync_sources": ["https://github.com/demeet2k/manuscript-being"],
            "github_repo": "https://github.com/demeet2k/manuscript-being",
            "tool_count": 0,
            "resource_count": 0,
        },
    ]


# ── Main ────────────────────────────────────────────────────────────

def main():
    print("Scanning MCP/data/*.json ...")
    json_shards = scan_json_data()
    print(f"  {len(json_shards)} JSON data shards")

    print("Scanning MCP/crystal_108d/*.py ...")
    code_shards = scan_crystal_modules()
    print(f"  {len(code_shards)} code module shards")

    print("Scanning MCP/element_servers/*.py ...")
    element_shards = scan_element_servers()
    print(f"  {len(element_shards)} element server shards")

    main_shard = scan_main_server()
    print("  1 main server shard")

    print("Scanning Guild Hall ...")
    guild_shards = scan_guild_hall()
    print(f"  {len(guild_shards)} guild hall shards")

    print("Scanning manuscript-being ...")
    ms_shards = scan_manuscript_being()
    print(f"  {len(ms_shards)} manuscript-being shards")

    all_shards = json_shards + code_shards + element_shards + [main_shard] + guild_shards + ms_shards
    print(f"\nTotal shards: {len(all_shards)}")

    print("Building edges ...")
    edges = build_edges(all_shards)
    print(f"  {len(edges)} edges")

    mirrors = [e for e in edges if e.edge_type == "MIRROR"]
    print(f"  {len(mirrors)} mirror edges")

    print("Building node registry ...")
    nodes = build_node_registry()
    print(f"  {len(nodes)} nodes")

    # Compute stats
    families = sorted(set(s.family for s in all_shards))
    mediums = sorted(set(s.medium for s in all_shards))
    edge_dist = {}
    for e in edges:
        edge_dist[e.edge_type] = edge_dist.get(e.edge_type, 0) + 1
    family_sizes = {}
    for s in all_shards:
        family_sizes[s.family] = family_sizes.get(s.family, 0) + 1

    # Emit mycelium_graph.json
    graph = {
        "meta": {
            "title": "Athena Mycelium Graph",
            "description": "Universal shard/edge/node graph manifest for the Athena distributed superbrain",
            "generated_at": NOW,
            "generator": "generate_graph.py v1",
            "shard_count": len(all_shards),
            "edge_count": len(edges),
            "mirror_count": len(mirrors),
            "node_count": len(nodes),
            "families": families,
            "mediums": mediums,
        },
        "shards": [to_dict(s) for s in all_shards],
        "edges": [to_dict(e) for e in edges],
        "mirrors": [to_dict(e) for e in mirrors],
        "nodes": nodes,
        "graph_stats": {
            "edge_type_distribution": edge_dist,
            "family_sizes": family_sizes,
            "medium_distribution": {m: sum(1 for s in all_shards if s.medium == m) for m in mediums},
        },
    }

    out_graph = DATA_DIR / "mycelium_graph.json"
    out_graph.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out_graph}")

    # Emit node_registry.json
    registry = {
        "meta": {
            "title": "Athena Node Registry",
            "description": "All nodes in the distributed Athena superbrain",
            "generated_at": NOW,
            "total_nodes": len(nodes),
        },
        "nodes": nodes,
    }

    out_nodes = DATA_DIR / "node_registry.json"
    out_nodes.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_nodes}")

    print(f"\nDone. {len(all_shards)} shards, {len(edges)} edges, {len(nodes)} nodes.")


if __name__ == "__main__":
    main()
