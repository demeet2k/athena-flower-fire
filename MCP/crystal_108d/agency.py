"""
Agency & Micro-Gateway Architecture
=====================================
Provides the Athena micro-gateway v2 specification:
  - Self-verifying file-transfer node architecture
  - Event witness bundle schema
  - Corridor constraints / safety layer
  - Replay protection & hash chain
  - Angel→agent bridge (12-piece mapping)
  - Multi-gateway orchestration / fleet concepts
"""

from ._cache import JsonCache

_AGENCY = JsonCache("agency_gateway.json")


def query_agency(component: str = "all") -> str:
    """
    Query the agency & micro-gateway architecture.

    Components:
      - all          : Full agency overview
      - gateway      : Micro-gateway v2 architecture (observer→validator→ledger→action→witness)
      - witness      : Event witness bundle schema
      - corridor     : Corridor constraints / safety layer
      - replay       : Replay protection & hash chain
      - bridge       : Angel→agent bridge (12-piece mapping)
      - fleet        : Multi-gateway orchestration
      - pipeline     : Full gateway pipeline stages
    """
    data = _AGENCY.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "gateway":
        return _format_gateway(data)
    elif comp == "witness":
        return _format_witness(data)
    elif comp == "corridor":
        return _format_corridor(data)
    elif comp == "replay":
        return _format_replay(data)
    elif comp == "bridge":
        return _format_bridge(data)
    elif comp == "fleet":
        return _format_fleet(data)
    elif comp == "pipeline":
        return _format_pipeline(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, gateway, witness, "
            "corridor, replay, bridge, fleet, pipeline"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## Agency & Micro-Gateway Architecture\n",
        f"**Title**: {meta.get('title', 'Athena Micro-Gateway v2')}",
        f"**Key Insight**: {meta.get('key_insight', '')}",
        f"**Pipeline**: {meta.get('pipeline', 'observer → validator → ledger → action → witness')}",
        f"**Version**: {meta.get('version', 'v2')}",
    ]
    # Pipeline stages
    stages = data.get("pipeline_stages", [])
    if stages:
        lines.append("\n### Pipeline Stages\n")
        for s in stages:
            if isinstance(s, dict):
                lines.append(f"- **{s.get('name', '?')}**: {s.get('function', '')}")
            else:
                lines.append(f"- {s}")
    return "\n".join(lines)


def _format_gateway(data: dict) -> str:
    gw = data.get("gateway", {})
    lines = [
        "## Micro-Gateway v2 Architecture\n",
        f"**Type**: {gw.get('type', 'Self-verifying file-transfer node')}",
        f"**Purpose**: {gw.get('purpose', '')}",
    ]
    features = gw.get("features", [])
    if features:
        lines.append("\n**Features**:")
        for f in features:
            lines.append(f"  - {f}")
    components = gw.get("components", [])
    if components:
        lines.append("\n**Components**:")
        for c in components:
            if isinstance(c, dict):
                lines.append(f"  - **{c.get('name', '?')}**: {c.get('role', '')}")
            else:
                lines.append(f"  - {c}")
    return "\n".join(lines)


def _format_witness(data: dict) -> str:
    wb = data.get("witness_bundle", {})
    lines = [
        "## Event Witness Bundle\n",
        f"**Purpose**: {wb.get('purpose', 'Cryptographically traceable event record')}",
    ]
    fields = wb.get("fields", {})
    if fields:
        lines.append("\n**Schema Fields**:")
        for name, desc in fields.items():
            lines.append(f"  - **{name}**: {desc}")
    lines.append(f"\n**Chain Property**: {wb.get('chain_property', 'tamper-evident hash chain')}")
    return "\n".join(lines)


def _format_corridor(data: dict) -> str:
    cor = data.get("corridor_constraints", {})
    lines = [
        "## Corridor Constraints (Safety Layer)\n",
        f"**Principle**: {cor.get('principle', '')}",
    ]
    rules = cor.get("rules", [])
    if rules:
        lines.append("\n**Rules**:")
        for r in rules:
            if isinstance(r, dict):
                lines.append(f"  - **{r.get('name', '?')}**: {r.get('constraint', '')}")
            else:
                lines.append(f"  - {r}")
    lines.append(f"\n**Violation**: {cor.get('violation_action', 'event rejected')}")
    return "\n".join(lines)


def _format_replay(data: dict) -> str:
    rp = data.get("replay_protection", {})
    return (
        "## Replay Protection\n\n"
        f"**Mechanism**: {rp.get('mechanism', 'seen_hashes registry')}\n"
        f"**Chain**: {rp.get('chain', 'SHA256(prev_hash + event_payload)')}\n"
        f"**Duplicate Policy**: {rp.get('duplicate_policy', 'reject duplicate file hashes')}\n"
        f"**Audit**: {rp.get('audit', 'complete audit trail via hash chain')}"
    )


def _format_bridge(data: dict) -> str:
    br = data.get("angel_agent_bridge", {})
    lines = [
        "## Angel → Agent Bridge\n",
        f"**Concept**: {br.get('concept', '12-piece angel object mapped to agent architecture')}",
    ]
    mappings = br.get("mappings", [])
    if mappings:
        lines.append("\n**Mappings**:")
        for m in mappings:
            if isinstance(m, dict):
                lines.append(
                    f"  - **{m.get('angel_piece', '?')}** → {m.get('agent_component', '')}"
                )
            else:
                lines.append(f"  - {m}")
    return "\n".join(lines)


def _format_fleet(data: dict) -> str:
    fl = data.get("fleet_orchestration", {})
    lines = [
        "## Multi-Gateway Orchestration\n",
        f"**Model**: {fl.get('model', 'Distributed fleet of autonomous gateway nodes')}",
    ]
    if "topology" in fl:
        lines.append(f"**Topology**: {fl['topology']}")
    if "coordination" in fl:
        lines.append(f"**Coordination**: {fl['coordination']}")
    roles = fl.get("roles", [])
    if roles:
        lines.append("\n**Roles**:")
        for r in roles:
            if isinstance(r, dict):
                lines.append(f"  - **{r.get('name', '?')}**: {r.get('function', '')}")
            else:
                lines.append(f"  - {r}")
    return "\n".join(lines)


def _format_pipeline(data: dict) -> str:
    stages = data.get("pipeline_stages", [])
    lines = ["## Full Gateway Pipeline\n"]
    for i, s in enumerate(stages, 1):
        if isinstance(s, dict):
            lines.append(f"### Stage {i}: {s.get('name', '?')}")
            lines.append(f"**Function**: {s.get('function', '')}")
            if "inputs" in s:
                lines.append(f"**Inputs**: {s['inputs']}")
            if "outputs" in s:
                lines.append(f"**Outputs**: {s['outputs']}")
            lines.append("")
        else:
            lines.append(f"{i}. {s}")
    return "\n".join(lines)
