from src.core.domain.rza.enums import AuxiliaryRelayType
from src.core.domain.rza.ralays.relay_models import Relay


class AuxiliaryRelay(Relay):
    def __init__(
        self,
        relay_type: AuxiliaryRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(relay_type=relay_type, schematic_designation=schematic_designation)
