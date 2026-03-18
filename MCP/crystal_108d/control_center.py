"""
Athena Control Center — Neural Network as Organism Cockpit.

The control center bridges the neural network's 4-element perception
architecture with the 108D crystal's telemetry and routing systems.
It transforms read-only observation into active steering.

Components:
  dashboard   — Full organism health dashboard
  perception  — Current perception input snapshot
  weights     — Internal weight configuration
  history     — Last 50 steering actions
  alerts      — Detected anomalies

Steering actions:
  promote_shard  — Promote a shard to a higher shell
  shift_phase    — Shift a shard's phase
  create_route   — Create a metro route between nodes
  rebalance_sfcr — Rebalance SFCR element percentages
  emit_seed      — Emit a compression seed from a shell
"""

from __future__ import annotations

import json
import os
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ._cache import JsonCache

# ── Data caches ─────────────────────────────────────────────────────
_GRAPH_CACHE = JsonCache("mycelium_graph.json")
_BRAIN_CACHE = JsonCache("brain_network.json")
_COORD_CACHE = JsonCache("crystal_coordinates.json")

# ── Control center database ─────────────────────────────────────────
_DB_PATH = Path(__file__).parent.parent / "data" / "control_center.db"

_VALID_ACTIONS = {
    "promote_shard",
    "shift_phase",
    "create_route",
    "rebalance_sfcr",
    "emit_seed",
}

_VALID_PHASES = {"Fixed", "Cardinal", "Mutable"}

_SFCR_CODES = {"S", "F", "C", "R"}

_SFCR_NAMES = {
    "S": "Square (Earth)",
    "F": "Flower (Fire)",
    "C": "Cloud (Water)",
    "R": "Fractal (Air)",
}


# ── Database initialization ─────────────────────────────────────────

