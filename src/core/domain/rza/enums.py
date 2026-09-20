from enum import IntEnum, Enum


class ValueQuality(IntEnum):
    DEFAULT = 0
    REAL = 1
    SETPOINT = 2


class DeviceType(Enum):
    pass


class EnclosureType(DeviceType):
    pass


class RelayType(DeviceType):
    pass


class AssemblyType(DeviceType):
    pass


class AuxiliaryRelayType(RelayType):
    RELAY_AR_ANY = "рп"
    RELAY_AR_23 = "рп-23"
    RELAY_AR_222 = "рп-222"
    RELAY_AR_255 = "рп-255"


class CurrentRelayType(RelayType):
    RELAY_CR_ANY = "рт"
    RELAY_CR_40 = "рт-40"


class VoltageRelayType(RelayType):
    RELAY_VR_ANY = "рн"
    RELAY_VR_55 = "рн-55"
    RELAY_VR_54 = "рн-54"


class TimeRelayType(RelayType):
    RELAY_TR_ANY = "рв"


class DistanceRelayType(RelayType):
    RELAY_DR_ANY = "др"


class PanelType(EnclosureType):
    PANEL_ANY = "панель"
    PANEL_EPZ_1636 = "эпз-1636"
    PANEL_PZ_5d2 = "пз-5/2"
    PANEL_DFZ_201 = "дфз-201"
    PANEL_DFZ_504 = "дфз-504"


class CabinetType(EnclosureType):
    CABINET_ANY = "шкаф"


class RelaySetType(AssemblyType):
    RELAY_SET_ANY = "комплект реле"
    RELAY_SET_KRB_12 = "крб-12"
    RELAY_SET_KRB_126 = "крб-126"


class MpTerminalType(AssemblyType):
    MP_TERMINAL_ANY = "терминал"
