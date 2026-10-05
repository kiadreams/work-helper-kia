import random as rnd

from src.core.domain.rza.enums import ValueQuality
from src.core.domain.rza.measure_value import MeasuredValue
from .base import AuxiliaryRelay
from .enums import AuxiliaryRelayType


class RelayAr23(AuxiliaryRelay):
    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(56, 72) if self.is_output else rnd.randint(48, 64)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)


class RelayAr220(AuxiliaryRelay):
    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_220, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(22, 29) if self.is_output else rnd.randint(15, 27)
        pickup_setting = rnd.randint(57, 79) if self.is_output else rnd.randint(49, 71)
        pickup_time = rnd.randint(5, 12) / 1000
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
        self._pickup_time = MeasuredValue(pickup_time, quality=ValueQuality.DEFAULT)


class RelayAr222(AuxiliaryRelay):
    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(44, 57) if self.is_output else rnd.randint(36, 45)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)


class RelayArKdr3M(AuxiliaryRelay):
    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_KDR_3M, is_output=is_output)
        self._hold_current: MeasuredValue | None = None
        self._dropout_time: MeasuredValue | None = None

    @property
    def hold_current(self) -> MeasuredValue | None:
        return self._hold_current

    @hold_current.setter
    def hold_current(self, value: float) -> None:
        self._hold_current = MeasuredValue(value, quality=ValueQuality.REAL)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(9, 13) if self.is_output else rnd.randint(6, 11)
        pickup_setting = rnd.randint(92, 105) if self.is_output else rnd.randint(89, 101)
        hold_current = rnd.randint(5, 11) / 1000
        dropout_time = rnd.randint(95, 140) / 1000
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
        self._hold_current = MeasuredValue(hold_current, quality=ValueQuality.DEFAULT)
        self._dropout_time = MeasuredValue(dropout_time, quality=ValueQuality.DEFAULT)