def _ensure_db() -> sqlite3.Connection:
    """Return a connection to the control center DB, creating tables if needed."""
    _DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(_DB_PATH))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS steering_log (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            action TEXT,
            target TEXT,
            parameters TEXT,
            result TEXT,
            crystal_coordinate TEXT,
            agent_id TEXT DEFAULT 'control_center'
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS organism_snapshots (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            graph_density REAL,
            sfcr_balance TEXT,
            phase_distribution TEXT,
            depth_distribution TEXT,
            edge_counts TEXT,
            alerts TEXT
        )
    """)
    conn.commit()
    return conn


# ── Safe cache loading ───────────────────────────────────────────────

def _safe_load(cache: JsonCache) -> dict | list | None:
    """Load cache data, returning None if the file doesn't exist."""
    try:
        return cache.load()
    except (FileNotFoundError, json.JSONDecodeError):
        return None


# ── Graph statistics helpers ─────────────────────────────────────────

def _compute_graph_stats(graph: dict | None) -> dict:
    """Extract key statistics from the mycelium graph."""
    if graph is None:
        return {
            "total_nodes": 0,
            "total_edges": 0,
            "edge_counts": {},
            "density": 0.0,
            "sfcr_balance": {"S": 0, "F": 0, "C": 0, "R": 0},
            "sfcr_pct": {"S": 0.0, "F": 0.0, "C": 0.0, "R": 0.0},
            "phase_dist": {"Fixed": 0, "Cardinal": 0, "Mutable": 0},
            "phase_pct": {"Fixed": 0.0, "Cardinal": 0.0, "Mutable": 0.0},
            "depth_dist": {},
        }

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    total_nodes = len(nodes)
    total_edges = len(edges)

    # Edge counts by type
    edge_counts: dict[str, int] = {}
    for e in edges:
        etype = e.get("type", e.get("edge_type", "unknown"))
        edge_counts[etype] = edge_counts.get(etype, 0) + 1

    # Density: actual edges / possible edges
    max_edges = total_nodes * (total_nodes - 1) / 2 if total_nodes > 1 else 1
    density = total_edges / max_edges if max_edges > 0 else 0.0

    # SFCR balance from node lens/element tags
    sfcr: dict[str, int] = {"S": 0, "F": 0, "C": 0, "R": 0}
    phase_dist: dict[str, int] = {"Fixed": 0, "Cardinal": 0, "Mutable": 0}
    depth_dist: dict[str, int] = {}

    for node in nodes:
        # Element affinity
        lens = node.get("sfcr_lens", node.get("lens", node.get("element", "")))
        if isinstance(lens, str):
            for code in _SFCR_CODES:
                if code in lens.upper():
                    sfcr[code] += 1

        # Phase
        phase = node.get("phase", node.get("modality", ""))
        if isinstance(phase, str):
            for p in _VALID_PHASES:
                if p.lower() in phase.lower():
                    phase_dist[p] += 1

        # Depth / shell
        depth = node.get("shell", node.get("depth", node.get("hpro_depth", None)))
        if depth is not None:
            dkey = str(depth)
            depth_dist[dkey] = depth_dist.get(dkey, 0) + 1

    # Percentages
    sfcr_total = sum(sfcr.values()) or 1
    sfcr_pct = {k: round(100 * v / sfcr_total, 1) for k, v in sfcr.items()}

    phase_total = sum(phase_dist.values()) or 1
    phase_pct = {k: round(100 * v / phase_total, 1) for k, v in phase_dist.items()}

    return {
        "total_nodes": total_nodes,
        "total_edges": total_edges,
        "edge_counts": edge_counts,
        "density": round(density, 6),
        "sfcr_balance": sfcr,
        "sfcr_pct": sfcr_pct,
        "phase_dist": phase_dist,
        "phase_pct": phase_pct,
        "depth_dist": depth_dist,
    }


def _compute_brain_health(brain: dict | None) -> dict:
    """Extract brain element health from brain_network.json."""
    if brain is None:
        return {"elements": {}, "bridges": {}, "total_tools": 0}

    elements = brain.get("elements", {})
    bridges = brain.get("bridges", {})

    elem_health = {}
    total_tools = 0
    for key, elem in elements.items():
        n_tools = len(elem.get("tools", []))
        total_tools += n_tools
        elem_health[elem.get("code", key)] = {
            "name": elem.get("name", key),
            "element": elem.get("element", "?"),
            "tools": n_tools,
            "dimension_home": elem.get("dimension_home", "?"),
            "status": "active",
        }

    bridge_health = {}
    for key, bridge in bridges.items():
        bridge_health[key] = {
            "weight": bridge.get("weight", 0),
            "resonance_type": bridge.get("resonance_type", "?"),
        }

    return {
        "elements": elem_health,
        "bridges": bridge_health,
        "total_tools": total_tools,
    }


def _get_recent_steerings(limit: int = 10) -> list[dict]:
    """Fetch the most recent steering actions from the ledger."""
    try:
        conn = _ensure_db()
        cursor = conn.execute(
            "SELECT id, timestamp, action, target, parameters, result, crystal_coordinate "
            "FROM steering_log ORDER BY id DESC LIMIT ?",
            (limit,),
        )
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                "id": r[0], "timestamp": r[1], "action": r[2],
                "target": r[3], "parameters": r[4], "result": r[5],
                "crystal_coordinate": r[6],
            }
            for r in rows
        ]
    except Exception:
        return []


def _detect_alerts(stats: dict, steerings: list[dict]) -> list[str]:
    """Detect organism anomalies."""
    alerts = []

    # SFCR imbalance: any element < 10%
    for code, pct in stats["sfcr_pct"].items():
        if pct < 10.0 and stats["total_nodes"] > 10:
            alerts.append(
                f"SFCR_IMBALANCE: {_SFCR_NAMES.get(code, code)} at {pct}% (< 10% threshold)"
            )

    # Graph density too low (< 0.001 with > 100 nodes)
    if stats["total_nodes"] > 100 and stats["density"] < 0.001:
        alerts.append(
            f"LOW_DENSITY: Graph density {stats['density']:.6f} with "
            f"{stats['total_nodes']} nodes (< 0.001 threshold)"
        )

    # Stagnation: no steering in 24h
    if steerings:
        latest_ts = steerings[0].get("timestamp", "")
        try:
            latest_dt = datetime.fromisoformat(latest_ts)
            now = datetime.now(timezone.utc)
            if hasattr(latest_dt, "tzinfo") and latest_dt.tzinfo is None:
                latest_dt = latest_dt.replace(tzinfo=timezone.utc)
            hours_since = (now - latest_dt).total_seconds() / 3600
            if hours_since > 24:
                alerts.append(
                    f"STAGNATION: No steering actions for {hours_since:.1f}h (> 24h threshold)"
                )
        except (ValueError, TypeError):
            pass
    else:
        alerts.append("STAGNATION: No steering actions recorded yet")

    # Phase freeze: > 90% Fixed
    fixed_pct = stats["phase_pct"].get("Fixed", 0.0)
    if fixed_pct > 90.0 and stats["total_nodes"] > 10:
        alerts.append(
            f"PHASE_FREEZE: {fixed_pct}% Fixed phase (> 90% threshold)"
        )

    return alerts


