from src.core.domain.protocol_domain import enums
from src.core.domain.protocol_domain.relay_models import Relay


class CurrentRelay(Relay):
    def __init__(
        self,
        current_relay_type: enums.CurrentRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(current_relay_type, schematic_designation)

    @property
    def pickup_current(self) -> float:
        return self._pickup_setting

    @pickup_current.setter
    def pickup_current(self, value: float) -> None:
        self._pickup_setting = value

    @property
    def reset_current(self) -> float:
        return self._reset_setting

    @reset_current.setter
    def reset_current(self, value: float) -> None:
        self._reset_setting = value

    @property
    def current_reset_ratio(self) -> float:
        return self._reset_ratio
