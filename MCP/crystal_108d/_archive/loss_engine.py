"""
Backward-compatibility shim — loss_engine was folded into geometric_forward.py.
Provides stub classes/functions for any remaining imports.
"""
from __future__ import annotations


class LossEngine:
    """Stub — loss computation now handled by GeometricEngine's commit layer."""

    def compute_loss(self, predicted, actual) -> float:
        """Compute simple L2 loss between predicted and actual vectors."""
        if not predicted or not actual:
            return 0.0
        return sum((p - a) ** 2 for p, a in zip(predicted, actual)) / len(predicted)


def get_loss_engine() -> LossEngine:
    return LossEngine()


__all__ = ["LossEngine", "get_loss_engine"]
