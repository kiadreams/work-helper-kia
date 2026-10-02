from enum import Enum

from src.core.domain.rza.enums import RelayType


class AuxiliaryRelayType(RelayType):
    RELAY_AR_ANY = "рп"
    RELAY_AR_23 = "рп-23"
    RELAY_AR_222 = "рп-222"
    RELAY_AR_255 = "рп-255"


class AuxRelayDefaultValues(Enum):
    AuxiliaryRelayType.RELAY_AR_23 = {"reset_setting": 23, }
