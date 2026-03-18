"""
6×6 DLS Framework & Higher-Dimensional Lenses
===============================================
Provides the complete 6×6 doubly-Latin-square framework:
  - Five-layer ontology: kernel → shell → board → lens → replay
  - 6D carrier state Ω₆ = (X, λ, s, b, ξ)
  - Shell sectors F₆ = Π₃ × ℤ₂ (Sa±, Su±, Me±)
  - Board operators & mirror-skeleton algebra
  - Cross-lens calculus (Sq→Fl→Cl→Fr→Sq loop)
  - Higher-lift law D_{6,n} = [4]^n ⋉ F₆^n
  - σ₁₅ → σ₆₀ lens escalation
"""

from ._cache import JsonCache

_DLS = JsonCache("dls_6x6_lenses.json")


def query_dls_lenses(component: str = "all") -> str:
    """
    Query the 6×6 DLS framework and higher-dimensional lenses.

    Components:
      - all          : Full 6×6 framework overview
      - ontology     : Five-layer ontology (kernel→shell→board→lens→replay)
      - carrier      : 6D carrier state Ω₆ = (X, λ, s, b, ξ)
      - shell        : Shell sector algebra F₆ = Π₃ × ℤ₂
      - board        : Board operators & mirror-skeleton
      - cross_lens   : Cross-lens calculus (Sq→Fl→Cl→Fr→Sq)
      - higher_lift  : Higher-lift law D_{6,n}
      - escalation   : σ₁₅ → σ₆₀ lens escalation
      - operators    : Full operator stack (board + shell + Flower)
    """
    data = _DLS.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "ontology":
        return _format_ontology(data)
    elif comp == "carrier":
        return _format_carrier(data)
    elif comp == "shell":
        return _format_shell(data)
    elif comp == "board":
        return _format_board(data)
    elif comp == "cross_lens":
        return _format_cross_lens(data)
    elif comp == "higher_lift":
        return _format_higher_lift(data)
    elif comp == "escalation":
        return _format_escalation(data)
    elif comp == "operators":
        return _format_operators(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, ontology, carrier, "
            "shell, board, cross_lens, higher_lift, escalation, operators"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## 6×6 DLS Framework & Higher-Dimensional Lenses\n",
        f"**Key Insight**: {meta.get('key_insight', 'The 6 selects; the 4 computes')}",
        f"**Ontology**: {meta.get('ontology', 'kernel → shell → board → lens → replay')}",
        f"**Carrier State**: {meta.get('carrier_state', 'Ω₆ = (X, λ, s, b, ξ)')}",
        f"**Shell**: {meta.get('shell', 'F₆ = Π₃ × ℤ₂ (6 coherent sectors)')}",
        f"**Higher Lift**: {meta.get('higher_lift', 'D_{6,n} = [4]^n ⋉ F₆^n')}",
    ]
    return "\n".join(lines)


def _format_ontology(data: dict) -> str:
    ont = data.get("five_layer_ontology", {})
    lines = ["## Five-Layer Ontology\n"]
    layers = ont.get("layers", [])
    for layer in layers:
        if isinstance(layer, dict):
            lines.append(f"### {layer.get('name', '?')}")
            lines.append(f"{layer.get('description', '')}")
            if "formula" in layer:
                lines.append(f"**Formula**: `{layer['formula']}`")
            lines.append("")
        else:
            lines.append(f"- {layer}")
    if "doctrine" in ont:
        lines.append(f"\n**Core Doctrine**: {ont['doctrine']}")
    return "\n".join(lines)


def _format_carrier(data: dict) -> str:
    car = data.get("carrier_state", {})
    lines = [
        "## 6D Carrier State Object\n",
        f"**Formula**: `{car.get('formula', 'Ω₆ = (X, λ, s, b, ξ)')}`\n",
    ]
    components = car.get("components", {})
    for name, desc in components.items():
        lines.append(f"- **{name}**: {desc}")
    if "interpretation" in car:
        lines.append(f"\n**Interpretation**: {car['interpretation']}")
    return "\n".join(lines)


