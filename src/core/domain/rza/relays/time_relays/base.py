from typing import TYPE_CHECKING

from core.domain.rza.measure_value import MeasuredValue
from core.domain.rza.relays.relay_model import Relay
from core.domain.rza.types import VoltageInterval
from core.domain.rza.enums import ValueQuality

if TYPE_CHECKING:
    from core.domain.rza.relays.time_relays.enums import TimeRelayType


class TimeRelay(Relay):
    _default_pickup_setting = VoltageInterval(109, 119)
    _default_reset_setting = VoltageInterval(17, 27)

    def __init__(
        self,
        relay_type: TimeRelayType,
        schematic_designation: str | None = None,
        relay_id: int | None = None,
    ) -> None:
        super().__init__(
            relay_type=relay_type, schematic_designation=schematic_designation, relay_id=relay_id
        )
        self._passing_contact_time_delay: MeasuredValue | None = None
        self._pickup_time_delay: MeasuredValue | None = None
        self._reset_time_delay: MeasuredValue | None = None

        self.passing_contact_time_delays: list[float] = []
        self.pickup_time_delays: list[float] = []
        self.reset_time_delays: list[float] = []

    @property
    def passing_contact_time_delay(self) -> MeasuredValue | None:
        return self._passing_contact_time_delay

    def calculate_passing_contact_time_delay(self) -> None:
        if self.passing_contact_time_delays:
            self._passing_contact_time_delay = self._calculate_average_value(
                self.passing_contact_time_delays
            )
            self.passing_contact_time_delays.clear()

    @property
    def pickup_time_delay(self) -> MeasuredValue | None:
        return self._pickup_time_delay

    def calculate_pickup_time_delay(self) -> None:
        if self.pickup_time_delays:
            self._pickup_time_delay = self._calculate_average_value(self.pickup_time_delays)
            self.pickup_time_delays.clear()

    @property
    def reset_time_delay(self) -> MeasuredValue | None:
        return self._reset_time_delay

    def calculate_reset_time_delay(self) -> None:
        if self.reset_time_delays:
            self._reset_time_delay = self._calculate_average_value(self.reset_time_delays)
            self.reset_time_delays.clear()

    def set_default_values(self) -> None:
        if self._default_pickup_setting:
            pickup_setting = self._default_pickup_setting.value
            self._pickup_setting = MeasuredValue(pickup_setting, quality=ValueQuality.DEFAULT)
        if self._default_reset_setting:
            reset_setting = self._default_reset_setting.value
            self._reset_setting = MeasuredValue(reset_setting, quality=ValueQuality.DEFAULT)