def _lookup_coordinate(target: str) -> str:
    """Look up the crystal coordinate for a target path/identifier."""
    coords = _safe_load(_COORD_CACHE)
    if coords is None:
        return ""
    if isinstance(coords, dict):
        # Try direct lookup
        coord = coords.get(target, "")
        if coord:
            return str(coord)
        # Try basename lookup
        basename = Path(target).name if "/" in target or "\\" in target else target
        coord = coords.get(basename, "")
        return str(coord) if coord else ""
    return ""


# ── MCP Tool: query_control_center ───────────────────────────────────

def query_control_center(component: str = "dashboard") -> str:
    """Query the Athena Neural Network Control Center.

    The control center is the organism's cockpit — it bridges the
    neural network's 4-element perception architecture with the
    108D crystal's telemetry and routing systems.

    Components:
      dashboard   — Full organism health dashboard
      perception  — Current perception input snapshot
      weights     — Internal weight configuration
      history     — Last 50 steering actions from the ledger
      alerts      — Detected anomalies and warnings
    """
    graph = _safe_load(_GRAPH_CACHE)
    brain = _safe_load(_BRAIN_CACHE)

    if component == "dashboard":
        return _render_dashboard(graph, brain)
    elif component == "perception":
        return _render_perception(graph, brain)
    elif component == "weights":
        return _render_weights(brain)
    elif component == "history":
        return _render_history()
    elif component == "alerts":
        return _render_alerts(graph)
    else:
        return (
            f"Unknown component: {component}. "
            "Use: dashboard, perception, weights, history, alerts"
        )


def _render_dashboard(graph: dict | None, brain: dict | None) -> str:
    """Render the full organism health dashboard."""
    stats = _compute_graph_stats(graph)
    bhealth = _compute_brain_health(brain)
    recent = _get_recent_steerings(10)
    alerts = _detect_alerts(stats, recent)

    lines = [
        "## Athena Control Center — Organism Dashboard\n",
        f"**Timestamp**: {datetime.now(timezone.utc).isoformat()}",
        f"**Status**: {'ALERT' if alerts else 'NOMINAL'}\n",
    ]

    # Graph overview
    lines.append("### Graph Topology")
    lines.append(f"  Nodes: {stats['total_nodes']:,}")
    lines.append(f"  Edges: {stats['total_edges']:,}")
    lines.append(f"  Density: {stats['density']:.6f}")
    if stats["edge_counts"]:
        lines.append("  Edge types:")
        for etype, count in sorted(stats["edge_counts"].items(),
                                    key=lambda x: -x[1]):
            lines.append(f"    {etype}: {count:,}")

    # SFCR balance
    lines.append("\n### SFCR Balance")
    for code in ("S", "F", "C", "R"):
        pct = stats["sfcr_pct"].get(code, 0.0)
        bar = "#" * int(pct / 2)
        lines.append(
            f"  {code} ({_SFCR_NAMES[code]}): {pct:5.1f}%  [{bar}]"
        )

    # Phase distribution
    lines.append("\n### Phase Distribution")
    for phase in ("Fixed", "Cardinal", "Mutable"):
        pct = stats["phase_pct"].get(phase, 0.0)
        bar = "#" * int(pct / 2)
        lines.append(f"  {phase:8s}: {pct:5.1f}%  [{bar}]")

    # HPRO depth distribution
    if stats["depth_dist"]:
        lines.append("\n### HPRO Depth Distribution")
        for depth in sorted(stats["depth_dist"].keys(),
                           key=lambda x: int(x) if x.isdigit() else 999):
            count = stats["depth_dist"][depth]
            lines.append(f"  Depth {depth}: {count:,}")

    # Brain element health
    if bhealth["elements"]:
        lines.append("\n### Brain Element Health")
        for code, info in bhealth["elements"].items():
            lines.append(
                f"  **{code}** [{info['element']}] — {info['status'].upper()}, "
                f"{info['tools']} tools, {info['dimension_home']}D home"
            )
        lines.append(f"  Total distributed tools: {bhealth['total_tools']}")

    # Recent steering
    lines.append("\n### Recent Steering Actions")
    if recent:
        for s in recent[:5]:
            lines.append(
                f"  [{s['timestamp']}] {s['action']} -> {s['target']}"
            )
    else:
        lines.append("  (no steering actions recorded)")

    # Alerts
    if alerts:
        lines.append(f"\n### Alerts ({len(alerts)})")
        for a in alerts:
            lines.append(f"  ! {a}")

    return "\n".join(lines)


