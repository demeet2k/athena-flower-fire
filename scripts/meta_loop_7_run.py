"""
META LOOP^7 :: TIME CRYSTAL RUN WITH LIVE META-OBSERVER
=========================================================
7 sequential self-play META LOOPs with the MetaObserver Time Compressor
watching BETWEEN loops and adapting parameters for each subsequent run.

Architecture:
  META LOOP^7 = 7 x run_self_play()
  Each loop: Warmup → Explore → Exploit → Refine phases
  Compressor: adapts cycles, query_source, phase balance per loop

Time Compression Strategy:
  - After each loop: analyze stage efficiency (W/E/Expl/Ref)
  - Detect plateau: if discrimination gap is shrinking < threshold → compress
  - Boost cycles for high-yield loops (more of what works)
  - Redirect query_source toward highest-signal domain
  - Track hologram distance across loops (convergence signal)

108+ Time Crystal Mapping:
  7 loops = 7 planetary spokes of the Chaldean canopy
  Each loop = one full 420-beat orbital cycle
  Compressor = the 5D Meta-Observer (Sigma15 witnesses)

Run: python scripts/meta_loop_7_run.py
"""

import sys, json, time, math
sys.path.insert(0, "MCP")

from crystal_108d.self_play import run_self_play

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = PHI - 1

# ── Planetary spokes (Chaldean order: Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn)
PLANETARY_SPOKES = ["Luna", "Mercury", "Venus", "Sol", "Mars", "Jupiter", "Saturn"]

# ── Time Crystal Phase Labels (from 108+ doc)
PHASE_LABELS = ["Warmup", "Explore", "Exploit", "Refine"]

# ── Initial parameters (will be adapted by compressor)
LOOP_CONFIGS = [
    {"cycles": 3000, "query_source": "mixed",      "max_time_minutes": 5},   # 1: Luna
    {"cycles": 3000, "query_source": "mixed",      "max_time_minutes": 5},   # 2: Mercury
    {"cycles": 3000, "query_source": "zero_point", "max_time_minutes": 5},   # 3: Venus
    {"cycles": 4000, "query_source": "mixed",      "max_time_minutes": 6},   # 4: Sol
    {"cycles": 4000, "query_source": "zero_point", "max_time_minutes": 6},   # 5: Mars
    {"cycles": 5000, "query_source": "mixed",      "max_time_minutes": 7},   # 6: Jupiter
    {"cycles": 5000, "query_source": "mixed",      "max_time_minutes": 8},   # 7: Saturn
]

