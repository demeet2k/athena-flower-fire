"""
Mycelium Graph — Universal Shard/Edge/Node Query Surface
=========================================================
Exposes the generated graph manifest as navigable MCP tools.
The mycelium graph is the connective tissue that makes every artifact
in the organism (JSON data, Python modules, element servers, doc sections)
addressable through one shared shard/edge/node schema.

Tools: query_shard, query_graph, query_node, query_promotion
"""

from ._cache import JsonCache

_GRAPH = JsonCache("mycelium_graph.json")
_NODES = JsonCache("node_registry.json")


def query_shard(shard_id_or_search: str = "all") -> str:
    """
    Query the mycelium shard graph.

    Components:
      - all          : Graph overview and statistics
      - stats        : Detailed graph statistics
      - families     : List all shard families with counts
      - family:NAME  : All shards in a family (e.g. family:brain)
      - medium:TYPE  : All shards of a medium type (json, code, doc)
      - lens:X       : All shards with lens affinity (S, F, C, R)
      - shard:ID     : Specific shard by ID or substring match
      - search:TERM  : Full-text search across shard summaries
    """
    data = _GRAPH.load()
    q = shard_id_or_search.strip()
    ql = q.lower()

    if ql == "all":
        return _format_overview(data)
    elif ql == "stats":
        return _format_stats(data)
    elif ql == "families":
        return _format_families(data)
    elif ql.startswith("family:"):
        return _format_family(data, q.split(":", 1)[1].strip())
    elif ql.startswith("medium:"):
        return _format_by_medium(data, q.split(":", 1)[1].strip())
    elif ql.startswith("lens:"):
        return _format_by_lens(data, q.split(":", 1)[1].strip().upper())
    elif ql.startswith("shard:"):
        return _format_shard(data, q.split(":", 1)[1].strip())
    elif ql.startswith("search:"):
        return _format_search(data, q.split(":", 1)[1].strip())
    else:
        # Try direct shard ID lookup
        return _format_shard(data, q)


def query_graph(component: str = "all") -> str:
    """
    Query the mycelium graph structure.

    Components:
      - all          : Full graph overview
      - edges        : Edge summary by type
      - edge:TYPE    : All edges of a specific type (e.g. edge:BUILD)
      - mirrors      : Cross-medium mirror relations
      - density      : Graph density and connectivity metrics
    """
    data = _GRAPH.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_graph_all(data)
    elif comp == "edges":
        return _format_edge_summary(data)
    elif comp.startswith("edge:"):
        return _format_edges_by_type(data, component.split(":", 1)[1].strip().upper())
    elif comp == "mirrors":
        return _format_mirrors(data)
    elif comp == "density":
        return _format_density(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, edges, edge:TYPE, mirrors, density"
        )


def query_node(node_name: str = "all") -> str:
    """
    Query the Athena node registry.

    Components:
      - all          : All registered nodes
      - node:NAME    : Specific node details (e.g. node:athena-mcp-server)
      - bridges      : Cross-node bridge summary
      - families     : Which nodes serve which shard families
    """
    data = _NODES.load()
    q = node_name.strip().lower()

    if q == "all":
        return _format_nodes_all(data)
    elif q.startswith("node:"):
        return _format_one_node(data, node_name.split(":", 1)[1].strip())
    elif q == "bridges":
        return _format_node_bridges(data)
    elif q == "families":
        return _format_node_families(data)
    else:
        # Try direct node name lookup
        return _format_one_node(data, node_name)


def query_promotion(shard_id: str = "") -> str:
    """
    Query promotion status of shards.

    Args:
      shard_id: Shard ID or substring. Empty = promotion overview.
    """
    data = _GRAPH.load()
    if not shard_id.strip():
        return _format_promotion_overview(data)
    return _format_promotion_detail(data, shard_id.strip())


def mycelium_status() -> str:
    """Return compact mycelium status for resource endpoint."""
    data = _GRAPH.load()
    m = data["meta"]
    stats = data["graph_stats"]
    return (
        "## Athena Mycelium Graph\n\n"
        f"**Shards**: {m['shard_count']} | "
        f"**Edges**: {m['edge_count']} | "
        f"**Mirrors**: {m['mirror_count']} | "
        f"**Nodes**: {m['node_count']}\n"
        f"**Families**: {', '.join(m['families'])}\n"
        f"**Mediums**: {', '.join(m['mediums'])}\n"
        f"**Edge Types**: {', '.join(f'{k}:{v}' for k, v in stats['edge_type_distribution'].items())}\n"
        f"**Generated**: {m['generated_at']}\n"
    )


# ── Shard Formatters ────────────────────────────────────────────────

