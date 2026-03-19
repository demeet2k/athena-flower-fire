"""
Backward-compatibility shim — self_play was replaced by meta_loop_engine.py + legacy_bridge.py.
Re-exports compatible classes/functions.
"""
from __future__ import annotations
import threading
import time
import logging

_log = logging.getLogger(__name__)


class ContinuousSelfPlay:
    """Background self-play loop (stub — delegates to meta loop engine)."""

    def __init__(self, interval_seconds: int = 120):
        self.interval = interval_seconds
        self._running = False
        self._thread = None

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            try:
                from ..legacy_bridge import run_self_play
                run_self_play()
            except Exception as exc:
                _log.debug("Self-play cycle error: %s", exc)
            time.sleep(self.interval)


def run_swarm_self_play(rounds: int = 5, parallel: int = 3) -> str:
    """Run a swarm of parallel self-play rounds."""
    try:
        from ..legacy_bridge import run_self_play
        results = []
        for i in range(rounds):
            r = run_self_play()
            results.append(f"Round {i+1}: {r[:100] if isinstance(r, str) else 'ok'}")
        return "\n".join(results)
    except Exception as exc:
        return f"Swarm self-play error: {exc}"


__all__ = ["ContinuousSelfPlay", "run_swarm_self_play"]
