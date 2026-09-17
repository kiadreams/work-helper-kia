from enum import Enum


class PCRelay(Enum):
    pass


class AuxiliaryRelayType(PCRelay):
    RELAY_AR_ANY = "РП"
    RELAY_AR_23 = "РП-23"
    RELAY_AR_222 = "РП-222"
    RELAY_AR_255 = "РП-255"


class CurrentRelayType(PCRelay):
    RELAY_CR_ANY = "РТ"
    RELAY_CR_40 = "РТ-40"


class VoltageRelayType(PCRelay):
    RELAY_VR_ANY = "РН"
    RELAY_VR_55 = "РН-55"
    RELAY_VR_54 = "РН-54"


class TimeRelayType(PCRelay):
    RELAY_TR_ANY = "РВ"
