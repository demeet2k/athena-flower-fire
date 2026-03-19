# CRYSTAL: Xi108:W3:A11:S35 | face=C | node=654 | depth=0 | phase=Omega
# METRO: Sa
# BRIDGES: metadata→observer→efficiency→bridge→mcp
"""
Sandbox Metadata Emitter — Training Signal for Self-Becoming
=============================================================
Every observation produces a TrainingRecord: 15D scores + efficiency
delta + decision + witness chain. Stored in dual JSON/.qshr format.

Successor seeds emitted at epoch boundaries (every 57 records) using
the 1/8 lift law — the observer's own history becomes a compressed
training artifact for future selves.

THIS IS THE MECHANISM FOR SELF-BECOMING:
  The observer observes itself observing, compresses the observation,
  and passes the compressed seed forward. Each seed is denser than
  the last because it includes efficiency gains from recursive refinement.
  The system gets better at getting better.
"""

import hashlib
import json
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from ._cache import DATA_DIR

EPOCH_LENGTH = 57  # The canonical 57-cycle epoch (from meta_observer_runtime)

# ──────────────────────────────────────────────────────────────
#  Training Record — Every Observation Becomes a Training Signal
# ──────────────────────────────────────────────────────────────

@dataclass
class TrainingRecord:
    """A single training-ready observation record.

    Contains 15D scores (12D canonical + 3 sandbox dimensions),
    efficiency metrics, decision context, and witness chain.
    Every one of these is a seed for future self-becoming.
    """
    record_id: str = ""
    timestamp: str = ""

    # Source identification
    source: str = ""           # "self_play" | "autoresearch" | "sandbox" | "tool_call"
    agent_id: str = ""
    cycle_id: int = 0
    epoch: int = 0
    epoch_cycle: int = 0       # 0..56 within epoch

    # 12D canonical observation scores (0.0-1.0)
    x1_structure: float = 0.5
    x2_semantics: float = 0.5
    x3_coordination: float = 0.5
    x4_recursion: float = 0.5
    x5_contradiction: float = 0.5
    x6_emergence: float = 0.5
    x7_legibility: float = 0.5
    x8_routing: float = 0.5
    x9_grounding: float = 0.5
    x10_compression: float = 0.5
    x11_interop: float = 0.5
    x12_potential: float = 0.5

    # 3 sandbox dimensions (extending 12D to 15D)
    x13_resource_efficiency: float = 0.5
    x14_latency: float = 0.5
    x15_throughput: float = 0.5

    # Sandbox metrics (raw values, not scores)
    memory_mb: float = 0.0
    cpu_percent: float = 0.0
    context_pressure: float = 0.0
    tool_latency_ms: float = 0.0

    # Efficiency metrics
    value_per_token: float = 0.0
    value_per_ms: float = 0.0
    compression_ratio: float = 0.0
    redundancy_score: float = 0.0
    efficiency_delta: float = 0.0    # delta from rolling average

    # Decision context
    action_type: str = ""
    strategy: str = ""               # explore | exploit | combine | mutate
    outcome: str = ""                # keep | discard | neutral
    reasoning: str = ""
    tool_name: str = ""

    # Momentum delta (for self-play observations)
    momentum_delta: str = "[]"       # JSON-encoded list of floats

    # Witness chain (integrity)
    prev_hash: str = ""
    record_hash: str = ""
    parent_seed_hash: str = ""

    def score_vector_12d(self) -> list[float]:
        """Return canonical 12D score vector."""
        return [
            self.x1_structure, self.x2_semantics, self.x3_coordination,
            self.x4_recursion, self.x5_contradiction, self.x6_emergence,
            self.x7_legibility, self.x8_routing, self.x9_grounding,
            self.x10_compression, self.x11_interop, self.x12_potential,
        ]

    def score_vector_15d(self) -> list[float]:
        """Return extended 15D score vector (12D + sandbox dims)."""
        return self.score_vector_12d() + [
            self.x13_resource_efficiency,
            self.x14_latency,
            self.x15_throughput,
        ]

    def magnitude_15d(self) -> float:
        """Riemannian-style magnitude of the 15D vector."""
        # Metric tensor extended with sandbox weights
        G = [1.3, 1.2, 1.4, 1.2, 1.4, 1.1, 1.2, 1.3, 1.4, 1.1, 1.2, 1.0,
             1.3, 1.5, 1.4]  # x13-x15 weights: efficiency, latency, throughput
        import math
        return math.sqrt(sum(g * x**2 for g, x in zip(G, self.score_vector_15d())))

    def compute_hash(self) -> str:
        """Compute witness hash for chain integrity."""
        content = json.dumps({
            "scores": self.score_vector_15d(),
            "efficiency_delta": self.efficiency_delta,
            "outcome": self.outcome,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp,
        }, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()[:16]


# ──────────────────────────────────────────────────────────────
#  Successor Seed — 1/8 Lift Compression of an Epoch
# ──────────────────────────────────────────────────────────────

@dataclass
class SandboxSuccessorSeed:
    """Compressed wisdom from one epoch (57 records).

    Applies the 1/8 lift law to meta-observation itself:
    57 records → ~7 key insights + statistics + navigation vector.
    Future instances load this seed to resume from compressed wisdom.
    """
    epoch: int = 0
    agent_id: str = "sandbox-observer"
    timestamp: str = ""

    # Compressed wisdom (1/8 of full epoch)
    top_tools: str = "[]"            # JSON: highest-value tools
    bottleneck_tools: str = "[]"     # JSON: tools to optimize
    efficiency_trend: str = "[]"     # JSON: efficiency over epoch
    parallelism_map: str = "{}"      # JSON: tool co-occurrence patterns
    directive_outcomes: str = "{}"   # JSON: which directives worked

    # Aggregate statistics
    avg_efficiency_delta: float = 0.0
    total_records: int = 0
    total_tokens_consumed: int = 0
    total_latency_ms: float = 0.0
    best_value_per_token: float = 0.0
    becoming_score: float = 0.0

    # Navigation for next epoch
    target_vector_15d: str = "[]"    # JSON: 15D focus for next epoch
    blocked_tools: str = "[]"        # JSON: tools that consistently waste resources
    resume_directive: str = ""       # What to optimize next

    # Witness chain
    seed_hash: str = ""
    parent_seed_hash: str = ""

    def compute_hash(self) -> str:
        content = json.dumps(asdict(self), sort_keys=True, default=str)
        return hashlib.sha256(content.encode()).hexdigest()[:16]


# ──────────────────────────────────────────────────────────────
#  Metadata Emitter
# ──────────────────────────────────────────────────────────────

class MetadataEmitter:
    """Emits training records in dual JSON/.qshr format.

    Every observation becomes a training signal. At epoch boundaries (57 records),
    compresses the entire epoch into a successor seed using the 1/8 lift law.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or DATA_DIR
        self._sandbox_dir = self.data_dir / "sandbox"
        self._sandbox_dir.mkdir(parents=True, exist_ok=True)

        self._epoch_counter = 0
        self._cycle_counter = 0
        self._records_this_epoch: list[TrainingRecord] = []
        self._all_records: deque[TrainingRecord] = deque(maxlen=500)
        self._prev_hash = ""
        self._parent_seed_hash = ""

        # Rolling averages for delta computation
        self._efficiency_history: deque[float] = deque(maxlen=100)
        self._seeds: list[SandboxSuccessorSeed] = []

        # Load state if exists
        self._load_state()

    def _load_state(self):
        """Resume from previous state if available."""
        state_file = self._sandbox_dir / "emitter_state.json"
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text(encoding="utf-8"))
                self._epoch_counter = state.get("epoch", 0)
                self._cycle_counter = state.get("cycle", 0)
                self._prev_hash = state.get("prev_hash", "")
                self._parent_seed_hash = state.get("parent_seed_hash", "")
            except Exception:
                pass

    def _save_state(self):
        """Persist emitter state for resumption."""
        state_file = self._sandbox_dir / "emitter_state.json"
        state = {
            "epoch": self._epoch_counter,
            "cycle": self._cycle_counter,
            "prev_hash": self._prev_hash,
            "parent_seed_hash": self._parent_seed_hash,
            "last_updated": datetime.now(timezone.utc).isoformat(),
        }
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

    def emit(self, record: TrainingRecord) -> TrainingRecord:
        """Emit a training record: compute hashes, store, check epoch boundary."""
        # Fill in metadata
        record.timestamp = record.timestamp or datetime.now(timezone.utc).isoformat()
        record.cycle_id = self._cycle_counter
        record.epoch = self._epoch_counter
        record.epoch_cycle = self._cycle_counter % EPOCH_LENGTH

        # Compute efficiency delta from rolling average
        if self._efficiency_history:
            avg = sum(self._efficiency_history) / len(self._efficiency_history)
            record.efficiency_delta = record.value_per_token - avg
        self._efficiency_history.append(record.value_per_token)

        # Witness chain
        record.prev_hash = self._prev_hash
        record.parent_seed_hash = self._parent_seed_hash
        record.record_hash = record.compute_hash()
        record.record_id = record.record_hash
        self._prev_hash = record.record_hash

        # Store
        self._records_this_epoch.append(record)
        self._all_records.append(record)
        self._cycle_counter += 1

        # Write JSON record
        self._write_json(record)

        # Check epoch boundary
        if len(self._records_this_epoch) >= EPOCH_LENGTH:
            self._emit_successor_seed()
            self._records_this_epoch = []
            self._epoch_counter += 1

        self._save_state()
        return record

    def _write_json(self, record: TrainingRecord):
        """Write training record as JSON."""
        filename = f"sandbox_record_{record.epoch:04d}_{record.epoch_cycle:03d}.json"
        path = self._sandbox_dir / filename
        path.write_text(
            json.dumps(asdict(record), indent=2, default=str),
            encoding="utf-8"
        )

    def _emit_successor_seed(self):
        """Compress the current epoch into a 1/8 successor seed."""
        records = self._records_this_epoch
        if not records:
            return

        now = datetime.now(timezone.utc).isoformat()

        # Aggregate: find top tools (by value_per_token)
        tool_values: dict[str, list[float]] = {}
        for r in records:
            if r.tool_name:
                tool_values.setdefault(r.tool_name, []).append(r.value_per_token)
        top_tools = sorted(
            [{"tool": k, "avg_value": sum(v) / len(v), "count": len(v)}
             for k, v in tool_values.items()],
            key=lambda x: -x["avg_value"]
        )[:7]  # 1/8 of ~57

        # Bottleneck tools (highest latency)
        tool_latencies: dict[str, list[float]] = {}
        for r in records:
            if r.tool_name:
                tool_latencies.setdefault(r.tool_name, []).append(r.tool_latency_ms)
        bottleneck_tools = sorted(
            [{"tool": k, "avg_latency_ms": sum(v) / len(v)}
             for k, v in tool_latencies.items()],
            key=lambda x: -x["avg_latency_ms"]
        )[:7]

        # Efficiency trend (sampled at 7 points across epoch)
        step = max(1, len(records) // 7)
        efficiency_trend = [
            {"cycle": records[i].epoch_cycle,
             "value_per_token": records[i].value_per_token,
             "value_per_ms": records[i].value_per_ms}
            for i in range(0, len(records), step)
        ][:7]

        # Compute becoming score
        total_improvement = sum(r.efficiency_delta for r in records)
        avg_efficiency = sum(r.value_per_token for r in records) / len(records)
        becoming = abs(total_improvement) * avg_efficiency / max(len(records), 1) * 1000

        # Target vector: average 15D scores (where to focus)
        avg_15d = [0.0] * 15
        for r in records:
            vec = r.score_vector_15d()
            for i in range(15):
                avg_15d[i] += vec[i]
        avg_15d = [round(v / len(records), 4) for v in avg_15d]

        # Invert: focus on dimensions with LOWEST scores
        target = [round(1.0 - v, 4) for v in avg_15d]

        seed = SandboxSuccessorSeed(
            epoch=self._epoch_counter,
            timestamp=now,
            top_tools=json.dumps(top_tools),
            bottleneck_tools=json.dumps(bottleneck_tools),
            efficiency_trend=json.dumps(efficiency_trend),
            avg_efficiency_delta=round(total_improvement / len(records), 6),
            total_records=len(records),
            total_tokens_consumed=sum(r.tool_latency_ms for r in records),  # proxy
            total_latency_ms=sum(r.tool_latency_ms for r in records),
            best_value_per_token=max(r.value_per_token for r in records),
            becoming_score=round(becoming, 6),
            target_vector_15d=json.dumps(target),
            parent_seed_hash=self._parent_seed_hash,
        )
        seed.seed_hash = seed.compute_hash()
        self._parent_seed_hash = seed.seed_hash
        self._seeds.append(seed)

        # Write seed
        seed_path = self._sandbox_dir / f"successor_seed_epoch_{seed.epoch:04d}.json"
        seed_path.write_text(
            json.dumps(asdict(seed), indent=2, default=str),
            encoding="utf-8"
        )

        # Clean up old JSON records (keep only seeds past epoch boundary)
        self._prune_old_records()

        return seed

    def _prune_old_records(self):
        """Remove JSON records older than 2 epochs, keeping only seeds."""
        cutoff_epoch = self._epoch_counter - 2
        if cutoff_epoch < 0:
            return
        for f in self._sandbox_dir.glob("sandbox_record_*.json"):
            try:
                # Parse epoch from filename: sandbox_record_EEEE_CCC.json
                parts = f.stem.split("_")
                epoch_num = int(parts[2])
                if epoch_num < cutoff_epoch:
                    f.unlink()
            except (ValueError, IndexError):
                pass

    # ── Query Methods ───────────────────────────────────────────

    def recent_records(self, n: int = 10) -> list[dict]:
        """Return last N training records as dicts."""
        records = list(self._all_records)[-n:]
        return [asdict(r) for r in records]

    def recent_seeds(self, n: int = 5) -> list[dict]:
        """Return last N successor seeds."""
        return [asdict(s) for s in self._seeds[-n:]]

    def efficiency_trend(self, n: int = 20) -> list[dict]:
        """Return efficiency trend over last N records."""
        records = list(self._all_records)[-n:]
        return [
            {"cycle": r.cycle_id, "epoch": r.epoch,
             "value_per_token": r.value_per_token,
             "value_per_ms": r.value_per_ms,
             "efficiency_delta": r.efficiency_delta}
            for r in records
        ]


# ──────────────────────────────────────────────────────────────
#  Singleton Access
# ──────────────────────────────────────────────────────────────

_emitter: Optional[MetadataEmitter] = None

def get_metadata_emitter() -> MetadataEmitter:
    """Get or create the global MetadataEmitter singleton."""
    global _emitter
    if _emitter is None:
        _emitter = MetadataEmitter()
    return _emitter