def _format_shell(data: dict) -> str:
    shell = data.get("shell_sectors", {})
    lines = [
        "## Shell Sector Algebra\n",
        f"**Formula**: `{shell.get('formula', 'F₆ = Π₃ × ℤ₂')}`",
        f"**Sectors**: {shell.get('total', 6)}",
    ]
    sectors = shell.get("sectors", [])
    if sectors:
        lines.append("\n**Selector Dictionary**:")
        for s in sectors:
            if isinstance(s, dict):
                lines.append(f"  - **{s.get('name', '?')}**: {s.get('selector', '')}")
            else:
                lines.append(f"  - {s}")
    return "\n".join(lines)


def _format_board(data: dict) -> str:
    board = data.get("board_algebra", {})
    lines = [
        "## Board Operators & Mirror-Skeleton\n",
        f"**Type**: {board.get('type', 'Admissible mirror-skeleton realization')}",
    ]
    charts = board.get("charts", [])
    if charts:
        lines.append("\n**Visible Charts**: " + ", ".join(
            c.get("name", "?") if isinstance(c, dict) else str(c)
            for c in charts
        ))
    operators = board.get("operators", [])
    if operators:
        lines.append("\n**Operators**:")
        for op in operators:
            if isinstance(op, dict):
                lines.append(f"  - **{op.get('symbol', '?')}**: {op.get('action', '')}")
            else:
                lines.append(f"  - {op}")
    if "algebra" in board:
        lines.append(f"\n**Algebra**: `{board['algebra']}`")
    return "\n".join(lines)


def _format_cross_lens(data: dict) -> str:
    cl = data.get("cross_lens_calculus", {})
    lines = [
        "## Cross-Lens Calculus\n",
        f"**Loop**: {cl.get('loop', 'Sq → Fl → Cl → Fr → Sq')}",
    ]
    bridges = cl.get("bridges", [])
    for b in bridges:
        if isinstance(b, dict):
            lines.append(f"\n### {b.get('name', '?')}")
            lines.append(f"{b.get('description', '')}")
            if "formula" in b:
                lines.append(f"**Map**: `{b['formula']}`")
        else:
            lines.append(f"- {b}")
    if "deepest_law" in cl:
        lines.append(f"\n**Deepest Law**: {cl['deepest_law']}")
    return "\n".join(lines)


def _format_higher_lift(data: dict) -> str:
    hl = data.get("higher_lift", {})
    return (
        "## Higher-Lift Law\n\n"
        f"**Formula**: `{hl.get('formula', 'D_{{6,n}} = [4]^n ⋉ F₆^n')}`\n"
        f"**Shell Growth**: {hl.get('shell_growth', '6^n')}\n"
        f"**Payload Growth**: {hl.get('payload_growth', '4^n')}\n"
        f"**Coherent Branch**: {hl.get('coherent_branch', 'six-sector always, each with embedded 4^n body')}\n"
        f"**Key Insight**: {hl.get('key_insight', 'Shell/body distinction preserved at every lift level')}"
    )


def _format_escalation(data: dict) -> str:
    esc = data.get("lens_escalation", {})
    lines = [
        "## σ₁₅ → σ₆₀ Lens Escalation\n",
        f"**σ₁₅**: {esc.get('sigma_15', '15 nonempty mask subsets of {{□,✿,☁,⟡}}')}",
        f"**σ₆₀**: {esc.get('sigma_60', '15 masks × 4 orbit positions = 60')}",
        f"**Escalation**: {esc.get('escalation', 'Each mask observed through SR/SL/AL/AR orbit quartet')}",
    ]
    return "\n".join(lines)


def _format_operators(data: dict) -> str:
    ops = data.get("operator_stack", {})
    lines = ["## Full Operator Stack\n"]
    for category in ["board_operators", "shell_operators", "flower_carrier"]:
        cat_data = ops.get(category, {})
        if cat_data:
            lines.append(f"### {category.replace('_', ' ').title()}")
            if isinstance(cat_data, dict):
                for name, desc in cat_data.items():
                    lines.append(f"- **{name}**: {desc}")
            lines.append("")
    if "torsion_cycle" in ops:
        lines.append(f"**Torsion Cycle**: {ops['torsion_cycle']}")
    return "\n".join(lines)