def _render_perception(graph: dict | None, brain: dict | None) -> str:
    """Render the perception input snapshot."""
    stats = _compute_graph_stats(graph)
    bhealth = _compute_brain_health(brain)
    coords = _safe_load(_COORD_CACHE)

    lines = [
        "## Control Center — Perception Snapshot\n",
        f"**Timestamp**: {datetime.now(timezone.utc).isoformat()}\n",
    ]

    # Graph perception
    lines.append("### Mycelium Graph State")
    if graph is not None:
        meta = graph.get("meta", {})
        lines.append(f"  Source: mycelium_graph.json")
        if meta:
            for k, v in meta.items():
                lines.append(f"  {k}: {v}")
        lines.append(f"  Live nodes: {stats['total_nodes']:,}")
        lines.append(f"  Live edges: {stats['total_edges']:,}")
        lines.append(f"  Density: {stats['density']:.6f}")
    else:
        lines.append("  [NOT LOADED — mycelium_graph.json not found]")

    # Brain perception
    lines.append("\n### Brain Network State")
    if brain is not None:
        meta = brain.get("meta", {})
        lines.append(f"  Source: brain_network.json")
        if meta:
            lines.append(f"  Architecture: {meta.get('elements', '?')} elements "
                         f"x {meta.get('bridges', '?')} bridges "
                         f"x {meta.get('closures', '?')} closures "
                         f"x {meta.get('aether', '?')} aether "
                         f"= {meta.get('total_stations', '?')} stations")
            lines.append(f"  Governing law: {meta.get('governing_law', '?')}")
        for code, info in bhealth["elements"].items():
            lines.append(f"  {code} ({info['element']}): {info['tools']} tools — {info['status']}")
    else:
        lines.append("  [NOT LOADED — brain_network.json not found]")

    # Coordinate coverage
    lines.append("\n### Coordinate Coverage")
    if coords is not None:
        if isinstance(coords, dict):
            n_coords = len(coords)
            coverage = (n_coords / stats["total_nodes"] * 100) if stats["total_nodes"] > 0 else 0
            lines.append(f"  Shards with coordinates: {n_coords:,}")
            lines.append(f"  Coverage: {coverage:.1f}%")
        else:
            lines.append(f"  Coordinate entries: {len(coords) if isinstance(coords, list) else '?'}")
    else:
        lines.append("  [NOT LOADED — crystal_coordinates.json not found]")

    return "\n".join(lines)


