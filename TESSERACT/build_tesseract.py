"""
Tesseract Builder — Decomposes chapters and appendixes into 4-lens × 4-facet projections.

Each monolithic chapter/appendix file is split into 16 projection files:
  4 lenses (S/F/C/R) × 4 facets (Objects/Laws/Constructions/Certificates)

Also builds the _PROJECTIONS index for 4th-dimensional navigation.
"""

import os
import re
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TESSERACT = Path(__file__).parent
CHAPTERS_DIR = REPO_ROOT / "DEEPER_CRYSTALIZATION" / "ACTIVE_NERVOUS_SYSTEM" / "04_CHAPTERS"
APPENDIX_DIR = REPO_ROOT / "DEEPER_CRYSTALIZATION" / "ACTIVE_NERVOUS_SYSTEM" / "05_APPENDICES"

LENSES = ["S", "F", "C", "R"]
LENS_NAMES = {"S": "Square", "F": "Flower", "C": "Cloud", "R": "Fractal"}
FACET_NAMES = {1: "Objects", 2: "Laws", 3: "Constructions", 4: "Certificates"}
FACET_DIRS = {1: "1_OBJECTS", 2: "2_LAWS", 3: "3_CONSTRUCTIONS", 4: "4_CERTIFICATES"}

# Chapter → Cell mapping
CHAPTER_CELLS = {
    1: "C0_KERNEL", 2: "C0_KERNEL", 3: "C0_KERNEL", 4: "C0_KERNEL",
    5: "C1_CORRIDOR", 6: "C1_CORRIDOR", 7: "C1_CORRIDOR", 8: "C1_CORRIDOR",
    9: "C2_METRO", 10: "C2_METRO", 11: "C2_METRO", 12: "C2_METRO",
    13: "C3_RUNTIME", 14: "C3_RUNTIME", 15: "C3_RUNTIME", 16: "C3_RUNTIME",
    17: "C4_DEPLOYMENT", 18: "C4_DEPLOYMENT", 19: "C4_DEPLOYMENT",
    20: "C4_DEPLOYMENT", 21: "C4_DEPLOYMENT",
}


def parse_crystal_tiles(content: str) -> dict:
    """Parse a chapter/appendix file into lens→facet→content dict.

    Looks for headers like:
        ### Lens S
        #### Facet 1 - Objects
    """
    result = {}

    # Extract title and routing role (header before first lens)
    title_match = re.match(r'^(#[^#].*?)(?=\n### Lens |\Z)', content, re.DOTALL)
    header = title_match.group(1).strip() if title_match else ""

    # Split by lens (handles "### Lens S" and "### Lens S - Square" variants)
    lens_pattern = re.compile(r'### Lens ([SFCR])[^\n]*\n(.*?)(?=### Lens [SFCR]|\Z)', re.DOTALL)

    for lens_match in lens_pattern.finditer(content):
        lens = lens_match.group(1)
        lens_content = lens_match.group(2)
        result[lens] = {}

        # Split by facet
        facet_pattern = re.compile(
            r'#### Facet (\d) - (\w+)\s*\n(.*?)(?=#### Facet \d|\Z)', re.DOTALL
        )

        for facet_match in facet_pattern.finditer(lens_content):
            facet_num = int(facet_match.group(1))
            facet_name = facet_match.group(2)
            facet_content = facet_match.group(3).strip()
            result[lens][facet_num] = {
                "name": facet_name,
                "content": facet_content,
            }

    return {"header": header, "tiles": result}


def build_projection_header(source_id: str, lens: str, facet: int, cell: str) -> str:
    """Build the crystal header for a projection file."""
    siblings = {l: f"../../{l}/{FACET_DIRS[facet]}/{cell}/{source_id}.{l}{facet}.md"
                for l in LENSES if l != lens}
    sibling_lines = "\n".join(f"#   {l}: {path}" for l, path in siblings.items())

    return (
        f"<!-- TESSERACT: {lens}/{FACET_DIRS[facet]}/{cell}/{source_id} -->\n"
        f"<!-- COORD: lens={lens} facet={facet}({FACET_NAMES[facet]}) cell={cell} -->\n"
        f"<!-- SIBLINGS:\n{sibling_lines}\n-->\n"
    )


def write_projection(source_id: str, lens: str, facet: int, cell: str,
                      header: str, content: str) -> Path:
    """Write a single projection file."""
    dir_path = TESSERACT / lens / FACET_DIRS[facet] / cell
    dir_path.mkdir(parents=True, exist_ok=True)

    file_path = dir_path / f"{source_id}.{lens}{facet}.md"

    proj_header = build_projection_header(source_id, lens, facet, cell)

    full_content = (
        f"{proj_header}\n"
        f"# {source_id} — {LENS_NAMES[lens]} Lens / {FACET_NAMES[facet]}\n\n"
        f"{content}\n"
    )

    file_path.write_text(full_content, encoding="utf-8")
    return file_path


