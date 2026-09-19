from src.core.domain.rza import enums
from src.core.domain.rza.ralays.relay_models import Relay


class CurrentRelay(Relay):
    def __init__(
        self,
        relay_type: enums.CurrentRelayType,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(relay_type=relay_type, schematic_designation=schematic_designation)