def _render_weights(brain: dict | None) -> str:
    """Render the internal weight configuration."""
    lines = [
        "## Control Center — Weight Configuration\n",
    ]

    # SFCR balance weights (steering targets)
    lines.append("### SFCR Balance Weights (ideal targets)")
    lines.append("  S (Square/Earth):  25.0%  — Structure / Address")
    lines.append("  F (Flower/Fire):   25.0%  — Relation / Corridor")
    lines.append("  C (Cloud/Water):   25.0%  — Observation / Fiber")
    lines.append("  R (Fractal/Air):   25.0%  — Compression / Seed")

    # Bridge weights from brain
    if brain is not None:
        ws = brain.get("weight_system", {})
        bridges = brain.get("bridges", {})

        lines.append("\n### Bridge Weights")
        if ws:
            bw = ws.get("base_weights", {})
            lines.append(f"  Self-loop:      {bw.get('self_loop', '?')}")
            lines.append(f"  Pair bridge:    {bw.get('pair_bridge', '?')}")
            lines.append(f"  Triple closure: {bw.get('triple_closure', '?')}")
            lines.append(f"  Full aether:    {bw.get('full_aether', '?')}")

        lines.append("\n### Pair Bridge Detail")
        for key, bridge in bridges.items():
            lines.append(
                f"  {key}: w={bridge.get('weight', '?')} "
                f"({bridge.get('resonance_type', '?')})"
            )

        # Resonance classes
        rp = ws.get("resonance_pairs", {})
        if rp:
            lines.append("\n### Resonance Classes")
            lines.append(f"  Golden  (phi^-1 = 0.618): {', '.join(rp.get('golden', []))}")
            lines.append(f"  Neutral (0.500):           {', '.join(rp.get('neutral', []))}")
            lines.append(f"  Distant (phi^-2 = 0.382): {', '.join(rp.get('distant', []))}")
    else:
        lines.append("\n### Bridge Weights")
        lines.append("  [NOT LOADED — brain_network.json not found]")

    # Metro line utilization (from graph edge types if available)
    graph = _safe_load(_GRAPH_CACHE)
    if graph is not None:
        stats = _compute_graph_stats(graph)
        metro_edges = {k: v for k, v in stats["edge_counts"].items()
                       if k.startswith("M") or "metro" in k.lower()}
        if metro_edges:
            lines.append("\n### Metro Line Utilization")
            total_metro = sum(metro_edges.values()) or 1
            for line, count in sorted(metro_edges.items(), key=lambda x: -x[1]):
                pct = 100 * count / total_metro
                lines.append(f"  {line}: {count:,} edges ({pct:.1f}%)")

    return "\n".join(lines)


def _render_history() -> str:
    """Render the last 50 steering actions."""
    try:
        conn = _ensure_db()
        cursor = conn.execute(
            "SELECT id, timestamp, action, target, parameters, result, "
            "crystal_coordinate, agent_id "
            "FROM steering_log ORDER BY id DESC LIMIT 50"
        )
        rows = cursor.fetchall()
        conn.close()
    except Exception as exc:
        return f"## Control Center — History\n\nError reading ledger: {exc}"

    lines = [
        "## Control Center — Steering History\n",
        f"**Total entries shown**: {len(rows)}\n",
    ]

    if not rows:
        lines.append("(no steering actions recorded)")
        return "\n".join(lines)

    for r in rows:
        sid, ts, action, target, params, result, coord, agent = r
        lines.append(f"### #{sid} — {action}")
        lines.append(f"  Time: {ts}")
        lines.append(f"  Target: {target}")
        lines.append(f"  Parameters: {params}")
        lines.append(f"  Result: {result}")
        if coord:
            lines.append(f"  Crystal Coordinate: {coord}")
        lines.append(f"  Agent: {agent}")
        lines.append("")

    return "\n".join(lines)


def _render_alerts(graph: dict | None) -> str:
    """Render detected anomalies."""
    stats = _compute_graph_stats(graph)
    recent = _get_recent_steerings(1)
    alerts = _detect_alerts(stats, recent)

    lines = [
        "## Control Center — Alerts\n",
        f"**Timestamp**: {datetime.now(timezone.utc).isoformat()}",
        f"**Status**: {'ALERT' if alerts else 'NOMINAL'}\n",
    ]

    if not alerts:
        lines.append("No anomalies detected. Organism is nominal.")
    else:
        lines.append(f"**{len(alerts)} anomaly(ies) detected**:\n")
        for i, a in enumerate(alerts, 1):
            # Parse alert type
            parts = a.split(":", 1)
            atype = parts[0].strip()
            detail = parts[1].strip() if len(parts) > 1 else a
            lines.append(f"### Alert {i}: {atype}")
            lines.append(f"  {detail}\n")

        # Recommendations
        lines.append("### Recommended Steering Actions")
        for a in alerts:
            if "SFCR_IMBALANCE" in a:
                # Find the low element
                for code in _SFCR_CODES:
                    if code in a:
                        lines.append(
                            f"  -> control_steer(action='rebalance_sfcr', "
                            f"target='{code}', parameters='{{\"target_pct\": 25}}')"
                        )
            elif "LOW_DENSITY" in a:
                lines.append(
                    "  -> control_steer(action='create_route', "
                    "target='<node_a>-><node_b>', parameters='{\"line\": \"Mt\"}')"
                )
            elif "STAGNATION" in a:
                lines.append(
                    "  -> Any steering action will clear this alert"
                )
            elif "PHASE_FREEZE" in a:
                lines.append(
                    "  -> control_steer(action='shift_phase', "
                    "target='<shard_path>', parameters='{\"new_phase\": \"Cardinal\"}')"
                )

    return "\n".join(lines)