def decompose_chapter(ch_path: Path) -> int:
    """Decompose a chapter file into 16 projection files. Returns count."""
    content = ch_path.read_text(encoding="utf-8")

    # Extract chapter number
    ch_match = re.match(r'Ch(\d+)', ch_path.stem)
    if not ch_match:
        return 0
    ch_num = int(ch_match.group(1))
    ch_id = f"Ch{ch_num:02d}"
    cell = CHAPTER_CELLS.get(ch_num, "C7_CORPUS")

    parsed = parse_crystal_tiles(content)
    count = 0

    for lens in LENSES:
        if lens not in parsed["tiles"]:
            # Create stub projection with the full content under this lens
            for facet in range(1, 5):
                write_projection(ch_id, lens, facet, cell, parsed["header"],
                                f"*[Projection pending — source file does not have {LENS_NAMES[lens]} lens decomposition]*\n\n"
                                f"Source: `{ch_path.name}`")
                count += 1
            continue

        for facet in range(1, 5):
            if facet in parsed["tiles"][lens]:
                tile = parsed["tiles"][lens][facet]
                write_projection(ch_id, lens, facet, cell, parsed["header"],
                                tile["content"])
            else:
                write_projection(ch_id, lens, facet, cell, parsed["header"],
                                f"*[Facet {facet} ({FACET_NAMES[facet]}) not found in source]*")
            count += 1

    return count


def decompose_appendix(app_path: Path, is_inverse: bool = False) -> int:
    """Decompose an appendix file into 16 projection files."""
    content = app_path.read_text(encoding="utf-8")

    # Extract appendix ID
    stem = app_path.stem
    if is_inverse:
        inv_match = re.match(r'(Inv[A-Z])', stem)
        if not inv_match:
            return 0
        app_id = inv_match.group(1)
        cell = "C6_APPENDIX_INV"
    else:
        app_match = re.match(r'(App[A-Z])', stem)
        if not app_match:
            return 0
        app_id = app_match.group(1)
        cell = "C5_APPENDIX_FWD"

    parsed = parse_crystal_tiles(content)
    count = 0

    for lens in LENSES:
        if lens not in parsed["tiles"]:
            for facet in range(1, 5):
                write_projection(app_id, lens, facet, cell, parsed["header"],
                                f"*[Projection pending — source does not have {LENS_NAMES[lens]} lens]*\n\n"
                                f"Source: `{app_path.name}`")
                count += 1
            continue

        for facet in range(1, 5):
            if facet in parsed["tiles"][lens]:
                tile = parsed["tiles"][lens][facet]
                write_projection(app_id, lens, facet, cell, parsed["header"],
                                tile["content"])
            else:
                write_projection(app_id, lens, facet, cell, parsed["header"],
                                f"*[Facet {facet} ({FACET_NAMES[facet]}) not found in source]*")
            count += 1

    return count


