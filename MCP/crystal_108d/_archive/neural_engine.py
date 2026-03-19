"""
Backward-compatibility shim — neural_engine was replaced by geometric_forward.py.
Re-exports the compatible classes/functions under the old names.
"""
from ..geometric_forward import (
    QueryState,
    GeometricEngine as CrystalNeuralEngine,
    get_engine,
)
from ..geometric_constants import BRIDGE_WEIGHTS, bridge_key as _bridge_key

__all__ = [
    "CrystalNeuralEngine",
    "QueryState",
    "get_engine",
    "_bridge_key",
    "BRIDGE_WEIGHTS",
]
