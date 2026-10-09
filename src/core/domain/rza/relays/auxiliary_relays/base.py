from typing import TYPE_CHECKING

from core.domain.rza.enums import ValueQuality
from core.domain.rza.measure_value import MeasuredValue
from core.domain.rza.relays.relay_model import Relay
from ...types import VoltageInterval, TimeInterval

if TYPE_CHECKING:
    from .enums import AuxiliaryRelayType


class AuxiliaryRelay(Relay):
    _default_reset_setting = (VoltageInterval(48, 64), VoltageInterval(56, 72))
    _default_pickup_setting = (VoltageInterval(102, 114), VoltageInterval(128, 142))
    _default_pickup_time = TimeInterval(0.010, 0.015)
    _default_dropout_time = TimeInterval(0.008, 0.011)

    def __init__(
        self,
        relay_type: AuxiliaryRelayType,
        schematic_designation: str | None = None,
        relay_id: int | None = None,
        is_output: bool = False,
    ) -> None:
        super().__init__(
            relay_type=relay_type, schematic_designation=schematic_designation, relay_id=relay_id
        )
        self.is_output = is_output
        self._pickup_time: MeasuredValue | None = None
        self._dropout_time: MeasuredValue | None = None

    @property
    def pickup_time(self) -> MeasuredValue | None:
        return self._pickup_time

    @pickup_time.setter
    def pickup_time(self, value: float) -> None:
        self._pickup_time = MeasuredValue(value=value, quality=ValueQuality.REAL)

    @property
    def dropout_time(self) -> MeasuredValue | None:
        return self._dropout_time

    @dropout_time.setter
    def dropout_time(self, value: float) -> None:
        self._dropout_time = MeasuredValue(value=value, quality=ValueQuality.REAL)

    def set_default_values(self) -> None:
        if self._default_pickup_setting:
            pickup_setting = self._default_pickup_setting[1 if self.is_output else 0].value
            self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
        if self._default_reset_setting:
            reset_setting = self._default_reset_setting[1 if self.is_output else 0].value
            self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
        if self._default_pickup_time:
            pickup_time = self._default_pickup_time.value
            self._pickup_time = MeasuredValue(pickup_time, quality=ValueQuality.DEFAULT)
        if self._default_dropout_time:
            dropout_time = self._default_dropout_time.value
            self._dropout_time = MeasuredValue(dropout_time, quality=ValueQuality.DEFAULT)