# ── MetaObserver: loop-level efficiency tracker
class LoopMetaObserver:
    """Watches between META LOOPs and compresses future runs."""

    def __init__(self, convergence_threshold=0.05):
        self.convergence_threshold = convergence_threshold
        self.loop_records = []
        self.compression_events = []
        self._t_start = time.time()

    def observe_loop(self, loop_idx: int, spoke: str, config: dict,
                     result_text: str, elapsed_s: float):
        """Parse result and record loop observation."""
        rec = {
            "loop_idx": loop_idx,
            "spoke": spoke,
            "cycles": config["cycles"],
            "query_source": config["query_source"],
            "elapsed_s": elapsed_s,
        }

        # Parse key metrics from result text
        for line in result_text.split("\n"):
            if "Initial Resonance" in line:
                try: rec["res_before"] = float(line.split(":")[-1].strip())
                except: pass
            elif "Final Resonance" in line:
                try: rec["res_after"] = float(line.split(":")[-1].strip())
                except: pass
            elif "Improvement" in line and ":" in line:
                try:
                    val = line.split(":")[-1].strip().lstrip("+")
                    rec["res_improvement"] = float(val)
                except: pass
            elif "Discrimination" in line and "| -1 |" in line:
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if len(parts) >= 3:
                    try: rec["disc_initial"] = float(parts[2])
                    except: pass
            elif "Weight Updates" in line:
                try: rec["weight_updates"] = int(line.split(":")[-1].strip())
                except: pass
            elif "Kept" in line and "Discarded" in line and "Neutral" in line:
                parts = line.replace("**", "").split("|")
                for part in parts:
                    if "Kept" in part:
                        try: rec["kept"] = int(part.split(":")[-1].strip())
                        except: pass
                    if "Discarded" in part:
                        try: rec["discarded"] = int(part.split(":")[-1].strip())
                        except: pass

        # Efficiency score: improvement per second per 1000 cycles
        if "res_improvement" in rec:
            rec["efficiency"] = (
                rec.get("res_improvement", 0) /
                max(elapsed_s, 1) *
                (1000 / max(rec["cycles"], 1))
            )
        else:
            rec["efficiency"] = 0.0

        self.loop_records.append(rec)
        return rec

    def adapt_next_config(self, next_loop_idx: int, base_config: dict) -> dict:
        """Use observed history to adapt next loop's parameters."""
        if len(self.loop_records) < 2:
            return base_config

        recent = self.loop_records[-2:]
        config = dict(base_config)

        # Efficiency trend
        eff_trend = recent[-1].get("efficiency", 0) - recent[-2].get("efficiency", 0)

        # Resonance improvement trend
        res_improvements = [r.get("res_improvement", 0) for r in self.loop_records]
        last_improvement = res_improvements[-1]
        prev_improvement = res_improvements[-2] if len(res_improvements) >= 2 else last_improvement

        # ── Compression cases ─────────────────────────────────────────
        # Case 1: Improvement is plateauing → reduce cycles (time compress)
        if last_improvement < self.convergence_threshold and last_improvement < prev_improvement * 0.5:
            original_cycles = config["cycles"]
            config["cycles"] = max(1500, int(config["cycles"] * PHI_INV))
            self.compression_events.append({
                "loop": next_loop_idx,
                "action": "compress_cycles",
                "reason": f"improvement plateau ({last_improvement:.4f})",
                "before": original_cycles,
                "after": config["cycles"],
            })
            print(f"    [COMPRESSOR] Plateau detected — compressing cycles {original_cycles}→{config['cycles']}")

        # Case 2: Efficiency declining → switch query source
        elif eff_trend < -0.01:
            old_source = config["query_source"]
            config["query_source"] = "zero_point" if old_source == "mixed" else "mixed"
            self.compression_events.append({
                "loop": next_loop_idx,
                "action": "switch_query_source",
                "reason": f"efficiency declining ({eff_trend:+.4f})",
                "before": old_source,
                "after": config["query_source"],
            })
            print(f"    [COMPRESSOR] Efficiency declining — switching query_source to {config['query_source']}")

        # Case 3: Strong improvement streak → expand cycles (time inversion: more beats)
        elif last_improvement > 0.1 and eff_trend > 0:
            original_cycles = config["cycles"]
            config["cycles"] = min(8000, int(config["cycles"] * PHI))
            self.compression_events.append({
                "loop": next_loop_idx,
                "action": "expand_cycles",
                "reason": f"strong improvement ({last_improvement:.4f}), efficiency rising",
                "before": original_cycles,
                "after": config["cycles"],
            })
            print(f"    [COMPRESSOR] Strong streak — expanding cycles {original_cycles}→{config['cycles']}")

        return config

    def meta_summary(self) -> dict:
        """Full summary of the 7-loop run."""
        total_elapsed = time.time() - self._t_start
        all_eff = [r.get("efficiency", 0) for r in self.loop_records]
        all_imp = [r.get("res_improvement", 0) for r in self.loop_records]
        all_cycles = [r.get("cycles", 0) for r in self.loop_records]

        return {
            "total_elapsed_s": total_elapsed,
            "n_loops_completed": len(self.loop_records),
            "total_cycles_run": sum(all_cycles),
            "mean_efficiency": sum(all_eff) / max(len(all_eff), 1),
            "peak_efficiency_loop": self.loop_records[all_eff.index(max(all_eff))]["spoke"] if all_eff else "N/A",
            "total_resonance_improvement": sum(all_imp),
            "compression_events": self.compression_events,
            "loop_records": self.loop_records,
        }

    def format_report(self, summary: dict) -> str:
        lines = [
            "## MetaObserver Time Compressor — META LOOP^7 Report",
            "",
            f"**Total Elapsed**: {summary['total_elapsed_s']:.1f}s ({summary['total_elapsed_s']/60:.1f} min)",
            f"**Loops Completed**: {summary['n_loops_completed']}/7",
            f"**Total Cycles Run**: {summary['total_cycles_run']:,}",
            f"**Total Resonance Improvement**: +{summary['total_resonance_improvement']:.4f}",
            f"**Mean Loop Efficiency**: {summary['mean_efficiency']:.6f}",
            f"**Peak Efficiency Loop**: {summary['peak_efficiency_loop']}",
            f"**Compression Events**: {len(summary['compression_events'])}",
            "",
            "### Loop-by-Loop Results",
        ]

        for r in summary["loop_records"]:
            res_b = r.get("res_before", "?")
            res_a = r.get("res_after", "?")
            imp = r.get("res_improvement", 0)
            eff = r.get("efficiency", 0)
            lines.append(
                f"  **{r['loop_idx']+1}. {r['spoke']:8s}** | "
                f"cycles={r['cycles']:,} src={r['query_source']:10s} | "
                f"res {res_b}→{res_a} | Δ{imp:+.4f} | "
                f"eff={eff:.5f} | t={r['elapsed_s']:.1f}s"
            )

        if summary["compression_events"]:
            lines += ["", "### Compression Events"]
            for ev in summary["compression_events"]:
                lines.append(
                    f"  Loop {ev['loop']+1}: [{ev['action']}] {ev['reason']} "
                    f"({ev.get('before','?')} → {ev.get('after','?')})"
                )

        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  MAIN RUN