def _format_overview(data: dict) -> str:
    m = data["meta"]
    stats = data["graph_stats"]
    lines = [
        "## Athena Mycelium Graph\n",
        f"**Shards**: {m['shard_count']} | **Edges**: {m['edge_count']} | "
        f"**Mirrors**: {m['mirror_count']} | **Nodes**: {m['node_count']}\n",
        "### Families\n",
    ]
    for fam, count in sorted(stats["family_sizes"].items()):
        lines.append(f"- **{fam}**: {count} shards")
    lines.append("\n### Mediums\n")
    for med, count in sorted(stats["medium_distribution"].items()):
        lines.append(f"- **{med}**: {count} shards")
    lines.append("\n### Edge Types\n")
    for etype, count in sorted(stats["edge_type_distribution"].items()):
        lines.append(f"- **{etype}**: {count}")
    return "\n".join(lines)


def _format_stats(data: dict) -> str:
    m = data["meta"]
    stats = data["graph_stats"]
    lines = [
        "## Graph Statistics\n",
        f"**Total Shards**: {m['shard_count']}",
        f"**Total Edges**: {m['edge_count']}",
        f"**Mirror Edges**: {m['mirror_count']}",
        f"**Nodes**: {m['node_count']}",
        f"**Families**: {len(m['families'])}",
        f"**Generated**: {m['generated_at']}\n",
        "### Edge Type Distribution\n",
    ]
    for k, v in sorted(stats["edge_type_distribution"].items()):
        lines.append(f"| {k} | {v} |")
    lines.append("\n### Family Sizes\n")
    for k, v in sorted(stats["family_sizes"].items(), key=lambda x: -x[1]):
        lines.append(f"| {k} | {v} |")
    return "\n".join(lines)


