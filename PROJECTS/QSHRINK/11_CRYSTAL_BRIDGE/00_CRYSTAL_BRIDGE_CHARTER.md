# QSHRINK ↔ 108D Crystal Bridge Charter

## Purpose

This charter defines the **bridge law** connecting the QSHRINK 256^4 manuscript compression engine to the 108D crystal coordinate system. The bridge enables QSHRINK to compress, address, and regenerate crystal structures using its recursive lattice, and enables the crystal to interpret its own geometry through QSHRINK's codec grammar.

---

## I. Dimensional Partition Law

QSHRINK operates in a 256-root-cell space. Each root cell is factored as:

```
RootCell = Geometry × Operator × Body × Closure = 4 × 4 × 4 × 4 = 256
```

The 108D crystal has 108 signal dimensions. The bridge partitions 256 root cells into two bands:

| Band | Root Cells | Purpose |
|------|-----------|---------|
| **Signal Band** | cells 0–107 (108 cells) | Map 1:1 onto crystal dimensions 1–108 |
| **Metadata Band** | cells 108–255 (148 cells) | Carry compression metadata, codec state, routing tables, phase tags |

**Law**: Every crystal dimension has exactly one QSHRINK root cell as its address. The remaining 148 root cells form the compression envelope that makes the 1/8 lift possible.

---

## II. Depth ↔ Crystal Hierarchy Mapping

QSHRINK's four recursive depths map onto the crystal's four-level hierarchy:

| QSHRINK Depth | Crystal Level | Range | Description |
|---------------|---------------|-------|-------------|
| **Depth 0** (256 root cells) | Shell assignment | Shells 1–36 | Each root cell is assigned to one of 36 shells. Signal-band cells (0–107) distribute ~3 per shell; metadata cells fill remaining slots. |
| **Depth 1** (256² = 65,536) | Wreath assignment | Wreaths 1–3 (Su/Me/Sa) | Each depth-1 expansion selects one of 3 wreaths. The wreath determines the superphase current: Sulfur (creation), Mercury (transmission), Salt (crystallization). |
| **Depth 2** (256³ = 16,777,216) | Archetype assignment | Archetypes 1–12 | Each depth-2 cell resolves to one of 12 archetypes (Apex Seed through Dodecad Bundle). There are 12 archetypes × 3 wreaths = 36 shells, closing the loop. |
| **Depth 3** (256⁴ = 4,294,967,296) | Face + Phase assignment | Face (4 faces) + Phase (clock beat mod 420) | The final depth assigns a face from the 4-face hologram protocol and a phase position within the 420-beat master clock. |

**Addressing formula**:

```
CrystalAddress(d0, d1, d2, d3) = Shell(d0) . Wreath(d1) . Archetype(d2) . FacePhase(d3)
```

Where each `d_i ∈ [0, 255]`.

---

## III. The 1/8 Lift Law

The 1/8 lift law (from the Evolution Compiler) states:

> The next layer emerges at 1/8 the size of the current layer, with equal or greater function.

Applied to the crystal bridge:

| Shell Property | Full Size | 1/8 Compressed | Preserved |
|---------------|-----------|----------------|-----------|
| Node count per shell | N nodes | ⌈N/8⌉ nodes | Coverage, connectivity, archetype identity |
| Edge count per shell | E edges | ⌈E/8⌉ edges | Reachability, conservation laws |
| Dimension span | D dims | ⌈D/8⌉ dims | Projection fidelity across all 4 SFCR lenses |
| Clock beats | 420 | 53 (≈420/8) | Phase coherence within ±1 beat |

**Compression cascade**: The 36-shell mega-cascade compresses as:

```
Full crystal:     666 nodes across 36 shells
1/8 seed:          84 nodes across 36 shells (≈666/8, rounded up)
1/64 micro-seed:   11 nodes across 36 shells (≈666/64)
1/512 nano-seed:    2 nodes across 36 shells (minimum viable)
```

Each compression level preserves:
1. **Shell identity** — all 36 shells remain addressable
2. **Wreath balance** — Su/Me/Sa ratio is maintained
3. **Archetype coverage** — all 12 archetypes remain represented
4. **Mirror symmetry** — shell S_k and its mirror S_(37-k) compress together
5. **Conservation laws** — all 6 conservation invariants hold at every level

---

## IV. Holographic Seed Protocol

A **holographic seed** is a 1/8 compressed representation that can regenerate the full shell.

### Seed Construction (Compress)