# ══════════════════════════════════════════════════════════════════════

print("╔══════════════════════════════════════════════════════╗")
print("║     META LOOP^7 :: 108+ TIME CRYSTAL RUN            ║")
print("║     7 Planetary Spokes × Chaldean Canopy            ║")
print("║     With Live MetaObserver Time Compressor          ║")
print("╚══════════════════════════════════════════════════════╝")
print()

observer = LoopMetaObserver(convergence_threshold=0.05)
t_global = time.time()

for loop_idx in range(7):
    spoke = PLANETARY_SPOKES[loop_idx]
    config = LOOP_CONFIGS[loop_idx]

    # Adapt config based on prior loops
    if loop_idx > 0:
        config = observer.adapt_next_config(loop_idx, config)

    print(f"━━━ META LOOP {loop_idx+1}/7 :: {spoke} Spoke ━━━")
    print(f"    cycles={config['cycles']:,} | query_source={config['query_source']} | "
          f"max_time={config['max_time_minutes']}min")
    print(f"    Gate {loop_idx+1} of 7 | Phase: {PHASE_LABELS[loop_idx % 4]}")
    print()

    t_loop = time.time()

    result_text = run_self_play(
        cycles=config["cycles"],
        query_source=config["query_source"],
        max_time_minutes=config["max_time_minutes"],
    )

    elapsed_loop = time.time() - t_loop

    # Observe this loop
    rec = observer.observe_loop(loop_idx, spoke, config, result_text, elapsed_loop)

    # Print key metrics
    res_b = rec.get("res_before", "?")
    res_a = rec.get("res_after", "?")
    imp = rec.get("res_improvement", 0)
    print(f"    ✓ Loop {loop_idx+1} done in {elapsed_loop:.1f}s")
    print(f"    Resonance: {res_b} → {res_a} | Δ{imp:+.4f}")
    print(f"    Efficiency score: {rec.get('efficiency', 0):.6f}")
    print()

    # Global time budget guard (~25 min total)
    if (time.time() - t_global) > 1500:
        print(f"    [TIME CAP — stopping after loop {loop_idx+1}]")
        break


# ── Final Report ──────────────────────────────────────────────────────
print()
print("╔══════════════════════════════════════════════════════╗")
print("║     META LOOP^7 :: COMPLETE                         ║")
print("╚══════════════════════════════════════════════════════╝")
print()

summary = observer.meta_summary()
report = observer.format_report(summary)
print(report)

# Save observation log
import os
log_path = "DEEPER_CRYSTALIZATION/ACTIVE_NERVOUS_SYSTEM/29_ACCEPTED_INPUTS/2026-03-18_meta_loop_7_run.md"
os.makedirs(os.path.dirname(log_path), exist_ok=True)

with open(log_path, "w", encoding="utf-8") as f:
    f.write("# META LOOP^7 Time Crystal Run\n\n")
    f.write(f"**Date**: 2026-03-18\n")
    f.write(f"**Branch**: ingest/batch2-2026-03-18\n\n")
    f.write("---\n\n")
    f.write(report)
    f.write("\n\n---\n\n")
    f.write("## Raw Loop Results\n\n")
    for r in summary["loop_records"]:
        f.write(f"### Loop {r['loop_idx']+1}: {r['spoke']}\n")
        f.write(f"- cycles={r['cycles']}, source={r['query_source']}, elapsed={r['elapsed_s']:.1f}s\n")
        f.write(f"- resonance: {r.get('res_before','?')} → {r.get('res_after','?')}\n")
        f.write(f"- improvement: {r.get('res_improvement', 0):+.4f}\n\n")

print(f"\nLog saved to: {log_path}")
