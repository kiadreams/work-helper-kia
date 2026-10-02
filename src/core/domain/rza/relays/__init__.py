from .current_relays import CurrentRelay
from .time_relays import TimeRelay
from .voltage_relays import VoltageRelay
from core.domain.rza.relays.auxiliary_relays.base import AuxiliaryRelay
from .relay_model import Relay

__all__ = [
    "Relay",
    "CurrentRelay",
    "TimeRelay",
    "VoltageRelay",
    "AuxiliaryRelay",
]
