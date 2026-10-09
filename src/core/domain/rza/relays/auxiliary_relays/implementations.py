from typing import TYPE_CHECKING
import random as rnd

from core.domain.rza.enums import ValueQuality
from core.domain.rza.measure_value import MeasuredValue
from .base import AuxiliaryRelay
from .enums import AuxiliaryRelayType

if TYPE_CHECKING:
    from ...types import VoltageInterval, CurrentInterval, TimeInterval


class RelayAr23(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_reset_setting = (VoltageInterval(48, 64), VoltageInterval(56, 72))
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(56, 72) if self.is_output else rnd.randint(48, 64)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)


class RelayAr220(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_reset_setting = (VoltageInterval(15, 27), VoltageInterval(22, 29))
    _default_pickup_setting = (VoltageInterval(49, 71), VoltageInterval(57, 79))

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
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_reset_setting = (VoltageInterval(36, 45), VoltageInterval(44, 57))
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)

    def set_default_values(self) -> None:
        reset_setting = rnd.randint(44, 57) if self.is_output else rnd.randint(36, 45)
        pickup_setting = rnd.randint(128, 142) if self.is_output else rnd.randint(102, 114)
        self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)


class RelayArKdr3M(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_reset_setting = (VoltageInterval(6, 11), VoltageInterval(9, 13))
    _default_pickup_setting = (VoltageInterval(89, 101), VoltageInterval(92, 105))
    _default_hold_current = (CurrentInterval(0.005, 0.011), CurrentInterval(0.007, 0.012))
    _default_dropout_time = TimeInterval(0.095, 0.140)

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
        reset_setting = self._df_rst_setting_output if self.is_output else self._df_rst_setting
        pickup_setting = self._df_pcp_setting_output if self.is_output else self._df_pcp_setting
        hold_current = rnd.randint(5, 11) / 1000
        dropout_time = rnd.randint(95, 140) / 1000
        self._reset_setting = MeasuredValue(
            self.random_measure(reset_setting), quality=ValueQuality.DEFAULT
        )
        self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
        self._hold_current = MeasuredValue(hold_current, quality=ValueQuality.DEFAULT)
        self._dropout_time = MeasuredValue(dropout_time, quality=ValueQuality.DEFAULT)