def _format_families(data: dict) -> str:
    stats = data["graph_stats"]
    lines = ["## Shard Families\n"]
    for fam, count in sorted(stats["family_sizes"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{fam}**: {count} shards")
    return "\n".join(lines)


def _format_family(data: dict, family: str) -> str:
    fl = family.lower()
    matches = [s for s in data["shards"] if s["family"].lower() == fl]
    if not matches:
        return f"No shards found in family '{family}'."
    lines = [f"## Family: {family} ({len(matches)} shards)\n"]
    for s in matches:
        lens = s["lens"] or "—"
        lines.append(
            f"- **{s['shard_id']}** [{s['medium']}] ({lens}) — {s['summary']}"
        )
    return "\n".join(lines)


def _format_by_medium(data: dict, medium: str) -> str:
    ml = medium.lower()
    matches = [s for s in data["shards"] if s["medium"].lower() == ml]
    if not matches:
        return f"No shards found with medium '{medium}'."
    lines = [f"## Medium: {medium} ({len(matches)} shards)\n"]
    for s in matches:
        lines.append(f"- **{s['shard_id']}** [{s['family']}] — {s['summary']}")
    return "\n".join(lines)


def _format_by_lens(data: dict, lens: str) -> str:
    matches = [s for s in data["shards"] if s.get("lens") == lens]
    if not matches:
        return f"No shards found with lens '{lens}'."
    lines = [f"## Lens: {lens} ({len(matches)} shards)\n"]
    for s in matches:
        lines.append(f"- **{s['shard_id']}** [{s['medium']}] — {s['summary']}")
    return "\n".join(lines)


def _format_shard(data: dict, query: str) -> str:
    ql = query.lower()
    # Exact match first
    for s in data["shards"]:
        if s["shard_id"] == query:
            return _render_shard(s, data)
    # Substring match
    matches = [s for s in data["shards"] if ql in s["shard_id"].lower()]
    if len(matches) == 1:
        return _render_shard(matches[0], data)
    if matches:
        lines = [f"## Multiple matches for '{query}' ({len(matches)})\n"]
        for s in matches:
            lines.append(f"- **{s['shard_id']}** [{s['medium']}] — {s['summary']}")
        return "\n".join(lines)
    return f"No shard found matching '{query}'."


def _format_search(data: dict, term: str) -> str:
    tl = term.lower()
    matches = [
        s for s in data["shards"]
        if tl in s["summary"].lower()
        or tl in s["family"].lower()
        or any(tl in t.lower() for t in s.get("tags", []))
    ]
    if not matches:
        return f"No shards match search term '{term}'."
    lines = [f"## Search: '{term}' ({len(matches)} results)\n"]
    for s in matches:
        lines.append(f"- **{s['shard_id']}** [{s['medium']}/{s['family']}] — {s['summary']}")
    return "\n".join(lines)


def _render_shard(s: dict, data: dict) -> str:
    lines = [
        f"## Shard: {s['shard_id']}\n",
        f"**Summary**: {s['summary']}",
        f"**Medium**: {s['medium']} | **Family**: {s['family']}",
        f"**Lens**: {s['lens'] or 'universal'} | **Dimension**: {s['dimensional_scope']}",
        f"**Repo**: {s['repo']}",
        f"**Payload**: `{s['payload_ref']}`",
        f"**Seed Vector**: [{', '.join(f'{v:.2f}' for v in s['seed_vector'])}]",
        f"**Truth**: {s['truth_status']} | **Promotion**: {s['promotion_status']}",
        f"**Tags**: {', '.join(s.get('tags', []))}",
    ]
    # Find connected edges
    in_edges = [e for e in data["edges"] if e["target_shard"] == s["shard_id"]]
    out_edges = [e for e in data["edges"] if e["source_shard"] == s["shard_id"]]
    if in_edges:
        lines.append(f"\n### Incoming Edges ({len(in_edges)})\n")
        for e in in_edges:
            lines.append(f"- **{e['edge_type']}** from `{e['source_shard']}` (w={e['weight']})")
    if out_edges:
        lines.append(f"\n### Outgoing Edges ({len(out_edges)})\n")
        for e in out_edges:
            lines.append(f"- **{e['edge_type']}** to `{e['target_shard']}` (w={e['weight']})")
    return "\n".join(lines)


# ── Graph Formatters ────────────────────────────────────────────────

def _format_graph_all(data: dict) -> str:
    m = data["meta"]
    stats = data["graph_stats"]
    lines = [
        "## Mycelium Graph Structure\n",
        f"**Shards**: {m['shard_count']} | **Edges**: {m['edge_count']}\n",
        "### Edge Type Distribution\n",
    ]
    for k, v in sorted(stats["edge_type_distribution"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{k}**: {v} edges")
    lines.append(f"\n### Connectivity\n")
    lines.append(f"- Average edges per shard: {m['edge_count'] * 2 / max(m['shard_count'], 1):.1f}")
    lines.append(f"- Mirror ratio: {m['mirror_count'] / max(m['edge_count'], 1):.1%}")
    return "\n".join(lines)


def _format_edge_summary(data: dict) -> str:
    stats = data["graph_stats"]
    lines = ["## Edge Summary\n"]
    for etype, count in sorted(stats["edge_type_distribution"].items(), key=lambda x: -x[1]):
        lines.append(f"### {etype} ({count} edges)\n")
        examples = [e for e in data["edges"] if e["edge_type"] == etype][:3]
        for e in examples:
            lines.append(f"  - `{e['source_shard']}` → `{e['target_shard']}` (w={e['weight']})")
        if count > 3:
            lines.append(f"  - ... and {count - 3} more")
        lines.append("")
    return "\n".join(lines)


def _format_edges_by_type(data: dict, etype: str) -> str:
    matches = [e for e in data["edges"] if e["edge_type"] == etype]
    if not matches:
        return f"No edges of type '{etype}' found."
    lines = [f"## {etype} Edges ({len(matches)})\n"]
    for e in matches:
        meta = f" ({e['metadata']})" if e.get("metadata") else ""
        lines.append(f"- `{e['source_shard']}` → `{e['target_shard']}` w={e['weight']}{meta}")
    return "\n".join(lines)


def _format_mirrors(data: dict) -> str:
    mirrors = data.get("mirrors", [])
    if not mirrors:
        return "No mirror edges in graph."
    lines = [f"## Mirror Relations ({len(mirrors)})\n"]
    for m in mirrors:
        lines.append(f"- `{m['source_shard']}` ↔ `{m['target_shard']}`")
        if m.get("metadata"):
            lines.append(f"  Type: {m['metadata'].get('mirror_type', '?')}")
    return "\n".join(lines)


def _format_density(data: dict) -> str:
    m = data["meta"]
    n = m["shard_count"]
    e = m["edge_count"]
    max_edges = n * (n - 1) if n > 1 else 1
    density = e / max_edges
    stats = data["graph_stats"]

    lines = [
        "## Graph Density\n",
        f"**Shards (V)**: {n}",
        f"**Edges (E)**: {e}",
        f"**Max Possible Edges**: {max_edges}",
        f"**Density**: {density:.6f}",
        f"**Avg Degree**: {e * 2 / max(n, 1):.2f}",
        f"\n### By Medium\n",
    ]
    for med, count in stats["medium_distribution"].items():
        lines.append(f"- {med}: {count} ({count/max(n,1):.0%})")
    return "\n".join(lines)


# ── Node Formatters ─────────────────────────────────────────────────

def _format_nodes_all(data: dict) -> str:
    nodes = data["nodes"]
    lines = [f"## Athena Node Registry ({len(nodes)} nodes)\n"]
    for n in nodes:
        lobe = f" [{n['lobe_affinity']}]" if n.get("lobe_affinity") else ""
        lines.append(
            f"### {n['node_id']}{lobe}\n"
            f"**Role**: {n['role']} | **Medium**: {n['medium_class']}\n"
            f"**Tools**: {n['tool_count']} | **Resources**: {n['resource_count']}\n"
            f"**Families**: {', '.join(n.get('shard_families', []))}\n"
            f"**Repo**: {n.get('github_repo') or '—'}\n"
        )
    return "\n".join(lines)


def _format_one_node(data: dict, name: str) -> str:
    nl = name.lower()
    for n in data["nodes"]:
        if n["node_id"].lower() == nl or nl in n["node_id"].lower():
            lines = [
                f"## Node: {n['node_id']}\n",
                f"**Role**: {n['role']}",
                f"**Medium**: {n['medium_class']}",
                f"**Lobe Affinity**: {n.get('lobe_affinity') or 'universal'}",
                f"**Tools**: {n['tool_count']} | **Resources**: {n['resource_count']}",
                f"**Shard Families**: {', '.join(n.get('shard_families', []))}",
                f"**Mirrors**: {', '.join(n.get('mirrors', []))}",
                f"**Cert Capabilities**: {', '.join(n.get('cert_capabilities', []) or ['none'])}",
                f"**Read Surfaces**: {', '.join(n.get('read_surfaces', []))}",
                f"**Write Surfaces**: {', '.join(n.get('write_surfaces', []) or ['none'])}",
                f"**Repo**: {n.get('github_repo') or '—'}",
            ]
            if n.get("bridges"):
                lines.append("\n### Bridges\n")
                for b in n["bridges"]:
                    lines.append(f"- **{b['type']}**: {b['description']}")
            return "\n".join(lines)
    return f"Node '{name}' not found."


def _format_node_bridges(data: dict) -> str:
    lines = ["## Cross-Node Bridges\n"]
    for n in data["nodes"]:
        if n.get("bridges"):
            lines.append(f"### {n['node_id']}\n")
            for b in n["bridges"]:
                lines.append(f"- **{b['type']}**: {b['description']}")
            lines.append("")
    return "\n".join(lines)


def _format_node_families(data: dict) -> str:
    lines = ["## Node → Family Mapping\n"]
    for n in data["nodes"]:
        fams = n.get("shard_families", [])
        lines.append(f"- **{n['node_id']}**: {', '.join(fams)}")
    return "\n".join(lines)


# ── Promotion Formatters ────────────────────────────────────────────

def _format_promotion_overview(data: dict) -> str:
    shards = data["shards"]
    by_truth = {}
    by_promo = {}
    for s in shards:
        by_truth[s["truth_status"]] = by_truth.get(s["truth_status"], 0) + 1
        by_promo[s["promotion_status"]] = by_promo.get(s["promotion_status"], 0) + 1

    lines = [
        "## Promotion Overview\n",
        "### Truth Status Distribution\n",
    ]
    for status in ["SEED", "DRAFT", "WITNESSED", "CERTIFIED", "CANONICAL"]:
        count = by_truth.get(status, 0)
        if count:
            lines.append(f"- **{status}**: {count}")
    lines.append("\n### Promotion Status Distribution\n")
    for status in ["LOCAL", "PROPOSED", "REVIEWED", "PROMOTED", "ARCHIVED"]:
        count = by_promo.get(status, 0)
        if count:
            lines.append(f"- **{status}**: {count}")
    return "\n".join(lines)


def _format_promotion_detail(data: dict, query: str) -> str:
    ql = query.lower()
    matches = [s for s in data["shards"] if ql in s["shard_id"].lower()]
    if not matches:
        return f"No shard found matching '{query}'."
    if len(matches) > 5:
        return f"Too many matches ({len(matches)}). Be more specific."
    lines = []
    for s in matches:
        lines.append(f"### {s['shard_id']}")
        lines.append(f"**Truth**: {s['truth_status']} | **Promotion**: {s['promotion_status']}")
        certs = [e for e in data["edges"] if e["target_shard"] == s["shard_id"] and e["edge_type"] == "CERTIFIES"]
        if certs:
            lines.append(f"**Certs**: {len(certs)}")
        else:
            lines.append("**Certs**: none")
        promotes = [e for e in data["edges"] if e["target_shard"] == s["shard_id"] and e["edge_type"] == "PROMOTES"]
        if promotes:
            lines.append(f"**Promoted by**: {', '.join(e['source_shard'] for e in promotes)}")
        lines.append("")
    return "\n".join(lines)