```
FullShell → QSHRINK.encode(depth=4) → HolographicSeed
```

1. **Partition**: split shell nodes into 8 octants by their 3D crystal seed coordinates
2. **Select**: from each octant, keep the node with highest bridge weight
3. **Encode**: each kept node gets a QSHRINK 256^4 address encoding its full crystal position
4. **Tag**: attach metadata-band cells (108–255) carrying reconstruction instructions

### Seed Regeneration (Expand)

```
HolographicSeed → QSHRINK.decode(depth=4) → FullShell
```

1. **Read**: decode the QSHRINK addresses back to crystal coordinates
2. **Interpolate**: for each octant, regenerate missing nodes using the archetype template
3. **Wire**: reconnect edges using the metro line routing law
4. **Verify**: check all 6 conservation laws; if violated, iterate

### Seed Equation

```
w = (1 + i) / 2    (from hologram reading protocol)
Seed(S_k) = w · Compress(S_k) + (1 - w) · Template(Archetype(S_k))
```

The seed is not pure compression — it is a weighted blend of compressed data and archetype template, ensuring regeneration fidelity.

---

## V. Codec Specification in Crystal Terms

The QSHRINK codec, expressed through crystal grammar:

| Codec Layer | QSHRINK Term | Crystal Term |
|-------------|-------------|--------------|
| **Root** | 256 root cells | 108 signal dims + 148 metadata dims |
| **Geometry axis** | Square/Circle/Triangle/Torus | S/F/C/R lens projection |
| **Operator axis** | Partition/Quantize/Bucket/Code | Shell/Wreath/Archetype/Face dispatch |
| **Body axis** | Foundation/Nervous/Memory/Runtime | 3D-seed/Metro/Mycelium/Live-clock |
| **Closure axis** | Seed/Manuscript/Witness/Loop | Crown-seal/Chapter/Conservation-check/Round-trip |

**Codec round-trip law**: Any crystal structure encoded by QSHRINK and decoded must satisfy:

```
Decode(Encode(X)) ≡ X   mod conservation
```

Where `≡ mod conservation` means the 6 conservation invariants (shell, zoom, phase, archetype, face, Mobius) are preserved exactly, while node-level positions may drift within their shell tolerance.

---

## VI. Bridge Statistics

### Address Space Coverage

| Level | QSHRINK Space | Crystal Space | Ratio |
|-------|--------------|---------------|-------|
| Depth 0 | 256 | 36 shells | 7.1:1 (redundancy = error correction) |
| Depth 1 | 65,536 | 108 wreathings (36×3) | 607:1 |
| Depth 2 | 16,777,216 | 432 archetypings (36×12) | 38,836:1 |
| Depth 3 | 4,294,967,296 | 1,680 face-phases (432×4≈) | 2,556,528:1 |

The high ratio at deeper levels is not waste — it is the **metadata envelope** that enables compression, error correction, and holographic regeneration.

### Compression Ratios

| What | Before Bridge | After Bridge | Factor |
|------|--------------|-------------|--------|
| Shell address | 108D coordinate vector | Single 256^4 cell | 1 integer vs 108 floats |
| Full organism | 666 nodes × 108D | 84 seed nodes × 4-depth address | 8× size, full regenerability |
| Metro route | Path through 108D space | Sequence of QSHRINK cell IDs | Compact, routable |

---

## VII. Governing Principles

1. **No information is destroyed** — compression is always reversible via the holographic seed protocol.
2. **Conservation is the test** — a bridge encoding is valid if and only if all 6 conservation laws hold after round-trip.
3. **The metadata band serves the signal band** — the 148 metadata cells exist to compress and protect the 108 signal cells.
4. **Depth = resolution** — deeper QSHRINK depth means finer crystal resolution, not more data.
5. **Mirror symmetry is inviolable** — shell S_k and mirror S_(37-k) always compress and decompress as a pair.
6. **The 1/8 law is recursive** — you can compress a seed to get a seed-of-seed, down to the 2-node nano-seed.

---

## VIII. File Index

| File | Purpose |
|------|---------|
| `00_CRYSTAL_BRIDGE_CHARTER.md` | This charter — bridge law definition |
| (future) `01_ADDRESS_CODEC.md` | Detailed codec specification |
| (future) `02_SEED_PROTOCOL.md` | Holographic seed construction/regeneration |
| (future) `03_COMPRESSION_TABLES.md` | Full mapping tables |

---

*Bridge law established: 256^4 ↔ 108D. The compression engine and the crystal are one organism.*