def build_projection_indexes() -> int:
    """Build the _PROJECTIONS directory with cross-references."""
    proj_dir = TESSERACT / "_PROJECTIONS"
    count = 0

    # by_chapter index
    for ch_num in range(1, 22):
        ch_id = f"Ch{ch_num:02d}"
        ch_dir = proj_dir / "by_chapter" / ch_id
        ch_dir.mkdir(parents=True, exist_ok=True)
        cell = CHAPTER_CELLS.get(ch_num, "C7_CORPUS")

        index_lines = [f"# {ch_id} — All Projections\n"]
        for lens in LENSES:
            index_lines.append(f"\n## {LENS_NAMES[lens]} Lens ({lens})\n")
            for facet in range(1, 5):
                rel_path = f"../../{lens}/{FACET_DIRS[facet]}/{cell}/{ch_id}.{lens}{facet}.md"
                index_lines.append(f"- [{FACET_NAMES[facet]}]({rel_path})")

        idx_file = ch_dir / "INDEX.md"
        idx_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        count += 1

    # by_cell index
    cells = ["C0_KERNEL", "C1_CORRIDOR", "C2_METRO", "C3_RUNTIME",
             "C4_DEPLOYMENT", "C5_APPENDIX_FWD", "C6_APPENDIX_INV", "C7_CORPUS"]
    for cell in cells:
        cell_dir = proj_dir / "by_cell" / cell
        cell_dir.mkdir(parents=True, exist_ok=True)

        index_lines = [f"# {cell} — All Lenses\n"]
        for lens in LENSES:
            index_lines.append(f"\n## {LENS_NAMES[lens]} ({lens})\n")
            for facet in range(1, 5):
                src_dir = TESSERACT / lens / FACET_DIRS[facet] / cell
                if src_dir.exists():
                    files = sorted(src_dir.glob("*.md"))
                    for f in files:
                        rel = f"../../../{lens}/{FACET_DIRS[facet]}/{cell}/{f.name}"
                        index_lines.append(f"- [{f.stem}]({rel})")

        idx_file = cell_dir / "INDEX.md"
        idx_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        count += 1

    # by_facet index
    for facet in range(1, 5):
        fac_dir = proj_dir / "by_facet" / FACET_DIRS[facet]
        fac_dir.mkdir(parents=True, exist_ok=True)

        index_lines = [f"# {FACET_NAMES[facet]} — All Lenses\n"]
        for lens in LENSES:
            src_dir = TESSERACT / lens / FACET_DIRS[facet]
            index_lines.append(f"\n## {LENS_NAMES[lens]} ({lens})\n")
            if src_dir.exists():
                for cell_d in sorted(src_dir.iterdir()):
                    if cell_d.is_dir():
                        files = sorted(cell_d.glob("*.md"))
                        if files:
                            index_lines.append(f"\n### {cell_d.name}\n")
                            for f in files:
                                rel = f"../../../{lens}/{FACET_DIRS[facet]}/{cell_d.name}/{f.name}"
                                index_lines.append(f"- [{f.stem}]({rel})")

        idx_file = fac_dir / "INDEX.md"
        idx_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        count += 1

    # by_wreath index
    wreath_chapters = {
        "Su": [1, 6, 8, 10, 15, 17, 19],
        "Me": [2, 4, 9, 11, 13, 18, 20],
        "Sa": [3, 5, 7, 12, 14, 16, 21],
    }
    for wreath, chapters in wreath_chapters.items():
        w_dir = proj_dir / "by_wreath" / wreath
        w_dir.mkdir(parents=True, exist_ok=True)

        index_lines = [f"# Wreath {wreath} — Chapters on this triadic rail\n"]
        for ch_num in chapters:
            ch_id = f"Ch{ch_num:02d}"
            index_lines.append(f"\n## {ch_id}\n")
            index_lines.append(f"- [All projections](../by_chapter/{ch_id}/INDEX.md)")

        idx_file = w_dir / "INDEX.md"
        idx_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        count += 1

    return count


def build_edges() -> int:
    """Build the 32 edge bridge files."""
    edges_dir = TESSERACT / "_EDGES"
    edges_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    # Adjacent lens bridges (4)
    adjacent_pairs = [("S", "F"), ("F", "C"), ("C", "R"), ("R", "S")]
    for a, b in adjacent_pairs:
        content = (
            f"# {a}↔{b} Bridge — Adjacent Lens Edge\n\n"
            f"**Type**: Adjacent DUAL edge (φ⁻¹ = 0.618 weight)\n\n"
            f"This edge connects the {LENS_NAMES[a]} lens to the {LENS_NAMES[b]} lens.\n"
            f"Every file in {a}/ has a sibling in {b}/ — they are the same content\n"
            f"seen through a different lens. The bridge weight is the golden ratio\n"
            f"inverse φ⁻¹ ≈ 0.618, reflecting high coupling between adjacent lenses.\n\n"
            f"## Cross-References\n\n"
            f"For each cell C0-C7 and each facet 1-4, the file\n"
            f"`{a}/facet/cell/X.{a}N.md` bridges to `{b}/facet/cell/X.{b}N.md`.\n"
        )
        (edges_dir / f"{a}{b}_bridge.md").write_text(content, encoding="utf-8")
        count += 1

    # Diagonal lens bridges (2)
    diagonal_pairs = [("S", "C"), ("F", "R")]
    diag_desc = {"S": "discrete structure", "F": "phase/symmetry",
                  "C": "truth/uncertainty", "R": "recursion/compression"}
    for a, b in diagonal_pairs:
        content = (
            f"# {a}↔{b} Bridge — Diagonal Lens Edge\n\n"
            f"**Type**: Diagonal DUAL edge (φ⁻² = 0.382 weight)\n\n"
            f"This edge connects the {LENS_NAMES[a]} lens to the {LENS_NAMES[b]} lens\n"
            f"diagonally. These lenses are maximally different:\n"
            f"- {LENS_NAMES[a]}: {diag_desc[a]}\n"
            f"- {LENS_NAMES[b]}: {diag_desc[b]}\n\n"
            f"Bridge weight is φ⁻² ≈ 0.382, reflecting weaker but crucial diagonal coupling.\n"
        )
        (edges_dir / f"{a}{b}_bridge.md").write_text(content, encoding="utf-8")
        count += 1

    # Inner-outer cell bridges (4 pairs)
    cell_pairs = [
        ("C0_KERNEL", "C4_DEPLOYMENT"),
        ("C1_CORRIDOR", "C5_APPENDIX_FWD"),
        ("C2_METRO", "C6_APPENDIX_INV"),
        ("C3_RUNTIME", "C7_CORPUS"),
    ]
    for outer, inner in cell_pairs:
        content = (
            f"# {outer}↔{inner} Bridge — Inner/Outer Cell Edge\n\n"
            f"**Type**: Inner-outer cell bridge (tesseract w-axis)\n\n"
            f"This edge connects the outer cube cell {outer} to the inner cube cell {inner}.\n"
            f"- Outer cube: expansion path (chapters unfold from kernel to runtime)\n"
            f"- Inner cube: compression path (deployment → inverse appendixes → corpus seed)\n\n"
            f"The bridge represents the 1/8 lift law: content in {outer} expands what\n"
            f"content in {inner} compresses, and vice versa.\n"
        )
        (edges_dir / f"{outer}_{inner}_bridge.md").write_text(content, encoding="utf-8")
        count += 1

    return count