# ── MCP Tool: control_steer ──────────────────────────────────────────

def control_steer(
    action: str = "promote_shard",
    target: str = "",
    parameters: str = "{}",
) -> str:
    """Execute a steering command on the organism.

    Steering actions transform the control center from passive observation
    into active cockpit control. Each action is logged to a persistent
    SQLite ledger for audit and replay.

    Actions:
      promote_shard  — Promote a shard to a higher shell
        target: path/to/file
        parameters: {"target_shell": 5}

      shift_phase    — Shift a shard's phase (Fixed/Cardinal/Mutable)
        target: path/to/file
        parameters: {"new_phase": "Cardinal"}

      create_route   — Create a metro route between nodes
        target: "node_a->node_b"  (use -> as separator)
        parameters: {"line": "Mt"}

      rebalance_sfcr — Rebalance an SFCR element's target percentage
        target: element code (S, F, C, or R)
        parameters: {"target_pct": 25}

      emit_seed      — Emit a compression seed from a shell
        target: "shell:N"
        parameters: {"compression": 8}
    """
    # Validate action
    if action not in _VALID_ACTIONS:
        return (
            f"Invalid action: {action}. "
            f"Valid actions: {', '.join(sorted(_VALID_ACTIONS))}"
        )

    if not target:
        return "Error: target is required."

    # Parse parameters
    try:
        params = json.loads(parameters) if isinstance(parameters, str) else parameters
    except json.JSONDecodeError:
        return f"Error: invalid JSON in parameters: {parameters}"

    # Validate and simulate each action
    result, coord = _simulate_action(action, target, params)

    # Log to SQLite ledger
    ts = datetime.now(timezone.utc).isoformat()
    try:
        conn = _ensure_db()
        conn.execute(
            "INSERT INTO steering_log "
            "(timestamp, action, target, parameters, result, crystal_coordinate) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (ts, action, target, json.dumps(params), result, coord),
        )
        conn.commit()

        # Also snapshot current organism state
        _save_snapshot(conn)
        conn.close()
    except Exception as exc:
        return f"Steering logged but DB error: {exc}\n\n{result}"

    lines = [
        "## Control Center — Steering Executed\n",
        f"**Action**: {action}",
        f"**Target**: {target}",
        f"**Parameters**: {json.dumps(params)}",
        f"**Timestamp**: {ts}",
    ]
    if coord:
        lines.append(f"**Crystal Coordinate**: {coord}")
    lines.append(f"\n### Result\n{result}")
    lines.append("\n*Steering command logged to control_center.db*")

    return "\n".join(lines)


