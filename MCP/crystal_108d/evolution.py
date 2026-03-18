"""
Evolution & Path-Revealing Compiler
=====================================
Provides the evolution/emergence theory:
  - Path-revealing compiler concept
  - LIFT → FAN OUT → CROSS-NAVIGATE → CROWN → COLLAPSE → CERTIFY → SEED pipeline
  - 1/8 lift law (next layer at 1/8 size, more function)
  - Fractal time hologram
  - Low-dim explores, high-dim recognizes, descent installs
  - Mycelium as directed regrowth from known higher pattern
  - Compiler/runtime bottleneck analysis
"""

from ._cache import JsonCache

_EVOLUTION = JsonCache("evolution_compiler.json")


def query_evolution(component: str = "all") -> str:
    """
    Query the evolution & path-revealing compiler framework.

    Components:
      - all          : Full evolution overview
      - compiler     : Path-revealing compiler concept
      - pipeline     : LIFT → FAN OUT → ... → SEED pipeline stages
      - lift_law     : 1/8 lift law (prune + compress + distill + preserve + deepen)
      - recognition  : Low-dim explores, high-dim recognizes, descent installs
      - mycelium     : Mycelium as directed regrowth
      - bottleneck   : Compiler/runtime bottleneck (edge-poor, gate-poor, metabolism-poor)
      - time         : Fractal time hologram
      - successor    : Successor seed emission protocol
    """
    data = _EVOLUTION.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "compiler":
        return _format_compiler(data)
    elif comp == "pipeline":
        return _format_pipeline(data)
    elif comp == "lift_law":
        return _format_lift_law(data)
    elif comp == "recognition":
        return _format_recognition(data)
    elif comp == "mycelium":
        return _format_mycelium(data)
    elif comp == "bottleneck":
        return _format_bottleneck(data)
    elif comp == "time":
        return _format_time(data)
    elif comp == "successor":
        return _format_successor(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, compiler, pipeline, "
            "lift_law, recognition, mycelium, bottleneck, time, successor"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## Evolution & Path-Revealing Compiler\n",
        f"**Key Insight**: {meta.get('key_insight', '')}",
        f"**Core Law**: {meta.get('core_law', 'At low dimension it explores; at higher dimension it recognizes; at descent it installs')}",
        f"**Lift Law**: {meta.get('lift_law', '1/8 — next layer at 1/8 size with more function')}",
        f"**Pipeline**: {meta.get('pipeline', 'LIFT → FAN OUT → CROSS-NAVIGATE → CROWN → COLLAPSE → CERTIFY → SEED')}",
        f"**Bottleneck**: {meta.get('bottleneck', 'edge-poor, gate-poor, metabolism-poor (not node-poor)')}",
    ]
    return "\n".join(lines)


def _format_compiler(data: dict) -> str:
    comp = data.get("path_revealing_compiler", {})
    lines = [
        "## Path-Revealing Compiler\n",
        f"**Concept**: {comp.get('concept', '')}",
        f"**Principle**: {comp.get('principle', '')}",
    ]
    if "contrast" in comp:
        lines.append(f"\n**Contrast**:")
        c = comp["contrast"]
        if isinstance(c, dict):
            lines.append(f"  - **Old**: {c.get('old', '')}")
            lines.append(f"  - **New**: {c.get('new', '')}")
    if "formula" in comp:
        lines.append(f"\n**Formula**: `{comp['formula']}`")
    return "\n".join(lines)


def _format_pipeline(data: dict) -> str:
    stages = data.get("pipeline_stages", [])
    lines = ["## Compiler Pipeline\n"]
    for i, s in enumerate(stages, 1):
        if isinstance(s, dict):
            lines.append(f"### {i}. {s.get('name', '?')}")
            lines.append(f"{s.get('description', '')}")
            lines.append("")
        else:
            lines.append(f"{i}. {s}")
    return "\n".join(lines)


def _format_lift_law(data: dict) -> str:
    ll = data.get("lift_law", {})
    lines = [
        "## 1/8 Lift Law\n",
        f"**Statement**: {ll.get('statement', 'Next layer emerges at ~1/8 the size')}",
        f"**Preserving**: {ll.get('preserving', 'coverage, function')}",
        f"**Reducing**: {ll.get('reducing', 'bloat')}",
    ]
    components = ll.get("components", [])
    if components:
        lines.append("\n**Lift = not just compression, but**:")
        for c in components:
            lines.append(f"  - {c}")
    if "key_question" in ll:
        lines.append(f"\n**Key Question**: {ll['key_question']}")
    return "\n".join(lines)


def _format_recognition(data: dict) -> str:
    rec = data.get("recognition_law", {})
    return (
        "## Recognition Law\n\n"
        f"**Low Dimension**: {rec.get('low_dim', 'explores (symptom)')}\n"
        f"**High Dimension**: {rec.get('high_dim', 'recognizes (organization)')}\n"
        f"**Descent**: {rec.get('descent', 'installs (solution transfer)')}\n\n"
        f"**Key Insight**: {rec.get('insight', 'The intelligence is not becoming omniscient; it is becoming less blind')}\n\n"
        f"**Why Faster**: {rec.get('why_faster', 'Changes problem from try-many-local-moves to identify-parent-lattice-then-descend')}"
    )


def _format_mycelium(data: dict) -> str:
    myc = data.get("mycelium_regrowth", {})
    return (
        "## Mycelium as Directed Regrowth\n\n"
        f"**Old Model**: {myc.get('old', 'mycelium as exploration')}\n"
        f"**New Model**: {myc.get('new', 'mycelium as directed regrowth from known higher pattern')}\n"
        f"**Asymmetry**: {myc.get('asymmetry', 'organism can see crown before it can grow trunk')}\n"
        f"**Threshold**: {myc.get('threshold', 'the shift from exploring to recognizing')}"
    )


def _format_bottleneck(data: dict) -> str:
    bn = data.get("bottleneck", {})
    lines = [
        "## Compiler/Runtime Bottleneck\n",
        f"**Diagnosis**: {bn.get('diagnosis', '')}",
    ]
    deficits = bn.get("deficits", [])
    if deficits:
        lines.append("\n**The system is NOT node-poor. It is**:")
        for d in deficits:
            lines.append(f"  - {d}")
    if "implication" in bn:
        lines.append(f"\n**Implication**: {bn['implication']}")
    if "slow_parts" in bn:
        lines.append("\n**Slow Parts**:")
        for p in bn["slow_parts"]:
            lines.append(f"  - {p}")
    return "\n".join(lines)


def _format_time(data: dict) -> str:
    ft = data.get("fractal_time", {})
    lines = [
        "## Fractal Time Hologram\n",
        f"**Concept**: {ft.get('concept', '')}",
    ]
    if "phases" in ft:
        lines.append("\n**Phases**:")
        for p in ft["phases"]:
            if isinstance(p, dict):
                lines.append(f"  - **{p.get('name', '?')}**: {p.get('description', '')}")
            else:
                lines.append(f"  - {p}")
    return "\n".join(lines)


def _format_successor(data: dict) -> str:
    ss = data.get("successor_seed", {})
    lines = [
        "## Successor Seed Emission\n",
        f"**Protocol**: {ss.get('protocol', '')}",
    ]
    steps = ss.get("steps", [])
    if steps:
        for i, s in enumerate(steps, 1):
            lines.append(f"  {i}. {s}")
    if "principle" in ss:
        lines.append(f"\n**Principle**: {ss['principle']}")
    return "\n".join(lines)