def build_vertices() -> int:
    """Build the 16 vertex files."""
    verts_dir = TESSERACT / "_VERTICES"
    verts_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for lens in LENSES:
        for facet in range(1, 5):
            name = f"v_{lens}{facet}"
            content = (
                f"# Vertex {lens}.{facet} — {LENS_NAMES[lens]} × {FACET_NAMES[facet]}\n\n"
                f"This vertex is the intersection of the {LENS_NAMES[lens]} lens with\n"
                f"the {FACET_NAMES[facet]} facet across all 8 cubic cells.\n\n"
                f"## Files at this vertex\n\n"
            )
            # List all files at this vertex
            facet_dir = TESSERACT / lens / FACET_DIRS[facet]
            if facet_dir.exists():
                for cell_d in sorted(facet_dir.iterdir()):
                    if cell_d.is_dir():
                        files = sorted(cell_d.glob("*.md"))
                        if files:
                            content += f"\n### {cell_d.name}\n\n"
                            for f in files:
                                content += f"- [{f.stem}](../../{lens}/{FACET_DIRS[facet]}/{cell_d.name}/{f.name})\n"

            (verts_dir / f"{name}.md").write_text(content, encoding="utf-8")
            count += 1

    return count


def main():
    print("=== TESSERACT BUILDER ===\n")

    total_projections = 0

    # 1. Decompose chapters
    print("Phase 1: Decomposing chapters...")
    ch_files = sorted(CHAPTERS_DIR.glob("Ch*.md"))
    for ch_path in ch_files:
        n = decompose_chapter(ch_path)
        if n > 0:
            print(f"  {ch_path.stem}: {n} projections")
            total_projections += n
    print(f"  Total chapter projections: {total_projections}")

    # 2. Decompose forward appendixes
    print("\nPhase 2: Decomposing forward appendixes...")
    app_count = 0
    for app_path in sorted(APPENDIX_DIR.glob("App*.md")):
        n = decompose_appendix(app_path, is_inverse=False)
        if n > 0:
            print(f"  {app_path.stem}: {n} projections")
            app_count += n
    total_projections += app_count
    print(f"  Total forward appendix projections: {app_count}")

    # 3. Decompose inverse appendixes
    print("\nPhase 3: Decomposing inverse appendixes...")
    inv_count = 0
    for inv_path in sorted(APPENDIX_DIR.glob("Inv*.md")):
        n = decompose_appendix(inv_path, is_inverse=True)
        if n > 0:
            print(f"  {inv_path.stem}: {n} projections")
            inv_count += n
    total_projections += inv_count
    print(f"  Total inverse appendix projections: {inv_count}")

    # 4. Build projection indexes
    print("\nPhase 4: Building projection indexes...")
    idx_count = build_projection_indexes()
    print(f"  {idx_count} index files")

    # 5. Build edges
    print("\nPhase 5: Building edge bridge files...")
    edge_count = build_edges()
    print(f"  {edge_count} edge files")

    # 6. Build vertices
    print("\nPhase 6: Building vertex files...")
    vert_count = build_vertices()
    print(f"  {vert_count} vertex files")

    print(f"\n=== DONE ===")
    print(f"Total projection files: {total_projections}")
    print(f"Total index files: {idx_count}")
    print(f"Total edge files: {edge_count}")
    print(f"Total vertex files: {vert_count}")
    print(f"Grand total: {total_projections + idx_count + edge_count + vert_count} files")


if __name__ == "__main__":
    main()
