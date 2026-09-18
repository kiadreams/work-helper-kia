from src.core.domain.protocol_domain import enums
from core.domain.protocol_domain.ralays.relay_models import Relay


class VoltageRelay(Relay):
    def __init__(
        self,
        voltage_relay_type: enums.VoltageRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(voltage_relay_type, schematic_designation)

    @property
    def pickup_voltage(self) -> float:
        return self._pickup_setting

    @pickup_voltage.setter
    def pickup_voltage(self, value: float) -> None:
        self._pickup_setting = value

    @property
    def reset_voltage(self) -> float:
        return self._reset_setting

    @reset_voltage.setter
    def reset_voltage(self, value: float) -> None:
        self._reset_setting = value

    @property
    def voltage_reset_ratio(self) -> float:
        return self._reset_ratio