def _simulate_action(action: str, target: str, params: dict) -> tuple[str, str]:
    """Simulate a steering action and return (result_text, crystal_coordinate)."""
    coord = _lookup_coordinate(target)

    if action == "promote_shard":
        target_shell = params.get("target_shell", "?")
        if not isinstance(target_shell, int) or target_shell < 1:
            return "Error: target_shell must be a positive integer.", coord
        # Check if shard exists in graph
        graph = _safe_load(_GRAPH_CACHE)
        current_shell = "?"
        if graph is not None:
            for node in graph.get("nodes", []):
                node_path = node.get("path", node.get("id", ""))
                if target in str(node_path):
                    current_shell = node.get("shell", node.get("depth", "?"))
                    break
        return (
            f"WOULD promote shard '{target}' from shell {current_shell} "
            f"to shell {target_shell}.\n"
            f"This moves the shard higher in the HPRO hierarchy, "
            f"increasing its visibility and routing priority."
        ), coord

    elif action == "shift_phase":
        new_phase = params.get("new_phase", "")
        if new_phase not in _VALID_PHASES:
            return (
                f"Error: new_phase must be one of {_VALID_PHASES}. Got: {new_phase}",
                coord,
            )
        # Look up current phase
        graph = _safe_load(_GRAPH_CACHE)
        current_phase = "?"
        if graph is not None:
            for node in graph.get("nodes", []):
                node_path = node.get("path", node.get("id", ""))
                if target in str(node_path):
                    current_phase = node.get("phase", node.get("modality", "?"))
                    break
        return (
            f"WOULD shift phase of '{target}' from {current_phase} "
            f"to {new_phase}.\n"
            f"Phase shifts change the shard's temporal behavior:\n"
            f"  Fixed    = stable, archival\n"
            f"  Cardinal = active, initiating change\n"
            f"  Mutable  = adaptive, in transition"
        ), coord

    elif action == "create_route":
        line = params.get("line", "Mt")
        # Parse node_a->node_b
        if "->" in target:
            node_a, node_b = target.split("->", 1)
        else:
            return "Error: target must be 'node_a->node_b' format.", coord
        return (
            f"WOULD create metro route on line '{line}':\n"
            f"  From: {node_a.strip()}\n"
            f"  To:   {node_b.strip()}\n"
            f"This adds a new edge to the mycelium graph, "
            f"increasing connectivity and density."
        ), coord

    elif action == "rebalance_sfcr":
        target_code = target.upper()
        if target_code not in _SFCR_CODES:
            return (
                f"Error: target must be an SFCR element code (S, F, C, R). "
                f"Got: {target}",
                coord,
            )
        target_pct = params.get("target_pct", 25)
        # Current balance
        graph = _safe_load(_GRAPH_CACHE)
        stats = _compute_graph_stats(graph)
        current_pct = stats["sfcr_pct"].get(target_code, 0.0)
        return (
            f"WOULD rebalance {_SFCR_NAMES[target_code]} from "
            f"{current_pct:.1f}% to {target_pct}%.\n"
            f"Current SFCR balance:\n"
            + "\n".join(
                f"  {c}: {stats['sfcr_pct'].get(c, 0.0):.1f}%"
                for c in ("S", "F", "C", "R")
            )
            + f"\nRebalancing would adjust shard element tagging and "
            f"metro line routing to shift weight toward {target_code}."
        ), coord

    elif action == "emit_seed":
        compression = params.get("compression", 8)
        # Parse shell:N
        shell_num = "?"
        if target.startswith("shell:"):
            try:
                shell_num = int(target.split(":")[1])
            except (ValueError, IndexError):
                return "Error: target must be 'shell:N' format.", coord
        else:
            return "Error: target must be 'shell:N' format.", coord
        return (
            f"WOULD emit compression seed from shell {shell_num} "
            f"with compression factor {compression}.\n"
            f"Seed emission compresses the state of all shards in shell {shell_num} "
            f"into a minimal regenerative checkpoint (the 4D inverse crystal seed).\n"
            f"Compression {compression} = {108 // compression if compression else '?'} "
            f"dimensions retained."
        ), coord

    return "Unknown action (should not reach here).", coord


def _save_snapshot(conn: sqlite3.Connection) -> None:
    """Save a point-in-time organism snapshot."""
    try:
        graph = _safe_load(_GRAPH_CACHE)
        stats = _compute_graph_stats(graph)
        recent = _get_recent_steerings(1)
        alerts = _detect_alerts(stats, recent)

        conn.execute(
            "INSERT INTO organism_snapshots "
            "(timestamp, graph_density, sfcr_balance, phase_distribution, "
            "depth_distribution, edge_counts, alerts) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                datetime.now(timezone.utc).isoformat(),
                stats["density"],
                json.dumps(stats["sfcr_pct"]),
                json.dumps(stats["phase_pct"]),
                json.dumps(stats["depth_dist"]),
                json.dumps(stats["edge_counts"]),
                json.dumps(alerts),
            ),
        )
        conn.commit()
    except Exception:
        pass  # Snapshot failure should not block steering
