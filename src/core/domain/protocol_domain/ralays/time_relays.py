from src.core.domain.protocol_domain import enums
from src.core.domain.protocol_domain.relay_models import Relay


class TimeRelay(Relay):
    _passing_contact_time_delay: list[float]

    def __init__(
        self,
        time_relay_type: enums.TimeRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(time_relay_type, schematic_designation)
        self._passing_contact_time_delay = list()

    @property
    def passing_contact_time_delay(self) -> float:
        if self._passing_contact_time_delay:
            return sum(self._passing_contact_time_delay) / len(self._passing_contact_time_delay)
        return -1

    @passing_contact_time_delay.setter
    def passing_contact_time_delay(self, value: float) -> None:
        self._passing_contact_time_delay.append(value)

    def clean_passing_contact_time_delay(self) -> None:
        self._passing_contact_time_delay.clear()
