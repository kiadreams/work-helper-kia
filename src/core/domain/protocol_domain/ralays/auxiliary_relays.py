from src.core.domain.protocol_domain import enums
from core.domain.protocol_domain.ralays.relay_models import Relay


class AuxiliaryRelay(Relay):
    def __init__(
        self,
        auxiliary_relay_type: enums.AuxiliaryRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(auxiliary_relay_type, schematic_designation)

    @property
    def reset_ratio(self) -> float:
        return self._reset_setting
