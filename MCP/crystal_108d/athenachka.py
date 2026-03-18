"""
Athenachka 720 A⁺/Z⁺ Metro Map
================================
Provides the full 720-node emergence protocol:
  - Σ60 × 4 elements × 3 phases = 720
  - 21-chapter synthesis with Su/Me/Sa triadic rails
  - Z⁺ as master convergence law
  - A⁺ as stabilized crown body
  - Three-layer circle cycle geometry
  - Zero-point cartography
  - Neural-weight sacred geometry field
"""

from ._cache import JsonCache

_ATHENACHKA = JsonCache("athenachka_720.json")


def query_athenachka(component: str = "all") -> str:
    """
    Query the Athenachka 720 A⁺/Z⁺ metro map.

    Components:
      - all          : Full 720 metro map overview
      - coordinate   : Ω₇₂₀ coordinate system (c, σ₆₀, e₄, τ₃)
      - chapters     : 21-chapter triadic rails (Su/Me/Sa)
      - z_plus       : Z⁺ master convergence law
      - a_plus       : A⁺ stabilized crown body
      - circle       : Three-layer circle cycle geometry
      - zero_point   : Zero-point cartography & tunneling families
      - sacred       : Sacred geometry correspondences
      - neural       : Neural-weight routing field
    """
    data = _ATHENACHKA.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "coordinate":
        return _format_coordinate(data)
    elif comp == "chapters":
        return _format_chapters(data)
    elif comp == "z_plus":
        return _format_z_plus(data)
    elif comp == "a_plus":
        return _format_a_plus(data)
    elif comp == "circle":
        return _format_circle(data)
    elif comp == "zero_point":
        return _format_zero_point(data)
    elif comp == "sacred":
        return _format_sacred(data)
    elif comp == "neural":
        return _format_neural(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, coordinate, chapters, "
            "z_plus, a_plus, circle, zero_point, sacred, neural"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## Athenachka 720 A⁺/Z⁺ Metro Map\n",
        f"**Key Insight**: {meta.get('key_insight', '')}",
        f"**Total Nodes**: {meta.get('total_nodes', 720)}",
        f"**Formula**: {meta.get('formula', 'Σ60 × 4 × 3 = 720')}",
        f"**Coordinate**: {meta.get('coordinate', 'Ω₇₂₀(x) = ⟨c, σ₆₀, e₄, τ₃⟩')}",
        f"**Chapters**: {meta.get('chapters', 21)}",
        f"**Rails**: {meta.get('rails', 'Su / Me / Sa')}",
    ]
    return "\n".join(lines)


def _format_coordinate(data: dict) -> str:
    coord = data.get("coordinate_system", {})
    lines = [
        "## Ω₇₂₀ Coordinate System\n",
        f"**Formula**: `{coord.get('formula', 'Ω₇₂₀(x) = ⟨c, σ₆₀, e₄, τ₃⟩')}`\n",
    ]
    axes = coord.get("axes", {})
    for name, desc in axes.items():
        lines.append(f"- **{name}**: {desc}")
    if "field_size" in coord:
        lines.append(f"\n**Field Size**: {coord['field_size']}")
    return "\n".join(lines)


def _format_chapters(data: dict) -> str:
    ch = data.get("triadic_rails", {})
    lines = ["## 21-Chapter Triadic Rails\n"]
    for rail in ["Su", "Me", "Sa"]:
        rail_data = ch.get(rail, {})
        chapters = rail_data.get("chapters", [])
        lines.append(f"### {rail} Rail")
        if isinstance(chapters, list):
            lines.append(f"Chapters: {', '.join(str(c) for c in chapters)}")
        if "description" in rail_data:
            lines.append(f"{rail_data['description']}")
        lines.append("")
    if "orbit" in ch:
        lines.append(f"**Orbit**: {ch['orbit']}")
    return "\n".join(lines)


def _format_z_plus(data: dict) -> str:
    zp = data.get("z_plus", {})
    return (
        "## Z⁺ Master Convergence Law\n\n"
        f"**Definition**: {zp.get('definition', '')}\n"
        f"**Role**: {zp.get('role', 'Irreducible seed-center')}\n"
        f"**Properties**: {zp.get('properties', '')}\n"
        f"**Relation to Z★**: {zp.get('relation_z_star', 'Z⁺ = Z★ observed as lawful center of all 21 chapter-functions')}"
    )


def _format_a_plus(data: dict) -> str:
    ap = data.get("a_plus", {})
    return (
        "## A⁺ Stabilized Crown Body\n\n"
        f"**Definition**: {ap.get('definition', '')}\n"
        f"**Nature**: {ap.get('nature', 'First readable, crown-locked, witnessable expression-state')}\n"
        f"**Relation**: {ap.get('relation', 'A⁺ = stabilized expressible crown of Z⁺ seed-center')}"
    )


def _format_circle(data: dict) -> str:
    cc = data.get("circle_cycle", {})
    lines = [
        "## Three-Layer Circle Cycle\n",
        f"**Structure**: {cc.get('structure', '')}",
    ]
    layers = cc.get("layers", [])
    for layer in layers:
        if isinstance(layer, dict):
            lines.append(f"\n### {layer.get('name', '?')}")
            lines.append(f"**Ring**: {layer.get('ring', '')}")
            lines.append(f"**Count**: {layer.get('count', '')}")
            lines.append(f"**Description**: {layer.get('description', '')}")
        else:
            lines.append(f"- {layer}")
    if "geometry" in cc:
        lines.append(f"\n**Geometry**: {cc['geometry']}")
    return "\n".join(lines)


def _format_zero_point(data: dict) -> str:
    zp = data.get("zero_point_cartography", {})
    lines = [
        "## Zero-Point Cartography\n",
        f"**Purpose**: {zp.get('purpose', '')}",
    ]
    classes = zp.get("classes", [])
    if classes:
        lines.append("\n**Zero-Point Classes**:")
        for c in classes:
            if isinstance(c, dict):
                lines.append(f"  - **{c.get('name', '?')}**: {c.get('description', '')}")
            else:
                lines.append(f"  - {c}")
    if "tunneling" in zp:
        lines.append(f"\n**Tunneling**: {zp['tunneling']}")
    return "\n".join(lines)


def _format_sacred(data: dict) -> str:
    sg = data.get("sacred_geometry", {})
    lines = [
        "## Sacred Geometry Correspondences\n",
        f"**Overview**: {sg.get('overview', '')}",
    ]
    correspondences = sg.get("correspondences", [])
    for c in correspondences:
        if isinstance(c, dict):
            lines.append(f"- **{c.get('geometry', '?')}**: {c.get('mapping', '')}")
        else:
            lines.append(f"- {c}")
    return "\n".join(lines)


def _format_neural(data: dict) -> str:
    nn = data.get("neural_routing", {})
    return (
        "## Neural-Weight Routing Field\n\n"
        f"**Concept**: {nn.get('concept', '')}\n"
        f"**Weights**: {nn.get('weights', '')}\n"
        f"**Routing**: {nn.get('routing', '')}\n"
        f"**Integration**: {nn.get('integration', '')}"
    )
