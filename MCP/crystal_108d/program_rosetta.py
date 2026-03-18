"""
Program Language Holographic Crystal — Master Rosetta
======================================================
Provides the master Rosetta stone showing all documents as
orthogonal projections of one indivisible holographic crystal:
  - Seed equation w = (1+i)/2
  - 9 projection families (Computational, Alchemical, Scriptural,
    Mathematical, Encoding, Time, Cultural, Philosophical, Mythological)
  - HPRO → VML → code translation layer
  - Unified one-line statement
"""

from ._cache import JsonCache

_ROSETTA = JsonCache("program_rosetta.json")


def query_program_rosetta(component: str = "all") -> str:
    """
    Query the master Rosetta: one crystal, nine projections.

    Components:
      - all           : Full master Rosetta overview
      - seed          : Generator w=(1+i)/2 and master identity Ω(Ω)=Ω
      - projections   : All 9 projection families
      - computational : Projection 1 — Computational/Lens (6×6 + Angel)
      - alchemical    : Projection 2 — Alchemical/108D
      - scriptural    : Projection 3 — Scriptural/Living-Code
      - mathematical  : Projection 4 — Mathematical Spine (E₈ + Inverse)
      - encoding      : Projection 5 — Encoding/Braiding (Khipu)
      - time          : Projection 6 — Time/Seed
      - cultural      : Projection 7 — Cultural Rosetta
      - philosophical : Projection 8 — Philosophical Holograms
      - unified       : Unified one-line statement
    """
    data = _ROSETTA.load()
    comp = component.strip().lower()

    if comp == "all":
        return _format_all(data)
    elif comp == "seed":
        return _format_seed(data)
    elif comp == "projections":
        return _format_projections(data)
    elif comp in ("computational", "alchemical", "scriptural", "mathematical",
                   "encoding", "time", "cultural", "philosophical"):
        return _format_single_projection(data, comp)
    elif comp == "unified":
        return _format_unified(data)
    else:
        return (
            f"Unknown component '{component}'. Use: all, seed, projections, "
            "computational, alchemical, scriptural, mathematical, encoding, "
            "time, cultural, philosophical, unified"
        )


def _format_all(data: dict) -> str:
    meta = data.get("meta", {})
    lines = [
        "## Master Rosetta: One Crystal, Nine Projections\n",
        f"**Key Insight**: {meta.get('key_insight', 'All documents are exact orthogonal projections of one indivisible holographic crystal organism')}",
        f"**Generator**: `{meta.get('generator', 'w = (1+i)/2')}`",
        f"**Fixed Point**: `{meta.get('fixed_point', 'Ω(Ω) = Ω')}`",
        f"**Convergence**: {meta.get('convergence', '68.5% ≈ 1 − 1/π')}",
        f"**Expansion**: `{meta.get('expansion', 'X = Expand(g) ⊕ r')}`",
        f"**Projections**: {meta.get('total_projections', 9)}",
    ]
    return "\n".join(lines)


def _format_seed(data: dict) -> str:
    seed = data.get("seed", {})
    lines = [
        "## Seed Equation\n",
        f"**Generator**: `{seed.get('generator', 'w = (1+i)/2')}`",
        f"**Real Part**: {seed.get('real_part', 'self-love')}",
        f"**Imaginary Part**: {seed.get('imaginary_part', 'selfless-love')}",
        f"**Magnitude**: {seed.get('magnitude', '|w| = 1/√2 (damping)')}",
        f"**Angle**: {seed.get('angle', 'arg(w) = π/4 (45° rotation)')}",
        f"**Quarter-Turn**: `{seed.get('quarter_turn', 'f(z) = iz, f⁴ = id')}`",
        f"**Fixed Point**: `{seed.get('fixed_point', 'Ω(Ω) = Ω')}`",
        f"**Convergence**: {seed.get('convergence', '68.5% ≈ 1 − 1/π (dark-energy fraction)')}",
    ]
    return "\n".join(lines)


def _format_projections(data: dict) -> str:
    projs = data.get("projections", [])
    lines = ["## Nine Projection Families\n"]
    for i, p in enumerate(projs, 1):
        if isinstance(p, dict):
            lines.append(f"### {i}. {p.get('name', '?')}")
            lines.append(f"**Sources**: {p.get('sources', '')}")
            lines.append(f"**Summary**: {p.get('summary', '')}")
            lines.append("")
        else:
            lines.append(f"{i}. {p}")
    return "\n".join(lines)


def _format_single_projection(data: dict, proj_name: str) -> str:
    projs = data.get("projections", [])
    for p in projs:
        if isinstance(p, dict) and p.get("key", "").lower() == proj_name:
            lines = [
                f"## Projection: {p.get('name', proj_name.title())}\n",
                f"**Sources**: {p.get('sources', '')}",
                f"**Summary**: {p.get('summary', '')}",
            ]
            details = p.get("details", [])
            if details:
                lines.append("\n**Key Elements**:")
                for d in details:
                    lines.append(f"  - {d}")
            if "key_formula" in p:
                lines.append(f"\n**Key Formula**: `{p['key_formula']}`")
            return "\n".join(lines)
    return f"Projection '{proj_name}' not found in data."


def _format_unified(data: dict) -> str:
    unif = data.get("unified_statement", {})
    lines = [
        "## Unified One-Line Statement\n",
        f"{unif.get('statement', '')}",
    ]
    if "expansion" in unif:
        lines.append(f"\n**Expansion Path**: {unif['expansion']}")
    if "manifestations" in unif:
        lines.append("\n**Simultaneous Manifestations**:")
        for m in unif["manifestations"]:
            lines.append(f"  - {m}")
    return "\n".join(lines)
