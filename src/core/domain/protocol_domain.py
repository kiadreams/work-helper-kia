from dataclasses import dataclass
from enum import Enum


class RelayType(Enum):
    RELAY_RP_23 = 0


@dataclass
class Relay:
    type: RelayType


