import random as rnd

from core.domain.rza.enums import ValueQuality
from core.domain.rza.measure_value import MeasuredValue
from core.domain.rza.relays.auxiliary_relays.enums import AuxiliaryRelayType
from src.core.domain.rza.relays import AuxiliaryRelay


class RelayAr23(AuxiliaryRelay):
    def __init__(self, is_output: bool) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(56, 72) if self.is_output else rnd.randint(48, 64)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)


class RelayAr222(AuxiliaryRelay):
    def __init__(self, is_output: bool) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(44, 57) if self.is_output else rnd.randint(36, 45)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
