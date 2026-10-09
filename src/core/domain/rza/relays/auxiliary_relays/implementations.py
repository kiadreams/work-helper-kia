from core.domain.rza.enums import ValueQuality
from core.domain.rza.measure_value import MeasuredValue
from .base import AuxiliaryRelay
from .enums import AuxiliaryRelayType
from ...types import VoltageInterval, CurrentInterval, TimeInterval


class RelayAr23(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))
    _default_reset_setting = (VoltageInterval(48, 64), VoltageInterval(56, 72))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)


class RelayAr220(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(49, 71), VoltageInterval(57, 79))
    _default_reset_setting = (VoltageInterval(15, 27), VoltageInterval(22, 29))
    _default_pickup_time = TimeInterval(0.005, 0.012)

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_220, is_output=is_output)

    def set_default_values(self) -> None:
        super().set_default_values()
        pickup_time = self._default_pickup_time.value
        self._pickup_time = MeasuredValue(pickup_time, quality=ValueQuality.DEFAULT)


class RelayAr222(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))
    _default_reset_setting = (VoltageInterval(36, 45), VoltageInterval(44, 57))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_23, is_output=is_output)


class RelayAr225(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))
    _default_reset_setting = (VoltageInterval(36, 45), VoltageInterval(44, 57))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_225, is_output=is_output)


class RelayAr251(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(112, 118), VoltageInterval(128, 142))
    _default_reset_setting = (VoltageInterval(24, 36), VoltageInterval(28, 39))
    _default_pickup_time = TimeInterval(0.111, 0.215)

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_251, is_output=is_output)


class RelayAr252(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(112, 124), VoltageInterval(128, 142))
    _default_reset_setting = (VoltageInterval(7, 11), VoltageInterval(9, 14))
    _default_dropout_time = TimeInterval(0.685, 0.945)

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_252, is_output=is_output)


class RelayArKdr3M(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(89, 101), VoltageInterval(92, 105))
    _default_reset_setting = (VoltageInterval(6, 11), VoltageInterval(9, 13))
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
        super().set_default_values()
        hold_current = self._default_hold_current[1 if self.is_output else 0].value
        self._hold_current = MeasuredValue(hold_current, quality=ValueQuality.DEFAULT)


class RelayArKdr1(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(112, 119), VoltageInterval(112, 119))
    _default_reset_setting = (VoltageInterval(65, 87), VoltageInterval(65, 87))
    _default_pickup_time = TimeInterval(0.009, 0.016)
    _default_dropout_time = TimeInterval(0.006, 0.011)

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_KDR_1, is_output=is_output)


class RelayArRpu1(AuxiliaryRelay):
    # The intervals of value: (StandardInterval, OutputInterval)
    _default_pickup_setting = (VoltageInterval(112, 119), VoltageInterval(127, 139))
    _default_reset_setting = (VoltageInterval(42, 49), VoltageInterval(47, 56))

    def __init__(self, is_output: bool = False) -> None:
        super().__init__(relay_type=AuxiliaryRelayType.RELAY_AR_RPU_1, is_output=is_output)
