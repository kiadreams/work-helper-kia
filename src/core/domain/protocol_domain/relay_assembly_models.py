from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.domain.protocol_domain.relay_models import Relay


class RelayAssembly:
    relays: list[Relay]

    def __init__(
        self,
        schematic_designation: str | None = None,
    ):
        self.schematic_designation = schematic_designation

    def add_relay(self, relay: Relay) -> None:
        self.relays.append(relay)

    def remove_relay(self, relay: Relay) -> None:
        self.relays.remove(relay)
