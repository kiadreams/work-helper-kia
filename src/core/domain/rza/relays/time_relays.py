from typing import TYPE_CHECKING

from src.core.domain.rza.measure_value import MeasuredValue
from src.core.domain.rza.relays.relay_model import Relay

if TYPE_CHECKING:
    from src.core.domain.rza.enums import TimeRelayType


class TimeRelay(Relay):
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
        self.passing_contact_time_delays: list[float] = []
        self._pickup_time_delay: MeasuredValue | None = None
        self._reset_time_delay: MeasuredValue | None = None

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
