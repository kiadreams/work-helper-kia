from enum import StrEnum, IntEnum, Enum


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


class AuxiliaryRelayType(RelayType):
    RELAY_AR_ANY = "РП"
    RELAY_AR_23 = "РП-23"
    RELAY_AR_222 = "РП-222"
    RELAY_AR_255 = "РП-255"


class CurrentRelayType(RelayType):
    RELAY_CR_ANY = "РТ"
    RELAY_CR_40 = "РТ-40"


class VoltageRelayType(RelayType):
    RELAY_VR_ANY = "РН"
    RELAY_VR_55 = "РН-55"
    RELAY_VR_54 = "РН-54"


class TimeRelayType(RelayType):
    RELAY_TR_ANY = "РВ"


class RelaySetType(DeviceType):
    SET_KRB_12 = "КРБ-12"
    SET_KRB_126 = "КРБ-126"


class PanelType(EnclosureType):
    PANEL_ANY = "панель"
    PANEL_EPZ_1636 = "ЭПЗ-1636"
    PANEL_PZ_5d2 = "ПЗ-5/2"
    PANEL_DFZ_201 = "ДФЗ-201"
    PANEL_DFZ_504 = "ДФЗ-504"


class CabinetType(EnclosureType):
    CABINET_ANY = "шкаф"
