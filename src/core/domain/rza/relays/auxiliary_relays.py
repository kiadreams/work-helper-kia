from typing import TYPE_CHECKING

from src.core.domain.rza.relays.relay_model import Relay

if TYPE_CHECKING:
    from src.core.domain.rza.enums import AuxiliaryRelayType


class AuxiliaryRelay(Relay):
    def __init__(
        self,
        relay_type: AuxiliaryRelayType,
        schematic_designation: str | None = None,
        relay_id: int | None = None,
    ) -> None:
        super().__init__(
            relay_type=relay_type, schematic_designation=schematic_designation, relay_id=relay_id
        )
